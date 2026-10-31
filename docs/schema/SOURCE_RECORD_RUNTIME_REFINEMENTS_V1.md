# Runtime refinement 1: examined lost entry content

The frozen design is preserved unchanged in its original specification directory. This release schema refines only entry.items and entry.measurements to admit null as well as their existing array types.

Use null only when important source content in that category is genuinely unrecoverable after examination. Each null requires an exact field-targeted qualification, null_reason=unreadable, reasoning, and evidence anchored to the lost original line. Never invent an item, measurement, number, or dimension to represent the lacuna. Omit a field when no assertion is made or it is inapplicable. Unprocessed content remains a coverage gap. Fully examined damage does not alone prevent complete coverage. Independent full-source review confirms the distinction.

Royal standard identity: gur_lugal binds the explicitly attested phrase gur lugal to capacity unit gur without a conversion factor. Owning measurement evidence must include that exact designation. It makes no conversion or cross-source equivalence assertion.

The dimensionless ratio unit is used only for explicitly qualified arithmetic quotient/scaling results. It is never inferred from a bare written coefficient.

## Production refinements: known unit spelling and unassessed document type

Interpreted lexical codes permit hyphens and apostrophes used by the existing bound unit vocabulary (for example ma-na, gu2 and bur'u). Syntax does not authorize a new unit: semantic vocabulary resolution remains required.

For a partial extraction with explicit unprocessed coverage, document_type may be null without an uncertainty qualification when the document type has not been assessed. This is coverage incompleteness, not scientific ambiguity, and does not generate important_uncertainty. An assessed but genuinely ambiguous document type still requires its targeted qualification. Complete records with null document_type still require a qualification. No other material-null requirement is waived.


# Bounded source-record representation refinement

These are representation/mechanical changes. They supply no source interpretation, scientific acceptance or graph admission.

## Exact lost-surface marker

An unreadable reading mark may cite the exact ATF editorial surface marker `$ beginning broken`, `$ end broken` or `$ broken`. The leading `$` and the whole marker text are required. Ordinary prose containing `broken`, `$ blank space`, and other structural labels do not become unreadability evidence. Existing sign-level unreadable notation is unchanged. This allows an examined lost-content entry with null items/measurements and its targeted unreadable qualification; it does not identify what was lost or dictate coverage completeness.

## Open native standard designation

An adopted quantity may optionally have:

    "standard_ref": null,
    "native_standard": {
      "native_term_id": "atf:gur%20AN%20zabar-ta",
      "evidence": ["ev_standard"]
    }

The native ID is generated from the selected exact evidence with the same rule used for item designations. No new registry entry is needed for another attested written standard. `RecordBuilder.native_standard([evidence_id])` generates this object. Pass it explicitly to `native_value(..., native_standard=label)` or attach it to the authored quantity.

- The source author selects the label and its attachment. The helper does not find it, select its meaning or infer an applicable unit.
- `standard_ref` remains for previously bound interpreted standards. It must be null when `native_standard` is present; the two are not silently declared equivalent. Existing records using `gur_lugal` remain valid. A new literal `gur lugal` can use the same open native label shape.
- The selected evidence must reproduce the native ID exactly, including case, suffixes and editorial marks. The literal designation is available in the review view.
- Mixed native components remain unchanged; no factor, normalized total or cross-standard equivalence is supplied.
- Arithmetic compatibility retains the exact native label identity. Missing/different labels do not silently become the same standard. A derived quantity cannot drop/change its input standard. Matching literal labels are only a mechanical prerequisite; scientific support for arithmetic membership remains separately required.
- If the quantity or its governing standard is materially uncertain, use the existing targeted qualification/withheld-adoption rules. A material ambiguous/unresolved target at `/adopted/native_standard` (or its native-term child) withholds the quantity and its calculated dependants from adopted analysis, using the existing target mechanism. This field is not an uncertainty bypass.

## Anchored occurrence ordinal

An entry or calendar formula may optionally contain the existing anchored ordinal shape:

    "occurrence": {"value": "2", "evidence": ["ev_occurrence"]}

Use the containing entry/date ID and `/occurrence/value` as a qualification target. `value` is an explicitly authored positive integer string, exact native-term value, or a qualified null. Evidence remains compulsory. The schema does not calculate an ordinal from the text or adopt a reading.

P132818's author can attach the source-local second-occurrence phrase to its entry. For P135852/P201302, occurrence belongs inside the calendar formula object; it is not `year_number`. An authored ninth-occurrence interpretation of the literal ten-less-one formula must retain that exact evidence and its reasoning. The written year formula remains complete. Occurrence produces no amount, duration, date offset, event count or automatically reconstructed missing prior events. Absence of the field asserts no ordinal.
