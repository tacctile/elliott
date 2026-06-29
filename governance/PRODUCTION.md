# Production

> **Equipment specs, material costs, nesting rules, and process details.**
>
> Last Updated: 2026-06-29 (Session AC — Convex High Bond + Polycarbonate Overlaminate material costs added: 3 new materials with roll specs and $/sq ft. Previously 2026-06-09 Session I — singles costing normalized to §25 canonical: 1230820 quick-reference entry now $2.60; small-format cut vinyl quick reference tape figures corrected from the area pseudo-rate to the length-based method (audit D3) — documentation-only, no sell prices changed. Previously Session H: kit-family §25 normalization — 1278930 $2.99 → $3.60, 1245130 $5.16 → $5.95)

---

## Equipment

| Equipment | Specs | Used For |
|-----------|-------|----------|
| Roland SG3-300 | 30" printer/cutter, 28" max cut width | Print + contour cut (printed items), cut only (vinyl lettering) |
| 54" plotter | 54" cut width | Cut vinyl on 48" roll stock |
| Polyester laminator | **13.5" max width** | Overlaminating printed items with 1-mil polyester |
| Rollsroller flat laminating table | Sheet lamination, up to 4' × 8' | Convex High Bond + polycarbonate laminate family. Documentation only — no pass count or width calculations apply. |

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
| Cardinal Red | 53 | **15" × 50yd** | **$433.77** | **$8.6754** | **$2.3134** | **2026-06-05** |
| Black | 12 | **24" × 50yd** | **$659.26** | **$13.1852** | **$6.5926** | **2026-06-05** |
| Olympic Blue | 57 | 24" × 10yd | $162.78 | $16.278 | $2.71 | 2026-05-22 |
| White | 10 | 24" × 10yd | $131.16 | $13.116 | $2.19 | 2026-05-21 |
| White | 10 | **24" × 50yd** | **$619.21** | **$12.3842** | **$6.1921** | **2026-06-05** |
| White | 10 | 48" × 10yd | $257.44 | $25.744 | $2.15 | 2026-05-21 |

**Roll selection note (2026-06-05):** The 15" Cardinal Red roll is used for large-format cut vinyl items where label height fits within 15" roll width with single-across nesting (used by P/N 3010704 at 14.375" label height, 0.625" clearance). The 24" Cardinal Red roll continues to be used for the 2.51–2.56 sq ft small-format cluster where 2-across nesting is optimal.

**Roll selection note (2026-06-05) — Band C sub-1 sq ft program:** The new 24" × 50yd Black ($659.26) and 24" × 50yd White ($619.21) production-volume rolls are used by the Band C sub-1 sq ft cut vinyl program (P/N 3010708 Black, P/N 3010709 White). Band C items at 4" label height nest 5-up on the 24" roll (5 × 4" = 20" across 24" roll, 4" clearance). P/N 3010707 (Cardinal Red Band C variant) uses the existing 24" × 50yd Cardinal Red roll. The existing 24" × 10yd White roll continues to serve P/N 3017435 (Band A small-format) for its smaller production runs.

**Note on Black/White 50yd cost_per_sq_ft derivation:** Cost_per_sq_ft on the new Black and 50yd White materials is derived as `cost_per_linear_yd / roll_width_ft` (Black: $13.1852 / 2 ft = $6.5926/sq ft; White 50yd: $12.3842 / 2 ft = $6.1921/sq ft), consistent with the Cardinal Red 24"×50yd derivation method. This is the length-based method used by all 50yd 24"-roll cut vinyl on this account. Item pricing uses cost_per_linear_yd directly via the length-based nesting calculation.

### Application Tape

| Product | Roll Size | Cost/Roll | Cost/Yard | Cost/Sq Ft | Verified |
|---------|-----------|-----------|-----------|------------|----------|
| TransferRite Ultra 582U | 24" × 100yd | $118.21 | $1.1821 | $0.5911 | 2026-05-28 |
| TransferRite Ultra 582U | **30" × 100yd** | **$141.86** | **$1.4186** | **$0.1891** | **2026-06-05** |

**Process improvement note (2026-05-28):** TransferRite 582U roll width is now 24" (for the small-format cluster), matching the 3M 180mC vinyl roll width exactly. The previous 30" roll had 6" of overhang on 24" vinyl stock. The 24" tape is cleaner — no overhang, no waste strip. No negative application implication.

**Roll selection note (2026-06-05):** The 30" TransferRite 582U roll is used for large-format cut vinyl items where 2-up tape nesting is required to amortize the tape feed across two labels (used by P/N 3010704: 2 × 14.375" = 28.75" across 30" tape, 1.25" waste strip). The 24" roll continues to be used for the 2.51–2.56 sq ft small-format cluster where 1 label per tape row matches the vinyl row layout.

### Printed Labels — Orajet 3951 + Polyester Lam

| Component | Cost | Notes | Verified |
|-----------|------|-------|----------|
| Orajet 3951 cast vinyl | ~$1.21/sq ft | White cast, adhesive back | 2026-04-22 |
| 1-mil polyester overlaminate | $1.6592/MSI = $0.2389/sq ft (Flexcon FLX000233, all-in incl. freight) | 13.5" max width on current laminator | 2026-05-28 |
| Eco-solvent ink — **full bleed / full coverage (standard)** | **$0.50/sq ft × full label sq ft** | Account standard — every Elliott printed/laminated item priced at full coverage. No partial/medium/low coverage assumptions. | 2026-06-01 |

#### Account-Wide Ink Coverage Standard (Established 2026-06-01)

All printed/laminated items on this account are priced assuming **full bleed / full coverage ink at all times**. There is no medium, low, or partial coverage routing for any Elliott printed/laminated item — past, present, or future. The standard ink rate is **$0.50/sq ft applied to the full label sq ft**.

**Canonical material cost formula for any Elliott printed/laminated item:**

```
(Orajet 3951 sq ft × $1.21) + (laminate sq ft × $0.2389) + (label sq ft × $0.50) + incidental buffer
```

**Incidental buffer convention:** The calculated material total is rounded **conservatively upward** to account for setup scrap, registration pulls, and minor production waste. The buffer is judgment-applied, not a fixed number. The frontmatter `material_cost_per_unit` field on every printed/laminated item reflects the buffered total, not the pure calculation.

**Worked example (P/N 1210810 at 0.292 sq ft):**

| Component | Calculation | Cost |
|-----------|-------------|------|
| Orajet 3951 cast vinyl | 0.292 × $1.21 | $0.353 |
| 1-mil polyester overlaminate | 0.292 × $0.2389 | $0.070 |
| Eco-solvent ink (full bleed) | 0.292 × $0.50 | $0.146 |
| Calculated total | | **$0.569** |
| Incidental buffer (conservative round-up) | | + $0.031 |
| **Canonical `material_cost_per_unit`** | | **$0.60** |

This is the canonical method on this account. See `PRICING_RULES.md` §25 and `MASTER_CONTEXT.md` Core Rules.

---

### Printed Decals — Convex High Bond + Polycarbonate Overlaminate

| Component | Product | Roll Size | Cost/Roll | Cost/Sq Ft | Notes | Verified |
|-----------|---------|-----------|-----------|------------|-------|----------|
| Base (print media) | Convex 6-mil High Bond | 30" × 150 ft = 375 sq ft | $599.13 | $1.5976 | Supplier provisional — Convex, Elliott account only | 2026-06-29 |
| Overlaminate (Combination A) | 5-mil Polycarbonate Overlaminate | 51" × 150 ft = 637.5 sq ft | $612.00 | $0.9600 | Usable width 30" (governed by base); supplier provisional | 2026-06-29 |
| Overlaminate (Combination B) | Kapco 10-mil PSA Velvet Polycarbonate (KJ10VPC/38/150) | 38" × 150 ft = 475 sq ft | $670.00 | $1.4105 | In stock at Kapco; single-roll buying only | 2026-06-29 |

**Combined rates (base + lam + §25 ink $0.50/sq ft, before incidental buffer):**
- Combination A (5-mil): $1.5976 + $0.9600 + $0.50 = **$3.0576/sq ft**
- Combination B (10-mil Kapco): $1.5976 + $1.4105 + $0.50 = **$3.5081/sq ft**

> Supplier status provisional on Convex base and 5-mil lam — replacement suppliers may be evaluated before first production run. The 13.5" polyester laminator cannot accommodate 30" Convex base material; polycarbonate lamination method (wide-format process) to be confirmed at first item quote. See `categories/convex-high-bond-polycarbonate.md` (SHELL) for lamination notes and pricing profile placeholder.

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

Canonical per the §25 formula (`kit sq ft × ($1.21 + $0.2389 + $0.50) + incidental buffer`):

- Vinyl: 0.609 sq ft × $1.21/sq ft = ~$0.74/label
- Laminate (1-mil polyester): 0.609 sq ft × $0.2389/sq ft = ~$0.15/label
- Ink (full bleed per §25): 0.609 sq ft × $0.50/sq ft = ~$0.30/label
- **Per-label material cost: ~$1.19–$1.20** (canonical §25)
- **2-label kit (1278890): $2.40** (1.218 sq ft × $1.9489 = $2.374 + buffer)
- **3-label kit (1278930): $3.60** (1.827 sq ft × $1.9489 = $3.561 + buffer)
- **5-label kit (1245130): $5.95** (3.045 sq ft × $1.9489 = $5.934 + buffer)

> **Costing-era note (2026-06-09, Session H):** The prior kit totals ($2.99 and
> $5.16) were a legacy pre-§25 build that amortized laminate per lamination
> pass instead of charging the §25 per-sq-ft rate, and used a ~$0.27/label ink
> estimate instead of the §25 full-bleed $0.50/sq ft. That method is RETIRED as
> "canonical." The §25 canonical formula (PRICING_RULES.md §25, Account-Wide Ink
> Coverage Standard above) is the single costing method for every printed/
> laminated item — kits included. Frontmatter `material_cost_per_unit` values
> are ground truth and now carry the §25 canonical totals on the full kit
> family. No sell prices changed in the normalization.

### At 15" × 12.44" (single load chart label)

Canonical per the §25 formula (`sq ft × ($1.21 + $0.2389 + $0.50) + incidental buffer`):

- Vinyl: 1.296 sq ft × $1.21 = $1.568
- Laminate (1-mil polyester): 1.296 sq ft × $0.2389 = $0.310
- Ink (full bleed per §25): 1.296 sq ft × $0.50 = $0.648
- Calculated: $2.526 + incidental buffer (conservative round-up)
- **Per-label material cost: $2.60** (canonical §25 — P/N 1230820, normalized 2026-06-09; the prior $2.32–$3.23 range carried a legacy pre-§25 waste/setup line, retired)

### Cut Vinyl at ~2.51–2.56 sq ft (Small-Format Band)

Vinyl AND tape are both length-based (tape harmonized 2026-06-09, audit D3): `feed length (label length + 6" spacing) in yd × cost_per_linear_yd ÷ labels per row`.

- Cardinal Red, 24" roll: ~$7.23 vinyl + $0.65 tape = **~$7.88/label total** *(at 2.56 sq ft, P/N 1205720 / 1186310 — 2-up, feed 39.5625" = 1.0990 yd)*
- Olympic Blue, 24" roll: ~$7.43 vinyl + $0.64 tape = **~$8.07/label total** *(at 2.512 sq ft, P/N 3018378 — 2-up, feed 38.88" = 1.0800 yd)*
- White, 24" roll: ~$8.00 vinyl + $0.82 tape = **~$8.82/label total** *(at 2.56 sq ft, P/N 3017435 — 2-up, feed 49.91" = 1.3864 yd)*
- White, 48" roll: ~$6.28 vinyl + $0.33 tape = **~$6.61/label total** *(at 2.56 sq ft, P/N 3017435 — 5-up on 48" roll)*

> **Tape method note (2026-06-09):** The prior tape figures (~$1.49–$1.51/label) used `label area × $0.5911/sq ft` — a pseudo-rate ($1.1821/yd ÷ 2 ft roll width) that is not a true area rate and overstated tape ~2.7×. Retired. Tape amortizes per row exactly like vinyl. The 582U `cost_per_sq_ft` field is a derived convenience value — never use it in a per-label cost build.

### Cut Vinyl at ~7.069 sq ft (Large-Format Band — added 2026-06-05)

- Cardinal Red, **15" roll** + **30" TransferRite tape**: **$18.51 vinyl + $1.51 tape = $20.02/label total** *(at 7.069 sq ft, P/N 3010704 — length-based method)*
  - Vinyl: 2.1337 yd feed × $8.6754/yd = $18.51 (single-across nesting on 15" roll, 14.375" label height + 0.625" clearance, feed length 70.8125" + 6" spacing = 76.8125" = 2.1337 yd).
  - Tape: 2.1337 yd feed × $1.4186/yd = $3.03 per row of 2 labels (2-up nesting on 30" tape, 2 × 14.375" = 28.75" across 30" tape with 1.25" waste strip). Per-label tape cost: $3.03 ÷ 2 = $1.51.
  - Material cost per sq ft: $20.02 ÷ 7.069 = $2.83/sq ft (vs $3.41/sq ft on the small-format band — larger area amortizes the tape feed cost).

### Cut Vinyl at ~0.969 sq ft (Sub-1 sq ft Band C — added 2026-06-05)

Three founding data points share identical geometry (34.887" × 4" = 0.969 sq ft) and identical nesting (5-up on 24" × 50yd roll, feed length per row of 5 = 34.887" + 6" spacing = 40.887" = 1.1357 yd). Vinyl and tape cost per row of 5 are divided by 5 to get per-label cost. All three colors use the 24" × 100yd TransferRite 582U tape (matches 24" roll width exactly, no overhang).

| Color | Vinyl Roll | $/Yd | Vinyl/Row | Vinyl/Label | Tape/Label | **Total/Label** | $/Sq Ft |
|-------|-----------|------|-----------|-------------|------------|------------------|---------|
| **Cardinal Red** (worst case anchor) | 24" × 50yd ($775.10) | $15.502 | $17.603 | **$3.52** | $0.27 | **$3.79** | $3.91 |
| **Black** | 24" × 50yd ($659.26) | $13.1852 | $14.972 | **$2.99** | $0.27 | **$3.26** | $3.36 |
| **White** | 24" × 50yd ($619.21) | $12.3842 | $14.063 | **$2.81** | $0.27 | **$3.08** | $3.18 |

- Vinyl cost per row of 5 = 1.1357 yd × cost_per_linear_yd. Per-label vinyl = row cost ÷ 5.
- Tape cost per row of 5 = 1.1357 yd × $1.1821/yd = $1.342. Per-label tape = $1.342 ÷ 5 = $0.27.
- Labels per 50yd roll = floor(50 / 1.1357) = 44 rows × 5 = **220 labels per roll** for all three colors.
- Cardinal Red anchors the Band C pricing (worst-case material cost). All three P/Ns (3010707, 3010708, 3010709) share identical tier table — color-only difference, no price difference. See `items/3010707.md` for the 4-wave validation record.
