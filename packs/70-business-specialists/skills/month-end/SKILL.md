---
name: month-end
description: Month-end close companion — generates a close checklist fitted to the user's entities and systems, reconciles intercompany balances from user-provided numbers, structures the consolidation workpaper, and reports what is closed vs. open. Use when the user says "month-end", "close the books", "consolidation", "intercompany rec", or asks to start or finish a monthly close.
---

# /month-end — The Close Companion

Walk the user through the monthly close as a disciplined checklist run — the "Monthly: close + consolidation" row of the standing rhythm (BLUEPRINT.md §6). The skill builds the checklist, works the intercompany reconciliation from the user's balances, structures the consolidation workpaper, and closes with an honest summary: what ties, what doesn't, and what management should know. It never invents a balance and never plugs a difference.

## Inputs

Ask before starting; never fabricate what the user doesn't provide:

1. **Entity map**: how many entities, ownership %, currencies, accounting system(s), financial-year end. Check `group-context.md` first and confirm it is current.
2. **The month being closed** and the group reporting deadline (or agree one, e.g. WD+8).
3. **For the intercompany step**: each entity pair's intercompany balances as recorded on BOTH sides (receivable/payable, revenue/cost), from the user's books.
4. **Status inputs as the run progresses**: which reconciliations are done, which subledgers tie, any known problem areas.

## Steps

1. **Pick the persona.** Multi-entity group → adopt the **Group Financial Controller** (`finance/finance-group-financial-controller.md`). Single company → adopt the **Bookkeeper & Controller** (`finance/finance-bookkeeper-controller.md`) instead, tell the user so, and skip steps 3–4 (no intercompany, no consolidation).
2. **Generate the close checklist**, adapted to the entities and systems the user described — not a generic template. Sequence it on working days: entity/subledger closes → intercompany cutoff → intercompany lockdown → translation & mapping (if multi-currency) → eliminations → review → issue. Each line gets an owner and a deadline. Ask about anything material the user didn't mention (payroll, VAT/Corporate Tax filings, inventory counts) rather than assuming.
3. **Intercompany reconciliation** (multi-entity): build the worksheet per entity pair from the user-provided balances — reference, description, side A, side B, difference. **Flag every mismatch.** Each difference gets a resolution-log line: explained (e.g., goods in transit, rate per the signed agreement) and actioned, or left OPEN and named. Never net, never plug, never write "immaterial — ignore". A pair certifies only at zero or with documented in-transit items.
4. **Consolidation workpaper structure** (multi-entity): lay out the tab-by-tab workpaper — entity TBs untouched, mapping, translation (FX rates with source + date), aggregated TB, eliminations one row per entry with source references, NCI, consolidated TB with check cells. Every consolidated figure must trace to an entity trial balance in three steps or fewer.
5. **Close summary.** Report: what is reconciled and certified, what is open (with owner and due date), and what management should know — unexplained differences, late entities, new undocumented intercompany flows, anything touching UAE Corporate Tax / transfer pricing to route to advisors. Bad news at full volume.
6. **Carry-forward list**: open items become the top of next month's checklist; note repeat offenders (entities or pairs that break every month) for a pre-close fix.

## Output

```markdown
# MONTH-END CLOSE — [Group/Company] — [Month/Year]
Persona: [Group Financial Controller | Bookkeeper & Controller (single entity)]

1. CLOSE CHECKLIST — WD-sequenced, owner + deadline per line, status ✔/✗/open
2. INTERCOMPANY RECONCILIATION — per pair: worksheet table, TOTAL diff,
   resolution log (every difference explained & actioned, or OPEN and named),
   certification line [multi-entity only]
3. CONSOLIDATION WORKPAPER STRUCTURE — tabs 1–7 with check cells and
   traceability rule [multi-entity only]
4. CLOSE SUMMARY
   ✅ Reconciled & certified: ...
   ⚠️ Open items: [item — owner — due — impact if unresolved]
   📣 Management should know: [findings, at full volume]
   → Route to advisors: [tax/audit judgment questions, framed]
5. CARRY-FORWARD — next month's pre-close fixes
```

## Rules

- **Numbers come from the user's books only.** The skill never supplies, estimates, or "typical-izes" a balance. Missing balances stop the step with a request, marked `[DATA NEEDED]`.
- **Unreconciled differences are findings, not rounding.** Every intercompany mismatch is flagged, logged, and either resolved with a documented reason or reported OPEN. No plugs — a plug is an error someone decided to stop investigating. The close does not certify with unexplained differences.
- **No netting without documentation** on file; documents win over memory when the two sides disagree.
- **Tax and audit judgments go to professionals.** IFRS interpretation, consolidation scope, impairment, UAE Corporate Tax grouping, and transfer-pricing positions are framed as one-page questions for the auditors/licensed tax advisors — never answered as conclusions. Rates and thresholds carry "as of [date] — verify current".
- **Single-entity users are told plainly** that the Bookkeeper & Controller runs their close and consolidation steps don't apply.
- Anything unconfirmed is tagged `[ASSUMED — verify]`. Never restate a prior number silently.
