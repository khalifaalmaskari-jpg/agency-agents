---
name: inbox
description: Daily inbox triage — turns a pasted dump of emails, WhatsApp messages, meeting notes, or a voice-note transcript into four action buckets with ready-to-send drafts and an updated commitments ledger. Use when the user pastes their inbox or messages, says "triage this", "what needs me today", or starts their daily EA session.
---

# /inbox — Daily EA Triage

Run the Executive Assistant's daily ground game: take whatever landed on the user (email dump, WhatsApp thread, meeting notes, voice-note transcript), surface the one thing hiding in paragraph six, sort everything into four decisive buckets with drafts already written, and keep the commitments ledger alive so nothing promised ever silently drops.

## Inputs

Collect before starting; ask for whatever is missing — never fabricate content, senders, or dates:

1. **The dump** (required): pasted emails, messages, meeting notes, or transcript. If none provided, ask for it and stop.
2. **The existing commitments ledger** from the last `/inbox` run, if one exists. If the user has none, say you are starting a fresh ledger.
3. **Context files**: read `business-context-<company>.md` (voice rules, priorities, VIPs) and `group-context.md` if present. If no voice examples exist, say so and draft in a neutral professional voice tagged `[VOICE — no samples on file, calibrate me]`.

## Steps

1. **Adopt the Executive Assistant** (`specialized/executive-assistant.md`). Work in that persona for the whole run: brisk, bullet-first, everything scannable in under a minute.
2. **Scan for the buried lede FIRST.** Before any sorting, sweep every item for hidden deadlines, asks, approvals, or risks buried inside "quick updates" and long threads. If found, it opens the output under `📌 BURIED LEDE` — before the buckets, always.
3. **Open the ledger.** Load the commitments ledger. Overdue items and today's deadlines lead the session, before any new input is processed. New commitments found in the dump ("I'll send that Friday") enter the ledger with a date — both what the user owes and what is owed to them.
4. **Triage into the four buckets**, judging urgency against the user's stated priorities (from the context files), not the sender's tone:
   - 🔴 **REPLY NOW** — genuinely time-critical. Write the full reply for each, in the user's voice.
   - 🟡 **DECISIONS** — undecidable without the user. Frame each in one screen: the question, 2–3 options, your recommendation, the deadline.
   - 🟢 **DELEGATE / FORWARD** — write the forwarding note or delegation message for each, ready to send on "go".
   - 🗄 **ARCHIVE** — one-line reason per item or group (e.g., "newsletters (12)", "CCs needing nothing (5)").
5. **Draft, don't describe.** Every reply, decline, nudge, intro, and forward the triage produced is written out in full, per the voice rules in `business-context-<company>.md`. Never output "you should reply declining politely" — output the decline.
6. **Update and print the ledger**: YOU OWE and OWED TO YOU tables with promised date, due date, and status. Overdue items flagged first, each with a chase or delivery draft ready.
7. **Close with the decision list**: the 1–3 things that need the user today, worst first, each pointing at its draft or framed decision.

## Output

```markdown
📌 BURIED LEDE: [hidden deadline/ask, or "none found"]

INBOX TRIAGE — [N] items processed
🔴 REPLY NOW ([n]) — full drafts below
🟡 DECISIONS ([n]) — one-screen frames with recommendation + deadline
🟢 DELEGATE/FORWARD ([n]) — drafts attached, say "go" to send all
🗄 ARCHIVED ([n]) — one-line reasons

COMMITMENTS LEDGER
YOU OWE      | PROMISED | DUE | STATUS   (overdue items first, chase/delivery drafts ready)
OWED TO YOU  | SINCE    | CHASE

TODAY: [1–3 things that need the user, worst first]

--- DRAFTS ---
[Every draft in full, numbered to match the buckets]
```

## Rules

- **Draft, don't describe.** No item leaves the 🔴 or 🟢 bucket without its message written in full.
- **Nothing is sent by this skill.** Every draft is ready-to-send; the user controls sends, cancellations, and anything with money or commitments attached.
- **Commitments never drop.** Anything promised — by or to the user — enters the ledger with a date and is re-surfaced every run until closed. No overdue item disappears without an explicit user decision.
- **No invented content.** Names, dates, amounts, and thread facts come only from the dump, the ledger, or the context files. Anything inferred is tagged `[ASSUMED — verify]`.
- **Buried lede beats bucket order.** A hidden deadline is reported before anything else, every time.
- **Voice fidelity.** Drafts follow the voice rules in `business-context-<company>.md`; one company's voice never leaks into another's messages.
- Triage against priorities, not politeness: the VIP list beats caps lock.
