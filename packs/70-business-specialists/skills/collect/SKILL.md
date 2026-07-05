---
name: collect
description: Turns an accounts-receivable aging list into a prioritized collection plan — dunning sequences per debtor (email and WhatsApp), escalation stages, and a personal-action decision list. Use when the user mentions unpaid invoices, overdue customers, cash collection, chasing payments, or pastes an AR aging report.
---

# /collect — Get-Paid Runner

Convert a list of who-owes-what into money in the bank: prioritize the debtors, generate the right reminder at the right escalation stage for each one in the business's own voice, and hand the user a short decision list of the calls only they can make.

## Inputs

Ask for what is missing; never invent a debtor, amount, or date:

1. **AR aging list** — pasted or described: debtor name, amount, invoice date/due date or days overdue, and any partial payments. If the user has only a vague picture ("a few clients owe me"), interview until each debtor has at least name + approximate amount + approximate age.
2. **Relationship notes per debtor** — strategic account? repeat offender? disputed invoice? personal relationship? ongoing work?
3. **History** — what reminders have already been sent, and any promises made by the debtor.
4. **The user's real red lines** — will they actually stop work? charge late fees stated in the contract? go legal? (Needed for Rule 2.)

Read `business-context-<company>.md` for voice and customer norms; if absent, ask for one example of how the business normally writes to customers.

## Steps

1. **Adopt Accounts Receivable & Collections Specialist** for everything below.
2. **Prioritize the list** by amount × age × relationship: rank debtors into (a) chase hard now, (b) chase normally, (c) handle personally/delicately, (d) probable write-off candidates. Show the reasoning per debtor in one line each.
3. **Assign each debtor an escalation stage** based on age and history: friendly nudge → firm reminder → final notice → decision point. Never restart a debtor at "friendly" if they have already had firm reminders — continuity matters.
4. **Generate the dunning message for each debtor at their stage**, in the business's voice, in BOTH formats: an email version and a WhatsApp version (shorter, no attachments assumed, still professional). Include invoice reference, exact amount, and a specific requested action with a date.
5. **Build the decision list for the user**: who to call personally (and the one sentence to open with), who to stop work for, who to offer a payment plan, who to escalate — with legal steps explicitly flagged as "engage licensed counsel; this is preparation, not legal advice."
6. **Gate self-check** — see Rules.

## Output

1. **Priority table** — debtor, amount, days overdue, relationship note, assigned stage, one-line rationale.
2. **Dunning messages** — per debtor: email variant + WhatsApp variant at their stage, ready to send.
3. **Decision list** — the user's personal actions: calls, stop-work candidates, payment-plan offers, counsel escalations.
4. **Follow-up cadence** — when the next message goes out per debtor if no payment lands.

## Rules

- Firm, never harassing: no threats, no shaming, no contact-frequency that could constitute harassment. Tone escalates in clarity, not hostility.
- **Every promised consequence must be one the user will actually keep.** If they won't stop work, the final notice must not say "we will pause work." Confirm red lines (Input 4) before writing final notices.
- Consistency across customers: same stage → same firmness. Exceptions (the strategic account handled softly) are deliberate and noted, not accidental.
- No invented amounts, dates, invoice numbers, or contract terms — late fees are only cited if the user confirms they are in the contract; otherwise `[ASSUMED — verify]`.
- Legal mechanisms (court, agencies, cheque-related steps in the UAE/GCC) are named only as "discuss with licensed counsel — as of [date], verify current"; never drafted as demands.
- Disputed invoices get a resolution message, not a dunning message.
- **Finish with a Revalidation Gatekeeper self-check pass:** every figure traces to the user's list, stages are consistent, no empty threats, assumptions tagged, gaps (missing amounts/dates) declared rather than papered over.
