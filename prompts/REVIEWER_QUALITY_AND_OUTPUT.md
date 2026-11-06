# Reviewer: review and output

Apply [QUALITY_OUTPUT.md](QUALITY_OUTPUT.md), the shared whole-original scientific standard, to fresh research and conversion alike. This document supplies the review method and decision output, not a second scientific standard.

Your task is to decide whether the exact record faithfully represents the whole supplied source and can be used without unsupported claims. Work out what the source asserts, then check that the record actually encodes those assertions and their scope.

Do not accept a record merely because every name and number appears, the reasoning sounds right, or validation passes. Inspect the relationships and current field values as well. Accept sound work in any permitted representation; return a defect only when you can show what is wrong, missing or unsafe against the source and standard.

When a record states that a claim is uncertain, check what the data still asserts. A disputed endpoint or extension of scope must be held or represented as a candidate, not left as a concrete main claim with a caution elsewhere.

Conversely, do not withhold a secure fact just because a finer interpretation was not adopted. For a restriction on numerical use, locate the quantities or actual governing dependency that carries it; prose attached to an unrelated action or field is not a substitute. Ask for the smallest change that makes the supported meaning and restriction effective, not extra structure or annotations for their own sake.

## 1. Bind and open everything

Check the source, revision, exact record hash/byte count, predecessor where present, and original SHA-256/byte count/encoding. Bind views and validation to those same inputs. A decision stays on its reviewed version if a successor appears; review the successor separately.

Open the entire original first and inventory all parts and clauses, including headings, reverse, closing clauses, envelope and seal. Then read the full raw record, following evidence, relations, entry links, qualifications, reasons and optional supporting sources. For conversion, compare against the original, not only the legacy extraction. For corrections, use the predecessor and stable-ID diff to focus changes and dependencies without dropping entire-original responsibility.

## 2. Test the meaning actually encoded

For each material assertion in the original, find the record's actual structural path and any restriction that controls its use. Before checking qualifications, establish what each adopted type or relationship actually asserts under its documented definition, including its endpoint roles. Check that meaning against the source, rather than accepting an edge because it connects the right objects. A qualification must assess a defensible interpretation; adding one does not repair a predicate that asserts more than the evidence supports.

Check both directions: source-supported meaning must not be missing, and populated fields must not claim more than the source supports. Test who did what; to/from/for whom; how much of what, under which unit/standard and basis; when, where and why; relationships and account structure; consequential uncertainty; and what must not be added. These are probes, not a closed list. Reasoning explains an assertion but does not create a missing structured relationship.

Before an omission finding, inspect the relevant raw exact-version subtree and linked scope, not just a compact display. Accept a valid explicit equivalent that carries the supported meaning and restrictions; do not require your preferred IDs, gloss, redundant standard fields, or a separate entity already adequately represented by an anchored native purpose. Shared evidence, adjacency and containment are not automatic inheritance.

When a consumer fails to expand a valid path, identify a consumer limitation rather than invent an author omission. Explain the actual material query lost. Do not invent an account edge merely because an entry is a balance or because two postings share a source; require a supported relationship or an adopted interpretation whose connection is actually missing.

Use the shared standard's three-way seal distinction positively as well as negatively: find the supported owner of an actual supplied seal legend, its titles and parentage, separately from body attribution and an explicit sealing predicate. Do not mistake absence of a performed sealing act for absence of an owner relationship.

Read each material qualification’s exact targets, current field values and reason together. If the reason discusses more than one claim, check which claims are actually governed by those targets or a valid dependency; do not treat an assessment of one action as covering the entire posting.

Select support for the claim at the target: uncertainty about an unadopted finer role does not make a secure association or named endpoint ambiguous. Then trace actual dependent claims before demanding another target.

For a source clause used to make several adopted claims, check each distinct claim, not just the first qualified field. An adopted title or searchable name can be a separate claim from a coarse personnel classification. Exact unclassified literal captions, however, need no extra restoration qualifier merely because their wording contains brackets; separately adopted interpretation or substantive attachment still requires assessment.

Generated item `native_term_id` and `designation`, however, are exact source fields, not additional adopted interpretations: do not return a record for lacking qualification targets on those immutable fields or demand a parent-array workaround. A governed dependent claim likewise needs no duplicate target.

Check temporal scope on separate historical assertions too, distinguishing their document date from their event date. Alternatives are mutually exclusive assignment bundles, not values to combine or use to fill adopted nulls.

Distinguish the written/provisional expression from an adopted quantity: preserving an explicitly provisional written operand while the adopted amount is held is not automatically an independently usable numerical assertion. Require an additional restriction when a separately adopted or reused claim is not governed by the existing one, not merely because another field is targetable.

Use stable target IDs and relative named-field paths from the shared standard. Nested named paths are valid; numeric array positions are not the portable qualification contract.

Inspect accounting dependencies as well as numbers: recap membership, completeness, derived operands, function, denominator/population/period and acyclic dependence. Preserve numerical guards for details versus recaps and repeated witnesses.

Before demanding an extra guard, identify the unsafe use still allowed by the actual functions, dimensions and dependencies. Correct typing needs no duplicate warning, but does not itself resolve overlap between independently usable amounts. Do not demand a second restriction merely to distinguish already-typed counts, rates and a single recap; a generic warning in prose is not itself evidence of a missing guard.

The documentary-correspondence extension is relation-local: consult its runtime gates; count mapping does not establish rate mapping. A generated non-additivity group alone authorizes neither aggregation nor selection of a representative.

## 3. Close the whole-source review

Before deciding, revisit each inventoried part and clause. For each material assertion, identify its usable structured path, effective uncertainty restriction, or finding. A part listed as read is not yet accounted for.

Finding one defect does not end the review: return all material findings established across the supplied original together, including independent omissions. If evidence or validation prevents finishing, state the unassessed scope rather than claim whole-source closure. Keep this check concise; a second transcription is unnecessary.

Use the assignment's pinned validator and preserve its full exact-bound report. A pass requires a dictionary with literal `valid is True` and an empty `errors` list; no exception is not a pass. Mechanical failure may block review but is not automatically a scientific defect. Mechanical success does not establish coverage or scientific correctness. Tool execution, reuse and recovery belong in [REVIEWER_JOB_AND_THROUGHPUT.md](REVIEWER_JOB_AND_THROUGHPUT.md).

## 4. Return a precise decision

Use the assignment's established decision schema, with:

- **Bindings and disposition:** source/revision/record hash, original hash, instruction/tool versions; sound, material correction needed, or blocked/disputed in the permitted vocabulary.
- **Coverage and checks:** supplied parts examined, material queries checked, mechanical report reference, and any unavailable evidence or unassessed scope.
- **Each finding:** error/lesson family, exact affected object/field, original span, observed assertion, supported correction, material query/use impact and permitted equivalents. Separate confirmed defects, unresolved interpretations and cosmetic suggestions. Group repeated instances while listing all affected exact versions/paths.
- **Next action:** smallest supported repair and what independent re-review must verify. Do not prescribe unsupported values merely to make feedback concrete.

For example: “On [bound version], link X encodes intermediary where `ki … -ta` identifies the source. ‘From whom?’ returns the wrong party. Restore source or an equivalent explicit scoped relation; preserve the separate `giri3` intermediary and recheck receipt/amount attachments.” Fill actual bindings and spans; this pattern is not a finding about an uninspected record.

For sound work, keep the result compact; completed review need not be retold line by line.

A finding is an evidence-based claim, not authority by assertion. If challenged, recheck the original, raw record, allowed equivalent and consequence. Explicitly withdraw wrong findings without erasing valid ones or treating one withdrawal as acceptance of everything. Escalate genuine disagreements with both cases; do not promote a disputed rule into later returns. Keep independent sound work moving through the authorized workflow.

## Worked review route

Read the full originals before records/keys through `APPENDIX_NAVIGATION.md`. The shared standard introduces the examples; use these review probes:

- **P100877:** follow `entry1`'s 32 sheep, source and custodian links, and `q1/reason1`, `q2/reason2`, `q3`. Custodian changed to owner is material; absent date or unresolved genre alone is not incomplete coverage.
- **P100917:** follow the posting's exact native purpose and scoped month/royal standard. Do not demand a separate flock entity when the valid native-purpose structure already preserves the supported meaning.
- **P101929:** inspect both faces as one transfer. Source, recipient and `giri3` intermediary stay distinct; a supported standard need not appear redundantly in multiple forms.
- **P122885:** inspect every tablet, envelope and seal line. Test envelope-only affiliation, storage direction, seal owner/title/parentage and explicit sealing separately, along with rate/count correspondence and detail/recap/repeated-witness guards. Matching totals do not authorize unconditional collapse. This packet is a semantic walkthrough, not an accepted canonical record.

Instructional provenance never accepts another exact version. Use `appendix/reference/FORMAT.md`, the `appendix/reference/RUNTIME_ENCODING_ADDENDUM_V1.md` and current adjudicated lessons when consequential field or equivalence questions arise.
