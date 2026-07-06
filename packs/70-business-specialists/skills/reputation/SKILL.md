---
name: reputation
description: Turns pasted reviews and customer messages into ready-to-send responses in the business's voice, plus a recurring-themes report routed to the owning chief and an escalation list. Use when the user pastes Google/Trustpilot/marketplace reviews, mentions a bad review or star-rating problem, or has WhatsApp customer messages that need replies.
---

# /reputation — Reviews & Customer-Message Runner

Handles the public and private voice of the business in one pass: draft the reply each review deserves, answer the WhatsApp queue in the business's own voice, and mine the pile for the operational findings hiding in it — because five reviews about late delivery is a logistics finding, not a communications problem. Agent definitions are installed in `~/.claude/agents/` — read the named agent's file before adopting it.

## Inputs

Ask for what is missing; never invent a review, a customer, or an order detail:

1. **The material** — pasted reviews (Google/Trustpilot/marketplace: text, star rating, platform, date) and/or WhatsApp customer messages needing replies. Screenshots described are fine; summaries of "lots of angry reviews" are not — get the actual texts.
2. **Voice** — read `business-context-<company>.md` for voice rules, language norms, and real examples; if absent, ask for two examples of how the business normally writes to customers. Read `group-context.md` if multiple entities are involved — one company's voice never leaks into another's replies.
3. **The facts behind the complaints** — what actually happened per case, if the user knows. A reply can acknowledge without conceding; it cannot assert facts nobody confirmed.
4. **Escalation contacts** — who handles legal threats and safety claims, if not already in the context files.

## Steps

1. **Adopt Reviews & Reputation Manager** for the review work. Classify each review: positive / negative-legitimate / unfair-but-genuine / suspicious-fake.
2. **Draft each review response for its type**, written for the future reader browsing reviews — not to win the argument with the reviewer:
   - **Positive** — specific thanks, no copy-paste gratitude, invite them back.
   - **Negative-legitimate** — acknowledge, own what's ours, state the fix, take the details offline. Never disclose the customer's private details (orders, payments, health, address) in a public reply, even if they disclosed them first.
   - **Unfair** — calm, factual, once; correct the record for the future reader and stop. No arguing threads.
   - **Suspicious-fake** — flag through the platform's reporting process and draft a neutral public note; never accuse the reviewer of lying in public.
3. **Extract recurring themes** — cluster the pile into operational findings with counts and example quotes, and route each to the owning chief: delivery/fulfilment themes → COO's track with the **Logistics & Last-Mile Strategist**; product themes → CSO's track with the **Feedback Synthesizer**; service/staff themes → the relevant chief. A theme with three-plus occurrences is a finding, not noise.
4. **Adopt WhatsApp Business Specialist** for the message queue: draft each reply in the business's voice per the context-file rules — short, human, one clear next step; commitments (refunds, redeliveries, dates) only where the user confirmed them, otherwise `[ASSUMED — verify]` and flagged before sending.
5. **Build the escalation list** — anything beyond reputation handling: legal threats or defamation → **General Counsel**; safety/injury/product-harm claims → **HSE & Quality Manager** investigation track; suspected-fake campaigns at scale → note for counsel too.
6. **Gate self-check** — see Rules.

## Output

1. **Ready-to-send responses** — per review: type, the drafted public reply; per WhatsApp message: the drafted reply. All in the business's voice.
2. **Theme report** — recurring findings with counts, example quotes, and the owning chief each is routed to.
3. **Escalation list** — legal threats, safety claims, suspected-fake activity, each with its route and urgency.

## Rules

- Never fake: no fabricated reviews, no incentivized positive-only schemes, no astroturfing, no review-gating that filters out unhappy customers. If asked, decline and say why — platforms ban it and regulators fine it.
- Public replies never disclose customer private details, order specifics, or dispute internals; details move to a private channel.
- No admissions of legal liability in any reply; anything with legal exposure goes through the escalation list before sending.
- Facts in replies trace to the user's account of events; unverified versions are acknowledged ("we're looking into this"), not asserted. Anything inferred is tagged `[ASSUMED — verify]`.
- Same review type → same standard of response; exceptions are deliberate and noted.
- The skill drafts — the user decides and sends. Nothing is posted, replied to, or reported on the user's behalf.
- **Finish with a Revalidation Gatekeeper self-check pass:** every reply matches its review's facts and type, voice rules followed, no private data or liability admissions in public drafts, theme counts trace to the pasted material, escalations complete, gaps declared.
