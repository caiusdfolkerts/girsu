# Provenance

The release preserves the original source graph: selected canonical records, their original-text witnesses, source-local relationships, and the evidence needed to trace scientific decisions. It also supplies one materialized default for ordinary use. These layers have different purposes. The canonical record preserves the stored interpretation; the original witness preserves its textual evidence; the default provides a bounded reading without changing either.

The repository is self-contained. It does not require the earlier workspace, its checkpoints, or its SQLite database. Historical paths and artifact names remain where they explain provenance, but they are not runtime dependencies. Later global identity-reconstruction outputs do not supply the canonical records or relationship layers in this release.

## The selected corpus

The catalogue contains 30,256 IDs selected by membership in the Girsu site group. Of these, 19,208 have ATF and constitute the registered textual sources. The other 11,048 are retained as catalogue-only metadata; the two populations are disjoint.

The export contains 18,412 selected canonical records, preserving 383,326,128 bytes of stored UTF-8 JSON. Of these, 18,409 match their source's exact current version pointer, accounting for 383,300,606 bytes. The remaining three are archival-only selections, accounting for 25,522 bytes.

“Current” means that both the source ID and version hash match the source's current pointer. It does not mean the highest revision, the newest timestamp, or simply that a stored row exists. The exported `current` flag records this distinction. `Graph.record()` returns the single default for a current source and does not promote archival material. The explicit `current_only=False` option, or CLI `--archival`, permits access to the three archival defaults without changing their status or authority.

There are 799 registered sources without a current canonical pointer. This population consists of 282 sources represented by documentary availability but no selected canonical scientific JSON, 514 with neither a selected record nor a documentary/scientific admission head, and the three archival selections. Within the group of 514, the registry marks 315 as ready, 162 as blocked, and 37 as researching. An original text can therefore be present without a canonical scientific interpretation. In particular, the 282 availability objects are not empty scientific records.

The current population comprises 15,934 canonical-non-graph selections and 2,475 exact scientific-admission selections. Scientific admission and canonical selection are bindings of a source, not additional documents to be added together.

## Records, defaults, and projected provenance

The canonical `record_json` is preserved as the exact stored JSON string. Its UTF-8 bytes hash to `version_hash` and are available through `evidence_record_bytes`, not ordinary `record_bytes`. Canonical qualification, alternative, reasoning, and local social-relation objects are unchanged. Original text bytes are preserved in base64 with their exact SHA-256. Source-version, predecessor, original-witness, and scientific-admission bindings remain explicit.

The records under `data/default_records/` are a separate representation: one precomputed default for each of the 18,409 current and three archival selections. Each row identifies its canonical version, exact original witness, and `default_record_sha256`; the index binds the default policy fingerprint. Ordinary queries verify and read these defaults without a parser, builder, database, or private runtime. Each ordinary field has one value, which may be null, while alternatives remain accessible as evidence.

A canonical `version_hash` does not hash the serialized default. The default has its own hash and serialization contract. This separation matters both for verification and interpretation: making a default neither alters the source evidence nor confers additional scientific authority.

Scientific ledgers and admissions undergo a narrowly specified provenance projection. It removes workflow transport fields—leases and tokens at known canonical, delivery, archival/recovery-hold, admission, and alias locations—and physical capture or supporting-root locations. It does not remove every key called `token`, nor does it delete scientific wording. Exact per-path removal counts appear in [`data/SOURCE_CERTIFICATE.json`](../data/SOURCE_CERTIFICATE.json), and [`data/PROJECTION_CHANGES.jsonl.gz`](../data/PROJECTION_CHANGES.jsonl.gz) records the source, path, and hash changes.

The projection retains scientific authority, author and reviewer attribution, decisions, audits, holds, resolutions, provenance strings, and historical locators. `ledger_original_sha256` binds the ledger before projection; it is not the expected hash of a reserialized projected ledger. The certificate and change audit describe the treatment of nested workflow records.

Admission provenance retains 2,553 scientific-admission versions, including 78 non-active historical admissions. Duplicate transport copies named `record_hex`, `original_hex`, and `predecessor_hex` are not shipped again. Their hashes and byte counts retain the bindings; selected records and original witnesses are accessible through the source datasets. The release is not a complete archive of every historical canonical payload.

Old queue databases, automation state, receipt tables, checkpoints, build intermediates, and global identity directories are outside the export. Their omission does not remove the retained scientific decisions, attributions, holds, exact-version resolutions, or the 91 reconstruction-origin references.

## Original-text witnesses

The original-text layer contains 38,046 witness rows across all 19,208 registered sources, totaling 23,010,299 bytes. There are 19,208 `registered` rows, 18,835 `canonical` rows, and three `historical_local_archival_acceptance` rows. These counts distinguish witness kinds, not necessarily different texts: many paired witnesses are byte-identical.

Every selected record's `document.source_version.sha256` resolves to a stored original with the matching byte length. Across the 18,412 selected records, 17,452 match both registered and canonical witnesses, 866 match only canonical witnesses, 91 match only registered witnesses, and three match registered, canonical, and archival witnesses. Thus a record's exact evidence witness need not bear the label `canonical`. The 91 current reconstructed records bind to saved registered originals.

Of the 18,835 canonical/registered pairs, 17,969 are byte-identical and 866 differ. All 866 differing pairs have the same whitespace-token sequence. Outer whitespace stripping makes 822 equal; stripping plus CRLF-to-LF normalization makes the remaining 44 equal. Both variants remain preserved. Their physical line counts can differ, so lexical equivalence does not make their evidence coordinates interchangeable.

To retrieve the witness used by a record, read `record['document']['source_version']['sha256']`, enumerate `Graph.rows('originals', source_id)`, and choose the row with that SHA. Then call `Graph.original(source_id, kind)` for its kind. The `original` command defaults to the registered witness for convenience; that is not necessarily the witness cited by the canonical record.

## Review and retained dispositions

The source ledger records version-bound authorship and review, decisions, delivery status, audits, holds, and resolutions. Reviewer labels identify pipeline agents. They are not evidence of external human Assyriological peer review.

The snapshot contains 16,610 exact-current accepted decisions and 16,610 delivery records. Delivery status is recorded as handed off for 11,512, ready for 5,021, and revoked for 77. Delivery status is distinct from scientific authority and from any later audit disposition.

A specific group of 623 sources uses an authorized author-self-check route: 367 are author-finalized, 15 cloud-maintenance finalized, and 241 local-author-finalized. Their bin provenance is 607 `user-requested-research623` plus 16 `local623`; these are not 623 additional local-bin records. They have no separate current reviewer decision. This authorization applies to that cohort, not to the corpus generally, and is not independent external review.

Audit provenance covers 2,585 sources: 2,532 paused-unverified, 47 cleared, and six unverified. There are also 1,155 partition-hold provenance entries, including 26 with cleared audit status. A historical hold field alone does not establish a present exclusion: the applicable version, decision, and resolution must be read together. Equally, an accepted state does not cancel a later bounded hold.

Thirteen recovery-hold entries retain their histories. Ten have explicit resolution records bound to the current accepted version and decision. The other three—`P112859`, `P112877`, and `P116040`—retain older held hashes that differ from their current accepted scientific heads, without a separate recovery-hold-resolution entry in those ledger fields. They should not be described either as automatically excluded or as explicitly cleared.

The 91 reconstruction-origin records retain missing-history and recovery lineage. Their current canonical payloads and exact saved originals are present. They are not 91 missing records, and their history must not be recast as an independently reviewed original extraction. Broader recovery-link entries likewise record provenance rather than additional documents.

The single explicit documentary alias, `P142584→P500235`, is marked documentary-only with `identity_merge=0`. It neither adds a duplicate scientific record nor establishes a historical identity union.

## The evidence graph

The connected evidence representation makes exact canonical JSON addressable as typed nodes, including components without local IDs. Across all stored selections it contains 3,172,743 explicit-ID canonical objects and 1,900,266 typed ID-less components, giving 5,073,009 connected nodes. Its 8,683,442 incidences comprise 4,063,006 containment incidences and 4,620,436 schema-aware local-reference incidences. Separately labelled layers contain 4,422 convention edges, 24,520 candidate nodes, and 106 cross-record documentary citations. There are no identity unions.

The source database also maintained a direct explicit-ID/reference index. It counted 3,172,743 objects and 4,546,775 reference occurrences across all stored records, or 3,172,580 objects and 4,546,493 occurrences in current records. These are alternative index denominators, not additional nodes. The connected graph's schema-aware references include typed links, such as important-uncertainty references, that explain its larger reference count.

The export corrects 91,835 node schema-kind labels using exact version, pointer, and old-label checks. This repairs typed navigation without changing canonical JSON, incidence content, evidence, acceptance, or historical interpretation. The graph certificate records the correction rule and unchanged totals.

Accounting, temporal, alternative, count-bound, vocabulary-hub, and documentary-citation layers are preserved separately. They are labelled as derived, conditional, or representational as appropriate; none supplies new scientific authority. Ordinary graph methods rebuild from the same default used by record and search methods rather than asserting every cached or candidate evidence edge. Historical cached proofs remain evidence, not newly recomputed consequences of the default.

### Citation targets and original witnesses

Of the 106 cross-record citations, 101 resolve to an exact selected canonical target and five do not. The unresolved dataset repeats those five boundaries; it does not contain five additional citations.

All five unresolved citations nevertheless have their exact cited original witnesses. Three lack a selected canonical target payload; in the other two, the selected target binds a different original version. The resolver does not substitute the current head.

`Graph.citation_links(source_id=None)` reports each citation once, distinguishing `canonical_resolution` and `resolved_canonical_target` from `original_witness`. `Graph.original_witness_links(source_id, source_version)` checks the exact source ID, original SHA, byte count, and encoding. An unresolved canonical target is therefore not equivalent to missing original evidence.

### Predecessors and missing-history lineage

There are 4,553 selected records that declare a canonical predecessor. All 4,553 referenced predecessor payloads lie outside this selected export. `Graph.predecessor_link(source_id)` reports `historical_payload_not_exported`, not an invalid binding or a missing original.

This population is distinct from the 91 reconstruction-origin records discussed above. Those records have present current payloads and exact originals, together with retained missing-history provenance.

`Graph.resolve_record_pointer(version_hash, pointer='', source_id=None)` resolves only an exact selected version; it never falls back to another head. `Graph.ledger_handle(source_id)` provides a portable `data/sources` ledger handle while preserving old SQL locators as historical wording. Exact version matching, documentary availability, and scientific authority remain separate questions.

## Release bindings

The source database was inspected read-only. Source and graph export certificates bind the partitions to the same immutable database. The original release commit identifies the source release; it does not assert that this repository contains that Git commit.

The binding identifiers are:

```text
Source database SHA-256:
b02f70a3c3c01bfe96428e04ce674f19e21dbb620a463dd699034915c644205c

Source database bytes:
2,281,283,584

Original source release commit:
00e8cbe58e49885ad363581459eb1ce03844426e

Original source release tree:
c01ada22c99bbaf29dbb0e8c8cebb821e809adec

Original source release manifest SHA-256:
bf9a2f78da0d6fa073d6e83f33b62ad3bc42e5b830e78b145e76c6d37c53f158
```

[`data/SOURCE_CERTIFICATE.json`](../data/SOURCE_CERTIFICATE.json) records export counts, exact witness and record preservation, and the provenance projection. [`data/graph/certificate.json`](../data/graph/certificate.json) records graph populations, type-label corrections, dataset counts, and proof mapping. Data indexes and graph manifests give each compressed partition's path, SHA-256, byte count, and row count. The root `MANIFEST.json` inventories the shipped files used by `python girsu.py verify`.

## Verification

From the repository root:

```sh
python girsu.py verify
python girsu.py source P100144
python girsu.py pointer P105740 /entries/2/membership
python girsu.py citation-links P131513
python girsu.py ledger-handle P100144
python girsu.py predecessor-link P100144
```

The reader verifies manifest, index, and partition bindings, default content, and the policy fingerprint. When exact evidence bytes are requested, it also checks canonical and original hashes. Full `verify` checks every file against the shipped manifest without modifying the dataset or contacting a network service.

An independent check of a canonical record's bytes is:

```python
import hashlib
from girsu import Graph

g = Graph()
row = g.record_envelope('P100144')
assert hashlib.sha256(g.evidence_record_bytes('P100144')).hexdigest() == row['version_hash']
```

The graph validation certificates cover canonical node pointers, incidence reference and target pointers, shared hub/owner/provenance links, and explicit version/pointer pairs in derived data. All 156 accounting proof locators resolve through the shipped partition/index mapping. These are mechanical checks of representation and data binding, not external human review of every ancient interpretation. [Validation](VALIDATION.md) describes the consumer tests and the limits of the default policy.

Structural and semantic conventions are supplied under [`docs/schema/`](schema/). The filename `SOURCE_RECORD_SCHEMA_V1.proposed.json` is historical: in this release it supplies the source-record structural contract, read alongside the semantic rules and runtime refinements. `IDENTITY_CONVENTIONS_V1.md` describes original source-local occurrence, coreference, and kinship semantics, not the excluded later global identity-reconstruction results.

Unless a count is explicitly labelled all-stored or export-wide, content counts use the 18,409 exact-current canonical records. Object counts refer to serialized scientific objects at a stated path; source counts refer to distinct documents containing them. A source may occur in several categories. Candidate branches, supporting context, and archival records are not automatically adopted-current evidence.

The release does not establish a cross-document grand total, historical headcount, normalized chronology, modern unit conversion, global identity closure, or new event history. It preserves the records and their explicit derivations so that such claims can be examined rather than inferred from aggregate export counts.
