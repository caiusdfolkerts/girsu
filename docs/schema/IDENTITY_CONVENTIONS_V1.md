# Identity conventions V1 — design fixtures, not scientific successors

Prepared from the complete saved P205120 and P133163 originals and the identity lane's repeated extraction costs. This file changes no code, queue, graph, packet, membership or review status. The two JSON records are **partial design fixtures**, not full source extractions or renewed acceptance of the historical readings. The six root keys remain `document`, `mentions`, `relations`, `entries`, `qualifications`, `reasoning`.

Use the shared core evidence/ID convention and the verifier's qualification convention. The document wrapper, parts, coverage and evidence follow CORE_REFERENCE_CONVENTIONS_V1.md; entry kind is detail under the shared account convention. This file owns the exact identity fields and endpoint semantics below. The companion JSON files are canonical serialized design fixtures, with expected query results in IDENTITY_EXPECTED_QUERIES_V1.json.

## 1. Occurrences; no second person layer

A mention has exactly these required fields:

| Field | Type and rule |
|---|---|
| `id` | Source-local stable string, unique across this record. Do not renumber retained mentions in a correction. |
| `kind` | One of `person`, `unnamed_role_holder`, `collective`, `institution`, `place`, `deity`, or null when entity classification itself is withheld. |
| `literal` | Exact core-extracted source string: one space between selected tokens and LF between selected spans. Preserve signs, determinatives and editorial marks. |
| `search_form` | Conservative normalized string, or null if no supported lexical selection/reading is adopted. |
| `part_id` | Existing source-part ID. |
| `evidence` | Nonempty array of interned evidence IDs. |

A mention is a written occurrence, not a person profile. Two equal search forms remain two occurrences. No local-coreference link means no link asserted, not a claim that they are different people. Unnamed people designated by an office can be represented by `unnamed_role_holder` and a title relation; do not invent a proper name. A parent may be female or unspecified: `child_of` does not imply father, sex or gender.

There is no authored referent object, merged person row or global identifier. A generated local group can be computed from adopted local-coreference relations, retaining its contributing links and qualifications. Its attributes remain attached to their original occurrences and contexts, rather than being copied onto every member.

### Name selection and normalization

1. Select the complete lexical name, not a name-like substring inside a longer compound. A grammatical case suffix may fall outside the selected name span when its boundary is supported; this is source segmentation, not an alias rule. Ambiguous segmentation is qualified and the adopted search form is null where necessary.
2. Evidence uses 1-based physical lines and 0-based/end-exclusive token ranges after removal of a numbered-line label. A **strict substring of exactly one token** may additionally use paired `character_start`/`character_end`, zero-based/end-exclusive Unicode code-point positions in that raw token. Whole-token selections omit both. This is needed for P205120's `lu2-{d}nin-gir2-su-ta`, where the name is the first 18 characters.
3. Apply Unicode NFC and collapse inter-piece whitespace. Remove only supported transcription markup delimiters (`[ ]`, `< >`, and reading flags `#`, `?`, `!`) from the selected lexical form for searching; preserve the marked source through evidence. Deletion/overstrike markup is not silently adopted. A normalization routine must reject unsupported markup rather than guessing. Important readings or restorations still require the shared qualification and reasoning; cleanup itself does not validate them.
4. Preserve sign spelling, hyphens, determinatives and case distinctions. Do not silently convert `lu2` to `lu`, `ba-ba6` to `ba-ba`, `igi-zi` to an English display name, or one phonetic spelling to another. Keep explicit `x` or damaged components in a fragment-search representation; they do not become a complete-name match. The full source is available for a separate literal/fragment search.
5. `ur-{d}lamma-x-gil` is not an exact occurrence of `ur-{d}lamma`. A deity determinative within a person's name does not create an independent deity participant. A deified ruler explicitly named as another endpoint, such as Shulgi in a cupbearer title, may have its own person mention.
6. Name equality and spelling normalization never establish local or cross-source identity. Semantic aliases require separate reviewed evidence and are outside this source-record convention.

The authoritative normalizer/vocabulary version is a contract dependency outside each fact. No independently maintained transliterated display-name field is required.

## 2. Exact relation shapes

All relations have `id`, `type`, `evidence`. Optional `scope_refs` is an array of the precise existing entry/group IDs whose context limits the relation. For an affiliation that belongs to a particular office, it may point to that title relation ID. This is an explicit scope pointer, not a context bundle or inheritance rule.

Three discriminated shapes suffice:

- **Binary**: add `subject_id`, `object_id`.
- **Attribute**: add `subject_id`, `value`.
- **Local coreference**: add `members`, an array of at least two mention IDs.

Do not include unused `object_id`/`value`/`members` placeholders. A material endpoint that is required but unresolved is null with a scoped qualification. Null is never an invented person or an automatically anonymous extra participant.

### Closed identity relation enum and direction

| `type` | Shape | Allowed endpoints / meaning |
|---|---|---|
| `child_of` | Binary | Subject: child mention or explicit child-group entry. Object: parent mention, unnamed-role-holder mention or supported parent-group entry. No automatic gender. |
| `spouse_of` | Binary | Person/role-holder mentions. Symmetric: store the lexicographically smaller stable ID as subject, larger as object; queries inspect both endpoints. |
| `sibling_of` | Binary | Person mentions or explicitly stated sibling groups. Same symmetric storage rule. No inferred shared parent. |
| `title` | Attribute | Subject: person/role-holder mention or an explicitly titled group. Value: adopted title code plus native term. A post-parent title may have null subject and owner/parent alternatives. |
| `affiliation` | Binary | Subject: person/role-holder/group. Object: institution/place/collective/person mention explicitly associated in that capacity. For an office-bound affiliation, scope_refs names the title relation. No conversion of a commodity purpose into personal affiliation. |
| `person_status` | Attribute | Subject: exact person/group. Value: adopted status code plus native term. A status is not automatically a dated event. |
| `on_behalf_of` | Binary | Subject: acting person/group, object: behalf-party person/group; scope_refs must include the relevant entry. An unwritten actor stays null if that absence is material. |
| `nominal_association` | Binary | Subject: person/group; object: the named item, institution or place. This preserves a written boat/house/etc. association without asserting legal ownership. Evidence supplies the actual nominal construction. |
| `seal_owner` | Binary | Subject: legend owner mention; object: seal or composite_seal_legend part ID. The part kind must remain visible to queries; seal means an actual seal component, while composite_seal_legend is a separately described composite. This says whose legend is represented, not who physically impressed or carried it. |
| `local_coreference` | Coreference | Supported local mention group only. Each member ID is distinct; equal names alone are insufficient. |
| `unclassified` | Binary or attribute | Only for a supported local relation not covered above. Add `native_label`, an anchored native phrase. Do not invent a per-source predicate name. |

Account/document relations such as `repeated_representation`, `summarizes`, `discharges` and `balance_of` belong to the separately agreed account portion of this same relations array. They are not extra identity predicates. A documentary party is an entry role, not a duplicate binary relation to the same entry.

### Attribute values and bounded vocabulary

Attribute value shape: `{"code": <controlled code or null>, "native_term": <anchored native term>}`. The code is a coarse query category; the native term preserves the source distinction. Fixed unambiguous mappings are generated/validated from the versioned vocabulary, not independently edited labels.

Initial title codes: `scribe`, `governor`, `administrator`, `overseer`, `farmer`, `gudu_priest`, `cupbearer`, `messenger`, `leatherworker`, `cook`, `chief_surveyor`, `unclassified`. Examples of ordinary mappings are `dub-sar` → scribe, `sagi` → cupbearer, `engar` → farmer. These lexical mappings do not settle title ownership. Less familiar/ambiguous meanings are not forced into these categories.

Initial person-status codes: `deceased`, `absent`, `escaped`, `unclassified`. Retain a distinct native term even where two terms share a coarse code. Do not map `replaced` or an account-purpose clause into `deceased` merely to avoid the catchall.

`unclassified` means a supported concept lies outside the coarse vocabulary; it must retain the native term/label. If the meaning itself is ambiguous, the adopted code is null and typed alternatives/qualification apply. A bounded unclassified list is reviewed for recurring terms before vocabulary changes; individual authors cannot create new enum keys, prose-valued codes or silently broaden an existing code. The source record remains usable before a later vocabulary extension.

### Local coreference use

Store a multi-member link once, rather than all pairs or an additional referent object. Adopted links may support a generated connected local group only while every traversed link is active, supported and compatible. A conflict or candidate link prevents an unconditional combined group. Never traverse candidates, superseded versions, or links from another source as local coreference. When a query uses a derived group, return the original mention and supporting link IDs; the title/role/date claim stays anchored in its original part and entry.

## 3. Exact entry participant links

`entries[*].participants` is an array of:

`{"id": "p1", "ref": "m1", "role": "source", "evidence": ["ev1"]}`

- `ref` resolves to a mention or a semantic group entry. No recursive group flattening into duplicated amounts.
- `role` is one of `source`, `recipient`, `intermediary`, `supervisor`, `custodian`, `witness`, `beneficiary`, `document_party`, `referenced_document_party`, `associated_person`, `unclassified`, or null when its interpretation is withheld.
- `document_party` names a party in the present documentary/archival clause; `referenced_document_party` names a party in a cited or required other document. Neither means physical receiver, seal imprinter or bearer.
- `associated_person` requires a supported non-directional connection to the entry. It is not a generic substitute for a role that has not been assessed.
- `unclassified` additionally requires `native_label`. Ambiguous source-versus-recipient reading uses null plus alternatives, not unclassified.
- Participant ID is the qualification target for `/ref` or `/role`. It is globally unique in the record. No separate participant collection or person-profile copy is created.
- The entry owns its action and action state. A future document requirement is a distinct scoped action from a completed receipt; it is not a blanket future status on every participant. On-behalf-of relationships link the actor and behalf-party through the binary relation, rather than also maintaining an equivalent participant-role assertion.

Roster group `group_members` names explicit occurrence/group IDs or has null adopted membership with scoped alternatives. This semantic membership is separate from arithmetic operands and source-part containment. A plural child relation can point at the group without silently distributing uncertain parentage to every adjacent name.

## 4. Null endpoints and alternative assignments

Use QUALIFICATION_REVIEW_CONVENTIONS_V1.md exactly: qualification targets are `{record_id,field}` with a relative RFC6901 path. Adopted ambiguous endpoints are null. Options are typed assignment bundles; alternatives within one object are mutually exclusive and `exhaustive:false` is the default. If title ownership and its ruler/institution affiliation depend on the same choice, put both endpoint assignments in each option. Do not enumerate them as independent lists that allow inconsistent combinations.

Qualifications point to one reasoning record; reasoning contains evidence_refs, premise_refs and explanatory text. Do not repeat the reasoning target list. Direct ordinary grammar and fixed lexical decoding do not need formulaic explanations. Substantive title attachment, local coreference, restored kinship or inherited group attachment does.

## 5. Fully serialized partial fixture A: P205120

The complete original was read. This fixture covers only physical lines 12–14, demonstrating exact same-name occurrences, participant roles and explicit filiation. Quantities, purpose and dates are deliberately outside its partial fixture coverage, represented by gap1 (physical lines 5–10) and gap2 (physical lines 15–16). No absence inference is permitted for those categories. The source hash binds the full original.

The source token at physical line 12, token 1 is `lu2-{d}nin-gir2-su-ta`. The strict substring [0,18) selects the name while preserving the case suffix in the bound source. The recipient at physical line 13 is a separate occurrence with a written parent. No local-coreference relation is supplied merely because the names match.

```json
{
  "document": {
    "coverage": {
      "gaps": [
        {
          "evidence": [
            "ev8"
          ],
          "id": "gap1",
          "reason": "unprocessed"
        },
        {
          "evidence": [
            "ev9"
          ],
          "id": "gap2",
          "reason": "unprocessed"
        }
      ],
      "status": "partial"
    },
    "dates": [],
    "document_type": "receipt",
    "edition": "PPAC 5, 0400",
    "evidence": [
      {
        "id": "evpart",
        "spans": [
          {
            "line": 3,
            "token_end": 1,
            "token_start": 0
          }
        ]
      },
      {
        "id": "ev1",
        "spans": [
          {
            "character_end": 18,
            "character_start": 0,
            "line": 12,
            "token_end": 2,
            "token_start": 1
          }
        ]
      },
      {
        "id": "ev2",
        "spans": [
          {
            "line": 13,
            "token_end": 1,
            "token_start": 0
          }
        ]
      },
      {
        "id": "ev3",
        "spans": [
          {
            "line": 13,
            "token_end": 3,
            "token_start": 2
          }
        ]
      },
      {
        "id": "ev4",
        "spans": [
          {
            "line": 12,
            "token_end": 2,
            "token_start": 0
          }
        ]
      },
      {
        "id": "ev5",
        "spans": [
          {
            "line": 13,
            "token_end": 3,
            "token_start": 0
          }
        ]
      },
      {
        "id": "ev6",
        "spans": [
          {
            "line": 14,
            "token_end": 2,
            "token_start": 0
          }
        ]
      },
      {
        "id": "ev7",
        "spans": [
          {
            "line": 12,
            "token_end": 2,
            "token_start": 0
          },
          {
            "line": 13,
            "token_end": 3,
            "token_start": 0
          },
          {
            "line": 14,
            "token_end": 2,
            "token_start": 0
          }
        ]
      },
      {
        "id": "ev8",
        "spans": [
          {
            "line": 5,
            "token_end": 3,
            "token_start": 0
          },
          {
            "line": 6,
            "token_end": 7,
            "token_start": 0
          },
          {
            "line": 7,
            "token_end": 5,
            "token_start": 0
          },
          {
            "line": 8,
            "token_end": 2,
            "token_start": 0
          },
          {
            "line": 9,
            "token_end": 3,
            "token_start": 0
          },
          {
            "line": 10,
            "token_end": 5,
            "token_start": 0
          }
        ]
      },
      {
        "id": "ev9",
        "spans": [
          {
            "line": 15,
            "token_end": 2,
            "token_start": 0
          },
          {
            "line": 16,
            "token_end": 4,
            "token_start": 0
          }
        ]
      }
    ],
    "id": "d1",
    "important_uncertainty": [],
    "parts": [
      {
        "id": "part1",
        "kind": "tablet",
        "line_ranges": [
          {
            "end": 17,
            "start": 3
          }
        ],
        "parent_id": null
      }
    ],
    "purposes": [],
    "revision": 1,
    "schema": "ur.source_record.v1",
    "source_id": "P205120",
    "source_version": {
      "bytes": 401,
      "encoding": "utf-8",
      "sha256": "367e2e05c4d7e48a99a5dfaaa8d85a46203171eba174539195e15c9bbd5086b5"
    },
    "supersedes": null
  },
  "entries": [
    {
      "action": {
        "evidence": [
          "ev6"
        ],
        "state": "source_asserts_completed",
        "type": "receipt",
        "id": "action1"
      },
      "evidence": [
        "ev7"
      ],
      "id": "e1",
      "kind": "detail",
      "part_id": "part1",
      "participants": [
        {
          "evidence": [
            "ev4"
          ],
          "id": "p1",
          "ref": "m1",
          "role": "source"
        },
        {
          "evidence": [
            "ev5",
            "ev6"
          ],
          "id": "p2",
          "ref": "m2",
          "role": "recipient"
        }
      ]
    }
  ],
  "mentions": [
    {
      "evidence": [
        "ev1"
      ],
      "id": "m1",
      "kind": "person",
      "literal": "lu2-{d}nin-gir2-su",
      "part_id": "part1",
      "search_form": "lu2-{d}nin-gir2-su"
    },
    {
      "evidence": [
        "ev2"
      ],
      "id": "m2",
      "kind": "person",
      "literal": "lu2-{d}nin-gir2-su",
      "part_id": "part1",
      "search_form": "lu2-{d}nin-gir2-su"
    },
    {
      "evidence": [
        "ev3"
      ],
      "id": "m3",
      "kind": "person",
      "literal": "igi-zi",
      "part_id": "part1",
      "search_form": "igi-zi"
    }
  ],
  "qualifications": [],
  "reasoning": [],
  "relations": [
    {
      "evidence": [
        "ev5"
      ],
      "id": "rel1",
      "object_id": "m3",
      "subject_id": "m2",
      "type": "child_of"
    }
  ]
}
```

Expected identity queries (fixture scope only):

| Query | Adopted result |
|---|---|
| Exact name `lu2-{d}nin-gir2-su` | m1 and m2, two written occurrences; no person-count assertion. |
| Name + role=source | m1 through p1/e1. |
| Name + role=recipient | m2 through p2/e1. |
| Name + child_of parent search_form `igi-zi` | m2 through rel1; m1 does not inherit that parent. |
| Is the source the same person as the recipient? | No adopted link. The fixture does not answer yes or assert different people. |
| Commodity totals, closing year, or absent title | Not answered by this partial fixture; no fabricated zero, date or absence. |

## 6. Fully serialized partial fixture B: P133163

The complete original was read. This fixture deliberately covers only actual-seal physical lines 30–33, with the seal-part marker at 29. It is a design test of source-local kinship, own versus parent title attachment, and correlated alternatives. Unprocessed tablet material at physical lines 5, 6, 8–9, 11–12, 14–16 and envelope material at 19–22, 24–28 are explicitly bound by gap1/gap2. Body/envelope correspondence is not newly decided here. Final sagi/Shulgi attachment remains open in this fixture, not newly corrected or accepted in any production packet.

```json
{
  "document": {
    "source_id": "P133163",
    "source_version": {
      "sha256": "c700fceb13e01606961913c02e4cb9ef45c2332717fed044bd830009fc6b4be2",
      "bytes": 671,
      "encoding": "utf-8"
    },
    "edition": "TCTI 2, 03968",
    "document_type": "receipt",
    "parts": [
      {
        "id": "tablet1",
        "kind": "tablet",
        "parent_id": null,
        "line_ranges": [
          {
            "start": 3,
            "end": 17
          }
        ]
      },
      {
        "id": "envelope1",
        "kind": "envelope",
        "parent_id": null,
        "line_ranges": [
          {
            "start": 17,
            "end": 29
          }
        ]
      },
      {
        "id": "seal1",
        "kind": "seal",
        "parent_id": null,
        "line_ranges": [
          {
            "start": 29,
            "end": 34
          }
        ]
      }
    ],
    "evidence": [
      {
        "id": "evpart",
        "spans": [
          {
            "line": 29,
            "token_start": 0,
            "token_end": 2
          }
        ]
      },
      {
        "id": "ev1",
        "spans": [
          {
            "line": 30,
            "token_start": 0,
            "token_end": 1
          }
        ]
      },
      {
        "id": "ev2",
        "spans": [
          {
            "line": 31,
            "token_start": 0,
            "token_end": 1
          }
        ]
      },
      {
        "id": "ev3",
        "spans": [
          {
            "line": 32,
            "token_start": 1,
            "token_end": 2
          }
        ]
      },
      {
        "id": "ev4",
        "spans": [
          {
            "line": 32,
            "token_start": 0,
            "token_end": 2
          }
        ]
      },
      {
        "id": "ev5",
        "spans": [
          {
            "line": 33,
            "token_start": 1,
            "token_end": 2
          }
        ]
      },
      {
        "id": "ev6",
        "spans": [
          {
            "line": 33,
            "token_start": 0,
            "token_end": 2
          }
        ]
      },
      {
        "id": "ev7",
        "spans": [
          {
            "line": 30,
            "token_start": 0,
            "token_end": 1
          },
          {
            "line": 31,
            "token_start": 0,
            "token_end": 1
          },
          {
            "line": 32,
            "token_start": 0,
            "token_end": 2
          },
          {
            "line": 33,
            "token_start": 0,
            "token_end": 2
          }
        ]
      },
      {
        "id": "ev8",
        "spans": [
          {
            "line": 5,
            "token_start": 0,
            "token_end": 3
          },
          {
            "line": 6,
            "token_start": 0,
            "token_end": 2
          },
          {
            "line": 8,
            "token_start": 0,
            "token_end": 3
          },
          {
            "line": 9,
            "token_start": 0,
            "token_end": 4
          },
          {
            "line": 11,
            "token_start": 0,
            "token_end": 2
          },
          {
            "line": 12,
            "token_start": 0,
            "token_end": 4
          },
          {
            "line": 14,
            "token_start": 0,
            "token_end": 3
          },
          {
            "line": 15,
            "token_start": 0,
            "token_end": 1
          },
          {
            "line": 16,
            "token_start": 0,
            "token_end": 1
          }
        ]
      },
      {
        "id": "ev9",
        "spans": [
          {
            "line": 19,
            "token_start": 0,
            "token_end": 3
          },
          {
            "line": 20,
            "token_start": 0,
            "token_end": 2
          },
          {
            "line": 21,
            "token_start": 0,
            "token_end": 2
          },
          {
            "line": 22,
            "token_start": 0,
            "token_end": 2
          },
          {
            "line": 24,
            "token_start": 0,
            "token_end": 2
          },
          {
            "line": 25,
            "token_start": 0,
            "token_end": 1
          },
          {
            "line": 26,
            "token_start": 0,
            "token_end": 2
          },
          {
            "line": 27,
            "token_start": 0,
            "token_end": 2
          },
          {
            "line": 28,
            "token_start": 0,
            "token_end": 6
          }
        ]
      }
    ],
    "coverage": {
      "status": "partial",
      "gaps": [
        {
          "id": "gap1",
          "evidence": [
            "ev8"
          ],
          "reason": "unprocessed"
        },
        {
          "id": "gap2",
          "evidence": [
            "ev9"
          ],
          "reason": "unprocessed"
        }
      ]
    },
    "important_uncertainty": [
      "q1"
    ],
    "schema": "ur.source_record.v1",
    "id": "d1",
    "revision": 1,
    "supersedes": null,
    "dates": [],
    "purposes": []
  },
  "mentions": [
    {
      "id": "m1",
      "kind": "person",
      "literal": "du11-ga-zi-da",
      "search_form": "du11-ga-zi-da",
      "part_id": "seal1",
      "evidence": [
        "ev1"
      ]
    },
    {
      "id": "m2",
      "kind": "person",
      "literal": "nig2-u2-rum",
      "search_form": "nig2-u2-rum",
      "part_id": "seal1",
      "evidence": [
        "ev3"
      ]
    },
    {
      "id": "m3",
      "kind": "person",
      "literal": "{d}szul-gi",
      "search_form": "{d}szul-gi",
      "part_id": "seal1",
      "evidence": [
        "ev5"
      ]
    }
  ],
  "relations": [
    {
      "id": "rel1",
      "type": "seal_owner",
      "subject_id": "m1",
      "object_id": "seal1",
      "evidence": [
        "evpart",
        "ev1"
      ]
    },
    {
      "id": "rel2",
      "type": "title",
      "subject_id": "m1",
      "value": {
        "code": "scribe",
        "native_term": "dub-sar"
      },
      "evidence": [
        "ev1",
        "ev2"
      ]
    },
    {
      "id": "rel3",
      "type": "child_of",
      "subject_id": "m1",
      "object_id": "m2",
      "evidence": [
        "ev1",
        "ev4"
      ]
    },
    {
      "id": "rel4",
      "type": "title",
      "subject_id": null,
      "value": {
        "code": "cupbearer",
        "native_term": "sagi"
      },
      "evidence": [
        "ev6"
      ]
    },
    {
      "id": "rel5",
      "type": "affiliation",
      "subject_id": null,
      "object_id": "m3",
      "scope_refs": [
        "rel4"
      ],
      "evidence": [
        "ev6"
      ]
    }
  ],
  "entries": [],
  "qualifications": [
    {
      "id": "q1",
      "targets": [
        {
          "record_id": "rel4",
          "field": "/subject_id"
        },
        {
          "record_id": "rel5",
          "field": "/subject_id"
        }
      ],
      "support": "ambiguous",
      "impact": [
        "meaning"
      ],
      "null_reason": "unresolved",
      "reasoning_ref": "reason1",
      "alternatives": {
        "exhaustive": false,
        "options": [
          {
            "id": "owner_option",
            "assignments": [
              {
                "target": {
                  "record_id": "rel4",
                  "field": "/subject_id"
                },
                "value": "m1"
              },
              {
                "target": {
                  "record_id": "rel5",
                  "field": "/subject_id"
                },
                "value": "m1"
              }
            ]
          },
          {
            "id": "father_option",
            "assignments": [
              {
                "target": {
                  "record_id": "rel4",
                  "field": "/subject_id"
                },
                "value": "m2"
              },
              {
                "target": {
                  "record_id": "rel5",
                  "field": "/subject_id"
                },
                "value": "m2"
              }
            ]
          }
        ]
      }
    },
    {
      "id": "q2",
      "targets": [
        {
          "record_id": "rel5",
          "field": "/type"
        }
      ],
      "support": "well_supported",
      "impact": [
        "evidence_dependence"
      ],
      "reasoning_ref": "reason1"
    }
  ],
  "reasoning": [
    {
      "id": "reason1",
      "evidence_refs": [
        "ev7"
      ],
      "premise_refs": [
        "rel2",
        "rel3"
      ],
      "text": "The pre-filiation dub-sar belongs to the owner named at physical line 30. The following dumu clause explicitly names Nig-urum as parent. The final sagi Shulgi phrase identifies a cupbearer relationship to Shulgi, but its position after the parent leaves owner-versus-parent attachment open in this design fixture. The title subject and its linked Shulgi affiliation must change together. Neither option is adopted; these two options are not claimed exhaustive."
    }
  ]
}
```

Expected identity queries (fixture scope only):

| Query | Adopted result |
|---|---|
| Actual seal legend owner | m1 through rel1/seal1, with actual-seal part type. |
| Duggazida child_of Nig-urum | rel3, m1 → m2. |
| Own scribe title | m1 through rel2. The father does not inherit this title. |
| Adopted cupbearer person | No person endpoint adopted: rel4.subject_id is null. The written cupbearer term remains searchable. |
| Cupbearer candidates | owner_option m1, father_option m2, both explicitly non-active and non-exhaustive. |
| Adopted personal affiliation to Shulgi | No person endpoint adopted. rel5 remains scoped to rel4. |
| Candidate title owner and affiliated person | Each option assigns the same endpoint to rel4 and rel5. Mixing owner_option title with father_option affiliation is invalid. |
| Was the bearer/receiver the seal owner? | Not answered by this seal-only fixture. No fabricated carrier or transfer event. |

The fixture shows why sparse qualifications must be displayed beside their affected fields: a query returning the word cupbearer without its null subject and alternatives would be scientifically misleading.

## 7. Canonical query and efficiency priorities

1. **Make the local comparison join direct.** Given a mention, return its entry roles, kinship endpoints, own titles/statuses, source part, scoped date/place/purpose links, quantities and effective qualifications in one generated view. Keep adopted and candidate tiers separate. This replaces repeated full-source assembly; it does not infer global identity.
2. **Produce a two-sided feature table from those fields.** For each compared source, show adopted, candidate, not assessed and material not-written states independently. This would have exposed the unsupported shared E-guzala institution and shared Ka-amu purpose in earlier comparisons before copied prose propagated them. Empty joins alone must not mean absent.
3. **Generate anchors, inverse links and correction impact.** Let the author select spans and link existing IDs; derive reverse reasoning/qualification indexes and the affected dependency list. Repeated manual paths, hashes and copied role/amount prose were avoidable time costs. Preserve the immutable corrected-record boundary.
4. **Reuse exact native fields instead of retyping glosses.** The corrected 128-to-88 gur comparator spread through five fields and three downstream copies. A later identity comparison should reference the source measurement and qualification, not maintain another numeral sentence. Likewise use the written year formula, not a shorthand that could confuse a physical line number with a chronological year.

Remove: separate local-person objects; all-pairs coreference; second participant/profile lists; a new entity for every title word; duplicate on-behalf-of or document-party assertions in both entry roles and relations; per-fact source hashes; duplicate typed/prose amounts; free-form custom predicates; repeated explanation text; hand-maintained candidate/adopted display copies. Keep canonical source facts and derive views.

No measured gain is claimed. Consistent complete source records should eliminate most routine local re-extraction; ambiguous readings, important new cross-source comparisons and suspected errors will still justify original consultation. Global same-person decisions remain a separate later research step.

## 8. Required small acceptance checks before implementation

- Both fixtures parse as six-section JSON; all stable IDs, evidence references and qualification paths resolve.
- Literal name selection reproduces the exact bound source substring; suffix handling cannot turn a compound personal name into a shorter name occurrence.
- Binary endpoint kinds/directions, participant ref types and attribute value vocabularies are checked.
- Same spelling does not introduce local_coreference; local grouping never transfers a father's title or a different entry's action/date.
- Ambiguous main endpoints remain null; candidate bundles remain inactive and internally correlated.
- Group membership, account operands and source layout remain independently addressable.
- Search uses only the effective externally admitted record scope. Partial fixtures and unreviewed proposals cannot become exhaustive corpus absence evidence.

This is a design deliverable. The companion fixtures follow the shared core wrapper. Final integrated-dictionary and scientific pilot review are still required before implementation; nothing here authorizes migration or live research-state changes.
