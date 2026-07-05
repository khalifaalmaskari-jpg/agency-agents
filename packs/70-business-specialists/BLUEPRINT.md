# 🏛️ The Group AI Agency — Master Blueprint

> **One chairman. Nine chiefs. 128 specialists. One gate. Zero tolerated hallucinations.**
>
> This document is the complete design of the system: its structure, its processes, its honesty rules, and the plan to put it into operation. If you read nothing else, read this.

**Version:** 1.2 · **Pack:** 158 agents (`agents.txt`) · **Repo:** 294 agents total
**Install:** `./scripts/install.sh --tool claude-code --agents-file packs/70-business-specialists/agents.txt`

---

## 1 · What this system is

A complete AI staff for a group of companies, organized the way a real group is: a chairman who decides, a CEO office that routes, chiefs who own departments, specialists who execute, and an assurance layer that makes sure what reaches the top is **true, sourced, and on-brief**.

Three design principles govern everything:

1. **One owner per job.** Every task has exactly one accountable agent. Chiefs delegate; specialists execute; nobody blends five specialties into one generic answer.
2. **Nothing unverified reaches the chairman.** Every fact needs a source, every assumption a label, every unknown a declaration — enforced by a gate that sends failures back.
3. **Independence where it matters.** Audit and the gate answer to the chairman only. The people who check the work never report to the people who produce it.

---

## 2 · The structure

```
TIER 1 · CHAIRMAN (you)
│  Direct reports (independent of the CEO line):
│  🗳️ Board Secretary · ⚠️ Enterprise Risk Manager · 🌳 Family & Succession
│  🚦 Revalidation Gatekeeper
│  🕵️ AUDIT FUNCTION: Chief Audit Executive → Internal Auditor 🔦 ·
│     Fraud Examiner 🪤 · IT Auditor 🗝️
│
├── 🚦 THE REVALIDATION GATE (everything upward passes through)
│
TIER 2 · CEO OFFICE
│  CEO seat (Chief of Staff) · 🛎️ Front Desk Router · 📥 Executive Assistant
│  🎤 Onboarding Interviewer · 🗂️ Group Portfolio Manager · 📈 Reporting
│  unit (Analytics, Exec Summary, Data Consolidation, BI & Data Analyst 📏)
│
TIER 3 · NINE CHIEF SEATS
   CFO        Finance & Treasury (13): bookkeeping, FP&A, tax, pricing, AP,
              AR & Collections, Treasury, Group Controller, UAE Payroll,
              Insurance, Fundraising, Investor Relations 🪙
   CMO 📢     Marketing & Branding (30): content, copy (EN + Arabic 🖋️),
              email, SEO + local, all social, PR, internal comms 📻,
              WhatsApp, reviews, influencer, e-commerce, events, all paid
              ads, brand & design
   CRO 💹     Revenue & Customers (14): sales, partnerships, customer
              service, success, support, translation
   COO 🧰     Operations (12): workflows, projects, docs, retail 🏪,
              logistics 🛵, procurement, franchise 🎡, BCM 🧯, HSE 🦺,
              facilities 🏢
   CHRO 👥    People (6): recruitment, onboarding, training, org
              psychology, change management
   CSO 🛤️    Strategy & Markets (10): competitive intel 🔬, trends, product,
              M&A, GCC 🦅 & KSA 🏜️ navigation, ESG 🌱
   GC 🔏      Legal & Compliance (8): UAE law 🐪, contracts, privacy,
              tenders 🏆, government relations/PRO 🪪 — binding matters →
              licensed counsel
   CISO 🏰    Security & AI (3 + bench): UAE cyber compliance 🇦🇪, OT 🛢️,
              AI governance 🧿
   CIO 💾     Information Technology (15): IT Service Manager (ITIL 4),
              Enterprise IT Architect 🏙️, Azure ⛅, AWS 🪣, M365 & Copilot 🧑‍✈️,
              Full-Stack 🥞 + Digital Build unit (web, mobile, backend,
              prototyping, CMS, DevOps, UX, AI)
```

Full per-agent roster: see [README.md](README.md). Interactive chart: `agency-org-chart.html`.

---

## 3 · The context architecture (how it sounds like YOUR group)

Three files, read top-down at the start of every session. This is the single most important setup step — without it, every agent is a generic consultant.

| File | Contains | Written by | Read by |
|---|---|---|---|
| `CLAUDE.md` | Standing rules: read context first, quality gate, no invented facts, voice, regional conventions | You (copy from [`CLAUDE.md.template`](CLAUDE.md.template)) | Every agent, automatically |
| `group-context.md` | Holding structure, who owns what, where each entity is registered, intercompany rules, group-wide policies | 🎤 Interviewer (group mode) | Group agents (chiefs, controller, treasury, governance, audit) |
| `business-context-<company>.md` | Per company: what it sells, customers, market & language, channels, voice with real examples, 90-day priority | 🎤 Interviewer (per company) | That company's specialists, on top of the group file |

**Rules:** facts nobody confirmed are marked `[ASSUMED — verify]`, never invented. One subsidiary's voice or facts never leak into another's output. Files carry review dates; the Interviewer's update mode refreshes only what changed.

---

## 4 · The operating processes

### P1 — Onboarding (run once)
```
You → 🎤 Interviewer group mode  → group-context.md
    → 🎤 Interviewer per company → business-context-<name>.md (each)
    → copy CLAUDE.md.template as CLAUDE.md → everything automatic from then on
```

### P2 — The directive loop (every piece of work, same shape)
```
1. YOU issue a directive in plain words
2. CEO OFFICE — 🛎️ Router turns it into a plan: which chief, which
   specialists, what order, ONE primary owner
3. CHIEF plans the department's work, assigns, and runs the FIRST quality
   pass (sources present, assumptions tagged, on-brief)
4. SPECIALISTS execute — briefed by the context files
5. 🚦 GATE — five checks:
     ① every fact has a source        ② hallucination hunt
     ③ answers your actual directive  ④ consistency & compliance
     ⑤ gaps declared, not hidden
   PASS → cover note (what was verified, what couldn't be)
   RETURN → numbered fix list back to the producer (max 2 cycles,
   then it reaches you WITH the gaps declared in writing)
6. EXECUTIVE SUMMARY — one page, bad news at full volume
7. YOU decide — agents draft, the chairman signs
```

### P3 — Multi-department plans
The Router sequences several specialists with one primary owner; each step's output pastes into the next step's prompt. Example — *"launch in Saudi Arabia"*: KSA Navigator 🏜️ (primary) + Competitive Intel 🔬 in parallel → Arabic Copywriter 🖋️ → Paid Social → gate → you.

### P4 — Assurance (three layers, permanently on)
1. **Chiefs** — quality at the source, before the gate
2. **🚦 Gatekeeper** — every deliverable, before your desk
3. **🕵️ Audit function** — planned, independent examination of the whole machine (including, periodically, the Gatekeeper itself), reporting only to you; findings close on **retested evidence**, never promises

### P5 — Escalation rules (pre-decided, not improvised)
- Credible **fraud** indicators, or anything implicating senior management or family → chairman/audit committee **only**
- **Security incidents** → chairman at full severity within the hour — no massaging while "gathering facts"
- **Legal** disputes, deadlines, regulator contact → licensed counsel engaged, GC coordinates
- **Crisis** (site, system, supplier) → 🧯 BCM first-hour action card; pre-set thresholds decide what "counts"
- Gate failures twice → to you with gaps declared

---

## 5 · The no-lies constitution

Written into the agents' instructions and enforced at the gate — not a slogan:

1. Every fact traces to: your context files, a provided document, a cited source, or arithmetic shown in the work. Anything else fails.
2. Assumptions wear labels: `[ASSUMED — verify]`. Research claims wear `[VERIFIED] / [REPORTED] / [INFERRED]`.
3. **"I could not verify this" is a required sentence**, not a weakness.
4. Laws, rates, and prices carry dates: "as of [date] — verify current." No invented article numbers, ever. Binding calls go to licensed humans (counsel, tax, brokers, regulators).
5. Bad news travels at full volume. "We will miss the deadline" — never "timeline pressures exist."
6. The gate tracks its own pass rate: weeks of 100% passes are treated as a broken gate, not a perfect organization.

---

## 6 · Implementation plan

### Day 1 — Install (≈ 15 minutes)
```bash
git clone https://github.com/khalifaalmaskari-jpg/agency-agents.git
cd agency-agents
./scripts/install.sh --tool claude-code --agents-file packs/70-business-specialists/agents.txt
cp packs/70-business-specialists/CLAUDE.md.template /your/workspace/CLAUDE.md
# The skills layer — 14 one-command workflows (see skills/README.md):
mkdir -p ~/.claude/skills && cp -r packs/70-business-specialists/skills/*/ ~/.claude/skills/
```
With skills installed, the processes in §4 become commands: **P1 = `/onboard`**, **P2 = `/directive`**, the gate alone = `/gate`, and the standing rhythm runs on `/inbox`, `/weekly`, `/month-end`, `/audit`, `/board-pack` — plus functional skills (`/campaign`, `/collect`, `/hire`, `/tender`, `/bia`, `/market-entry`). Full index: [skills/README.md](skills/README.md).

### Week 1 — Onboard & first directives
- Run the 🎤 Interviewer: group mode first, then your 2–3 most active companies
- Issue 3 real directives through the 🛎️ Router — pick ones you already know the answer to, so you can judge quality
- Let the 🚦 gate reject something. Watching the RETURN → fix → PASS loop work once builds more trust than any document

### Weeks 2–4 — Put the chiefs to work
- Each chief produces its first quarterly artifact: CFO cash view, CMO marketing plan, CRO pipeline review, COO ops cadence, CIO systems landscape map
- 🕵️ CAE drafts the audit committee charter and the first risk-based audit plan
- 🧯 BCM runs the first BIA on your most critical process

### Days 30–90 — Make it yours
- Fix what feels off: every agent is a Markdown file — edit it, and the change is permanent
- Retire what you don't use; the Router's "gap report" tells you what to build next
- Consider MCP connections (email, files, sheets) so agents act, not just draft — scope with the CIO/CISO agents first

### Standing rhythm
| Cadence | What | Who |
|---|---|---|
| Daily | Inbox triage, directives via Router | EA 📥, Router 🛎️ |
| Weekly | Pipeline review, ops review, cash position | CRO, COO, Treasury 💧 |
| Monthly | Close + consolidation, cost reviews, gate analytics | Controller 🧮, CIO, Gatekeeper 🚦 |
| Quarterly | Board pack, audit committee report, risk report, people report | Board Sec 🗳️, CAE 🕵️, ERM ⚠️, CHRO 👥 |
| Annually | Strategy refresh, audit plan, comp bands, BCM exercises | CSO 🛤️, CAE, CHRO, BCM 🧯 |

---

## 7 · Extending the system (the rules that keep it clean)

When you add an agent — or ask Claude to — the conventions that protected quality so far:

1. **One file per agent** in the right division folder, with `name / description / color / emoji (unique) / vibe` frontmatter and the nine standard sections
2. **Pass the checks**: `./scripts/lint-agents.sh <file>` (zero warnings) and `./scripts/check-agent-originality.sh <file>` (no re-skins — a new agent must be a genuinely new role)
3. **Give it one owner and explicit boundaries** — who it defers to, what it hands off, when it routes to licensed humans
4. **Wire it in**: add its name to `agents.txt`, a row to the pack README, and (if it changes the structure) the org chart
5. **The honesty rules are non-negotiable** — every new agent inherits the no-lies constitution and the gate

---

## 8 · What the system does NOT do

Stated plainly, because a blueprint that oversells is itself a gate failure:

- **Agents draft; you decide.** Nothing is sent, signed, filed, or paid by an agent. Every output is a prepared decision, not an action.
- **Not licensed advice.** Law, tax, insurance, audit opinions, and Sharia matters are prepared *for* licensed professionals, never replaced by the agents.
- **Knowledge has a date.** Regulations and prices move; the agents' discipline is to say "as of — verify current," and yours is to let them.
- **Untested = unproven.** True for BCM plans, backups, and this system itself: it becomes real the first week you run it against real work, not the day it was installed.

---

*Built on [The Agency](../../README.md) (MIT licensed). This pack: 158 agents + 9 chief seats + independent audit + the gate + 17 skills. Blueprint version 1.2 — update this document when the structure changes; it is the map, and the map must match the territory.*
