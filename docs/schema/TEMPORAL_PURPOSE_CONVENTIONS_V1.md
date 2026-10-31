# Temporal and purpose conventions — proposed source-record v1

Design specification only. Uses the shared source-local ID and evidence-ID conventions. No runtime changes.

## Temporal records: document.dates

Each record has exactly `id`, `kind`, `evidence`, and the fields for its kind. Evidence is a nonempty list of document evidence IDs. `kind` is one of `calendar`, `relative`, `duration`, `interval`.

### calendar

Allowed component fields: `year_formula`, `year_number`, `month_name`, `month_number`, `day`. Omit an unexpressed/inapplicable optional component. An expressed but materially unresolved component is explicitly null and qualified. At least one component or qualified unresolved component must be present.

- A string year_formula is the source's written year designation in the conservative ATF search form, including its event/royal designation. It is not silently mapped to a regnal/Gregorian date.
- year_number is an integer only where a numerical year is actually written and its reference is supported. The formula/reference must preserve what the number counts. A physical source-line number is never a year_number.
- month_name preserves the adopted native month designation. month_number is populated only if explicitly written or independently supported with reasoning; a calendar-specific equivalence is not assumed merely from month spelling.
- day is an integer when a calendar day reading is adopted. A disputed day/duration interpretation remains a candidate bundle, not two simultaneously adopted values.
- Null/omission follows the common field-state convention finalized by the review worker. Absence of a date component is not automatically uncertainty. A damaged, materially unresolved expressed component is qualified.
- No per-record Gregorian conversion or default calendar is required. Future chronology tools may produce a versioned derived alignment without overwriting the source date.

### relative

Fields: `base_ref`, `relation`, and optional `offset`. base_ref targets a temporal record or an explicit source-local event/entry. relation is `before`, `after`, `during`, `at_start`, or `at_end`. Optional offset is `{value,unit}` with a nonnegative canonical exact rational value and unit `day`, `month`, or `year`; direction comes only from relation. Do not require or invent a numeric offset for an unquantified clause such as “when the chief minister was seated” (P106899 physical line24). Unsupported base_ref is null and qualified; do not attach to an arbitrary closing date.

Example: source P132285's mu-kur2-ra supports a following-year period. A relative-year offset can be linked to the documented year context when supported, with concise reasoning. It does not change the receipt into a future receipt.

### duration

Field: `measurement_ref`, referencing the one authoritative duration measurement. Do not store another separately editable length here. The measurement holds its native expression/unit and qualifications.

### interval

Fields: `start_ref`, `end_ref`, referencing temporal records. Either can be null if materially unresolved, with qualifications. Preserve stated endpoints; do not infer inclusive/exclusive arithmetic unless it is needed and supported in an explicit derivation.

## Entry time attachments

`entries[*].dates` holds objects `{id,ref,role,evidence}`; evidence contains exact evidence IDs supporting this attachment. Ref points to a temporal record, or null with a qualification/candidate when applicability itself is unresolved. Role is one of:
- document_date
- entry_date
- service_period
- due_date
- duration
- reference_date

These are attachment roles, not a second date-kind field. document_date means the entry is documented by the closing date; it does not automatically date the described action, an earlier subaccount or an obligation. The same date object may be reused by several entries with explicit links. No implicit inheritance from document order or part containment.

P132285 can have links to a closing calendar date and a relative service period. P361899 can have two separate calendar formula objects, one referenced/internal and one closing; the formulas occur at physical lines11/14 but contain no numerical years11/14. P202040's closing month does not resolve an ambiguous route-to-person attachment.

## Place attachments

`entries[*].places` holds `{id,ref,role,evidence}`. Ref targets a place-kind mention. Role enum:
- location
- origin
- destination
- storage_location
- reference_location

A clearly read place can remain an adopted mention while a particular entry's applicability is null/candidate. No source-site label is automatically copied into transaction location.

## Purpose records: document.purposes

Fields: `id`, `category`, `native_term`, `entity_refs`, `evidence`.

Category enum:
- remuneration
- subsistence
- travel_provision
- animal_feed
- production
- construction
- institutional_service
- ritual_or_festival
- debt_or_obligation
- other

`native_term` is an anchored designation/search term, not explanatory prose. Preserve economically important qualifiers through controlled item/entry attributes or qualifications, not a long custom category name. `other` means a known purpose not in the coarse code list; retain its native term and relevant entity references. A materially unresolved category is null with a qualification; candidates belong in qualifications. This bounded coarse vocabulary is an indexing aid, not a reason to drop important information or claim a new scientific classification without support.

`entity_refs` points only to relevant existing mention/group IDs, with precise role/relationship records if needed; do not infer personal affiliation from a purpose phrase. `entries[*].purposes` uses `{id,ref,role:"purpose",evidence}` links to these records. Purpose applicability is separate from recognizing the purpose itself.

## Required convention checks

1. Calendar date, relative period and duration remain distinct.
2. One duration has one measurement authority.
3. Direct role-labelled time/place references survive reordering; unrelated entries receive nothing.
4. Physical-line anchors cannot populate temporal numeric values.
5. Uncertain applicability produces an unresolved link, not a false shared date/place.
6. A known month name does not silently select a calendar or numeric month equivalence.
7. Purpose categories remain coarse; exact native designation/evidence and material qualifications remain available.

These are proposed finite conventions for expert cross-check, not finalized production vocabulary.
