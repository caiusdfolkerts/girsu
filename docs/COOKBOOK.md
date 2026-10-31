# Field and occurrence queries

`query_examples.py` provides six streaming retrieval patterns over the same single default used by `girsu.py`. They retrieve existing fields and kinds; they do not introduce a research classification, semantic taxonomy, or identity layer. The examples use Python's standard library.

## Starting with a source

Run these commands from the release root to inspect a single source:

```sh
python query_examples.py genre null --root . --source P100144
python query_examples.py date mu --root . --source P100144
python query_examples.py institution szabra --root . --source P100144
python query_examples.py commodity barley --root . --source P100144
python query_examples.py relation metrological_standard --root . --source P100144
python query_examples.py person 'ur-{d}nin-a-zu' --root . --source P100144
```

Repeat `--source` to inspect several exact IDs, or omit it for a streaming corpus scan. `--limit 10` returns a prefix, not a corpus count. Queries use current sources by default. Adding `--archival` explicitly includes selected archival sources and retains their `current:false` status.

## What a match represents

A genre query such as `genre receipt` matches the exact default controlled genre and returns one row per document. `genre null` matches an actual null rather than the string “null”, returning documents whose default genre is null.

The `date mu` recipe matches a literal substring in a calendar year formula or month name. Each row represents one calendar expression and includes its entry applicability. This recipe does not search intervals, durations, or relative dates, and it supplies no absolute chronology.

The institution and person recipes match literal substrings in a mention's literal or search form. Each row represents a mention occurrence, not a uniquely identified historical institution or person. Matching both forms of the same mention still produces one row. A literal can match even when its interpreted search form is null; the output retains that null and its explanation. Personal occurrences must not be read as a count of people.

The `commodity barley` recipe matches a literal substring of an item type ID or an exact native-term ID. Each row represents one item, accompanied by directly linked measurements from the same entry.

The `relation metrological_standard` recipe matches the exact `native_label` on an unclassified relation. Each row represents one source-local relation with endpoint pointers. The query uses the preserved label, including explanatory English labels where present, without reclassifying the relation.

Substring matching is case-insensitive. It does not normalize spelling or transliteration, equate synonyms, or merge identities.

## Reading the evidence in a result

Each result carries the source ID, original source-record `version_hash`, current status, layer, exact pointer or local ID, and one default `value`. It also includes separate `has_branches` and `has_ambiguity` flags, applicable qualifications, labelled branch and qualification annotations, evidence pointers, and context. The original source-record hash identifies the preserved source record; it does not hash the default result row.

Direct source anchors give the exact original SHA and coordinates. Some fields, including genre, instead have indirect evidence through qualifications or reasons. Follow those pointers rather than assuming that an absent direct evidence list means there is no support.

Context matters because linked measurements, dates, and endpoints retain their own scoped qualification and branch maps. A quantity's qualification is not attached indiscriminately to the item noun, nor is one endpoint's uncertainty attributed to every participant in a relation. Inspect the context as well as the row target.

`has_branches` identifies choices; `has_ambiguity` also covers scoped qualification context. Neither flag certifies certainty. The annotation field `is_identified_branch` distinguishes an actual choice set from the 10,601 qualification-only annotations across the stored population.

Calendar applicability retains roles such as document date, reference date, and service period. A rate's numerator, denominator, population, and time basis remain distinct from an amount. Native-vector units are neither silently converted nor summed across unlike components. A null is not zero.

## Exporting JSON Lines or CSV

JSON Lines is the default output format. It preserves nested provenance and exact rational strings. For example:

```sh
python query_examples.py commodity barley --root . --source P100144 > barley.jsonl
python query_examples.py commodity barley --root . --source P100144 --format csv > barley.csv
```

Every CSV cell contains a JSON value, including strings and nulls. Decode each cell with `json.loads`, and import spreadsheet columns as text. This convention preserves `"1/2"` as an exact string rather than a spreadsheet date, distinguishes null from empty text, and prevents strings from beginning executable formulas. Nested provenance stays in JSON instead of expanding into duplicated rows.

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

For general scalar search rather than these typed recipes, use `Graph.search_page`. An empty page need not mean that the search is exhausted. Pass its exact `next_cursor`, check `exhausted`, and do not use a limited page as a corpus denominator. The [README](../README.md) and [semantics](SEMANTICS.md) explain the broader interface.
