# ⚡ The Skills Layer

The agents are *who*; skills are *how*. Each skill is a one-command workflow that orchestrates the right agents in the right order — so the processes in the [BLUEPRINT](../BLUEPRINT.md) run without you re-explaining them every time.

## Install (once)

Skills are directories containing a `SKILL.md`. Copy them where Claude Code looks for skills:

```bash
# Personal — available in every project on this machine:
mkdir -p ~/.claude/skills
cp -r packs/70-business-specialists/skills/*/ ~/.claude/skills/

# OR project-level — available in one workspace (and shareable via git):
mkdir -p /your/workspace/.claude/skills
cp -r packs/70-business-specialists/skills/*/ /your/workspace/.claude/skills/
```

(This README isn't a skill and is skipped automatically — only directories with a `SKILL.md` register.)

Then in any Claude Code session, type `/` to see them, or just describe the job — Claude invokes the matching skill by its trigger conditions.

## The 22 skills

### Core system — the machine itself
| Skill | What it runs |
|---|---|
| **`/directive`** | The flagship: your goal in plain words → Router plans it → specialists execute → 🚦 gate checks → executive summary. The whole loop, one command |
| **`/gate`** | The Gatekeeper's five-check audit on ANY document — including ones written outside the system |
| **`/onboard`** | The Interviewer end-to-end: group mode → per-company → context files written |
| **`/board-pack`** | Quarterly board pack in the Board Secretary's skeleton, gated, with `[DATA NEEDED]` discipline |

### Cadence — the standing rhythm
| Skill | Cadence |
|---|---|
| **`/inbox`** | Daily — EA triage: four buckets, drafts written, commitments ledger, buried ledes first |
| **`/weekly`** | Weekly — pipeline + ops + cash in one Monday one-pager: 3 numbers, 3 risks, 3 decisions |
| **`/month-end`** | Monthly — the close companion: checklist, intercompany reconciliation, consolidation, close summary |
| **`/audit`** | Per engagement — CAE scoping → fieldwork → findings → follow-up ledger (fraud path gates at counsel) |

### Functional — high-frequency jobs
| Skill | What it delivers |
|---|---|
| **`/campaign`** | Brief → copy variants (EN/Arabic transcreation) → media plan → measurement plan |
| **`/collect`** | AR aging list → prioritized dunning sequences (email + WhatsApp) → decision list |
| **`/hire`** | Role check against the plan → job post → interview kit → offer checklist (UAE cost flags) |
| **`/tender`** | Tender doc → compliance matrix → bid/no-bid scorecard → response skeleton → deadline back-plan |
| **`/bia`** | Guided business impact analysis → MTPD/RTO/RPO for sign-off → gaps and single points of failure |
| **`/market-entry`** | Market brief + competitor snapshot → recommendation with kill criteria → first-90-days checklist |

### Governance & resilience
| Skill | What it delivers |
|---|---|
| **`/crisis`** | Live crisis activation or drill: first-hour card, situation log, comms sequencing, specialist tracks |
| **`/legal-prep`** | Prepare-for-your-lawyer pack: jurisdiction triage, facts chronology, documents, questions, counsel brief |
| **`/risk-review`** | Quarterly ERM cycle: register update, cross-entity concentration sweep, board risk report |

### Departments & resilience
| Skill | What it delivers |
|---|---|
| **`/it-landscape`** | CIO systems landscape review |
| **`/incident`** | Security incident response runbook |
| **`/payroll`** | UAE/GCC monthly payroll run |
| **`/reputation`** | Reviews + WhatsApp response handling |
| **`/succession`** | Family succession & bus-plan session |

## Workspace files

Skills persist state in canonical files in the workspace — they check for these before asking you to paste, and write updates back:

- `business-context*.md` and `group-context.md` — written by `/onboard`, read by everything
- `commitments-ledger.md` — `/inbox`
- `risk-register.md` — `/risk-review`
- `audit-follow-up.md` — `/audit`
- `situation-log-<date>.md` — `/crisis` (append-only)

Agent definitions are installed in ~/.claude/agents/ — skills read the named agent's file before adopting it.

## The rules every skill obeys

1. **Context first** — skills read `group-context.md` / `business-context-*.md`; if missing, they say so and tag everything `[ASSUMED — verify]`
2. **No invented facts** — numbers come from you or are marked `[DATA NEEDED]`; laws carry "as of — verify current"; capability claims in bids are marked `[NEEDS EVIDENCE]`
3. **The gate applies** — substantive outputs end with a Gatekeeper self-check; failures are fixed or declared, never polished over
4. **Skills draft; you decide** — nothing is sent, signed, filed, or paid by a skill

## Extending

Copy any skill's structure (`frontmatter → Inputs → Steps → Output → Rules`), name the exact agents each step adopts, keep the no-lies rules, and drop the new directory beside these. If the same `/directive` sequence keeps recurring, that's the signal to freeze it into a skill.
