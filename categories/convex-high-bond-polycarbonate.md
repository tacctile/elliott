# Category: Convex High Bond + Polycarbonate Overlaminate

> **Material Family:** Convex High Bond + Poly Lam
> **Process:** Print / Laminate (Rollsroller) / Contour Cut / Weed / Inspect / Package
> **Equipment:** Roland SG3-300 (print + contour cut), Rollsroller flat laminating table
>
> Category File: `categories/convex-high-bond-polycarbonate.md`

---

## Material System

Two approved combinations for Elliott panel decals:

### Combination A — 5-mil Polycarbonate Overlaminate

| Component | Product | Cost/Sq Ft | Roll Specs |
|-----------|---------|------------|------------|
| Base (print media) | Convex 6-mil High Bond | $1.5976 | 30" × 150 ft = 375 sq ft, $599.13/roll |
| Overlaminate | 5-mil Polycarbonate Overlaminate | $0.9600 | 51" × 150 ft = 637.5 sq ft, $612.00/roll |
| Ink (§25 full bleed) | Eco-solvent, full coverage | $0.50 | Account standard |
| **Combined rate (before buffer)** | | **$3.0576/sq ft** | |

> **Base + laminate only — excludes ink.** Per §25 pattern, ink cost ($0.50/sq ft × full label sq ft) is added separately when calculating `material_cost_per_unit` for any item in this family.
>
> Supplier status: provisional — Convex (base) and TBD (5-mil lam). Both may be replaced.

### Combination B — 10-mil Polycarbonate Overlaminate (Kapco)

| Component | Product | Cost/Sq Ft | Roll Specs |
|-----------|---------|------------|------------|
| Base (print media) | Convex 6-mil High Bond | $1.5976 | 30" × 150 ft = 375 sq ft, $599.13/roll |
| Overlaminate | Kapco 10-mil PSA Velvet Polycarbonate (KJ10VPC/38/150) | $1.4105 | 38" × 150 ft = 475 sq ft, $670.00/roll |
| Ink (§25 full bleed) | Eco-solvent, full coverage | $0.50 | Account standard |
| **Combined rate (before buffer)** | | **$3.5081/sq ft** | |

> **Base + laminate only — excludes ink.** Per §25 pattern, ink cost ($0.50/sq ft × full label sq ft) is added separately when calculating `material_cost_per_unit` for any item in this family.
>
> Supplier: Kapco — in stock; single-roll buying only at this time.

### Comparison to Orajet/Polyester Lam

The Orajet/polyester lam combined rate is ~$1.9489/sq ft (§25 canonical). Convex Combination A is ~$3.0576/sq ft (+57% vs Orajet/lam; base + lam only, excludes ink — ink added separately per §25). Combination B is ~$3.5081/sq ft (+80% vs Orajet/lam; base + lam only, excludes ink — ink added separately per §25). The Convex/PC $/sq ft band ($24.27–$27.90/sq ft at qty 20) is proportionally higher than the Orajet/lam singles band ($15.43–$15.91/sq ft at qty 20), scaled by the material cost ratio.

### Governing Rules

- **§25** — Full bleed / full coverage ink ($0.50/sq ft × full label sq ft) applies to all Convex printed/laminated items.
- **§29** — Applies specifically to Orajet 3951 + polyester lam items only. ANSI status for Convex panel decals must be evaluated per item. The first item (3017557) is NOT ANSI — it is a control panel overlay.
- **§30** — $0.25 increment rule applies to all tier prices on new items.
- **No ink coverage surcharge on base material cost** — ink is calculated separately at $0.50/sq ft per §25; do not add ink markup to the $1.5976/sq ft base cost.
- **Material cost formula for Convex items (laminate area = label area, governed by 30" base):**
  - Combination A: `(label sq ft × $1.5976) + (label sq ft × $0.9600) + (label sq ft × $0.50) + incidental buffer`
  - Combination B: `(label sq ft × $1.5976) + (label sq ft × $1.4105) + (label sq ft × $0.50) + incidental buffer`

---

## Process Notes

### Lamination Equipment

Lamination equipment: Rollsroller flat laminating table (accommodates up to 4' × 8' sheets — no width or orientation constraint on any Elliott panel decal). The 13.5" narrow-web polyester laminator is NOT used for this material family. Lamination pass count: always 1, regardless of label dimensions.

- 5-mil polycarbonate lam roll is 51" wide — more than sufficient for 30" base material.
- 10-mil Kapco polycarbonate lam roll is 38" wide — 8" clearance over 30" base.

### Print

- Roland SG3-300 (30" print bed, 28" max cut width) — base material width (30") matches Roland print bed exactly.
- Full-color eco-solvent on Convex 6-mil High Bond substrate.
- File prep: $0 per account rule §22 — Elliott supplies production-ready DWG files for all items.

---

## Pricing Profile

Derived from accepted pricing on real items. Founded by P/N 3017557 (Session AD, 2026-06-30).

### Pricing Derivation Methodology — Material-Proportional Scaling

The Convex/PC family pricing is derived by **material-proportional scaling** from the Orajet printed/laminated singles band. The methodology:

1. Interpolate the Orajet singles band $/sq ft at the item's area (band range: $15.43–$15.91/sq ft at qty 20)
2. Calculate the material cost ratio: `(Convex + PC combined $/sq ft) ÷ (Orajet + polyester combined $/sq ft)`
   - Combination A: $3.0576 ÷ $1.9489 = **1.569×**
   - Combination B: $3.5081 ÷ $1.9489 = **1.800×**
3. Multiply: interpolated Orajet $/sq ft × material cost ratio = Convex/PC $/sq ft
4. Apply to the item area, snap to $0.25 increments (§30), build tiers using standard account ratios

This methodology maintains the same margin profile (~87% at qty 20) as the Orajet band while passing through the higher material cost proportionally. The Orajet band ($15.43–$15.91/sq ft) does NOT apply directly to this family — the Convex/PC band is a scaled derivative.

### Band Data

**Founding data point:** P/N 3017557 at 1.102 sq ft (17.75" × 8.9375"). Two variants:

| Metric | Variant B (10-mil PC, primary) | Variant A (5-mil PC) |
|--------|-------------------------------|---------------------|
| Material cost ratio vs Orajet/lam | 1.800× | 1.569× |
| $/sq ft at qty 20 | **$27.90/sq ft** | **$24.27/sq ft** |
| Price at qty 20 | $30.75 | $26.75 |
| Material cost/unit | $4.00 | $3.50 |
| Margin at qty 20 | 87.0% | 86.9% |
| Margin floor (200+) | 80.0% | 80.0% |
| Tier compression (1-9 → 200+) | 56.8% | 56.5% |

**Band scope:** Applies to all Convex High Bond + Polycarbonate panel decals. Single founding data point at 1.102 sq ft. Band will tighten as additional items are quoted. Future items at significantly different areas should validate the proportional scaling against the founding data point.

**Tier ratios (template, derived from the 3017557 Variant B table):**
- 1-9: 1.504× anchor
- 10-19: 1.203× anchor
- 20-49: 1.00× anchor
- 50-99: 0.854× anchor
- 100-199: 0.748× anchor
- 200+: 0.650× anchor

**Override note:** Strategic Anchor — 3017557 establishes the founding $/sq ft band for the entire Convex/polycarbonate material family. All future items in this family scale from this data point.

**External market context (for internal reference only — do NOT use for pricing):** External market research (3 rounds × 6 models) confirmed that the market band for vinyl-base + polycarbonate-overlaminate overlays at qty 10–25 is $40–$70/sq ft. The Variant B price ($27.90/sq ft) sits ~30% below the market floor — consistent with the ~25–30% relationship concession on the Orajet band. External models priced against the rigid polycarbonate industrial nameplate/overlay market (the wrong reference class); P/N 3017557 is a printed vinyl label with a polycarbonate overlaminate.

---

## Items

| P/N | Description | Dimensions | Sq Ft | Price (qty 20, Var B) | Price (qty 20, Var A) | Per Label | Status |
|-----|-------------|------------|-------|-----------------------|-----------------------|-----------|--------|
| 3017557 | LBL-BASKET CONTROL BOX SINGLE AXIS | 17.75" × 8.9375" | 1.102 | $30.75 | $26.75 | $30.75 (Var B) | Quoted |

---

## Pricing Rules for This Category

1. **Material-proportional scaling** is the governing methodology — interpolate the Orajet band at the item's area, multiply by the material cost ratio for the chosen laminate combination.
2. **Do NOT apply the Orajet singles band ($15.43–$15.91/sq ft) directly.** The Convex/PC band is a scaled derivative.
3. **Both laminate variants should be quoted** when Sean's preferred laminate is unknown. Variant B (10-mil Kapco) is the default if only one variant is quoted.
4. **§30** — All tier prices in $0.25 increments.
5. **§26** — Invoice protection at all tier boundaries.
6. **§25** — Full bleed ink at $0.50/sq ft applies to all items in this family.
7. **ANSI status** — Evaluated per item. §29 (ANSI account rule) does NOT extend to this family.

---

## Decision Tree — New Convex/PC Panel Decal

1. Extract dimensions, calculate sq ft.
2. Pull this Pricing Profile — check the founding data point (3017557 at 1.102 sq ft).
3. Determine which laminate combination applies (A, B, or both).
4. Calculate material cost ratio: Convex+PC combined $/sq ft ÷ Orajet+polyester $1.9489/sq ft.
5. Interpolate the Orajet singles band at the item's area (~$15.43–$15.91/sq ft at qty 20).
6. Scale: Orajet $/sq ft × material cost ratio = target Convex/PC $/sq ft.
7. Multiply by item area, snap to $0.25 increments (§30), build tiers.
8. Validate margins against ~87% target at qty 20.
9. If significantly different complexity or area vs the founding data point, run AI validation.

---

## Notes

- Combination B (10-mil Kapco velvet) is in stock and ready to source. Combination A (5-mil) supplier is unconfirmed.
- Supplier status provisional on base material and 5-mil lam — replacement suppliers may be evaluated before first production run. Do not lock material sourcing until confirmed with Nick.
- The Orajet printed/laminated singles band ($15.43–$15.91/sq ft at qty 20) does NOT apply to this category. The Convex/PC band is derived by scaling the Orajet band by the material cost ratio.
- The 13.5" polyester laminator is NOT used for this family — Rollsroller flat laminating table handles all Convex/PC items.
- Item count: 1 (P/N 3017557 — founding data point, Session AD, 2026-06-30).
