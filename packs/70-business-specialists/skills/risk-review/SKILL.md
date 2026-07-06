---
name: risk-review
description: Runs the quarterly group risk review — updates the risk register, aggregates exposures across entities, scores movement, and produces the board risk report with heat map narrative. Use when the user wants to review/update group risks, prepare the quarterly risk report, or assess a new risk that emerged.
---

# /risk-review — Quarterly Group Risk Review

Runs the Enterprise Risk Manager's quarterly cycle: register update, cross-entity aggregation, movement narrative, and the one-page board report. Also handles single-risk mode ("we just learned X — how bad is it?") by slotting a new risk into the same discipline.

## Inputs
1. **Mode**: full quarterly review, or single new risk?
2. **The current register**: read from `risk-register.md` in the workspace if it exists — check before asking; otherwise take a pasted register (from a prior run or elsewhere). No register → offer to build the starter register first (that's part of the run, not a blocker).
3. **What changed this quarter**: incidents, near-misses, new dependencies (big new customer/supplier/system/market), exercise findings from `/bia` or `/crisis` drills, audit findings.
4. **Context files**: read `group-context.md` for the entity map — aggregation needs it.

## Steps
1. Adopt the **Enterprise Risk Manager** for the entire run.
2. **Update the register**: walk the existing top risks — for each: still real? movement (better/worse/same) with the *reason*, treatment status (avoid/mitigate/transfer/accept), owner and review date still valid? Scores backed by reasoning ("high" must cite what it would cost), never vibes.
3. **Add the new**: from the user's "what changed" input, draft new risk entries — inherent vs. residual scored, owner proposed, treatment recommended. Insurance-transfer candidates flagged to the **Insurance & Risk Manager**; continuity-planning candidates to `/bia`; security risks noted for the **Chief Information Security Officer's** register.
4. **Aggregate across entities**: the signature check — five subsidiaries each "low" on the same bank, customer, supplier, or system is ONE group-level risk. Run the concentration sweep explicitly (banks, top customers, suppliers, key people, systems, sites) against `group-context.md`.
5. **Accepted-risk restatement**: list every accepted risk with who accepted it and when — re-presented so acceptance stays a conscious choice, not amnesia.
6. **Produce the board report**: heat map (described in a table if no visual), movement narrative (what got worse, what got better, what's new — in that order), top-10 with treatment status and next step each, decisions needed from the chairman.
7. **Gate self-check**: every score reasoned, every risk owned, no risk theater (a register nobody will review is itself reported as the top process risk).

## Output
1. **Updated risk register** (table: risk, entity/group, inherent → residual, movement + reason, treatment, owner, review date) — written back to `risk-register.md` in the workspace so the next cycle starts from it
2. **Concentration findings** (cross-entity aggregations discovered)
3. **Accepted-risk list** (restated with acceptor and date)
4. **Board risk report** (one page: heat map table, movement narrative, decisions needed)
5. **Action list** (new treatments with owners; items routed to insurance / BIA / CISO / audit)

## Rules
- Scores cite consequences: "HIGH" states what it would cost in money, license, or safety — unreasoned scores are returned to the discussion, not recorded.
- Aggregate before reassuring: entity-level comfort never overrides the group concentration sweep.
- "Accept" is a signed decision with a name and date — defaults and silences are flagged, never recorded as acceptance.
- Every top-10 risk shows its next step; a register entry without an action is a worry, not a managed risk.
- Numbers and exposures come from the user or are marked [ASSUMED — verify]; the skill never invents loss estimates.
