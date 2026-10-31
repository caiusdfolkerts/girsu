# Data dictionary

The source-record model is `ur.source_record.v1`. Ordinary access returns one materialized default derived from that model; the unchanged canonical records and original texts remain available as evidence. The default is not a second source record or a competing interpretation presented alongside the first.

This reference describes what the schema can represent, not what every source contains. Unless stated otherwise, content counts refer to preserved canonical evidence, before default decisions hold any fields null.

See the [README](../README.md) for access, [semantics](SEMANTICS.md) for interpretation and worked examples, and [provenance](PROVENANCE.md) for release bindings and counting populations.

## Files and exported populations

The data directories contain gzip-compressed UTF-8 JSON Lines. Each row is an independent JSON value. Compression partitions are transport boundaries, not historical archives. Use each dataset's manifest or index to locate a source; a partition number or row position in one dataset does not identify the corresponding source in another.

### Default records

`data/default_records/` contains 18,409 current defaults and three explicitly archival defaults. Ordinary access excludes the archival three. The source index locates each row by gzip partition and zero-based row number.

Each row has schema `ur.default_record.v1`. Its `source_id` identifies the documentary source, `version_hash` binds the exact original canonical bytes, and `original_hash` binds the original-text witness. The `record` field contains the default structured document, including held-null fields and branch-evidence pointers.

Two further hashes describe parsed JSON under compact, sorted-key UTF-8 serialization. `record_canonical_json_sha256` hashes the parsed source object; it does not replace the raw-byte `version_hash`. `default_record_sha256` hashes the default `record`. These bindings are not interchangeable. Before access, the reader checks partition hashes, source/version and original-witness bindings, and that the index policy fingerprint matches the portable reader.

`branches`, flags and annotations describe choices and their context. `diagnostics` records conflicts, affected recipe recomputation or withholding, and other processing dispositions. `coverage` describes the bounded default policy, not the source extraction coverage in `record.document.coverage`. `current` and `research_population` distinguish current selection from explicit archival inclusion.

The remaining metadata makes the layer and its limits explicit. `identity_scope` records source-local scope, `evidence_accessor` identifies advanced evidence navigation, and `layer` identifies the default value layer. `canonical_mutated` is false and `scientific_review_credit` is zero: defaulting neither rewrites the source nor constitutes an independent scientific review.

`Graph.research_value(source_id, pointer)` returns one `value`, its `json_pointer`, source/version/original binding, applicable qualifications, labelled `branches` annotations, counts, flags, diagnostics and coverage. Where applicable, the metadata includes targets, selected or held status, null cause, dependencies, evidence and option pointers, and hashes. It does not supply another default value. `Graph.research` returns the whole document under `record` rather than `value`. `iter_records` streams detached default envelopes with source-level context; it does not calculate field-specific qualification lists.

The `branches` collection includes both identified branches and qualification-only annotations. Each annotation has `is_identified_branch` and `annotation_kind`, whose value is `branch` or `qualification`. `identified_branch_count` counts branches; `qualification_annotation_count` counts qualification annotations. `has_branches` means that the identified count is greater than zero. `has_ambiguity` means that the scope contains a preserved annotation or an applicable qualification marked ambiguous or unresolved. Field access recalculates these over overlapping targets. Neither flag is a probability or a claim of complete prose analysis. In particular, the policy's `machine_reason_not_established` is distinct from a source stating uncertainty or supplying no interpretation.

For an actual source field beneath an ancestor held null in the default, the annotated accessor returns null with `value_status='null_due_to_unresolved_ancestor'` and `ancestor_pointer`, while retaining applicable context. A misspelled or nonexistent source field still fails. `pointer` uses strict traversal, so a traversal error beneath null is not evidence that the source field was absent.

### Canonical evidence

`data/records/` holds 18,412 selected records: 18,409 current and three archival-only. `source_id` is unique within this population. It is a selection of records, not an inventory of every historical revision. The archival-only sources are `P110939`, `P111261` and `P111282`, all letters.

`record_no` is an integer key in the source snapshot, not an ancient identifier. `source_id` is the documentary or catalogue identifier, such as `P100144`. `record_json` is a JSON string containing the unchanged canonical evidence, and `version_hash` is the SHA-256 of that string's exact UTF-8 bytes. Advanced `evidence_record_bytes` returns those bytes; `evidence_record` parses them. Ordinary `record` returns the default instead.

`original_hash` binds the original-text witness. The canonical `document.source_version` also records its SHA and byte length. `current` says whether the selected payload equals the registry's exact current-version pointer. `origin` retains the selected scientific payload's origin, and `gp_binding` retains its scientific-admission binding where applicable; neither adds another canonical record.

### Registry, originals and catalogue

`data/sources/` retains the documentary registry and a scientific provenance projection through `source_id`, `current_version_hash`, `canonical_state`, `coverage_status` and `ledger`. Source presence, current-payload presence, acceptance, coverage, and retained audit or hold disposition are separate properties. The ledger does not add historical assertions.

`data/originals/` stores `source_id`, `kind`, `sha256` and `original_bytes_b64`. To inspect a witness, decode the base64, verify SHA-256, then decode UTF-8. There are 38,046 witness rows for 19,208 sources: 19,208 `registered`, 18,835 `canonical` and three `historical_local_archival_acceptance`. These are not 38,046 distinct texts: 17,969 registered/canonical pairs have identical bytes. Resolve evidence spans against the witness matching the record's `source_version.sha256`; the registered witness is not always that witness.

`data/catalogue/` contains `source_id` and `metadata` for 11,048 catalogue-only/no-ATF sources. Together with the 19,208 ATF-present registry sources, these make a documentary universe of 30,256 IDs. Catalogue-provenience and period labels are not place mentions or adjudicated event dates. Here, no-ATF means that the documentary appendix has no saved ATF text; it does not imply that a blank canonical record exists.

`data/availability/`, `data/aliases/` and `data/admission/` separately retain documentary availability, explicit documentary aliases and dispositions, and scientific-admission provenance. Their rows must not be added to canonical-record counts.

## Record structure and addressing

The root has six required sections: `document`, `entries`, `mentions`, `relations`, `qualifications` and `reasoning`. `supporting_sources` is optional.

IDs are local to the enclosing record. The literal `m1` in two different sources identifies two different stored objects. Within a record, every ID-bearing object's identifier is unique, including those in candidate and supporting-context objects. Stable external addressing requires the immutable `version_hash` and a local ID or exact JSON pointer.

A missing optional key, explicit null, empty array and empty string are different representations. Required nullable fields remain present. Materially withheld interpretations have scoped qualifications; the validator distinguishes them from structural inapplicability. A default decision may hold a target null, but its alternatives remain in the evidence layer rather than becoming additional ordinary values.

Numbers are reduced exact rational strings, for example `"4"`, `"1/3"` or `"-2"`, not floating-point approximations. The canonical schema rejects unknown structural keys. Codes such as `other` and `unclassified` preserve native content within the schema; they do not permit arbitrary structure.

## The document object

Every document has `schema: "ur.source_record.v1"`, local `id: "d1"` and a documentary `source_id`. `source_version` is the required `{sha256, bytes, encoding}` binding to the entire original text, with encoding `utf-8`.

`edition` is a required string or null. It designates a source, not a global identity. `revision` is an integer of at least one. `supersedes` is either the exact predecessor binding `{source_id, revision, sha256, bytes}` or null; revision 1 has null. A predecessor reference does not imply that the selected export contains every earlier payload.

`document_type` is a required genre code or qualified null. The required collections are `parts`, `evidence`, `dates` and `purposes`; the document also requires an extraction `coverage` object. `important_uncertainty` is a sorted, unique index of qualification IDs for material ambiguous or unresolved content. It helps locate that content; it is not a probability score.

In current canonical evidence, genres are `account` in 8,979 records, `receipt` in 3,494, `other` in 2,434, null in 1,301, `expenditure` in 1,090, `personnel_list` in 325, `legal_record` in 321, `letter` in 233 and `inventory` in 232. Records with `other` or null genre can still contain substantial historical information. There is no separate royal genre code: royal material occurs in seal legends, titulary, affiliations, date formulae, standards and body assertions.

### Parts

A part has `{id, kind, parent_id, line_ranges}`. The observed kinds are `tablet`, `envelope`, `seal`, `composite_seal_legend` and `block`. `parent_id` is another part ID or null, and part parentage is acyclic.

Each `line_ranges` interval has `{start,end}` physical-line bounds, with start inclusive and end exclusive. A child's ranges fit inside its parent's. A source may contain several documentary witnesses; a source ID therefore does not necessarily correspond to one physical tablet.

### Evidence anchors

An evidence object has `{id, spans}`, with one or more ordered, nonoverlapping spans. `line` is the one-based physical line of the exact bound original, including headers, directives, comments and blank lines. `token_start` and `token_end` are zero-based, end-exclusive token positions after the defined printed line-prefix handling.

Optional `character_start` and `character_end` occur as a pair. They are zero-based, end-exclusive Unicode-code-point positions within one raw token, not byte offsets.

Evidence references point to these interned IDs. Several assertions may cite one anchor, and one assertion may cite several anchors. Counting citations does not count distinct ancient facts or independent observations.

### Extraction coverage

`coverage` has `status` and `gaps`. Status `complete` requires no gaps; `partial` requires at least one. Each gap has `{id,evidence,reason}`, with reason `unprocessed` or `not_modeled`.

Of the current records, 18,322 declare complete coverage and 87 partial coverage. Complete extraction does not mean that the ancient text is intact or that every interpretation is certain.

## Entries and applicability

An entry requires `id`, `part_id`, `kind` and `evidence`. It represents a source-local semantic unit, not necessarily a transaction. Observed kinds are `detail`, `group`, `subtotal`, `total`, `balance` and `calculation`.

An optional `action` is an addressable predicate with `{id,type,state,evidence}`; `type=other` also requires `native_label`. Type and state are separate. A receipt, issue or return predicate does not establish completion by itself. States `intended`, `owed`, `referenced`, `stated` and `source_asserts_completed` preserve the documentary force or stage. Native labels and reasoning can express distinctions finer than the controlled codes.

`items` and `measurements`, when present, are nonempty arrays or qualified nulls. Null records examined content that is unrecoverable: object content for `items`, quantitative content for `measurements`. `membership` gives the arithmetic operand scope of a recap, balance or calculation. By contrast, `group_members` lists mention or group-entry IDs for a group entry; it does not instruct numerical addition. `allocation_basis` is `joint`, `per_member` or qualified null. `occurrence` identifies an anchored ordinal occasion, not a quantity, duration or regnal year.

The optional `participants`, `places`, `dates` and `purposes` collections contain applicability links. Each link has its own `{id,ref,role,evidence}`, making the application of a person, place, date or purpose separately addressable and qualifiable. A materially unresolved target or role may be null with an explicit qualification.

Participant roles include `source`, `recipient`, `intermediary`, `supervisor`, `custodian`, `witness`, `beneficiary`, `document_party`, `referenced_document_party`, `associated_person` and `unclassified`. An unclassified role retains `native_label`. A document party need not be a physical giver or recipient.

Place roles are `location`, `origin`, `destination`, `storage_location` and `reference_location`. Date roles are `document_date`, `entry_date`, `service_period`, `due_date`, `duration` and `reference_date`. Purpose links apply a known purpose through role `purpose`.

## Mentions

A mention requires `{id,kind,literal,search_form,part_id,evidence}`. Its kind is `person`, `unnamed_role_holder`, `collective`, `institution`, `place`, `deity` or qualified null.

`literal` preserves the selected written occurrence. `search_form` supplies a conservative retrieval form or null; it is not a resolved global entity identifier. A seal owner, patronymic and entry recipient may remain separate occurrences even when supported local relations connect them. Mention counts are not people counts.

The 149,429 current mention objects comprise 107,941 personal mentions, 5,308 unnamed role holders, 8,095 collectives, 5,818 institutions, 16,137 places, 3,679 deities and 2,451 null-kind mentions.

## Items and native terms

An item requires `id`, `type_id`, `designation` and `native_term_id`. `type_id` is a controlled coarse class, `unclassified` or qualified null. `designation` gives exact evidence for the object or population phrase; it is null when the designation is contextually represented but unwritten.

`native_term_id` is a generated `atf:` identifier built from the exact selected token pieces. It is null exactly when `designation` is null. Its encoding is canonical percent-encoded UTF-8. Equal native-term IDs support exact retrieval; they do not establish synonyms, commodity equivalence, historical identity or a dimensional conversion.

Optional `attributes` uses the closed set of keys `species`, `sex`, `material`, `quality`, `status`, `age_class` and `grade`. Attributes retain their own evidence. Lexical values preserve native-term IDs or qualified nulls; ordinal age and grade values may be supported positive integer strings. An animal class is not silently converted into biological age in years.

## Measurements and written expressions

A measurement requires `id`, `subject_ref`, `function`, `evidence`, `expression` and `adopted`. It may also have `derivation` and `geometric_axis`.

`subject_ref` identifies the measured item or group entry, or is qualified null. `function` is `amount`, `rate`, `duration`, `relative_work` or qualified null. `expression` holds the written expression authority or null. A computed nonnull adopted result requires an explicit derivation, not an invented written expression.

`adopted` is a quantity, rate or qualified null representing the canonical record's adopted interpretation. Candidate alternatives are separate. Ordinary access reads this field through the single default, which may retain it, select a justified branch or hold it null. `geometric_axis` can distinguish length, breadth, height and depth; it does not by itself authorize an inferred area or volume.

A written expression has `{id,rule,terms}`. Its rule is `native_vector`, `entity_count` or `unresolved`. Ordered terms have `{id,op,number,unit,evidence}`, with optional `unit_evidence` and `deleted`.

`op` is `add`, `subtract` or null. `number` is an exact rational string or null. `unit` is a supported unit code, an exact native-term ID or null. Editorially deleted terms remain present with `deleted:true` but are excluded from evaluation. Unknown positions remain unknown rather than becoming zeros.

### Quantities

A quantity requires `{dimension,components,standard_ref}`. Dimensions include count, capacity, mass, length, area, volume, time, relative work and ratio, or qualified null. `components` is a nonempty map from unit identity to exact rational string. For example:

    {"dimension":"count","components":{"count":"2"},"standard_ref":null}

A native vector preserves separate units; unlike components must not be silently added.

Optional `native_standard` contains `{native_term_id,evidence}` and requires `standard_ref:null`. It preserves a written standard without asserting an interpreted equivalence. Optional `unit_evidence` binds native component keys to their exact evidence. A null `standard_ref` never licenses an assumed conversion factor.

### Rates

A rate requires `numerator`, `denominator` and `population_ref`; `time_basis_ref` is optional. Both numerator and denominator are quantities.

The denominator describes the rate basis, not the total population amount. The population reference is source-local. An absent time basis does not mean daily. A source-supported geometric denominator can have an inapplicable null population; that is different from an unknown historical workforce.

## Arithmetic membership and derivation

Membership has `{id,target_measurement_ref,state,member_measurement_ids}`. State is `complete`, `partial` or `unresolved`. Unresolved membership has null operands; complete and partial membership retain their supported array of unique measurement IDs. Arithmetic membership is not the same structure as a group of people.

A derivation recipe requires `id`, `mode` and `operation`. Mode is `calculate` or `reconstruct`. Operations are `sum_members`, `copy`, `add`, `subtract`, `multiply` and `divide`.

`sum_members` takes its operands solely from `membership_id`; there is no competing duplicate operand list. Other operations use ordered `input_measurement_ids`. `copy` takes one input and the remaining operations take two. Subtraction and division preserve first-minus-second and first-divided-by-second order.

Addition and subtraction require compatible units and standards. Multiplication supports population×rate or ratio scaling, not unrestricted dimensional algebra. Division requires compatible scalar quantities and a nonzero divisor. Dependencies must be acyclic. An incomplete sum cannot become an unconditional complete total by treating unknown inputs as zero.

Optional `standard_ref` binds an actually implemented conversion rule. The mere presence of arithmetic does not establish a historical conversion.

## Dates, durations, intervals and purposes

Every temporal object has `id`, `kind` and `evidence`, followed by fields appropriate to its kind.

A calendar object contains at least one of `year_formula`, `year_number`, `month_name`, `month_number` or `day`. Material uncertainty can attach to individual fields. Optional `occurrence` is an ordinal within the formula.

A relative object has `base_ref` and `relation`, with relation `before`, `after`, `during`, `at_start` or `at_end`. An optional offset has a nonnegative rational `value` and `unit` of day, month or year. A duration object uses `measurement_ref` to point to its single duration measurement authority. An interval has separate `start_ref` and `end_ref`, each a date ID or qualified null.

Temporal objects belong to the document collection; entry links state where they apply. A seal ruler, oath ruler, reference date, accounting period and body date are not automatically one chronological assertion.

Purpose objects require `{id,category,native_term,entity_refs,evidence}`. `category` is coarse or null; the native phrase and entity references preserve the substantive interpretation. The object's evidence supports the phrase, while its entry link supports application to that entry.

## Relations

Every relation has `id`, `type` and `evidence`, with endpoints, values or members appropriate to its type. A value relation does not need unused binary placeholders. A group relation should not be flattened into arbitrary pairs.

`child_of` is directed from child to parent. It does not infer fatherhood, sex or a transitive family tree. `spouse_of` and `sibling_of` are symmetric and stored in canonical local-ID order, so retrieval must consider both endpoints.

`title` and `person_status` identify a bearer and a value object retaining the controlled code or null and exact `native_term`. `affiliation` and administrative or service links preserve the stated source-local connection, with its typed endpoints and evidence. `seal_owner` connects an owner occurrence to a seal or composite-seal-legend part.

`local_coreference` connects at least two supported mention IDs within the source, retaining their original scoped attributes. `repeated_representation` records supported entry or measurement members. Controlling numerical contribution requires appropriate measurement-level support; an entry-level connection alone is not enough.

`summarizes` links a recap entry to membership where an explicit link is needed. `discharges` and `balance_of` preserve source-local entry, obligation or balance scope; their numerical operands remain explicit elsewhere. An `unclassified` relation preserves its native content through `native_label` and typed endpoints or value. Unclassified does not mean empty.

Optional `scope_refs` limits a relation's applicability. A relation involving a group does not automatically apply to every child of that group.

Four supported repeated-representation relations contain `documentary_correspondence`. This has scope `source_local_tablet_envelope`, one or two `{left_item_id,right_item_id}` pairs and nonempty `context_relation_refs`. It supports correspondence between those specific documentary witnesses, not a universal lexical equation or cross-source identity merge.

## Qualifications and alternatives

A qualification requires `{id,targets,support,impact,reasoning_ref}`. Each target is `{record_id,field}`: `record_id` identifies the local object, and `field` is a relative RFC6901 object-field pointer, not an array-index or wildcard replacement path.

`support` is `well_supported`, `ambiguous` or `unresolved`, without a numerical probability. `impact` is a nonempty set drawn from `meaning`, `evidence_dependence` and `permitted_use`; it is not a severity score. Optional `null_reason` is `not_written`, `unreadable` or `unresolved` where required for material nulls. Optional `reading_marks` contains `{evidence_ref,condition}`, retaining damaged, restored, queried, unreadable, editorial correction or editorial deletion conditions.

An alternatives object contains `exhaustive` and `options`. Each option has `id`, `assignments` and optional `reasoning_ref`. Each assignment declares a `target` and a schema-compatible candidate `value`.

An option is an atomic correlated bundle. Combining a field from one option with a field from a competing option invents an unencoded reading. `exhaustive:false` leaves other possibilities open, even if only one candidate is recorded.

Candidate payloads remain accessible through advanced evidence, not as a second ordinary default panel. The bounded policy can select a justified whole bundle; otherwise, a held target becomes null with branch-evidence pointers. The policy does not change canonical structure or derive a universal preference from option count, order or support labels.

## Reasoning and supporting originals

A reasoning object requires `{id,evidence_refs,premise_refs,text}`. It preserves the source-specific explanation and explicit local dependencies rather than reducing them to a confidence label. Optional `supporting_evidence_refs` points into separately bound supporting originals.

A supporting source has `{id,source_id,source_version,evidence}`. Its exact binding supplies documentary context. It neither merges source identities nor authorizes importing every assertion from that source. There are 106 supporting-source objects in 82 current records.

## Connected evidence

`data/graph/connected/` preserves one assembled evidence row for each stored canonical record, available through `evidence_connected`. Each row has `binding`, `nodes`, `incidences`, `convention_edges`, `qualification_targets`, `candidate_bundles`, `external_record_citations` and `identity_unions`.

Node columns are ordered as JSON pointer, local ID or null, schema kind, layer and category. Incidence columns are ordered as from-node index, to-node index, typed role, exact reference pointer, layer, optional resolution class and optional target pointer. Consumers must preserve these positions.

A node's identity is its immutable record binding plus pointer. ID-less quantities, spans, target objects and component maps are nodes too. `contains` denotes syntactic containment, not historical identity or semantic entailment. N-ary assertions retain role-bearing incidences. Candidate bundles, convention edges and external documentary citations remain distinguishable. `identity_unions` is empty.

Across the 18,412 stored records, the preserved evidence graph has 5,073,009 nodes and 8,683,442 incidences. It expands the same records rather than adding canonical documents. These are not fixed counts for the default graph.

Ordinary `connected`, `neighbours` and typed retrieval rebuild connectivity from the same default used by `record` and search. Nodes use the `research_default` layer. Selected and default references are followed; null endpoints are not replaced with their old evidence endpoints. Candidate and convention links are not asserted as default edges.

When qualifications target objects beneath a null default, their source targets and dispositions remain available. Stable keys use source, original version and pointer, not presentation-local node indices. See [semantics](SEMANTICS.md) for the distinction between containment, source-local assertions and documentary connections.

## Current canonical-content inventory

The following counts cover preserved canonical evidence for the 18,409 current records, excluding the three archival-only records. They do not measure nonnull default fields after machine decisions. Record populations overlap and must not be added together.

There are 172,723 entries in 17,757 records, 149,429 mentions in 18,153 records and 171,251 relations in 17,129 records. Items number 167,028 across 16,357 records; measurements number 165,959 across 15,859 records. Candidate alternative values are not counted as adopted measurements.

All 18,409 current records contain evidence anchors and parts: 872,362 anchors and 23,169 parts in total. There are 23,267 temporal objects in 14,495 records and 13,777 purposes in 6,677 records.

Qualifications number 251,231 and reasoning objects 246,756, each occurring in 18,141 records. There are 3,537 alternative sets in 1,998 records.

Arithmetic structures include 1,172 derivations in 313 records and 4,422 memberships in 1,549 records. Geometric-axis measurements number 683 across 66 records.

The evidence contains 933 observed structural paths and 1,220 object key-shapes. Its records vary substantially: 652 current sources have no entries but preserve other content, while the largest has 701 entries. Analyses therefore need explicit paths, qualifications and counting units rather than an assumption that every source has the same flat structure.
