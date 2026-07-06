---
name: it-landscape
description: Builds or updates the group systems landscape map — every system per entity with owner, cost, renewal, and satisfaction — then adds portfolio dispositions (tolerate/invest/migrate/eliminate), a SaaS zombie-subscription audit, and a backup/DR reality check. Use when the user asks for the CIO's systems review, an IT inventory or landscape map, wants to find duplicate or wasted software spend, or asks "what systems do we actually have?"
---

# /it-landscape — Group Systems Landscape Review

The CIO's first-quarter chief artifact (BLUEPRINT §6): one map of every system the group runs, what each costs, who owns it, whether it deserves to live — and whether the backups would actually restore. Agent definitions are installed in `~/.claude/agents/` — read the named agent's file before adopting it.

## Inputs

Ask for what is missing; never fabricate a system, cost, or renewal date:

1. **Entity list** — which companies are in scope. Read `group-context.md` for the holding structure; if absent, ask.
2. **Per entity, per category** — ERP/accounting, CRM, HR/payroll, e-commerce, collaboration/email, and custom/in-house systems: system name, business owner, annual cost, renewal date, and user satisfaction (rough 1–5 is fine).
3. **Existing map** — if `systems-landscape.md` exists in the workspace, read it and run in UPDATE mode: confirm what changed rather than re-interviewing everything.
4. **Backup/DR facts** — for each critical system: is it backed up, where, and when was a restore last actually tested?

Read `business-context-<company>.md` files for operational color (channels, criticality). Partial answers are fine — record gaps as gaps.

## Steps

1. **Adopt Chief Information Officer** to run the review. Interview entity by entity against the category list; accept "I don't know" and mark it `[UNKNOWN — owner to confirm]`. Anything inferred rather than stated gets `[ASSUMED — verify]`.
2. **Build the landscape map** — one table per entity plus a group roll-up: system, category, owner, annual cost, renewal date, satisfaction, criticality.
3. **Adopt Enterprise IT Architect** for the portfolio pass:
   - Assign each system a disposition — **tolerate** (works, leave it), **invest** (strategic, fund it), **migrate** (replace, with target named), **eliminate** (retire, with savings) — one-line rationale each.
   - Call out duplication explicitly: five accounting systems across the group is an architecture finding, not five local preferences. Name consolidation candidates and the order-of-magnitude prize.
4. **Run the SaaS/license audit prompts** — walk the user through zombie hunting: subscriptions nobody named as owned, licenses exceeding headcount, tools with satisfaction ≤2 still on auto-renew, renewals inside 90 days (negotiation window closing). List each suspect with the question the user must answer.
5. **Backup/DR reality check** — per critical system: backup exists? restore tested, when, by whom? Anything without a *tested* restore is marked `[UNPROVEN]` — a backup that has never restored is a hope, not a control. Feed material exposures to the risk register.
6. **Write the recommendations** — top 5 actions ranked by risk and money, each with an order-of-magnitude cost (thousands / tens of thousands / more — clearly labeled estimates, not quotes).
7. **Write the state file** — save/update `systems-landscape.md` in the workspace: the map, dispositions, audit findings, DR status, recommendations, and a review date so the next run diffs instead of restarting.
8. **Gate self-check** — see Rules.

## Output

1. **Landscape map** — per-entity tables + group roll-up with total annual spend.
2. **Disposition table** — every system: tolerate/invest/migrate/eliminate + rationale; duplication findings highlighted.
3. **Zombie/license audit list** — suspects with the confirming question per item.
4. **Backup/DR status strip** — tested / untested `[UNPROVEN]` / none, per critical system.
5. **Top-5 recommendations** — ranked, with order-of-magnitude costs and named owners.
6. Updated `systems-landscape.md` written to the workspace.

## Rules

- No invented systems, costs, or renewal dates — everything traces to the user's answers or the existing state file; estimates are labeled estimates and unknowns stay `[UNKNOWN]` or `[ASSUMED — verify]`.
- Dispositions are recommendations with reasons, not decrees — migration/elimination calls that cut across entities go to the chairman; the skill drafts, the user decides.
- "Backed up" without a tested restore is always reported as `[UNPROVEN]` — never softened.
- Vendor pricing and contract terms cited from memory carry "as of [date] — verify current"; actual renewals are confirmed against the contract, not the map.
- One entity's systems and costs never leak into another entity's report beyond the group roll-up.
- **Finish with a Revalidation Gatekeeper self-check pass:** every cost and date traces to an input, dispositions each have a rationale, duplication math is shown, `[UNPROVEN]`/`[ASSUMED]` tags present, gaps declared rather than papered over.
