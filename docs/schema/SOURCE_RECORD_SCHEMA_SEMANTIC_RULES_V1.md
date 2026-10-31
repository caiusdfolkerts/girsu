# Checks outside the proposed JSON Schema

Design only. `SOURCE_RECORD_SCHEMA_V1.proposed.json` checks structure and local value syntax. Passing it does not establish scientific acceptance, exact source fidelity, arithmetic correctness or operational readiness.

## Exact source, identity and references

- Verify source byte count/hash and strict UTF-8 before applying the core line/token/subtoken rules. Check span bounds, canonical ordering, strict substring conditions, literal equality and source-part containment.
- Build one local-ID index over every addressable nested record. Reject duplicate IDs, dangling references, wrong endpoint kinds, invalid field targets and traversal through array indices. Part, semantic-group, temporal and numeric dependency graphs must be acyclic.
- Validate the referenced predecessor's exact bytes and source/revision fields. Preserve IDs for continuing objects. Effective acceptance is an external exact version-and-scope selection; never infer it from revision numbers or filenames.
- Resolve candidate assignment targets against the actual referenced field type. Require every assignment target to be declared by its qualification. Mutually exclusive options cannot be combined or promoted to main values implicitly.
- Require a qualification and reason for a material adopted null or substantive inference. Distinguish permitted structural absence from withheld scientific interpretation. Validate reading-mark references against the actual notation.
- Recompute `important_uncertainty` from structured support/impact. Check that every source-condition search remains able to retrieve notation even without a qualification.
- Check attachment uniqueness by owner/array/role/reference. References and their qualifications must survive the effective view. A known date/place does not independently prove applicability.

## Lexical and numerical checks

- Generate each `native_term_id` from its exact designated evidence using the agreed UTF-8 percent encoding. Check decode/re-encode equality; a syntactically valid `atf:` string can still be incorrectly generated.
- Resolve interpreted type/unit/standard codes against the exact shared vocabulary. A matching string pattern is not permission to introduce a semantic class, equivalence, dimension or conversion.
- Reduce rational strings exactly; check denominator positivity and greatest common divisor. JSON Schema cannot prove reduction.
- Evaluate the single expression or derivation authority and require exact equality with its adopted cache. Preserve ordered operators, unknown positions and editorial deletions. A bare coefficient or unknown written unit cannot become a count.
- Verify recipe arity, input types, dimensional meaning and exact standard applicability. Division requires a nonzero supported denominator. Conditional standards cannot create unconditional values.
- Recap recipes resolve one authoritative complete membership list. Unresolved/partial membership or essential unresolved inputs hold a full result. Reconstructed values cannot circularly establish their own premises.
- For numerical repeated-representation groups, check function/subject/unit/value compatibility and retain all evidence. Collapse only supported equivalence; unresolved equivalence cannot be silently doubled or collapsed.
- Validate ordinal-versus-count distinctions and the exact evidence for item attributes. A rate's denominator/population/time basis is not inferred from a nearby amount.

## Scientific review and query behavior

- Full-source review checks completeness, interpretation, omitted inferences and the scope of qualifications. Schema validation cannot prove that a source was read or that a relationship is historically correct.
- A partial extraction's empty sections are not complete negative findings. Unprocessed material remains explicit coverage, not an assessed scientific null.
- Default analysis uses exactly accepted scope and adopted values with applicable qualifications. Candidates, raw coefficients and fragments are explicit separate modes. No projection can fill a null from cautious prose or a parser default.
- Collective facts remain collective. Repeated references, calculations, repeated writings and search hits create no extra historical entity, transfer or source credit.

## Canonical bytes and residual vocabulary dependencies

Canonical serialization is a byte-level requirement outside JSON Schema: reject duplicate keys, noncanonical escapes, alternate number spellings and floating-point syntax even where a JSON Schema implementation treats `1.0` as an integer. Verify UTF-8, key order, array order and the final LF before hashing.

The final integrated convention must bind the interpreted unit/standard vocabulary and any remaining domain codes. The proposed schema's comments identify such dependencies explicitly; they are not waived by a structural pass.

No custom validator or live enforcement was installed with this document.
