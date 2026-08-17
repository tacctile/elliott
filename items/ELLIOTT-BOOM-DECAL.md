---
part_number: "ELLIOTT BOOM DECAL"
description: "Elliott Boom Decal"
model: "Multiple"
item_type: "Vinyl Cut Lettering"
material_family: "3M 180mC Cut Vinyl"
label_count: 1
width_in: 33.1261
height_in: 10
sq_ft_per_label: 2.300
sq_ft_per_kit: 2.300
material_cost_per_unit: 6.68
cost_version_date: "2026-08-17"
price_1_9: 45
price_10_19: 40
price_20_49: 35
price_50_99: 30
price_100_199: 26
price_200_plus: 22
first_article_price: ""
per_label_at_qty_20: 35.00
margin_at_qty_20: "~81% (Config A / White canonical) — see Margin Analysis for Config B (Black + Red)"
pricing_logic: "Direct dollar-tier-table match to P/N 1186310 (2.564 sq ft, closest sq ft/price match), also identical to P/N 3018378 (2.512 sq ft) and P/N 3017435 (2.56 sq ft, White single-color production reference) — $45/$40/$35/$30/$26/$22 across all four items. NOT scaled proportionally to this item's smaller 2.300 sq ft footprint. Nick-confirmed and sent to Sean directly; the calculator's own validation brief proposed a lower Band A default table ($40/$35/$30/$25/$22/$19) — REJECTED, superseded by Nick's quote. At 2.300 sq ft, $35/qty 20 = $15.22/sq ft — above both the Cut Vinyl Band A Relationship Concession Corridor ($13.65-$13.94/sq ft, governance/PRICING_RULES.md §32) and the Small-Format Premium Corridor ($14.33-$14.36/sq ft). This is a documented above-profile-band exception (see scripts/validate.py BAND_EXCEPTIONS), not a Profile-derived price. §32 Direction B (smaller item must carry >= $/sq ft than its nearest larger validated neighbor) is satisfied with margin to spare: this item, at 2.300 sq ft, is smaller than the 2.512-2.564 sq ft cluster and prices at a materially HIGHER $/sq ft ($15.22 vs $13.65-$13.94) — no chain-consistency violation in either direction."
benchmark_item: "P/N 1186310 (closest sq ft/price match, 2.564 sq ft) — also P/N 3018378 (2.512 sq ft) and P/N 3017435 (2.56 sq ft, White single-color production/material reference)"
downstream_items: "None yet."
process: "Cut/Weed/Mask"
lamination_passes: 0
cut_runs: 1
status: "Quoted"
date_quoted: "2026-08-17"
override_type: "Owner Judgment"
notes: "VARIABLE-BOM ITEM — color composition (1-color White or 2-color Black+Red) is determined per-order by Elliott, not fixed by drawing. Frontmatter material_cost_per_unit ($6.68) reflects Config A (White, single color) — the first production run and the STRUCTURE_RULES-designated canonical basis. Config B (Black + Red, two color, $14.48/label) is documented in full below but is NOT filed as a second item or a second frontmatter cost — do not average the two configs. Price is identical regardless of configuration. First article: not specified/requested — TBD, flag for Sean follow-up. Non-standard P/N: no numeric Elliott drawing part number exists for this item; 'ELLIOTT BOOM DECAL' is Nick-assigned and filed as the literal, permanent P/N string."
---

# Spec Extraction

Item priced from a Nick-provided session brief (already quoted directly to Sean), not from an Elliott engineering drawing PDF. No formal title-block extraction exists. Reconstructed per `governance/SPEC_EXTRACTION.md` format below.

```
SPEC EXTRACTION — P/N ELLIOTT BOOM DECAL

Identity:
  Part Number: ELLIOTT BOOM DECAL — Confirmed (non-standard; no numeric Elliott drawing P/N exists; Nick-assigned literal string, permanent, not a placeholder)
  Revision: None — Assumed (no drawing on file)
  Model: Not model-specific — Confirmed (applies generically across boom-equipped models, per account convention for non-model-specific brand/component decals, matching P/N 3017435's "Multiple" filing)
  Description: Elliott Boom Decal — Confirmed (Nick-provided)
  Engineer/Drafter: Not captured — Assumed (informational only, no pricing impact)

Dimensions:
  Width: 33.1261" — Confirmed (Nick-provided)
  Height: 10" — Confirmed (Nick-provided)
  Tolerances: ±1/16" — Assumed (account default)
  Corners: Square — Assumed (cut vinyl lettering/decal, no radius called out)
  Unit of Measure: Inches — Assumed (account default)

Structure:
  Label Count: 1 — Confirmed
  Labels Same Size: N/A (single label) — Confirmed

Material:
  Substrate Callout: "3M 180mC" — Confirmed (Nick-provided, family only)
  Mapped To: 3M Controltac 180mC Cut Vinyl — Confirmed
  Color Count / Combination: VARIABLE — Confirmed as a permanent property of this item, not a data gap. Two configurations shipped to date: Config A (White only) and Config B (Black + Cardinal Red). Elliott's own spec does not fix color count or combination per order.
  Laminate: N/A — cut vinyl, no laminate
  Application Tape: TransferRite Ultra 582U — Assumed (account standard for cut vinyl)

Print:
  Colors: Variable — White (Config A) or Black + Cardinal Red (Config B) — Confirmed as genuinely variable, see Configuration Variability section below
  Coverage: N/A — cut vinyl
  Variable Data: None — Confirmed

Environment:
  Durability: 5-7 year outdoor industrial — Assumed (account default)
  Regulatory: None — Confirmed (brand/component decal, no ANSI content)

Finish & Delivery:
  Finish: Standard vinyl finish — Assumed
  Packaging: Flat, masked with transfer tape — Assumed (account standard)
  Application: Hand-applied on equipment — Assumed (account default)

BLOCKED FIELDS: None. (Color count/combination is intentionally VARIABLE, not Blocked — see Configuration Variability.)
ASSUMPTIONS: (1) No drawing revision on file. (2) Not model-specific — applies generically. (3) Tolerances ±1/16". (4) Square corners. (5) TransferRite Ultra 582U tape (account standard). (6) 5-7yr outdoor durability. (7) Hand-applied.
```

---

# Item Overview

- **Part Number:** ELLIOTT BOOM DECAL (non-standard, Nick-assigned — no numeric Elliott drawing P/N exists for this item)
- **Description:** Elliott Boom Decal
- **Type:** Vinyl cut lettering/decal (no printing)
- **Content:** Boom-mounted decal, applied to Elliott boom sections. Not tied to a specific model.
- **Dimensions:** 33.1261" W × 10" H (2.300 sq ft per label)
- **Tolerances:** ±1/16" (assumed account default)
- **DWG Date:** No drawing on file — Nick-provided spec, already quoted to Sean
- **Status:** Quoted 2026-08-17

---

# Configuration Variability

**This item has a genuinely variable BOM — a permanent property of the part, not a placeholder or a data gap.** Elliott's own spec does not fix the color count or color combination per order; the buyer has ordered two distinct, valid configurations to date:

| Config | Colors | Passes | Status |
|--------|--------|--------|--------|
| **Config A** | White (single color) | 1 | **First production run.** Canonical basis for frontmatter `material_cost_per_unit`. |
| **Config B** | Black + Cardinal Red (two color) | 2 | Second known order. Registered to the identical 33.1261" × 10" footprint. |

**Price is identical across both configurations** — $45/$40/$35/$30/$26/$22 regardless of whether the order comes in as Config A or Config B. This is not a placeholder awaiting resolution: both configurations are currently valid, ongoing, real order patterns for this P/N, and a future order may repeat either one or introduce a new valid combination within the same White/Cardinal Red/Black 3M 180mC palette. Do not resolve this to a single fixed color count in a future session without new information from Elliott.

Material cost and production process are documented separately for each known configuration below (Nesting and Material Cost, Production Process). Per `governance/STRUCTURE_RULES.md`'s convention for the canonical frontmatter cost field, Config A (White) governs `material_cost_per_unit` because it was the first production run — this is a documentation convention, not a statement that White is "the" configuration. Config A and Config B costs are **not averaged or blended** into a single figure.

---

# Material Specification

## Config A — White (single color)

- **Substrate:** 3M Controltac 180mC-10 White
- **Film Type:** 2-mil calendered vinyl
- **Adhesive:** Controltac repositionable pressure-sensitive
- **Roll Used (canonical):** 24" × 10yd = $131.16/roll ($13.116/yard) — `materials/3m-180mc-white-24in.md`. This is the higher-cost/smaller-roll scenario per `governance/STRUCTURE_RULES.md` convention (same roll used canonically by P/N 3017435 and P/N 1257750). A 48" × 10yd roll (`materials/3m-180mc-white-48in.md`) and a 24" × 50yd production roll also exist for this color and would improve yield at volume — not filed canonically, per account convention of documenting the conservative smaller-roll cost in frontmatter.
- **Application Tape:** TransferRite Ultra 582U, 24" × 100yd = $118.21 ($1.1821/linear yd) — `materials/transferrite-582u.md`

## Config B — Black + Cardinal Red (two color)

- **Substrate (Black):** 3M Controltac 180mC-12 Black, 24" × 50yd = $659.26/roll ($13.1852/yard) — `materials/3m-180mc-black.md`
- **Substrate (Cardinal Red):** 3M Controltac 180mC-53 Cardinal Red, 24" × 50yd = $775.10/roll ($15.502/yard) — `materials/3m-180mc-cardinal-red.md`
- **Film Type:** 2-mil calendered vinyl (both colors)
- **Adhesive:** Controltac repositionable pressure-sensitive (both colors)
- **Application Tape:** TransferRite Ultra 582U, 24" × 100yd — one mask pass per color, `materials/transferrite-582u.md`
- **Registration:** Both colors are cut, weeded, and masked independently to the same 33.1261" × 10" footprint, then registered together — see Production Process.

**Laminate:** N/A (cut vinyl, no laminate) — both configs.

---

# Nesting and Material Cost

## Config A — White (24" × 10yd roll, canonical)

Label height (10") nests 2-across on the 24" roll (2 × 10" = 20", 4" waste strip) — same nesting convention as the 2.51-2.564 sq ft cluster (1186310, 3018378, 3017435).

**Vinyl (length-based):**

| Step | Value |
|------|-------|
| Label length (feed direction) | 33.1261" = 0.920169 yd |
| Cost per row of 2 labels | 0.920169 yd × $13.116/yd = $12.0689 |
| Vinyl cost per label | $12.0689 ÷ 2 = **$6.03** |

**Application Tape (length-based):**

| Step | Value |
|------|-------|
| Feed length per row | 33.1261" + 6" spacing = 39.1261" = 1.086836 yd |
| Tape cost per row of 2 labels | 1.086836 yd × $1.1821/yd = $1.2847 |
| Tape cost per label | $1.2847 ÷ 2 = **$0.64** |

**Total Material Cost per Label (Config A, canonical):**

| Component | Cost |
|-----------|------|
| Vinyl (3M 180mC-10 White, 24"×10yd) | $6.03 |
| Application tape (TransferRite 582U) | $0.64 |
| **Total material cost per label** | **$6.68** |

## Config B — Black + Cardinal Red (24" × 50yd rolls, two full-footprint passes)

Each color is cut from its own vinyl, sized to the full 33.1261" × 10" bounding box (the account's standard conservative convention for multi-color decals with no known area split between colors — see the G50 set, P/N 3010722/3010723/3010724, for precedent). Same 2-across nesting on 24" roll for both colors.

**Black (materials/3m-180mc-black.md, $13.1852/yd):**

| Step | Value |
|------|-------|
| Cost per row of 2 labels | 0.920169 yd × $13.1852/yd = $12.1326 |
| Vinyl cost per label | $12.1326 ÷ 2 = **$6.07** |

**Cardinal Red (materials/3m-180mc-cardinal-red.md, $15.502/yd):**

| Step | Value |
|------|-------|
| Cost per row of 2 labels | 0.920169 yd × $15.502/yd = $14.2645 |
| Vinyl cost per label | $14.2645 ÷ 2 = **$7.13** |

**Application Tape (two mask passes, one per color):**

| Step | Value |
|------|-------|
| Tape cost per pass (same feed length as Config A) | **$0.64** |
| Two passes (Black mask + Red mask) | 2 × $0.64 = **$1.28** |

**Total Material Cost per Label (Config B, documentation only — NOT the canonical frontmatter figure):**

| Component | Cost |
|-----------|------|
| Black vinyl | $6.07 |
| Cardinal Red vinyl | $7.13 |
| Application tape (2 passes) | $1.28 |
| **Total material cost per label** | **$14.48** |

Per `governance/STRUCTURE_RULES.md`'s canonical-cost convention, `material_cost_per_unit` in frontmatter files Config A's $6.68 (the first production run). Config B's $14.48 is documented here in full but is not blended, averaged, or filed as a second cost figure.

---

# Production Process

## Config A — White (Cut/Weed/Mask, 1 pass)

1. File import/setup — open the Elliott-supplied production-ready DWG, send to cutter. ~5 min mechanical. NOT billable labor (see `PRICING_RULES.md` §22).
2. Cut — Roland SG3-300 on 24" White stock, 2 labels per row.
3. Weed — remove excess vinyl around the boom decal artwork.
4. Mask — apply TransferRite 582U application tape.
5. Inspect and package.

- **Lamination Passes:** 0
- **Cut Runs:** 1

## Config B — Black + Cardinal Red (Cut/Weed/Mask/Register, 2 passes)

1. File import/setup — open the Elliott-supplied production-ready DWG (both color layers), send to cutter. ~5 min mechanical. NOT billable labor.
2. Cut — Roland SG3-300, Black stock, full-footprint pass 1.
3. Cut — Roland SG3-300, Cardinal Red stock, full-footprint pass 2.
4. Weed — remove excess vinyl on each color separately.
5. Mask — apply TransferRite 582U to each color separately (one mask pass per color).
6. Register — align the two color layers to the same 33.1261" × 10" footprint during application prep so the finished decal reads as a single two-color graphic.
7. Inspect and package.

- **Lamination Passes:** 0 (cut vinyl, no lamination in either config)
- **Cut Runs:** 2 (one per color)

---

# Pricing

| Qty | Price |
|-----|-------|
| 1-9 | $45 |
| 10-19 | $40 |
| 20-49 | $35 |
| 50-99 | $30 |
| 100-199 | $26 |
| 200+ | $22 |

*Price is identical for Config A and Config B — see Configuration Variability.*

*No first article pricing — not specified/requested this session; TBD, flag for Sean follow-up.*

---

# Pricing Derivation

**Methodology:** Direct dollar-tier-table match, not a $/sq ft scale-off.

**Comparison:**

| Item | Dimensions | Sq Ft | Price (qty 20) | $/sq ft |
|------|-----------|-------|-----------------|---------|
| P/N 1186310 (closest match) | 33-9/16" × 11" | 2.564 | $35 | $13.65 |
| P/N 3018378 | 32.88" × 11.00" | 2.512 | $35 | $13.94 |
| P/N 3017435 (White reference) | 43.91" × 8.38" | 2.56 | $35 | $13.67 |
| **ELLIOTT BOOM DECAL (this item)** | **33.1261" × 10"** | **2.300** | **$35** | **$15.22** |

**Step 1 — Source of the price.** Nick priced this item directly and sent the quote to Sean before this session began, per the session brief: "Nick-confirmed, sent to Sean directly — do not re-derive from calculator brief." The calculator's own validation brief for this item proposed a Band A default table ($40/$35/$30/$25/$22/$19, Band A small-format routing) — this is **explicitly rejected** per the session brief and not used.

**Step 2 — Benchmark basis.** Nick's quoted table ($45/$40/$35/$30/$26/$22) is byte-identical to the accepted/quoted tables on P/N 1186310, P/N 3018378, and P/N 3017435 — all three in the 2.51-2.564 sq ft cluster. P/N 1186310 is the closest sq ft/price match cited in the session brief. This item, at 2.300 sq ft, is smaller than all three — the price was **not** scaled down proportionally for the smaller footprint; it was matched dollar-for-dollar.

**Step 3 — Profile band check (Rule 15).** $35 ÷ 2.300 sq ft = $15.22/sq ft at qty 20. This is above both currently documented Band A corridors:
- Relationship Concession Corridor (≥~1.5 sq ft): $13.65-$13.94/sq ft
- Small-Format Premium Corridor (<~1.2 sq ft): $14.33-$14.36/sq ft

At 2.300 sq ft this item sits inside the size range covered by the Relationship Concession Corridor's interior gap zone (1146650, 3010698, 3023921, the 2.51-2.564 sq ft cluster) — none of which reach $15.22/sq ft. **This is a documented above-profile-band exception**, filed in `scripts/validate.py` `BAND_EXCEPTIONS`, not a Profile-derived or AI-validated price.

**Step 4 — §32 chain-consistency check (Direction B).** §32 requires a smaller item's $/sq ft to be at or above its nearest larger validated neighbor's, at every tier. This item (2.300 sq ft) is smaller than its nearest larger neighbors (the 2.512-2.564 sq ft cluster, all $13.65-$13.94/sq ft at qty 20) and prices at $15.22/sq ft — comfortably above at every tier (the full tier table is byte-identical to 1186310/3018378/3017435's, so every tier clears by the same margin). **No §32 violation in either direction** — this item satisfies Direction B with significant headroom, unlike prior flagged cases (1257750, 3023921) where the smaller item priced below its larger neighbor.

**AI Validation:** Not run. Price was Nick-confirmed and already communicated to Sean prior to this session, per explicit session instruction not to re-derive from the calculator brief.

**Override:** `override_type: "Owner Judgment"` — Nick set the exact tier table directly, bypassing both the calculator's Band A default output and $/sq ft-proportional scaling from the cited benchmarks.

---

# Margin Analysis

## Config A — White (canonical, $6.68/label material cost)

| Qty Tier | Price | Material Cost | Gross Profit | Margin |
|----------|-------|----------------|---------------|--------|
| 1-9 | $45.00 | $6.68 | $38.32 | ~85% |
| 10-19 | $40.00 | $6.68 | $33.32 | ~83% |
| 20-49 | $35.00 | $6.68 | $28.32 | ~81% |
| 50-99 | $30.00 | $6.68 | $23.32 | ~78% |
| 100-199 | $26.00 | $6.68 | $19.32 | ~74% |
| 200+ | $22.00 | $6.68 | $15.32 | ~70% |

## Config B — Black + Cardinal Red (documentation only, $14.48/label material cost)

| Qty Tier | Price | Material Cost | Gross Profit | Margin |
|----------|-------|----------------|---------------|--------|
| 1-9 | $45.00 | $14.48 | $30.52 | ~68% |
| 10-19 | $40.00 | $14.48 | $25.52 | ~64% |
| 20-49 | $35.00 | $14.48 | $20.52 | ~59% |
| 50-99 | $30.00 | $14.48 | $15.52 | ~52% |
| 100-199 | $26.00 | $14.48 | $11.52 | ~44% |
| 200+ | $22.00 | $14.48 | $7.52 | ~34% |

**Margin at qty 20: ~81% on Config A, ~59% on Config B.** Because price is fixed regardless of configuration, actual realized margin on any given order depends on which color combination Elliott specifies. This is a real, permanent margin spread on this P/N — not a costing error. `margin_at_qty_20` in frontmatter reports the Config A figure as canonical, consistent with the material_cost_per_unit convention.

---

# Notes and Warnings

- **Variable-BOM item — do not resolve to a single fixed configuration in a future session.** Both Config A (White) and Config B (Black + Red) are current, valid, ongoing order patterns. A future order may repeat either one. Price stays fixed at $45/$40/$35/$30/$26/$22 regardless of which configuration ships.
- **Config B carries materially lower margin than Config A** (~59% vs ~81% at qty 20) because two full-footprint color passes are priced under one flat table. This is accepted account-level pricing simplicity (per §4-7, never expose multiplier/cost-plus math to the buyer) — do not attempt to surcharge Config B orders differently from Config A without Nick's direction.
- **Above-profile-band exception, not a violation.** $15.22/sq ft at qty 20 sits above both currently documented Band A corridors. This is a direct, Nick-directed dollar-match to 1186310/3018378/3017435, not a Profile-derived or scaled price. Flagged in `scripts/validate.py` `BAND_EXCEPTIONS` for transparency; does not represent a §32 chain-consistency violation (see Pricing Derivation Step 4) — if anything, this item's $/sq ft is well in excess of what §32 requires against its larger neighbors.
- **Calculator's Band A default table explicitly rejected.** The calculator-generated validation brief proposed $40/$35/$30/$25/$22/$19 based on Band A small-format routing. Nick's quote to the buyer supersedes it. Do not resurrect the calculator table as a benchmark for this item in a future session.
- **Non-standard P/N.** "ELLIOTT BOOM DECAL" is a Nick-assigned literal string, not a numeric Elliott drawing part number. `scripts/validate.py` does not enforce a numeric-only P/N pattern (confirmed before filing — see `check_architecture_registry()`'s `\d{7}` regex, which only targets 7-digit numeric P/Ns for a different, unrelated check and does not block or reject non-numeric part numbers elsewhere in the script). Filed as the literal string per explicit session instruction.
- **First article not specified.** Not requested or offered as of this session — flagged for Sean follow-up, does not block sending (already quoted).
- **Order quantity not specified** — standard 6-tier ladder quoted, flagged for Sean follow-up.

---

# Production Debrief

*No production debrief yet. Update after each production run — capture, per run, which configuration shipped (Config A White or Config B Black+Red), actual nesting yield, weeding/registration time (especially for Config B's two-color register step), and whether the material cost assumptions held for that specific configuration.*
