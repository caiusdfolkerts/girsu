# How Girsu was built

Girsu makes the interpretation of a historical corpus reusable. The output is a collection of structured source records, with an explicit graph of their contents and relationships. Its basic unit is a document read in context, rather than a token matched by a parser or a fact detached from its source.

The production method separates work that requires interpretation from work that should be deterministic. AI agents read the supplied scholarly transliterations, formulate the source-local interpretation and document uncertainty. Code creates and checks the record structure, binds assertions to their evidence and assembles the resulting graph. Separate reviewing agents examine the interpretation against the source. The published data preserves the actual decisions and exceptions made in that process.

This account describes the scientific workflow. The queue and parallel agents explain how that workflow was carried out at scale. File-transfer and recovery machinery is omitted here because it is not required to understand or use the resulting interpretation.

## Coordinate parallel work

The corpus was handled as queued source tasks rather than one long undifferentiated generation. Interpretation agents worked on separate sources in parallel, while review agents examined submitted versions. Task ownership and source reservations kept assignments explicit. A submission bound the record and its review to an immutable source version rather than to whatever happened to be present in a working file.

This organisation separated throughput from scientific authority. Completing a job, uploading a record or passing a structural check did not itself constitute acceptance. Review decisions identified the version examined, and correction work produced a successor rather than silently changing the object under review.

The method did not depend on one fixed number of workers. The useful unit of parallelism was an independently assignable source task, with the authoring and review obligations appropriate to that source. The published provenance retains the actual route, including the authorised self-check exception described below.

## Begin with a fixed source

The input to an authoring task is a particular version of a digital source text. A source identifier alone is insufficient because editions, formatting and stored copies can differ. The record therefore binds the complete supplied text by its SHA-256 hash, byte length and encoding.

This text is a scholarly transliteration, not a new reading of a tablet photograph. ATF carries the published readings together with conventions for surfaces, lines, seals, damage, restoration and uncertainty. The interpretation stage works from that supplied edition. Where a record uses another source as supporting evidence, the supporting text receives its own exact binding.

Source selection is defined at catalogue level. The registered Girsu set was subsequently reconciled against the preserved catalogue, while interpretation coverage is assessed separately. The Girsu site group has 19,208 registered sources with saved text. Catalogue entries without saved ATF remain in a separate appendix. Source selection, the availability of a text and completion of its interpretation are recorded separately. [Sources](SOURCES.md) explains the upstream collection and the evidence for its selection.

## Read the document before representing its parts

The authoring protocol requires reading the whole supplied source, including closing clauses, seal legends and envelopes. This matters because an entry's meaning can depend on a heading, a final verb, an official's title or a period stated elsewhere in the document. Reading isolated lines can produce correctly copied words attached to the wrong action or scope.

The author then represents the document in six principal sections: document, entries, mentions, relations, qualifications and reasoning. The document section describes the source and its parts. Entries express its local structure, including details, groups, totals, balances and calculations. Mentions preserve written occurrences. Relations state how those occurrences and entries are connected. Qualifications and reasoning explain what is supported, what is uncertain and why.

The author supplies the interpretation. The record-building helper generates identifiers and anchors and checks the mechanical contract; it does not decide what the text means or approve its own output.

An entry is not assumed to be a transaction. A subtotal can summarise several entries, an account can include both obligations and deliveries, and a seal can identify someone without stating that they physically transferred the goods. The record has to preserve these differences because subsequent analysis depends on them.

Similarly, a personal name is initially an occurrence in this source. A source can support local coreference, kinship, a title or an affiliation. Those relationships are recorded where justified, but a familiar spelling does not automatically identify the bearer with a person in another document. The release deliberately stops short of global identity resolution.

## Make assertions addressable

The interpretation is encoded in objects whose roles and references are explicit. A person participating in an entry has a role such as recipient, supervisor or witness. A place can be an origin, destination or storage location. A date can apply to the whole document, one entry, a service period or a referenced event.

These attachments are assertions in their own right. A date written at the end of a tablet does not necessarily date every event mentioned in it, and a title in a seal does not automatically describe the transaction role of its bearer. Making the attachment explicit lets a reviewer inspect it and a program query it without reconstructing the argument from prose.

The small controlled vocabularies make common structures accessible, but they are not treated as an exhaustive description of Sumerian institutions. Where a standard code is inadequate, the source's native term or an explanatory native label remains in the record, alongside its endpoints and evidence. A relation marked unclassified can still carry substantial positive content. The release does not force those labels into a new set of research categories.

Each object can be addressed by source, immutable record version and JSON pointer. This includes components without their own local identifier. A researcher can therefore cite a particular quantity, participant link or qualification rather than referring only to an entire document.

## Bind the interpretation to passages

Evidence anchors point into the exact supplied source. They use physical lines, token ranges and, when needed, positions within a token. An assertion can cite several passages, and several assertions can share a passage.

The distinction between text and interpretation remains visible. A copied written expression, an adopted quantity and the reasoning that connects them are different parts of the record. An argument based on a restored reading retains that dependence. An inference using context can cite both the immediate phrase and the premise that supplies its scope.

Reasoning is retained as source-specific explanation, with references to evidence and other premises. It is not reduced to a numerical confidence score. This allows later readers to ask whether an interpretation follows, whether a qualification applies to their intended use, or whether a different reading changes a result.

Anchoring does not by itself make an assertion correct. It makes the assertion inspectable. That distinction is essential to both the review process and the use of the resulting data.

## Preserve the structure of quantities and accounts

The quantitative model distinguishes the written expression from the quantity or rate adopted by the interpreter. Numbers use exact rational strings. Native units remain explicit, including mixed-unit vectors, and a standard is not treated as a conversion factor unless the required rule is actually established.

Rates preserve their numerator, denominator, relevant population and any stated time basis. An absent time basis does not silently become “per day.” An unreadable value is not zero. A group of people is not automatically an instruction to add every quantity attached to its members.

Totals require explicit membership. The record identifies which measurements contribute and whether that membership is complete, partial or unresolved. Calculations retain their operation and ordered inputs. The system can then distinguish a sum from a subtraction, a recorded balance from a computed check, and an independently written total from a consequence derived from other entries.

Documentary repetition is handled separately from arithmetic. When a tablet and envelope represent the same goods, both witnesses remain available, but the represented goods should not be counted again simply because they appear twice. P105740 provides a concrete example: two one-sheep details support a two-sheep total, and the corresponding documentary witnesses remain linked. The arithmetic scope is part of the interpretation, not something inferred from numerical coincidence during a later query.

P102673 illustrates another distinction. Its supported restored counts are 1, 1, 2 and 2. They support an encoded conditional schedule of 177. The written principal remains 217 and its discrepancy remains 20; a calculated path totalling 237 is retained as a diagnostic, not substituted to make the figures agree. A plausible restoration needs source support. An account's desired balance cannot supply that support by itself.

## Represent uncertainty where it belongs

Uncertainty is attached to a particular assertion or field. A damaged name does not make every quantity on the tablet doubtful, and an uncertain rate should not be hidden in a general note while the numerical field is presented as definite.

A qualification identifies its targets, the kind of support and the reasoning behind it. Alternatives can assign several fields together. This is important when two interpretations change both a value and the relationship that gives it meaning: selecting individual fields from incompatible alternatives would invent a third interpretation.

The method permits supported restoration and source-local inference. It does not demand that every usable value be physically intact. At the same time, a title cannot supply missing syllables of a name, and arithmetic agreement cannot alone prove a reconstruction.

Missing optional structure, an explicit null, an empty collection and zero remain distinct. The source may not write something, the text may be unreadable, the interpretation may be unresolved, or a field may be inapplicable. The record preserves those differences where they are material.

## Check the record, then review the interpretation

Technical validation checks whether the record follows its structural contract, whether references and anchors resolve, and whether its explicit quantitative operations and qualifications are represented consistently. Passing those checks is necessary for a usable record. It is not scientific acceptance.

The review workflow then asks a separate agent to examine the whole bound source and its structured meaning. The review contract requires confirmation that the complete original was reviewed, that the structured meaning was checked and that the qualifications were checked. Particular attention is paid to attachment, operators and units, documentary stage, arithmetic membership and the justification of adopted inferences.

A finding should identify the exact source version and field, explain the problem, cite the evidence and state the required correction. A cautious sentence in a note does not repair a definite field that expresses the wrong meaning.

This is independent review within an agent workflow, not independent human Assyriological peer review. The release also contains a specifically authorised cohort of 623 sources finalised through author self-check rather than a separate current reviewer decision. Historical audits and holds remain recorded. The documentation does not treat all current records as having the same review status; the exact populations are described in [Provenance](PROVENANCE.md).

## Revise without losing the earlier claim

Corrections produce successor versions tied to the record they replace. A submitted or accepted interpretation is not silently rewritten. Version-bound findings, decisions and retained history make it possible to determine which claim was reviewed and which record a correction affects.

Some canonical records were produced by converting earlier accepted source-local interpretations into the common schema. That route preserves their prior scope and restrictions. Conversion is not new interpretation of a previously unread text and does not earn new-source credit. A converted record can remain partial even when the conversion itself is faithful.

This distinction prevents a successful format migration from being reported as new historical work. It also keeps source coverage meaningful: possessing a record, preserving an earlier interpretation and completing a whole-source reading are different achievements.

## Assemble the graph from the records

Once interpretation has been recorded, assembly is a programming task. The graph exposes the objects already encoded in the canonical records and follows their explicit typed references. It includes addressable components without local IDs, preserves multi-party relations, and distinguishes containment from historical assertions.

The preserved evidence representation contains 5,073,009 nodes and 8,683,442 incidences across all 18,412 selected records, including the three archival records. These are views of the same source content, not millions of independent historical facts.

Documentary citations and shared vocabulary help connect and navigate the collection. They do not automatically merge people, events or goods. An exact reference to another record must resolve to the specified version rather than silently substituting a newer interpretation. The release retains unresolved documentary boundaries where the original text exists but the required canonical target does not.

## Publish one usable default

A researcher needs a consistent view to work over. The release therefore supplies a precomputed default for each selected record while preserving the canonical evidence and alternatives.

The default policy operates on existing interpretations. It can prefer a source-supported restoration or an explicitly supported branch where its bounded rules establish the target and justification. It does not choose by option order, by the mere presence of one option, by a blanket preference for an edition, or by which reading makes an account balance. If it cannot establish a preference, an affected target can be null.

A selected branch remains qualified. A held branch retains its explanation and evidence pointers. Dependent calculations are recomputed where supported or withheld where they would otherwise become stale. Record, search and graph access all use the same materialized default.

The current policy examined all 3,537 structured alternative sets and selected 26 typed choices, with one further bounded prose choice. The other 3,511 typed sets remain held. These are results of a deliberately limited rule system, not a claim that code has understood every argument in the reasoning prose. [Default policy](DEFAULT_POLICY.md) gives the detailed contract.

## What the method contributes

The result is an interpretation corpus that can support many investigations without being rebuilt around each one. A researcher can formulate a question, retrieve the relevant assertions, inspect their qualifications and gather a dossier whose members retain exact source references. Targeted identity or account reconstruction can then be carried out where the question requires it.

The contribution is the combination of source-level interpretation, explicit uncertainty, reviewable evidence and deterministic access at the scale of this corpus. With 18,409 current interpretations, the project makes a substantial body of documentary understanding available for systematic computation. The evidence and argument behind a field remain part of the resource, so computation can operate on interpreted meaning without severing its connection to the text.

The repository publishes the resulting data and the tools needed to read it. It is not a claim that the original AI authoring run can be reproduced bit for bit from a reader command. [Validation](VALIDATION.md) describes the checks on the released representation, while [Sources](SOURCES.md) and [Provenance](PROVENANCE.md) document the evidence and version history on which it rests.

The production account above is based on the preserved [source-first workflow](https://github.com/caiusdfolkerts/ur-reconstruction/blob/accb42db04a09233dc6795afab58ed041ab0b68d/pipeline/source_first_v1/README.md), [operating protocol](https://github.com/caiusdfolkerts/ur-reconstruction/blob/accb42db04a09233dc6795afab58ed041ab0b68d/pipeline/source_first_v1/OPERATING.md) and [method conventions](https://github.com/caiusdfolkerts/ur-reconstruction/blob/accb42db04a09233dc6795afab58ed041ab0b68d/pipeline/source_first_v1/METHODS.md), read alongside the released provenance and validation records. The protocols describe the workflow; the per-version ledgers establish what happened to a particular record.
