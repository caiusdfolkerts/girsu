# Validation

Validation addresses three questions: whether the released bytes match their recorded bindings, whether the portable reader handles them consistently, and whether the default policy stays within its stated rules. These checks do not establish that every source sentence has been interpreted, that every interpretation is correct, or that the corpus has received external human peer review.

## Checking a downloaded release

From the directory containing `girsu.py`, `data/`, `tests/`, and `MANIFEST.json`, run:

```sh
python girsu.py verify
python -m unittest discover -s tests
```

The reader and tests use Python 3.11 or later and its standard library. They require no database, network connection, parser build, private workspace, or original repository. Keep `MANIFEST.json` with the data: indexes and partitions are verified against it rather than trusted because their filenames exist.

The manifest's own SHA-256 identifies the package. The default index carries a policy fingerprint checked by the reader, and each default row has a content hash and exact source, version, and original-witness bindings. A mismatch causes failure; the reader does not silently substitute another version or recompute an unpinned interpretation.

The materialization audit's `reader_sha256` identifies the private build/materializer that produced the defaults. It does not identify the smaller public consumer file. The shipped `girsu.py` has its own hash in the root manifest, so those two implementation artifacts should not be expected to share a digest.

## Preservation of source evidence

All 18,412 selected canonical byte sequences and all 38,046 original-witness rows were independently hash-checked against the export bindings. Every selected record's original SHA and byte count resolves to an exact stored witness. Default selection changes neither canonical nor original evidence.

The immutable source database is identified by:

```text
b02f70a3c3c01bfe96428e04ce674f19e21dbb620a463dd699034915c644205c
```

The selected population is 18,409 current records and three archival-only records. It is not the entire catalogue. The 11,048 catalogue-only IDs without saved ATF are disjoint from the 19,208 registered textual sources. Defaults exist for the 18,412 selected records, not for every catalogue or documentary-availability ID.

The preserved evidence graph's pointers, reference targets, shared-vocabulary links, and all 156 accounting proof locators were mechanically audited. These checks establish that the representation is bound to its evidence. They do not make graph incidences independent historical observations, and historical cached proofs are not presented as newly recomputed consequences of the default.

## Scope of the default policy

The bounded 1.1 pass examined all 3,537 structured alternative sets, containing 6,026 options and 8,425 assignments, across the 18,412 stored records. It selected 26 typed decisions and held 3,511 typed sets. It also selected one bounded prose decision. Of the resulting 27 selected decisions, 13 used exact source evidence-anchor verification and 14 relied on supported source-record reasoning alone.

Among the held typed sets, 3,497 had no source preference established by the machine and 14 had unresolved overlaps. These are counts of sets and decisions, not unusable documents or historical facts. A held field is null in the ordinary default, while its evidence and the cause of the null remain available. The annotations distinguish ambiguity in the source from the machine's inability to resolve it.

Defaults also retain 10,601 `source-qualified-not-machine-resolved` annotations. These are contextual warnings with a defined scope, not further proven branches or instructions to null every field sharing a reason.

A wider scan produced 9,512 prose-signal review items from 246,786 stored reasoning objects. A signal is not a proven alternative set, a selected reading, or evidence of complete semantic analysis. Unparsed prose is neither universally converted into branches nor used to null fields indiscriminately. The policy uses a bounded deterministic grammar with explicit anchor and dependency checks; it is not universal natural-language understanding or a source-ID whitelist.

Existing atomic assignments are accepted only when their target binding and evidence are supported. A singleton option, its position, an inherited support label, or an arbitrary confidence value does not establish preference. Unproved dependencies, inconsistent bundles, joint-world ambiguity, and repeated-witness conflicts fail closed. Evidence verification tests existing candidates against exact anchors; it does not extract new candidates or choose values merely to balance totals.

## Reader and policy regressions

The consumer regressions test that record, field, scalar-search, and graph methods expose the same materialized default. Held-null targets must retain their branch, qualification, and evidence pointers. A valid source field beneath a null ancestor must return an annotated null, whereas a misspelled path must still fail. Tests also cover exact rational strings, field-local qualification scope, preservation of source and original bytes, current-only access with explicit archival opt-in, bounded search and cursors, and enforcement of manifest, default-hash, and policy-fingerprint checks. Source-local graph endpoints must remain connected without asserting stale edges from held alternatives.

Two fixtures preserve particularly specific distinctions. For `P102673`, the tests retain the restored **1,1,2,2** and encoded schedule **177**, alongside written **217** and discrepancy **20**. For `P105740`, they test the supported administrator title separately from `P204204`'s primary queried judge interpretation. Neither fixture introduces a new relation taxonomy or global identity.

The underlying reviewed policy suites also tested negation, rejection, and hypothetical wording; wrong-target bindings; exact numeric anchors; atomic dependencies; and repeated-witness protection. Derived-refresh tests covered stale expression caches, changed repeated witnesses, transitive rate/time-basis changes, and preservation of unrelated caches. Native-standard evidence must remain attached to the quantity it supports rather than being applied across unrelated recipes.

For the final 1.1 consumer candidate, 17 portable-reader tests and 10 cookbook tests passed. The documented CLI commands and six source-filtered cookbook recipes were executed against the same materialized default. Final package integrity is checked again after assembly by manifest verification.

These results concern implementation rules and selected regression fixtures. They are not fresh expert collations of every original text and do not confer independent scientific review credit. The shipped test output and manifest-bound validation records give the exact final inventory. Counts from overlapping suites must not be added as if they represented different sources or scientific reviews.

## Materialization and portable access

The defaults in `data/default_records/` are precomputed data: 18,409 current records and three explicit archival records. The ordinary reader consumes them rather than running the scientific parser for each query. Source-indexed gzip partitions permit single-source access without loading a corpus-sized list. Default content and its policy fingerprint are bound separately from the preserved canonical source hash.

Full scans still require work. For an interactive first look, use source-filtered calls or `search_page`. An empty bounded page can occur before matching results in later sources; preserve its exact cursor and check `exhausted`. A limited page is not a corpus count. Performance observations from another reader or machine do not establish query latency for this release.

## Documentary links and review lineage

The release retains each of the 106 documentary citations once. Of these, 101 join to an exact selected canonical target and five remain unresolved at the canonical level. All five unresolved cases still have exact original witnesses. Resolver statuses distinguish an absent selected canonical payload from a selected target bound to a different original version; no replacement target is fabricated.

All 4,553 declared historical predecessor payloads are outside this selected export. Their explicit historical disposition is not a broken current-source link. The 91 reconstruction-origin sources form a separate lineage cohort: their current records and originals are present. The documentary alias remains documentary-only and performs no identity merge.

Author and reviewer attribution, the specific authorization for 623 author-self-check sources, audits, holds, and exact-version resolutions remain part of the provenance. Default selection adds no independent scientific review credit and clears no hold. [Provenance](PROVENANCE.md) gives the authority populations and explains why accepted decisions, delivery status, and later audit dispositions must be read separately.

## Known candidate-encoding issues

[`data/KNOWN_ENCODING_ISSUES.json`](../data/KNOWN_ENCODING_ISSUES.json) identifies 13 options in eight qualification sets whose candidate reference types cannot be fully validated. Their original assignments and exact diagnostics remain available. None of these options is selected as a default, but an encoding defect does not scientifically disprove an interpretation. These issues are separate from missing originals, current-record coverage, and the availability of historical versions.

## Limits of the release

The release supplies no new global identity closure, speculative relation categories, absolute chronology, metrological conversion table, cross-document economic grand total, or ranking of external scholarly consensus. Native labels and source-local relations remain intact in the preserved evidence; ordinary default labels remain searchable unless explicitly held null, as documented. The ordinary interface offers one practical default, including nulls where required, with pointers back to its evidence. Its consistency and reproducibility should not be mistaken for scientific completeness.
