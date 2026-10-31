# Girsu source graph

An application-independent data foundation for Girsu source records: structured documentary content, source-local relationships, exact evidence and provenance, with a portable read-only Python reader.

**Ordinary access returns one default reading. Its value can be `null`.** Ambiguity, applicable qualifications and exact evidence pointers accompany that reading; consumers do not have to choose between two parallel records. Exact original text and preserved canonical records remain available through explicitly advanced evidence access. No later global identity reconstruction is included.

## Quick start

Use **Python 3.11+**, with no third-party packages, database server, network service or old workspace required. Run from the directory containing `girsu.py`, `data/` and `MANIFEST.json`:

```sh
python girsu.py verify
python girsu.py record P105740
python girsu.py research P102673 /entries/21/measurements/0/adopted
python girsu.py pointer P105740 /entries/2/membership
python girsu.py neighbours P105740 /entries/2/membership
python girsu.py search P100144 metrological_standard
python girsu.py search-page metrological_standard --source-limit 25 --limit 20
```

```python
from girsu import Graph

g = Graph()                       # or Graph('/path/to/release')
record = g.record('P105740')       # the same default used by search and graph access
field = g.research_value('P102673', '/entries/21/measurements/0/adopted')
print(field['value'])             # one value, including null when held
print(field['has_branches'])      # identified choice set only
print(field['has_ambiguity'])     # broader scoped annotation/uncertainty warning
print(field['qualifications'])
print(field['branches'])          # labelled branch OR qualification annotations
```

`research_value` is the annotation-bearing field accessor; `research` returns the same default record with context. It can report a valid source field beneath a held-null parent as `value_status='null_due_to_unresolved_ancestor'`, with its ancestor pointer and evidence. `pointer` is strict traversal and may fail beneath that null parent; use the annotated accessor for such fields. A null is not zero and must not be replaced with a candidate from a different API. See [semantics](docs/SEMANTICS.md).

For a detached record stream, use `g.iter_records()`; each envelope contains `record` plus source-level context. Use `research_value` when field-applicable qualifications are needed. In the preserved `branches` annotation list, `is_identified_branch`/`annotation_kind` distinguish real choice sets from qualification-only context. Neither boolean flag is a probability or completeness certificate.

For bounded corpus search, pass the returned `next_cursor` unchanged to `search_page`. **An empty page need not mean completion:** check `exhausted`; a completed search has no next cursor. A page or `--limit` is not a corpus count. `search_all` streams the complete default population when an unrestricted scan is wanted.

## What is preserved

| Holding | Count |
|---|---:|
| Registered textual sources | 19,208 |
| Catalogue-only IDs without saved ATF | 11,048 |
| Documentary universe | 30,256 |
| Selected canonical source records | 18,412 |
| Current source records, included by default | 18,409 |
| Explicit archival-only selected records | 3 |
| Stored original-text witness rows | 38,046 |

Witness rows are not necessarily distinct texts: 17,969 registered/canonical pairs are byte-identical. One source can contain tablet, envelope and seal parts. Source IDs, physical witnesses, mentions and historical people are different counting units.

The preserved current canonical evidence contains 172,723 entries, 149,429 mentions, 171,251 relations, 165,959 measurements and 872,362 evidence anchors. These are **source-evidence counts**, not a census of populated fields after default nulling. The source covers accounts, receipts, expenditure, personnel lists, inventories, legal records, letters, seal/royal representations and other/unsettled genres.

All **98,928 current unclassified relations retain their populated `native_label` in the preserved canonical evidence**. Default labels are searchable unless an explicit unresolved branch makes that field null; in that case the original label remains accessible at its evidence pointer. No speculative relation taxonomy has been imposed. Some labels are explanatory English, not verbatim Sumerian. Native temporal formulas are preserved without fabricating absolute chronology. Quantities use exact rational strings and native units, without arbitrary conversions.

## One default, common checks

* P102673's supported restored counts are **1,1,2,2**, with conditional schedule **177**. Written principal **217** and discrepancy **20** stay unchanged; calculated **237** is diagnostic, not a replacement chosen to balance an account.
* P105740 retains **administrator** as the supported title interpretation, with its judge alternative available in evidence. P204204 is a different source whose primary queried title is judge. No new `judge` enum or cross-source identity is invented.
* An unresolved structured choice can yield null without claiming the ancient source has no preference. The bounded machine policy does not interpret all prose meaning.

The structured-set pass inspected 3,537 sets: 26 typed selections and one additional bounded prose selection; 3,511 typed sets were held. Thirteen selections used exact evidence-anchor verification and fourteen used source-record reasoning alone. A further 10,601 source-qualified-not-machine-resolved annotations preserve context, not additional proven branches. The separate 9,512-item prose-signal queue is **not** 9,512 proven branches or additional adopted readings. Details and test scope are in [validation](docs/VALIDATION.md).

## Files and access

* `data/default_records/`: precomputed, hash-checked default records and field-context metadata; no interpretation engine is needed at query time.
* `data/records/`, `originals/`, `sources/`: exact canonical strings, exact original bytes and scientific provenance.
* `data/catalogue/`, `availability/`, `aliases/`, `admission/`: documentary coverage and retained bindings.
* `data/graph/`: preserved assembled evidence, including conditional accounting, temporal, alternatives and documentary-support structures. Default graph access rebuilds from the same default values; historical cached consequences are not falsely described as recomputed defaults.

Compressed JSONL partitions, source indexes, manifests, RFC6901 pointers and SHA-256 bindings are portable; no SQLite file is shipped. Stable addresses use source ID, original record-version hash and pointer. Graph row/node ordinals are not stable identifiers.

Advanced evidence access is explicit: `evidence_record`, `evidence_record_bytes`, `evidence_original`, `evidence_connected`, `evidence_proofs`, and `inspect`. `version_hash` identifies the original canonical bytes, **not** the derived default serialization; defaults have their own `default_record_sha256` and policy fingerprint. See [data dictionary](docs/DATA_DICTIONARY.md), [default policy](docs/DEFAULT_POLICY.md), [provenance](docs/PROVENANCE.md) and [validation](docs/VALIDATION.md). The small [query cookbook](docs/COOKBOOK.md) demonstrates generic field/occurrence retrieval, not a research classification system.
