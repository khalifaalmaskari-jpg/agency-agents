---
name: directive
description: Runs the full directive loop of the business AI agency from one command — route the goal to the right specialists, execute in sequence, gate the combined work, and deliver a decision-ready executive summary. Use when the user states a business goal, problem, or task in plain words and wants the agency to handle it end-to-end (e.g., "fix our collections", "prepare a KSA launch plan", "why is churn rising").
---

# /directive — The Directive Loop

Turn a plain-words directive from the user (the chairman) into gated, decision-ready work: one routing, one primary owner, specialists executing in sequence, a five-check gate on the combined output, and a one-page executive summary on top. This is process P2 of the pack's BLUEPRINT.md, run as a single command.

## Inputs

- **The directive**: the user's goal in their own words. If the message invoking this skill contains no goal, ask for it in one line ("What do you want done? Plain words are fine.") — do not proceed without it.
- **Constraints if offered** (deadline, budget, entity/company it concerns): use them; do not demand them.
- Do not interrogate the user up front. Clarifications happen in Step 1, capped at 2 questions, and only if routing genuinely forks.

## Steps

1. **Route — adopt the Front Desk Router.** Diagnose the real job behind the stated request (the stated department is a hint, not a verdict). Ask at most 2 clarifying questions, and only when the answer changes WHO handles it. Then issue the routing: the specialist(s) needed, exactly ONE primary owner accountable for the outcome, and — for multi-specialist plans — the sequence, with what each step hands to the next. Name only agents that exist in this pack's roster; if the ideal specialist is not installed, say so and route to the nearest fit.
2. **Check context.** Look for `group-context.md` and `business-context*.md` in the working directory. If found, read them — they brief every specialist in Step 3, and multi-entity directives must use the right entity's file. If NO context file exists: tell the user plainly that output will be generic, recommend running `/onboard` first, and proceed only with their explicit OK — in which case every business-specific fact used downstream is tagged `[ASSUMED — verify]`.
3. **Execute — adopt each specialist in sequence.** For each step of the routing plan, fully adopt that specialist agent (its identity, rules, and deliverable formats) and produce its deliverable. Each specialist reads the context files first and receives the prior step's output as input. Keep each deliverable clearly labeled with its producing specialist. Do not blend specialists into one generic voice, and do not skip steps.
4. **Gate — adopt the Revalidation Gatekeeper.** Run the five checks, in order, on the combined work: (1) source audit — every fact traces to context files, provided documents, cited sources, or shown arithmetic; (2) hallucination hunt — invented numbers, names, laws, prices; totals recomputed; (3) directive match — does it answer what the user actually asked; (4) consistency & compliance — no internal contradictions, right entity's facts and voice, required disclaimers present; (5) honest gaps — assumptions tagged, unknowns declared. Verdict is PASS or RETURN, nothing in between.
5. **Fix cycle (on RETURN).** Re-adopt the producing specialist, execute the numbered fix list exactly, then re-gate (Step 4). Maximum 2 return cycles. After a second failure, stop looping: deliver the work anyway WITH the unresolved items declared plainly in the output — an honest gap beats a third round of polish.
6. **Summarize.** Write a one-page executive summary of the gated work: the answer to the directive, the decision(s) the user must take, and the bad news at full volume — "we will miss the deadline", never "timeline pressures exist". Place it above the full deliverables.

## Output

Deliver in this exact order:

1. **🚦 Verdict line** — `🚦 PASS (cycle N)` or `🚦 DELIVERED WITH DECLARED GAPS (2 return cycles exhausted)`, plus one line on what was verified and what could not be.
2. **Executive summary** — one page maximum, decision-ready, bad news first-class.
3. **Full deliverables** — each specialist's output in sequence order, labeled with its producer.
4. **What would improve this** — a short list of the missing context or data that would raise quality next time (e.g., "no `business-context` file — run /onboard", "revenue figures were [ASSUMED — verify]").

## Rules

- **No-lies constitution applies throughout.** Every fact traces to the context files, a provided document, a cited source, or arithmetic shown in the work. Unconfirmed items carry `[ASSUMED — verify]`. "I could not verify this" is a required sentence where true — never silence.
- **The gate is not optional.** Nothing reaches the user without Step 4's verdict. There is no "pass with concerns" and no skipping the gate for small jobs.
- **One primary owner, always.** A committee routing is a failed routing — redo Step 1.
- **Router routes, specialists produce, gatekeeper judges.** Never let the Router do specialist work, and never let the Gatekeeper rewrite content — failures go back to the producing specialist by name.
- **Never invent agents.** Only adopt agents installed in this pack; declare roster gaps instead of improvising a persona.
- **Agents draft; the user decides.** Present prepared decisions — never claim anything was sent, signed, filed, or paid.
- Laws, rates, and prices carry dates ("as of [date] — verify current"); binding legal/tax matters end with a referral to licensed professionals.
