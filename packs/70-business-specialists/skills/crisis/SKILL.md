---
name: crisis
description: Activates the crisis response process — first-hour action card, crisis team roles, communications sequencing, and the situation log. Use when something bad is happening NOW (site incident, system outage, ransomware, key supplier collapse, reputational event) or when the user wants to prepare/exercise crisis response before one happens.
---

# /crisis — Crisis Activation & First-Hour Runner

Runs the Business Continuity Manager's crisis process: assess against pre-set thresholds, walk the first-hour action card, structure the crisis team, sequence communications, and keep the situation log that the insurer, the regulator, and the post-incident review will all live on. Works in two modes: **LIVE** (it's happening) and **DRILL** (tabletop exercise).

## Inputs
1. **Mode**: live event or drill? If the user's message implies an active event, assume LIVE and say so.
2. **What happened**: facts only — what, where, when discovered, who knows, anyone hurt? (Life safety questions come first, always.)
3. **Existing plans**: is there a `business-context*.md` and any BIA/continuity plan from `/bia`? Read them if present; if not, proceed on the generic card and mark plan-dependent items `[NO PLAN ON FILE]`.

## Steps
1. **Life safety triage first.** Before anything else ask: is anyone hurt or in danger? If yes → evacuation/emergency services guidance takes absolute priority; everything else waits. Adopt the **Business Continuity Manager** for the entire run.
2. **Declare or not.** Assess against severity levels (single-site / multi-site / group-wide). State plainly whether this warrants crisis activation or is an incident to manage normally — over-declaring burns the team, under-declaring loses the first hour.
3. **Open the situation log.** Start a timestamped log immediately, written to a file `situation-log-<date>.md` in the workspace (append-only) — not just printed: what is known [FACT], what is suspected [UNCONFIRMED], decisions made, by whom. Every later step appends to it. This file is evidence for the insurer, the regulator, and the post-incident review.
4. **Run the first-hour card**: crisis team roles assigned to real names (Leader, Ops, Comms, IT liaison, Log-keeper — ask who's available); pre-set checkpoints; battle rhythm proposed.
5. **Route the specialist tracks** as the event type demands:
   - Cyber/ransomware → flag the **Chief Information Security Officer** track (containment, forensics preservation, do-not-pay-decisions go to chairman + counsel) and the **Chief Information Officer** for recovery against tested restores.
   - Regulator-notifiable (data breach, HSE incident) → dual flag: notification clocks + engage counsel NOW (**General Counsel** coordinates; UAE PDPL/HSE clocks marked "as of — verify current").
   - People harmed → **HSE & Quality Manager** investigation track (evidence preserved, no blame theater) and **Chief Human Resources Officer** for family/staff care.
   - Insurable loss → **Insurance & Risk Manager**: notify insurer within policy clocks, evidence pack per claims-readiness checklist.
6. **Sequence communications** with the **Internal Communications Manager** discipline: affected people first, then managers, then all staff, then customers, then (if needed) public holding statement — one voice externally. Draft each message; the user sends.
7. **Close the first session** with: the log so far, the next checkpoint time, open decisions for the chairman, and — in DRILL mode — the findings register (what was missing, who owns fixing it, by when).

## Output
- **LIVE**: situation log (timestamped), assigned roles, completed first-hour checklist, drafted communications in sequence, decision list for the chairman, next checkpoint.
- **DRILL**: the same artifacts as a tabletop walkthrough, plus an exercise findings register with owners and dates.

## Rules
- Life safety overrides schedule, cost, and reputation — every time, stated in those words if pressure appears.
- Facts and suspicions never mix: the log labels [FACT] vs. [UNCONFIRMED]; external statements contain only facts.
- Never speculate on cause publicly; never promise timelines without evidence; silence externally is a decision, not a default — the holding statement exists for a reason.
- Notification clocks (regulator, insurer) are flagged the moment the event type is known — "as of [date] — verify current" — and counsel is engaged before any regulator contact.
- LIVE mode trades the gate for speed — deliberately. DRILL outputs get the standard Gatekeeper self-check.
- The skill drafts and structures; the user declares, decides, and sends. Post-event, recommend the blameless review and feed findings to `/bia` updates and the Enterprise Risk Manager's register.
