# Core reference conventions V1

Design only, 2026-10-20. Proposed exact encodings for the six-section source record. No implementation, scientific migration, acceptance, queue, alias or graph change. Identity, account, qualification and document-domain files supply their own finite enums and field types; root synthesis must combine them into one dictionary before declaring a schema executable.

## 1. Root and document dictionary

The root has exactly six required keys. `document` is an object; the other five are arrays:

```json
{"document":{},"mentions":[],"relations":[],"entries":[],"qualifications":[],"reasoning":[]}
```

Required document fields:

| Field | Exact encoding |
|---|---|
| `schema` | Proposed identifier `"ur.source_record.v1"`. |
| `id` | `"d1"`. |
| `source_id` | Catalogue source ID, e.g. `"P132285"`. |
| `source_version` | `{sha256,bytes,encoding}`: lowercase 64-character SHA-256, nonnegative integer byte count, `encoding:"utf-8"`. Binds the entire original once. |
| `edition` | Edition/catalogue designation string, or `null` when unavailable. |
| `revision` | Positive integer; first record is 1, explicit successor is predecessor revision + 1. |
| `supersedes` | `null`, or exact predecessor record reference below. |
| `document_type` | Document-domain genre code, or `null` when unresolved. Genre enum is defined once in the document-domain convention. |
| `parts` | Array of physical parts below. |
| `evidence` | Array of interned evidence records below. |
| `dates`, `purposes` | Arrays of document-domain records. |
| `coverage` | Declaration in section 6. |
| `important_uncertainty` | Checked generated array of qualification IDs, sorted lexicographically under the qualification convention. |

No filesystem path, expiring URL, parser diagnostic or review/delivery status is a scientific source identity. An external resolver locates the source by its exact binding. Loading different bytes under the same source ID is an error. Unknown keys are rejected by the final integrated dictionary, not silently interpreted.

### Revision identity and effective selection

An exact external record reference, also used by `document.supersedes`, is:

```json
{"source_id":"P132285","revision":2,"sha256":"<canonical record hash>","bytes":12345}
```

The referenced record must match all four values. A successor retains the same source ID; any changed source edition/bytes must be explicitly bound and all affected anchors rechecked. Each revision is a complete record, not an inherited patch. Local IDs for continuing objects remain stable.

The record never contains its own hash. Its externally computed canonical-byte hash is bound by submission/review receipts. Effective scientific selection uses those exact accepted version/scope bindings. Revision number, filename, timestamp or an unreviewed supersession does not imply acceptance. Conflicting or incomplete selection stays unresolved; old records remain retrievable. No self-hash recursion or “latest wins” rule.

## 2. Local IDs and physical parts

Every addressable object has a source-local ID matching `[a-z][a-z0-9_]*`, unique throughout the record, including nested objects. Suggested IDs: `d1`, `p1`, `ev1`, `m1`, `rel1`, `e1`, `date1`, `purpose1`, `item1`, `measure1`, `membership1`, `calc1`, `link1`, `q1`, `reason1`. Prefixes help readers but do not replace type checks.

References are local ID strings, never array positions or unversioned external names. An independently referenced/qualified nested object has its own ID. Plain object fields can use stable field paths without extra IDs. IDs persist across corrections to the same object, are not renumbered after reordering and are never recycled for another occurrence. Splits/merges are explicit reviewed version differences. Equal spelling is not identity. External identity of a local object is its exact record reference plus local ID.

Physical part:

```json
{"id":"p1","kind":"tablet","parent_id":null,"line_ranges":[{"start":3,"end":15}]}
```

Kinds: `tablet`, `envelope`, `seal`, `composite_seal_legend`, `block`. A block is physical, not a semantic group. A written seal reference is not an actual seal part. Ranges are one-based physical lines, start inclusive/end exclusive, sorted, nonempty and nonoverlapping. A child's ranges must lie within its parent's; parent links are acyclic. Multiple top-level parts may have null parents. These ranges never imply additive membership or contextual inheritance.

## 3. Evidence and exact indexing

Intern evidence once in `document.evidence`; domain fields named `evidence` contain arrays of evidence IDs. No inline competing anchor format.

```json
{"id":"ev1","spans":[{"line":6,"token_start":0,"token_end":3}]}
```

Rules:

1. Verify original bytes/hash before strict UTF-8 decoding. No Unicode/transliteration normalization.
2. Physical lines are one-based and count headers, directives, comments and blanks. Split on LF; exclude CR when it is part of CRLF. A terminal LF does not create an additional blank line.
3. Strip a printed numbered-line prefix only when it matches `^[ \t]*[0-9]+[A-Za-z'′?]*\.[ \t]*`. This includes uppercase/lowercase suffix letters, ASCII apostrophes and U+2032 prime marks supported by the saved source-census convention, plus queried labels. Otherwise use the whole line content. Printed labels are not physical addresses.
4. Tokens are maximal nonempty runs separated by ASCII space/tab. Keep brackets, query marks, determinatives, suffixes and corrections unchanged.
5. Token indices are zero-based; end is exclusive. Require `0 <= token_start < token_end <= token_count`. Each span stays on one line. Multiline/discontinuous evidence uses source-ordered nonoverlapping spans. Combine adjacent whole-token spans on the same line.
6. Empty lines have no token evidence. Physical extent uses part ranges; a written `$ 1 line blank` marker can be token evidence.
7. Exact occurrence extraction joins selected tokens with one space and separate spans with LF. This defines a literal token sequence, not original whitespace. The original remains available. A domain `literal` representing an exact occurrence must match this extraction.

Strict one-token substring extension:

```json
{"line":12,"token_start":1,"token_end":2,"character_start":0,"character_end":18}
```

Both character keys appear together, only with `token_end=token_start+1`. Offsets are zero-based/end-exclusive Unicode code points in the raw token, not bytes or graphemes. Require a nonempty in-bounds strict substring. Whole-token spans must omit both keys; a redundant full-token character range is invalid. This permits an exact name without its attached case suffix. It does not normalize evidence.

## 4. Stable qualification targets and explanation links

```json
{"record_id":"measure1","field":"/adopted"}
```

`record_id` resolves to one local object. `field` is a nonempty RFC 6901 object-field pointer relative to it (`~0` for `~`, `~1` for `/`). Every traversed segment is an object field, never an array index. Empty-root paths, wildcards, `-`, ranges and dangling fields are invalid. The integrated domain dictionary declares allowed target fields.

An array-valued field may be targeted as a whole only where its domain permits that interpretation. To qualify one array member, target that object's own ID. IDs, source bindings and exact raw transcription are not candidate replacement targets. Applicable unresolved adopted fields are explicitly null, so their targets exist; genuinely inapplicable optional fields are omitted.

Candidate assignments use the same target and its ordinary field type:

```json
{"target":{"record_id":"link1","field":"/ref"},"value":"date1"}
```

Candidates never fill a main null automatically. Correlated assignments stay in the mutually exclusive options specified by the qualification convention.

Authoritative explanation direction: `qualification.reasoning_ref -> reasoning.id`. Reverse target/reason indexes are generated. `reasoning.premise_refs` contains local justification-input IDs, not a second target/operand list. Exact external standards or other permitted evidence use their designated typed domain references, not arbitrary external strings disguised as local IDs.

## 5. Direct attachments and calculation links

Every direct attachment has required fields `{id,ref,role,evidence}`. Evidence is a nonempty array of local evidence IDs. `ref` is an allowed local ID, or null with a qualification on `/ref` when applicability is unresolved. A materially unresolved role is null with a qualification on `/role`. The sole conditional extra field is `native_label`, required only where the domain permits role `unclassified`; it uses that domain's anchored-label type.

```json
{
  "id":"e1",
  "dates":[
    {"id":"link1","ref":"date1","role":"document_date","evidence":["ev2"]},
    {"id":"link2","ref":"date2","role":"service_period","evidence":["ev1"]}
  ],
  "places":[
    {"id":"link3","ref":"m3","role":"origin","evidence":["ev3"]},
    {"id":"link4","ref":"m4","role":"destination","evidence":["ev4"]}
  ]
}
```

This is an entry fragment; complete records include the required domain fields.

| Attachment array | Allowed reference home |
|---|---|
| `entry.participants` | Mention or explicitly permitted semantic-group entry. Role is local to this entry. |
| `entry.dates` | `document.dates`. Application role is on this link, not duplicated on the date. |
| `entry.places` | Place-kind mention in `mentions`. |
| `entry.purposes` | `document.purposes`. |

Roles have finite domain enums. The attachment evidence binds its applicability; substantive inferred application additionally needs qualification/reasoning. A clearly read date/place alone does not establish entry scope.

Entry links are the sole membership authority: no reverse authored covered-entry list, context bundle, header default or override precedence. A helper may attach references to explicitly selected entries; the stored result is these ordinary links. Repeated evidence may be folded in a generated review view. Duplicate `(entry,array,role,ref)` pairs are invalid. Different roles coexist; unresolved same-role competition is never resolved by first/last position.

A collective quantity remains collective. Referencing it repeatedly neither distributes the amount nor creates events, memberships or credit.

For recap calculations, membership owns operand IDs and the recipe references `membership_id`. Standalone reconstruction recipes own explicit ordered inputs. Reasoning may cite those records without duplicating operands. Dependencies are acyclic; a result cannot independently prove its own input. The account convention owns the single exact rational/unit/vector/recipe representation.

## 6. Coverage and absence

```json
{"status":"complete","gaps":[]}
```

```json
{"status":"partial","gaps":[{"id":"gap1","evidence":["ev9"],"reason":"unprocessed"}]}
```

Exactly these coverage fields. `status`: complete/partial. Each gap has ID, nonempty evidence array and `reason`: unprocessed/not_modeled. Gaps are empty exactly when complete. Complete means the author declares important source material extracted within this design; scientific review still checks it. It does not mean intactness or resolved interpretation.

Unreadable/restored text may be fully examined and represented by a qualified null, without being an extraction gap. Distinctions:

- Supported applicable field: typed adopted value.
- Material interpretation intentionally withheld: null plus exact qualification; `null_reason` follows the qualification convention.
- Genuinely inapplicable optional field: omitted.
- Unassessed important content: coverage gap, never default-supported or relabelled scientific ambiguity.
- Empty array: no such assertions in covered extraction, not proof the historical phenomenon did not exist. Partial coverage cannot support a complete negative search.

Required sections remain present. Missing required fields are invalid. False, zero, empty array, null and omission are distinct; none is a fallback unit or value. IDs, enum codes, references and exact occurrence literals cannot be empty strings.

`important_uncertainty` is the sorted unique qualification IDs selected by the qualification-domain support/impact rule. Source-condition searches separately index exact transcription/evidence marks, including harmless marks that did not warrant qualifications. Editorial status is not a confidence score.

## 7. Canonical serialization

One UTF-8 JSON object followed by exactly one LF. No BOM, comments, duplicate keys, floats, NaN or infinities. Object keys sort by Unicode code point; no insignificant whitespace. Arrays preserve their declared order. Strings are not Unicode-normalized: escape quote/backslash, use JSON short escapes for backspace/tab/LF/form-feed/CR, lowercase `\u00xx` for other U+0000–001F, and write other characters directly. Surrogate code points are invalid.

Structural integers use base ten, without leading zeros or negative zero. Scientific quantities use the account convention's reduced rational strings. Hash and byte count include the terminal LF. This canonicalizes a given ordered JSON value; it does not infer semantic equivalence, reorder scientific sets or select an accepted version.

## 8. Minimum checks and query defaults

Machine checks: six-root/types/known fields; source hash and anchors; unique IDs and allowed reference types; part containment; stable field targets and candidate types; required null qualifications; attachment uniqueness; coverage consistency; acyclic dependencies; exact account arithmetic; generated uncertainty equality; predecessor/reference consistency. An omitted inference or falsely complete extraction still requires scientific review to detect.

Default analytical queries select the effective exactly reviewed source/version/scope externally, then expose adopted fields and resolved links alongside applicable qualifications/evidence. Candidates, coefficients and known fragments require explicit query modes; none fills a null. Proposed-record search remains clearly proposed and gives no acceptance/credit.

Repeated representations require an explicit supported collapse before addition. Null operands, partial membership or unresolved equivalence cannot be skipped to manufacture a full total. A repeated link/search hit never creates an additional historical entity or completed source.

## 9. Three verified anchor examples

These are design fragments, not fresh scientific acceptance.

**P132285:** 287 bytes; SHA-256 `9edc424197fb2ab3ec595186f5a7a097195da5594e08edbb19d2bc6c7ffcc81d`.

```json
[
  {"id":"ev1","spans":[{"line":6,"token_start":0,"token_end":3}]},
  {"id":"ev2","spans":[{"line":13,"token_start":0,"token_end":2},{"line":14,"token_start":0,"token_end":5}]}
]
```

Expected extraction: ev1 = `a2 hun-ga2 mu-kur2-ra`; ev2 = `iti sze-sag11-ku5` + LF + `mu en {d}inanna masz-e i3-pa3`. Separate document_date/service_period links permit separate queries. An unlinked entry receives neither. Domain reasoning must establish the relative period's base; no numeric year is invented.

**P202040:** 779 bytes; SHA-256 `0aaef1111e17142c792417b938dd9a5a023fd00d7b6d17c9b362627cde512437`. At physical line27, tokens0 and2 are `an-sza-an{ki}-ta` and `nibru{ki}-sze3`. Separate place links retain origin/destination. If applicability is unresolved, link3.ref=null with a qualification while the known place occurrence remains searchable. Nearby entries inherit neither link.

**P205120:** 401 bytes; SHA-256 `367e2e05c4d7e48a99a5dfaaa8d85a46203171eba174539195e15c9bbd5086b5`. At physical line12, token1 is `lu2-{d}nin-gir2-su-ta` (21 code points). The substring span in section3 extracts exactly `lu2-{d}nin-gir2-su` (18). The original view retains the suffix. This does not merge another equal-spelling occurrence.

Additional expected checks: a qualification on link1./ref survives array reorder; `/dates/0/ref` fails. Revision3 proposal does not displace an exactly accepted revision2. Material unprocessed scope prevents a claimed complete extraction even when all present records validate.
