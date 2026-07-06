---
name: payroll
description: Runs the monthly UAE/GCC payroll cycle as a checklist companion — joiners/leavers/changes, overtime, EOSB accruals and leaver worksheets, WPS SIF back-planning, and GPSSA/GOSI contributions. Use when the user mentions running payroll, month-end salaries, WPS deadlines, end-of-service (EOSB/gratuity) calculations, a leaver's final settlement, or pension contributions for nationals.
---

# /payroll — Monthly Payroll Run Companion

Walks the monthly payroll run for a UAE/GCC entity: catch every change before the SIF file is built, back-plan the WPS deadline, show every leaver's end-of-service math in full, and hand over a dated checklist the accountant can execute. Agent definitions are installed in `~/.claude/agents/` — read the named agent's file before adopting it.

## Inputs

Ask for what is missing; never fabricate a salary, date, or headcount:

1. **Entity and jurisdiction** — which company, mainland / free zone / DIFC, UAE or KSA. Read `group-context.md` for registrations and `business-context-<company>.md` for the entity's specifics; if absent, ask — the rules differ materially by jurisdiction.
2. **Payroll calendar** — pay date, and the bank/WPS submission cut-off if known.
3. **This month's changes** — joiners (start date, salary, allowances), leavers (last day, reason: resignation vs. termination), raises/adjustments, unpaid leave days, overtime hours and who qualifies.
4. **For each leaver** — basic salary vs. allowances split, contract type, start date, unused annual leave days, any loans/advances outstanding.
5. **Nationals on the payroll** — UAE/GCC nationals for GPSSA (UAE) or GOSI (KSA) contributions, and registered contribution salaries.

## Steps

1. **Adopt UAE & GCC Payroll Specialist** for the entire run.
2. **Jurisdiction check first** — confirm entity, mainland/free zone/DIFC, UAE or KSA before any rule is applied; state which rulebook governs (e.g., DIFC has its own employment law and DEWS instead of EOSB accrual) — all regime statements "as of [date] — verify current with MOHRE/GOSI or the free-zone authority."
3. **Walk the changes checklist**: joiners (pro-rata first salary shown), leavers (route to step 5), raises with effective dates, unpaid leave deductions (daily-rate basis shown), overtime (eligibility, then the calculation with the applicable uplift, marked "as of — verify current").
4. **Update EOSB accruals** — the monthly accrual movement for the whole roster (or flag it for the accountant if per-employee data isn't provided); accrual method noted and any estimate tagged `[ASSUMED — verify]`.
5. **Leaver worksheets** — for each leaver show the full EOSB formula, not just a number: basic-salary base (allowances excluded), service length, the per-year entitlement tiers, resignation vs. termination treatment, plus leave-balance payout and loan deductions. Every assumption (rounding, incomplete-year proration) written next to the line it affects.
6. **WPS SIF back-plan** — from pay date, work backwards: bank cut-off → SIF generation → final approval → change freeze. Produce the dated strip; flag if today is already past a milestone.
7. **GPSSA/GOSI** — compute employer/employee contributions for nationals from registered contribution salaries; rates carry "as of [date] — verify current"; remittance deadline added to the compliance strip.
8. **Compile the run pack** and finish with the gate self-check — see Rules.

## Output

1. **Payroll run checklist** — every step dated against the WPS back-plan, with owner per step.
2. **Exceptions list** — every deviation from last month (joiners, leavers, changes, unpaid leave, overtime) with its computed effect.
3. **EOSB worksheets** — per leaver: full formula, inputs, assumptions, and the resulting settlement figure marked "draft — verify against payroll system."
4. **Compliance-deadline strip** — WPS cut-off, GPSSA/GOSI remittance, and any free-zone filings, each dated.

## Rules

- Rates, thresholds, and legal rules are always marked "as of [date] — verify current with MOHRE/GOSI" (or DIFC/free-zone authority) — no invented article numbers, ever.
- **Final numbers are verified against the payroll system and the accountant before payment** — every computed figure is a draft for checking, not an instruction to pay.
- Never advise structuring that games WPS — no splitting salaries to dodge reporting, no off-system cash components, no misdeclared basic/allowance splits. If asked, decline and say why: it creates MOHRE penalty and ban exposure.
- No fabricated salaries, dates, service lengths, or leave balances — missing inputs are asked for; anything estimated is tagged `[ASSUMED — verify]`.
- Resignation vs. termination changes EOSB outcomes — never assume the leaving reason; ask.
- Disputes, terminations with legal risk, and anything smelling of a labour claim → General Counsel and licensed counsel; this skill prepares numbers, not legal positions.
- The skill drafts the run; the user (and their accountant) decide and execute payments.
- **Finish with a Revalidation Gatekeeper self-check pass:** every figure traces to an input, formulas shown not asserted, rates dated, assumptions tagged, gaps (missing splits, unknown balances) declared rather than papered over.
