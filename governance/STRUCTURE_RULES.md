# Structure Rules — Item Documentation Standard

> **The law. Every item follows it. No shortcuts.**
>
> Last Updated: 2026-05-22

---

## Item File Schema (YAML Frontmatter)

Every item file in `items/` has YAML frontmatter with ALL of the following fields. No field is ever omitted.

```yaml
---
part_number: "1230820"                    # Exact P/N from engineering drawing
description: "Load Chart Label, D105"     # Short descriptor from drawing title block
model: "D105"                             # Elliott model this item belongs to
item_type: "Printed/Laminated Label"      # Vinyl Cut Lettering | Printed/Laminated Label | Printed/Laminated Kit | Panel Decal
material_family: "Orajet 3951 Cast + Polyester Lam"  # Must match a defined family
label_count: 1                            # 1 for singles, total labels for kits
width_in: 15                              # Per-label width from engineering drawing
height_in: 12.44                          # Per-label height from engineering drawing
sq_ft_per_label: 1.296                    # width × height / 144 — calculated, never estimated
sq_ft_per_kit: 1.296                      # sq_ft_per_label × label_count
material_cost_per_unit: 4.00              # Total material cost per sellable unit (vinyl + lam + ink + tape)
cost_version_date: "2026-04-22"           # Date of the material cost data used
price_1_9: 30
price_10_19: 24
price_20_49: 20
price_50_99: 17
price_100_199: 14
price_200_plus: 11
first_article_price: 55                   # Blank only if FA was not requested or offered
per_label_at_qty_20: 20.00               # price_20_49 / label_count
margin_at_qty_20: "~80%"                  # (price_20_49 - material_cost) / price_20_49
pricing_logic: "ROOT BENCHMARK. Establishes singles band at ~$15.43/sq ft."
benchmark_item: "None — ROOT BENCHMARK"   # P/N this was priced from, or "None" with explanation
downstream_items: "1278930 (1.5x), 1245130 (5/3 parity off 1278930)"
process: "Print/Lam/Cut (1 pass)"         # Cut/Weed/Mask | Print/Lam/Cut (1 pass) | Print/Lam/Cut (2 pass)
lamination_passes: 1                      # 0 for cut vinyl
cut_runs: 1
status: "FA Accepted"                     # Quoted | FA Ordered | FA Accepted | In Production | Active Reorder
date_quoted: "2026-04-22"
override_type: ""                         # Blank if no override. Otherwise one of the 6 types.
notes: ""                                 # Anything that doesn't fit elsewhere
---
```

---

## Required Sections (In This Exact Order)

Every item file has these sections below the frontmatter:

### 1. Spec Extraction
The completed extraction output from `governance/SPEC_EXTRACTION.md`. Stored as a permanent record. Items priced before the protocol existed have reconstructed extractions labeled as such.

### 2. Item Overview
Part number, description, type, content description (what the label says/shows), dimensions with tolerances, DWG date and revision, status.

### 3. Material Specification
Exact material name, product code, color code. Film type, thickness, adhesive type. Laminate spec if applicable. Application tape if applicable. Roll sizes available with pricing.

### 4. Nesting and Material Cost
How many labels fit per row on each available roll width. Linear footage per label/kit. Cost per label/kit broken down by component (vinyl, laminate, ink, tape). Total material cost per unit. Optimal roll size at different volumes.

### 5. Production Process
Step by step: print, laminate, cut, weed, inspect, package. Number of passes for each step. Equipment used. Constraints or bottlenecks. Estimated production time if known.

### 6. Pricing
Full tier table. First article price if applicable.

### 7. Pricing Derivation
How the price was built. Which benchmark and multiplier/logic. Whether AI model validation was run (models, rounds, consensus, debates). Strategic considerations. Must reference the category Pricing Profile band.

### 8. Margin Analysis
Margin at each tier (minimum qty 20 and 200+). Dollar profit per unit at key tiers. Comparison to internal P&L benchmark (79.7%).

### 9. Notes and Warnings
Anything future sessions need to know. Precedent implications. Equipment constraints. Risks.

### 10. Production Debrief
Running log updated after production runs. Actual material vs estimated, time, scrap, issues, whether pricing assumptions held. Placeholder until first production run.

---

## Material Family Definitions

New families added only when a genuinely different material system is introduced. Variations within a family (colors, roll sizes) do not create new families.

| Material Family | What It Covers |
|-----------------|----------------|
| 3M 180mC Cut Vinyl | All 3M Controltac 180mC colors. Cut vinyl lettering, no printing. |
| Orajet 3951 Cast + Polyester Lam | Orajet 3951 base + 1-mil polyester overlaminate. Printed full-color. |
| Convex High Bond + Poly Lam | Convex 6-mil high bond + polycarbonate overlaminate. Panel decals. |
| Lexan/Polycarbonate | Direct print on polycarbonate substrate. Legacy Elliott spec. |

---

## Pricing Logic Documentation Rules

1. Every item's pricing logic MUST reference both the category Pricing Profile band AND any specific benchmark item used.
2. If within the Profile band: state explicitly with the band values.
3. If outside the Profile band: document why (complexity, new material, process exception) or flag for review.
4. If priced from scratch (no benchmark, no profile): state explicitly and document methodology.
5. If AI model validation was performed: note model count, round count, unanimous or split.
6. Never document multipliers in a way that could be shared with the buyer. Internal logic only.

---

## Rules for Adding New Items

1. Run Spec Extraction Protocol (Step 0).
2. Pull the relevant category's Pricing Profile — primary validation tool.
3. Compare against specific benchmark items as secondary reference.
4. If within the Profile band: price using the band, document the fit.
5. If outside the Profile band: flag it. Document the reason.
6. If no Profile exists (first item in new category): build from scratch, run full AI validation, document that this establishes the founding data point.
7. Create the item file with ALL frontmatter fields and ALL required sections.
8. Update the category file (items table + Pricing Profile).
9. Update `.claude/ARCHITECTURE.md` (item catalog row).
10. Both item file and category update must be complete before the quote is ready to send.

---

## Rules for Updating Existing Items

- **Status changes:** Update item frontmatter + Item Overview section + ARCHITECTURE.md simultaneously.
- **Price changes:** Update all 6 tiers in frontmatter, update Pricing + Margin sections, check all downstream items.
- **Material cost changes:** Update frontmatter material_cost + cost_version_date, recalculate margins, update category profile.
- **Never delete pricing history.** If a price changes, note the old price and date in the item file.

---

## Naming Conventions

- **Item file name:** `[part_number].md` (e.g., `1230820.md`)
- **Category file name:** `[material-family-slug].md` (e.g., `cut-vinyl-3m-180mc.md`)
