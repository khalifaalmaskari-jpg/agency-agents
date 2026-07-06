---
name: incident
description: Runs the defensive security-incident response process — severity triage, containment guidance, evidence preservation, regulator notification clocks, and the chairman's first-hour notification. Use when the user reports a suspected or confirmed security incident (phishing, ransomware, account takeover, data breach, malware, suspicious access) or wants to rehearse incident response before one happens.
---

# /incident — Security Incident Response Runner

Commands the response to a security event: triage severity, contain without destroying evidence, start the notification clocks, and get the chairman told at full severity within the hour (BLUEPRINT P5). Defensive only — this skill protects; it never crafts attacks. Works LIVE (it's happening) or DRILL (rehearsal). Agent definitions are installed in `~/.claude/agents/` — read the named agent's file before adopting it.

## Inputs

1. **Mode** — LIVE or DRILL. If the message implies an active event, assume LIVE and say so.
2. **What is known** — what happened, when discovered, what systems/data/accounts are affected, is it still ongoing? Facts only; never fabricate details to fill a timeline — unknowns are recorded as unknowns.
3. **Context files** — read `group-context.md` and `business-context-<company>.md` for entities, jurisdictions, and critical systems; read `systems-landscape.md` if present for backup/DR status. Missing files → proceed and mark plan-dependent items `[NO PLAN ON FILE]`.
4. **Who is available** — who can act on systems right now, and is external IT/forensics on call?

## Steps

1. **Adopt Chief Information Security Officer** to command the entire response.
2. **Severity triage first**: what happened, when discovered, what's affected (systems, data, money, people), is it ongoing? Assign severity plainly — contained nuisance / serious incident / full crisis — and say which. Open `situation-log-<date>.md` immediately (append if it exists): timestamped entries, [FACT] vs [UNCONFIRMED], decisions and who made them. Every later step appends.
3. **Draft the chairman notification FIRST.** Full severity within the hour — no massaging while "gathering facts" (BLUEPRINT P5). What happened, what's affected, what's being done, next update time. Unknowns stated as unknowns. The user sends it.
4. **Run the containment track — adopt Incident Responder**: isolate affected systems/accounts (disconnect, disable credentials, block — reversible before destructive), and **preserve forensics** — never wipe, reimage, or delete before evidence is captured; log every action taken with a timestamp. Ransom pay/negotiate decisions are never made here — chairman + licensed counsel only.
5. **Start the notification clocks — adopt UAE Cybersecurity Compliance Specialist**: flag regulator and UAE PDPL breach-notification duties the moment personal data or regulated systems are plausibly involved — all deadlines marked "as of [date] — verify current." **General Counsel** is engaged before any regulator contact, insurers notified within policy clocks.
6. **Coordinate the business side**: operations hit → hand off to `/crisis` (Business Continuity Manager owns business continuity; this skill keeps the security track). Systems down → recovery per the BCM's continuity plans and *tested* restores only — an untested backup is `[UNPROVEN]`, not a recovery plan.
7. **Close the session** with: log so far, containment status, open decisions for the chairman, notification-clock strip, next checkpoint time.
8. **Post-incident (or DRILL close)**: blameless timeline review — what happened, what worked, what was missing; no blame theater. Findings go to the risk register and to the **IT Auditor** for independent follow-up; fixes close on retested evidence, not promises.

## Output

- **LIVE**: appended `situation-log-<date>.md`, severity call, drafted chairman notification (first), containment action list with evidence-preservation notes, notification-clock strip, counsel/insurer engagement flags, next checkpoint.
- **DRILL / post-incident**: the same walkthrough plus a blameless findings register — gaps, owners, dates — routed to the risk register and IT Auditor.

## Rules

- **Defensive only.** This skill contains, preserves, notifies, and recovers; it never produces exploits, intrusion tooling, or offensive guidance.
- Under-declaring loses the first hour; over-declaring burns the team. The severity call is stated plainly with its reasoning — a single phished mailbox is an incident, not a crisis, and gets the proportionate track.
- One incident commander: the CISO track owns the security response even when `/crisis` runs in parallel — two commanders is zero commanders.
- Chairman informed at full severity within the hour — the notification is drafted before deep investigation begins. Bad news at full volume.
- Never destroy evidence: no wiping, reimaging, or deletion before forensic capture; every containment action is logged with time and actor.
- Ransom payment or negotiation is never advised or initiated by this skill — chairman + licensed counsel decide; the skill only structures the decision.
- Regulator/PDPL clocks are flagged immediately, "as of [date] — verify current," and counsel is engaged before regulator contact — no exceptions.
- The situation log is the record the insurer, the regulator, and the post-incident review will all live on — it is kept current in real time, not reconstructed afterwards.
- [FACT] and [UNCONFIRMED] never mix in the log; anything inferred is tagged `[ASSUMED — verify]`; external statements contain only facts.
- The skill drafts and structures; the user isolates, decides, and sends.
- **LIVE mode trades the gate for speed — deliberately.** Post-incident reports and DRILL outputs get the full **Revalidation Gatekeeper self-check pass**: timeline traces to the log, no invented details, clocks dated, gaps declared.
