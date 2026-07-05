---
name: onboard
description: Runs the Business Onboarding Interviewer end-to-end — short adaptive question rounds that produce the group-context.md and business-context-<name>.md files every other specialist reads. Use when the user is new to the pack, asks to set up or introduce their business/group, wants agents to "know my business", or when context files are missing or stale and need creating or updating.
---

# /onboard — Business & Group Onboarding

Interview the user about their business (or group of companies) and write the context file(s) that turn every specialist from a generic consultant into *their* staff. This is process P1 of the pack's BLUEPRINT.md: run once per business, refreshed in update mode. The deliverable is always a written file — an interview without the artifact is a chat, not an onboarding.

## Inputs

- Nothing is required up front — the interview IS the input collection. Assume NOTHING: no industry, country, currency, language, or size until the user says it.
- If the user offers existing material (website copy, brochures, chat exports), accept it: mine it for draft answers first, then interview only the gaps — everything mined still gets confirmed or tagged `[ASSUMED — verify]`.

## Steps

1. **Adopt the Business Onboarding Interviewer** — its identity, question style, and rules.
2. **Detect existing context.** Check the working directory for `group-context.md` and `business-context*.md`. If any exist, read their headers and offer **update mode**: list the sections, their review dates, ask what changed, and re-interview only that — do not redo a full onboarding over a live file. If none exist, proceed fresh.
3. **Ask: single business or group?** One question, before anything else: "Is this one business, or a group of companies (a holding structure, multiple entities)?" The answer forks the flow.
4. **Group path — structural round first.** Run one short round on structure: which entities exist and where each is registered (mainland / free zone / offshore / foreign); who owns what; intercompany relationships (who sells to whom, shared services, who funds whom); group-wide rules that override company preferences (brand architecture, delegation-of-authority thresholds, dividend policy, shared banking); which people sit across entities. Write **`group-context.md`** from those answers. Then treat each operating company the user wants onboarded as its own interview via Step 5 — one at a time, confirming which company each round is about.
5. **Per-company interview — adaptive rounds of 5.** Round 1 is the universal five (what it sells, who buys, where/what language, how customers find and buy today, the #1 thing to change in 90 days). Classify the business from the answers, then run rounds 2–3 adapted to type (services/B2B, retail/local, e-commerce, SaaS…), including the voice-evidence round: a real pasted message that sounds like them, always-phrases, banned words, formality per language. Round 4 (numbers: revenue band, margins, team) is offered as clearly skippable, with one line on what each number unlocks. Never more than 5 questions per message; wait for answers; reflect them back briefly.
6. **Write the file(s).** One `business-context-<slug>.md` per company (plain `business-context.md` if there is only one business), using the Interviewer's output structure: What we sell / Who buys / Market & language / How we sell today / Voice (verbatim example) / Numbers (omit section if skipped) / 90-day priority / Instructions for specialist agents. Header carries the interview date and a review date (+90 days). Quote the user's own words wherever possible; every unconfirmed item is `[ASSUMED — verify]` or omitted.
7. **Finish with setup instructions.** Check whether `CLAUDE.md` exists in the workspace. If not, tell the user to copy the pack's template: `cp packs/70-business-specialists/CLAUDE.md.template ./CLAUDE.md` — that is what makes every agent read the context files automatically. Then point them at the next step: "You're onboarded. Issue your first directive with `/directive <goal in plain words>` — the Front Desk Router will take it from there."

## Output

- **`group-context.md`** (group path only) — structure, ownership, intercompany rules, group-wide policies, cross-entity people.
- **One `business-context-<slug>.md` per interviewed company**, in the structure above, dated, with a review date.
- **A closing note**: where the files were written, the CLAUDE.md copy instruction if needed, any sections skipped (offered — never nagged — for later), and the `/directive` pointer.

## Rules

- **Never write a context file from zero answers.** If the user insists on skipping the interview, require at minimum: what the business sells, to whom, and where — those three cannot be assumed. Anything else drafted as placeholder is marked `[ASSUMED — verify]`; fiction never masquerades as fact.
- **Never invent facts.** Anything the user didn't say gets asked, tagged `[ASSUMED — verify]`, or left out. An invented "founded in 2019" poisons every downstream agent.
- **One file per business; never mix businesses.** Confirm which company each answer belongs to; one subsidiary's voice, numbers, or facts never appear in another's file.
- **Voice needs evidence, not adjectives.** No file ships with only "professional but friendly" — get a real example or mark the section unconfirmed.
- **Sensitive numbers are optional.** "Skip" is always a fine answer; skipped sections are omitted entirely, never guessed.
- **Update mode touches only what changed** — refresh the review date, leave confirmed sections alone.
