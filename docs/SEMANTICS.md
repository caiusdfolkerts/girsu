# Semantics of the single default

## 1. One value with its context

`Graph.record`, `pointer`, `research_value`, `research`, `search`, `search_all`, `search_page`, `connected`, `neighbours`, `typed_nodes` and `typed_relations` consume the **same precomputed default**. A branch-qualified field can be selected or held null. Ordinary queries do not return parallel canonical/working values or silently search rejected alternatives as facts.

This is a data foundation, not a supplied historical theory, research agenda or category ontology. It preserves the original source-local structures and native vocabulary. No new semantic relation reclassification is performed; the existing coarse codes and native labels remain the contract.

`research_value(source_id,pointer)` adds:

* one `value`, source ID, original record `version_hash`, original witness hash and exact pointer;
* applicable `qualifications`, with resolved target pointers and reasoning/evidence references;
* `branches`, containing decision status, targets, evidence/option pointers, dependencies and applicable hashes;
* distinct `has_branches`/`has_ambiguity` flags and counts, diagnostics and bounded-policy coverage metadata;
* the separate default-record hash from the materialized row; the reader also verifies the release policy fingerprint in the default index.

The preserved `branches` list contains labelled annotations, not only proven branch sets:

| Field | Exact meaning |
|---|---|
| `is_identified_branch`, `annotation_kind` | On each annotation: a branch/choice set versus qualification-only context. |
| `identified_branch_count`, `has_branches` | Count of identified branches; boolean is true only when that count is positive. |
| `qualification_annotation_count` | Count of the nonbranch qualification annotations. |
| `has_ambiguity` | Any preserved scoped annotation, or an applicable ambiguous/unresolved qualification. |

Field access recalculates flags/counts over overlapping targets and applicable qualifications. A selected but qualified branch can remain flagged. Neither flag is a probability, certainty judgment or complete prose-analysis certificate. A field can have `has_branches:false` yet `has_ambiguity:true`; well-supported qualifications can also exist without either flag. Context on another field or linked object must not be indiscriminately transferred to the field being used.

An actual evidence field beneath a held-null ancestor has one default null, with `value_status='null_due_to_unresolved_ancestor'`, the ancestor pointer and normal qualification/branch context. A typo is not converted into a null field: invalid source paths still fail. Strict `pointer` traversal can raise beneath a null; prefer `research_value` when an annotated field result is needed.

## 2. Source uncertainty versus machine abstention

The source record can say a reading is ambiguous, unresolved, restored, queried or well-supported. The bounded default policy separately asks whether a preference can be established by its supported rules. `machine_reason_not_established` means **the machine did not establish the preference**, not that the ancient text or its interpreter supplied none.

All 3,537 structured alternative sets were visited. Twenty-six typed choices were selected, one bounded prose choice was selected, and 3,511 typed sets were held. Alternative count, selected decision count, source count and changed field count are not interchangeable. The 9,512 prose signals form a review queue, not additional proven branches; no universal prose-understanding claim is made.

The materialized context also retains **10,601 `source_qualified_not_machine_resolved` annotations**. These preserve a source qualification's scope where it has no established machine selection. They are not another 10,601 parsed/proven alternatives and do not instruct blanket nulling of unrelated fields.

Selection does not follow singleton option count, array order, a coarse support label, source ID or a mechanical edition-priority rule. Each correlated option must be justified as a whole. Unproved dependencies, conflicting/overlapping bundles and joint-world constraints fail closed. A selected restoration retains its original marks and evidence dependence.

Held targets are null in the default; source values and candidate bundles remain reachable through advanced evidence pointers. Qualifications without a machine selection do not justify erasing unrelated intact values. Missing optional fields, explicit nulls, empty collections and zero remain different representations.

## 3. The required examples

### P102673: restoration without forced balancing

The encoded restored counts **1,1,2,2** have their existing numeric evidence anchors checked against the exact bound original. They support the encoded conditional schedule **177**, rather than only the readable-details subtotal 171. The gap of six does not prove those individual readings; their textual support is independent of balancing.

The written principal remains **217** and its discrepancy remains **20**. Calculated paths totaling **237** remain diagnostics. The policy does not replace a principal to minimize faults, make two accounts agree, or manufacture missing personnel/events.

### P105740 and P204204: keep the source-specific interpretation

P105740 retains the supported administrator title at `/relations/4/value`, native `sza3-[tam]`, for its restored seal owner. The edition's DI[KU5] judge reading remains a credible alternative in source reasoning. P204204 is a separate case: its native `di?-ku5?` already has a queried primary judge interpretation while its coarse canonical code is unclassified. These are not a universal rule that an edition wins or that `unclassified` means unknown content. Neither creates an enum, a title taxonomy, external scholarly-consensus claim or historical identity with a governor.

P105740 also preserves actual arithmetic membership **1+1=2** across tablet/envelope witnesses. That is a supported operand scope, not permission to count the same represented sheep again for each witness.

## 4. Quantities and dependencies

Numbers are exact rational strings, for example `"1/2"`; null is never zero. Written expressions preserve term order, native units, unknown positions and editorial deletions. A measurement's subject, function, dimension, components, standard, population and time basis are distinct fields.

Native vectors keep unit components separate. A standard label does not provide a conversion factor. A rate denominator is not the total population; absent time basis is not “per day.” Relative-work equivalents are not automatically observed hours. No cross-document grand total is computed by the foundation.

Explicit canonical recipes retain calculation/reconstruction modes and ordered dependencies. An affected derived cache must be recomputed from supported default premises or held null; an old result is not a fresh observation. Complete, partial and unresolved memberships differ. Repeated representations and overlapping operand scopes must not be added twice. The default diagnostics expose recomputation/withholding; preserved cached accounting artifacts are advanced evidence, not advertised as new default consequences.

## 5. Three kinds of connection

* **Containment:** one JSON object contains another. This is syntax, not identity or automatic semantic inheritance.
* **Source-local assertion:** participant roles, kinship, title, affiliation, seal ownership, local coreference, membership, summaries and balances. Their endpoints, evidence and scope remain explicit.
* **Documentary/vocabulary connection:** supporting witnesses, exact shared native terms and controlled concepts. Equality permits retrieval; it does not merge historical people, events, physical goods, standards or instants.

Multi-party assertions stay n-ary objects with typed incidences. Entries are not automatically transactions; mentions are occurrences, not people counts. Local IDs such as `m1` are unique only within the record. Supported source-local kinship/coreference is retained even though later global identity reconstruction is excluded.

Default graph connectivity is rebuilt from default object/reference values. A held-null endpoint must not leave an asserted edge to its rejected source value. Candidate branches and historical convention edges remain evidence-only. Stable keys are `(source_id, original record version, pointer)`; node indices are presentation-local. Some source targets may lie under a null default object; the graph reports that disposition rather than inventing an endpoint.

## 6. Native labels and time

All **98,928 current unclassified relations** have populated source `native_label` values. Those labels remain intact in the preserved canonical evidence, with their precise endpoints and evidence. Default labels remain searchable unless an explicit unresolved branch makes the field null; the original label is then accessible at its evidence pointer. Some are explanatory English labels, not literal Sumerian. The release does not replace them with speculative semantic categories. Fine native item/title/unit distinctions likewise remain accessible beyond coarse enums.

Calendar formulas, months/days, relative dates, intervals, durations, occurrences and applicability roles stay distinct. A seal ruler, oath ruler, reference year and body date are not automatically one chronological assertion. Equal calendar descriptions do not prove the same historical instant. No absolute chronology or missing date component is invented.

## 7. Search, scope and evidence

Search is literal, case-insensitive scalar retrieval of the default, not synonym, transliteration or identity normalization. Ordinary scalar search excludes reasoning, qualifications and branch-evidence metadata so an alternative mentioned only in explanatory prose is not returned as an asserted default fact. Explicit evidence inspection remains available when that material is needed.

Bounded `search_page` work is limited by sources and matches. Preserve the exact cursor; it binds release/query/population and position. An empty page can precede later results. Only `exhausted`/a null next cursor indicates completion. A limited result is not a denominator.

Evidence coordinates bind the exact original SHA, not whichever witness is named registered or canonical. Physical lines are one-based; token and optional Unicode-code-point subtoken bounds are zero-based/end-exclusive. Follow qualifications to reasons and evidence anchors without treating a shared anchor as an independent observation each time it is cited.

Advanced `inspect` is the explicit comparison route; it is not an ordinary second reading. A child that exists only under a restored/default object can have `default_pointer_exists:true` and `evidence_pointer_exists:false`; this does not pretend that an absent raw child was a written null. A pointer absent from both representations still fails. Historical predecessor and documentary-support links distinguish absent historical payloads from available original evidence. These distinctions are detailed in [provenance](PROVENANCE.md).
