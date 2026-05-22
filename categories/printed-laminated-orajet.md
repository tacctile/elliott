# Category: Printed + Laminated (Orajet 3951 + Polyester)

> **Material Family:** Orajet 3951 Cast + 1-mil Polyester Overlaminate
> **Process:** Print / Laminate / Contour Cut / Weed / Inspect / Package
> **Equipment:** Roland SG3-300 (print + contour cut), 13.5" max width polyester laminator

---

## Items in This Category

### Single Labels

| P/N | Description | Dimensions | Sq Ft | Price (qty 20) | Per Label | Status |
|-----|-------------|------------|-------|-----------------|-----------|--------|
| 1230820 | Load Chart, D105 | 15" × 12.44" | 1.296 | $20 | $20.00 | FA Accepted |

### Multi-Label Kits

| P/N | Description | Labels | Dimensions (each) | Sq Ft/Kit | Price (qty 20) | Per Label | Lam Passes | Status |
|-----|-------------|--------|-------------------|-----------|-----------------|-----------|------------|--------|
| 1278930 | Capacity Chart Kit, E190 | 3 | 11.13" × 7.88" | 1.83 | $30 | $10.00 | 1 | FA Accepted |
| 1245130 | Capacity Chart Kit, E160 | 5 | 11.13" × 7.88" | 3.045 | $50 | $10.00 | 2 | Quoted |

---

## Pricing Profile (Rolling)

Derived from accepted pricing on real items. Tightens with every new item.

### Single Labels

**Data points:** 1 item (1230820 — 1.296 sq ft)

| Metric | Current Band | Notes |
|--------|-------------|-------|
| Material cost / sq ft | ~$3.09/sq ft | Fully loaded (vinyl + lam + ink + waste) |
| Selling price / sq ft at qty 20 | ~$15.43/sq ft | $20 / 1.296 sq ft |
| Margin at qty 20 | ~80% | On target with internal benchmark |
| Tier compression (1-9 → 200+) | 63% discount | $30 → $11 |
| Margin floor (200+) | ~64% | Lowest tier still healthy on single-pass |

**Band width:** Wide — 1 data point. Future items in 0.5–2.0 sq ft range should land within ±15% of the per-sq-ft rate.

### Multi-Label Kits (Same Dimensions, Same Material)

**Data points:** 2 items (1278930 — 3 labels, 1245130 — 5 labels)

| Metric | Current Band | Notes |
|--------|-------------|-------|
| Per-label material cost | ~$1.48/label | At the 11.13" × 7.88" size |
| Per-label selling price at qty 20 | $10.00/label | Parity across both kits |
| Kit margin at qty 20 | ~87-88% | Higher than singles — lower per-label material cost relative to price |
| Per-label price / sq ft at qty 20 | ~$16.42/sq ft | Higher than singles — intentional (see below) |
| Tier compression (1-9 → 200+) | 60% discount | $45→$18 (3-label), $75→$30 (5-label) |
| Margin floor (200+) | ~79% | Kit margins hold better at volume |

**Per-sq-ft kit premium:** ~$16.42 vs ~$15.43 for singles. This ~6% premium is intentional — matched-set collation, multi-label inspection, controlled-set packaging. Not a pricing error.

**Parity boundary:** Per-label parity ($10.00/label at qty 20) applies when:
- All labels same dimensions
- Same material system
- Kit requires ≤2 lamination passes

Beyond 2 lam passes or mixed dimensions → cost-build from scratch. Boundary is production passes, not label count.

---

## Pricing Rules for This Category

1. **Single labels** — validate against the singles per-sq-ft band.
2. **Same-dimension kits (≤2 lam passes)** — validate against the kit per-label band.
3. **Kits exceeding 2 lam passes** — cost-build from scratch. Run AI validation.
4. **Mixed-dimension kits** — see methodology below. Cost-build from scratch.
5. **The Pricing Profile is the primary validation tool, not the benchmark chain.**

---

## Decision Tree — New Single Label

1. Extract dimensions, calculate sq ft.
2. Pull this Pricing Profile (singles section).
3. Scale proportionally by sq ft against the $15.43/sq ft band.
4. Validate margins against ~80% target at qty 20.
5. If significantly different complexity (data density, color count, tolerance), adjust.

## Decision Tree — New Kit (Same Dimensions)

1. Count labels.
2. Verify all same dimensions. If not → mixed-dimension methodology.
3. Calculate lamination passes (narrow dimension vs 13.5" laminator).
4. If same dimensions and ≤2 lam passes → per-label parity ($10.00/label at qty 20).
5. If >2 lam passes → cost-build from scratch, run AI validation.
6. If mixed dimensions → cost-build from scratch.

---

## Mixed-Dimension Kit Methodology

For kits where labels are NOT all the same size.

1. **Decompose into size groups.** Each group gets its own material cost + production routing.
2. **Calculate material cost per group** from component costs.
3. **Calculate lamination passes per group.** Sum total passes.
4. **Calculate total kit material cost.** Sum all groups.
5. **Price bottom-up, not from a multiplier.** Apply target margin band (~80-88% at qty 20).
6. **Validate against Pricing Profile.** Per-sq-ft selling price should land in the general vicinity.
7. **Run AI model validation.** Minimum Rounds 1 + 2. All 4 rounds if annual spend is significant.
8. **Document clearly.** Future kits with similar structures should reference this approach.

**Do NOT:**
- Apply flat per-label parity across different label sizes
- Average label sizes and pretend the kit is uniform
- Anchor to the same-dimension kit multiplier chain
