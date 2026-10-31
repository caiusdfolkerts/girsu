# Small field and occurrence queries

`query_examples.py` demonstrates six streaming retrieval patterns over the **same single default** as `girsu.py`. These are examples of existing fields/kinds, not a new research classification system, semantic taxonomy or identity layer. Use Python's standard library.

From the release root, start with exact source-filtered examples:

```sh
python query_examples.py genre null --root . --source P100144
python query_examples.py date mu --root . --source P100144
python query_examples.py institution szabra --root . --source P100144
python query_examples.py commodity barley --root . --source P100144
python query_examples.py relation metrological_standard --root . --source P100144
python query_examples.py person 'ur-{d}nin-a-zu' --root . --source P100144
```

Repeat `--source` to inspect several exact IDs. Omit it for a streaming corpus scan. `--limit 10` emits only a prefix; it is **not a corpus count**. Current sources are the default; `--archival` explicitly includes archival selected sources and retains `current:false`.

## Matching and counting units

| Mode | Matching rule | One row means |
|---|---|---|
| `genre receipt` | Exact default controlled genre | One document |
| `genre null` | Actual null, not the string “null” | One document with null default genre |
| `date mu` | Literal substring of calendar year formula/month name | One calendar expression, with entry applicability |
| `institution szabra` | Literal substring of institution mention literal/search form | One mention occurrence |
| `commodity barley` | Literal substring of item type ID or exact native-term ID | One item, with directly linked same-entry measurements |
| `relation metrological_standard` | Exact `native_label` on an unclassified relation | One source-local relation with endpoint pointers |
| `person ...` | Literal substring of person mention literal/search form | One mention occurrence |

Substring matching is case-insensitive, with no spelling/transliteration normalization, synonym equation or identity merging. Matching both literal and search form on one mention gives one row. A literal can match while its interpreted search form is null; that null and its explanation remain in the output. An institution occurrence is not a uniquely identified historical institution, and a personal occurrence is not a people count.

The relation recipe searches the exact preserved label, including explanatory English labels where present. It does not reclassify them. The date recipe searches calendar strings only, not intervals/durations/relative dates, and supplies no absolute chronology.

## Provenance travels with the row

Each result includes source ID, original source-record `version_hash`, current status, layer, exact pointer/local ID, one default `value`, separate `has_branches`/`has_ambiguity` flags, applicable qualifications, labelled branch/qualification annotations, evidence pointers and context.

Direct source anchors include exact original SHA and coordinates. Genre and other fields can have indirect evidence through qualifications/reasons rather than their own direct evidence list. Follow those pointers. The original source-record hash does not hash an edited/default result row.

Linked measurements, dates and endpoints keep their own scoped qualification/branch maps under context. A qualification on a quantity is not falsely attached to the item noun, nor one endpoint's uncertainty to every relation participant. Check context as well as the row target. `has_branches` refers only to identified choices; `has_ambiguity` also covers scoped qualification context. Neither is a certainty certificate. Annotation `is_identified_branch` distinguishes a real choice set from the 10,601 qualification-only annotations across the stored population.

Calendar applicability preserves roles such as document date, reference date or service period. A rate's numerator/denominator/population/time basis remains distinct from an amount. Native-vector units are not silently converted or added across unlike components. Null is not zero.

## JSONL and reversible CSV

JSON Lines is the default and preserves nested provenance and rational strings:

```sh
python query_examples.py commodity barley --root . --source P100144 > barley.jsonl
python query_examples.py commodity barley --root . --source P100144 --format csv > barley.csv
```

Every CSV cell is a **JSON value**, including strings and nulls. Decode it with `json.loads`; import spreadsheet columns as text. This preserves `"1/2"` as an exact string rather than a spreadsheet date, distinguishes null from empty text and prevents strings from beginning executable formulas. Nested provenance stays JSON, not duplicated row expansion.

```python
import csv, json
from fractions import Fraction

with open('barley.csv', newline='', encoding='utf-8') as stream:
    rows = ({key: json.loads(value) for key, value in cells.items()}
            for cells in csv.DictReader(stream))
    for row in rows:
        pass  # row['value'], row['qualifications'], row['evidence'] remain structured

exact_half = Fraction('1/2')  # exact arithmetic; no missing unit conversion is supplied
```

For general scalar search rather than these typed recipes, use `Graph.search_page`: an empty page need not be exhausted. Pass its exact `next_cursor`, check `exhausted` and never treat a limited page as a corpus denominator. See [README](../README.md) and [semantics](SEMANTICS.md).
