# Workflow Example: A Chairman's Directive, End to End

> A worked example of the [70 Business Specialists pack](../packs/70-business-specialists/BLUEPRINT.md)'s directive loop — the same flow the `/directive` skill runs in one command. Use it to understand the machinery or to run the loop manually.

**The directive (turn 1, from the chairman):**

> "Our Dubai retail company keeps getting 1-star reviews about delivery delays. Fix it."

---

## Step 1 — The Router diagnoses (Front Desk Router 🛎️)

The stated ask is "reviews." The Router's job is the *real* job:

```
🛎️ ROUTING: reviews complaint about delivery
REAL JOB: an operations problem wearing a reputation costume — reviews are
the symptom; delivery performance is the disease. Fix both, in that order.
➡ PRIMARY: Logistics & Last-Mile Strategist 🛵 (owns the outcome)
SUPPORTING: Reviews & Reputation Manager (symptom containment, runs parallel)
            BI & Data Analyst 📏 (evidence first: is it one courier? one zone?)
NOT NEEDED: more marketing. New customers into a broken funnel makes it worse.
```

One primary owner. Two clarifying questions maximum — here the Router asks only: *"Own drivers or courier company? And do you have delivery data exports?"*

## Step 2 — Context check

The agents read `group-context.md` (which entity, its rules) and `business-context-retailco.md` (voice, customers, channels). Missing facts get asked or tagged `[ASSUMED — verify]` — never invented.

## Step 3 — Specialists execute, in sequence

1. **BI & Data Analyst 📏** — takes the delivery export: *"78% of late deliveries trace to one courier's COD orders in two zones. The data can't tell us why — ask the courier for their failed-attempt logs."* (Data caveats stated, per its rules.)
2. **Logistics & Last-Mile Strategist 🛵** — builds the fix on that evidence: courier scorecard opened, 90-day decision rule set, delivery promise re-based on the actual 90th-percentile times, COD-to-prepaid conversion tactics for the two zones.
3. **Reviews & Reputation Manager** — in parallel: responses drafted for the existing 1-star reviews (written for the future reader, never revealing customer details), and a review-recovery sequence for affected customers — no fake reviews, no incentivized-positive-only schemes.

Each output feeds the next prompt. That's the whole handoff mechanism.

## Step 4 — The Gate (Revalidation Gatekeeper 🚦)

Five checks on the combined work. In this run:

```
🚦 VERDICT: RETURN — cycle 1 of 2
F1 [UNSOURCED] "Couriers average 92% success in Dubai" — no source. Cite or cut.
F2 [DIRECTIVE] The chairman asked to FIX it — the plan lacks a date when
   review scores should recover. Add the checkpoint.
```

The producing agents fix both; the re-gated version passes with a cover note stating what was verified and the one thing that couldn't be (the courier's internal failure reasons — pending their logs).

## Step 5 — Executive summary to the chairman

One page: the finding (one courier, two zones, COD), the fix (scorecard + promise re-base + zone tactics), the containment (review responses out), the checkpoint (review average back above 4.2 within 60 days or the courier is replaced per the scorecard rule), and the honest gap (courier logs pending). Bad news at full volume; decision requested: approve the possible courier switch cost.

## Step 6 — The chairman decides

Agents drafted everything. Nothing was sent, promised, or purchased until this moment.

---

**Run it yourself:** install the pack and skills per the [BLUEPRINT](../packs/70-business-specialists/BLUEPRINT.md), then type `/directive` and state the problem in plain words. The loop above is what executes.
