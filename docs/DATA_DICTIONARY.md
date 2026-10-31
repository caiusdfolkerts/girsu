# Data dictionary

This repository represents the original Girsu **source graph** through one materialized default, with exact canonical/original evidence separately preserved. The normative source-record model is `ur.source_record.v1`; the default is a projection of it, not a second competing consumer reading. A field described below is a source-schema capability, not a promise that every source populates it. All content inventories explicitly measure preserved canonical evidence, not the number of nonnull fields in the default.

See [README](../README.md) for access, [semantics](SEMANTICS.md) for interpretation and worked examples, and [provenance](PROVENANCE.md) for exact release bindings and denominators.

## 1. Exported populations and envelopes

The data directories use gzip-compressed UTF-8 JSON Lines. A JSONL row is one independent JSON value; compression partitions are transport boundaries, not historical archives. Consult each dataset's manifest/index rather than assuming the same partition or line identifies the same source in another dataset.

### Ordinary default envelope — `data/default_records/`

The source index selects a gzip partition and zero-based row. One row binds one source/version and contains `schema`, `source_id`, `version_hash`, `original_hash`, `default_record_sha256`, `record`, `branches`, `diagnostics`, `coverage`, `research_population`, current status and associated context. There are 18,409 current defaults and three explicitly archival defaults; ordinary access excludes the archival three.

`record` is the one consumer reading, including held-null fields. `version_hash` identifies the original immutable canonical payload; `default_record_sha256` identifies the compact sorted-key UTF-8 serialization of the default record. They are different bindings and must not be interchanged. The index policy fingerprint must match the portable reader; partition hashes, source/version and original-witness bindings are checked before access.

| Default-envelope field | Meaning |
|---|---|
| `schema` | `ur.default_record.v1` for the materialized row. |
| `source_id`, `version_hash`, `original_hash` | Documentary source, exact canonical-byte version and exact bound original witness. |
| `record_canonical_json_sha256` | Digest of the parsed source object under compact sorted-key JSON serialization; not a substitute for the original raw-byte `version_hash`. |
| `default_record_sha256` | Digest under that serialization contract of the one default `record`. |
| `record` | Default structured document, including applicable nulls and branch-evidence pointers. |
| `branches`, flags and annotations | Identified choice/context metadata; interpreted with the flag contract below, not a confidence score. |
| `diagnostics` | Conflicts, affected recipe recomputation/withholding and other explicit default-processing dispositions. |
| `coverage` | Bounded default-policy coverage, distinct from the source extraction scope in `record.document.coverage`. |
| `current`, `research_population` | Exact current selection versus explicit archival inclusion. |
| `canonical_mutated`, `scientific_review_credit` | False and zero respectively; defaulting does not rewrite or independently review the source. |
| `identity_scope`, `evidence_accessor`, `layer` | Source-local scope, advanced evidence navigation and explicit default value layer. |

`Graph.research_value(source_id,pointer)` returns `value`, `json_pointer`, source/version/original binding, applicable qualifications, labelled `branches` annotations, `has_branches`, `has_ambiguity`, counts, diagnostics and coverage. Metadata carries targets, selected/held status, null cause, dependencies and evidence/option pointers and hashes where applicable. It does not provide another default value. `Graph.research` uses `record` instead of `value` for the whole document. `iter_records` streams detached default envelopes with source-level context; it does not calculate field-applicable qualification lists.

Each preserved `branches[]` annotation has `is_identified_branch` and `annotation_kind` (`branch` or `qualification`). `identified_branch_count` counts only the former; `qualification_annotation_count` counts the latter. `has_branches` means identified count >0. `has_ambiguity` means the scope has any preserved annotation or an applicable qualification marked ambiguous/unresolved. Field access recalculates these over overlapping targets. Neither flag is a probability or complete prose-analysis certificate. The bounded policy's `machine_reason_not_established` is distinct from source-level ambiguity or absence. See [semantics](SEMANTICS.md).

For an actual source field beneath a held-null default ancestor, the annotated accessor returns null with `value_status='null_due_to_unresolved_ancestor'` and `ancestor_pointer`, retaining applicable context. A misspelled/nonexistent source field still fails. `pointer` remains strict traversal; do not confuse that traversal failure with missing source evidence.

### Advanced canonical evidence envelope — `data/records/`

| Field | Meaning |
|---|---|
| `record_no` | Integer key in the source snapshot; an index key, not an ancient identifier. |
| `source_id` | Documentary/catalogue ID, for example `P100144`. |
| `version_hash` | SHA-256 of the **exact UTF-8 bytes** in `record_json`. |
| `record_json` | A JSON **string** containing the unchanged canonical evidence. Advanced `evidence_record_bytes` preserves its exact UTF-8 bytes; `evidence_record` parses it. Ordinary `record` returns the single default instead. |
| `original_hash` | Exact original-text witness binding. The canonical `document.source_version` also supplies its SHA and byte length. |
| `current` | Whether this selected payload equals the source registry's exact current version pointer. |
| `origin` | Retained origin of the selected scientific payload. |
| `gp_binding` | Retained scientific-admission binding where applicable; not another independent canonical record. |

There are **18,412** stored selected records: **18,409 current** and **3 archival-only**. `source_id` is unique in this selected population; this is not an inventory of every historical revision. Archival-only sources are `P110939`, `P111261`, `P111282`, all letters.

### Source envelope — `data/sources/`

`source_id`, `current_version_hash`, `canonical_state`, `coverage_status` and `ledger` retain the documentary registry and a scientific provenance projection. Source presence, current-payload presence, acceptance, coverage and retained audit/hold disposition are distinct dimensions. The ledger is not a new historical assertion layer.

### Original envelope — `data/originals/`

`source_id`, `kind`, `sha256`, `original_bytes_b64` preserve exact original bytes. Decode base64, verify SHA-256, then decode UTF-8 to inspect text. There are **38,046 stored witness rows** for **19,208 sources**: 19,208 `registered`, 18,835 `canonical`, and 3 `historical_local_archival_acceptance`. These are not 38,046 distinct texts: 17,969 registered/canonical pairs are byte-identical. Use the witness matching the record's `source_version.sha256` when resolving evidence spans; the default registered witness is not always that binding.

### Catalogue envelope — `data/catalogue/`

`source_id` and `metadata` preserve the **11,048 catalogue-only/no-ATF** documentary appendix. The full documentary universe is **30,256 IDs** when these are combined with the 19,208 ATF-present registry sources in `data/sources/`. Catalogue-provenience and period labels are not place mentions or adjudicated event dates. No-ATF means no saved ATF text in this documentary appendix; it does not mean a blank canonical record exists.

`data/availability/`, `data/aliases/` and `data/admission/` retain documentary availability, explicit documentary alias/disposition and scientific-admission provenance separately. They must not be added to canonical-record counts.

## 2. Canonical record conventions

The following field dictionary describes the preserved source model. Default fields retain its meanings, but a held branch can replace a target with null and alternative payloads are replaced by `branch_evidence` pointers. Do not validate a default projection as though it were the unchanged canonical artifact or hash it against the original version hash. Source-schema requirements and current default-population measurements are different contracts.

The root has six required sections: `document`, `entries`, `mentions`, `relations`, `qualifications`, `reasoning`. The optional seventh section is `supporting_sources`.

* IDs are local to the enclosing record. The same literal `m1` in two sources identifies two different stored objects.
* An ID-bearing object's identifier is unique throughout that record, including candidate and supporting-context objects.
* Stable external addressing requires the immutable `version_hash` plus local ID or exact JSON pointer.
* Missing optional key, explicit `null`, empty array and an empty string are not interchangeable.
* Required nullable fields remain present. A material withheld interpretation has a scoped qualification; structural inapplicability is distinguished by the validator.
* Exact rational numbers are strings, such as `"4"`, `"1/3"`, `"-2"`. They are reduced; no floating-point/decimal approximation is implied.
* Unknown structural keys are rejected by the canonical schema. An `other` or `unclassified` code retains native content rather than permitting arbitrary new structure.

## 3. Document envelope

| Field | Contract and interpretation |
|---|---|
| `schema` | Required literal `ur.source_record.v1`. |
| `id` | Required local document ID `d1`. |
| `source_id` | Required documentary ID. |
| `source_version` | Required `{sha256, bytes, encoding}` binding to the entire original; encoding is `utf-8`. |
| `edition` | Required string or null; a source designation, not a global identity key. |
| `revision` | Required integer ≥1. |
| `supersedes` | Required exact predecessor `{source_id, revision, sha256, bytes}` or null. Revision 1 has null. A predecessor reference does not require every earlier payload to occur in this selected export. |
| `document_type` | Required genre code or qualified null. Actual current values are listed below. |
| `parts` | Required documentary/physical part objects. |
| `evidence` | Required interned exact evidence anchors. |
| `dates` | Required temporal-object collection. |
| `purposes` | Required purpose-object collection. |
| `coverage` | Required extraction coverage object. |
| `important_uncertainty` | Required sorted unique qualification-ID index of material ambiguous/unresolved content. It is a navigation index, not a probability score. |

Genres in the preserved current canonical evidence:

| Genre | Records |
|---|---:|
| `account` | 8,979 |
| `receipt` | 3,494 |
| `other` | 2,434 |
| null | 1,301 |
| `expenditure` | 1,090 |
| `personnel_list` | 325 |
| `legal_record` | 321 |
| `letter` | 233 |
| `inventory` | 232 |

`other` and null-genre records can contain extensive positive historical content. There is no separate royal genre code; royal material appears in seal legends, titulary, affiliations, date formulae, standards and body assertions.

## 4. Parts, coverage and evidence

### Parts

`{id, kind, parent_id, line_ranges}`. Actual kinds are `tablet`, `envelope`, `seal`, `composite_seal_legend`, `block`. `parent_id` is a part ID or null; part parentage is acyclic. `line_ranges` consists of `{start,end}` physical-line intervals, start inclusive/end exclusive. A child's ranges fit within its parent's. One source can therefore contain multiple documentary witnesses; a source ID is not necessarily one physical tablet.

### Evidence

An evidence object is `{id, spans}` with one or more ordered, nonoverlapping spans. Each span has:

| Field | Coordinates |
|---|---|
| `line` | One-based physical line of the **exact bound original**, including headers, directives, comments and blank lines. |
| `token_start`, `token_end` | Zero-based token positions, end exclusive, after the defined printed line-prefix handling. |
| `character_start`, `character_end` | Optional paired subtoken bounds; Unicode code-point positions within one raw token, end exclusive. Not byte offsets. |

Evidence references point to these interned IDs. An anchor can support several assertions, and an assertion can cite several anchors. Evidence occurrence counts are neither distinct ancient facts nor independent observations.

### Coverage

`coverage` has `status` (`complete` or `partial`) and `gaps`. Complete requires no gaps; partial requires at least one. A gap has `{id,evidence,reason}` with reason `unprocessed` or `not_modeled`. Current records declare complete in 18,322 cases and partial in 87. Complete extraction does not mean the ancient text is intact or every interpretation is certain.

## 5. Entries, actions and applicability links

An entry has required `id`, `part_id`, `kind`, `evidence`. It is a source-local semantic unit, **not automatically a transaction**. Actual entry kinds are `detail`, `group`, `subtotal`, `total`, `balance`, `calculation`.

Optional entry fields:

| Field | Meaning |
|---|---|
| `action` | Addressable predicate `{id,type,state,evidence}`; `native_label` is required for `type=other`. |
| `items` | Nonempty item array or qualified null where examined content is unrecoverable. |
| `measurements` | Nonempty measurement array or qualified null where examined quantitative content is unrecoverable. |
| `membership` | Explicit arithmetic operand scope for recap/balance/calculation entries. |
| `group_members` | Mention/group-entry IDs for a group entry; not numerical addition. |
| `allocation_basis` | `joint`, `per_member` or qualified null. |
| `occurrence` | Anchored ordinal occasion, not a quantity, duration or regnal year. |
| `participants` | Participant applicability links. |
| `places` | Place applicability links. |
| `dates` | Temporal applicability links. |
| `purposes` | Purpose applicability links. |

Links have their own `{id,ref,role,evidence}`. This makes the application of a person/place/date/purpose to an entry separately targetable and qualified.

Participant roles include `source`, `recipient`, `intermediary`, `supervisor`, `custodian`, `witness`, `beneficiary`, `document_party`, `referenced_document_party`, `associated_person`, `unclassified`. Unclassified roles retain a `native_label`. A document party is not necessarily a physical giver or recipient.

Place roles are `location`, `origin`, `destination`, `storage_location`, `reference_location`. Date roles are `document_date`, `entry_date`, `service_period`, `due_date`, `duration`, `reference_date`. Purpose links apply a known purpose through role `purpose`. A link can contain a materially unresolved null target/role with an explicit qualification.

Action type and state are separate. A receipt/issue/return predicate does not by itself imply completion; `intended`, `owed`, `referenced`, `stated` and `source_asserts_completed` preserve documentary force/stage. Native labels and reasons retain finer distinctions than the controlled coarse index.

## 6. Mentions and social referents

`{id,kind,literal,search_form,part_id,evidence}` are required. Kinds are `person`, `unnamed_role_holder`, `collective`, `institution`, `place`, `deity`, or qualified null.

`literal` preserves the selected written occurrence. `search_form` is a conservative retrieval form or null, not a globally resolved entity identifier. A seal owner, a patronymic and an entry recipient may be distinct occurrences even when a supported local relation links them. Counts of mentions are **not counts of people**.

Current populations: 107,941 personal mentions; 5,308 unnamed role holders; 8,095 collectives; 5,818 institutions; 16,137 places; 3,679 deities; 2,451 null-kind mentions. Their sum is 149,429 mention objects.

## 7. Items and native vocabulary

An item has required `id`, `type_id`, `designation`, `native_term_id`.

* `type_id` is a controlled coarse item class, `unclassified`, or qualified null.
* `designation` is exact evidence for the object/population phrase, or null for a contextually represented but unwritten designation.
* `native_term_id` is a generated `atf:` identifier from exact selected token pieces; it is null exactly when designation is null.
* Native-term encoding uses canonical percent-encoded UTF-8. It is not a synonym, commodity-equivalence, historical identity or dimensional conversion key.

Optional `attributes` has closed keys: `species`, `sex`, `material`, `quality`, `status`, `age_class`, `grade`. Attributes retain their own evidence. Lexical values preserve native-term IDs or qualified nulls; ordinal age/grade values can be supported positive integer strings. An animal class is not silently converted to biological age in years.

## 8. Measurements, expressions, quantities and rates

### Measurement

Required: `id`, `subject_ref`, `function`, `evidence`, `expression`, `adopted`. Optional: `derivation`, `geometric_axis`.

* `subject_ref` identifies the item/group-entry measured, or is qualified null.
* Functions are `amount`, `rate`, `duration`, `relative_work`, or qualified null.
* `expression` is the written expression authority or null. A computed non-null adopted result needs an explicit derivation rather than an invented written expression.
* `adopted` is a quantity, a rate or qualified null. It is the canonical record's adopted interpretation, distinct from candidate alternatives and the separate operational working layer.
* `geometric_axis` can distinguish length, breadth, height, depth. It does not turn any length into an inferred area/volume.

### Written expression and terms

Expression: `{id,rule,terms}`. Rules: `native_vector`, `entity_count`, `unresolved`. Ordered terms have `{id,op,number,unit,evidence}` and optional `unit_evidence`, `deleted`.

`op` is `add`, `subtract` or null; `number` is an exact rational string or null; `unit` is a supported unit code, exact native-term ID or null. Editorially deleted terms are retained with `deleted:true` but excluded from evaluation. Unknown positions stay unknown; they are not dropped as zeros.

### Quantity

`{dimension,components,standard_ref}` is required. Dimensions include count, capacity, mass, length, area, volume, time, relative work, ratio, or qualified null. `components` is a nonempty map of unit identity to exact rational string.

Example shape: `{"dimension":"count","components":{"count":"2"},"standard_ref":null}`. A native vector preserves its separate units; do not silently add unlike components.

Optional `native_standard` has `{native_term_id,evidence}` and requires null `standard_ref`: it retains a written standard whose interpreted equivalence is not asserted. Optional `unit_evidence` binds native component keys to their exact evidence. `standard_ref:null` never authorizes an assumed conversion factor.

### Rate

Required `numerator`, `denominator`, `population_ref`; optional `time_basis_ref`. Numerator and denominator are quantity objects. The denominator is the rate basis, not the total population amount. A population reference is source-local; an absent time basis is not implicitly daily. Source-supported geometric denominators can have an inapplicable null population distinct from a missing historical workforce.

## 9. Arithmetic membership and derivation recipes

Membership has `{id,target_measurement_ref,state,member_measurement_ids}`. State is `complete`, `partial`, `unresolved`; unresolved uses null operands, while complete/partial retain their supported unique measurement-ID array. A group of people and the arithmetic membership of a total are different structures.

Recipe has required `id`, `mode`, `operation`. Modes: `calculate`, `reconstruct`. Operations: `sum_members`, `copy`, `add`, `subtract`, `multiply`, `divide`.

* `sum_members` refers to its sole authority `membership_id`; there is no competing duplicated operand list.
* Other operations use ordered `input_measurement_ids`. Copy takes one input, the remaining operations two.
* Subtraction/division preserve first-minus/divided-by-second order.
* Addition/subtraction require compatible units/standards. Multiplication is supported population×rate or ratio scaling, not unrestricted dimensional algebra.
* Division requires compatible scalar quantities and a nonzero divisor.
* Dependencies must be acyclic. An incomplete sum cannot become an unconditional complete total by treating unknown inputs as zero.
* Optional `standard_ref` binds an actually implemented conversion rule; no historical conversion follows merely from the existence of arithmetic.

## 10. Dates, durations, intervals and purposes

Temporal objects have `id`, `kind`, `evidence`, plus a kind-specific shape:

| Kind | Structure |
|---|---|
| Calendar | At least one of `year_formula`, `year_number`, `month_name`, `month_number`, `day`; material uncertainty can be field-specific. Optional `occurrence` is an ordinal within the formula. |
| Relative | `base_ref`, `relation`; relation before/after/during/at_start/at_end. Optional offset has nonnegative rational `value` and day/month/year `unit`. |
| Duration | `measurement_ref` to the one duration measurement authority. |
| Interval | Separate `start_ref`, `end_ref`, each date ID or qualified null. |

A date object exists in the document collection; entry links assert applicability. A seal ruler, oath ruler, reference date, accounting period and body date are not automatically the same chronological assertion.

Purpose objects require `{id,category,native_term,entity_refs,evidence}`. Category is coarse or null; the native phrase and entities preserve the positive interpretation. A purpose's evidence supports the phrase; its entry link supports application to the entry.

## 11. Relations

Every relation has `id`, `type`, `evidence`; each type has its own endpoint/value/member shape. Do not demand unused binary placeholders in a value relation or flatten a group relation into arbitrary pairs.

| Relation family | Meaning |
|---|---|
| `child_of` | Directed child→parent. Does not automatically infer father, sex or a transitive family tree. |
| `spouse_of`, `sibling_of` | Symmetric relations stored in canonical local-ID order; inspect both endpoints. |
| `title`, `person_status` | Bearer plus value object retaining controlled code/null and exact `native_term`. |
| `affiliation` and administrative/service links | Source-local stated connection with its actual typed endpoints and evidence. |
| `seal_owner` | Owner occurrence→seal or composite-seal-legend part. |
| `local_coreference` | At least two supported mention IDs within this source. Original scoped attributes remain intact. |
| `repeated_representation` | Supported entry or measurement members; numerical contribution control requires appropriate measurement-level support. |
| `summarizes` | Recap entry→membership where an explicit link is needed. |
| `discharges`, `balance_of` | Source-local entry/obligation/balance scope; numerical operands remain explicit elsewhere. |
| `unclassified` | Native relation preserved through `native_label` and its typed endpoints/value. Not empty content. |

Optional `scope_refs` limits applicability. No automatic inheritance into every child of a group is implied.

`documentary_correspondence` occurs on four supported repeated-representation relations. It has scope `source_local_tablet_envelope`, one or two `{left_item_id,right_item_id}` pairs and nonempty `context_relation_refs`. It supports these specific documentary witnesses; it is not a universal lexical equation or a cross-source identity merge.

## 12. Qualifications and alternatives

Qualification requires `{id,targets,support,impact,reasoning_ref}`.

* `targets` are `{record_id,field}`. `record_id` identifies the local object; `field` is a relative RFC6901 object-field pointer, not an array-index/wildcard replacement path.
* `support`: `well_supported`, `ambiguous`, `unresolved`; no numerical probability.
* `impact`: nonempty set drawn from `meaning`, `evidence_dependence`, `permitted_use`; not a severity score.
* Optional `null_reason`: `not_written`, `unreadable`, `unresolved` where required for material nulls.
* Optional `reading_marks`: `{evidence_ref,condition}` with damaged/restored/queried/unreadable/editorial correction/editorial deletion conditions.

An alternatives object has `exhaustive` and `options`. Each option has `id`, `assignments` and optional `reasoning_ref`. Each assignment has a declared `target` and schema-compatible candidate `value`. **An option is one atomic correlated bundle**; taking one field from each competing option invents an unencoded reading. `exhaustive:false` means other possibilities remain, even when only one candidate is recorded.

Candidate payloads remain accessible in advanced evidence, not as another ordinary default panel. The bounded policy can select a justified atomic bundle; a held target becomes null with branch-evidence pointers. It does not alter the canonical structure or establish a universal preference from singleton/order/support labels.

## 13. Reasoning and supporting originals

Reasoning requires `{id,evidence_refs,premise_refs,text}`. It preserves a source-specific explanation and explicit local dependencies, not just a confidence label. Optional `supporting_evidence_refs` points into separately bound supporting originals.

A supporting source has `{id,source_id,source_version,evidence}`. The binding is exact; it supplies documentary context, not a merged source identity or permission to import all its assertions. There are 106 such objects in 82 current records.

## 14. Preserved connected-evidence row contract

`data/graph/connected/` preserves one assembled **evidence** row per stored canonical record, available through `evidence_connected`. Its keys are `binding`, `nodes`, `incidences`, `convention_edges`, `qualification_targets`, `candidate_bundles`, `external_record_citations`, `identity_unions`.

Node columns, in order:

1. JSON pointer;
2. local ID or null;
3. schema kind;
4. layer;
5. category.

Incidence columns, in order:

1. from-node index;
2. to-node index;
3. typed role;
4. exact reference pointer;
5. layer;
6. optional resolution class;
7. optional target pointer.

Node identity is the immutable record binding plus pointer. ID-less quantities, spans, target objects and component maps are nodes too. `contains` is syntactic containment, not historical identity or semantic entailment. N-ary assertions retain role-bearing incidences. Candidates, separate convention edges and external documentary citations remain distinguishable; `identity_unions` is empty.

The preserved evidence graph contains **5,073,009 nodes** and **8,683,442 incidences** across all 18,412 stored records. These are an expanded view of the same records, not extra canonical documents and not a frozen count of default-graph nodes.

Ordinary `connected`, `neighbours` and typed retrieval rebuild connectivity from the same default as `record`/search. Nodes use the `research_default` layer; selected/default references are followed, null endpoints are not replaced with old evidence endpoints, and candidate/convention links are not asserted as default edges. Qualifications targeting objects beneath a null default retain their source target/disposition. Stable keys use source/version/pointer, not presentation node indices. See [SEMANTICS](SEMANTICS.md) for scope.

## 15. Preserved current canonical-content inventory

| Canonical path/family | Objects | Records containing content |
|---|---:|---:|
| Entries | 172,723 | 17,757 |
| Mentions | 149,429 | 18,153 |
| Relations | 171,251 | 17,129 |
| Items | 167,028 | 16,357 |
| Measurements | 165,959 | 15,859 |
| Evidence anchors | 872,362 | 18,409 |
| Parts | 23,169 | 18,409 |
| Temporal objects | 23,267 | 14,495 |
| Purposes | 13,777 | 6,677 |
| Qualifications | 251,231 | 18,141 |
| Reasoning objects | 246,756 | 18,141 |
| Derivations | 1,172 | 313 |
| Arithmetic memberships | 4,422 | 1,549 |
| Alternative sets | 3,537 | 1,998 |
| Geometric-axis measurements | 683 | 66 |

These evidence counts exclude the three archival-only records; they do not count populated default fields after machine nulling. Source-presence columns overlap and are not additive. Candidate alternative values are not counted as adopted measurements. There are 933 observed structural paths and 1,220 object key-shapes. The dataset is genuinely heterogeneous: 652 current source records have no entries yet preserve other content, while the largest has 701 entries. Use exact paths, qualifications and counting units rather than treating one flat table as the entire record.
