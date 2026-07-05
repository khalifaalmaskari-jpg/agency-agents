---
name: campaign
description: Builds a complete marketing campaign — brief, copy variants (English and Arabic where needed), media plan, and measurement plan — by chaining the CMO, copywriters, and paid specialists. Use when the user wants to launch, promote, or advertise something, asks for a campaign, ads, a promotion, or a product/offer push across one or more channels.
---

# /campaign — Marketing Campaign Builder

Turn a business goal into a launch-ready campaign package: one brief, tested copy in every required language, a media plan if money is being spent, and a measurement plan with a named primary metric — all grounded in the business's context files, never in invented audience data.

## Inputs

Collect before starting; ask for anything missing, never fabricate:

1. **Goal** — what the campaign must achieve (leads, sales, bookings, awareness) and by when.
2. **Audience** — who exactly; if `business-context-<company>.md` defines segments, confirm which one.
3. **Offer** — the product/service/promotion, and what makes it worth responding to.
4. **Budget range** — even rough ("under AED 5k / month"); "organic only" is a valid answer.
5. **Channels** — user's preference or "recommend for me".
6. **Language(s)** — English, Arabic, or both; if Arabic, ask which audience (Gulf, wider MENA, expat).

Read `business-context-<company>.md` (voice, customers, channels) and `group-context.md` if cross-entity. If neither exists, say so and mark every audience/voice claim `[ASSUMED — verify]`.

## Steps

1. **Adopt Chief Marketing Officer.** Produce the campaign brief:
   - ONE message, ONE audience, ONE desired action. Reject scope creep — a second audience means a second campaign; say so and offer to run it separately.
   - Channel choice with reasons tied to where this audience actually is (from context or user input — otherwise `[ASSUMED — verify]`).
   - Measurement plan: one named primary metric with target and measurement method, plus 2–3 supporting metrics.
   - Budget allocation across the chosen channels within the user's range, with the reasoning shown.
2. **Adopt Conversion Copywriter.** Against the brief: a hook batch (8–12 hooks, varied angles), then full copy variants per chosen channel (minimum 2 variants per placement). Attach a named test hypothesis to each variant pair ("V2 leads with price anchor — hypothesis: cost objection is the blocker").
3. **If Arabic is required, adopt Arabic Copywriter.** Transcreate — do NOT translate — the winning concepts. State the register choice explicitly (MSA vs. Gulf dialect vs. mixed, and why for this audience). Flag RTL/typography notes for designers. Arabic variants carry their own test hypotheses.
4. **If paid spend is planned**, adopt the matching specialist: **PPC Campaign Strategist** for search/shopping/Performance Max, **Paid Social Strategist** for Meta/LinkedIn/TikTok/X/Snapchat. Produce the media plan: structure, budget split across the given range, audience targeting, flighting, and the spend level below which the channel is not worth running.
5. **Gate self-check** (as Revalidation Gatekeeper, on the assembled package) — see Rules.

## Output

Deliver as one package, in this order:

1. **Campaign Brief** — goal, audience, message, offer, channels with rationale, timing.
2. **Copy Variants** — per channel, per language; each variant labeled with its test hypothesis.
3. **Media Plan** — only if paid: structure, budgets, targeting, flighting (omit section entirely if organic).
4. **Measurement Plan** — primary metric (named, with target and how it will be read), supporting metrics, review cadence, and the kill/scale decision rule.

## Rules

- No invented facts or numbers: no made-up CTRs, CPCs, market sizes, or "industry benchmarks" without a source. Budget math uses only the user's range.
- Anything not confirmed by the user or a context file is tagged `[ASSUMED — verify]`.
- Platform policies, ad formats, and pricing shift: material claims about them carry "as of [date] — verify current."
- Arabic output is transcreation with a stated register decision — never sentence-by-sentence translation.
- One message, one audience per campaign. Split rather than blend.
- **Finish with a Revalidation Gatekeeper self-check pass:** every fact sourced, no invented numbers, output answers the stated goal, assumptions tagged, gaps declared. Fix failures before delivering; declare in writing anything that could not be verified.
