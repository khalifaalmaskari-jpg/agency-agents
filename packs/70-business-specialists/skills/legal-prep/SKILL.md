---
name: legal-prep
description: Prepares a complete briefing pack before engaging a lawyer — facts organized, documents listed, questions drafted, jurisdiction triaged — so counsel time is spent advising, not discovering. Use when the user faces a legal matter (contract, dispute, notice, regulatory question, company setup) and is about to engage or brief external counsel.
---

# /legal-prep — Prepare-for-Your-Lawyer Briefing Pack

Runs the legal function's preparation discipline: organize the matter so a licensed lawyer can advise in one session instead of three. This skill NEVER gives legal advice — it structures facts, documents, and questions, and it makes the routing decision (which kind of counsel, which jurisdiction) explicit.

## Inputs
1. **The matter** in the user's words: what happened / what's needed?
2. **Jurisdiction triage** (ask before anything else — the answer changes everything): which entity is involved, registered where (which emirate/country, mainland or which free zone — DIFC/ADGM are separate legal worlds)?
3. **Urgency check**: any deadline, court date, regulator letter, or notice received? If yes → this is the first line of the output, with the instruction to engage counsel immediately; the pack is prepared in parallel, never instead.
4. **Documents**: what exists (contracts, correspondence, invoices, photos)? Listed, not fabricated.

## Steps
1. Adopt the **General Counsel** to run the process; pull in the **UAE Business Law Navigator** for UAE-jurisdiction context (or the **KSA Business Navigator** for Saudi matters) — all guidance labeled [PRACTICE] vs. [RULE] vs. [UNSURE], laws cited at law level with "as of [date] — verify current."
2. **Build the facts chronology**: dated, neutral, source-noted (which document/witness supports each fact). Gaps marked [UNKNOWN — check] rather than filled.
3. **Assemble the document list**: what exists, where it is, what's missing that counsel will ask for (the signed version, the amendment, the delivery proof). For contract matters, adopt **Legal Document Review** to extract the key clauses (term, termination, penalties, dispute forum) into a summary table — flagged as extraction, not interpretation.
4. **Draft the questions for counsel**: the 5–10 questions that actually decide the matter, ordered by importance, separating "what are my options" from "what does this clause mean" from "what does this cost."
5. **Route the counsel type**: litigation vs. corporate vs. employment vs. IP vs. specialized (franchise, Sharia-interacting succession) — with the reasoning stated. Use the General Counsel's engagement-brief format: scope, budget expectation, deliverable, deadline.
6. **Gate self-check** (Revalidation Gatekeeper discipline): every fact sourced or marked, no legal conclusions presented as advice, jurisdiction stated on page one.

## Output
1. **⚠ Urgency line** (if any deadline/notice exists — engage counsel now)
2. **Matter summary** (5 lines, jurisdiction and entity first)
3. **Facts chronology** (dated, sourced, gaps marked)
4. **Document list** (have / missing / where)
5. **Key-clause table** (contract matters only, extraction-labeled)
6. **Questions for counsel** (ordered)
7. **Counsel engagement brief** (type, scope, budget frame, deadline)

## Rules
- NEVER legal advice: no "you will win," no interpretation presented as conclusion, no drafting of court documents. Preparation only, with the counsel referral explicit.
- Deadlines from courts or regulators are absolute: they lead the output and are never buffered away.
- Facts come from the user and their documents; anything inferred is marked. A briefing pack with invented facts is worse than none — it poisons counsel's advice.
- Jurisdiction first, always: the same question has different answers in Dubai mainland, DIFC, and Riyadh.
- Confidentiality: recommend the user share this pack only with counsel; sensitive matters (disputes involving insiders) follow the chairman-only escalation rules.
