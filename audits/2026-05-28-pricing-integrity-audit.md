# Elliott Equipment — Pricing Audit Progress Log

---

## 2026-05-28 — Full Pricing Integrity Audit

**Scope:** All 14 items, all 7 material files, all category files, ARCHITECTURE.md, STATE.yml.
**Branch:** `claude/eager-ride-WsrAr`
**Validator result:** 0 errors, 0 warnings (before and after corrections).

---

### Summary

11 audit checks completed. 6 permitted documentation corrections applied. 2 flags raised for Nick's review (no pricing fields changed). No prices changed in this audit.

---

### CHECK 1 — Frontmatter Math Verification

**Result: PASS**

All 14 items verified:

| P/N | sq_ft calc | material_cost logic | margin calc | Result |
|-----|------------|---------------------|-------------|--------|
| 1230820 | 15×12.44/144 = 1.296 ✓ | vinyl+lam+ink+waste = $4.00 ✓ | (20-4)/20 = 80% ✓ | PASS |
| 1278930 | 11.13×7.88/144 = 0.609/label, ×3 = 1.827 ✓ | vinyl+lam+ink = $3.63 ✓ | (30-3.63)/30 = 88% ✓ | PASS |
| 1245130 | 0.609/label ×5 = 3.045 ✓ | vinyl+lam+ink = $6.03 ✓ | (50-6.03)/50 = 88% ✓ | PASS |
| 1205720 | 33.5625×11/144 = 2.5638 → 2.56 ✓ | length-based: $7.226 vinyl + $1.513 tape = $8.74 ✓ | (35-8.74)/35 = 75% ✓ | PASS |
| 3017435 | 43.91×8.38/144 = 2.5560 → 2.56 ✓ | $8.00 vinyl (24") + $1.513 tape = $9.51 ✓ | (35-9.51)/35 = 73% (24") ✓ | PASS |
| 3018378 | 32.88×11/144 = 2.512 ✓ | $7.43 vinyl + $1.485 tape = $8.92 ✓ | (35-8.92)/35 = 75% ✓ | PASS |
| 1186310 | 33.5625×11/144 = 2.564 ✓ | same as 1205720: $8.74 ✓ | (35-8.74)/35 = 75% ✓ | PASS |
| 1277970 | Ø1-3/16" circle area = 0.00768 → 0.008 (per file) ✓ | $6.94 full job / 20 = $0.35 ✓ | N/A (one-off) | PASS |
| 1277980 | Same as 1277970 ✓ | $0.35 ✓ | N/A | PASS |
| 1277990 | Same as 1277970 ✓ | $0.35 ✓ | N/A | PASS |
| 1278000 | Same as 1277970 ✓ | $0.35 ✓ | N/A | PASS |
| 3017583 | 2.5×1.5/144 = 0.026 ✓ | $1.70 job / 6 = $0.28 ✓ | (9.17-0.28)/9.17 = 97% ✓ | PASS |
| 3017584 | 0.5×0.5/144 = 0.00174 ✓ | ~$0.50 job / 6 = $0.08 ✓ | (9.17-0.08)/9.17 = 99% ✓ | PASS |
| 1082570 | 10×7.25/144 = 0.5035 → 0.503 ✓ | $0.61+$0.49+$0.60 = $1.70 ✓ | (8-1.70)/8 = 79% ✓ | PASS |

No frontmatter calculation errors found on any item.

---

### CHECK 2 — Material Cost Verification

**Result: PASS**

Cut vinyl items use length-based method ($/linear yd ÷ labels per row + tape at $0.5911/sq ft). All verified:

- **1205720:** 0.9323 yd × $15.502/yd ÷ 2 = $7.226 vinyl + 2.56 sq ft × $0.5911 = $1.513 tape = **$8.74** ✓
- **1186310:** Same dims/material as 1205720 = **$8.74** ✓
- **3018378:** 0.9133 yd × $16.278/yd ÷ 2 = $7.433 vinyl + 2.512 × $0.5911 = $1.485 tape = **$8.92** ✓
- **3017435 (24"):** 1.2197 yd × $13.116/yd ÷ 2 = $8.001 vinyl + 2.56 × $0.5911 = $1.513 tape = **$9.51** ✓
- **3017435 (48"):** 1.2197 yd × $25.744/yd ÷ 5 = $6.281 vinyl + 1.513 tape = **$7.79** ✓

Print/lam items use area method + ink estimates + waste. All breakdowns shown in item files and verified as internally consistent against material rates ($1.21/sq ft Orajet, $0.98/sq ft lam).

---

### CHECK 3 — Pricing Profile Band Consistency

**Result: PASS (one documentation correction applied)**

**Cut Vinyl band:**
- 1205720: $35/2.56 = $13.67/sq ft ✓ (lower bound)
- 3017435: $35/2.56 = $13.67/sq ft ✓
- 3018378: $35/2.512 = $13.94/sq ft ✓ (upper bound)
- 1186310: $35/2.564 = $13.65/sq ft ✓ (3-decimal rounding artifact — same dims as 1205720)

Band table in `categories/cut-vinyl-3m-180mc.md` listed "$13.67–$13.93" but actual range is $13.65–$13.94. Corrected to match the narrative already present in the same file. *(Correction D applied.)*

**Printed/Lam singles band:**
- 1230820: $20/1.296 = $15.43/sq ft ✓
- 1082570: $8/0.503 = $15.91/sq ft ✓

**Kit band:**
- 1278930: $30/3 = $10.00/label ✓
- 1245130: $50/5 = $10.00/label ✓

---

### CHECK 4 — Precedent Chain Integrity

**Result: PASS**

- 1230820 → 1278930: $20 × 1.5 = $30 ✓
- 1278930 → 1245130: $30 × 5/3 = $50 ✓
- 1205720 → 3017435/3018378/1186310: sq ft parity at $35 ✓
- 1082570 → 1230820 singles band: $15.91/sq ft vs $15.43/sq ft anchor (+3%) ✓

All chains intact.

---

### CHECK 5 — Override Documentation

**Result: PASS**

- 1205720: override_type "Relationship Concession" — documented in frontmatter, pricing_logic, prose, and category file ✓
- 1278930: override_type "Relationship Concession (FA only)" — documented in frontmatter and Pricing Derivation ✓
- All other 12 items: override_type empty ("") or no override — appropriate ✓

---

### CHECK 6 — One-Off Item Isolation

**Result: PASS**

All 6 one-off items properly isolated:

| P/N | DO NOT BENCHMARK in frontmatter | Warning blocks in body | Excluded from category Pricing Profile | ARCHITECTURE ⚠ marker |
|-----|--------------------------------|------------------------|----------------------------------------|------------------------|
| 1277970 | ✓ | ✓ (5 blocks) | ✓ | ✓ |
| 1277980 | ✓ | ✓ | ✓ | ✓ |
| 1277990 | ✓ | ✓ | ✓ | ✓ |
| 1278000 | ✓ | ✓ | ✓ | ✓ |
| 3017583 | ✓ | ✓ (6 blocks) | ✓ | ✓ |
| 3017584 | ✓ | ✓ (6 blocks) | ✓ | ✓ |

---

### CHECK 7 — Cross-File Sync

**Result: 4 corrections applied**

| Location | Issue | Resolution |
|----------|-------|------------|
| `materials/orajet-3951-white.md` `used_in_items` | Missing 3017583, 3017584, 1082570 | Added all three *(Fix A)* |
| `materials/1mil-polyester-overlaminate.md` `used_in_items` | Missing 3017583, 3017584, 1082570 | Added all three *(Fix B)* |
| `items/1205720.md` Notes section | Stale prose: "$153.60/roll is the known cost" — predates 2026-05-28 cost update | Updated to "$775.10/roll (24"×50yd, verified 2026-05-28)" *(Fix C)* |
| `.claude/STATE.yml` `pending_quotes` | 1082570 (Quoted 2026-05-28) not listed | Added 1082570 to pending_quotes *(Fix F)* |

ARCHITECTURE.md: all 14 items correctly listed with matching data — no corrections needed. Category table entries vs frontmatter: all match.

---

### CHECK 8 — Category File Integrity

**Result: 2 corrections applied**

**`categories/cut-vinyl-3m-180mc.md`:**
- Pricing Profile table band: "$13.67–$13.93/sq ft" → "$13.65–$13.94/sq ft" to match the narrative section in the same file and the actual per-sq-ft figures of all 4 items. *(Fix D)*

**`categories/printed-laminated-orajet.md`:**
- Pricing Profile singles table referenced pre-validation 1082570 tier data. After 4-round AI validation, the 1-9 tier was raised from $12 to $16.50 and 200+ was revised to $4.25 (see item file Step 4). Two stale rows corrected:
  - Tier compression: "~58–63% ($12→$5, 58%)" → "~63–74% ($16.50→$4.25, 74%)" *(Fix E)*
  - Margin floor: "~64–66% (1082570 at ~66%)" → "~60–64% (1082570 at ~60%, intentional volume reward)" *(Fix E)*

---

### CHECK 9 — Material File Integrity

**Result: 2 fixes applied (used_in_items — see CHECK 7), 2 flags raised**

| Material | used_in_items | cost fields | Other |
|----------|---------------|-------------|-------|
| orajet-3951-white | Corrected (Fix A) | $1.21/sq ft ✓ | — |
| 1mil-polyester-overlaminate | Corrected (Fix B) | $0.98/sq ft ✓ | ⚠ FLAG 1: cost_per_msi = 1.41 inconsistent with cost_per_sq_ft = 0.98 |
| 3m-180mc-cardinal-red | ✓ complete | $15.502/yd ✓ | ⚠ FLAG 2: cost_per_sq_ft = 7.751 uses $/yd÷width_ft formula, not area method |
| 3m-180mc-olympic-blue | ✓ complete | $16.278/yd ✓ | cost_per_sq_ft = 2.713 (area method) ✓ |
| 3m-180mc-white-24in | ✓ complete | $13.116/yd ✓ | cost_per_sq_ft = 2.19 (area method) ✓ |
| 3m-180mc-white-48in | ✓ complete | $25.744/yd ✓ | cost_per_sq_ft = 2.15 (area method) ✓ |
| transferrite-582u | ✓ complete | $0.5911/sq ft ✓ | cost_per_sq_ft derived as $/yd÷width_ft (consistent with how items use it) |

**FLAG 1:** `1mil-polyester-overlaminate.md` `cost_per_msi: 1.41` — if MSI = 1000 sq in = 6.944 sq ft, then $1.41/MSI = $0.203/sq ft, inconsistent with cost_per_sq_ft = 0.98. Field is informational only (not used in item pricing). No correction applied — Nick to verify manufacturer quote unit.

**FLAG 2:** `3m-180mc-cardinal-red.md` `cost_per_sq_ft: 7.751` — derived as $15.502/yd ÷ 2 ft = $7.751/sq ft (using $/yd÷width_ft formula), while the three white/blue materials use the area method ($roll_cost / roll_area). Inconsistency is informational only — item pricing uses length-based method directly and does not read cost_per_sq_ft from the material file. No correction applied without Nick direction.

---

### CHECK 10 — STATE.yml Accuracy

**Result: 1 correction applied**

- item_count: 14 ✓
- material_count: 7 ✓
- last_session date: 2026-05-28 ✓
- pending_quotes: missing 1082570 — added *(Fix F)*
- next_action: current and accurate ✓
- blockers: current and accurate ✓

---

### CHECK 11 — Open Items and Flags

**Open items (unchanged — already documented in item files and STATE.yml):**

1. **1082570 color conflict** — OPEN. Samples delivered ~26 hrs after request. Sean has not confirmed Safety Yellow vs black-on-white. PO not received. Production BLOCKED until resolution. Pricing assumes Safety Yellow (conservative — covers cost under either outcome).

2. **1082570 PO pending** — SO 20125600, qty 2 at $42.00 flat. Next action: send quote when PO arrives, job-economics framing, no per-label math, no MOQ language.

3. **Elliott engineering/procurement standard project** — Sean and his manager initiating. Pro Label has opportunity to help define the standard. Not a pricing input. Nick's outreach pending.

**Flags for Nick's review:**

- FLAG 1: `1mil-polyester-overlaminate.md` cost_per_msi inconsistency (see CHECK 9).
- FLAG 2: `3m-180mc-cardinal-red.md` cost_per_sq_ft formula inconsistency vs other material files (see CHECK 9).

---

### Corrections Applied (6 total)

| Fix | File | Change |
|-----|------|--------|
| A | `materials/orajet-3951-white.md` | used_in_items: added 3017583, 3017584, 1082570 |
| B | `materials/1mil-polyester-overlaminate.md` | used_in_items: added 3017583, 3017584, 1082570 |
| C | `items/1205720.md` | Notes: "$153.60/roll" → "$775.10/roll (24"×50yd, verified 2026-05-28)" |
| D | `categories/cut-vinyl-3m-180mc.md` | Band table: "$13.67–$13.93" → "$13.65–$13.94/sq ft" |
| E | `categories/printed-laminated-orajet.md` | Singles Pricing Profile: stale pre-validation 1082570 tiers corrected (2 rows) |
| F | `.claude/STATE.yml` | pending_quotes: added 1082570 |

**No price fields changed. No frontmatter price, material_cost_per_unit, status, override_type, pricing_logic, or benchmark_item modified.**

---

### Validator

`python scripts/validate.py` — **PASS: 0 errors, 0 warnings** (post-corrections)

---

## 2026-05-28 — Material Cost Update: 1-Mil Polyester Overlaminate

**Scope:** Laminate rate corrected from unreconciled $0.98/sq ft to verified invoice-derived $0.2389/sq ft (all-in including freight). 10 affected printed/laminated items recalculated. No prices changed.
**Branch:** `claude/eager-ride-WsrAr`

---

### Invoice Verification (Nick-confirmed)

| Line | Value |
|------|-------|
| Supplier | Flexcon |
| Product Code | FLX000233 |
| Item | 1055390 |
| Rolls purchased | 8 |
| Roll dimensions | 13.5" wide × 386 ft long |
| Roll area | 13.5" × 386 ft = 5,211 sq in = 434.25 sq ft/roll |
| Material subtotal | $705.36 |
| Freight | $124.66 |
| Total paid | $830.02 |
| **Cost per roll** | $830.02 ÷ 8 = **$103.7525/roll** |
| **Cost per sq ft** | $103.7525 ÷ 434.25 sq ft = **$0.2389/sq ft** |
| Cost per MSI | $103.7525 ÷ (500.256 MSI total ÷ 8) = **$1.6592/MSI** |
| Cost per linear ft | $103.7525 ÷ 386 ft = **$0.2688/linear ft** |
| Cost per linear yd | $0.2688 × 3 = **$0.8063/linear yd** |

Prior rate: $0.98/sq ft — unreconciled (flagged in 2026-05-28 audit as FLAG 1, cost_per_msi inconsistency). $0.98/sq ft is retired — do NOT use in any future cost build.

---

### Pre-Edit Math Verification — All 10 Affected Items

Laminate consumption figures extracted from each item's Nesting and Material Cost section. Items 1230820, 1278930, 1245130 have only dollar costs documented — implied sq ft back-calculated at $old_lam / $0.98. Items 1082570, 1277970-series, 3017583, 3017584 have explicit sq ft.

**Method for items with only dollar cost:** implied sq ft = documented_cost / $0.98/sq ft

| P/N | Lam sq ft source | Lam sq ft | Old lam cost | New lam cost (× $0.2389) | Old total | New total | Old margin (qty 20) | New margin (qty 20) |
|-----|-----------------|-----------|-------------|--------------------------|-----------|-----------|---------------------|---------------------|
| 1230820 | Back-calc: $1.02/$0.98 | 1.041 sq ft | $1.02 | 1.041 × $0.2389 = $0.2487 ≈ **$0.25** | $4.00 | $4.00 − $1.02 + $0.25 = **$3.23** | ~80% ($16.77/$20) | ~84% ($16.77/$20) |
| 1278930 | Back-calc: $0.85/$0.98 | 0.867 sq ft | $0.85 | 0.867 × $0.2389 = $0.2071 ≈ **$0.21** | $3.63 | $3.63 − $0.85 + $0.21 = **$2.99** | ~88% ($26.37/$30) | ~90% ($27.01/$30) |
| 1245130 | Back-calc: $1.15/$0.98 | 1.173 sq ft | $1.15 | 1.173 × $0.2389 = $0.2802 ≈ **$0.28** | $6.03 | $6.03 − $1.15 + $0.28 = **$5.16** | ~88% ($43.97/$50) | ~90% ($44.84/$50) |
| 1082570 | Explicit: 0.503 sq ft | 0.503 sq ft | $0.49 | 0.503 × $0.2389 = $0.1202 ≈ **$0.12** | $1.70 | $1.70 − $0.49 + $0.12 = **$1.33** | ~79% ($6.30/$8) | ~83% ($6.67/$8) |
| 1277970–1278000 | Explicit: 2.8125 sq ft (whole 20-label job) | 2.8125 sq ft | $2.76 | 2.8125 × $0.2389 = $0.6721 ≈ **$0.67** | $6.94 job | $6.94 − $2.76 + $0.67 = **$4.85** job | N/A (one-off) | N/A |
| 1277970–1278000 per label | $4.85 ÷ 20 | — | $0.35/label | — | — | **$0.24/label** | — | — |
| 3017583 | Explicit: 0.5 sq ft (whole 6-label job) | 0.5 sq ft | $0.49 | 0.5 × $0.2389 = $0.1195 ≈ **$0.12** | $1.70 job | $1.70 − $0.49 + $0.12 = **$1.33** job | N/A (one-off) | N/A |
| 3017583 per label | $1.33 ÷ 6 | — | $0.28/label | — | — | **$0.22/label** | — | — |
| 3017584 | Explicit: 0.20 sq ft (whole 6-label job) | 0.20 sq ft | $0.20 | 0.20 × $0.2389 = $0.0478 ≈ **$0.05** | $0.50 job | $0.50 − $0.20 + $0.05 = **$0.35** job | N/A (one-off) | N/A |
| 3017584 per label | $0.35 ÷ 6 | — | $0.08/label | — | — | **$0.06/label** | — | — |

**Verification:**
- 1230820: ($20 − $3.23)/$20 = $16.77/$20 = 83.85% ≈ ~84% ✓
- 1278930: ($30 − $2.99)/$30 = $27.01/$30 = 90.0% ≈ ~90% ✓
- 1245130: ($50 − $5.16)/$50 = $44.84/$50 = 89.7% ≈ ~90% ✓
- 1082570: ($8.00 − $1.33)/$8.00 = $6.67/$8.00 = 83.4% ≈ ~83% ✓

No prices changed. All margin improvements are a direct result of the corrected laminate cost — the price structure is unchanged.

---

### Files Updated

| File | Change |
|------|--------|
| `materials/1mil-polyester-overlaminate.md` | Added manufacturer/product_code/roll dimensions/cost_per_roll; updated cost_per_sq_ft ($0.98→$0.2389), cost_per_msi ($1.41→$1.6592); added cost_per_linear_ft/yd; verified_date→2026-05-28 |
| `governance/PRODUCTION.md` | Laminate row updated; Material Cost Quick Reference updated for all lam-affected figures |
| `items/1230820.md` | material_cost_per_unit: 4.00→3.23; margin_at_qty_20: ~80%→~84%; Nesting lam line/total updated; Margin Analysis table updated; cost_version_date→2026-05-28 |
| `items/1278930.md` | material_cost_per_unit: 3.63→2.99; margin_at_qty_20: ~88%→~90%; Nesting lam line/total updated; Margin Analysis table updated; cost_version_date→2026-05-28 |
| `items/1245130.md` | material_cost_per_unit: 6.03→5.16; margin_at_qty_20: ~88%→~90%; Nesting lam line/total updated; Margin Analysis table updated; cost_version_date→2026-05-28 |
| `items/1277970.md` | material_cost_per_unit: 0.35→0.24; cost_version_date→2026-05-28; Nesting lam line/totals updated |
| `items/1277980.md` | material_cost_per_unit: 0.35→0.24; cost_version_date→2026-05-28; Nesting lam line/totals updated |
| `items/1277990.md` | material_cost_per_unit: 0.35→0.24; cost_version_date→2026-05-28; Nesting lam line/totals updated |
| `items/1278000.md` | material_cost_per_unit: 0.35→0.24; cost_version_date→2026-05-28; Nesting lam line/totals updated |
| `items/3017583.md` | material_cost_per_unit: 0.28→0.22; cost_version_date→2026-05-28; Nesting lam line/totals updated |
| `items/3017584.md` | material_cost_per_unit: 0.08→0.06; cost_version_date→2026-05-28; Nesting lam line/totals updated |
| `categories/printed-laminated-orajet.md` | Singles profile: material cost/sq ft, margin at qty 20, margin floor updated; Kits profile: per-label material cost, margins updated |
| `.claude/ARCHITECTURE.md` | Margin columns updated for all printed/laminated items |
| `.claude/STATE.yml` | last_session updated |

**No prices changed. No frontmatter price, status, override_type, pricing_logic, or benchmark_item modified.**

---

### Validator

`python scripts/validate.py` — **PASS: 0 errors, 0 warnings** (post-update)
