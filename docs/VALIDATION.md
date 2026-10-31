# Validation and release scope

Validation binds exact data, a single default, portable access and explicit scope. It is not a claim that a machine has interpreted every source sentence or that every ancient interpretation received external human peer review.

## 1. Checks to run after obtaining the release

From the directory containing `girsu.py`, `data/`, `tests/` and `MANIFEST.json`:

```sh
python girsu.py verify
python -m unittest discover -s tests
```

Use Python 3.11+ and its standard library. The reader/tests do not require a database, network connection, parser build, private workspace or the original repository. Keep the manifest with the release: source/default indexes and partitions are verified against it, not trusted merely because a filename exists.

The manifest's own SHA-256 identifies the exact package. The default index also carries a policy fingerprint, which the reader checks before use. Each default row has its own content hash and exact source/version/original-witness bindings. A mismatch fails rather than silently substituting another version or recomputing an unpinned interpretation.

The materialization audit's retained `reader_sha256` identifies the private build/materializer used to create defaults, not the smaller public consumer file. The shipped `girsu.py` is hashed separately by the root manifest. Do not compare those two different implementation artifacts as though they should share a digest.

## 2. Source-evidence checks

The original immutable source database SHA is `b02f70a3c3c01bfe96428e04ce674f19e21dbb620a463dd699034915c644205c`. All 18,412 selected record byte sequences and 38,046 original witness rows were independently hash-checked. Every selected record's original SHA and byte count resolves to an exact stored witness. Canonical/original evidence is not changed by defaulting.

The source denominator is 18,409 current plus three explicit archival-only records. The catalogue-only appendix has 11,048 IDs without saved ATF, disjoint from the 19,208 registered textual sources. Defaults exist for the 18,412 selected source records, not for every catalogue-only or availability ID.

The preserved evidence graph's pointers, reference targets, shared-vocabulary links and all 156 accounting proof locators were mechanically audited. Those checks validate bindings and representation; they do not turn graph incidences into independent historical observations. Historical cached proof datasets are not presented as newly recomputed default consequences.

## 3. Bounded default-policy coverage

The bounded 1.1 pass visited all **3,537 structured alternative sets**, **6,026 options** and **8,425 assignments** across 18,412 stored records. It selected **26 typed decisions**, held **3,511 typed sets**, and selected **one additional bounded prose decision**. Of the 27 selected decisions, **13** used exact source evidence-anchor verification and **14** used supported source-record reasoning alone.

The held typed sets comprise 3,497 cases where the machine did not establish a source preference and 14 unresolved-overlap cases. These counts are sets/decisions, not unusable documents or historical facts. A held field becomes null in the ordinary default, with its evidence and null cause retained. Source ambiguity and machine inability are separately reported.

The defaults additionally preserve **10,601 source-qualified-not-machine-resolved annotations**. These are scoped contextual warnings, not additional proven branches or instructions to null every field sharing a reason.

The wider scan produced **9,512 prose-signal review items** from 246,786 stored reasoning objects. Signals are not proven alternative sets, selected readings or an assertion of complete semantic analysis. Unparsed prose is not universally converted into branches or used as a blanket-null instruction. The policy is a bounded deterministic grammar with explicit anchor/dependency checks, not universal natural-language understanding or a source-ID whitelist.

Existing atomic assignments are accepted only with supported target binding and evidence. Singleton status, option order, inherited support labels and arbitrary confidence do not establish preference. Unproved dependencies, inconsistent bundles, joint-world ambiguity and repeated-witness conflicts fail closed. Evidence verification checks existing candidates and exact anchors; it does not extract new source candidates or choose values to balance totals.

## 4. Required regression behavior

Consumer regression tests and release-command checks exercise the materialized records and actual portable reader, including:

* one default across record, field, scalar-search and graph methods;
* held-null targets retaining branch/qualification/evidence pointers;
* valid source fields beneath null ancestors returning annotated null, while misspelled paths still fail;
* P102673's restored **1,1,2,2** and encoded schedule **177**, with written **217** and discrepancy **20** preserved;
* P105740's supported administrator title, distinct from P204204's primary queried judge interpretation, with no new relation taxonomy or global identity;
* exact rational strings, field-local qualification scope and preservation of source/original bytes;
* current-only access and explicit archival opt-in;
* bounded search/cursor behavior and manifest/default hash/fingerprint enforcement;
* source-local endpoint connectivity without stale asserted edges from held alternatives.

The underlying reviewed policy suites also exercised negation/rejection/hypothetical wording, wrong-target binding, exact numeric anchors, atomic dependencies and repeated-witness protection. Derived refresh was tested against stale expression caches, changed repeated witnesses, transitive rate/time-basis changes and unrelated-cache preservation. Native-standard evidence remains attached to the quantity it supports rather than leaking across unrelated recipes.

These are rule/implementation tests and selected regression fixtures, not fresh expert collation of every original text or independent scientific review credit. See the shipped test output and manifest-bound validation records for the exact final consumer test inventory; do not add test totals from overlapping suites as though they measured different sources.

For the final 1.1 consumer candidate, **17 portable-reader tests and 10 cookbook tests passed**. The documented CLI commands and six source-filtered cookbook recipes were also executed against that same materialized default. These suite counts describe software checks, not additional source records or scientific reviews. Final package integrity is checked again by the manifest verification command after assembly.

## 5. Materialization and portability

Defaults are precomputed data under `data/default_records/`, including 18,409 current and three explicit archival records. The ordinary reader is a small standard-library consumer; it does not run the scientific parser on every query. Source-indexed gzip partitions allow single-source access without loading a corpus-sized list. The final materialization binds its content and policy fingerprint separately from the preserved canonical source hash.

Full scans still take work: prefer source-filtered calls or `search_page` for an interactive first look. An empty bounded page can precede results in later sources. Preserve its exact cursor and check `exhausted`; do not mistake a limited page for a corpus count. No query-latency claim is inferred from an earlier reader or a different machine.

## 6. Documentary and lineage checks

All **106** documentary citations are retained once: 101 exact canonical joins and five unresolved canonical boundaries. All five unresolved cases still have exact original witnesses. Resolver statuses distinguish missing selected canonical payloads from mismatched original versions; they do not fabricate a target.

All **4,553** declared historical predecessor payloads are unshipped in this selected export. Their explicit historical disposition is not a broken current-source link. The **91** reconstruction-origin sources are a different lineage cohort: their current records and originals are present. The documentary alias remains documentary-only, with no identity merge.

Source author/reviewer attribution, the specific 623 author-self-check authority, audits/holds and exact-version resolutions remain provenance. Default selection creates zero independent scientific review credit and clears no hold. See [provenance](PROVENANCE.md) for the original authority denominators.

## 7. What is deliberately not claimed

No new global identity closure, speculative relation categories, absolute chronology, metrological conversion table, cross-document economic grand total or external scholarly-consensus ranking is supplied. Original native labels and source-local relations remain intact and searchable. The data exposes one practical default, null where appropriate, with the pointers needed to inspect its evidential basis.

## Known candidate-encoding issues

`data/KNOWN_ENCODING_ISSUES.json` indexes 13 options in eight qualification sets whose candidate reference types cannot be fully validated. Their original assignments and exact diagnostics are retained. These options are not selected as defaults, but encoding trouble does not scientifically disprove an interpretation. This is separate from missing originals, current-record coverage, and historical-version availability.
