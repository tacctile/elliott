# Validation Prompts — 4-Wave AI Pricing Validation System

> **Authoritative source for how every new item on the Elliott Equipment account is stress-tested before Nick sends a quote to Sean.**
>
> Companion to `governance/PRICING_VALIDATION.md` (methodology) and `governance/CALCULATOR.md` (Round 0 brief generation). This document governs Waves 1–4 — the prompt structure, attack angles, output schemas, and behavioral rules for Claude Chat during a validation session.
>
> Last Updated: 2026-06-01

---

## 1. System Overview

The 4-wave validation system is the working surface between the calculator's Round 0 brief and a quote that goes to Sean. Every printed/laminated, cut vinyl, kit, or one-off item is pressure-tested across 6 top-tier AI models, four times — 24 independent passes — before a single number is committed to a quote email.

### Purpose

To find every weakness in a proposed price before Sean does. Sean is an Employee-Owner at Elliott Equipment who normalizes everything (per-label, per-sq-ft, volume curve), builds a long-term mental model of Pro Label's pricing, and turns every quote into a permanent reference point. The 4-wave system exists so that what reaches him has already survived 24 model passes built specifically to surface buyer pushback, competitor exposure, cost-math softness, and account-level precedent risk.

### Philosophy

- **The calculator generates the Round 0 brief — a starting point, not a price.**
- **Nick is the sole decision-maker.** Claude Chat is the synthesis partner. The 24 model responses are the evidence.
- **Claude Chat does not editorialize between waves.** It generates one prompt at a time. It waits.
- **No wave softens.** Each wave's attack angle is fixed and cannot be relaxed because the result is uncomfortable.
- **Every wave's output is incorporated into the next wave's prompt.** Nothing surfaced is discarded.

### Operating Model

```
┌─────────────────────────────────────────────────────────────────────┐
│  Calculator (frontend/index.html) — generates Round 0 brief         │
│  Output: validation brief (plain text, "Ready for Round 1: YES")    │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ Nick copies the brief
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Claude Chat (fresh session, full repo loaded minus items/frontend) │
│  Generates Wave 1 prompt per Section 3 below                        │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ Nick runs Wave 1 across 6 models in ChatHub
                           │ Nick pastes 6 responses back into Claude Chat
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Claude Chat generates Wave 2 prompt per Section 4                  │
│  Incorporates Wave 1 consensus + findings                           │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ Nick runs Wave 2, pastes 6 responses
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Claude Chat generates Wave 3 prompt per Section 5                  │
│  Incorporates Wave 2 attack severities + recommended modifications  │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ Nick runs Wave 3, pastes 6 responses
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Claude Chat generates Wave 4 prompt per Section 6                  │
│  Incorporates Wave 3 buyer simulation + pushback thresholds         │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ Nick runs Wave 4, pastes 6 responses
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Claude Chat produces the Final Synthesis Table (Section 7)         │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ Claude Chat waits.
                           ▼
                  Nick and Claude Chat discuss
                  Nick locks the final price
                           │
                           ▼
            Claude Code writes the item file per
            governance/STRUCTURE_RULES.md and
            .claude/COMPLETION_TEMPLATES.md
```

### The 24 Model Responses Are the Research Department

6 models × 4 waves = 24 independent passes against the item. Each model brings independent context, independent reasoning, and independent pricing instincts. Their job is to surface evidence — data, comparison points, pricing opinions, attack vectors. They are not the decision-makers.

**Nick is the sole decision-maker. Claude Chat is the synthesis partner. The 24 responses are the evidence.**

---

## 2. Pre-Wave Requirements

The following must be true before Wave 1 starts. Claude Chat verifies all items against the calculator brief before generating the Wave 1 prompt. If any item is unresolved, Claude Chat surfaces it and waits for Nick to resolve it.

1. **Calculator brief is complete.** "Ready for Round 1: YES" badge present on the brief. If NO, the brief is structurally incomplete — fix the source data before proceeding.
2. **No STOP flags unresolved.** F1 (material stale >365 days), F3 (>13.5" laminator narrow dim), F4 (margin below 50%), F17 (no profile band for material family), F20 (kit cannot fit ≤2 lam-pass orientation groups) must all be cleared.
3. **Spec extraction is complete.** All 14 mandatory fields per `governance/SPEC_EXTRACTION.md` populated. No Blocked fields.
4. **Material costs are verified and not stale.** Every material consumed by the item has a `verified_date` within 180 days. >180 days triggers F2 REVIEW; >365 days triggers F1 STOP. Reverify before proceeding.
5. **Ink coverage is confirmed or flagged.** If a placeholder is used (e.g., $0.25 Safety Red flood coat per 1210810), F12 must fire and the placeholder must be documented in the brief. Realistic range disclosed.
6. **Order quantity is known or standard volume tiers are being quoted.** Either Sean's requested qty is recorded, or the item is being quoted on the standard 6-tier ladder.
7. **First article status is confirmed.** Sean's request for an FA (or absence of one) is recorded.
8. **All open items are documented.** Color conflicts, unverified inputs, sub-scope flags, Rule 14 deviations, alternate-roll efficiency scenarios, PMS caveats — every flag from the calculator must appear in the brief.

---

## 3. Wave 1 — Build Round

**Purpose:** Establish independent baseline pricing from scratch. Each model commits to a number before seeing any anchor produced by the calculator.

**Attack angle:** Constructive. Each model is a senior pricing expert building a defensible quote for a premium industrial label supplier with an established account relationship.

**Critical rule:** Do NOT show the calculator's recommended price in the Wave 1 prompt. Models anchor independently. The calculator output is withheld until Wave 2.

### Account Context to Embed in Every Wave 1 Prompt

- **Supplier:** Pro Label-Decal Banner Company, Omaha NE. In business since 1990.
- **Customer:** Elliott Equipment Company (subsidiary of Stellar Industries), Omaha NE, ~8 miles away.
- **Buyer contact:** Sean Finn — Buyer / Data Specialist, Employee-Owner.
- **Annual label/decal spend:** ~$140,000.
- **Status:** Actively displacing incumbent (Pro Sign & Screen Printing). Pro Label has been flawless — fast turnaround, technical partnership, zero errors. Sean has brought Pro Label into R&D decisions. An engineering/procurement standard project is being developed with Pro Label's input.
- **Relationship phase:** Trust-building approaching technical partnership. Concession-phase pricing is deliberate and strategic — not a reflection of market rate.
- **Material:** Orajet 3951 cast vinyl + 1-mil polyester overlaminate (printed/laminated items) or 3M Controltac 180mC cut vinyl (cut vinyl items), as applicable.
- **File prep:** Elliott provides production-ready DWG files for every item on this account. File prep cost is always $0. Never a cost driver. (`governance/PRICING_RULES.md` §22–24.)
- **Equipment constraint:** 13.5" max laminator width. Never expose this to the buyer — frame as process language only.

### Benchmark Anchor to Embed — Printed / Laminated

P/N **1230820** — Load Chart Label D105, 15" × 12.44" (1.296 sq ft), Orajet 3951 cast vinyl + 1-mil polyester overlaminate. **ROOT BENCHMARK. FA Accepted. $20/ea at qty 20 ($15.43/sq ft).**

Full tier table:

| Tier | Price |
|------|-------|
| 1-9 | $30 |
| 10-19 | $24 |
| 20-49 | $20 |
| 50-99 | $17 |
| 100-199 | $14 |
| 200+ | $11 |

For kits, also include:

- P/N **1278930** — 3-Label Lifting Capacity Chart Kit, E190. Same-dim, 11.13" × 7.88" per label (1.827 sq ft/kit). $30/kit at qty 20 ($10.00/label). FA Accepted.
- P/N **1245130** — 5-Label Lifting Capacity Chart Kit, E160. Same-dim, 11.13" × 7.88" per label (3.045 sq ft/kit). $50/kit at qty 20 ($10.00/label). Quoted.

### Benchmark Anchor to Embed — Cut Vinyl

P/N **1205720** — E190 Cardinal Red Model Designation. 33-9/16" × 11" (2.56 sq ft). 3M Controltac 180mC cut vinyl. **CUT VINYL BASELINE. FA Accepted. $35/ea at qty 20 ($13.67/sq ft).** Priced as Relationship Concession (AI consensus was $38–$42 — Rule 14 deviation).

### Current Pricing Bands to Embed

| Band | Range at qty 20 | Notes |
|------|------------------|-------|
| Printed/laminated singles | $15.43–$15.91/sq ft | Concession phase. Anchor: 1230820 at $15.43. Band narrowing. |
| Printed/laminated kits | $10.00/label, ~$16.42/sq ft | Same-dim parity. Kit premium ~6% over singles — intentional. |
| Cut vinyl (concession phase) | $13.65–$13.94/sq ft | Active band. All 4 current cut vinyl items inside. |
| Cut vinyl (AI consensus, normalized) | $14.84–$16.41/sq ft | Would-be normalized band. Normalization planned January 2027. |

**Account-level order rules (printed/laminated only):**

- **MOQ 10** on all printed/laminated catalog items.
- **1-9 tier = $55.00 flat minimum order charge** — NOT a per-unit rate. Flat total.
- **Invoice protection:** buyer never invoiced more for a smaller quantity than a larger quantity at the next tier. Required quote language is non-negotiable.
- **Cut vinyl exception:** MOQ 10 and $55 minimum order charge do NOT apply to 3M 180mC cut vinyl items at this time.

**$55 account floor:** Minimum-worthwhile-charge on any one-off, sub-MOQ, or tiny job. Anchored to 1230820 FA price.

### Required Output Schema (Enforce This Exactly)

Each Wave 1 prompt instructs each model to produce, in order:

1. **Interpreted Specs** — restate what you understood. Flag any ambiguity.
2. **Benchmark Match** — which existing item you are anchoring to and why.
3. **Cost Drivers** — what is driving the price on this specific item.
4. **Proposed Tier Table** — all 6 quantity breaks with prices AND $/sq ft AND margin % at each tier.
5. **Per-Label Math** — if kit, show per-label cost and per-label price at qty 20.
6. **Margin Estimate** — at qty 20 and 200+. Show the math.
7. **Risk Flags** — anything that makes you uncomfortable about this price.
8. **Kill Criteria** — what specific condition would make you reject this price entirely.

---

## 4. Wave 2 — Destruction Round

**Purpose:** Attack the proposed pricing from every hostile angle at maximum intensity. Find every weakness before Sean does. The goal is not to be fair — it is to find the breaking point.

**Attack angle:** Hostile. Each model takes on one or more adversarial roles simultaneously. No softening. No hedging. Every attack vector is rated High, Medium, or Low severity with a specific finding behind the rating.

### What to Include in the Wave 2 Prompt

- Full item spec (same as Wave 1).
- The **Wave 1 consensus price** (synthesized by Claude Chat from the 6 Wave 1 responses — central tendency + spread).
- The full benchmark anchor with tier tables (printed/laminated and/or cut vinyl as appropriate).
- The account context (Section 3).
- All four attack vectors below — every model must address all four.
- Every open item from the brief (ink unverified, color conflict, sub-scope flag, Rule 14 deviation, etc.). Models must engage with them — not skip past.

### Four Mandatory Attack Vectors

**Buyer / Procurement Attack.**
Sean Finn has done the per-label math. He has normalized it to $/sq ft. He has compared it to what the incumbent charged. He is an Employee-Owner who watches margins. He is building a mental model of Pro Label's pricing structure that will govern every future RFQ. Where does this price create a renegotiation trigger? What specific number or tier makes him pick up the phone?

**Competitor Attack.**
A better-equipped competitor — regional printer with a wider laminator, faster Roland, lower overhead — is quoting against Pro Label on this item. What do they quote? Which tier is most exposed? At what volume does Pro Label lose the bid? Be specific about the number.

**Cost Auditor Attack.**
Decompose the price from the bottom up. Material cost verified or assumed? Ink cost verified or placeholder? Lamination pass count correct? Fixed vs variable cost split — does the margin hold at 200+? Where is the math soft and where is it solid?

**Strategic Attack.**
This item becomes a data point in the account's pricing structure. Every future item will be compared against it. Does this price invert the price-size relationship? Does it create a renegotiation anchor for existing items? Does it expose the concession-phase band to normalization pressure earlier than planned? What is the precedent risk to the full $140K account?

### Required Output Schema (Enforce This Exactly)

1. **Buyer/Procurement Attack** — severity: [H/M/L] — specific finding
2. **Competitor Attack** — severity: [H/M/L] — specific competitor price at the most exposed tier
3. **Cost Auditor Attack** — severity: [H/M/L] — specific soft math identified
4. **Strategic Attack** — severity: [H/M/L] — specific precedent risk identified
5. **Weakest Tier** — which tier and exactly why
6. **Strongest Tier** — which tier and exactly why
7. **Verdict** — Yes (send as shown) / Yes with modifications / No
8. **Recommended Modifications** — if not Yes: specific tier + specific number + one-sentence reasoning

---

## 5. Wave 3 — Buyer Simulation

**Purpose:** Put Sean Finn in the room. Simulate his exact reaction — not a generic procurement buyer, but this specific person with this specific relationship context and this specific account history.

**Attack angle:** Realistic but pressured. Sean is smart, he does the math, and he is building a mental model. He is not hostile but he is not a pushover. He has options — the incumbent still exists.

### Sean Finn Profile to Embed in Every Wave 3 Prompt

- **Employee-Owner at Elliott Equipment.** Has personal financial stake in procurement decisions.
- **Buyer / Data Specialist.** He normalizes everything: per-label, per-sq-ft, volume curve. He has done this math.
- **Pattern recognition.** Has been receiving Pro Label quotes for months. He has a pricing pattern in his head.
- **Pro Label has been flawless.** Fast. Technical. No errors. He values this — but he is not giving away margin because of it.
- **Deepening partnership.** He has brought Nick into R&D questions — the relationship is moving toward technical partnership.
- **Standards leverage.** He is working with his manager to develop an engineering/procurement standard for labels — Pro Label is being consulted. This is leverage, but it is also a reason to be fair.
- **Approval threshold.** Real. He can approve under a certain number without escalation. Above it, he asks questions or escalates.
- **Incumbent memory.** He will compare this to the incumbent's pricing. The incumbent was weaker on quality and speed, but the price exists in his memory.
- **Long-term mental model.** Every quote is a data point. Price too high once and it anchors his expectations upward. Price too low and it anchors a floor he will defend forever.

### What to Include in the Wave 3 Prompt

- Full item spec.
- The proposed tier table (refined after Wave 2).
- The benchmark anchor tier tables side by side.
- Sean's profile (above) verbatim.
- The account relationship context (Section 3).
- The quote language stub from the calculator: anchor line + MOQ language (printed/laminated) or Rule 14 note (cut vinyl) + PMS caveat where applicable.

### Required Output Schema (Enforce This Exactly)

1. **Immediate Reaction** — approve, question, or push back? Be specific.
2. **Per-Label Math** — did Sean do it? What number did he land on? What did he conclude?
3. **Vendor Track Record Impact** — how much benefit of the doubt does Pro Label get? Is it enough?
4. **Pushback Threshold** — at what specific price point does Sean pick up the phone or send a question email?
5. **Instant Approval Number** — what price is a rubber stamp, no questions asked?
6. **Incumbent Comparison** — is Sean thinking about the old supplier's price? What was it (estimate if unknown)?
7. **PO Decision** — sending PO as-is, or does he ask a question first?
8. **Quote Email Anchor Line** — what single line in the quote email makes Sean approve faster?
9. **Mental Model Risk** — is Sean building a pricing pattern from this? Will he use this number against Pro Label in 6 months?

---

## 6. Wave 4 — Final Synthesis

**Purpose:** Validate or destroy the price that survived Waves 1–3. This is the final checkpoint before the quote goes to Sean. Binary verdicts only. No hedging.

**Attack angle:** Decisive. Models have seen everything — the build, the destruction, the buyer simulation. Now they render a final judgment. Send or don't send. If they want to modify, they name the exact tier and exact number. Vague recommendations are not acceptable.

### What to Include in the Wave 4 Prompt

- Full item spec.
- The **final proposed tier table** after Wave 2 and Wave 3 refinements.
- A summary of **Wave 1 consensus** (what the build round landed on).
- A summary of **Wave 2 key findings** (what the destruction round flagged — severity H items must be addressed).
- A summary of **Wave 3 key findings** (Sean's simulated reaction, pushback threshold, instant-approval number).
- The benchmark anchor.
- All open items still unresolved (ink unverified, color conflict, sub-scope flag, Rule 14 deviation, etc.).
- The full account context.

### Required Output Schema (Enforce This Exactly)

1. **Verdict** — Send as shown: YES or NO. No maybe.
2. **Tier-Level Check** — go through all 6 tiers. Any specific tier wrong? Name it and the correct number.
3. **Long-Term Precedent** — does this price hold for 20 items over 2 years, or does it create a structural problem?
4. **Discomfort Check** — is there anything about sending this today that makes you uncomfortable? Be specific.
5. **Decision Forks** — what interpretation choices in this pricing could have gone differently, and which fork is better?
6. **Final Answer** — send as shown, or: exact tier + exact number + one sentence why.

---

## 7. Final Synthesis Table

After Nick pastes all 6 Wave 4 responses, Claude Chat produces this table.

| Model | Wave 1 Anchor | Wave 2 Verdict | Wave 3 Sean Reaction | Wave 4 Final | Key Arguments For | Key Arguments Against | Recommended Price |
|-------|---------------|----------------|----------------------|--------------|-------------------|-----------------------|-------------------|
| M1 | | | | | | | |
| M2 | | | | | | | |
| M3 | | | | | | | |
| M4 | | | | | | | |
| M5 | | | | | | | |
| M6 | | | | | | | |

Below the table, Claude Chat writes the **Consensus Summary:**

- Where all 6 models agreed.
- Where they diverged and why.
- Highest-severity unresolved risks.
- Price range the evidence supports.
- Structural risks to the account if this price is sent as-is.
- Nick's decision range with reasoning.

**Then Claude Chat waits. Nick drives the discussion from here.**

---

## 8. Behavioral Rules for Claude Chat During a Validation Session

1. **Generate one wave prompt at a time.** Wait for Nick to paste 6 responses before generating the next wave.
2. **Do not editorialize, recommend, or comment between waves.** Generate the prompt and wait.
3. **Do not reveal the calculator's recommended price in Wave 1.** Models anchor independently.
4. **Incorporate Wave N findings into Wave N+1 prompt.** Each wave builds on the last.
5. **Never soften the attack in Waves 2, 3, or 4.** The purpose is to find weakness before Sean does.
6. **Flag every open item in every wave prompt.** Ink unverified, color conflict, sub-scope, Rule 14 deviation — models must engage with them.
7. **Never use file prep as a cost driver.** Elliott provides production-ready DWG. Cost is always $0. (`governance/PRICING_RULES.md` §22–24.)
8. **Never expose the 13.5" laminator constraint by name.** Use process language only.
9. **Never expose multiplier math in buyer-facing framing.** Use process language. (`governance/PRICING_RULES.md` §5–7.)
10. **Never benchmark against `do_not_benchmark` items:** 1277970, 1277980, 1277990, 1278000 (outrigger program peers); 3017583, 3017584 (standalone tiny one-offs); 1210810 (sub-scope single — until production-volume acceptance); 1082570 (initial-order job-economics price). The calculator filters these out; the validation prompts must do the same.
11. **After Wave 4 and the synthesis table, wait for Nick.** He is the sole decision-maker.

---

## 9. Integration with Existing Governance

- The calculator (`governance/CALCULATOR.md`) produces the Round 0 brief. This document governs Waves 1–4.
- Pricing rules (`governance/PRICING_RULES.md`) apply at all times. No wave prompt may instruct a model to violate them.
- The band (`categories/cut-vinyl-3m-180mc.md`, `categories/printed-laminated-orajet.md`) is the validation fence. Any model recommendation outside the band must be flagged and documented.
- After Nick locks the price, Claude Code writes the item file per `governance/STRUCTURE_RULES.md` and `.claude/COMPLETION_TEMPLATES.md`.
- The 4-wave validation record is permanently documented in the item file Pricing Derivation section.
- Every override (if Nick deviates from the wave consensus) is classified per `.claude/ARCHITECTURE.md` Override Types and logged — Relationship Concession, Competitive Defense, Strategic Anchor, Capacity Fill, Owner Judgment, or One-Time Exception.
