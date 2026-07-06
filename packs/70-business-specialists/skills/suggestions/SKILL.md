---
name: suggestions
description: The company suggestion channel — captures efficiency proposals from anywhere in the organization (a new skill, agent, department, section, or process change), reviews them for duplication, value, and evidence, and delivers only the reviewed shortlist to the chairman with adopt/decline/defer recommendations. Use when logging an improvement idea, when any agent or skill notices recurring friction, or when the chairman asks "what is the company suggesting?" — run the review monthly.
---

# /suggestions — The Company Suggestion Channel

Bottom-up improvement, with a filter. Any session may log a proposal; nothing reaches the chairman raw. The R&D & Innovation Lead screens every idea against the existing organization, and the chairman receives a short, reviewed decision list — not a suggestion box to wade through.

Agent definitions are installed in `~/.claude/agents/` — read the named agent's file before adopting it.

## Two modes

**LOG** (takes a minute): capture a proposal into the register and stop.
**REVIEW** (the monthly cadence, or on request): screen everything pending and produce the chairman's decision list.

## Inputs
1. Mode — log or review? A message containing one idea = LOG; "review the suggestions" or a month since the last review = REVIEW.
2. The register — read `suggestions-register.md` from the workspace; create it on first use.
3. For REVIEW, also gather the organization's own signals if available: the Front Desk Router's gap report ("asked for but doesn't exist"), the Revalidation Gatekeeper's ledger patterns (recurring failure types), chiefs' recurring friction the user pastes, and lessons from the R&D Lead's experiment ledger.

## Steps — LOG mode
1. Capture the proposal in the register format below: the **problem first** (what recurring pain, with an example), then the proposed fix, its type (skill / agent / department / section / process / tooling), and who raised it (which agent, skill, or the user).
2. One-line duplication glance: if an existing agent or skill already does this, say so immediately and point to it — logged anyway with that note, so the pattern ("people can't find X") is itself data.
3. Confirm it's logged and stop. No pitch to the chairman from LOG mode, ever.

## Steps — REVIEW mode
1. Adopt the **R&D & Innovation Lead** — intake screening is its craft: ideas earn attention with evidence, and a suggestion box that goes nowhere is innovation theater.
2. Collect all `PENDING` register entries plus the organizational signals from Inputs 3.
3. Screen each proposal:
   - **Duplication check** — against the installed roster and skills (verify by searching the actual agent/skill files, not memory). Duplicate → recommend DECLINE with a pointer to the existing owner.
   - **Evidence check** — does the problem recur? One occurrence = DEFER ("watch for repetition"); a pattern across sessions, gate failures, or router gaps = real.
   - **Value vs. effort** — order-of-magnitude only, stated honestly: what it saves weekly vs. what it costs to build and maintain.
   - **Classification** — new skill / new agent / new department or section / process change / tooling — and a 3-line implementation sketch for anything recommended ADOPT.
4. Run the Revalidation Gatekeeper self-check on the review (sources for every claim of recurrence; no invented savings numbers — estimates tagged `[ASSUMED — verify]`).
5. Deliver the **chairman's decision list** and update the register: every entry moves to ADOPTED (with owner + next step), DECLINED (with the reason, so it doesn't resurface monthly), or DEFERRED (with what evidence would revive it).

## Output — the chairman's decision list
```markdown
📬 SUGGESTIONS REVIEW — [date] · 7 pending → 2 recommended, 3 declined, 2 deferred
RECOMMENDED (decision requested):
1. NEW SKILL /vendor-renewals — Procurement flagged 3 missed renewal windows
   this quarter (register #12, #15; gate ledger F-pattern). Sketch: calendar
   sweep + negotiation prep. Effort: small. Decide: build?
2. PROCESS — weekly brief to include FX exposure line (Treasury, #14). Decide: adopt?
DECLINED (no action needed): #11 duplicate of /collect · #13 no recurrence ·
#16 already owned by BI & Data Analyst
DEFERRED: #10, #17 — single occurrences; revive on repetition
```

## Register format (`suggestions-register.md`)
```markdown
| # | Date | Raised by | Problem (evidence) | Proposal | Type | Status |
|---|------|-----------|--------------------|----------|------|--------|
| 12 | 07-06 | Procurement & Vendor Negotiator session | missed SaaS renewal window twice | /vendor-renewals skill | skill | PENDING |
```

## Rules
- **Nothing reaches the chairman unreviewed** — LOG mode never escalates; only REVIEW's screened list goes up.
- **Problem before solution** — a proposal that can't state its recurring pain with an example gets deferred, not polished.
- **Duplicates are answered, not built** — the fix for "this already exists" is a pointer, and repeated duplicates are a discoverability finding for the Router's map.
- **Decisions stay decided** — declined items carry their reason in the register; re-raising requires new evidence.
- **Adopted means owned** — every ADOPT leaves the review with a named owner and a next step, or it's theater.
- The skill drafts and recommends; the chairman decides. Building an adopted agent/skill follows the pack's extension rules (BLUEPRINT §7, `./scripts/check-pack.sh` clean).
