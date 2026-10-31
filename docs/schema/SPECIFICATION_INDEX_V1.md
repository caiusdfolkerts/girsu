# Girsu source record conventions, proposed version 1

Status: design complete enough for an implementation pilot; not activated. The live pipeline and graph have not been migrated. This specification is a clean, standard, searchable extraction of information valuable for identity and accounting, linked to the text and carrying qualifications that affect its meaning.

## One record, six sections

- **document**: exact original version, edition, physical parts and evidence anchors, dates, purposes, extraction coverage and important uncertainty references.
- **mentions**: source-local people, groups, institutions, places and other named participants; literal reading and conservative searchable form.
- **relations**: parentage, titles, affiliations, local coreference and other supported local relationships, with explicit endpoints.
- **entries**: documentary actions, participants, items, quantities, rates, totals, calculation operands and their scope. An asserted transaction is distinguished from an obligation or documentary reference.
- **qualifications**: sparse, targeted records for substantive inference, ambiguity and limits on use. Qualitative support is well_supported, ambiguous or unresolved. No numeric confidence scores.
- **reasoning**: one concise explanation for each substantive inference or shared inference pattern, linked to evidence and premises.

The convention documents below jointly define one contract. Their division into files is for readability, not separate worker formats or separate tools.

## Authoritative design files

1. CORE_REFERENCE_CONVENTIONS_V1.md: identifiers, original versions, anchors, references, coverage and canonical bytes.
2. IDENTITY_CONVENTIONS_V1.md: mentions, relations and participant roles.
3. ACCOUNT_VALUE_CONVENTIONS_V1.md: items, exact quantities, rates, membership and calculations.
4. QUALIFICATION_REVIEW_CONVENTIONS_V1.md: qualifications, nulls, alternatives, reasoning and review presentation.
5. TEMPORAL_PURPOSE_CONVENTIONS_V1.md: dates, periods, purposes and their scope.
6. DOCUMENT_ENTRY_CODES_V1.md: document, entry and action codes.
7. LEXICAL_TERM_CONVENTIONS_V1.md: open attested vocabulary within the fixed record structure.

SOURCE_RECORD_SCHEMA_V1.proposed.json expresses structural requirements. SOURCE_RECORD_SCHEMA_SEMANTIC_RULES_V1.md lists checks that a JSON schema alone cannot establish. These include reference resolution, original-text fidelity, reduced fractions, arithmetic and scientific support.

## Important invariants

- One authoritative quantity and explanation; later views and prose are generated or reference them.
- Explicit links attach a title, quantity, rate, date or qualification to its actual subject. Nearby placement does not imply attachment.
- A well-supported reconstructed value may be adopted with evidence and reasoning. An ambiguous value stays null in the adopted field, with alternatives kept separately.
- A bare grain coefficient does not become a count quantity merely because a parser represents it that way.
- Native mixed-unit vectors stay intact. Conversion requires an explicit supported standard.
- Calculation inputs have one authority. Recaps and details cannot be silently double-counted.
- Every important ambiguous or unresolved qualification appears in the document-level uncertainty list. Clear facts elsewhere remain usable.
- New attested words can enter without a code change. Their interpretation and equivalence still require review.
- Coverage completeness means extraction has covered the important source content; it does not mean every reading or identity is resolved.

## Evidence from design tests

Three source-linked fixtures, P205120, P133163 and P205530, exercise the complete six-section structure with explicitly partial extraction coverage. They are illustrative excerpts, not new completed texts.

The schema receipt records 33 passing shape tests, including the three fixtures. Separate root checks verify exact originals, anchors, literals, references and selected query/calculation behavior. These include distinguishing equal-name occurrences, assigning patronymics and titles to the right subject, preserving correlated alternatives, calculating 25 + 50 = 75 through explicit membership, and retaining an unmeasured grain coefficient without inventing its unit.

ROOT_IDENTITY_DESIGN_CHECKS_V1.json and ROOT_ACCOUNT_DESIGN_CHECKS_V1.json contain many low-level assertions. Their assertion totals must not be reported as independent scientific cases or as evidence of a measured throughput gain.

## Remaining proof before deployment

A production authoring/review path still needs to implement the semantic rules and generated evidence view, then pass a bounded live pilot with independent scientific review. No runtime validator, migration, staffing change or graph admission is authorized by this design artifact. The user has kept implementation paused while discussing the design.

The existing CONSOLIDATED_SOURCE_RECORD_DRAFT_V1.md and specialist critiques are explanatory history; the seven conventions and proposed schema above control exact field definitions. SPECIFICATION_MANIFEST_V1.json binds the files and checks by hash.
