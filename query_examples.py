#!/usr/bin/env python3
"""Small streaming research queries; no identity merging or numeric conversion.

After installation beside girsu.py (or under examples/), see --help.
CSV cells contain JSON values: decode with json.loads, not spreadsheet inference.
"""
import argparse
import csv
import json
from pathlib import Path
import sys

FIELDS = ('source_id', 'version_hash', 'current', 'layer', 'pointer', 'local_id',
          'value', 'has_branches', 'has_ambiguity', 'qualifications', 'branches', 'evidence', 'context')
MODES = ('genre', 'date', 'institution', 'commodity', 'relation', 'person')


def walk(value, pointer=''):
    yield pointer, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, pointer + '/' + key.replace('~', '~0').replace('/', '~1'))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, pointer + '/' + str(index))


def overlaps(a, b):
    return a == b or a.startswith(b + '/') or b.startswith(a + '/')


def contains(value, text):
    return isinstance(value, str) and text.casefold() in value.casefold()


def query(graph, mode, text, source_ids=None, include_archival=False):
    """Yield occurrence rows, preserving one default reading and field context.

    genre and relation are exact labels; all other modes use literal substring
    matching (case-insensitive, no transliteration/synonym normalization).
    'genre null' explicitly selects null genres. Default population is current.
    """
    if mode not in MODES:
        raise ValueError('Unknown query mode')
    sources = (graph.record_envelope(s, not include_archival) for s in source_ids) if source_ids else graph.rows('records')
    for envelope in sources:
        if not include_archival and not envelope['current']:
            continue
        sid = envelope['source_id']
        result = graph.research(sid, current_only=not include_archival)
        record = result['record']
        id_map = {v['id']: (p, v) for p, v in walk(record)
                  if isinstance(v, dict) and isinstance(v.get('id'), str)
                  and not p.startswith(('/qualifications/', '/reasoning/'))} if mode == 'relation' else {}
        candidates = []
        if mode == 'genre':
            value = record['document']['document_type']
            if value == (None if text == 'null' else text):
                candidates.append(('/document/document_type', record['document'], value, {}))
        elif mode == 'date':
            for i, value in enumerate(record['document']['dates']):
                if value.get('kind') == 'calendar' and any(contains(value.get(k), text) for k in ('year_formula', 'month_name')):
                    links = [{'pointer': f'/entries/{ei}/dates/{di}', 'value': link}
                             for ei, entry in enumerate(record['entries'])
                             for di, link in enumerate(entry.get('dates') or []) if link.get('ref') == value['id']]
                    candidates.append((f'/document/dates/{i}', value, value, {'date_applicability': links}))
        elif mode in ('institution', 'person'):
            for i, value in enumerate(record['mentions']):
                if value.get('kind') == mode and any(contains(value.get(k), text) for k in ('search_form', 'literal')):
                    # One row per mention, even when both literal and search_form match.
                    candidates.append((f'/mentions/{i}', value, value, {'count_unit': 'mention_occurrence_not_historical_entity'}))
        elif mode == 'commodity':
            for ei, entry in enumerate(record['entries']):
                for ii, value in enumerate(entry.get('items') or []):
                    if any(contains(value.get(k), text) for k in ('type_id', 'native_term_id')):
                        measurements = [{'pointer': f'/entries/{ei}/measurements/{mi}', 'value': m}
                                        for mi, m in enumerate(entry.get('measurements') or []) if m.get('subject_ref') == value['id']]
                        candidates.append((f'/entries/{ei}/items/{ii}', value, value, {'entry_id': entry['id'], 'measurements': measurements}))
        elif mode == 'relation':
            for i, value in enumerate(record['relations']):
                if value.get('type') == 'unclassified' and value.get('native_label') == text:
                    endpoints = []
                    for key in ('subject_id', 'object_id', 'members'):
                        refs = value.get(key)
                        refs = refs if isinstance(refs, list) else [refs]
                        for ref in refs:
                            if ref in id_map:
                                p, obj = id_map[ref]
                                endpoints.append({'role': key, 'local_id': ref, 'pointer': p, 'value': obj})
                    candidates.append((f'/relations/{i}', value, value, {'endpoints': endpoints}))
        if not candidates:
            continue
        anchors = {v['id']: (i, v) for i, v in enumerate(record['document']['evidence'])}
        reasons = {v['id']: (i, v) for i, v in enumerate(record.get('reasoning', []))}
        for pointer, obj, value, context in candidates:
            # Include separately scoped context qualification rows; never assert
            # that a participant or quantity qualification belongs to the item.
            context_pointers = [v['pointer'] for key in ('endpoints', 'measurements', 'date_applicability') for v in context.get(key, [])]
            def qs(p):
                selected = []
                for q in result['qualifications']:
                    if not any(overlaps(p, t) for t in q.get('resolved_targets', [])):
                        continue
                    q = dict(q)
                    if q.get('reasoning_ref') in reasons:
                        ri, reason = reasons[q['reasoning_ref']]
                        q['reasoning_pointer'] = f'/reasoning/{ri}'
                        q['reasoning'] = reason
                        q['anchor_pointers'] = [f'/document/evidence/{anchors[e][0]}' for e in reason.get('evidence_refs', []) if e in anchors]
                    selected.append(q)
                return selected
            context['qualifications_by_pointer'] = {p: qs(p) for p in context_pointers}
            context['branches_by_pointer'] = {p: [b for b in result['branches'] if any(overlaps(p, t) for t in b.get('targets', []))] for p in context_pointers}
            quals = qs(pointer)
            branches = [b for b in result['branches'] if any(overlaps(pointer, p) for p in b.get('targets', []))]
            refs = obj.get('evidence') or obj.get('designation') or []
            # Document.evidence is an anchor table, not a list of evidence IDs.
            refs = [ref for ref in refs if isinstance(ref, str)]
            evidence = [{'original_sha256': record['document']['source_version']['sha256'],
                         'pointer': f'/document/evidence/{anchors[ref][0]}', 'anchor': anchors[ref][1]}
                        for ref in refs if ref in anchors]
            yield dict(source_id=sid, version_hash=result['version_hash'], current=envelope['current'],
                       layer=result['layer'], pointer=pointer, local_id=obj.get('id'), value=value,
                       has_branches=any(b.get('is_identified_branch', b.get('annotation_kind') == 'branch') for b in branches),
                       has_ambiguity=bool(branches) or any(q.get('support') in ('ambiguous', 'unresolved') for q in quals),
                       qualifications=quals, branches=branches, evidence=evidence, context=context)


def write_rows(rows, stream, format='jsonl'):
    if format == 'jsonl':
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n')
    elif format == 'csv':
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            # Every cell is JSON, preserving null vs empty string and exact
            # rational strings; strings cannot begin a spreadsheet formula.
            writer.writerow({k: json.dumps(row[k], ensure_ascii=False, separators=(',', ':')) for k in FIELDS})
    else:
        raise ValueError('Expected jsonl or csv')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=MODES)
    parser.add_argument('text')
    parser.add_argument('--root', type=Path, required=True, help='Released repository root containing girsu.py and data/')
    parser.add_argument('--source', action='append', help='Optional exact source ID; repeat to narrow the scan')
    parser.add_argument('--archival', action='store_true', help='Explicitly include archival selected records')
    parser.add_argument('--format', choices=('jsonl', 'csv'), default='jsonl')
    parser.add_argument('--limit', type=int, help='Display prefix only, not a total count')
    args = parser.parse_args()
    if args.limit is not None and args.limit < 0:
        parser.error('--limit must be nonnegative')
    sys.path.insert(0, str(args.root.resolve()))
    from girsu import Graph
    rows = query(Graph(args.root), args.mode, args.text, args.source, args.archival)
    if args.limit is not None:
        from itertools import islice
        rows = islice(rows, args.limit)
    write_rows(rows, sys.stdout, args.format)


if __name__ == '__main__':
    main()
