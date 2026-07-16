# Pricing Pattern Discovery Audit
**Date:** 2026-07-15  
**Scope:** All 56 items in `items/`, all three `categories/*.md` files, `governance/PRICING_RULES.md`  
**Purpose:** Identify consistent, directional divergences between the engine's algorithmic starting point and independently validated locked prices — analogous to the sub-scope premium gradient (items 1247120, 3020477, 1279130, 1210810, 3024595, all landing above the ratio-scaled floor, following an inverse-size curve).  
**Format:** Findings report only. No changes to `calculator_config.json`, `scripts/build_calculator_config.py`, or the HTML engine.  
**Rule:** Patterns supported by fewer than 3 independently-validated items are flagged "insufficient sample" — no rule proposed.

---

## Summary Table

| # | Area | Verdict | Items | Direction | Magnitude |
|---|------|---------|-------|-----------|-----------|
| Q1 | Cut vinyl Band A small-format premium | **Insufficient sample** | 3010736, 3010722/23/24 | Upward from flat band rate | +3–5% at qty 20 |
| Q2 | Kit premium vs singles | **Holding — no drift** | 1245130, 1278890, 1278930 | N/A | +6.4% vs root floor, stable |
| Q3 | Convex/polycarbonate family | **Insufficient sample** | 3017557 only | N/A | N/A |
| Q4 | Singles band deep-tier underestimation | **Confirmed** | 1267140, 1278980, 3020335, 1277020 | Upward on 100-199 and 200+ | +$1.00–$1.75/label |
| Q5a | §31 floor breach at deep tiers — grandfathered | **Known, documented** | 1247120, 3020477, 1279130 | Below §31 floor at 200+ | Noted in PRICING_RULES.md |
| Q5b | Convex deep-tier ratios vs Orajet root | **Insufficient sample** | 3017557 only (consistent with size-dependent pattern but non-independent) | N/A | N/A |

---

## Q1 — Cut Vinyl (3M 180mC): Does Length-Based Tape Costing Produce Systematic AI-Validation Corrections?

### Finding: Insufficient Sample (2 independent validation events, not 3)

**Items:** 3010736 (1.012 sq ft, $14.33/sq ft at qty 20), 3010722/3010723/3010724 (1.167 sq ft, $14.36/sq ft at qty 20).

**Gap in one sentence:** The engine routes all Band A items (1.0–5.0 sq ft) to the concession-phase corridor of $13.65–$13.94/sq ft, but every independently-validated item below ~1.5 sq ft lands above that corridor, at $14.33–$14.36/sq ft, because AI validators consistently add a small-format premium that the flat band rate does not encode.

**Supporting evidence:**

- The concession-phase Band A corridor ($13.65–$13.94/sq ft) was established off items in the 2.51–3.20 sq ft range and is **not recalibrated by size within the band**.
- For 3010722 (1.167 sq ft): Wave 1 converged at $16.00–$16.25 (direct $/sq ft ratio-scale from the $13.67/sq ft cluster anchor). Wave 2 (5/6 High severity) found that holding this item flat against 2.5+ sq ft anchors "applied no size premium for the smaller format" — and corrected the qty-20 price **upward** to $16.75 ($14.36/sq ft). That correction is directional, not random.
- For 3010736 (1.012 sq ft): Wave 1 landed at $14.50–$15.00 anchored off 3010722. Wave 2 found a "premium stacked on a premium" risk and corrected **downward** to $14.50 ($14.33/sq ft), just below 3010722's rate. The final price is still above the band corridor.
- Together the two items form a confirmed, converging sub-band at $14.33–$14.36/sq ft — documented in the category profile as the "corrected price-size relationship" — but they represent only **2 independent wave-validated derivations** (3010722/23/24 share one validation process; 3010736 is a separate one).
- The tape cost correction (2026-06-09) was **documentation-only**: the area-method pseudo-rate that overstated tape ~2.7× was corrected to the length-based method, restating margins upward ~2 points, but **no sell prices changed**. The correction did not introduce this premium — it predates the premium's identification. The premium is a fixed-labor/size economics phenomenon, not a tape cost artifact.

**Why not proposing a rule:** With only 2 independent validation events supporting the premium, the threshold for encoding a sub-band rate is not met. The $14.33–$14.36/sq ft range is documented in the category profile as a reference for future items in the 1.0–1.5 sq ft range, and any new item in that range requires independent 4-wave validation rather than automatic inheritance. This is the correct posture until a third independent data point confirms the sub-band.

---

## Q2 — Kits vs Singles: Is the ~6% Kit Premium Holding or Drifting?

### Finding: Premium Holding — No Drift; Sample Too Homogeneous to Test Cross-Size Behavior

**Items:** 1245130 (5-label, $50/kit at qty 20), 1278890 (2-label, $20/kit at qty 20), 1278930 (2-label, $20/kit at qty 20, FA Accepted).

**Gap in one sentence:** The documented ~6% per-sq-ft premium is intact and stable at $10.00/label = $16.42/sq ft across all three validated kits, but all three use the same 0.609 sq ft label, so the premium has only ever been tested at one label size and would require a kit at a different label size to confirm that $10.00/label — rather than $16.42/sq ft — is the invariant.

**Supporting data:**

| P/N | Labels | Sq Ft/Kit | Kit p20 | Per-Label p20 | Per-Sq-Ft p20 | Premium vs root |
|-----|--------|-----------|---------|----------------|----------------|-----------------|
| 1278930 | 2 | 1.218 | $20.00 | $10.00 | $16.42 | +6.4% vs $15.43 |
| 1278890 | 2 | 1.218 | $20.00 | $10.00 | $16.42 | +6.4% vs $15.43 |
| 1245130 | 5 | 3.045 | $50.00 | $10.00 | $16.42 | +6.4% vs $15.43 |

The premium vs the root floor ($15.43/sq ft from 1230820) is exactly +6.4% for all three kits. The tier compression is uniformly 60% (1-9 to 200+) and the 200+ margin floor is uniformly ~80%. These ratios are parity-inherited by design, not independently validated per kit.

**Structural limitation:** The kit sample tests label-count variation (2, 2, and 5 labels per kit) while holding label size fixed at 0.609 sq ft. This means the sample confirms that the per-label parity rule works across label counts but **does not test whether $10.00/label would hold at a different label size**. An open question: if a future kit used 0.231 sq ft labels (a sub-scope-sized label), would the kit price be $10.00/label (sub-scope-ignoring) or would the sub-scope premium gradient apply to the per-label rate? The current data cannot answer this. No action required unless a cross-size kit is quoted.

---

## Q3 — Convex/Polycarbonate Family: Is a Pattern Emerging?

### Finding: Insufficient Sample

**Items:** 3017557 only (1.102 sq ft, Strategic Anchor).

No pattern is detectable from a single founding item. The category file documents the tier template derived from 3017557 (1.504× / 1.203× / 1.000× / 0.854× / 0.748× / 0.650×) and the material-proportional scaling methodology, but these are methodology commitments, not empirically confirmed patterns. The "deep-tier ratio vs size" phenomenon identified in Q4 (see below) is consistent with 3017557's 200+ ratio of 0.650 being higher than the Orajet root benchmark's 0.550 — the convex item at 1.102 sq ft having a higher 200+ ratio than 1230820 at 1.296 sq ft is the expected direction if deep-tier ratios are size-dependent — but a single data point cannot confirm this.

A minimum of 2–3 additional convex items at different areas would be needed before any pattern can be characterized.

---

## Q4 — Tier Ladder Shape: Consistent Deep-Tier Underestimation for Small Singles

### Finding: Confirmed — 4 Independent Validation Events, All Upward Correction

**Items:** 1267140 (0.560 sq ft), 1278980 (0.609 sq ft), 3020335 (0.625 sq ft), 1277020 (0.635 sq ft).  
**Gap in one sentence:** The engine ratio-scales the 100-199 and 200+ tier prices from the root benchmark (1230820 at 1.296 sq ft), producing deep-tier prices that are consistently $1.00–$1.75/label too low for singles in the 0.56–0.64 sq ft range, and AI validators have corrected every independently-validated item in this bracket upward by a uniform directional amount.

### Mechanism

The engine computes 100-199 and 200+ prices by ratio-scaling from 1230820:

```
100-199 calc = $14 × (item_sqft / 1.296)   [0.700× of root's qty-20]
200+    calc = $11 × (item_sqft / 1.296)   [0.550× of root's qty-20]
```

This gives the same ratio as the root benchmark at every item size. But the root benchmark at 1.296 sq ft has a steeper deep-tier discount curve than is appropriate for items at 0.56–0.64 sq ft, because larger items have more room to discount before hitting an effective per-sqft floor.

### Measured Gap (verified against category documentation)

| P/N | Sq Ft | Qty-20 | Calc 100-199 | Val 100-199 | Gap | Calc 200+ | Val 200+ | Gap | 100-199 ratio | 200+ ratio |
|-----|-------|--------|-------------|-------------|-----|-----------|----------|-----|---------------|------------|
| 1267140 | 0.560 | $8.75 | $6.00 | $7.25 | **+$1.25** | $4.75 | $6.50 | **+$1.75** | 0.829 | 0.743 |
| 1278980 | 0.609 | $9.50 | $6.50 | $7.50 | **+$1.00** | $5.25 | $6.75 | **+$1.50** | 0.789 | 0.711 |
| 3020335 | 0.625 | $9.75 | $6.75 | $7.75 | **+$1.00** | $5.25 | $7.00 | **+$1.75** | 0.795 | 0.718 |
| 1277020 | 0.635 | $10.00 | $6.75 | $8.00 | **+$1.25** | $5.50 | $7.25 | **+$1.75** | 0.800 | 0.725 |
| *(root)* | 1.296 | $20.00 | $14.00 | $14.00 | 0 | $11.00 | $11.00 | 0 | 0.700 | 0.550 |

*Calc values confirmed from category documentation: "original 200+ ($4.75 = $8.48/sq ft)" for 1267140; "calculator brief's $5.25 at 200+" for 3020335.*

### Wave-Level Evidence

All four validations triggered upward corrections specifically on the deep tiers:

- **1267140:** Wave 2/4 raised 100-199 and 200+ after finding the calculator's 200+ ($4.75 = $8.48/sq ft) "sat 45% below the band floor" — the implied per-sqft equivalent of the root benchmark per label.
- **1278980:** Wave 2 found "a 200+ floor below $6.50 inverts against 1267140's floor on $/sq ft" — corrected upward; Nick accepted $6.75.
- **3020335:** Wave 2 "corrected a size/price inversion against the 0.609 sq ft cluster (calculator brief's $5.25 at 200+) up to $7.00 to restore proportional interpolation between both flanking anchors."
- **1277020:** Category doc records "same band-protection pattern as 1267140" — implying Wave 2 raised deep tiers here as well. Final 200+ at $7.25 = 0.725× qty-20 vs the calculator's 0.550×.

The correction is consistently **upward**, the reason is consistently "inversion against a validated flanking anchor," and the result is consistently a 200+ ratio of **0.711–0.743** (avg ~0.72) vs the calculator's 0.550.

### Proposed Formula

**Do not encode yet** — per the split agreed at the start of this audit, engine changes go in a separate session. But the formula is:

```
For singles in the 0.56–0.65 sq ft bracket:
  100-199 tier: 0.80 × qty-20 price (vs current 0.700 root-ratio)
  200+ tier:    0.72 × qty-20 price (vs current 0.550 root-ratio)

Resulting corrections vs current calculator baseline (at representative qty-20 prices):
  At 0.56 sq ft ($8.75 p20):  100-199 →  $7.00 (was $6.00), 200+ → $6.25 (was $4.75)
  At 0.61 sq ft ($9.50 p20):  100-199 →  $7.50 (was $6.50), 200+ → $6.75 (was $5.25)
  At 0.63 sq ft ($10.00 p20): 100-199 →  $8.00 (was $6.75), 200+ → $7.25 (was $5.50)
```

*Snap to $0.25 increments per §30 after computing the ratio.*

**Boundary note:** The 0.503 sq ft position (1062390/1068270/1073950/1082570/1132950, all validated at $8.00/qty-20, $4.25/200+, ratio 0.531×) was validated earliest, before the 1267140-era "deep-tier band-protection" doctrine emerged. Its 200+ ratio of 0.531 is in the opposite direction from the 0.56–0.64 sqft bracket and likely reflects different validation dynamics at the sub-scope boundary. A fresh 4-wave validation of a new 0.503 sq ft item would test whether the same correction pattern applies, but the existing parity-clone items cannot confirm this.

---

## Q5 — Other Systematic Gaps: ≥3 Items, Same Directional Correction

### Q5a — §31 Floor Breach at Deep Tiers for Small Sub-Scope Items (Known/Grandfathered)

**Items:** 1247120 (0.122 sq ft), 3020477 (0.130 sq ft), 1279130 (0.148 sq ft).

This pattern is **already identified and documented in `governance/PRICING_RULES.md` §31**, which explicitly names the grandfathered tiers. Including it here for completeness.

**Gap in one sentence:** Three sub-scope items in the 0.12–0.15 sq ft range have their 200+ tier prices, converted to $/sq ft, falling below the §31 root floor of $15.43/sq ft because the per-label floor pricing structure at this size class naturally descends below the $/sq ft floor at high volume.

| P/N | Sq Ft | p200 | p200/sqft | §31 floor equivalent | Shortfall | Grandfathered tiers |
|-----|-------|------|-----------|----------------------|-----------|---------------------|
| 1247120 | 0.122 | $1.75 | $14.34 | $1.88 | –$0.13 | 200+ |
| 3020477 | 0.130 | $1.75 | $13.46 | $2.01 | –$0.26 | 100-199, 200+ |
| 1279130 | 0.148 | $2.00 | $13.51 | $2.28 | –$0.28 | 200+ |

These items were validated before the §31 doctrine was codified (2026-07-01) and are explicitly listed in §31's grandfathered exception table. The §31 rule instructs that these tiers "should be brought into §31 compliance the next time that item is independently revised for any other reason — not proactively."

**Engine gap (no rule to propose now):** The engine currently has no guard that prevents per-label-floor pricing from breaching the §31 $/sq ft floor at deep tiers. The corrective formula when revision triggers: `min_tier_price = ceil(15.43 × sqft_per_label / 0.25) × 0.25`. Not proposing an engine rule in this session per the findings-only scope; this is flagged for the revision cycle that next touches any of these three items.

### Q5b — No Other New Pattern Meeting the ≥3-Item Threshold

The following were examined and either below threshold or already documented:

**Cut vinyl Band A concession vs AI consensus gap (all 11 Band A items):** Every Band A item sits at the concession-phase rate ($13.65–$13.94/sq ft) while AI validators recommend $14.84–$16.41/sq ft. This is a systematic, documented policy decision (Relationship Concession, January 2027 normalization planned) — not an undiscovered correction. Flagging as pre-existing and intentional.

**Cut vinyl 3010701 deep-tier compression (1 item):** 3010701 at 3.202 sq ft (Cardinal Red) has a 200+ ratio of 0.886 — far higher than other Band A items (~0.629–0.650). This reflects the high Cardinal Red material cost ($12.78/label) creating a natural floor at deep tiers, preventing the same steep discount curve. Single item; insufficient sample.

**Micro-Format tier template fidelity (2 items):** 1279000 and 1278220 (both 0.097 sq ft) match the Micro-Format tier template (1.50× / 1.167× / 1.000× / 0.867× / 0.767× / 0.700×) exactly. Per-label floor items (3024592, 3024140, 1012080, 1205870) diverge from the template at deep tiers because the absolute floor price overrides the ratio — by design, not a gap.

**1101250 sub-scope gradient deviation (1 item):** 1101250 (0.132 sq ft) at $2.25/label at qty 20 = $17.05/sq ft breaks the monotonic sub-scope gradient; its size-adjacent neighbors 1247120 (0.122 sq ft, $22.54/sq ft) and 3020477 (0.130 sq ft, $21.15/sq ft) price substantially higher. This is a deliberately validated outcome documented in the category file and item file, tied to the specific governing benchmark constraint (1210810 excluded from the benchmark set). Non-precedent-setting, 1 item.

**Cut vinyl Band C tier compression (3 founding items at identical size/price):** 3010707/3010708/3010709 all 0.969 sq ft, $20/qty 20, 200+ = $11.50 (0.575× ratio). This is the founding three-item cluster with identical pricing; the ratio reflects a deliberate design choice (59% tier compression anchored to the worst-case Cardinal Red), not an algorithmic correction pattern.

---

## Audit Notes

1. **Q4 is the only new actionable finding.** The singles band 100-199 and 200+ deep-tier underestimation is systematic, direction-consistent across 4 independent validations, quantifiable, and encodable. Magnitude: +$1.00–$1.75/label for the 0.56–0.64 sq ft bracket; ratios 0.80 and 0.72 vs the engine's current 0.700 and 0.550 from the root benchmark.

2. **Q1 (cut vinyl small-format premium) is the strongest near-miss.** Two independent validations with clear directional consistency is one short of the rule-proposal threshold. If a third item in the 1.0–1.5 sq ft range is independently validated and lands above the concession corridor, this pattern should be revisited immediately.

3. **Q2 (kit premium) is structurally under-tested.** The three kits all use the same 0.609 sq ft label. The premium is holding, but the sample doesn't test whether $10.00/label or $16.42/sq ft is the invariant across label sizes. The first kit with a materially different label size will be the acid test.

4. **Q3 (convex) and Q5b (no new ≥3-item patterns) have no action.** Convex needs more items. No undiscovered patterns survive the 3-item threshold outside Q4.

5. **The §31 grandfathered breaches (Q5a) are known and self-documenting.** Three items (1247120, 3020477, 1279130) are on the §31 grandfathered list. The engine needs a deep-tier floor guard added when these items are next revised — the formula is `ceil(15.43 × sqft / 0.25) × 0.25` per tier.
