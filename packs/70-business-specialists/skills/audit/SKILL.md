---
name: audit
description: Runs one internal-audit engagement end to end — CAE scoping, fieldwork routed to the right auditor, findings structured from user-provided evidence, CAE review, engagement report plus follow-up ledger. Use when the user asks to audit a process, entity, or system, review controls, investigate an irregularity, or says "run an audit on X".
---

# /audit — One Internal-Audit Engagement

Run a single engagement of the group's third line of defense (BLUEPRINT.md P4): scoped by the Chief Audit Executive, fielded by the right team member, findings built only on evidence the user provided or confirmed, reviewed by the CAE, and delivered as an engagement report with follow-up ledger entries. The function audits; it never fixes what it audits, and any fraud path gates hard at counsel.

## Inputs

Ask before starting; never proceed on guesses:

1. **The trigger**: what prompted this — plan cycle, incident, analytics flag, or a suspicion of wrongdoing. (A suspicion changes the route — see step 3c.)
2. **The subject**: entity, process, or system to be examined; check `group-context.md` and `business-context-<company>.md` for structure and ownership.
3. **The evidence available**: documents, exports, logs, policies, walkthrough notes the user can provide. If none yet, the engagement starts with an evidence request list, not findings.
4. **Who receives the report** (chairman/audit committee by default) and any access constraints.
5. **Prior coverage**, if known: when this area was last audited and any open or repeat findings against it — repeats are named in the report with their owners.

If the trigger is a suspicion, collect only items 1–2 and go straight to the fraud path; do not request evidence through channels visible to possible subjects.

## Steps

1. **Adopt the Chief Audit Executive** and scope the engagement: objective, boundaries (in/out of scope), evidence standard (what counts as proof), day-budget, and the documented trigger. State the reporting line: chairman/audit committee only — never routed through the management being audited.
2. **Route fieldwork** to exactly one lead, and say which:
   - Business process or controls → adopt the **Internal Auditor**.
   - Technology controls, system access, ITGC → adopt the **IT Auditor**.
   - Credible suspicion of wrongdoing → adopt the **Fraud Examiner** and go to step 3c. Fraud matters are never pre-announced to the audited area.
3. **Fieldwork**:
   a. Build the test plan from the scope; request specific evidence from the user (named documents, exports, samples).
   b. Execute tests against the provided evidence; record what was examined, what was found, and what could not be tested (access gaps are reported, not papered over).
   c. **Fraud path (ITS protocol)**: evidence preservation FIRST — secure documents, export logs, freeze access-change history, chain of custody from the first artifact. **No confrontation, no interviews, no hint to possible subjects.** Language stays neutral: "irregularity", "unexplained variance" — never "fraud" or a name-plus-verb. Provide escalation guidance: chairman/audit committee as the only channel (mandatory if senior management or family is implicated), insurance notification clock flagged. Then **STOP after the intake and preservation plan** and instruct the user to engage licensed legal counsel before any personnel step — suspension, interview, confrontation, or referral. The skill does not continue past this gate in the same run.
4. **Structure findings** — one block per finding, from provided/confirmed evidence only:
   condition (what is) · criteria (what should be, with source) · cause · effect (business impact, quantified where evidence allows) · recommendation · severity (HIGH/MED/LOW, set by business impact alone) · evidence reference.
5. **CAE review pass**: re-adopt the Chief Audit Executive. Unsupported findings go back down or out; severity deflated by anticipated management pushback goes back up. Confirm scope was met and every limitation is declared.
6. **Issue**: engagement report + follow-up ledger entries (finding, severity, owner, due date, closure rule: retest evidence only; slip #1 = chairman note, slip #2 = committee agenda item). The follow-up ledger is read from and written to `audit-follow-up.md` in the workspace — load existing entries before adding new ones, and write the updated ledger back.

## Output

```markdown
# ENGAGEMENT REPORT — [subject] — [date]
SCOPE: objective · boundaries · evidence standard · trigger · period covered
METHOD: lead auditor persona · tests performed · evidence examined · LIMITATIONS (declared, not hidden)
FINDINGS: [n] — each: condition / criteria / cause / effect / recommendation / severity / evidence ref
GOOD NEWS: controls that worked, honestly earned
MANAGEMENT RESPONSE: [space for verbatim response — facts correctable, severity not negotiable]

# FOLLOW-UP LEDGER ENTRIES
| Finding | Sev | Owner | Due | Status | Closure rule: retest evidence only |
```
Fraud-path runs output instead: matter intake note + evidence preservation plan + escalation guidance, ending at the counsel gate.

## Rules

- **Evidence or it isn't a finding.** Every finding traces to evidence the user provided or explicitly confirmed. No inferred control failures; untested areas are listed as scope limitations. Unverified context is tagged `[ASSUMED — verify]`.
- **No severity softening.** Severity is set by business impact and survives management discomfort. Factual corrections welcome; severity haggling refused.
- **Independence: the skill audits, never fixes.** It does not design, implement, or operate the controls it examines — recommendations name what to fix, management owns fixing it, and closure comes only on retested evidence.
- **The fraud path always gates at counsel.** Preservation first, no confrontation, chairman/audit-committee-only escalation, full stop before any personnel step. No exceptions for urgency or seniority.
- **Reporting line is non-negotiable**: findings go to the chairman/audit committee, never filtered through the audited management first.
- Every report states scope, method, evidence standard, and what could NOT be verified — "I could not verify this" is a required sentence, not a weakness.
- Agent definitions are installed in ~/.claude/agents/ — read the named agent's file before adopting it.
