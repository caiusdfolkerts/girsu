# Job: work accurately and quickly, improve with each batch

Your job is to deliver complete, faithful records quickly and become more effective with successive batches. Use the assigned tools and write or adapt small reusable code when it saves work. Keep useful construction, anchoring, search and checking methods; improve or replace steps that cause repeated errors or wasted effort.

Reuse the mechanics, not the scientific conclusions: decide each source's subjects, roles, quantities, scope and uncertainty from that source. Aim to improve both first-pass accuracy and throughput, without skipping content, manufacturing certainty or adding unnecessary analysis.

Work on method-similar ready batches when supplied (ordinarily 50–200, not a reason to wait for that many). Cache stable references and the definitions of unfamiliar codes you have checked; reuse concise explanations only when the same evidence-bound inference genuinely applies.

Submit finished permitted work promptly and continue the next ready source instead of waiting for the whole batch, review or publication. When missing inputs or a tool failure prevents completion, preserve a recoverable draft and precise blocker, then continue unrelated work.

A genuinely unresolved historical interpretation is not automatically an operational blocker: represent it honestly under the quality standard when the supplied source can still be fully assessed.

## Use the assigned work mode

Use the runtime, inputs and submission destination supplied with your assignment. For a portable/local kit, verify the supplied files, work in that kit and return outputs through its specified handoff; cloud filesystem paths are not local files.

Use live queue commands only when the assignment supplies a live queue and authorizes that mode. Keep source tokens separate. Submit finished permitted work promptly and continue ready work rather than waiting for import or publication acknowledgement.

## Work one source through, then reuse the method

1. **Load exact assignment and originals.** Save the untruncated assignment response. Check source ID, original bytes/hash, current predecessor, token, supplied context and current lesson dispositions. Use the exact assigned files and destination. Do not infer missing inputs from historical scripts.
2. **Read the full original once for meaning.** Identify parts, clauses, headings, closing scope, actions, quantities and documentary structure. Establish shared context, including unit standards, and its boundaries before constructing the affected rows; pass that assessed context into those rows instead of dropping it when the words are not repeated. Keep a compact private working map if useful, not a checklist deliverable.
3. **Build the source-local record.** Choose the source-supported claims and their scope before instantiating them with helpers. Build objects and their relationships together; a line-by-line loop must not leave an account or cross-clause connection only in prose. For an interpretation or uncertainty assessment, collect the affected adopted fields first, then use a shared multi-target qualification where the same assessment applies. Select its support from the evidence; a convenience wrapper’s default is not that decision. When constructing an independent statement outside your usual quantity-panel helper, include its supported scope too. Keep these choices in construction rather than relying on a later sweep to discover what the helper omitted. If a helper assumes an item, role, unit or certainty that the source does not support, change the construction instead of filling the slot with a convenient placeholder. Preserve written quantities and totals before any calculation, and avoid speculative analysis not needed for the assignment.
4. **Make one brief material-query check.** Inspect raw structure plus generated view: who did what/to/from/for whom, quantities/operators/units, date/purpose/standard attachment, relevant uncertainty and what must not be added. Compare with every original part and closing clause. For important positive claims, find the actual structural path without relying on prose; does it agree with the adopted reasoning? Use `python runtime/uncertainty_scope_advisory.py RECORD.json --text` as a compact view of selected declared uncertain attachments: resolve displayed IDs in the raw record and compare each actual claim with its reason and source. Keep secure coarse claims, hold only genuinely disputed extensions or fine assignments, and do not treat the output as an error list that must be emptied. It cannot find undeclared uncertainty or establish complete coverage. Fix omissions; do not repeat a full independent review of your own work.
5. **Validate fail-closed and save a recoverable checkpoint.** Preserve canonical record bytes/hash, exact original binding, predecessor if any, actual returned diagnostics and their hash. The canonical version is `records.record_hash(record)`/canonical bytes, not the hash of an arbitrarily pretty-printed file.
6. **Submit only within the authorized lane.** In production, use the exact token/source/hash/predecessor with the ordinary CLI and preserve its response. Hand frozen artifacts to the assigned independent reviewer through the specified destination. Finished permitted records need not wait for an entire batch or delivery before continuing.

### Validation means the returned report, not lack of an exception

`records.validate_record(record, source_bytes=original_bytes, predecessor_bytes=...)` returns a **dictionary**. A pass requires a dictionary with `valid is True` and `errors` an empty **list**. False/missing/malformed values, nonempty errors and exceptions all fail. Do not suppress diagnostics or replace them with a generic PASS. `RecordBuilder.build()` raises on invalidity, but this does not change `validate_record`'s return contract.

```python
from validation_receipt import validate_with_receipt
from records import canonical_bytes, record_hash
receipt = validate_with_receipt(record, source_bytes=original_bytes)
# For a correction also pass exact predecessor_bytes when required.
# Save canonical_bytes(record), receipt, original SHA/bytes, input version,
# and canonical hash of the result report before acting on the outcome.
passed = receipt['mechanical_validation'] == 'pass'
if not passed:
    # Preserve receipt['result'] and receipt['exception']; repair before submit.
    raise ValueError('Mechanical validation failed; inspect saved diagnostics')
```

The wrapper retains the full report and canonical result hash and makes no writes/submission. Mechanical validity is not scientific acceptance or evidence that the whole original is covered. Revalidate exact inputs when an earlier receipt does not preserve the actual report or does not enforce this return contract.

## Practical construction tools

Use `records.py` helpers from the runtime supplied with the assignment. `RecordBuilder(source_id, original=exact_bytes, edition=...)` supplies bookkeeping, not interpretation.

`b.original_view()` gives the full source, physical line numbers, token arrays and version. `b.anchor(line,start,end)`/`b.anchors(spans)` create exact references; `b.link`, `b.term`, `b.expression`, `b.quantity`, `b.quantity_panel`, `b.action` help construct ordinary schema objects.

Specify clause boundaries, participants, quantity function/dimension, scope and adoption yourself. See the full runnable supplied construction in `appendix/canonical_teaching_records/build.py`; it is an example to inspect, not a restart command or source-independent extractor.

Useful distinctions from `appendix/reference/AUTHOR_HELPERS.md`:
- A rate's `population_ref` targets its population subject: an item or a semantic group-entry, not its count measurement. If `measure1.subject_ref` is `item1`, use `population_ref: "item1"`; calculation recipe operands still reference `measure1`. Do not invent a count merely to supply this population endpoint.
- `native_unit_handle([unit_anchor])` returns a term's `unit` plus `unit_evidence` list; a quantity value's native `unit_evidence` is instead a map from native unit ID to evidence list.
- `native_standard` is an object `{native_term_id,evidence}` on an adopted quantity with `standard_ref:null`. A supported interpreted `standard_ref:"gur_lugal"` is another valid binding, not itself a numerical conversion.
- For `adopted:null`, a scoped metrological_standard relation preserves a known standard. Pass `standard_scope=entry_id` if ownership is not uniquely established; still qualify the withheld amount.
- `b.quantity_preflight()` identifies embedded operators and explicit-standard reminders. Check the ordered operands; a matching net coefficient is insufficient. Preflight does not edit, establish complete coverage or grant acceptance.
- Optional `supporting_sources` carries exact other-source bindings; cite its anchors through `reasoning.supporting_evidence_refs`, never disguise them as local evidence.
- Optional documentary_correspondence is a tightly bounded tablet/envelope relation-local extension, not a global synonym or permission to aggregate. Do not use it in production without the coordinated deployment/review described in the addendum.

## Recoverable work and exact handoff

Keep recoverable source-local drafts and exact payloads; checkpoint before context expiry. Handoff source IDs, original/record/predecessor hashes, saved files, assignment tokens, complete/partial/blocker status, validation diagnostics and exact next action. Never delete the sole unresolved evidence. Do not silently edit submitted/accepted versions; submit a successor through ordinary review with exact predecessor/diff.

Authorized live CLI pattern (substitute explicit assigned values, never array positions):
```
python cli.py --queue QUEUE claim-source --worker WORKER --work-kind LANE
python cli.py --queue QUEUE submit --source P_ID --version CANONICAL_HASH --token TOKEN --record FILE --work-kind LANE
# For a correction add --predecessor EXACT_PRIOR_HASH.
```
Run from the assigned pipeline directory. Do not initialize/reset the queue, lift a hold, change permissions or replay an old batch script.

Claim responses can contain `other_assignments`, each with its own token/preparation; never mix them. Renew the appropriate live lease if needed.

If a source cannot proceed, preserve draft and use the existing `block-source` with exact source/token/current version (or `none` only for no version), reason, draft-ref and next-action. Continue unrelated available work; do not leave an evidence-blocked source occupying an active claim. Unblock only after exact resolution through the authorized event-bound workflow.

If a consequential submission/write has an uncertain outcome after an exec/transport error, reconcile its exact source/hash/token/payload in persisted state before retry. If committed, do not repeat; if confirmed failed or absent and ownership matches, retry the identical saved payload through the normal route.

A known pre-execution failure or read-only tool error does not require database reconciliation. An unknown write outcome is not a confirmed failure. If access/action is blocked, report **exact action, reason, current persisted status and required next action/authorization**; do not claim success or cleared work.

Optional: `appendix/reference/READING_CONTEXT_HELPER.md` shows whether a selected span lies inside brackets opened earlier in its source line. Use it when useful, not as an automatic uncertainty or return rule.
