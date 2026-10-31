#!/usr/bin/env python3
"""Read-only, standard-library access to the Girsu source graph.

No database, network, builder, identity closure or old workspace is required.
Default accessors share one source-preferred reading. Explicit evidence accessors
retain byte-exact originals and historical graphs; no global identity is inferred.
"""
import argparse
import base64
import copy
from collections import OrderedDict
import gzip
import hashlib
import json
from pathlib import Path
import re
import sys

SOURCE_DATASETS = frozenset(('records', 'sources', 'originals', 'catalogue', 'availability', 'aliases', 'admission', 'default_records'))
GRAPH_DATASETS = frozenset(('connected', 'shared_hubs', 'shared_incidences', 'accounting_accounts',
    'accounting_linear_systems', 'accounting_conclusions', 'temporal', 'alternatives',
    'alternative_connections', 'count_bounds', 'documentary_bridges', 'cross_record_citations', 'unresolved_documentary_citations'))

def resolve_pointer(value, pointer):
    """Resolve an RFC6901 JSON pointer; do not evaluate code or a filesystem path."""
    if pointer == '':
        return value
    if not isinstance(pointer, str) or not pointer.startswith('/'):
        raise ValueError('JSON pointer must be empty or begin with /')
    for piece in pointer[1:].split('/'):
        if re.search(r'~(?![01])', piece):
            raise ValueError('Invalid JSON pointer escape')
        piece = piece.replace('~1', '/').replace('~0', '~')
        if isinstance(value, list):
            if not re.fullmatch(r'0|[1-9][0-9]*', piece):
                raise ValueError('Invalid JSON array index')
            value = value[int(piece)]
        elif isinstance(value, dict):
            value = value[piece]
        else:
            raise KeyError(pointer)
    return value

class Graph:
    def __init__(self, root=None):
        self.root = Path(root or Path(__file__).parent).resolve()
        self._indexes = {}
        self._parts = OrderedDict()
        self._file_manifest = None
        self._defaults = OrderedDict()

    def _path(self, relative):
        p = (self.root / relative).resolve()
        if not p.is_relative_to(self.root):
            raise ValueError('Path escapes repository')
        return p

    def _json(self, relative):
        p = self._path(relative)
        with (gzip.open(p, 'rt', encoding='utf-8') if p.suffix == '.gz' else p.open(encoding='utf-8')) as f:
            return json.load(f)

    def _verify_manifest_file(self, relative):
        # The published manifest protects source indexes as well as payloads.
        if self._file_manifest is None:
            manifest = self._path('MANIFEST.json')
            if not manifest.exists():
                raise ValueError('Published MANIFEST.json is required')
            self._file_manifest = {v['path']: v for v in self._json('MANIFEST.json')['files']}
        info = self._file_manifest.get(relative)
        if info is None:
            raise ValueError('File absent from published manifest: ' + relative)
        raw = self._path(relative).read_bytes()
        if len(raw) != info['bytes'] or hashlib.sha256(raw).hexdigest() != info['sha256']:
            raise ValueError('Manifest mismatch: ' + relative)

    @staticmethod
    def _binding(row):
        binding = row.get('binding', row.get('context', {}))
        target = row.get('target', row.get('key', {}))
        return (row.get('source_id', binding.get('source_id')),
                row.get('version_hash', row.get('record_hash', row.get('record_version',
                    binding.get('version_hash', binding.get('record_hash', target.get('version_hash')))))))

    def _index(self, dataset):
        if dataset not in SOURCE_DATASETS and dataset not in GRAPH_DATASETS:
            raise ValueError('Dataset is not allowlisted')
        if dataset not in self._indexes:
            if dataset in SOURCE_DATASETS:
                relative = 'data/' + dataset + '/index.json'
                self._verify_manifest_file(relative)
                idx = self._json(relative)
            else:
                prefix = 'data/graph/' + dataset + '/'
                self._verify_manifest_file(prefix + 'manifest.json')
                manifest = self._json(prefix + 'manifest.json')
                index_info = manifest['index']
                raw = self._path(prefix + index_info['path']).read_bytes()
                if hashlib.sha256(raw).hexdigest() != index_info['sha256']:
                    raise ValueError('Graph index hash mismatch')
                idx = {'rows': self._json(prefix + index_info['path']), 'manifest': manifest}
            self._indexes[dataset] = idx
        return self._indexes[dataset]

    def _part(self, path, expected_hash):
        key = (path, expected_hash)
        if key not in self._parts:
            raw = self._path(path).read_bytes()
            if hashlib.sha256(raw).hexdigest() != expected_hash:
                raise ValueError('Partition hash mismatch: ' + path)
            self._parts[key] = [json.loads(line) for line in gzip.decompress(raw).splitlines()]
            while len(self._parts) > 2:
                self._parts.popitem(last=False)
        else:
            self._parts.move_to_end(key)
        return self._parts[key]

    def rows(self, dataset, source_id=None, version_hash=None):
        """Low-level dataset stream; default_records carry explicit population flags; other datasets preserve evidence."""
        idx = self._index(dataset)
        if dataset in SOURCE_DATASETS:
            if source_id is None:
                for part in idx['files']:
                    for row in self._part(part['path'], part['sha256']):
                        if version_hash is None or row.get('version_hash') == version_hash:
                            yield copy.deepcopy(row)
            else:
                for part_no, line in idx['sources'].get(source_id, []):
                    part = idx['files'][part_no]
                    row = self._part(part['path'], part['sha256'])[line]
                    if row.get('source_id') != source_id:
                        raise ValueError('Source index binding mismatch')
                    if version_hash is None or row.get('version_hash') == version_hash:
                        yield copy.deepcopy(row)
        else:
            parts = {p['path']: p for p in idx['manifest']['parts']}
            for entry in idx['rows']:
                if source_id is not None and entry.get('source_id') != source_id:
                    continue
                if version_hash is not None and entry.get('version_hash') != version_hash:
                    continue
                part = parts[entry['part']]
                row = self._part('data/graph/' + dataset + '/' + entry['part'], part['sha256'])[entry['line']]
                actual_source, actual_version = self._binding(row)
                if entry.get('source_id') is not None and entry['source_id'] != actual_source:
                    raise ValueError('Graph source index binding mismatch')
                if entry.get('version_hash') is not None and entry['version_hash'] != actual_version:
                    raise ValueError('Graph version index binding mismatch')
                yield copy.deepcopy(row)

    def resolve_proof(self, proof):
        """Resolve an accounting proof's upstream artifact/hash/one-based line/pointer."""
        mapping = {'accounts.jsonl.gz': 'accounting_accounts', 'linear_systems.jsonl.gz': 'accounting_linear_systems'}
        dataset = mapping.get(proof.get('artifact'))
        if dataset is None:
            raise ValueError('Proof artifact is not allowlisted')
        idx = self._index(dataset)
        if not any(s['sha256'] == proof['artifact_sha256'] for s in idx['manifest']['sources']):
            raise ValueError('Upstream proof artifact hash mismatch')
        original_line = proof['jsonl_line'] - 1
        entry = next((e for e in idx['rows'] if e['original_line'] == original_line), None)
        if entry is None:
            raise KeyError(original_line)
        part = next(p for p in idx['manifest']['parts'] if p['path'] == entry['part'])
        value = self._part('data/graph/' + dataset + '/' + entry['part'], part['sha256'])[entry['line']]
        return resolve_pointer(value, proof.get('json_pointer', ''))

    def verify(self):
        """Verify the entire published file manifest, without writing anything."""
        manifest = self._json('MANIFEST.json')
        for item in manifest['files']:
            p = self._path(item['path'])
            with p.open('rb') as f:
                digest = hashlib.file_digest(f, 'sha256').hexdigest()
            if p.stat().st_size != item['bytes'] or digest != item['sha256']:
                raise ValueError('Manifest mismatch: ' + item['path'])
        return {'files_verified': len(manifest['files']), 'status': 'passed'}

    def source(self, source_id):
        """Registry/ledger metadata, not a research reading or acceptance grant."""
        for dataset in ('sources', 'catalogue'):
            row = next(self.rows(dataset, source_id), None)
            if row is not None:
                return copy.deepcopy(row)
        raise KeyError(source_id)

    def record_envelope(self, source_id, current_only=True):
        row = next(self.rows('records', source_id), None)
        if row is None or (current_only and not row['current']):
            raise KeyError('No selected current record' if current_only else 'No selected record')
        return row

    def evidence_record_bytes(self, source_id, current_only=True):
        """Advanced evidence: byte-exact stored record, never preferences."""
        row = self.record_envelope(source_id, current_only)
        raw = row['record_json'].encode('utf-8')
        if hashlib.sha256(raw).hexdigest() != row['version_hash']:
            raise ValueError('Evidence record hash mismatch')
        return raw

    def evidence_record(self, source_id, current_only=True):
        return json.loads(self.evidence_record_bytes(source_id, current_only))

    def original(self, source_id, kind='registered'):
        """Advanced evidence: original source bytes; not a research default."""
        for row in self.rows('originals', source_id):
            if row['kind'] == kind:
                raw = base64.b64decode(row['original_bytes_b64'], validate=True)
                if hashlib.sha256(raw).hexdigest() != row['sha256']:
                    raise ValueError('Original byte hash mismatch')
                return raw
        raise KeyError((source_id, kind))

    evidence_original = original

    def _source_original(self, record):
        """Resolve the exact witness cited by this record, not a newer registration."""
        document = record.get('document', {})
        binding = document.get('source_version', {})
        for row in self.rows('originals', document.get('source_id')):
            if row.get('sha256') == binding.get('sha256'):
                raw = base64.b64decode(row['original_bytes_b64'], validate=True)
                if hashlib.sha256(raw).hexdigest() != binding['sha256'] or len(raw) != binding['bytes']:
                    raise ValueError('Record source witness hash/length mismatch')
                return raw
        raise KeyError('Exact record-cited source witness unavailable')

    @staticmethod
    def _set_pointer(record, pointer, value):
        if not isinstance(pointer, str) or not pointer.startswith('/') or re.search(r'~(?![01])', pointer):
            raise ValueError('Invalid assignment JSON pointer')
        parent_pointer, raw_key = pointer.rsplit('/', 1)
        parent = resolve_pointer(record, parent_pointer)
        key = raw_key.replace('~1', '/').replace('~0', '~')
        if isinstance(parent, list):
            if not re.fullmatch(r'0|[1-9][0-9]*', key):
                raise ValueError('Invalid assignment array index')
            parent[int(key)] = copy.deepcopy(value)
        elif isinstance(parent, dict):
            if key not in parent:
                raise KeyError(pointer)
            parent[key] = copy.deepcopy(value)
        else:
            raise ValueError('Assignment parent is not a JSON container')

    @staticmethod
    def _overlaps(a, b):
        return a == b or a.startswith(b + '/') or b.startswith(a + '/')

    @staticmethod
    def _ambiguity_metadata(context, record):
        annotations = context.get('branches', [])
        for annotation in annotations:
            identified = annotation.get('status') != 'source_qualified_not_machine_resolved'
            annotation['is_identified_branch'] = identified
            annotation['annotation_kind'] = 'branch' if identified else 'qualification'
        context['identified_branch_count'] = sum(a['is_identified_branch'] for a in annotations)
        context['qualification_annotation_count'] = len(annotations) - context['identified_branch_count']
        context['has_branches'] = context['identified_branch_count'] > 0
        context['has_ambiguity'] = bool(annotations) or any(q.get('support') in ('ambiguous', 'unresolved') for q in record.get('qualifications', []))
        return context

    def _default(self, source_id, current_only=True):
        envelope = self.record_envelope(source_id, current_only)
        cache_key = (source_id, envelope['version_hash'])
        if cache_key in self._defaults:
            self._defaults.move_to_end(cache_key)
            return copy.deepcopy(self._defaults[cache_key])
        index = self._index('default_records')
        if index.get('policy_fingerprint') != RESEARCH_POLICY_FINGERPRINT:
            raise ValueError('Default records belong to another release policy build')
        row = next(self.rows('default_records', source_id, envelope['version_hash']), None)
        if row is None or row.get('original_hash') != envelope.get('original_hash'):
            raise ValueError('Default record missing or immutable witness binding mismatch')
        record = row.pop('record')
        row.pop('schema', None)
        self._ambiguity_metadata(row, record)
        if digest(record) != row.get('default_record_sha256'):
            raise ValueError('Default record content hash mismatch')
        result = record, row
        self._defaults[cache_key] = copy.deepcopy(result)
        while len(self._defaults) > 2:
            self._defaults.popitem(last=False)
        return result

    def record(self, source_id, current_only=True):
        """One source-preferred research record; held choices are null."""
        return self._default(source_id, current_only)[0]

    def record_bytes(self, source_id, current_only=True):
        """Serialized research record; original hashes apply only to evidence bytes."""
        return json.dumps(self.record(source_id, current_only), ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')

    def research_value(self, source_id, pointer='', current_only=True):
        working, context = self._default(source_id, current_only)
        evidence = self.evidence_record(source_id, current_only)
        ancestor_pointer = None
        try:
            value = resolve_pointer(working, pointer)
        except (KeyError, IndexError, TypeError):
            # Only an actual evidence field can inherit a chosen-null ancestor.
            # This check preserves strict errors for typos and invalid pointers.
            resolve_pointer(evidence, pointer)
            pieces = pointer.split('/')[1:]
            for end in range(1, len(pieces)):
                prefix = '/' + '/'.join(pieces[:end])
                if resolve_pointer(working, prefix) is None:
                    ancestor_pointer = prefix
                    value = None
                    break
            if ancestor_pointer is None:
                raise
        branches = [b for b in context['branches'] if any(self._overlaps(pointer, p) for p in b['targets'])]
        qualifications = []
        ids = {v['id']: p for p, v in walk(evidence) if isinstance(v, dict) and isinstance(v.get('id'), str) and '/alternatives/' not in p}
        for i, q in enumerate(working.get('qualifications', [])):
            targets = [ids[t['record_id']] + t.get('field', '') for t in q.get('targets', []) if t.get('record_id') in ids]
            if any(self._overlaps(pointer, p) for p in targets):
                qualifications.append(dict(q, evidence_pointer='/qualifications/' + str(i), resolved_targets=targets))
        return dict(context, value=value, json_pointer=pointer, branches=branches,
                    value_status='null_due_to_unresolved_ancestor' if ancestor_pointer is not None else ('null' if value is None else 'present'),
                    ancestor_pointer=ancestor_pointer,
                    has_branches=any(b.get('is_identified_branch', b.get('status') != 'source_qualified_not_machine_resolved') for b in branches),
                    has_ambiguity=bool(branches) or any(q.get('support') in ('ambiguous', 'unresolved') for q in qualifications),
                    identified_branch_count=sum(b.get('is_identified_branch', b.get('status') != 'source_qualified_not_machine_resolved') for b in branches),
                    qualification_annotation_count=sum(not b.get('is_identified_branch', b.get('status') != 'source_qualified_not_machine_resolved') for b in branches),
                    qualifications=qualifications)

    def research(self, source_id, current_only=True):
        result = self.research_value(source_id, '', current_only)
        result['record'] = result.pop('value')
        return result

    def pointer(self, source_id, pointer, current_only=True):
        return resolve_pointer(self.record(source_id, current_only), pointer)

    def inspect(self, source_id, pointer='', current_only=True):
        """Explicit advanced comparison; never called by default queries."""
        try:
            result = self.research_value(source_id, pointer, current_only)
            result['default_pointer_exists'] = result.get('value_status') != 'null_due_to_unresolved_ancestor'
        except (KeyError, IndexError, TypeError):
            _, context = self._default(source_id, current_only)
            result = dict(context, value=None, json_pointer=pointer, default_pointer_exists=False)
        try:
            result['evidence_value'] = resolve_pointer(self.evidence_record(source_id, current_only), pointer)
            result['evidence_pointer_exists'] = True
        except (KeyError, IndexError, TypeError):
            if not result['default_pointer_exists']:
                raise
            result['evidence_value'] = None
            result['evidence_pointer_exists'] = False
        return result

    @staticmethod
    def _search_scalars(record, text):
        needle = text.casefold()
        def visit(value, pointer):
            if isinstance(value, dict):
                for key, child in value.items():
                    if key in ('branch_evidence', 'reasoning', 'qualifications'):
                        continue
                    yield from visit(child, pointer + '/' + key.replace('~', '~0').replace('/', '~1'))
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    yield from visit(child, pointer + '/' + str(index))
            elif needle in str(value).casefold():
                yield {'pointer': pointer, 'value': value}
        return visit(record, '')

    def _iter_default_rows(self, source_offset=0, source_limit=None):
        """Private verified rows. Never expose cached dicts to public callers."""
        index = self._index('default_records')
        if index.get('policy_fingerprint') != RESEARCH_POLICY_FINGERPRINT:
            raise ValueError('Default records belong to another release policy build')
        if not hasattr(self, '_default_source_order'):
            self._default_source_order = [sid for _, _, sid in sorted(
                (part, line, sid) for sid, positions in self._index('records')['sources'].items()
                for part, line in positions)]
            self._verified_default_hashes = set()
        order = self._default_source_order
        if source_offset > len(order):
            raise ValueError('Search cursor source offset out of range')
        end = len(order) if source_limit is None else min(len(order), source_offset + source_limit)
        for offset in range(source_offset, end):
            sid = order[offset]
            positions = index['sources'].get(sid, [])
            if len(positions) != 1:
                raise ValueError('Default source index missing or nonunique')
            part_number, line = positions[0]
            part = index['files'][part_number]
            row = self._part(part['path'], part['sha256'])[line]
            if row.get('source_id') != sid:
                raise ValueError('Default source index binding mismatch')
            key = (part['sha256'], line)
            if key not in self._verified_default_hashes:
                if digest(row['record']) != row.get('default_record_sha256'):
                    raise ValueError('Default record content hash mismatch')
                if not isinstance(row.get('current'), bool) or row.get('research_population') != ('current' if row['current'] else 'explicit_archival'):
                    raise ValueError('Default population binding mismatch')
                self._verified_default_hashes.add(key)
            yield offset, row

    def iter_records(self, current_only=True):
        """Stream detached materialized default envelopes; no raw or second reading."""
        for _, row in self._iter_default_rows():
            if not current_only or row['current']:
                detached = copy.deepcopy(row)
                yield self._ambiguity_metadata(detached, detached['record'])

    def search(self, source_id, text, current_only=True):
        """Literal scalar search of the single default, not alternative evidence."""
        return list(self._search_scalars(self.record(source_id, current_only), text))

    def search_all(self, text, current_only=True, offset=0, limit=None):
        """Stable source-order stream of detached default scalar matches."""
        if offset < 0 or (limit is not None and limit < 0):
            raise ValueError('offset and limit must be nonnegative')
        seen = emitted = 0
        for _, row in self._iter_default_rows():
            if current_only and not row['current']:
                continue
            for match in self._search_scalars(row['record'], text):
                if seen < offset:
                    seen += 1
                    continue
                if limit is not None and emitted >= limit:
                    return
                emitted += 1
                yield dict(match, source_id=row['source_id'], version_hash=row['version_hash'],
                    layer='source_preferred_research_default')

    def search_page(self, text, current_only=True, cursor=None, source_limit=25, limit=100):
        """Bound work by sources and matches; empty pages can have continuation."""
        if not isinstance(source_limit, int) or source_limit < 1 or not isinstance(limit, int) or limit < 1:
            raise ValueError('source_limit and limit must be positive integers')
        binding = hashlib.sha256(self._path('MANIFEST.json').read_bytes()).hexdigest()
        query = hashlib.sha256(json.dumps([text, current_only], ensure_ascii=False).encode()).hexdigest()
        if cursor is not None and (cursor.get('release') != binding or cursor.get('query') != query):
            raise ValueError('Search cursor belongs to another release/query/population')
        offset = (cursor or {}).get('source_offset', 0)
        within = (cursor or {}).get('match_offset', 0)
        if not isinstance(offset, int) or not isinstance(within, int) or offset < 0 or within < 0:
            raise ValueError('Invalid cursor offsets')
        results, scanned = [], 0
        for logical_offset, row in self._iter_default_rows(offset, source_limit):
            offset = logical_offset
            scanned += 1
            matches = list(self._search_scalars(row['record'], text)) if not current_only or row['current'] else []
            if within > len(matches):
                raise ValueError('Search cursor match offset out of range')
            while within < len(matches) and len(results) < limit:
                results.append(dict(matches[within], source_id=row['source_id'], version_hash=row['version_hash'],
                    layer='source_preferred_research_default'))
                within += 1
            if within == len(matches):
                offset += 1
                within = 0
            if len(results) == limit:
                break
        exhausted = offset == len(self._default_source_order)
        continuation = None if exhausted else {'release': binding, 'query': query, 'source_offset': offset, 'match_offset': within}
        return {'matches': results, 'next_cursor': continuation, 'exhausted': exhausted,
            'sources_scanned_this_page': scanned, 'total_matches': None,
            'note': 'No total or completeness claim until next_cursor is null.'}

    def evidence_connected(self, source_id, current_only=True):
        envelope = self.record_envelope(source_id, current_only)
        row = next(self.rows('connected', source_id, envelope['version_hash']), None)
        if row is None:
            raise KeyError('No connected evidence for exact selected version')
        return copy.deepcopy(row)

    def connected(self, source_id, current_only=True):
        """Rebuild source-local connectivity from the same default as record/search.

        Candidate evidence and convention joins are not asserted working edges.
        Node indices are presentation-local; stable keys are source/version/pointer.
        """
        record, context = self._default(source_id, current_only)
        baseline = self.evidence_connected(source_id, current_only)
        metadata = {n[0]: n for n in baseline['nodes'] if n[3] == 'encoded'}
        nodes, values, incidences, by_pointer, by_id = [], {}, [], {}, {}
        def walk(value, pointer='', parent=None):
            if isinstance(value, dict):
                here = parent
                if pointer and 'branch_evidence' not in pointer:
                    key = pointer.rsplit('/', 1)[-1]
                    inferred = {'adopted': 'quantity', 'numerator': 'quantity', 'denominator': 'quantity',
                        'components': 'components', 'expression': 'expression', 'derivation': 'derivation'}.get(key, 'component')
                    meta = metadata.get(pointer, [pointer, value.get('id'), inferred, 'encoded', 'typed_component'])
                    here = len(nodes)
                    nodes.append([pointer, value.get('id'), meta[2], 'research_default', meta[4]])
                    values[here] = value
                    by_pointer[pointer] = here
                    if isinstance(value.get('id'), str):
                        by_id.setdefault(value['id'], []).append(here)
                    if parent is not None:
                        incidences.append([parent, here, 'contains', pointer, 'research_default'])
                for key, child in value.items():
                    if key == 'branch_evidence':
                        continue
                    walk(child, pointer + '/' + key.replace('~', '~0').replace('/', '~1'), here)
            elif isinstance(value, list):
                for i, child in enumerate(value):
                    walk(child, pointer + '/' + str(i), parent)
        walk(record)
        roles = {'evidence': 'evidence', 'designation': 'evidence', 'evidence_refs': 'evidence',
            'ref': 'encoded_endpoint', 'subject_ref': 'encoded_endpoint', 'subject_id': 'encoded_endpoint',
            'object_id': 'encoded_endpoint', 'entity_refs': 'encoded_endpoint',
            'part_id': 'document_structure', 'parent_id': 'document_structure',
            'reasoning_ref': 'reasoning', 'premise_refs': 'reasoning',
            'record_id': 'qualification_target', 'important_uncertainty': 'qualification',
            'scope_refs': 'scope', 'unit_evidence': 'evidence', 'evidence_ref': 'evidence',
            'supporting_evidence_refs': 'evidence'}
        for key in ('member_measurement_ids', 'members', 'population_ref', 'group_members',
                    'target_measurement_ref', 'measurement_ref', 'input_measurement_ids',
                    'time_basis_ref', 'start_ref', 'end_ref', 'base_ref', 'membership_id',
                    'context_relation_refs', 'left_item_id', 'right_item_id'):
            roles[key] = 'encoded_endpoint'
        unresolved = []
        for i, value in values.items():
            p = nodes[i][0]
            local_roles = dict(roles)
            if p.endswith('/unit_evidence'):
                local_roles.update({key: 'evidence' for key in value})
            for key, role in local_roles.items():
                child = value.get(key)
                refs = list(enumerate(child)) if isinstance(child, list) else [(None, child)]
                for index, ref in refs:
                    if not isinstance(ref, str):
                        continue
                    rp = p + '/' + key + (('/' + str(index)) if index is not None else '')
                    candidates = by_id.get(ref, [])
                    if len(candidates) == 1:
                        target = candidates[0]
                        incidences.append([i, target, 'reference:' + role + ':' + key, rp,
                            'research_default', 'source_local', nodes[target][0]])
                    else:
                        unresolved.append({'reference_pointer': rp, 'local_id': ref,
                            'status': 'ambiguous_local_id' if candidates else 'unresolved_or_external'})
        qualification_targets = []
        original_local_ids = {n[1]: n[0] for n in baseline['nodes'] if n[1] is not None and n[3] == 'encoded'}
        for qi, q in enumerate(record.get('qualifications', [])):
            for target in q.get('targets', []):
                matches = by_id.get(target.get('record_id'), [])
                base_pointer = original_local_ids.get(target.get('record_id'))
                resolved = base_pointer + target.get('field', '') if base_pointer is not None else None
                qualification_targets.append({'qualification_id': q.get('id'),
                    'qualification_pointer': '/qualifications/' + str(qi),
                    'target_pointer': resolved, 'support': q.get('support'),
                    'resolution': 'source_local' if len(matches) == 1 else ('source_target_under_null_default' if resolved is not None else 'unresolved_target')})
        return {'binding': dict(baseline['binding'], value_layer='source_preferred_research_default', ledger_lookup="Graph.source(source_id)['ledger']"),
            'nodes': nodes, 'incidences': incidences, 'convention_edges': [],
            'convention_edges_note': 'Evidence-only conventions available via evidence_connected; not working identity or edges.',
            'unresolved_references': unresolved, 'identity_unions': [],
            'qualification_targets': qualification_targets,
            'has_branches': context['has_branches'], 'branches': context['branches'],
            'has_ambiguity': context.get('has_ambiguity', bool(context['branches'])),
            'identified_branch_count': context.get('identified_branch_count'),
            'diagnostics': context['diagnostics']}

    def neighbours(self, source_id, pointer, current_only=True):
        graph = self.connected(source_id, current_only)
        matches = {i for i, node in enumerate(graph['nodes']) if node[0] == pointer or node[1] == pointer}
        if not matches:
            raise KeyError(pointer)
        incidences = [r for r in graph['incidences'] if r[0] in matches or r[1] in matches]
        endpoints = {v for row in incidences for v in row[:2]} | matches
        return {'value_layer': 'source_preferred_research_default', 'binding': graph['binding'],
            'nodes': {str(i): graph['nodes'][i] for i in sorted(endpoints)}, 'incidences': incidences,
            'has_branches': graph['has_branches'], 'branches': graph['branches'],
            'has_ambiguity': graph['has_ambiguity'], 'identified_branch_count': graph['identified_branch_count'],
            'unresolved_references': graph['unresolved_references']}

    def typed_nodes(self, kind=None, layer=None, source_id=None, current_only=True):
        for envelope in self.rows('records', source_id):
            if current_only and not envelope['current']:
                continue
            record = self.record(envelope['source_id'], current_only)
            for node in self.connected(envelope['source_id'], current_only)['nodes']:
                if (kind is None or node[2] == kind) and (layer is None or node[3] == layer):
                    yield {'source_id': envelope['source_id'], 'version_hash': envelope['version_hash'],
                        'pointer': node[0], 'local_id': node[1], 'kind': node[2], 'layer': node[3],
                        'category': node[4], 'value': resolve_pointer(record, node[0])}

    def typed_relations(self, relation_type=None, source_id=None, current_only=True):
        """Default relation values with source-local endpoint bindings, never identity closure."""
        for envelope in self.rows('records', source_id):
            if current_only and not envelope['current']:
                continue
            source = envelope['source_id']
            record = self.record(source, current_only)
            for i, relation in enumerate(record.get('relations', []) or []):
                if not isinstance(relation, dict) or (relation_type is not None and relation.get('type') != relation_type):
                    continue
                yield dict(self.research_value(source, '/relations/' + str(i), current_only),
                    relation_type=relation.get('type'), identity_scope='source_local_no_global_identity')

    def evidence_proofs(self, source_id, current_only=True):
        """Historical cached proof artifacts. Not recomputed default consequences."""
        envelope = self.record_envelope(source_id, current_only)
        return {'value_layer': 'stored_evidence_not_recomputed_research_default',
            'datasets': {dataset: list(self.rows(dataset, version_hash=envelope['version_hash'])) for dataset in (
            'accounting_accounts', 'accounting_linear_systems', 'accounting_conclusions',
            'temporal', 'alternatives', 'alternative_connections', 'count_bounds')}}



    def _portable_evidence_bytes(self, source_id):
        accessor = getattr(self, 'evidence_record_bytes', None)
        if accessor is None:  # compatibility with the audited pre-default reader
            accessor = self.record_bytes
        return accessor(source_id, current_only=False)

    def _portable_versions(self):
        if not hasattr(self, '_portable_version_index'):
            by_hash = {}
            for row in self.rows('records'):
                h = row['version_hash']
                if h in by_hash:
                    raise ValueError('Ambiguous selected version hash')
                by_hash[h] = {'source_id': row['source_id'], 'version_hash': h,
                              'current': row['current']}
            self._portable_version_index = by_hash
        return self._portable_version_index

    def resolve_record_pointer(self, version_hash, pointer='', source_id=None):
        """Resolve only the exact selected immutable payload; never fall back to a head."""
        binding = self._portable_versions().get(version_hash)
        if binding is None:
            return {'resolution': 'version_not_in_selected_export', 'target': None,
                    'requested': {'source_id': source_id, 'version_hash': version_hash,
                                  'pointer': pointer}}
        if source_id is not None and binding['source_id'] != source_id:
            raise ValueError('Source/version binding mismatch')
        raw = self._portable_evidence_bytes(binding['source_id'])
        if hashlib.sha256(raw).hexdigest() != version_hash:
            raise ValueError('Exact version binding mismatch')
        value = resolve_pointer(json.loads(raw), pointer)
        return {'resolution': 'exact_selected_version',
                'target': dict(binding, pointer=pointer), 'value': value,
                'scientific_authority_upgrade': False}

    def original_witness_links(self, source_id, source_version):
        """Bind source + SHA + byte length independently of canonical availability."""
        matches = []
        if source_version.get('encoding') != 'utf-8':
            raise ValueError('Unsupported original encoding')
        for row in self.rows('originals', source_id):
            if row['sha256'] != source_version['sha256']:
                continue
            raw = self.original(source_id, row['kind'])
            if len(raw) != source_version['bytes']:
                raise ValueError('Original witness length mismatch')
            matches.append({'dataset': 'originals', 'source_id': source_id,
                            'kind': row['kind'], 'sha256': row['sha256'],
                            'bytes': len(raw), 'encoding': source_version['encoding']})
        return {'resolution': 'exact_shipped_witness' if matches else 'exact_witness_not_exported',
                'targets': matches, 'requested_source_id': source_id,
                'requested_source_version': dict(source_version)}

    def citation_links(self, source_id=None):
        """Each stored citation once; null canonical target does not mean absent evidence."""
        versions = self._portable_versions()
        for row in self.rows('cross_record_citations'):
            owner_hash, pointer = row['from']
            owner = versions.get(owner_hash)
            if owner is None:
                raise ValueError('Citation owner absent from selected export')
            if source_id is not None and owner['source_id'] != source_id:
                continue
            cited = row['citation']
            canonical_citation = self.resolve_record_pointer(owner_hash, pointer)['value']
            if (canonical_citation['source_id'] != cited['source_id'] or
                    canonical_citation['source_version'] != cited['source_version']):
                raise ValueError('Citation canonical evidence mismatch')
            target_hash = row['to_record_version']
            target = None
            if target_hash is not None:
                resolved = self.resolve_record_pointer(target_hash, '/document', cited['source_id'])
                if resolved['target'] is None or resolved['value']['source_version'] != cited['source_version']:
                    raise ValueError('Invalid non-null citation target')
                target = dict(versions[target_hash], pointer='/document')
                disposition = 'exact_selected_version'
            elif row['resolution'] == 'no_selected_canonical_record':
                disposition = 'documentary_target_without_selected_canonical_payload'
            elif row['resolution'] == 'canonical_head_version_mismatch':
                disposition = 'selected_canonical_target_original_version_mismatch'
            else:
                raise ValueError('Unknown unresolved citation disposition')
            if target_hash is None:
                selected = next(self.rows('records', cited['source_id']), None)
                if disposition == 'documentary_target_without_selected_canonical_payload':
                    if selected is not None:
                        raise ValueError('Unresolved citation contradicts selected target availability')
                else:
                    if selected is None:
                        raise ValueError('Version-mismatch citation lacks selected target')
                    selected_doc = json.loads(self._portable_evidence_bytes(cited['source_id']))['document']
                    if selected_doc['source_version'] == cited['source_version']:
                        raise ValueError('Version-mismatch citation actually matches target')
            yield {'owner': dict(owner, pointer=pointer),
                   'relationship': row['relationship'],
                   'canonical_resolution': disposition, 'resolved_canonical_target': target,
                   'original_witness': self.original_witness_links(cited['source_id'], cited['source_version']),
                   'upstream_resolution': row['resolution'],
                   'canonical_evidence_unchanged': True, 'scientific_authority_upgrade': False}

    def ledger_handle(self, source_id):
        """Portable ledger location, with the original SQL description retained separately."""
        source = self.source(source_id)
        if 'ledger' not in source:
            return {'resolution': 'catalogue_only_no_scientific_ledger', 'target': None,
                    'source_id': source_id, 'scientific_authority_upgrade': False}
        historical = []
        for row in self.rows('connected', source_id=source_id):
            value = row.get('binding', {}).get('ledger_lookup')
            if value is not None and value not in historical:
                historical.append(value)
        return {'resolution': 'shipped_source_ledger',
                'target': {'dataset': 'sources', 'source_id': source_id, 'pointer': '/ledger'},
                'ledger_original_sha256': source.get('ledger_original_sha256'),
                'historical_locators': historical,
                'historical_locator_is_runtime_dependency': False,
                'scientific_authority_upgrade': False}

    def predecessor_link(self, source_id):
        """Historical canonical predecessor, not the original witness or recovery history."""
        e = self.record_envelope(source_id, current_only=False)
        doc = json.loads(self._portable_evidence_bytes(source_id))['document']
        predecessor = doc['supersedes']
        out = {'owner': {'source_id': source_id, 'version_hash': e['version_hash'],
                         'pointer': '/document/supersedes'},
               'requested_predecessor': predecessor, 'target': None,
               'relation': 'canonical_revision_predecessor',
               'not_a_missing_original_or_reconstruction_history_count': True,
               'scientific_authority_upgrade': False}
        if predecessor is None:
            out['resolution'] = 'no_predecessor_declared'
            return out
        binding = self._portable_versions().get(predecessor['sha256'])
        if binding is None:
            out['resolution'] = 'historical_payload_not_exported'
            return out
        raw = self._portable_evidence_bytes(binding['source_id'])
        target_doc = json.loads(raw)['document']
        if (binding['source_id'] != predecessor['source_id'] or
                target_doc['revision'] != predecessor['revision'] or
                len(raw) != predecessor['bytes'] or
                hashlib.sha256(raw).hexdigest() != predecessor['sha256']):
            raise ValueError('Historical predecessor binding mismatch')
        out.update(resolution='exact_selected_version', target=dict(binding, pointer=''))
        return out

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).parent)
    parser.add_argument('command', choices=('source', 'record', 'original', 'pointer', 'neighbours',
        'citation-links', 'ledger-handle', 'predecessor-link', 'resolve-record-pointer', 'search', 'search-all', 'search-page', 'research', 'inspect', 'evidence-record', 'evidence-proofs', 'verify'))
    parser.add_argument('source_id', nargs='?')
    parser.add_argument('value', nargs='?')
    parser.add_argument('--archival', action='store_true')
    parser.add_argument('--kind', default='registered')
    parser.add_argument('--offset', type=int, default=0)
    parser.add_argument('--limit', type=int, default=100)
    parser.add_argument('--source-limit', type=int, default=25)
    parser.add_argument('--cursor', help='Exact next_cursor JSON from search-page')
    args = parser.parse_args()
    g = Graph(args.root)
    if args.command == 'verify':
        result = g.verify()
    elif args.command == 'citation-links':
        result = list(g.citation_links(args.source_id))
    elif not args.source_id:
        parser.error('source_id (or search-all text) required')
    elif args.command == 'search-page':
        result = g.search_page(args.source_id, not args.archival, json.loads(args.cursor) if args.cursor else None, args.source_limit, args.limit)
    elif args.command == 'search-all':
        result = list(g.search_all(args.source_id, not args.archival, args.offset, args.limit))
    elif args.command == 'resolve-record-pointer':
        result = g.resolve_record_pointer(args.source_id, args.value or '')
    elif args.command in ('ledger-handle', 'predecessor-link'):
        result = getattr(g, args.command.replace('-', '_'))(args.source_id)
    elif args.command == 'source':
        result = g.source(args.source_id)
    elif args.command == 'original':
        sys.stdout.buffer.write(g.original(args.source_id, args.kind)); return
    elif args.command == 'evidence-record':
        sys.stdout.buffer.write(g.evidence_record_bytes(args.source_id, not args.archival)); return
    elif args.command in ('pointer', 'neighbours', 'search'):
        if args.value is None:
            parser.error('pointer or search text required')
        result = getattr(g, args.command)(args.source_id, args.value, not args.archival)
    elif args.command in ('research', 'inspect'):
        result = getattr(g, args.command)(args.source_id, not args.archival) if args.command == 'research' and args.value is None else (
            g.research_value(args.source_id, args.value, not args.archival) if args.command == 'research' else
            g.inspect(args.source_id, args.value or '', not args.archival))
    else:
        result = getattr(g, args.command.replace('-', '_'))(args.source_id, not args.archival)
    print(json.dumps(result, ensure_ascii=False, indent=2))

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def walk(value, pointer=''):
    yield pointer, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, pointer + '/' + str(key).replace('~', '~0').replace('/', '~1'))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, pointer + '/' + str(index))

RESEARCH_POLICY_FINGERPRINT = 'a20b3fc7a61fb297004d7bc8c2281e5bc25f0bf75c581e1da1ceb543e2efd02f'

if __name__ == '__main__':
    main()
