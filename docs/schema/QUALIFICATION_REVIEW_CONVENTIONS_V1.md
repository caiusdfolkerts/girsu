# Qualification and review conventions V1

Design only, prepared by the scientific verifier. No runtime, schema, code, queue or graph change. This convention follows the user's latest restriction: record important qualifications, not every editorial mark.

## 1. Admission test: when to create a qualification

Create one sparse record when it is necessary to explain a substantive inference or when a limitation changes:
- the adopted domain meaning (who, what, amount/unit, role, temporal/spatial scope or relationship);
- the positive evidence on which acceptance of that meaning depends; or
- permitted use, including whether a value is usable, additive, comparable or a duplicate.

Do not create one just because the source contains #, brackets, a corrected spelling or an orthographic variant. If the adopted meaning and its justified use are unaffected, the raw original and ordinary evidence anchor suffice. A supported editorial restoration whose adoption depends on another source component is important evidentially; a harmless spelling mark need not be separately encoded.

Source-condition searches use a generated, exact-token index of the bound transcription/evidence, including marks that did not warrant a qualification. This index reports source notation only, not support or confidence, and is not separately authored. Important inherited restorations also remain discoverable through their inference qualifications. Omitting a harmless qualification must never erase editorial status from source queries.

This is not permission to ignore source damage while reviewing. The reviewer checks the raw source, then records only the consequential result. One shared reason may cover a homogeneous pattern. Routine literal copying, fixed numeral decoding and deterministic spelling cleanup do not need inference wrappers.

## 2. Exact minimal shape

Qualification:

    {
      "id": "q1",
      "targets": [
        {"record_id": "m1", "field": "/adopted"}
      ],
      "support": "well_supported | ambiguous | unresolved",
      "impact": ["meaning | evidence_dependence | permitted_use"],
      "reasoning_ref": "r1"
    }

Optional fields only when needed:
- reading_marks: [{evidence_ref, condition}]
- alternatives: {exhaustive: boolean, options: [{id, assignments: [{target: {record_id, field}, value}], reasoning_ref?}]}

IDs are globally unique within the versioned source. The field key is a relative RFC6901 path (for example /adopted); array-index traversal is forbidden, and targeted nested objects have stable IDs. Evidence IDs refer to interned document.evidence spans; physical lines are 1-based, tokens 0-based/end-exclusive under the shared core convention. A strict substring of one token may use paired zero-based/end-exclusive Unicode-code-point character_start/character_end; full-token spans omit them. All paths, support values, impact labels and condition labels are controlled and searchable. Values in alternatives follow the target field's ordinary type. Explanatory text appears only in the referenced reasoning record. A qualification may additionally carry null_reason for its null targets (section4); different absence causes require separately scoped qualifications, not extra keys on field references.

The three impact labels are a set, not a score or severity scale:
- meaning: alternative resolution changes the adopted interpretation/value/endpoints/scope;
- evidence_dependence: adoption rests on a substantive comparison, editorial supply, reconstruction or other inference that must remain inspectable;
- permitted_use: uncertainty or dependence changes admissibility, additivity, comparability or duplicate treatment.

At least one impact is required. It is a reviewable semantic assertion, not something inferred by parsing prose. Do not add a second important=true flag, priority number or whole-text grade. The controlled impact declaration records why this qualification passed the admission test.

## 3. Reading condition and support are distinct

Conditions: damaged, restored, queried, unreadable, editorial_correction, editorial_deletion. Attach them to exact token spans, and only include those relevant to the qualification. A damaged category and an intact numeral need not share a condition. No condition means no relevant source-condition assertion here, not a blanket claim that the source is intact.

These marks describe the bound source transcription. A bracketed reading inherited from that edition is editorial evidence; the pipeline did not invent it. A new proposed restoration is a candidate/inference, never a silent change to the original or a claim that it was already supplied by the editor.

Support applies to the exact target interpretation:
- well_supported: positive evidence supports adoption at the stated scope, with the reasoning making any substantive inference explicit;
- ambiguous: one proposed interpretation lacks adequate resolution, or multiple viable interpretations remain;
- unresolved: no sufficiently specified interpretation is supported.

No probabilities are implied. Damaged/restored can be well_supported; an intact coefficient can have unresolved unit/meaning. A qualification can target several fields only if its support assessment applies to each. Split only the qualification when assessments genuinely differ; do not split the whole source.

## 4. Main null, omitted and unassessed

- Main value present: supported enough for adoption. Ordinary direct facts stay compact; default support is usable only within the externally accepted review scope, never merely because a draft omitted a qualification.
- Main value null: the record intentionally withholds a material interpretation. A qualification targets that field and gives null_reason = not_written | unreadable | unresolved. The reason describes the scientific limit. Null is not zero, not an empty name, and not a generic count unit.
- Omitted optional field: not modeled/applicable as an ordinary requirement here. It must not be queried as an observed absence. An omitted required field is invalid. Do not manufacture uncertainty records for every optional date or role absent from a text.
- Material observed absence, where scientifically important: retain an explicit scoped not_written/null statement rather than hiding it by omission. A written grain rate with no recoverable unit is such a case; the lack of an optional month on an otherwise dated receipt need not be.
- Unassessed: authoring/coverage state, not scientific ambiguity. Keep exact unassessed material spans/targets in document.coverage; do not relabel them ambiguous or give them default well_supported. A claimed complete review cannot contain unassessed required material scope. Partial review acceptance must remain explicitly bounded outside the scientific record.

An exact numeral may survive inside an incomplete expression. Keep it in the written expression's known components; the full adopted value remains null. Do not copy known components into qualifications or promote them into active quantities. Distinguish an unexpressed unit, unreadable unit, and unresolved semantic relation when that distinction affects interpretation.

## 5. Alternatives are assignment bundles

Each option is a set of assignments that stand or fall together. Options within one alternatives object are mutually exclusive; code may not mix fields from different options. A candidate has no active/adopted status merely because its value is typed.

exhaustive=false is the normal conservative setting: the listed candidates do not rule out an unknown interpretation. exhaustive=true requires an explicit scientific argument that the options exhaust the possibilities. A single non-exhaustive option is valid for an inherited editorial restoration that remains a candidate.

Every assignment target must be declared in qualification.targets and must match its field type. Preserve independently secure fields outside the bundle. A shared reasoning_ref explains the alternatives; an option gets its own reasoning_ref only if its basis differs. No candidate confidence score is added.

## 6. One link direction; no duplicated inputs

Reasoning:

    {"id": "r1", "evidence_refs": ["s1"], "premise_refs": [], "text": "Concise source-specific argument."}

Qualification → reasoning_ref is the only authored explanation link. Reverse target/reason indexes are generated. A reasoning record does not maintain a duplicate target list.

Every substantive inferred field, including a well-supported inference, is targeted by a qualification citing its reason. A shared qualification may target all fields of a genuinely homogeneous pattern. A plain direct fact requires neither a qualification nor formulaic reasoning.

Arithmetic recipes do not also carry reasoning_ref. The inferred measurement/result or recipe field is targeted by the qualification. A recipe evaluating a recap references its one authoritative membership ID; it does not copy the membership operand list. Other reconstruction recipes own explicit input IDs. Reasoning may cite the recipe ID in premise_refs instead of copying its operands. Independent non-arithmetic premises may be cited directly.

No schema can detect every silent inference automatically. Mechanical coverage can prove that identified inferred fields have reasons and all targets resolve; full-source review must still detect unsupported implicit commodity, role, title, date, identity and membership assignments.

## 7. Generated important_uncertainty

For the completed covered record:

    important_uncertainty = sorted unique IDs of admitted qualifications
                           with support in {ambiguous, unresolved}
                           and a nonempty controlled impact set.

All qualifications already passed the substantive admission test. There is no prose classifier, second importance flag or separate whole-text confidence grade. A supported inference/restoration remains searchable but does not raise an uncertainty headline solely because it needed reasoning.

Materiality depends on the domain meaning, not a known future query. Resolving a recipient attachment, animal class, unit, event state, service period or additive scope changes interpretation/use and belongs here. A minor spelling variant that leaves the adopted meaning and justified use unchanged does not.

Empty means no material ambiguity identified in the covered, reviewed record. It does not mean a perfectly preserved object or proof that unreviewed/omitted scope is sound. The view displays coverage separately. A short readable summary is generated from these IDs and their reasons, not independently authored.

## 8. Two encoded design examples

These are design illustrations, not new canonical acceptance or modifications of the existing packets. Evidence IDs below are local aliases with exact physical-line definitions.

### A. P133163: supported inherited envelope restoration

Evidence: t5=P133163.atf:L5 “1. 4(disz) kusz udu”; e19=L19 “5. [4(disz)] kusz# udu”. Source SHA c700fceb13e01606961913c02e4cb9ef45c2332717fed044bd830009fc6b4be2.

    measurement envelope_count:
      adopted: {dimension: count, components: {count: "4"}, standard_ref: null}
      evidence: [e19]
    relation repeat1:
      type: repeated_representation
      members: [tablet_entry, envelope_entry]
      evidence: [t5, e19, transaction_context]
    qualification:
      id: q_envelope4
      targets:
        - {record_id: envelope_count, field: /adopted}
        - {record_id: repeat1, field: /members}
      support: well_supported
      impact: [evidence_dependence, permitted_use]
      reading_marks:
        - {evidence_ref: e19_bracketed_numeral, condition: restored}
      reasoning_ref: r_envelope4
    reasoning:
      id: r_envelope4
      evidence_refs: [t5, e19, transaction_context]
      premise_refs: []
      text: "The envelope supplies4; the corresponding tablet preserves4 with matching transaction context. Treat these as representations of one entry, retaining the envelope restoration."
    important_uncertainty: []

Effective view: show tablet4 and envelope[4] together, restored numeral visibly marked, main4 supported by the comparison, and a duplicate-group aggregation guard. Do not show8. The damaged kusz mark remains in the raw original; no separate qualification is required if its adopted commodity meaning is supported and unaffected. If the comparison itself were uncertain, support and adopted relation would change.

### B. P129907: inherited single candidate without demonstrated local corroboration

Evidence: d5=P129907.atf:L5 “1. [1(disz)] ansze!”. Source SHA07c28beb8ea96275d86ad3ad4c79344ba8ac30f18fca9114671ea50d41144330. Full saved source has no repeated numeral independently corroborating1. No original editorial rationale or photograph was examined in the bounded inspection.

    measurement donkey_count:
      adopted: null
      evidence: [d5]
    qualification:
      id: q_restored1
      null_reason: unresolved
      targets:
        - {record_id: donkey_count, field: /adopted}
      support: ambiguous
      impact: [meaning, evidence_dependence, permitted_use]
      reading_marks:
        - {evidence_ref: d5_bracketed_numeral, condition: restored}
      alternatives:
        exhaustive: false
        options:
          - id: candidate_editorial1
            assignments:
              - target: {record_id: donkey_count, field: /adopted}
                value: {dimension: count, components: {count: "1"}, standard_ref: null}
      reasoning_ref: r_restored1
    reasoning:
      id: r_restored1
      evidence_refs: [d5, full_source]
      premise_refs: []
      text: "The supplied edition restores1. This inspection establishes that provenance but finds no local duplicate numeral or independently assessed editorial rationale sufficient to adopt the number under the new threshold. Retain1 as a non-exhaustive editorial candidate."
    important_uncertainty: [q_restored1]

Effective view: main count unavailable, editorial candidate1 visible beside the bracketed source; no zero, no inferred single animal and no active arithmetic operand. The correction mark on ansze remains visible in the original; it does not require a separate qualifier merely because it exists. This does not declare the editor wrong or claim the number is unrecoverable.

## 9. Ranked efficiency improvements and cuts

1. Canonical effective reviewer view. Show source-ordered entry, full original, adopted/candidate/components, function/unit, exact effective qualifications/reason and consumer projection together. Sparse storage without this view makes review slower.
2. One numerical and explanatory authority. Remove independently maintained scalar/prose copies. P207453 needed77 identical prose corrections; a single recipe/value and shared reason remove that consistency work.
3. Canonical correction view. Show exact immutable old/new bindings, changed fields, prior decision and affected dependency closure, with full original accessible. Mechanical verification confirms unchanged portions; scientific review focuses on the change and dependent meanings without blindly accepting untouched context.
4. Generate bookkeeping. Stable IDs, token spans, source hashes, reverse reason indexes and material-uncertainty summary should not be hand-maintained twice. Mechanical checks remain distinct from scientific acceptance.
5. Cut insignificant qualification objects. Keep raw marks in evidence; encode only consequential reading/inference/use issues. Avoid a reason for every normal numeral, spelling normalization or harmless damage flag.
6. Cut redundant layers. No local-referent object beside mention/coreference, no context inheritance bundles, no second rate collection, no second reasoning target list, no duplicated membership operands, no independent important flag/whole-text grade, and no candidate-to-active fallback.

Expected gain is fewer avoidable consistency and lookup checks, not less full-source scientific judgment. It is not a measured speedup. Pilot tests should include ordinary direct records, sparse important exceptions, alternative bundles, duplicates, unknown-unit coefficients and a narrowly corrected successor. Require the verifier to complete these without custom projection/diff scripts before calling the format canonical.
