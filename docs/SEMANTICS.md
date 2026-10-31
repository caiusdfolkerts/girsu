# Reading the graph

The graph provides one default reading of each source. `Graph.record`, `pointer`, `research_value`, `research`, `search`, `search_all`, `search_page`, `connected`, `neighbours`, `typed_nodes` and `typed_relations` all use that same precomputed reading. Where the default policy cannot select a branch, its target is held null. Ordinary queries neither offer a second competing reading nor search rejected alternatives as if they were accepted facts.

The original source-local structures and native vocabulary remain available. The release does not impose a new historical interpretation or reclassify relations into a new ontology: existing coarse codes and native labels retain their meanings. The [data dictionary](DATA_DICTIONARY.md) describes the fields; [provenance](PROVENANCE.md) explains their bindings to the preserved records and original texts.

## A value and its qualifications

`research_value(source_id, pointer)` returns one `value` together with its source ID, original record `version_hash`, original witness hash and exact pointer. It also returns the separate hash of the materialized default record. The reader checks the release policy fingerprint in the default index.

The accompanying `qualifications` identify the applicable targets and their reasoning and evidence references. The `branches` annotations retain decision status, targets, evidence and option pointers, dependencies and applicable hashes. Diagnostics and coverage metadata describe what the bounded policy did; they do not certify that it understood every statement in the source.

Despite its name, `branches` includes qualification-only annotations as well as identified choice sets. Each annotation distinguishes these with `is_identified_branch` and `annotation_kind`. `identified_branch_count` counts actual identified branches; `qualification_annotation_count` counts the other annotations. `has_branches` is true only when the identified count is positive. `has_ambiguity` is broader: it is true when the scope contains any preserved annotation or an applicable qualification marked ambiguous or unresolved.

Field access recalculates these counts and flags from overlapping targets and applicable qualifications. A selected branch can remain qualified, and a field can have `has_branches:false` but `has_ambiguity:true`. Well-supported qualifications can also exist without either flag. Neither flag measures probability or certainty. A qualification attached to another field or a linked object does not automatically qualify the field being read.

When an actual evidence field lies beneath an ancestor held null in the default, `research_value` returns null with `value_status='null_due_to_unresolved_ancestor'`, the ancestor pointer and the applicable context. It does not turn a misspelled path into a null field: invalid source paths still fail. Strict `pointer` traversal can raise an error beneath a null ancestor; use `research_value` when you need the annotated result.

## What the default policy can establish

A source may describe a reading as ambiguous, unresolved, restored, queried or well-supported. The default policy asks a separate question: can its supported rules establish a preference? `machine_reason_not_established` means that the machine did not establish one. It does not mean that the ancient text or its interpreter offered no reason.

The policy visited all 3,537 structured alternative sets. It selected 26 typed choices and held 3,511 typed sets; it also selected one bounded prose choice. These are different counting units from the number of sources or changed fields. The 9,512 prose signals are a review queue, not additional proven branches or evidence of comprehensive prose understanding.

The materialized context also retains 10,601 `source_qualified_not_machine_resolved` annotations. These record the scope of source qualifications without an established machine selection. They are not another 10,601 parsed alternatives, and they do not require unrelated fields to be nulled.

Neither a single recorded option nor its position in an array is enough to select it. Coarse support labels, source IDs and mechanical edition priority are not selection rules either. A correlated option must be justified as a whole. Unproved dependencies, conflicting or overlapping bundles and joint-world constraints fail closed. A selected restoration keeps its original marks and its dependence on the evidence.

Held targets become null in the default; their source values and candidate bundles remain available through advanced evidence pointers. A qualification without a machine selection does not justify erasing unrelated intact values. Missing optional fields, explicit nulls, empty collections and zero continue to mean different things.

## Three examples

### P102673: a restoration is not an arithmetic correction

The restored counts 1, 1, 2, 2 have numeric evidence anchors checked against the exact bound original. They support the encoded conditional schedule of 177, rather than just the readable-details subtotal of 171. The difference of six does not itself prove those readings; their textual support is independent of whether they balance the account.

The written principal remains 217, with its discrepancy of 20. Calculated paths totaling 237 remain diagnostics. The policy does not replace the principal to reduce discrepancies, force two accounts to agree or supply missing people and events.

### P105740: preserve the supported title and operand scope

P105740 retains the supported administrator title at `/relations/4/value`, with native form `sza3-[tam]`, for its restored seal owner. The edition's DI[KU5] judge reading remains a credible alternative in the source reasoning. The selection does not create a title taxonomy, assert scholarly consensus or identify the owner with a governor.

The same record preserves the supported arithmetic membership 1+1=2 across tablet and envelope witnesses. That scope does not permit counting the same represented sheep again for each witness.

### P204204: an unclassified code can still carry an interpretation

P204204 is a different case. Its native `di?-ku5?` already has a queried primary judge interpretation, while its coarse canonical code is unclassified. That code does not mean the content is unknown. Read alongside P105740, it also shows why neither edition priority nor a coarse code can replace the source-specific reasoning.

## Quantities and calculations

Numbers are exact rational strings, such as `"1/2"`; null is never zero. Written expressions preserve term order, native units, unknown positions and editorial deletions. A measurement's subject, function, dimension, components, standard, population and time basis are distinct fields.

A native vector keeps unlike unit components separate. A standard label does not supply a conversion factor. A rate denominator is not the total population, and an absent time basis does not mean “per day.” Relative-work equivalents are not automatically observed hours. The foundation computes no cross-document grand total.

Explicit canonical recipes retain their calculation or reconstruction mode and their ordered dependencies. When a default decision changes a premise, an affected derived cache must be recomputed from supported default premises or held null. Its old result is not a fresh observation. Complete, partial and unresolved memberships must remain distinct, and repeated representations or overlapping operand scopes must not be counted twice. Default diagnostics report recomputation and withholding; preserved cached accounting artifacts remain advanced evidence rather than newly established default consequences.

## Connections and identity

Containment, source-local assertions and documentary connections serve different purposes. JSON containment says that one object is stored inside another; it does not establish historical identity or transfer every property from parent to child.

Source-local assertions include participant roles, kinship, titles, affiliations, seal ownership, local coreference, membership, summaries and balances. Their endpoints, evidence and scope remain explicit. Multi-party assertions remain n-ary objects with typed incidences rather than being reduced to arbitrary pairs. Entries are not necessarily transactions, and mentions are written occurrences rather than counts of historical people.

Documentary and vocabulary connections support retrieval through witnesses, exact shared native terms and controlled concepts. Equality at that level does not merge people, events, physical goods, standards or instants across sources. A local ID such as `m1` is unique only within its record. Supported local kinship and coreference are preserved; later global identity reconstruction is outside this release.

Default connectivity is rebuilt from default objects and references. An endpoint held null must not leave an asserted edge to its rejected source value. Candidate branches and historical convention edges remain evidence-only. Stable node keys are `(source_id, original record version, pointer)`; node indices are local to a presentation. When a source target lies beneath a null default object, the graph reports that disposition rather than inventing an endpoint.

## Native labels and dates

All 98,928 current unclassified relations have populated source `native_label` values. The preserved canonical evidence retains those labels, their precise endpoints and their evidence. Default labels remain searchable unless an explicit unresolved branch makes the field null; the original is then available at its evidence pointer. Some labels are explanatory English, not literal Sumerian. They are not replaced with speculative categories. Fine distinctions in native items, titles and units likewise remain accessible beyond the coarse enums.

Calendar formulas, months and days, relative dates, intervals, durations, occurrences and applicability roles are separate structures. A seal ruler, oath ruler, reference year and body date are not automatically parts of one chronological assertion. Equal calendar descriptions do not establish the same historical instant. The release invents neither an absolute chronology nor missing date components.

## Searching and checking evidence

Search performs literal, case-insensitive scalar retrieval over the default. It does not normalize synonyms, transliterations or identities. Ordinary scalar search excludes reasoning, qualifications and branch-evidence metadata, so an alternative mentioned only in explanatory prose is not returned as an asserted default fact. That material remains available through explicit evidence inspection.

`search_page` limits work by sources and matches. Keep its exact cursor: it binds the release, query, population and position. An empty page can precede later matches. Only `exhausted` or a null next cursor establishes completion; a limited result is not a population denominator.

Evidence coordinates bind the exact original SHA, not whichever witness happens to be named registered or canonical. Physical lines are one-based. Token bounds and optional Unicode-code-point subtoken bounds are zero-based and end-exclusive. Qualifications lead to reasons and evidence anchors, but repeated citations of one anchor are not independent observations.

Use advanced `inspect` for an explicit comparison with preserved evidence, not as a second ordinary reading. A child introduced beneath a restored default object can have `default_pointer_exists:true` and `evidence_pointer_exists:false`; an absent raw child is not thereby treated as a written null. A pointer missing from both representations still fails. Historical predecessor references and documentary-support links also distinguish unavailable historical payloads from available original evidence. [Provenance](PROVENANCE.md) explains these cases in more detail.
