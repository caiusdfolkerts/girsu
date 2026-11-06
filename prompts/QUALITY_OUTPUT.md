# Quality and output: complete source reconstruction

**Historical extract:** Lightly edited from `20261024_v9_nullable_view_patch`, not proven to be the latest version. Referenced appendices, schemas, example files and runtime files are missing from this extract. Runtime instructions below apply only with the matching authorized assignment and complete package. See [README.md](README.md).

Every role applies this same scientific standard. Researchers and converters produce, and reviewers independently assess, faithful, complete first-pass records: preserve clear facts, make consequential uncertainty effective, and let downstream queries recover the source’s meaning without unsupported certainty or double-counting.

## Your result: a complete, faithful source record

Produce one canonical `ur.source_record.v1` JSON record for each assigned source, bound to the exact supplied original bytes. A later user should be able to query who did what, to/from/for whom, which goods and native quantities, when/where/why, relationships and accounting structure, while seeing important uncertainty and non-additivity restrictions. Put adopted meaning in fields; reasoning explains substantive interpretation, not a substitute database hidden in prose.

**Whole original means every surviving part and line of the supplied evidence**: tablet, envelope, seal, headings, reverse, closing clauses and dates. Here the evidence may be the full supplied transcription, not an independently collated tablet/image. Read it as a whole before deciding what a clause governs. Determine what is asserted, about which subject, over which entries, and with what support; then choose the fields and helpers that express those decisions.

Capture all important surviving parties, titles, parentage, roles, actions, items, quantities, units, standards, dates, places, purposes and account relationships, attached to their supported subjects and scope. Do not create an item, event, interval or relationship merely because a template has a slot for it.

Layout and helper defaults do not decide meaning. Distinguish original loss/damage from unavailable evidence and from work not yet assessed. A `(to be done)` placeholder is an evidence blocker, not a complete source.

A fully assessed damaged source can be complete: preserve what survives and the limits of what can be concluded. Conversely, a clean-looking JSON with an unprocessed closing clause is partial. Set `document.coverage` truthfully; the flag does not prove completeness. Never finish by merely changing a partial flag. Corrections and completion of an existing source do not earn another first-source completion credit.

Work is **source-local**. Represent distinct written name occurrences separately, attach title/parentage to the actual subject, and justify local coreference.

When one written occurrence governs several postings, reuse that occurrence or explicitly link its representations; do not leave them as disconnected people.

Same names alone do not establish identity; different parentage blocks automatic merging, not every possible historical identity hypothesis. `dumu` alone does not establish parent gender. Global identity research and graph admission are outside this job. Supporting-source comparison is allowed only within the assigned evidence scope; bind exact bytes/spans and use it for the stated lexical/documentary premise, not as permission for general identity research.

## Represent the claims you adopt, at the scope you support

### Adopt secure facts; hold only the unresolved claim.

Decide separately what the source establishes and what remains uncertain, then set each affected field accordingly. Preserve clear readings and well-supported inference/restoration with evidence; keep secure coarse associations, native captions, amounts and directional movement even when a finer interpretation is unavailable. Do not label a whole participant collection unresolved merely because receipt versus custody is undecided.

Conversely, withholding an amount does not hold an independently asserted commodity or species: if that classification is itself disputed, qualify or withhold that classification too. Null is not a substitute for assessing the evidence, and a helper's default support label is not your assessment.

Creating a typed object also asserts its existence and kind: retain two reference dates if an interval is unestablished, rather than creating an interval with null endpoints.

### Choose the meaning before the code.

Determine what the source actually establishes, then select a field/type whose documented meaning and endpoint roles match that claim.

For an unfamiliar or easily confused code, look up its definition in the format reference before using it; reuse that knowledge, not the previous source’s interpretation. Do not choose a stronger relation because its name sounds approximately right. `discharges`, for example, means a stated settlement/discharge against an obligation, not every debit, allocation, deployment or account subdivision. A well-supported qualification cannot make an unsupported obligation or settlement true.

Retain the strongest meaning the source supports through the appropriate typed or anchored native relation; do not discard a secure account association merely because its finer interpretation remains unresolved.

### Make every adopted connection recoverable from structure.

Encode the supported parties, roles and account associations, and bind each heading, date, purpose and standard to the claims it governs. Use the whole source to establish what a heading, unit standard or closing clause governs, even when it is written only once, and then encode that scope explicitly. “No implicit inheritance” is a requirement on the representation, not a ban on source-supported contextual reading.

A consumer must not have to guess scope from JSON placement, shared evidence, matching names or prose. Carry a shared standard through the account portions it demonstrably governs; do not extend it across unrelated sections or different dimensions merely by default. Reuse a valid shared entry, group, beneficiary, recipe or scoped relation rather than duplicating it.

If an account counterpart or relationship is not established, leave it unasserted: completeness does not justify an invented balance edge. A compact view may omit a valid binding; inspect the raw structure before repairing it.

### Keep temporal meanings distinct.

Distinguish the date of the document from the date of an event. Attach each independent historical statement to the supplied closing date where that documentary scope is supported, directly or through a valid governing scope. Use `document_date` for documentary context, not as the date of a journey, obligation or earlier act. Do not invent dates for undated sources. A date elsewhere in the record or a shared person supplies no attachment.

Pure calculations need no copied date when explicit inputs already preserve the complete temporal context. Do not broaden a rate's time basis into an elapsed duration of the entry unless the source supports both meanings.

### Distinguish roles and documentary acts.

Use the role the source supports, not whichever role a construction helper supplies. Source, intermediary, beneficiary, recipient and custodian differ. Preserve an adopted allocation-to meaning as beneficiary or equivalent even without a receipt verb; custody alone does not establish ownership or purchase.

Distinguish body seal attribution, ownership of an actual supplied seal legend and an explicitly stated sealing act. Encode the supplied legend's owner, titles and parentage at their supported scope; mention containment is not seal ownership, and a body attribution does not invent a performed sealing act.

A precise anchored native purpose may already preserve an unnamed beneficiary class. Add an entity/role link when a distinct named, independently quantified or relationally identified party would otherwise disappear, not merely to decompose every noun.

### Preserve the written quantities before deriving anything.

Keep native coefficients, signs, ordered operands, units and standards, including secure parts of a damaged expression. Choose the measurement function, subject and evaluation rule from the source; a recap marker is not a commodity designation or a substitute for a lost subject.

`10 la2 1` retains add 10, subtract 1 and adopted 9, not 11 or a hidden subtraction. `6+[n]` retains six and the unknown operand while withholding the whole amount; unknown is not zero. Keep `18 gur + 4 sila` as native components, not 22 sila.

A jar count is not a fixed volume, a half-work coefficient is not half a physical person, and a day ordinal is not duration. Normalize only under a supported named regime; retain a known standard when its amount is held.

### Make permitted numerical use explicit on the quantities it governs.

Distinguish details, written recaps, calculated totals, rates, populations and documentary repetitions. Bind an adopted account association without treating counts and rates as additive grain amounts or inventing a computed result. Preserve written/computed disagreement instead of forcing closure. Encode exact measurement membership and any repeated-representation or non-additivity restriction so a consumer of the affected amounts encounters it.

First identify any unsafe numerical use still permitted by the actual functions, dimensions and governing dependencies. Add only the restriction needed to govern that use; correct typing needs no duplicate warning, but does not by itself resolve overlap between independently usable amounts. For example, correctly typed people, per-person rates and a single grain recap need no extra warning merely to say they cannot be summed together. A reason containing “do not add” is not itself evidence of a missing guard.

An action-only qualification does not restrict those amounts merely because its reason says they must not be added. Target the affected numerical claims or a defined governing structure that actually applies to them; do not invent equality, identity or account edges to express a use restriction. Matching numbers alone establish none of those relationships.

### Make uncertainty effective, not just visible.

Identify every adopted claim affected by the uncertain reading or interpretation, then make the qualification govern those claims. One clause can support several distinct adopted claims: a searchable personal name, a title relation, a coarse personnel classification and an amount. Qualifying one does not qualify its siblings.

Reuse one qualification for several targets when the same assessment applies; do not create duplicate annotations where an existing dependency already governs the claim. Qualify the actual field or hold its endpoint under the runtime convention.

Where a scope has competing readings, retain the secure common scope and withhold only the disputed extension; represent correlated alternatives together rather than inventing independent choices. A concrete disputed endpoint plus an ambiguous parent-array label is not an effective hold.

Use source-bound reasons and alternatives, not numerical confidence scores. Do not add qualification for harmless spelling/sign cleanup or for a finer claim never adopted; consequential restoration, interpretation or permitted-use restrictions do need effective targets.

The `WORKED_STRUCTURAL_PATTERNS.md` (worked structural patterns; missing from this extract) clarify these rules with exact before/after records and permitted alternative structures. Use them to consolidate the decisions above, not to infer an extra rule for every tablet.

## Schema essentials and tools: make the scientific choices yourself

The six required root collections are `document`, `mentions`, `relations`, `entries`, `qualifications`, `reasoning`; optional `supporting_sources` is implemented. Do not add free-form root fields. Exact machine schema and closed vocabularies are in `appendix/reference/specs` (missing from this extract); `appendix/reference/FORMAT.md` (missing from this extract) is the exhaustive reference. `appendix/reference/RUNTIME_ENCODING_ADDENDUM_V1.md` (missing from this extract) resolves historical prose against the current runtime.

Consult the relevant field when needed, rather than reading 100 KB repeatedly. Do not invent codes or undocumented fields to fit an interpretation.

For a source-language caption or unclassified relation, set `native_label` to the selected native phrase recovered from its evidence, not a newly invented English identifier such as `documentary_seal_attribution`. Approved helper encodings are exceptions only where the runtime contract explicitly defines them, such as `metrological_standard` for a held amount’s known standard. Use the existing typed role/relation when it already carries the meaning; do not add a duplicate unclassified relation simply to restate it.

| Object | Working rule |
|---|---|
| Document | Exact original SHA-256, byte count and encoding; physical parts; evidence; dates/purposes; truthful coverage; revision/predecessor. |
| Evidence | Physical lines are 1-based; part line_ranges use an exclusive end. Tokens are 0-based and end-exclusive. Use actual token arrays, not guessed tablet line labels. Preserve damage and native spelling. |
| IDs | Unique source-local IDs, including targetable nested links/terms/recipes. Preserve IDs of the same referent through a correction. |
| Mentions | Written occurrences have kind, literal, search_form, part_id and evidence. A mention has no `/adopted` field. Use supported local_coreference rather than silently collapsing occurrences. |
| Entries/items | Entry kinds: group, detail, subtotal, total, balance, calculation. Commodity designation anchors exclude numerals/unrelated names. Native term is generated from exact designation; coarse type uses the active vocabulary. `unclassified` is not a license to avoid an available supported class. |
| Quantities | Exact rational strings (`"18"`, `"3/2"`), never scientific floats. Expression rules: native_vector, entity_count, unresolved. Functions include amount, rate, duration, relative_work. Adopted native components are checked evaluation, not independently edited arithmetic. Bare grain numeral is not automatically entity_count. |
| Scope/membership | `group_members` only on a group, referencing mentions/other groups, not arbitrary detail entries. Recap membership references measurement IDs; it is not general date inheritance. Current projection does not automatically expand inherited child links. |
| Qualifications | `record_id` names a stable object; `field` is a relative JSON pointer to its named field. Named nested paths such as `/occurrence/value` are permitted; numeric array-index traversal is not. Target a nested object by its stable ID, or target the named collection field when the qualification concerns that collection. Use mention `/search_form`, measurement `/adopted`, or link `/ref` as appropriate. Material null reasons: not_written, unreadable, unresolved. `unassessed` is coverage, not scientific uncertainty. Qualification points to reasoning; do not put reason pointers in measurements/recipes. |
| Reasoning | Concise evidence/premise-bound explanation of important inference, alternatives and allowed use. One reason may support several targets. Straightforward readings and arithmetic need no essay. |

### Put each important qualification on the claim it qualifies

A restored title reading and the identity of its bearer are different claims. Qualify the title relation's `/value` when its adopted reading materially depends on restoration; qualify `/subject_id` when attachment requires a substantive inference or remains uncertain. One qualification can target both when the same assessment applies. Mentioning both in a reason attached to only one field does not qualify the other field. Distinguish exact source fields from adopted interpretations before choosing a qualification target.

Item `native_term_id` and `designation` preserve the selected written form and are immutable evidence fields, not independent semantic classifications; do not qualify them or work around that restriction by qualifying the parent item collection. Judge the claim actually made, not merely whether a field can be targeted.

An exact unclassified native caption can preserve supplied damaged or restored wording without adding a qualification to each word. That does not license an unqualified interpretation: a normalized name, an adopted semantic classification, a title reading, or a substantive relationship or scope assignment must carry the assessment it needs.

A literal caption and its attachment can therefore have different requirements. For the title value, supplied `[gal]` changes boatman to chief boatman even if brackets remain, unlike harmless spelling cleanup. If bearer and title reading have different support, qualify them separately.

Read a selected word in its full source context: restoration brackets may open before its numeral or on an earlier part of the clause and still govern the word. Searching only the extracted word for `[` misses that context. Assess the affected adopted claim, not merely the characters retained in its selected label.

Reading condition and support are distinct. An edition-supplied restoration can be `well_supported` when the source-bound reasoning supports adoption at the stated scope; it is not automatically ambiguous, and a second source is not automatically required. Keep a substantive restoration's dependence explicit at the adopted field. Optional reading marks are not a universal extra requirement, and harmless notation changes need no inference wrapper.

Keep an unresolved native caption as a source-bound unclassified caption when its classification is genuinely unresolved. A familiar formula does not by itself make an ambiguous caption a personal name, quantity or ordinal. Preserve secure facts without manufacturing the missing classification. Qualify only the claim that is uncertain: an unresolved finer classification does not make the exact native caption uncertain, and unknown from/to semantics do not make secure coarse date references uncertain. Do not mark those retained secure fields unresolved merely to explain why a finer claim was withheld.

## Learn the shape from exact supplied examples

Use `APPENDIX_NAVIGATION.md` (missing from this extract) for exact full JSON, originals, coverage and status. Read an example original before its worked answer. Start with **P100877** for a short complete source, then **P100917** for purpose/date/royal-standard scope, and **P128382** for title/parentage without invented sealing.

- **P100877** has 32 sheep, `ki lu2-iri-mu-ta`, Nur-ili and `i3-dab5`: retain source versus custodian, not ownership; preserve literal morphology and explain source-local name segmentation.
- **P100917** has `1(asz) 2(barig) 3(ban2) sze gur lugal`, sheep fodder and month: retain native vector, standard, animal-feed purpose and scoped month without inventing an independently counted flock.
- **P128382** has Igi-anna-kezu, scribe, child of Zi-mu: attach title to the child and preserve gender-neutral parentage; no actual sealing act is written.

For tricky sources, the exact 24-source whole-source packet supplies complete originals and worked semantic keys:
- **P101929:** one gur dabin, source Lu-Ningirsu, A-tu receipt, separate giri3 intermediary and month. One transfer across obverse/reverse; keep three roles distinct.
- **P100901:** one dug dida, separate beer/flour vectors and four native gin2 oil. Hold uncertain dimension/subject without losing the native four or positive movement from Ur; do not invent commodity origin.
- **P100856:** five details and a written recap; do not add recap as extra grain. The supported Classic Ur III/OB comparison gives 156 sila, but arithmetic does not establish roles or membership.
- **P102422:** heading-inherited bread and beer list closed by zi-ga/date. If adopted as bread for named parties, encode beneficiary/equivalent, not generic association just because receipt is unwritten. Derived bread 11/beer 2 are not written recaps.
- **P122885:** tablet/envelope rate panels, recap, distinct gurusz/erin2 labels, additional envelope workforce context, explicit sealing predicate versus seal title/parentage. Preserve repeated numerical witnesses and non-additivity; count mapping does not map rates. Check the separate derived-quantity and recap guards before any aggregation.
- **P101917:** barley details/recap and metal entries/recap; same Ur-mes with different parentage cannot be automatically merged. Preserve supported supplied ku3 without claiming it intact locally; closing custody/purpose does not establish purchase/exchange rate.

These examples teach boundaries and permitted alternatives, not compulsory local IDs. Full JSON stays in the appendix. Read the tricky cases relevant to the next assigned batch.
