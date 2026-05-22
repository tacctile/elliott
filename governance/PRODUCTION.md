# Production

> **Equipment specs, material costs, nesting rules, and process details.**
>
> Last Updated: 2026-05-22

---

## Equipment

| Equipment | Specs | Used For |
|-----------|-------|----------|
| Roland SG3-300 | 30" printer/cutter, 28" max cut width | Print + contour cut (printed items), cut only (vinyl lettering) |
| 54" plotter | 54" cut width | Cut vinyl on 48" roll stock |
| Polyester laminator | **13.5" max width** | Overlaminating printed items with 1-mil polyester |

### The 13.5" Laminator Constraint

The single most important production constraint on this account.

- Labels with a dimension ≤13.5" can feed through on that dimension.
- The number of labels fitting in one lamination pass depends on the label's narrow dimension vs 13.5".
- Current impact:
  - 3-label kits (7.88" per label): 3 × 7.88" = 23.64" — all 3 fit in ONE pass
  - 5-label kits (7.88" per label): cannot fit 5 across — requires TWO passes
- **Future:** Wider laminator purchase planned after 18 months of locked-in orders. Target: ≥20" width. Cost: a few thousand dollars. This collapses multi-pass items to single-pass and improves margins without touching customer pricing.
- **Pricing rule:** The constraint is our problem. Absorb the extra labor during the trust-building phase. Never pass it to the buyer.

---

## Material Costs

### Cut Vinyl — 3M Controltac 180mC

| Color | Code | Roll Size | Cost/Roll | Cost/Yard | Cost/Sq Ft |
|-------|------|-----------|-----------|-----------|------------|
| Cardinal Red | 53 | 24" × 10yd | ~$153.60 | $15.36 | $2.56 |
| White | 10 | 24" × 10yd | $131.16 | $13.116 | $2.19 |
| White | 10 | 48" × 10yd | $257.44 | $25.744 | $2.15 |

### Application Tape

| Product | Roll Size | Cost/Roll | Cost/Sq Ft |
|---------|-----------|-----------|------------|
| TransferRite Ultra 582U | 30" × 100yd | $135.06 | $0.18 |

### Printed Labels — Orajet 3951 + Polyester Lam

| Component | Cost | Notes |
|-----------|------|-------|
| Orajet 3951 cast vinyl | ~$1.21/sq ft | White cast, adhesive back |
| 1-mil polyester overlaminate | ~$1.41/MSI | 13.5" max width on current laminator |
| Eco-solvent ink (Roland TR2) | ~$0.25-0.30/label | At 11.13" × 7.88" size |

---

## Nesting Rules

### Cut Vinyl

- Labels nested by the HEIGHT dimension across the roll width.
- 24" roll: usable cut width is 24" (Roland max is 28", but vinyl is only 24" wide).
- 48" roll: goes on the 54" plotter, not the Roland.
- Calculate how many labels fit side-by-side across roll width, then determine linear footage per row.

### Printed + Laminated

- Print width up to 28" on the Roland SG3-300.
- Lamination width capped at 13.5".
- Contour cut follows registration marks from the print step.
- Number of lam passes = critical production variable for kit pricing.

---

## Process Steps by Category

### Cut Vinyl (Cut/Weed/Mask)

1. File prep — import DWG/PDF, set up cut file
2. Cut — Roland SG3-300 (or 54" plotter for 48" stock)
3. Weed — remove excess vinyl around cut characters
4. Mask — apply TransferRite 582U application tape
5. Inspect and package

### Printed + Laminated (Print/Lam/Cut)

1. File prep — import DWG/PDF, set up print file with registration marks
2. Print — Roland SG3-300, full-color eco-solvent on Orajet 3951
3. Laminate — apply 1-mil polyester overlaminate (13.5" max width)
4. Contour cut — Roland follows registration marks
5. Weed — remove excess material
6. Inspect — print quality, laminate adhesion, cut accuracy, color fidelity
7. Package — singles: stack. Kits: collate as matched set.

---

## Material Cost Quick Reference

### At 11.13" × 7.88" (standard capacity chart label)

- Vinyl: 0.609 sq ft × $1.21 = $0.74
- Laminate: ~$0.47
- Ink: ~$0.27
- **Total per label: ~$1.48**
- 3-label kit: ~$3.50-3.75
- 5-label kit: ~$5.80-6.25

### At 15" × 12.44" (single load chart label)

- Vinyl: 1.296 sq ft × $1.21 = $1.57
- Laminate: ~$1.02
- Ink: ~$0.50
- **Total per label: ~$3.09-4.00**

### Cut Vinyl at ~2.56 sq ft

- Vinyl (Cardinal Red, 24" roll): ~$7.01/label
- Vinyl (White, 24" roll): ~$8.46/label
- Vinyl (White, 48" roll): ~$6.74/label
- Application tape: $0.46/label
