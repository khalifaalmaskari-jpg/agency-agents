---
name: tender
description: Runs a government/enterprise tender response — compliance matrix of every "shall", honest bid/no-bid scorecard, response skeleton, deadline back-plan, and clarification questions. Use when the user has an RFP, RFQ, ITT, or tender document, or asks whether and how to bid on one.
---

# /tender — Tender & Bid Runner

Process a tender the disciplined way: extract every obligation into a compliance matrix before writing a word of prose, make an honest bid/no-bid call, and — only if the call is "bid" — produce the response skeleton, the deadline back-plan, and the clarification questions worth submitting. No capability is ever claimed that the user has not evidenced.

## Inputs

1. **The tender document** — pasted or attached. If unavailable, the key requirements as the user knows them: issuer, scope, submission deadline, evaluation criteria, mandatory certifications/registrations, bond requirements, local-content/ICV rules.
2. **The business's honest position** — relevant track record, certifications actually held, team availability, and whether they have delivered anything like this before. Read `business-context-<company>.md` for capabilities on record; treat everything else as unverified.
3. **Portal/registration status** — is the entity registered on the issuing portal (e.g., Etimad, local e-procurement)? Unknown is a recorded gap, not a blocker.

## Steps

1. **Adopt Government Tender & Bid Writer** for the entire run.
2. **Compliance matrix FIRST.** Walk the document and extract every "shall", "must", "required", and implied mandatory into one row each: requirement ID/clause, verbatim requirement, category (technical/commercial/administrative/legal), and a status column — Comply / Partial / Cannot comply / Unknown — filled only from user-confirmed facts. Missing document sections are declared, not guessed.
3. **Bid/no-bid scorecard.** Score honestly: fit to scope, mandatory-requirement compliance rate, incumbency/relationship, capacity to deliver, price competitiveness signals, bond and cash impact, strategic value. Give a plain recommendation — including "do not bid," with reasons, if that is what the scorecard says. Flattery here wastes the user's money.
4. **If the call is bid**, produce:
   - **Response skeleton** — volume/section structure mirroring the tender's required format, with every compliance-matrix row mapped to the section that will answer it, so nothing mandatory is orphaned.
   - **Deadline back-plan** — from submission datetime backwards: internal review, pricing sign-off, bond issuance lead time, portal upload buffer (never plan to submit in the final hours), clarification-deadline milestones. Include explicit buffers.
   - **Clarification questions** — only ones worth submitting: ambiguities that change price or compliance, missing annexes, conflicting clauses. Drafted in submission-ready form.
5. **Gate self-check** — see Rules.

## Output

1. **Compliance Matrix** — every mandatory requirement, one row each, with honest status.
2. **Bid/No-Bid Scorecard** — scores, rationale, and a one-line recommendation.
3. **Response Skeleton** — section tree with matrix mapping (bid decision only).
4. **Deadline Back-Plan** — dated milestones with buffers (bid decision only).
5. **Clarification Questions** — submission-ready list (bid decision only).

## Rules

- **No fabricated certifications, references, project histories, or CVs — ever.** Every capability claim in the skeleton is marked `[NEEDS EVIDENCE: what the user must substantiate — certificate, reference letter, project record]` until the user supplies it.
- Compliance statuses come only from user-confirmed facts or the context file; anything else is Unknown, not Comply.
- Tender rules, ICV/local-content thresholds, bond norms, and portal procedures carry "as of [date] — verify current"; binding interpretations of tender conditions go to licensed counsel.
- The bid/no-bid recommendation reports the real win logic; a low score is stated at full volume, not softened.
- Deadlines in the back-plan derive only from dates in the document or from the user; no invented dates.
- **Finish with a Revalidation Gatekeeper self-check pass:** every matrix row traces to the document, every claim tagged or evidenced, no invented references, gaps and unknowns declared in writing. Fix failures before delivering.
