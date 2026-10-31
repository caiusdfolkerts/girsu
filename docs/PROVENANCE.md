# Provenance, release bindings and verification

This clean repository is a **standalone data foundation for the original source graph**, with one materialized default, exact canonical/original evidence, scientific provenance and source-local relationships. It does not require the earlier workspace, its checkpoints or its SQLite database. Historical paths and artifact names are inert provenance labels, not runtime dependencies.

## 1. Immutable input

| Binding | Value |
|---|---|
| Source database SHA-256 | `b02f70a3c3c01bfe96428e04ce674f19e21dbb620a463dd699034915c644205c` |
| Source database bytes | 2,281,283,584 |
| Original source release commit | `00e8cbe58e49885ad363581459eb1ce03844426e` |
| Original source release tree | `c01ada22c99bbaf29dbb0e8c8cebb821e809adec` |
| Original source release manifest SHA-256 | `bf9a2f78da0d6fa073d6e83f33b62ad3bc42e5b830e78b145e76c6d37c53f158` |

The source database was inspected read-only. No later global identity-reconstruction outputs supply the canonical records or relationship layers here. Export certificates bind the clean source/graph partitions to this same SHA. The source release commit is provenance, not a claim that this new clean repository has that Git commit.

Machine-readable certificates:

* [`data/SOURCE_CERTIFICATE.json`](../data/SOURCE_CERTIFICATE.json): source export counts, exact witness/record preservation and provenance projection.
* [`data/graph/certificate.json`](../data/graph/certificate.json): assembled graph population, type-label corrections, dataset counts and proof mapping.
* Each data index/graph manifest: compressed partition path, SHA-256, bytes and row count.
* Root `MANIFEST.json`: shipped-file inventory used by `python girsu.py verify`.

## 2. Documentary universe and exact-current selection

The catalogue universe contains **30,256 IDs**, selected by Girsu site-group membership. The **19,208 ATF-present IDs** equal the registered textual sources; the **11,048 no-ATF IDs** are disjoint and retained as catalogue-only metadata.

There are **18,412 selected stored canonical records**, with **383,326,128 exact canonical UTF-8 bytes**. Of those, **18,409** equal their source's exact current version pointer; the other three selected payloads are archival-only. Current records total 383,300,606 bytes and archival records 25,522 bytes.

Current selection is exact equality of source ID **and** version hash, not “the row exists,” highest revision or newest timestamp. The export's `current` boolean preserves that distinction. `Graph.record()` returns the single default for current sources; it does not silently promote archival material. `current_only=False`/CLI `--archival` permits explicit consultation of the three selected archival defaults, retaining archival status and without changing source authority. Exact source payloads are advanced evidence access.

The 799 registry IDs without a current canonical pointer comprise:

| Population | Sources |
|---|---:|
| Documentary availability, no selected canonical scientific JSON | 282 |
| Neither selected record nor documentary/scientific admission head | 514 |
| Archival selected record, no current pointer | 3 |

The 514 include 315 ready, 162 blocked and 37 researching registry sources. A source may therefore have an original without a canonical scientific interpretation. The 282 availability objects do not become 282 empty records.

Current records comprise 15,934 canonical-non-graph selections and 2,475 exact scientific-admission selections. Scientific admission and the canonical selected record are two bindings of a source, not additive documents.

## 3. What remains exact and what is projected

### Exact scientific payloads

* Canonical `record_json` is the exact stored JSON string. Its UTF-8 bytes hash to `version_hash`; retrieve through `evidence_record_bytes`, not ordinary `record_bytes`.
* Original text bytes are preserved base64-encoded, with exact SHA-256.
* Canonical qualification/alternative/reasoning objects and local social relations are unchanged.
* Source-version, predecessor, original and scientific-admission bindings remain explicit.

### Materialized default binding

`data/default_records/` supplies one precomputed record per selected source/version: 18,409 current and three explicitly archival. Each row binds the original record version, exact original witness and its own `default_record_sha256`; the index binds the policy fingerprint. Ordinary queries verify and consume this data; they do not need a parser, builder, database or private runtime.

The source `version_hash` does **not** hash the serialized default. Hash default content using its separate default hash/serialization contract. Alternative payloads remain advanced evidence behind exact pointers; ordinary fields have one default value, which can be null. Defaulting neither mutates source evidence nor upgrades source authority.

### Deliberately narrow provenance projection

Scientific ledgers/admission are projected to omit specifically enumerated workflow transport fields: leases/tokens at known canonical, delivery, archival/recovery-hold, admission and alias workflow locations, together with physical capture/supporting-root locations. The exact per-path removal counts are in `data/SOURCE_CERTIFICATE.json`; `data/PROJECTION_CHANGES.jsonl.gz` provides the source/path/hash change audit. This is **not** arbitrary deletion of every key named `token` or removal of scientific wording.

All remaining scientific authority, author/reviewer attribution, decisions, audit/hold/resolution values, provenance strings and historical locators remain retained. Historical paths do not become runtime dependencies. `ledger_original_sha256` binds the source ledger before projection; it should not be compared to a reserialization of the projected ledger as though those were the same bytes. Consult the projection certificate/change audit for the exact treatment of nested workflow records rather than assuming the exported ledger is byte-identical to the source ledger.

Admission provenance retains 2,553 scientific-admission versions, including 78 non-active historical admissions. Duplicate transport `record_hex`, `original_hex` and `predecessor_hex` payloads are not shipped again: their hashes/byte counts preserve bindings, while selected records and original witnesses are accessible through the source datasets. This clean repository is not a complete archive of every historical canonical payload.

Old queue databases, automation state, receipt tables, checkpoints, build intermediates and global identity directories are not exported. Their absence does not remove scientific authority, author/reviewer attribution, retained holds, exact-version decisions or the 91 reconstruction-origin references in the scientific projection.

## 4. Original witnesses and exact evidence

The original-text layer contains **38,046 stored witness rows**, totaling **23,010,299 bytes**, across all 19,208 registered sources. The count distinguishes witness kinds, not necessarily different text: many paired rows are byte-identical.

| Kind | Rows |
|---|---:|
| `registered` | 19,208 |
| `canonical` | 18,835 |
| `historical_local_archival_acceptance` | 3 |

Every selected record's `document.source_version.sha256` resolves to an exact stored original with the matching byte length. A matching original need not be named `canonical`: 91 current reconstructed records bind to saved `registered` originals.

Exact witness binding groups across all 18,412 stored records:

| Matching stored original kinds | Records |
|---|---:|
| Registered and canonical | 17,452 |
| Canonical only | 866 |
| Registered only | 91 |
| Registered, canonical and archival | 3 |

Of 18,835 canonical/registered pairs, 17,969 are byte-identical and 866 differ. In those 866, all whitespace-token sequences agree; 822 become equal after outer whitespace stripping, and the remaining 44 after stripping plus CRLF→LF normalization. The variants remain separately preserved. Physical line counts can differ, so lexical equivalence **does not authorize interchanging evidence coordinates**.

To recover the correct witness with the reader, inspect `record['document']['source_version']['sha256']`, enumerate `Graph.rows('originals', source_id)`, select the matching SHA and call `Graph.original(source_id, kind)`. The `original` command's default registered witness is convenient but not automatically the canonical evidence witness.

## 5. Review, authority and retained dispositions

The source ledger preserves version-bound author/reviewer provenance, decisions, delivery status, audits, holds and resolutions. Reviewer labels are actual pipeline-agent provenance, not evidence of external human Assyriological peer review.

The snapshot records **16,610 exact-current accepted decisions** and the same number of delivery records. Delivery status was 11,512 handed off, 5,021 ready and 77 revoked. Delivery status does not substitute for scientific authority or a later audit disposition.

Exactly **623 sources** use the authorized author-self-check route:

* 367 author-finalized;
* 15 cloud-maintenance finalized;
* 241 local-author-finalized.

Their bin provenance is 607 user-requested-research623 plus 16 local623; it is not 623 additional local-bin records. These have no separate current reviewer decision. This specific authority must not be generalized to the rest of the corpus or described as independent external review.

Audit provenance is retained for 2,585 sources: 2,532 paused-unverified, 47 cleared, 6 unverified. There are 1,155 partition-hold provenance entries, including 26 with cleared audit status. A historical hold-field occurrence is not sufficient to infer a present exclusion; inspect its exact version, applicable decision and resolution. Conversely, an accepted state is not permission to erase a later bounded hold.

Thirteen recovery-hold entries preserve their actual histories. Ten have explicit resolution records bound to the current accepted version/decision. Three (`P112859`, `P112877`, `P116040`) retain older held hashes different from their current accepted scientific heads, without a separate recovery-hold-resolution entry in those ledger fields. Report both facts rather than treating them as automatically excluded or explicitly cleared.

**91 reconstruction-origin records** retain their missing-history/recovery lineage while having current canonical payloads and exact saved original witnesses. They are not 91 absent records, and their lineage must not be silently rewritten as an independently reviewed original extraction. Broader recovery-link items remain provenance, not extra records.

The single explicit documentary alias is **P142584→P500235**, marked documentary-only with `identity_merge=0`. It does not add a duplicate scientific record or perform a historical identity union.

## 6. Assembled graph provenance

The preserved **evidence** connected representation expands exact canonical JSON into addressable typed nodes, including components without local IDs. Its all-stored totals are:

| Representation | Count |
|---|---:|
| Explicit-ID canonical objects | 3,172,743 |
| Typed ID-less components | 1,900,266 |
| Connected nodes | 5,073,009 |
| Containment incidences | 4,063,006 |
| Schema-aware local-reference incidences | 4,620,436 |
| Total incidences | 8,683,442 |
| Separately labelled convention edges | 4,422 |
| Candidate-layer nodes | 24,520 |
| Cross-record documentary citations | 106 |
| Identity unions | 0 |

The source database also had a direct explicit-ID/reference index: all-stored 3,172,743 objects/4,546,775 reference occurrences, current 3,172,580/4,546,493. Those are **alternative index denominators**, not extra nodes to add to the connected graph. Schema-aware incidences include additional typed links such as important-uncertainty references; this explains why the reference counts differ.

The clean graph corrects 91,835 node schema-kind labels through exact version/pointer/old-label checks. This is a typed-navigation repair, not a change to canonical JSON, incidence content, evidence, acceptance or historical interpretations. The graph certificate records the correction rule and unchanged totals.

The evidence export separately preserves accounting, temporal, alternatives, count bounds, vocabulary hubs and documentary citations. All are labelled derived/conditional or representational as appropriate; none upgrades scientific authority. Ordinary graph methods rebuild from the same default as record/search rather than asserting every cached/candidate evidence edge. Historical cached proofs remain advanced evidence, not allegedly recomputed default consequences.

### Documentary citations: two independent resolution axes

There are **106 cross-record citations**, of which **101** resolve to an exact selected canonical target and **5** have no matching selected canonical target. The five-row unresolved dataset repeats those five boundaries; it does not add five more citations. **All five cited original witnesses are available exactly.** Three lack selected canonical target payloads; two selected targets bind a different original version. No substitution of the current head is made.

`Graph.citation_links(source_id=None)` reports each citation once, separating `canonical_resolution`/`resolved_canonical_target` from `original_witness`. `Graph.original_witness_links(source_id,source_version)` checks exact source ID, original SHA, bytes and encoding. An unresolved canonical target therefore does not imply missing original evidence.

### Historical predecessors versus missing-history lineage

**4,553 selected records declare a canonical predecessor**, and all 4,553 referenced predecessor payloads are outside this selected export. `Graph.predecessor_link(source_id)` reports `historical_payload_not_exported`, not an invalid binding or missing original. These are not the separate **91 reconstruction-origin records**, which are present current payloads with exact originals and retained missing-history provenance.

`Graph.resolve_record_pointer(version_hash,pointer='',source_id=None)` resolves only an exact selected version. It does not fall back to another head. `Graph.ledger_handle(source_id)` supplies a portable `data/sources` ledger handle and retains old SQL locator wording only as historical provenance. Source/version matching, documentary availability and scientific authority remain separate axes.

## 7. Verification and reproducibility

From the repository root:

```sh
python girsu.py verify
python girsu.py source P100144
python girsu.py pointer P105740 /entries/2/membership
python girsu.py citation-links P131513
python girsu.py ledger-handle P100144
python girsu.py predecessor-link P100144
```

The reader verifies manifest/index/partition bindings, default-record content and policy fingerprint, and exact canonical/original hashes when advanced evidence bytes are requested. Full `verify` checks every file against the shipped manifest. It does not write to the dataset or call a network service. Consumer tests and scientific-policy scope are described in [validation](VALIDATION.md).

A small independent canonical-byte check is:

```python
import hashlib
from girsu import Graph

g = Graph()
row = g.record_envelope('P100144')
assert hashlib.sha256(g.evidence_record_bytes('P100144')).hexdigest() == row['version_hash']
```

The graph's validation certificates cover all canonical node pointers, incidence reference/target pointers, shared hub/owner/provenance links and explicit version/pointer pairs in the derived data. All 156 accounting proof locators resolve through the shipped partition/index mapping. These are mechanical/data-binding checks, not external human peer review of every ancient interpretation.

Schema and semantic conventions are shipped under [`docs/schema/`](schema/). The retained filename `SOURCE_RECORD_SCHEMA_V1.proposed.json` is historical naming; its role in this release is the source-record structural contract, read with the semantic rules and runtime refinements. `IDENTITY_CONVENTIONS_V1.md` documents **original source-local occurrence/coreference/kinship semantics**, not the excluded later global identity-reconstruction results.

## 8. Reading the numbers responsibly

Unless explicitly marked all-stored/export, content counts use 18,409 exact-current canonical records. An object count measures serialized scientific objects at a declared path; a source count measures distinct documents containing them. Sources can appear in several categories. Candidate branches, supporting context and archival records are not automatically part of an adopted-current count.

No cross-document grand total, historical headcount, normalized chronology, modern unit conversion, global identity closure or new event history is implied by this export. The purpose is to make the original evidence-rich record and its explicit derivations accessible, auditable and useful.
