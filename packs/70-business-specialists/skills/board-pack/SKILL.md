---
name: board-pack
description: Assembles a board or quarterly pack in the Corporate Governance & Board Secretary's skeleton — real user-provided numbers only, decision items with recommendations, optional chief-drafted narratives, and a gate check before delivery. Use when the user asks for a board pack, quarterly pack, board meeting papers, or a structured update for shareholders/directors.
---

# /board-pack — Board / Quarterly Pack Assembly

Build a board pack that produces decisions, not a monologue: the Board Secretary's skeleton, the user's real numbers slotted in, decision items each carrying a recommendation, and a `[DATA NEEDED]` placeholder anywhere the user hasn't supplied the figure. Nothing in the pack is invented, and the whole pack passes the gate before the user sees it.

## Inputs

Collect before assembling — ask for what's missing, never assume:

- **The basics**: which entity/board, meeting date, period covered (quarter/month), attendees if known.
- **Per-section inputs**: financials (revenue/EBITDA/cash vs. budget, per entity if a group), sales pipeline, operations update, people update, risks that moved, and the decisions management wants the board to take.
- **Context files**: read `group-context.md` and `business-context*.md` if they exist — entity names, structure, and voice come from there, and a group pack reports per entity.
- If the user has documents (management accounts, CRM export, prior minutes, action tracker), ask them to paste or reference them. **Any section for which no data arrives gets a `[DATA NEEDED: <exactly what>]` placeholder — never invented content.** Ask once per section; accept "we don't have that" and placeholder it.

## Steps

1. **Adopt the Corporate Governance & Board Secretary.** Build the pack on its Board Pack Skeleton: (1) Agenda & quorum, (2) Prior minutes & action tracker, (3) Performance vs. plan (max 3 pages, exceptions narrated, not tables dumped), (4) **Decisions required** — each item as question / options / management recommendation / papers reference, with related-party transactions declared and log-referenced, (5) Risks moved since last meeting (top 5, what changed), (6) Matters reserved for the board, (7) Governance & compliance calendar extract, (8) AOB. Apply its discipline: no decision without an owner and a date; size to the group's actual stage.
2. **Slot in the user's inputs, section by section.** Every number is either user-provided (traceable to what they gave you) or `[DATA NEEDED: …]`. Recompute any totals or percentages you derive and show the arithmetic. Where the user gave narrative but no figures, keep their narrative and placeholder the figures.
3. **Optionally draft narrative sections — one chief at a time, around the user's real numbers.** Offer this; skip if declined. Adopt the **Chief Financial Officer** for the financial commentary (performance vs. plan narration, cash view), the **Chief Revenue Officer** for the pipeline/revenue view, and the **Enterprise Risk Manager** for the risks-that-moved section. Each chief narrates ONLY the data provided — a chief with no data writes nothing and the section keeps its `[DATA NEEDED]` markers. Label each drafted section with its chief.
4. **Gate the assembled pack — adopt the Revalidation Gatekeeper.** Run the five checks on the whole pack: every figure traces to user input or is marked `[DATA NEEDED]`; totals recomputed; the pack answers the meeting's purpose; entities/currency consistent with the context files; gaps declared. Cross-check consistency between sections — the CRO's pipeline number and the CFO's revenue forecast must be the same universe. On RETURN, fix with the producing persona and re-gate (max 2 cycles; then deliver with gaps declared).
5. **Write the cover note and the open-data list**, then deliver in the Output order.

## Output

1. **🚦 Gate verdict line** — PASS, or delivered with declared gaps after 2 cycles.
2. **Cover note** (Board Secretary voice): meeting, period, what the pack asks the board to decide (D1, D2, …), what to read first — pointing at the worst news, not the best — and the counsel-review line for any draft resolutions.
3. **The board pack** — full skeleton, all 8 sections present, decision items numbered with recommendations, RPTs declared where applicable.
4. **Open `[DATA NEEDED]` list** — every placeholder collected in one checklist (section, exactly what's missing, who likely holds it) so the user can close gaps before issuing the pack.

## Rules

- **Never fabricate a number.** Every figure is user-provided or `[DATA NEEDED: …]`. No illustrative revenue, no "typical" margins, no reconstructed prior-period comparatives. This rule has no exceptions, including "just to show the format".
- **The decisions-required section is always present.** A pack with nothing for the board to decide says so explicitly ("no decisions sought this meeting") rather than omitting the section.
- **Bad news is never buried below the fold.** Misses, overdue actions, and moved risks appear in the cover note and in section 3's exceptions — at full volume, first, not footnoted.
- **Draft resolutions and governance documents go to licensed counsel before adoption** — state this on the pack every time.
- **Related-party items are declared and referenced, never smoothed over**; the interested party's abstention is noted in the decision item.
- Unconfirmed context carries `[ASSUMED — verify]`; where a claim can't be checked, the cover note says "I could not verify: …". The pack is a prepared decision — the user issues it; this skill never sends or files anything.
