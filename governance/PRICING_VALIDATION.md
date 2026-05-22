# Pricing Validation Process — Multi-Round AI Model Methodology

> **For high-stakes pricing decisions. Non-negotiable on qualifying items.**
>
> Last Updated: 2026-05-22

---

## When to Use This Process

- New item type without a direct pricing comparison in the catalog
- Kit pricing where production touches scale nonlinearly
- Any item where annual quote total could exceed $1,000+
- Any time gut instinct says something feels off
- When the pricing decision sets a precedent future items will be measured against

**When NOT to use it:** Items dimensionally and materially identical to something already quoted. Match the existing structure and move on. Note: this exempts multi-round AI validation only — Rule 15 (validate against category Pricing Profile band) still applies to every new item regardless.

---

## The Process

6 top-tier AI models per round, run independently in parallel. Model selection may change as new models release. Pick the 6 strongest reasoning models available at the time.

---

## Round 1 — Build Round (6 models)

**Purpose:** Establish baseline pricing from scratch.

**Include in the prompt:**
- Full item specs (dimensions, material, process, label count)
- Material cost breakdown
- Production process step by step, including equipment constraints
- Accepted benchmark item(s) with full pricing tiers
- Key comparisons (sq ft, production touches, material cost ratio)

**Required Output Schema:**

```
1. Interpreted Specs — what you understood. Call out anything ambiguous.
2. Benchmark Match — which existing item you're anchoring to and why.
3. Cost Drivers — what's driving the price.
4. Proposed Tiers — all 6 quantity breaks with prices.
5. Per-Label Math — if kit, show per-label cost at qty 20.
6. Margin Estimate — at qty 20 and 200+.
7. Risk Flags — anything uncomfortable about this price.
8. Kill Criteria — what would make you reject this price entirely.
```

---

## Round 2 — Destruction Round (6 models, fresh chat)

**Purpose:** Attack the proposed pricing from every hostile angle.

**Include:** Proposed pricing from Round 1, benchmark, full production details.

**Attack vectors:**

- **Buyer/Procurement:** Per-label math comparison, per-sq-ft normalization, volume discount curve analysis.
- **Competitor:** What a better-equipped shop would quote. Which tier is most vulnerable.
- **Cost Auditor:** Bottom-up cost decomposition. Does the multiplier hold across tiers. Fixed vs variable analysis.
- **Strategic:** Anchor visibility, reverse-engineering exposure, precedent risk.

**Required Output Schema:**

```
1. Buyer/Procurement Attack — severity: [L/M/H]
2. Competitor Attack — severity: [L/M/H]
3. Cost Auditor Attack — severity: [L/M/H]
4. Strategic Attack — severity: [L/M/H]
5. Weakest Tier — which and why.
6. Strongest Tier — which and why.
7. Verdict — survives? Yes / Yes with modifications / No.
8. Recommended Modifications — specific (tier + number + reasoning).
```

---

## Round 3 — Buyer Simulation Round (6 models, fresh chat)

**Purpose:** Simulate how the actual buyer reacts.

**Include:** Instruct model to role-play as buyer (experienced industrial procurement, ~$140K label spend). Give proposed pricing AND accepted benchmark pricing side by side. Context: vendor has been flawless, buyer transitioning from weak incumbent. Do NOT tell them what to think.

**Required Output Schema:**

```
1. Immediate Reaction — approve, question, or push back?
2. Per-Label Math — did you do it? What conclusion?
3. Vendor Track Record Impact — benefit of the doubt? How much?
4. Pushback Threshold — at what price point would you push back?
5. Instant Approval Number — what price is a rubber stamp?
6. Competitor Comparison — thinking about old supplier's price?
7. PO Decision — sending PO as-is, or questions first?
8. Email Suggestion — what one line in the quote email makes you approve faster?
9. Mental Model Building — building a pricing pattern? Will you push back eventually?
```

---

## Round 4 — Final Synthesis (6 models, same chat as Round 2 or 3 if possible)

**Purpose:** Validate or destroy the final decision.

**Include:** Final pricing, the rejected alternative, full reasoning, summary of previous rounds.

**Required Output Schema:**

```
1. Verdict — right call? Yes or No.
2. Tier-Level Check — any specific tiers wrong?
3. Long-Term Precedent — holds for 20 items, or creates a problem?
4. Discomfort Check — anything uncomfortable about sending today?
5. Decision Forks — interpretation choices that could have gone differently.
6. Final Answer — send as shown? Yes or No. If No, what changes?
```

---

## Key Findings (Apply to All Future Items)

These emerged across 55+ model runs on the first 5 items:

1. Buyers always do per-label math on kits. Any premium needs a ready explanation.
2. The "instant approval" threshold exists. Always aim for it. The gap is usually $2-6/unit.
3. Equipment limitations are your cost to absorb, not the buyer's to pay.
4. A one-line anchor in the quote email prevents 80% of buyer questions.
5. Flat multipliers are simple but vulnerable to audit. Be aware.
6. Never volunteer multiplier math. Use process language.
7. The benchmark chain is both the strength and the vulnerability.
8. Procurement builds mental models over time. Be the one who brings the framework conversation first.
9. Speed is the moat. Good quote today beats perfect quote next week.
