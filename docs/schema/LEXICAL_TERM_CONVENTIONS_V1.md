# Open lexical terms, closed structure — V1 design

Purpose: do not block routine source work whenever an attested new commodity, subtype or written unit appears. This is a design refinement; no runtime change.

## Native term identity

`native_term_id` is generated, not manually invented:

`"atf:" + percent_encode(canonical evidence-token sequence)`

Use the shared exact evidence extraction/token/subtoken convention. For a lexical designation selected from multiple spans, join the selected token pieces with one ASCII space in source order. Preserve case, determinatives, hyphens, sign indices and editorial notation. Percent-encode UTF-8 using uppercase hex escapes; only RFC3986 unreserved ASCII characters remain literal. Thus `udu` is `atf:udu`; `udu niga` is `atf:udu%20niga`.

This identifies an observed written form, not a global commodity identity or a synonym class. No registry approval is needed for a new observed form. Different spellings remain distinct. A generated mark-insensitive search view can find candidates, but may not declare their semantic equivalence.

## Item fields

Keep the account item shape, adding required generated `native_term_id` beside its exact designation evidence. `type_id` remains an adopted coarse semantic code, or `unclassified` for a known concept outside the current coarse vocabulary, or null when the meaning/classification is materially unresolved. Unknown attested terms can therefore pass structural validation without inventing a new semantic enum.

Initial coarse item type codes for the design fixtures/pilot are: barley, sheep, lamb, goat, ox, donkey, sheep_skin, textile, wooden_object, beer, bread, oil, flour, silver, personnel, land, service, unclassified. This is explicitly a small indexing vocabulary, not an exhaustive ontology. The original native designation remains authoritative evidence; important attributes are not erased to force a coarse code.

Attribute keys remain closed as in the account convention. Lexical attribute values may use this same native-term namespace; fixed recognized semantic values use the versioned vocabulary. Grade/age-class numerical ordinals use the stated numeric convention. New lexical values require scientific interpretation but no code/enum change. New attribute keys, semantic classes, equivalences or arithmetic unit meanings require a reviewed convention extension, not arbitrary prose keys.

## Units

Existing interpreted unit IDs and their dimensions remain controlled. An unseen written unit can be retained immediately as a native-term ID in the written expression; it does not automatically gain a dimension, conversion factor or arithmetic compatibility. Until its numerical/metrological use is sufficiently supported, expression rule is unresolved and the adopted measured amount is null with the appropriate qualification.

There is no fallback from an unknown unit to count. The raw coefficient and unit designation remain searchable. Native term identity alone is never enough to sum two quantities as equivalent or normalize them.

## Efficiency consequence

Authors do not maintain a new dictionary entry or ask for a tool change for every new noun. The helper generates the native ID from evidence; science concerns the adoption of a meaning, coarse class or equivalence. Search can retrieve exact forms immediately and broader candidates separately. Only changes to semantic conventions need coordinated review.
