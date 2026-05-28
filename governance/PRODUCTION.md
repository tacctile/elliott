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

**How it works:** Labels feed through the laminator with one dimension in the feed direction (length) and the other across the laminator width. The across-width dimension must be ≤13.5". Multiple labels can feed end-to-end in a single continuous pass as long as they share the same orientation.

**Pass count rule:** The number of lamination passes equals the number of distinct label orientations in the print layout. Labels that share an orientation (same dimension feeding across the 13.5" width) laminate together in one pass regardless of quantity.

**Current items:**
- **3-label kits (1278930):** 3 labels feed end-to-end (11.13" each = 33.39" total feed length); 7.88" feeds across the 13.5" width — **1 pass.**
- **5-label kits (1245130):** Print layout requires mixed orientations to fit the Roland's 28" print width — 3 labels at 7.88" wide, 2 rotated to 11.13" wide. Two orientation groups = **2 passes.**
- **Single labels (1230820):** 12.44" feeds across 13.5" width (1.06" clearance) = **1 pass.**

**How to determine pass count for a new kit:**
1. Lay out all labels on the Roland SG3-300 (28" max print width).
2. Count how many distinct orientations are required to fit the layout.
3. Each orientation group that has its across-width dimension ≤13.5" = 1 lamination pass.
4. Sum the passes.

**Example — hypothetical 4-label kit at 11.13" × 7.88":** All 4 at 7.88" wide = 4 × 7.88" = 31.56" total feed length, 7.88" across the 13.5" width. Exceeds 28" print width, so print layout would split into two rows — but both rows share the same orientation. **1 lamination pass.** (If layout forced a mixed orientation, it would be 2 passes.)

**Future:** Wider laminator purchase planned after 18 months of locked-in orders. Target: ≥20" width. Cost: a few thousand dollars. This collapses multi-orientation items to single-pass and improves margins without touching customer pricing.

**Pricing rule:** The constraint is our problem. Absorb the extra labor during the trust-building phase. Never pass it to the buyer.

---

## Material Costs

### Cut Vinyl — 3M Controltac 180mC

| Color | Code | Roll Size | Cost/Roll | Cost/Yard | Cost/Sq Ft | Verified |
|-------|------|-----------|-----------|-----------|------------|----------|
| Cardinal Red | 53 | 24" × 50yd | $775.10 | $15.502 | $7.751 | 2026-05-28 |
| Olympic Blue | 57 | 24" × 10yd | $162.78 | $16.278 | $2.71 | 2026-05-22 |
| White | 10 | 24" × 10yd | $131.16 | $13.116 | $2.19 | 2026-05-21 |
| White | 10 | 48" × 10yd | $257.44 | $25.744 | $2.15 | 2026-05-21 |

### Application Tape

| Product | Roll Size | Cost/Roll | Cost/Sq Ft | Verified |
|---------|-----------|-----------|------------|----------|
| TransferRite Ultra 582U | 24" × 100yd | $118.21 | $0.5911 | 2026-05-28 |

**Process improvement note (2026-05-28):** TransferRite 582U roll width is now 24", matching the 3M 180mC vinyl roll width exactly. The previous 30" roll had 6" of overhang on 24" vinyl stock. The new 24" tape is cleaner — no overhang, no waste strip. No negative application implication.

### Printed Labels — Orajet 3951 + Polyester Lam

| Component | Cost | Notes | Verified |
|-----------|------|-------|----------|
| Orajet 3951 cast vinyl | ~$1.21/sq ft | White cast, adhesive back | 2026-04-22 |
| 1-mil polyester overlaminate | $1.6592/MSI = $0.2389/sq ft (Flexcon FLX000233, all-in incl. freight) | 13.5" max width on current laminator | 2026-05-28 |
| Eco-solvent ink (Roland TR2) | ~$0.25-0.30/label | At 11.13" × 7.88" size | 2026-04-22 |

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

> **Account-level rule:** Elliott supplies production-ready DWG files for every item. Step 1 (file import/setup) is a ~5-minute mechanical operation per design — NOT artwork prep, design time, or pre-press labor. Do NOT include file prep as a billable labor input in any cost build on this account. See `PRICING_RULES.md` §22.

### Cut Vinyl (Cut/Weed/Mask)

1. File import/setup — open the Elliott-supplied production-ready DWG, send to cutter. ~5 min mechanical. NOT billable labor.
2. Cut — Roland SG3-300 (or 54" plotter for 48" stock)
3. Weed — remove excess vinyl around cut characters
4. Mask — apply TransferRite 582U application tape
5. Inspect and package

### Printed + Laminated (Print/Lam/Cut)

1. File import/setup — open the Elliott-supplied production-ready DWG with registration marks already defined, send to RIP. ~5 min mechanical. NOT billable labor.
2. Print — Roland SG3-300, full-color eco-solvent on Orajet 3951
3. Laminate — apply 1-mil polyester overlaminate (13.5" max width)
4. Contour cut — Roland follows registration marks
5. Weed — remove excess material
6. Inspect — print quality, laminate adhesion, cut accuracy, color fidelity
7. Package — singles: stack. Kits: collate as matched set.

---

## Material Cost Quick Reference

### At 11.13" × 7.88" (standard capacity chart label)

- Vinyl: 0.609 sq ft × $1.21/sq ft = ~$0.74
- Laminate (1-mil polyester): amortized across the full lamination pass — not a per-label charge
- Ink: ~$0.27
- **Per-label material cost: ~$1.21** (canonical)
- **3-label kit (1278930): ~$2.99** (1 lamination pass — all 3 labels fit across 13.5")
- **5-label kit (1245130): ~$5.16** (2 lamination passes required)

> **Note:** A per-label laminate estimate of ~$0.15 (at $0.2389/sq ft × 0.609 sq ft) produces a component total of ~$1.16/label. This overstates the actual cost because the laminate roll covers the full 13.5" pass width — the cost is amortized across all labels in the pass, not charged per label. Always use the kit-level totals ($2.99 and $5.16) as canonical material costs. These derive from frontmatter `material_cost_per_unit` values, which are ground truth.

### At 15" × 12.44" (single load chart label)

- Vinyl: 1.296 sq ft × $1.21 = $1.57
- Laminate: ~$0.25
- Ink: ~$0.50
- **Total per label: ~$2.32–$3.23**

### Cut Vinyl at ~2.51–2.56 sq ft

- Cardinal Red, 24" roll: ~$7.23 vinyl + $1.51 tape = **~$8.74/label total** *(at 2.56 sq ft, P/N 1205720 — length-based method)*
- Olympic Blue, 24" roll: ~$7.43 vinyl + $1.49 tape = **~$8.92/label total** *(at 2.512 sq ft, P/N 3018378 — length-based method)*
- White, 24" roll: ~$8.00 vinyl + $1.51 tape = **~$9.51/label total** *(at 2.56 sq ft, P/N 3017435 — length-based method)*
- White, 48" roll: ~$6.28 vinyl + $1.51 tape = **~$7.79/label total** *(at 2.56 sq ft, P/N 3017435)*
