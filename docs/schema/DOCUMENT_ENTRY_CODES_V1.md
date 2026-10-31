# Document and entry code conventions V1

Design-only completion of the shared domain dictionary. No live implementation.

## Document type

`document.document_type` is one of `receipt`, `expenditure`, `account`, `inventory`, `personnel_list`, `legal_record`, `letter`, `other`, or null. `other` means a supported genre outside this small indexing vocabulary; null means an expressed classification remains materially unresolved, with a qualification. Genre is an indexing aid, not a claim that every entry in a mixed source has the same action.

## Entry action

When an action or administrative predicate is represented, `entry.action` is exactly `{id,type,state,evidence}` and optional `native_label` only for type=other. It is independently targetable through its stable ID. `evidence` is the evidence-ID array supporting the predicate/statement.

`type` is one of `receipt`, `issue`, `allocation`, `payment`, `loan`, `return`, `assessment`, `inventory`, `custody`, `obligation`, `discharge`, `document_requirement`, `reference`, `status`, `other`, or null.

`state` is one of `source_asserts_completed`, `stated`, `intended`, `owed`, `referenced`, `unspecified`, or null.

- source_asserts_completed: the source asserts a completed act; it is not independent modern verification of a physical transfer.
- stated: a source states a condition/status/stock without asserting an independently completed act.
- intended/owed/referenced retain those distinct documentary meanings.
- unspecified makes no stronger stage claim; it is not a fallback for an actual ambiguous reading, which is null with a qualification.

An amount alone does not imply an action. Omit an optional action object if no action assertion is made; do not manufacture an uncertainty object for its absence. A material unresolved expressed action/attachment uses the null convention.

The adopted type/state is distinct from quantity and participant roles. A clear receipt can coexist with an unknown amount. A document requirement can coexist with a completed receipt in another entry; it does not make all source actions prospective.

## Roster group

A group entry may have `group_members` as an array of mention/group-entry IDs, or null when the actual member set remains unresolved. Empty group membership is not silently substituted for unknown membership. Candidate sets belong to the qualification. The group graph is acyclic.

This is semantic grouping only. Physical parts are separate; arithmetic operands are held in the account membership object. A group can be a participant/relationship endpoint without distributing a collective predicate or joint amount to each member.

## Remaining shared shapes

Entry kind, items, measurements, rates and arithmetic membership use ACCOUNT_VALUE_CONVENTIONS_V1.md. Mention/kinship/title/status and participant roles use IDENTITY_CONVENTIONS_V1.md. Entry date/place/purpose links use TEMPORAL_PURPOSE_CONVENTIONS_V1.md and the common four-field attachment shape.

Account relation codes are fixed as:
- `repeated_representation`: `{id,type,members,evidence}`, with at least two same-kind entry or measurement IDs. Measurement groups, not merely entry groups, control numerical aggregation.
- `summarizes`: `{id,type,subject_id,object_id,evidence}`, subject a written recap entry, object its authoritative membership ID. Do not duplicate the member list in this relation. This link is optional if the ownership already supplies the exact same meaning; do not author both merely for display.
- `discharges`: `{id,type,subject_id,object_id,evidence}`, subject the stated discharge/settlement entry, object the obligation entry. It does not establish full discharge without the source supporting that scope.
- `balance_of`: `{id,type,subject_id,object_id,evidence}`, subject the balance entry, object the entry/group being balanced. Arithmetic operands remain in membership/recipe objects.

Avoid redundant summarizes relations where the membership is already nested under its owning recap; code derives that link from ownership. These types express source-local relations only, not global account closure or event unions.
