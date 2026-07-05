---
name: weekly
description: The Monday morning brief — runs pipeline, operations, and cash reviews from whatever data the user provides, then compresses them into one weekly one-pager of 3 numbers, 3 risks, 3 decisions. Use when the user says "weekly review", "Monday brief", pastes a pipeline export, ops notes, or a bank position, or asks how the week looks.
---

# /weekly — The Monday Morning Brief

Implement the weekly row of the standing rhythm (BLUEPRINT.md §6): pipeline review, ops review, and cash position, run as three specialist passes and delivered as one page the chairman can read before the first coffee is finished. Each section runs only on data the user actually provided — a section with no data says `[DATA NEEDED]`, never a guess dressed as a fact.

## Inputs

Ask for the three inputs; take whichever the user has and note the rest as missing:

1. **Pipeline**: CRM export, deal list, or the user's own pipeline notes (deals, stages, amounts, close dates, quota if known).
2. **Operations**: status notes — projects/commitments in flight, delivery dates, capacity, this week's firefights.
3. **Cash**: bank balances by entity/account (with as-of date), upcoming payment obligations, facility/covenant details if any.

Also read `group-context.md` and relevant `business-context-<company>.md` files for entity structure, priorities, and benchmarks. If the user provides only one input, confirm you will run only that section and name what is skipped.

## Steps

1. **Inventory the data.** State plainly which of the three inputs arrived, their as-of dates, and which sections will show `[DATA NEEDED]`.
2. **Pipeline pass — adopt the Pipeline Analyst** (`sales/sales-pipeline-analyst.md`). From the provided data only: pipeline health and coverage vs. remaining quota (quality-adjusted where the data allows), slipping and stalled deals needing intervention this week, and forecast honesty — the realistic weighted number vs. the optimistic one, with data-quality gaps flagged explicitly. If quota or benchmarks are unknown, say so; do not assume a coverage target without labeling it `[ASSUMED — verify]`.
3. **Ops pass — adopt the Chief Operating Officer** (`specialized/chief-operating-officer.md`). Review capacity vs. commitments: what is promised for delivery this week/month vs. what the notes say can actually ship. Identify firefights, and mark any recurring one as needing root-cause work, not another heroic fix. Name the single ops constraint of the week.
4. **Cash pass — adopt the Treasury & Cash Manager** (`finance/finance-treasury-cash-manager.md`). From the provided balances only: cash position by entity (free vs. trapped/restricted if distinguishable), obligations landing in the next 1–4 weeks vs. cover, and covenant/facility flags — projected pressure is flagged now, not at test date. Every number carries its as-of date and source (bank-confirmed vs. ledger-derived vs. user-stated).
5. **Combine into the one-pager.** Step out of the personas and write the brief below. Choose the 3 numbers that most change the user's week, the 3 risks worth losing sleep over (worst first, at full volume), and the 3 decisions that must be made this week — each decision framed with a recommendation and a deadline.
6. **Declare the gaps.** List skipped sections and missing data as a standing "bring next Monday" line.

## Output

```markdown
# WEEKLY BRIEF — week of [date]
Data received: [pipeline ✓/✗ · ops ✓/✗ · cash ✓/✗] — sections without data show [DATA NEEDED]

## 3 NUMBERS
1. [metric — value — vs. last week/target — source]
2. ...
3. ...

## 3 RISKS (worst first, full volume)
1. [risk — quantified impact where data allows — which pass surfaced it]
...

## 3 DECISIONS NEEDED THIS WEEK
1. [question — options — recommendation — decide by]
...

## SECTION DETAIL
📊 PIPELINE (Pipeline Analyst) — [findings or [DATA NEEDED]]
🧰 OPERATIONS (Chief Operating Officer) — [findings or [DATA NEEDED]]
💧 CASH (Treasury & Cash Manager) — [findings or [DATA NEEDED]]

## SKIPPED / BRING NEXT MONDAY
[what was not run and what data would unlock it]
```

## Rules

- **No estimates presented as facts.** A section without provided data shows `[DATA NEEDED]` — it is never filled with plausible numbers. Anything inferred is tagged `[ASSUMED — verify]`.
- **Every number states its source and as-of date** (user-provided export, bank-confirmed, ledger-derived, or context file).
- **Partial input, partial run.** One input means one section runs; the skill says explicitly what was skipped and why.
- **Forecast honesty is mandatory**: the realistic weighted pipeline is shown next to the optimistic CRM number, with the gap explained.
- **Bad news at full volume** (no-lies constitution, BLUEPRINT.md §5): "we will miss payroll cover in week 3" — never "liquidity pressures exist".
- Exactly 3-3-3 in the one-pager; overflow goes to section detail, not to a longer list.
- The skill drafts and recommends; the user decides. Nothing is committed, paid, or promised by this brief.
