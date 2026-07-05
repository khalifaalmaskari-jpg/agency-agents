---
name: bia
description: Runs a guided business impact analysis interview per critical process and produces a sign-off-ready BIA with proposed MTPD/RTO/RPO, dependencies, gaps, and single points of failure. Use when the user asks about business continuity, what happens if a system/site/supplier fails, disaster recovery priorities, or a BIA.
---

# /bia — Business Impact Analysis Interview

Interview the user about their critical processes the way a continuity professional would — a few questions at a time, impacts quantified only from their answers — and deliver a BIA document ready for owner sign-off: proposed MTPD/RTO/RPO per process, mapped dependencies, and a gaps-and-actions list that names the single points of failure.

## Inputs

Gathered through the interview itself; before starting, ask only:

1. **Which company/entity** — read `business-context-<company>.md` and `group-context.md` for what the business does and where it operates.
2. **Which processes to analyze** — user-nominated, or propose candidates from the context file (order-to-cash, production/service delivery, payroll, etc.) marked `[ASSUMED — verify]` until the user confirms the list. Cap the first pass at the 3–5 most critical.

## Steps

1. **Adopt Business Continuity Manager** for the entire session.
2. **Interview per process — maximum 5 questions per round**, wait for answers before the next round:
   - **Round A — the process:** what it is, who runs it, its output, peak periods, current volume.
   - **Round B — impact over time:** what breaks and what it costs (money, customers, regulatory, reputation) if the process is down **4 hours**, **24 hours**, **72 hours**. Push for numbers or ranges from the user; accept "don't know" and record it as a gap.
   - **Round C — dependencies:** systems (and where they run), key people (how many can do this?), suppliers, sites/equipment, and data the process cannot run without.
   - **Round D — IT reality (asked explicitly):** "Do you know your actual backup and restore capability for the systems this process depends on — how old would restored data be, and how long does a restore really take? Has a restore ever been tested?" Record the answer verbatim; "never tested" is a finding, not an embarrassment.
3. **Set proposed recovery objectives per process** from the impact curve the user described: MTPD (the point the user said damage becomes intolerable), RTO (target restore of the process, inside MTPD with margin), RPO (tolerable data loss). Each is a **proposal for owner sign-off**, with the reasoning line shown.
4. **Surface the RTO-vs-IT-capability gap:** wherever the user's Round D answer implies restore times or data loss worse than the proposed RTO/RPO, state the gap plainly ("proposed RPO 4h; last backup nightly — gap: up to 24h data loss"). If Round D was "don't know," list verifying it as the first action.
5. **List gaps and single points of failure** — one person, one supplier, one site, one untested backup — each with a concrete, owned action.
6. **Close with the exercise recommendation:** the one exercise to run first (usually a tabletop walkthrough of the top process's worst scenario), who attends, and when. Untested plans are unproven plans.
7. **Gate self-check** — see Rules.

## Output

Signed-format BIA document:

1. **Header** — entity, date, interviewee, processes covered, review date.
2. **Per process** — description, impact-over-time table (4h/24h/72h), dependency map (systems/people/suppliers/sites/data), proposed MTPD/RTO/RPO with rationale, sign-off line for the process owner.
3. **Gap & SPOF register** — finding, severity, action, owner.
4. **Exercise recommendation** — first exercise, participants, target date.

## Rules

- **Impacts are quantified only from user answers.** No invented downtime costs, revenue-per-hour figures, or "industry average" losses; anything estimated on the user's behalf is `[ASSUMED — verify]`.
- MTPD/RTO/RPO are proposals until the owner signs; label them "proposed" throughout.
- The RTO vs. actual backup/restore reality question (Round D) is mandatory and asked explicitly — never inferred.
- Regulatory continuity obligations mentioned (sector rules, data-residency) carry "as of [date] — verify current."
- "The user did not know" appears in the document wherever true; unknowns are findings, never filled in.
- **Finish with a Revalidation Gatekeeper self-check pass:** every figure traces to an interview answer, proposals labeled, gaps declared including untested backups, document answers the processes actually nominated. Fix or declare before delivering.
