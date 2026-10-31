# Canonical account value conventions V1

Design only, 20 October 2026. Proposed for the shared six-section source record. No production schema, parser, queue, scientific acceptance or activation change. This fixes serialization choices rather than adding a general mathematics language.

## 1. Shared conventions

Use the technical convention: source-local IDs unique across the record; stable IDs survive corrections to the same referent. Every `evidence` value is an array of IDs from `document.evidence`. Physical lines are1-based; token spans are0-based/end-exclusive. A qualification target is `{record_id, field}`, where `field` is a schema-valid relative JSON pointer, never an array position. Targetable nested expressions, terms, links, memberships and recipes have their own IDs.

No reason pointer occurs in a measurement or recipe. An important inference/limitation is represented by a qualification targeting the appropriate field or recipe and pointing to one reasoning record. Literal decoding needs no essay. Raw transcription marks do not each require a qualification; the immutable evidence remains available.

**Exact rational:** a JSON string. Integers use `"0"`, `"18"`, `"-2"`; nonintegers use a reduced fraction such as `"3/2"` or `"-5/6"`. Denominator positive and greater than1; numerator nonzero in fraction form. No decimal, exponent, leading plus, leading zero, `-0`, whitespace or `/1`. Source spelling remains in evidence. Numerical JSON floats are prohibited for scientific quantities.

## 2. Entry and item shapes

Required entry fields:

    {"id":"e1","part_id":"part1","kind":"detail","evidence":["ev1"]}

Exact `kind` enum: `group`, `detail`, `subtotal`, `total`, `balance`, `calculation`.
- `subtotal`, `total`, `balance` describe a source-written account function, including a qualified/restored reading of it.
- `calculation` is an added researcher result, not an independently written total. Its evidence may be empty; its recipe identifies the source inputs.
- Layout grouping does not imply arithmetic membership.

Allowed optional account fields: `items`, `measurements`, `membership`, `allocation_basis`, `group_members`; action, participant and date/place/purpose links use the shared conventions. Omit inapplicable fields. Do not serialize empty optional arrays just to fill a template. An ambiguous material field is explicitly null with a qualification, not silently omitted.

`allocation_basis`: `joint`, `per_member`, or null. Null is unresolved when the distinction matters. Omission means no group-allocation assertion is made. Do not multiply a joint amount by the number of named participants.

Item shape:

    {"id":"item1","type_id":"sheep","native_term_id":"atf:udu",
     "designation":["ev_sheep_word"]}

`type_id` is an adopted coarse code from LEXICAL_TERM_CONVENTIONS_V1.md, `unclassified` for a known concept outside that small vocabulary, or null when classification is materially unresolved. It is never free prose. `designation` selects the commodity/object words, excluding the amount coefficient, rate and unrelated names. Required `native_term_id` is generated from that exact designation using the shared open lexical rule; `ev_sheep_word` above selects only `udu`. New attested forms require no registry approval or tool change. Different spellings are not automatically synonyms.

Attribute keys are closed: `species`, `sex`, `age_class`, `grade`, `material`, `quality`, `status`. Only important applicable attributes are recorded; omit an empty attributes map. Open native lexical values do not fail validation merely because they are new. Unknown field keys or adopted semantic codes still require a reviewed convention extension. Grades and age classes do not also become commodity measurements.

Each present attribute has exactly `{value,evidence}`, with no separate attribute ID. `species`, `sex`, `material`, `quality` and `status` take a generated native-term ID string. `grade` and `age_class` permit either a positive integer exact string matching `[1-9][0-9]*` or a native-term ID string, because both may be expressed lexically. The disjoint string forms distinguish an explicit ordinal from a lexical descriptor without an extra discriminator. Every key also permits a materially qualified null. Attribute evidence selects the descriptor/ordinal itself, independently of the item noun. A qualification can target `item1` at `/attributes/grade/value`; the path traverses objects, never array indices. No floats, fractions, free prose or independently invented semantic attribute codes are accepted in V1. A numbered class is not an inferred age in years. Choose `grade`, `age_class` or `quality` only when that semantic key is supported; preserve and qualify an unresolved classification rather than coerce an ordinal. Further semantic value enums require an explicit reviewed extension.

The same item can have count and mass measurements. An animal or personnel population is an item/class being counted, not thereby goods being transferred. A group entry can also be a measurement subject. No second authored population object is necessary.

## 3. Measurement, written expression and adopted value

Required measurement shape:

    {"id":"measure1","subject_ref":"item1","function":"amount",
     "evidence":["ev1"],"expression":EXPRESSION_OR_NULL,"adopted":VALUE_OR_NULL}

Optional: `derivation` (one recipe below). Exact `function` enum: `amount`, `rate`, `duration`, `relative_work`, or null. Null means the numerical function remains unresolved. It is never a fallback amount. Count, mass and length are dimensions, not additional functions. Calendar day/year ordinals belong to temporal records; grade/occasion ordinals belong to their attributes. A duration measurement is referenced by its temporal record rather than duplicated there.

`subject_ref` is an item or group-entry ID, or null under unresolved attachment. A person's half-work coefficient is not a fractional headcount: use relative_work with the appropriate dimension/unit and subject; preserve the separate headcount.

### Ordered native expression

    {"id":"expr1","rule":"native_vector","terms":[
      {"id":"term1","op":"add","number":"18","unit":"gur","evidence":["ev1"]},
      {"id":"term2","op":"add","number":"4","unit":"sila3","evidence":["ev2"]}
    ]}

Terms stay in source order. `number` is an exact rational or null for an unknown number position. `op` is `add`, `subtract`, or null for unresolved operation. `unit` is an interpreted unit ID from the controlled metrological vocabulary, a generated native-term ID for an unseen written unit, or null when no unit sign is expressed/legible. An unseen written unit receives no automatic dimension, conversion or arithmetic compatibility: until its metrological use is supported, use expression rule `unresolved` and adopted amount null with the applicable qualification. Evidence covers the numeral and its applicable unit/operator spans; a nonlocal unit attachment that requires interpretation receives the appropriate qualification/reason. Optional `deleted:true` is allowed only for a transcription-marked editorial deletion; such a term is retained but excluded from evaluation. Ordinary terms omit it.

Rules are exactly:
- `native_vector`: evaluate operative add/subtract terms within each explicitly interpreted native unit. Keep different units separate. Do not apply a conversion standard implicitly.
- `entity_count`: evaluate a source-supported count of the specified discrete objects/people. A unit sign need not be written; the adopted unit is `count`. Choosing this rule requires a genuine count construction and subject, not merely a legible numeral beside grain or oil.
- `unresolved`: keep the expression but do not produce an adopted measured amount.

A missing prefix is a term with `number:null`; it is not zero. If a quantity is not written, `expression:null` is allowed with the applicable material-null qualification. A pure calculation also has `expression:null` and a recipe. Expression terms carry known components once; do not copy those components into qualifications.

This is a small ordered additive/subtractive form, not an arbitrary expression tree. An unusual operation outside it remains anchored/unresolved until a specific convention is reviewed. Do not coerce it into addition.

### Adopted native quantity

    {"dimension":"capacity","components":{"gur":"18","sila3":"4"},"standard_ref":null}

`components` is a map from canonical unit ID to exact rational; one entry per unit, no artificial zero components. Source order belongs to the expression, not this evaluated vector. `dimension` is `count`, `capacity`, `mass`, `length`, `area`, `volume`, `time`, `relative_work`, `ratio`, or null. Null dimension does not silently become count or mass. `standard_ref` is an applicable standard ID or null when none is established/applicable.

The numeric components are a generated, checked evaluation of the expression or recipe. They are not independently editable arithmetic. Their interpretation (function, units, dimension, applicable standard) is scientific content and must be reviewed. A clear native quantity can retain a null dimension when its physical interpretation is unresolved; that null constrains conversion/aggregation. A legible coefficient with no supported measure, such as bare grain5, has **adopted:null**, not `{"count":"5"}`.

Unknown essential number/unit/operation or unresolved full-quantity interpretation makes the adopted amount null. Secure neighboring measurements remain usable. No parallel full_value/value/active_value/normalized_value fields are authored. Normalized query results are generated from this value and a named applicable standard; conditional standards cannot produce unconditional main values.

Material interpretation nulls use the shared sparse qualification with an exact target and `null_reason` drawn from `not_written`, `unreadable`, `unresolved`. `unassessed` belongs only to `document.coverage`, not scientific qualifications. Every qualification has a nonempty controlled `impact` set and `reasoning_ref`; reasoning records use `evidence_refs` and `premise_refs`.

Raw expression `unit:null` and adopted quantity `standard_ref:null` are permitted absence slots: a discrete count may have no written unit sign, and a native vector may need no adopted conversion standard. These nulls do not by themselves require an uncertainty qualification. If the absent/unreadable unit or unresolved standard instead prevents a material interpretation or use, qualify that exact limitation and withhold the affected adopted result. This does not turn ordinary absent optional details into uncertainty records.

## 4. Rates

A rate is a measurement with `function:"rate"`; no second rates collection. Its subject is the numerator commodity/item. Its adopted shape is:

    {"numerator":{"dimension":"capacity","components":{"sila3":"1"},"standard_ref":null},
     "denominator":{"dimension":"count","components":{"count":"1"},"standard_ref":null},
     "population_ref":"item_sheep"}

Optional `time_basis_ref` references a document duration/period. Omission makes no time-basis assertion; it never means per day. A disputed required basis is null and qualified. The denominator is the rate basis, such as one sheep, not a duplicated copy of the actual flock count. Querying the population's amount supplies the latter.

The ordered expression evaluates the numerator. Denominator, population and period attachments are separately reviewable scientific assertions. An inference about an unwritten denominator must be explained. If per-person versus aggregate interpretation is genuinely ambiguous, the adopted rate is null with typed alternative assignments; an intact capacity expression remains visible.

## 5. Membership and derivation: one operand authority

A subtotal/total/balance may own one membership object:

    {"id":"membership1","target_measurement_ref":"measure_total",
     "state":"complete","member_measurement_ids":["measure_a","measure_b"]}

Exact state enum: `complete`, `partial`, `unresolved`.
- Complete: the listed unique measurement IDs exhaust the proposed additive scope.
- Partial: listed members are known, but do not exhaust the scope. This does not license a full-total calculation.
- Unresolved: `member_measurement_ids:null`; typed candidates are in qualifications. Null is not an empty known sum.

Calculation leaves are **measurement IDs only**, never an entry ID whose count, mass or rate must be guessed. Member IDs are source-ordered; they do not imply an ordering-sensitive sum. A sum cannot combine multiple representations of one underlying measurement without the policy below. A membership record itself may be an important well-supported inference and then needs its qualification/reason.

Recipes are targetable objects. They have `id`, `mode` (`calculate` or `reconstruct`), and exactly one of these shapes:

    {"id":"calc1","mode":"calculate","operation":"sum_members",
     "membership_id":"membership1"}

    {"id":"calc2","mode":"reconstruct","operation":"subtract",
     "input_measurement_ids":["measure_total","measure_known"]}

Exact standalone operations and arities: `copy`(1), `add`(2), `subtract`(2, first minus second), `multiply`(2), `divide`(2, first divided by second). Input order is explicit. No embedded formula strings, arbitrary functions or nested expression trees. A genuinely required intermediate result is another measurement; this should not be invented merely to precompute every possible analysis.

Optional `standard_ref` names a required conversion rule/standard. Unit-compatible exact arithmetic is required. Multiplication/division must have an explicitly supported dimensional meaning, such as a population count times its rate; matching numbers alone is insufficient.

Rules:
1. Recap sum recipes reference the membership ID and **never copy its member list**.
2. Standalone recipes own their explicit input IDs. Other structures may cite the recipe, not repeat its numeric dependency list.
3. A missing entry reconstructed as total minus known members requires independently supported total membership, units and known inputs. The qualification/reason identifies that premise; validation must not accept a membership justified only by the reconstructed result. An independently written total is not a recipe for its own inputs.
4. Numeric dependencies must be acyclic. Do not use a calculated total to reconstruct an input from which that total was calculated.
5. A written total remains its own measurement. A sum or discrepancy is a separate calculation entry/measurement. Never replace the written amount to force closure.
6. Essential unresolved inputs, standards or membership hold the main result. For this pilot, do not introduce prose-based override or a general invariance prover. An exceptional uncertainty-independent result needs an explicit separately reviewed rule; otherwise retain it as a non-active candidate.
7. No recipe has its own reasoning pointer. Qualification→reason is the one link path.

## 6. Repeated representation and aggregation

The relation vocabulary supplies `repeated_representation` with explicit member IDs. For numerical aggregation, use measurement-level groups, e.g. tablet count and matching envelope count. An entry-level documentary link alone is insufficient to choose which of its count/weight/rate measurements correspond. Do not deduplicate by matching number, name, date or source adjacency.

Default aggregate policy is **once per supported representation group**:
- All included group members must represent the same numerical function/subject and have compatible supported adopted values.
- Collapse the group to one contribution and retain all evidence IDs. An internal representative may be selected deterministically by lowest ID; it has no greater scientific authority.
- An unresolved equivalence, conflicting values or unresolved material unit blocks a definite aggregate across that group. Do not silently count both or select a favored reading. A query can return the affected groups and an explicitly conditional scenario.
- Where a source-authored total already refers to a group member, do not add both the total and its members as separate shipments.

No third merged entry or independently authored merged quantity is stored. Query-time results may carry the complete support/qualification set. Alternative bundles never enter the adopted aggregate automatically.

## 7. Three serialized design fragments

These are fragments, not complete source records or new scientific acceptances. Evidence/part/item IDs omitted from a fragment are supplied by the ordinary source envelope, not inferred by the consumer. Values below illustrate the existing source readings. Qualification details follow the reviewer conventions; only important limitations/inferences are shown.

### A. P205530:50 sheep, a one-sila specification, bare grain5

Physical line7: `5(u) udu 1(disz) sila3-ta`; line8: `5(disz) sze ur-{d}ba-ba6`. `ev_count`, `ev_rate`, `ev_grain` select those exact expressions. The full envelope separately supplies `ev_sheep_word = {id:"ev_sheep_word",spans:[{line:7,token_start:1,token_end:2}]}` and `ev_grain_word = {id:"ev_grain_word",spans:[{line:8,token_start:1,token_end:2}]}`. These designation anchors select only `udu` and `sze`, not either coefficient.

```json
{
  "entries": [{
    "id": "e1", "part_id": "part1", "kind": "detail", "evidence": ["ev_count", "ev_rate", "ev_grain"],
    "items": [
      {"id": "item_sheep", "type_id": "sheep", "native_term_id": "atf:udu", "designation": ["ev_sheep_word"]},
      {"id": "item_grain", "type_id": "barley", "native_term_id": "atf:sze", "designation": ["ev_grain_word"]}
    ],
    "measurements": [
      {"id": "measure_count", "subject_ref": "item_sheep", "function": "amount", "evidence": ["ev_count"],
       "expression": {"id": "expr_count", "rule": "entity_count", "terms": [{"id": "term_count", "op": "add", "number": "50", "unit": null, "evidence": ["ev_count"]}]},
       "adopted": {"dimension": "count", "components": {"count": "50"}, "standard_ref": null}},
      {"id": "measure_rate", "subject_ref": "item_grain", "function": "rate", "evidence": ["ev_rate"],
       "expression": {"id": "expr_rate", "rule": "native_vector", "terms": [{"id": "term_rate", "op": "add", "number": "1", "unit": "sila3", "evidence": ["ev_rate"]}]},
       "adopted": {"numerator": {"dimension": "capacity", "components": {"sila3": "1"}, "standard_ref": null}, "denominator": {"dimension": "count", "components": {"count": "1"}, "standard_ref": null}, "population_ref": "item_sheep"}},
      {"id": "measure_grain", "subject_ref": "item_grain", "function": "amount", "evidence": ["ev_grain"],
       "expression": {"id": "expr_grain", "rule": "unresolved", "terms": [{"id": "term_grain", "op": "add", "number": "5", "unit": null, "evidence": ["ev_grain"]}]},
       "adopted": null}
    ]
  }],
  "qualifications": [{"id": "q1", "targets": [{"record_id": "measure_grain", "field": "/adopted"}], "support": "unresolved", "impact": ["meaning", "permitted_use"], "null_reason": "not_written", "reasoning_ref": "reason1"}],
  "reasoning": [{"id": "reason1", "evidence_refs": ["ev_grain"], "premise_refs": [], "text": "The grain coefficient5 is written without a measure. The adjacent animal rate does not establish its unit; no count or capacity amount is adopted."}]
}
```

Expected: sheep count50 and rate1sila per sheep are retrievable. The conditional rate calculation yields50sila for that population, with no assumed daily period. The independently written grain5 is excluded from measured-amount aggregation. No comparison residual against5 is produced. This fragment does not encode the recipient attachment, which belongs to the full record's participant links.

### B. P205530: written sheep recap75 and a separate calculation

The full record has `measure_25` and `measure_50`, the two written sheep headcounts at physical lines5 and7. Their adopted values are count25 and count50. `ev_recap` is physical line19's75-sheep recap. The membership is the proposed supported interpretation of this local sheep-class panel; it still requires normal independent review.

```json
{
  "entries": [
    {"id": "e_recap", "part_id": "part1", "kind": "subtotal", "evidence": ["ev_recap"],
     "measurements": [{"id": "measure_75", "subject_ref": "item_sheep_class", "function": "amount", "evidence": ["ev_recap"],
       "expression": {"id": "expr_75", "rule": "entity_count", "terms": [{"id": "term_75", "op": "add", "number": "75", "unit": null, "evidence": ["ev_recap"]}]},
       "adopted": {"dimension": "count", "components": {"count": "75"}, "standard_ref": null}}],
     "membership": {"id": "membership1", "target_measurement_ref": "measure_75", "state": "complete", "member_measurement_ids": ["measure_25", "measure_50"]}},
    {"id": "e_check", "part_id": "part1", "kind": "calculation", "evidence": [],
     "measurements": [{"id": "measure_sum", "subject_ref": "item_sheep_class", "function": "amount", "evidence": [], "expression": null,
       "derivation": {"id": "calc1", "mode": "calculate", "operation": "sum_members", "membership_id": "membership1"},
       "adopted": {"dimension": "count", "components": {"count": "75"}, "standard_ref": null}}]}
  ],
  "qualifications": [{"id": "q_members", "targets": [{"record_id": "membership1", "field": "/member_measurement_ids"}, {"record_id": "membership1", "field": "/state"}], "support": "well_supported", "impact": ["evidence_dependence", "permitted_use"], "reasoning_ref": "reason_members"}],
  "reasoning": [{"id": "reason_members", "evidence_refs": ["ev_count25", "ev_count50", "ev_recap"], "premise_refs": [], "text": "The two local sheep entries and their separate sheep-class recap support this membership; cattle, the wild animal and processed feed are separate classes. Numerical closure is a check, not the sole reason for membership."}]
}
```

Expected: the recipe resolves one list through membership1 and returns75count. Comparison with the independently written75 yields residual0. It does not count150 sheep or sum the subtotal alongside its detail. The same source's written cattle recap5 is retained even though the two cattle detail counts sum6; this sheep membership cannot repair that other discrepancy.

### C. P133163: tablet4, restored envelope[4], one aggregate contribution

`ev_tablet` is physical line5's four hides; `ev_envelope` is line19's restored `[4]` hides. The source-local correspondence and its support must be independently reviewed. The envelope's reconstruction recipe owns one input; no second operand list is maintained in the reason.

```json
{
  "entries": [{"id": "e_envelope", "part_id": "part_envelope", "kind": "detail", "evidence": ["ev_envelope"],
    "measurements": [{"id": "measure_envelope4", "subject_ref": "item_envelope_hides", "function": "amount", "evidence": ["ev_envelope"],
      "expression": {"id": "expr_envelope", "rule": "entity_count", "terms": [{"id": "term_envelope", "op": "add", "number": "4", "unit": null, "evidence": ["ev_envelope"]}]},
      "derivation": {"id": "calc_restore", "mode": "reconstruct", "operation": "copy", "input_measurement_ids": ["measure_tablet4"]},
      "adopted": {"dimension": "count", "components": {"count": "4"}, "standard_ref": null}}]}],
  "relations": [{"id": "rel_duplicate", "type": "repeated_representation", "members": ["measure_tablet4", "measure_envelope4"], "evidence": ["ev_tablet", "ev_envelope"]}],
  "qualifications": [{"id": "q_restore", "targets": [{"record_id": "measure_envelope4", "field": "/adopted"}, {"record_id": "rel_duplicate", "field": "/members"}], "support": "well_supported", "impact": ["evidence_dependence", "permitted_use"], "reading_marks": [{"evidence_ref": "ev_envelope", "condition": "restored"}], "reasoning_ref": "reason_restore"}],
  "reasoning": [{"id": "reason_restore", "evidence_refs": ["ev_tablet", "ev_envelope"], "premise_refs": ["calc_restore"], "text": "The corresponding intact tablet entry supports the envelope's supplied four and the repeated-representation interpretation. The envelope remains restored; the two writings are not independent receipts of four hides."}]
}
```

Expected: the full record supplies tablet count4. The copy recipe returns4. A once-per-supported-group aggregate contributes4, not8, and retains both evidence references. The restored condition is searchable; it does not alone raise important_uncertainty. If the repeated-representation inference becomes ambiguous, the aggregate across both is held rather than doubled or silently collapsed.

## 8. Efficiency improvements ranked

1. **One generated source-ordered author/reviewer view with effective values and qualifications.** Highest priority. Show exact text, item/population/rate links, literal expression, adopted/null result and shared reasoning together. This removes repeated manual joining of prose, parser output, account sections and projection copies. It must display the actual consumer view, not another authored narrative.
2. **Generate IDs, exact anchors, arithmetic caches and repeated explicit attachments from author choices.** A single header-scope selection may expand to canonical links; a single chosen membership drives the sum. This removes re-keying and inconsistent duplicate operands while leaving interpretation with the researcher.
3. **Exact field-diff and dependency-impact views for corrections.** Stable measurement/revision IDs plus the recipes above make the23 grain-field dependency audit and narrow successor review mechanical bookkeeping. Do not rescan or rewrite unrelated source/account content.

Cuts: no separate rates collection, no author-entered normalized scalar, no alternate full_value/value fields, no authored merged tablet/envelope record, no per-fact confidence, no separate whole-text confidence judgment, no duplicate calculation operands in reasoning, no requirement to reconcile every source before extraction is complete.

Expected benefit is reduced repeated extraction and clerical consistency work. No measured texts-per-hour or percentage gain is asserted. The pilot should measure author/reviewer effort and consumer failures before bulk adoption.
