# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> Last Updated: 2026-06-01

---

### 2026-06-01 — System: Added scripts/build_calculator_config.py — Generates frontend/calculator_config.json

**What:** Created a third build script following the established `build_frontend.py` / `build_materials.py` pattern. Reads governance documents, category files, item frontmatter, and material frontmatter; emits `frontend/calculator_config.json` as the single source of truth for the calculator's logic. The HTML calculator never hardcodes constants — pricing rules change → re-run script → fresh config.

**What's in the JSON:**

- `account` — floor ($55), floor_source_pn (1230820), MOQ rules for printed/laminated vs cut vinyl
- `routing` — sq ft thresholds (tiny/sub-scope/singles), laminator 13.5", Roland 28", parity max lam passes
- `bands` — cut_vinyl_lettering (concession + AI consensus + active band selector, margin targets, tier compression, default tier template, snap granularity), printed_laminated_singles (band $15.43–$15.91/sq ft, tier ratios, snap granularity), printed_laminated_kits (per-label $10 parity, 3-label + 5-label tier templates, 6% kit premium)
- `material_constants` — orajet_3951, polyester_lam_1mil, transferrite_582u (cost_per_sq_ft + verified_date read live from materials/*.md)
- `cut_vinyl_colors` — cardinal_red, olympic_blue, white_24in, white_48in (cost_per_linear_yd + verified_date read live from materials/*.md; available_widths + roll_width hardcoded)
- `ink_rates` — low/medium/high/flood_coat/flood_coat_safety_red with placeholder + unverified flags
- `do_not_benchmark` — 8 P/Ns with reasons (1277970–1278000 outrigger program peers, 3017583/3017584 standalone tiny one-offs, 1210810 sub-scope single, 1082570 job-economics initial order)
- `override_type_precedent` — maps each of the 6 override types to precedent-setting status (per ARCHITECTURE.md)
- `quote_language` — required MOQ language verbatim, anchor line template, PMS caveat template, sub-scope note, rule 14 note, ink unverified note
- `flag_thresholds` — material staleness (180/365 days), margin stop/warn percentages, band tolerance

**Dynamic reads:**
- `account.floor` ← `items/1230820.md` frontmatter `first_article_price`
- `material_constants.*.cost_per_sq_ft` + `verified_date` ← `materials/{orajet-3951-white,1mil-polyester-overlaminate,transferrite-582u}.md`
- `cut_vinyl_colors.*.cost_per_linear_yd` + `verified_date` ← `materials/3m-180mc-{cardinal-red,olympic-blue,white-24in,white-48in}.md`

**Static constants:** Tier ratios, band thresholds, snap granularity, ink rates, do_not_benchmark list, override type precedent, quote language templates, flag thresholds. All named at the top of the script for easy governance updates.

**Files Modified:**
- `scripts/build_calculator_config.py` — CREATED
- `.github/workflows/build-frontend.yml` — added 3rd build step (after build_frontend.py and build_materials.py), added script to path filter, added `frontend/calculator_config.json` to git add line
- `frontend/calculator_config.json` — CREATED (build output, generated 2026-06-01)
- `.claude/STATE.yml` — last_session updated
- `.claude/PROGRESS.md` — this entry

**Verification:**
- `python scripts/build_calculator_config.py` → clean, prints "3 material constants, 3 bands, 8 do_not_benchmark items"
- Generated JSON is valid; spot-checked: floor=55.0, orajet verified_date=2026-04-22, cardinal_red cost_per_linear_yd=15.502, all 4 cut vinyl colors present, all 8 do_not_benchmark items present
- `python scripts/validate.py` → 0 errors, 0 warnings
- `python scripts/build_frontend.py` → clean (15 items)
- `python scripts/build_materials.py` → clean (7 materials)

**Key Decisions:**
- No item files, category files, governance docs, or `index.html` were touched in this session. Config-only.
- Material costs and verified_date fields are read dynamically — the materials/*.md files remain the upstream source of truth. Updating a verified_date in a material file → regenerates the config on next run, no script change needed.
- All other constants (band thresholds, tier ratios, etc.) are explicit named constants at the top of the script. When governance docs change, edit the script's named constants to match — single, obvious update location.

**Status:** Complete. CI workflow will rebuild calculator_config.json automatically on next push that touches items, materials, or any of the three build scripts.

---

### 2026-06-01 — Maintenance: Resolved Audit Flags J-1 through J-5 — Olympic Blue Rename, White-48in Material Created, COMPLETION_TEMPLATES Ref Fixed, Dangling References Cleared

**What:** Pre-existing audit identified five flags unrelated to any recent pricing session. All five resolved in this session. No prices changed. No item statuses changed. No margin figures changed.

**Flags Resolved:**

- **J-1 (COMPLETION_TEMPLATES.md reference):** `.claude/COMPLETION_TEMPLATES.md` exists. MASTER_CONTEXT.md Core Rule #5 referenced bare `COMPLETION_TEMPLATES.md` — updated to `.claude/COMPLETION_TEMPLATES.md`. README.md had the same ambiguous reference — also updated. MASTER_CONTEXT.md file map updated to include the `materials/` directory (was absent).
- **J-2 (missing materials/3m-180mc-olympic-blue.md):** Resolved by J-4 fix. File now exists with correct data.
- **J-3 (missing materials/3m-180mc-white-48in.md):** Created with verified data from `governance/PRODUCTION.md` — cost_per_roll: 257.44, cost_per_linear_yd: 25.744, cost_per_sq_ft: 2.15, verified_date: 2026-05-21.
- **J-4 (wrong data in incorrectly-named material file):** File was created under the wrong color name. Renamed to `materials/3m-180mc-olympic-blue.md`. Fixed: material_id → "3m-180mc-olympic-blue", color_name → "Olympic Blue", color_code 37 → 57. product_code 180mC-57 and all cost fields were already correct.
- **J-5 (dangling references in transferrite-582u.md):** `transferrite-582u.md` compatible_cut_vinyls already listed the correct IDs ("3m-180mc-olympic-blue" and "3m-180mc-white-48in") — the files simply didn't exist yet. Resolved by J-3 + J-4. All four compatible_cut_vinyls now resolve to existing files.

**Files Modified:**
- `materials/3m-180mc-[wrong-name].md` — DELETED (incorrectly-named file replaced by olympic-blue.md)
- `materials/3m-180mc-olympic-blue.md` — CREATED (renamed and corrected: material_id, color_name, color_code fixed)
- `materials/3m-180mc-white-48in.md` — CREATED (new file, verified data from PRODUCTION.md)
- `.claude/MASTER_CONTEXT.md` — Core Rule #5 path corrected; file map updated to include materials directory
- `README.md` — COMPLETION_TEMPLATES.md reference updated to `.claude/COMPLETION_TEMPLATES.md`
- `.claude/PROGRESS.md` — this entry
- `.claude/STATE.yml` — last_session updated, material_count 6→7, next_action prepended with maintenance session completion note
- `frontend/materials.json` — rebuilt via build_materials.py (7 materials; incorrectly-named entry replaced by 3m-180mc-olympic-blue)

**Key Decisions:**
- No pricing changes of any kind. These are documentation and file structure fixes only.
- material_count incremented from 6 to 7 (added white-48in).
- All other STATE.yml fields unchanged — next_action quote to Sean preserved as primary next action.

**Status:** Complete. validate.py 0 errors, 0 warnings. build_frontend.py clean. build_materials.py clean (7 materials).

---

### 2026-06-01 — Pricing Revision + Governance Update: P/N 1210810 — Never-Pay-More Cliff Eliminated, $55 Flat MOQ Floor, $4.75 at 10-19, Account-Level MOQ 10 + $55 Minimum Order Charge Rules Codified

**What:** Revised tier structure on P/N 1210810 (LBL - DANGER FALLING JIB) to eliminate the never-pay-more cliff at the 1-9/10-19 boundary. New 1-9 = $55.00 flat minimum order charge (NOT per-unit). New 10-19 = $4.75. Initial order updated to $47.50. Established permanent account-level MOQ 10 and $55 minimum order charge rules for all printed/laminated items. Invoice protection language codified.

**Cliff Problem Eliminated:**
- Prior: 9 × $8.50 = $76.50 vs 10 × $5.00 = $50.00 → buyer ordering 9 paid $26.50 MORE than buyer ordering 10. Indefensible.
- New: 1-9 = $55.00 flat (minimum order charge, not per-unit). 10-19 = $4.75. Never-pay-more verified: 19 × $4.75 = $90.25 ≈ 20 × $4.50 = $90.00 ✓

**Order History Finding:**
- Every catalog RFQ Sean has sent has been at qty 10 or qty 20.
- Sub-10 orders have exclusively been one-off field service situations (3017583, 3017584, outrigger program) — priced at $55 account floor, not catalog pricing situations.
- The 1-9 tier was a structural formality never used in practice for catalog orders.

**New Tier Structure (1210810):**

| Tier | Prior Price | New Price | Notes |
|------|------------|-----------|-------|
| 1-9 | $8.50/unit | **$55.00 flat** | Minimum order charge — NOT per-unit |
| 10-19 | $5.00/unit | **$4.75/unit** | Never-pay-more compliant |
| 20-49 | $4.50 | $4.50 | Unchanged — validated anchor |
| 50-99 | $3.50 | $3.50 | Unchanged |
| 100-199 | $2.75 | $2.75 | Unchanged |
| 200+ | $2.50 | $2.50 | Unchanged |

Initial order (qty 10): $47.50 (was $50.00).

**Account-Level Rules Established (Printed/Laminated Only):**
- MOQ 10: all new printed/laminated catalog items start at qty 10
- $55 minimum order charge on any order producing a total below $55.00, regardless of qty (flat total, not per-unit)
- Invoice protection: buyer never invoiced more for a smaller quantity than a larger quantity at the next tier
- Required quote language: "Minimum order for printed labels is 10 units. Orders below 10 units are subject to a $55.00 minimum order charge. You will never be invoiced more for a smaller quantity."
- Sub-10 handling: flat-rate $55.00 one-off (same as 3017583, 3017584, outrigger program)
- Cut vinyl items NOT subject to these rules at this time

**Files Modified:**
- `items/1210810.md` — price_1_9 8.50→55.00 flat (min order charge); price_10_19 5.00→4.75; pricing_logic updated; notes updated; Item Overview initial order $50→$47.50; Pricing section header, tier table, invoice protection, and quote language updated; Notes and Warnings: MOQ 10 block replaces No-MOQ block, initial order block updated; Pricing Derivation: Step 7 added documenting tier restructure decision, cliff problem, order history finding, never-pay-more verification, and MOQ 10 rationale
- `categories/printed-laminated-orajet.md` — 1210810 Singles table row updated; footnote ² updated to reflect new tier structure, MOQ 10, $55 min charge, invoice protection; new Account-Level Order Rules block added (Rules 1–5); Pricing Rules section: Rules 7–8 added (MOQ 10, invoice protection)
- `governance/PRICING_RULES.md` — §25–29 added under new "Printed/Laminated MOQ and Minimum Order Rules" section; Last Updated 2026-05-22→2026-06-01
- `.claude/MASTER_CONTEXT.md` — Core Rule #8 added (reference to Account-Level Order Rules); new "Account-Level Order Rules" section added (MOQ 10, $55 min charge, invoice protection, quote language template, sub-10 handling, cut vinyl exception, 2028 context, pricing normalization internal note); Last Updated 2026-05-22→2026-06-01
- `.claude/ARCHITECTURE.md` — 1210810 catalog row updated (1-9: $55 flat MOQ floor, 10-19: $4.75, initial order $47.50); precedent chain updated (tier restructure 2026-06-01 documented, never-pay-more compliance noted); Category Registry Printed + Laminated entry updated (MOQ 10 in effect noted)
- `.claude/PROGRESS.md` — this entry
- `.claude/STATE.yml` — last_session, next_action, blockers updated

**Key Decisions:**
- $55.00 flat on 1-9 is a minimum order charge, not a per-unit rate. Never treat, quote, or document it as per-unit.
- Invoice protection language is mandatory in every printed/laminated quote going forward.
- Cut vinyl items not affected — MOQ structure for cut vinyl will be addressed separately.
- 2028 MOQ plan: this session is the beginning of the formalization, not the end of it.
- Ink confirmation task (Safety Red flood coat, $0.25 placeholder, realistic $0.40–$0.50) preserved — mandatory post-production task.
- All prior 4-round AI validation history on 1210810 preserved in Pricing Derivation section.

**Status:** Complete. validate.py 0 errors, 0 warnings. build_frontend.py clean. Item file locked with revised pricing.

---

### 2026-06-01 — Pricing Lock: P/N 1210810 — LBL - DANGER FALLING JIB — 4-Round AI Validation Complete, $4.50 Qty 20-49, $2.50 200+, No-MOQ Documented, Ink Unverified Pending First Run, 2028 MOQ Plan Logged

**What:** Created and fully documented item file for P/N 1210810 (LBL - DANGER FALLING JIB) with validated, locked pricing. The 4-round, 6-model external AI validation (24 total model runs) was completed prior to this session. This session creates the item file with final validated pricing and propagates all changes to dependent files.

**Item Summary:**
- P/N: 1210810 | Description: LBL - DANGER FALLING JIB
- Type: Single printed/laminated ANSI Z535.1/Z535.4 DANGER label
- Dimensions: 10.5" × 4" = 0.292 sq ft
- Material: Orajet 3951 cast vinyl + 1-mil polyester overlaminate
- Content: Safety Red flood coat header, white DANGER text, white triangle/exclamation icon, two white field panels with black technical schematics, black body text, black border
- Drafter: DS / TJK, dated 09/2015
- Customer: Elliott Equipment Company (Sean Finn)
- Initial order: qty 10 → $50.00 (10-19 tier at $5.00)
- Projected volume: ~30/month starting 2027

**Validated Final Pricing — Nick Approved:**

| Tier | Price | $/Sq Ft |
|------|-------|---------|
| 1-9 | $8.50 | $29.11 |
| 10-19 | $5.00 | $17.12 |
| 20-49 | $4.50 | $15.41 |
| 50-99 | $3.50 | $11.99 |
| 100-199 | $2.75 | $9.42 |
| 200+ | $2.50 | $8.56 |

Material cost: $0.67/label at $0.25 ink (UNVERIFIED). Realistic ink range: $0.40–$0.50.

**4-Round Validation Summary:**

**Round 1 (Build — 6 models):** Vote split 3/3 on below-band positioning. 3 models identified inverted price-size reasoning as a structural error. Ink flagged as understated ($0.25 on a Safety Red flood coat). Tier application error identified: qty 10 incorrectly placed in 1-9 tier in preliminary brief. Proposed 20-49 range: $3.50–$5.50.

**Round 2 (Destruction — 6 models):** Verdict 5 No / 1 Yes-with-modifications. All 4 attack vectors rated High severity. Key: Buyer/Procurement (H) — 25% below-band positioning creates renegotiation trigger on entire account. Competitor (H) — $3.50 at 30/month is attackable. Cost Auditor (H) — $0.25 ink on Safety Red flood coat is unreliable. Strategic (H) — below-band introduction inverts price-size relationship and permanently lowers buyer's reference floor. Proposed 20-49: $4.00–$4.75.

**Round 3 (Buyer Simulation — 6 models):** All 6 approved $45.00 for qty 10. Pushback threshold on 20-49: $3.25–$4.25. $4.00–$4.50 cleared every model. Dimensions flagged as must-include in quote email (4 of 6 models). 30/month recurring volume is the structural anchor — initial order is noise.

**Round 4 (Final Synthesis — 6 models):** Vote: 0 Option A / 3 Option B / 3 Option C. Option A (preliminary) rejected unanimously. Option B ($4.50 at qty 20) adopted — account is in active partnership phase, band integrity outweighs friction avoidance. Universal finding: 10-19 at $5.50 puts qty 10 at $55.00 above approval threshold → consensus fix: drop to $5.00 ($50.00 for qty 10).

**Post-Validation Audit Findings:**
- Material cost corrected: $0.68 filed → $0.67 (rounding artifact, no pricing impact)
- 200+ tier: Option B produced $2.25; audit identified this falls below category margin floor at realistic ink ($0.40–$0.50). Nick's decision: raised to $2.50 (200+ orders not expected; tier exists for structural completeness only; warehouse caution documented)
- No existing items undermined: $/sq ft story clean across all three singles (1230820 at $15.43, 1082570 at $15.91, 1210810 at $15.41)
- Fundamental error corrected: preliminary used below-band dimensional scope to justify below-band $/sq ft — backwards reasoning. $4.50 corrects this at $15.41/sq ft (essentially the band floor)

**Margin at 20-49 (recurring tier) across ink scenarios:**
- At $0.25 ink ($0.67 total): 85.1%
- At $0.40 ink ($0.82 total): 81.8%
- At $0.50 ink ($0.92 total): 79.6%

**Margin at 200+ across ink scenarios:**
- At $0.25 ink: 73.2%
- At $0.40 ink: 67.2%
- At $0.50 ink: 63.2% (at or near floor — intentional, Nick's decision)

**Strategic Decisions Documented:**
- **No MOQ:** Permanent account-level rule. Consistent with all Elliott items.
- **2028 MOQ plan:** Nick's deliberate strategic decision to introduce MOQ structure beginning January 1, 2028. Business justification: COGS and overhead increases. Not an omission — a planned future action.
- **Ink confirmation task:** Must confirm Safety Red flood coat ink cost after first production run. $0.25 is a placeholder. Do not assume a number — wait for production data.
- **Quote email anchor line (validated Round 4):** "Label measures 10.5" × 4" (0.292 sq ft) in cast vinyl with polyester overlaminate — priced at $4.50 at your projected monthly volume."
- **Pricing normalization note (internal only):** Current band ($15.43–$15.91/sq ft) is a relationship concession below industry standard (~$18–$22/sq ft). Nick's plan to normalize toward industry standard by January 1, 2027. Internal context for future sessions only — do not surface to buyer.
- **Dimensional scope exclusion:** 1210810 at 0.292 sq ft is excluded from singles band DATA POINTS on dimensional scope (below ~0.5 sq ft floor). Exclusion is dimensional, NOT pricing — the validated rate is band-consistent. Not added to band until production-volume acceptance confirmed by Nick.

**Files Updated:**
- `items/1210810.md` — new item file with all required frontmatter and all 10 required sections; complete 4-round validation record; full margin analysis at all 3 ink scenarios
- `categories/printed-laminated-orajet.md` — added 1210810 row to Singles table with footnote ²; updated Pricing Profile band scope note to document 0.1–0.5 sq ft sub-scope item handling
- `.claude/ARCHITECTURE.md` — added 1210810 to catalog (item count 14 → 15); Printed + Laminated count 10 → 11; added 1210810 to precedent chain; Last Updated 2026-05-28 → 2026-06-01
- `.claude/STATE.yml` — item_count 14 → 15; last_session and next_action updated
- `.claude/PROGRESS.md` — this entry
- `materials/orajet-3951-white.md` — added 1210810 to used_in_items
- `materials/1mil-polyester-overlaminate.md` — added 1210810 to used_in_items

**Status:** Complete. validate.py 0 errors, 0 warnings. build_frontend.py clean. Item file locked with validated pricing.

---

### 2026-05-29 — Documentation Audit Fix: FLAG 1 (cost_per_msi) + FLAG 2 (Cardinal Red derivation note)

**What:** Two documentation-only fixes to material files identified in the 2026-05-28 full pricing integrity audit. No prices changed. No item files changed. No category files changed. No margins changed.

**FLAG 1 — `materials/1mil-polyester-overlaminate.md` — `cost_per_msi`:**
Field was already correct at `1.6592` when this session began — no change needed. The prior audit flagged `cost_per_msi: 1.41` as inconsistent with `cost_per_sq_ft: 0.2389` (1 MSI = 1000 sq in = 6.944 sq ft → $0.2389/sq ft × 6.944 = $1.6592/MSI). That fix was already applied (likely during the 2026-05-28 laminate cost update session). Session brief confirmed the target value as `1.6592`; file already matched. No edit made to this file.

**FLAG 2 — `materials/3m-180mc-cardinal-red.md` — `notes` field derivation clarification:**
Added explanation to the `notes` field documenting that `cost_per_sq_ft: 7.751` for Cardinal Red is derived as `cost_per_linear_yd / roll_width_ft` ($15.502 / 2 ft = $7.751/sq ft) — the length-based method — not the area method used by other 180mC color files (Olympic Blue, White). This is intentional: item pricing uses the length-based method directly, so `cost_per_sq_ft` reflects that same basis. Numeric value unchanged at `7.751`.

**Files Updated:**
- `materials/3m-180mc-cardinal-red.md` — `notes` field updated (derivation explanation added; no numeric values changed)
- `.claude/STATE.yml` — last_session and next_action updated
- `.claude/PROGRESS.md` — this entry

**Files Confirmed Unchanged:**
- `materials/1mil-polyester-overlaminate.md` — FLAG 1 already correct; no edit made
- All item files — no changes
- All category files — no changes
- `governance/ARCHITECTURE.md` — no changes

**Status:** Complete. validate.py 0 errors, 0 warnings. build_materials.py clean (6 materials).

---

### 2026-05-28 — Audit: Cut Vinyl Margin Revalidation — Stale Prose References Corrected

**What:** Post-material-cost-update audit of all cut vinyl item files and supporting files. Verified that all margin figures, material costs, and cross-references are internally consistent following the 2026-05-28 material cost update session (Cardinal Red + TransferRite both changed).

**Margin Comparison Table:**

| P/N | Pre-Correction Margin | Post-Correction Margin | ARCH ✓ | Category ✓ | Frontmatter ✓ | Nesting Section ✓ | Margin Analysis ✓ |
|-----|----------------------|------------------------|--------|-----------|--------------|------------------|------------------|
| 1205720 | ~78% | ~75% | ✓ | ✓ | ✓ | ✓ | ✓ |
| 1186310 | ~78% | ~75% | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3017435 | ~76% / ~81% | ~73% / ~78% | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3018378 | ~78% | ~75% | ✓ | ✓ | ✓ | ✓ | ✓ |

**Stale reference search:**
- `$0.18` tape cost anywhere in repo: **0 instances** — fully cleaned in prior session ✓
- `$2.56/sq ft` as Cardinal Red vinyl cost anywhere in repo: **0 instances** in data sections ✓
- `~80%` on cut vinyl items at qty 20: **0 instances** ✓

**Stale prose references found and corrected (5 instances, 2 files):**

1. `items/3017435.md` — `pricing_logic` frontmatter: old costs "$8.46 on 24\", $6.74 on 48\"" → **"$9.51 on 24\", $7.79 on 48\""**
2. `items/3017435.md` — `notes` frontmatter: "Material cost drops from $8.46 to $6.74 on 48\" stock" → **"Material cost: $9.51 on 24\" stock, $7.79 on 48\" stock"**
3. `items/3018378.md` — `pricing_logic` frontmatter: "material cost ($7.88 vs $7.01)" → **"material cost per label ($8.92 vs $8.74)"**
4. `items/3018378.md` — Pricing Derivation section: stale "$7.88 vs $7.01. This reduces margin by ~2 points at qty 20 (78% vs 80%)" → **updated to reflect current $8.92 vs $8.74, both ~75% at qty 20**
5. `items/3018378.md` — Notes and Warnings: stale reference to "P/N 1205720 used the label-area method ($6.55 = 2.56 sq ft × $2.56/sq ft)" → **corrected to document the historical error accurately without carrying the stale $2.56/sq ft cost figure as a live calculation**

**Also corrected:**
- `.claude/ARCHITECTURE.md` — `Last Updated` date was still 2026-05-22 after the prior session updated the margin columns; corrected to **2026-05-28**

**Files Updated:**
- `items/3017435.md` — pricing_logic and notes frontmatter fields updated (old costs → new costs)
- `items/3018378.md` — pricing_logic frontmatter, Pricing Derivation section, Notes and Warnings section updated
- `.claude/ARCHITECTURE.md` — Last Updated date corrected
- `.claude/STATE.yml` — last_session and next_action updated
- `.claude/PROGRESS.md` — this entry

**Status:** Complete. All 4 cut vinyl items fully in sync — margins, material costs, and all prose references consistent. validate.py 0 errors, 0 warnings. build_frontend.py and build_materials.py rebuilt.

---

### 2026-05-28 — Material Cost Update: Cardinal Red 24"×50yd $775.10 + TransferRite 582U 24"×100yd $118.21 — Margins Recalculated on 4 Cut Vinyl Items

**What:** Two material cost changes. (1) 3M Controltac 180mC-53 Cardinal Red roll size changed from 24"×10yd at $153.60 to 24"×50yd at $775.10 — roll width unchanged, only length and price changed. Cardinal Red only; all other 180mC colors unchanged. (2) TransferRite Ultra 582U application tape changed from 30"×100yd at $135.06 to 24"×100yd at $118.21 — tape width now matches vinyl roll width exactly at 24", eliminating prior 6" overhang. This applies to all cut vinyl items on the account.

**New Material Costs (Nick confirmed — not recalculated):**

| Material | Old Roll | Old $/yd | Old $/sq ft | New Roll | New $/yd | New $/sq ft |
|----------|----------|----------|-------------|----------|----------|-------------|
| Cardinal Red 3M 180mC-53 | 24"×10yd $153.60 | $15.360 | $7.680 | 24"×50yd $775.10 | $15.502 | $7.751 |
| TransferRite Ultra 582U | 30"×100yd $135.06 | $1.3506 | $0.5402 | 24"×100yd $118.21 | $1.1821 | $0.5911 |

**Full Nesting Math — All 4 Affected Items:**

---

**P/N 1205720 — E190 Cardinal Red (Cardinal Red vinyl + tape both change)**

Nesting (from existing item file):
- 2 labels across 24" roll (11" + 11" = 22" — 2" waste strip)
- Label length: 33.5625" = 0.9323 yd
- Labels per roll: 20 (2 across × 10 positions down 360" roll)

Vinyl cost (new $15.502/yd):
- Row cost: 0.9323 yd × $15.502/yd = $14.452
- Per label: $14.452 ÷ 2 = **$7.226** (was $7.16)

Tape cost (new $0.5911/sq ft):
- Label area: 2.56 sq ft
- Tape cost: 2.56 × $0.5911 = **$1.513** (was $0.46)

Total: $7.226 + $1.513 = $8.739 → **$8.74** (was $7.62, Δ +$1.12)
Margin at qty 20: ($35 − $8.74) ÷ $35 = $26.26 ÷ $35 = **~75%** (was ~78%)

---

**P/N 1186310 — E160 Cardinal Red (Cardinal Red vinyl + tape both change)**

Nesting (from existing item file — dimensions identical to 1205720):
- 2 labels across 24" roll (11" + 11" = 22")
- Label length: 33.5625" = 0.9323 yd

Vinyl cost (new $15.502/yd):
- Row cost: 0.9323 yd × $15.502/yd = $14.452
- Per label: $14.452 ÷ 2 = **$7.226** (was $7.16)

Tape cost (new $0.5911/sq ft):
- Label area: 2.564 sq ft (3-decimal precision)
- Tape cost: 2.564 × $0.5911 = **$1.516** (was $0.46)

Total: $7.226 + $1.516 = $8.742 → **$8.74** (was $7.62, Δ +$1.12)
Margin at qty 20: ($35 − $8.74) ÷ $35 = **~75%** (was ~78%)

---

**P/N 3017435 — ELLIOTT White (tape only — White vinyl costs unchanged)**

Nesting 24" roll (from existing item file):
- 2 labels across (8.38" + 8.38" = 16.76" ≤ 24")
- Label length: 43.91" = 1.22 yd

Vinyl cost (White, $13.116/yd — unchanged):
- Row cost: 1.22 × $13.116/yd = $16.002; ÷ 2 = **$8.00** (unchanged)

Tape cost (new $0.5911/sq ft):
- Label area: 2.56 sq ft
- Tape cost: 2.56 × $0.5911 = **$1.513** (was $0.46)

Total (24" roll): $8.00 + $1.513 = **$9.513 → $9.51** (was $8.46, Δ +$1.05)
Margin at qty 20 (24" roll): ($35 − $9.51) ÷ $35 = $25.49 ÷ $35 = **~73%** (was ~76%)

Nesting 48" roll (from existing item file):
- 5 labels across (8.38" × 5 = 41.9" ≤ 48")
- Label length: 43.91" = 1.22 yd

Vinyl cost (White 48", $25.744/yd — unchanged):
- Row cost: 1.22 × $25.744/yd = $31.407; ÷ 5 = **$6.28** (unchanged)

Tape cost: 2.56 × $0.5911 = **$1.513** (same label area)

Total (48" roll): $6.28 + $1.513 = **$7.793 → $7.79** (was $6.74, Δ +$1.05)
Margin at qty 20 (48" roll): ($35 − $7.79) ÷ $35 = $27.21 ÷ $35 = **~78%** (was ~81%)

---

**P/N 3018378 — D115 Olympic Blue (tape only — Olympic Blue vinyl cost unchanged)**

Nesting (from existing item file):
- 2 labels across 24" roll (11" + 11" = 22")
- Label length: 32.88" = 0.9133 yd

Vinyl cost (Olympic Blue, $16.278/yd — unchanged):
- Row cost: 0.9133 × $16.278/yd = $14.867; ÷ 2 = **$7.43** (unchanged)

Tape cost (new $0.5911/sq ft):
- Label area: 2.512 sq ft
- Tape cost: 2.512 × $0.5911 = **$1.485** (was $0.45)

Total: $7.43 + $1.485 = $8.915 → **$8.92** (was $7.88, Δ +$1.04)
Margin at qty 20: ($35 − $8.92) ÷ $35 = $26.08 ÷ $35 = **~75%** (was ~78%)

---

**Margin Flag Check:** All margins at qty 20 remain well above 60%. No price changes needed or recommended. No flags.

**Material cost per sq ft — new band:** $3.04–$3.72 (vinyl + tape combined)
**Margin band — new range:** ~73–78% at qty 20

**Files Updated:**
- `materials/3m-180mc-cardinal-red.md` — roll_length_yd 10→50, cost_per_roll 153.60→775.10, cost_per_linear_yd 15.36→15.502, cost_per_sq_ft 2.56→7.751, verified_date 2026-05-28
- `materials/transferrite-582u.md` — roll_width_in 30→24, cost_per_roll 135.06→118.21, cost_per_sq_ft 0.18→0.5911, added cost_per_linear_yd 1.1821, verified_date 2026-05-28
- `governance/PRODUCTION.md` — Cardinal Red row updated, TransferRite row updated, process improvement note added (tape width = vinyl width, no overhang), quick reference section updated for all 4 items
- `items/1205720.md` — material_cost_per_unit 7.62→8.74, cost_version_date, margin_at_qty_20 ~78%→~75%, Material Specification, Nesting and Material Cost, Margin Analysis sections updated
- `items/1186310.md` — material_cost_per_unit 7.62→8.74, cost_version_date, margin_at_qty_20 ~78%→~75%, Material Specification, Nesting and Material Cost, Margin Analysis sections updated
- `items/3017435.md` — material_cost_per_unit 8.46→9.51, cost_version_date, margin_at_qty_20 ~76%/~81%→~73%/~78%, Material Specification, Nesting and Material Cost, Margin Analysis sections updated
- `items/3018378.md` — material_cost_per_unit 7.88→8.92, cost_version_date, margin_at_qty_20 ~78%→~75%, Material Specification, Nesting and Material Cost, Margin Analysis sections updated
- `categories/cut-vinyl-3m-180mc.md` — Pricing Profile material cost band $6.74–$8.46→$7.79–$9.51, margin band ~76–78%→~73–78%, margin floor note updated
- `.claude/ARCHITECTURE.md` — margin columns updated for all 4 cut vinyl items
- `.claude/STATE.yml` — last_session and next_action updated
- `.claude/PROGRESS.md` — this entry

**Status:** Complete. validate.py 0 errors, 0 warnings. build_frontend.py and build_materials.py rebuilt.

---

### 2026-05-28 — Pricing Lock: P/N 1082570 — $42 Flat Qty 2, Validated Tiers, 4-Round AI Validation Complete, Color Conflict Pending (Samples Delivered)

**What:** Post-validation pricing lock for P/N 1082570 (Load Chart Label, I70 EZR Mount 3.6K). The 4-round, 6-model AI validation process (24 total model runs) was completed following the initial quote session. This session locks the validated pricing into the item file and all dependent files.

**Validation Summary:**

**Round 1 (Build — 6 models):** Qty 2 consensus $38–$45 cluster. Qty 20 consensus $8.50–$11.00. All 6 rejected $55 floor for this label size vs D105 comparison. All 6 agreed setup-recovery logic applies to the current order.

**Round 2 (Destruction — 6 models):** All 6 found $55 floor indefensible at 0.503 sq ft vs D105. All 6 identified 20-49 tier as most competitively exposed. All 6 recommended Option B (job economics) over Option A ($55 floor). Consensus qty 2: $40–$42. Consensus 20-49 tier: $7.25–$8.50/label. Consensus 1-9 tier: $14–$18/label (one model recommended $16.50 — noted for Round 4).

**Round 3 (Buyer Simulation — 6 models):** 5 of 6 approved $42 for qty 2 without question (instant approval below $50–$100). D105 delta at qty 20: +3% ($15.91 vs $15.43/sq ft) — every model called it a non-issue. Job economics framing was the single most cited approval driver. 1 outlier at $24–$26 rejected (ignores setup recovery).

**Round 4 (Final Synthesis — 6 models):** 5 of 6 unanimous: send as shown. 1 model recommended bumping 1-9 from $16.00 → $16.50 to widen the gap at low quantities — adopted. No MOQ — Nick's decision, permanent account-level rule.

**Validated Pricing Locked:**
- Current order (qty 2, SO 20125600): **$42.00 flat** — job economics framing (setup recovery), NOT a per-label rate, NOT a floor-anchored price
- Tiers: 1-9: $16.50 / 10-19: $10.50 / 20-49: $8.00 / 50-99: $6.25 / 100-199: $5.25 / 200+: $4.25
- No MOQ — permanent account-level rule

**Key Decisions:**
- **Option A ($55 floor) rejected.** Indefensible at 0.503 sq ft vs D105 comparison. All 6 models in Round 2 rejected it.
- **Option B ($42 flat) adopted.** Job economics / setup recovery framing. 5 of 6 models in Round 3 approved without question.
- **$16.50 for 1-9 tier** adopted on Round 4 model recommendation — widens gap between current-order flat price and low-end catalog tier.
- **200+ at $4.25** ($8.45/sq ft) intentionally below D105 anchor ($15.43/sq ft) — volume reward for strategic account. 60% margin is below standard category minimum (~64%) by design.
- **No MOQ.** Elliott is a strategic account; access at any quantity is intentional and permanent.

**Color Conflict Update (Status Unchanged — Open):**
- Nick sent Sean physical samples of both versions (black on white per artwork; Safety Yellow per drawing note 6)
- Samples delivered within **~26 hours** of the request
- Sean has not confirmed which version he wants; PO not received
- Pricing assumes Safety Yellow (conservative); production blocked pending selection

**Strategic Account Development Note:**
Sean's response to the sample delivery included a request for Nick to suggest what specs to call out on a drawing for label/decal procurement. More significantly, Sean and his manager are initiating a project to develop an **engineering and procurement standard for labels/decals at Elliott Equipment**. They will reach out to Nick for input. Documented in item file Notes and Warnings.

**Files Updated:**
- `items/1082570.md` — frontmatter: prices updated (16.50/10.50/8.00/6.25/5.25/4.25), pricing_logic and notes updated; Pricing section: $42 flat current order, tier table updated; Pricing Derivation: PENDING removed, Step 3 labeled pre-validation, Step 4 rewritten (Option A/B + full 4-round validation), Step 6 updated to $42; Margin Analysis: tier table and one-off order section updated; Notes and Warnings: color conflict updated (samples delivered), current order section rewritten ($42/job-economics/no-MOQ), AI VALIDATION COMPLETE section added, strategic account development note added
- `categories/printed-laminated-orajet.md` — 1082570 footnote updated (AI validated, $42 flat, no MOQ); Pricing Profile singles data points note updated
- `.claude/ARCHITECTURE.md` — 1082570 catalog row updated (samples delivered, $42 job economics); category registry Profile Status updated; precedent chain updated
- `.claude/STATE.yml` — last_session and next_action updated
- `.claude/PROGRESS.md` — this entry

**Status:** Pricing locked. Ready to quote $42.00 flat to Sean when PO arrives. Awaiting: (1) Sean's color selection via PO; (2) Sean's outreach re: engineering/procurement standard project. validate.py passes 0 errors, 0 warnings.

---

### 2026-05-28 — New Item: P/N 1082570 — Load Chart Label, I70 EZR Mount 3.6K (Singles Band, Qty 2 One-Off, Safety Yellow Assumed, Color Conflict Pending)

**What:** Priced and documented P/N 1082570 — a single 10" × 7.25" (0.503 sq ft) crane operation load chart label for the Elliott I70 (75") model. Material: Orajet 3951 cast vinyl + 1-mil polyester overlaminate ("1 mil clear Mylar overlay" on drawing — Mylar = polyester trade name). Drawing dated 08-25-04 (R.M.W./KML). No dimensions on drawing — confirmed by Derrik Walton, P.E., Engineering Manager at Elliott Equipment, via email 2026-05-28, referencing I50 chart as size standard.

**Item Created:** `items/1082570.md`

**Pricing:** Production tier table anchored to singles band ($8/label at qty 20 = $15.91/sq ft). Current order (qty 2, SO 20125600) floor-anchored at $55 total ($27.50/label) — specific I70 unit shipping, urgent. No first article.

**Production tier table:**
- 1-9: $12 / 10-19: $10 / 20-49: $8 / 50-99: $7 / 100-199: $6 / 200+: $5

**Job economics (current order, qty 2):**
- Material cost: 2 × $1.70 = $3.40 (Safety Yellow flood coat assumption)
- File prep: $0 (account rule — Elliott provides production-ready DWG, `PRICING_RULES.md` §22)
- Production time: ~20-25 min
- Program total: $55.00
- Contribution margin: ~94% (structural — one-off floor pricing)

**Key Decisions:**
- **Singles band applied.** At 0.503 sq ft, 1082570 is at the low end of the singles scope (~0.5–2.0 sq ft). Band rate: 0.503 × $15.43 = $7.76 → $8 at qty 20 ($15.91/sq ft, within ±15% of band center). Production tiers proportioned from 1230820 tier ratios.
- **$55 floor applies to the current order (qty 2).** At the production tier 1-9 rate ($12/label), qty 2 = $24 — below the $55 minimum-worthwhile-charge threshold. Floor applied consistently with all prior one-off small-run precedents. Production tier table is valid for reorder volumes.
- **Floor price does NOT contaminate the singles band.** $27.50/label (=$54.67/sq ft implied) is an arithmetic artifact of the $55 floor at qty 2. It is explicitly excluded from band calculations.
- **Safety Yellow flood coat assumed (open color conflict):** Drawing note 6 specifies Safety Yellow background; artwork shows white background. These are in direct conflict. Nick will send Sean mockups of both versions; Sean selects via PO. Pricing assumes Safety Yellow (higher ink coverage, conservative — $0.60/label ink vs ~$0.25 for black-on-white). If Sean selects black-on-white: pricing holds, margin improves ~4 points. Under no circumstances produce without Sean's color selection.
- **Material cost $1.70/label (Safety Yellow assumption):** vinyl $0.61 + lam $0.49 + flood coat ink $0.60.
- **Margin at qty 20:** ~79% (band target). Floor at 200+: ~66% (above category minimum ~64%).
- **No first article** — not requested, not offered. One-off tied to specific ship order.
- **Multi-round AI validation pending** — Nick will run separately. Pricing methodology is established (singles band scaling + account floor); no novel element requiring pre-validation.
- **Singles Pricing Profile band tightening:** 1082570 adds a second band-consistent calibration point at the opposite end of the singles scope (0.503 vs 1.296 sq ft). Both land within 3% per-sq-ft ($15.43 vs $15.91). Band is converging. Tightening deferred pending production-volume acceptance.
- **Mylar terminology documented** as polyester trade name (consistent with 3017584 note).
- **200+ tier set at $5 (not $4):** Proportional calculation gives $4.40 → $4, but at $1.70 material, $4 yields ~59% margin (below ~64% category floor). Rounded up to $5 to maintain ~66% at the floor tier.

**Files Updated:**
- `items/1082570.md` — new item file with all required frontmatter and all 10 required sections
- `categories/printed-laminated-orajet.md` — added 1082570 to singles catalog table with floor-anchoring footnote; updated Pricing Profile singles section (1 confirmed → 2 data points note, band tightening deferred)
- `.claude/ARCHITECTURE.md` — added 1082570 to catalog; updated Printed + Laminated count 9 → 10; added singles band precedent chain entry; updated category registry Profile Status
- `.claude/STATE.yml` — incremented item_count 13 → 14; last_session and next_action updated
- `.claude/PROGRESS.md` — this entry

**Status:** Quoted. $55 total for qty 2 (SO 20125600). Urgent — specific I70 unit shipping. Pending: (1) Sean's color version selection (Safety Yellow vs white background); (2) multi-round AI validation (Nick's separate session). `validate.py` passes 0 errors, 0 warnings.

---

### 2026-05-27 — New Item: P/N 3017584 — LBL - PTO Active (One-Off Tiny Label, Smallest Item on the Account, Job Economics)

**What:** Priced and documented P/N 3017584 — a single 0.5" × 0.5" PTO ACTIVE label (black 0.1" Helvetica Bold text on white, R1/8 rounded corners, backing slit at middle) on Orajet 3951 cast vinyl + 1-mil polyester overlaminate. One-off order of qty 6 for a field service request. Rev A, dated 05/26/2026, drafter TJM. Arrived alongside P/N 3017583 as part of the same next-day-rush field service request (separate line items, not a kit).

**Item Created:** `items/3017584.md`

**Pricing:** $55 program total for qty 6 ($9.17/label flat across all six tiers). Anchored to the $55 account minimum-worthwhile-charge floor (P/N 1230820 FA price). Sq ft 0.00174 — **smallest item on the entire Elliott account.** Far outside the ~0.5–2.0 sq ft singles band scope; band is structurally inapplicable.

**Job economics:**
- Production footprint: ~0.20 sq ft Orajet 3951 + ~0.20 sq ft 1-mil polyester laminate (single pass through 13.5" laminator, single print run)
- Material cost: ~$0.50 for the 6-label job ($0.08/label) — effectively zero relative to the $55 floor; documented for completeness, does not drive pricing
- File prep: **$0** per account rule (PRICING_RULES.md §22) — Elliott supplies production-ready DWG
- Production time: ~20-25 min total (5 min file import + 15-20 min print/lam/cut/inspect/package)
- Contribution margin: ~$54.50 on $55 revenue (~99%); ~$149/hr per production-minute
- Implied per-sq-ft rate: ~$5,270/sq ft — the most extreme arithmetic artifact on the account; explicitly meaningless as a reference

**Key Decisions:**
- **Sq ft band explicitly NOT applied.** At 0.00174 sq ft, the singles band ($15.43/sq ft at qty 20) yields $0.027/label — far below the worthwhile-charge floor and below even the file-import time. Documented in Pricing Derivation.
- **Anchored to the $55 account floor**, same logic as P/N 3017583 and the outrigger switch program. Outrigger has 20 labels in its program ($55 ÷ 20 = $2.75); 3017583 has 6 labels ($55 ÷ 6 = $9.17); 3017584 has 6 labels ($55 ÷ 6 = $9.17). Per-label rates scale inversely with quantity and are not properties of the labels themselves — explicitly documented.
- **3017583 + 3017584 are separate line items, not a kit.** They arrived together as part of the same next-day-rush field service request but require separate file imports + separate print/lam/cut/inspect/package runs. Combined PO is quoted as two separate $55 programs ($110 total), not one combined $55. Documented in Pricing Derivation under "Field-service context."
- **No first article** — one-off, not applicable.
- **No multi-round AI validation** — straightforward one-off job-economics call per session brief; no precedent-setting risk to existing bands.
- **Mylar = polyester terminology note documented.** Drawing reads "1 mil clear Mylar overlay" — Mylar is a polyester-film trade name (originally DuPont), so this maps directly to the standard 1-mil polyester laminate used across the Orajet 3951 material family. No material change. Documented as a tagged warning block in Notes and Warnings. Sister item 3017583 uses "1 mil clear vinyl overlay" wording on its drawing for the same physical laminate — Elliott is actively working with Pro Label to standardize spec-sheet verbiage per Nick's account context.
- **NOT a benchmark.** Eight warning blocks added to Notes and Warnings: ONE-OFF ORDER, DO NOT BENCHMARK, SMALLEST ITEM ON THE ACCOUNT (new structural warning for this item), DO NOT SURFACE PER-LABEL MATH, REORDER PRICING, ACCOUNT FLOOR, MYLAR TERMINOLOGY, ARTWORK PREP. Future tiny labels and one-offs rebuild job economics from scratch — do NOT extrapolate from this item's per-label number.
- **Pricing Profile band NOT contaminated.** Added 3017584 to the existing "Standalone Tiny One-Offs" subsection in `categories/printed-laminated-orajet.md` (created with 3017583 earlier today), distinct from both the outrigger switch program subsection and the singles Pricing Profile band. Singles band scope (~0.5–2.0 sq ft) and kit band remain intact and unchanged.

**Files Updated:**
- `items/3017584.md` — new item file with all required frontmatter and all 10 required sections
- `categories/printed-laminated-orajet.md` — added 3017584 row to "Standalone Tiny One-Offs" subsection table and a new 3017584 job-economics breakdown table; singles Pricing Profile band untouched
- `.claude/ARCHITECTURE.md` — added 3017584 to catalog (item count 12 → 13); category registry count 8 → 9 for Printed + Laminated; precedent chain extended with 3017584 standalone one-off block
- `.claude/STATE.yml` — incremented item_count 12 → 13; last_session and next_action updated
- `.claude/PROGRESS.md` — this entry

**Status:** Quoted. Ready to send to Sean as a single program line — "one-time minimum program charge: $55.00 total" — for qty 6 of P/N 3017584. If 3017583 and 3017584 land on the same PO, quote as two separate $55 programs ($110 total). validate.py passes 0 errors, 0 warnings.

---

### 2026-05-27 — New Item: P/N 3017583 — LBL - PTO Engage Process (One-Off Tiny Label, Job Economics)

**What:** Priced and documented P/N 3017583 — a single 2.5" × 1.5" ANSI Z535 NOTICE label (Safety White base, Safety Blue header, Safety Black text) on Orajet 3951 cast vinyl + 1-mil polyester overlaminate. One-off order of qty 6 for a unit in the field. Rev B, dated 05/26/2026, drafter TJM.

**Item Created:** `items/3017583.md`

**Pricing:** $55 program total for qty 6 ($9.17/label flat across all six tiers). Anchored to the $55 account minimum-worthwhile-charge floor (P/N 1230820 FA price). Sq ft 0.026 — outside the ~0.5–2.0 sq ft singles band scope; band is inapplicable.

**Job economics:**
- Production footprint: ~0.5 sq ft Orajet 3951 + ~0.5 sq ft 1-mil polyester laminate (single pass through 13.5" laminator, single print run)
- Material cost: ~$1.70 for the 6-label job ($0.28/label)
- File prep: **$0** per account rule (PRICING_RULES.md §22) — Elliott supplies production-ready DWG
- Production time: ~20-25 min total (5 min file import + 15-20 min print/lam/cut/inspect/package)
- Contribution margin: ~$53.30 on $55 revenue (~97%); ~$145/hr per production-minute

**Key Decisions:**
- **Sq ft band explicitly NOT applied.** At 0.026 sq ft, the singles band ($15.43/sq ft at qty 20) yields $0.40/label — below the worthwhile-charge floor. Documented in Pricing Derivation.
- **Anchored to the $55 account floor**, NOT to the outrigger switch $2.75/label. Outrigger has 20 labels in its program ($55 ÷ 20 = $2.75); 3017583 has 6 labels in its program ($55 ÷ 6 = $9.17). Per-label rates scale inversely with quantity and are not properties of the labels themselves — explicitly documented.
- **No first article** — one-off, not applicable.
- **No multi-round AI validation** — straightforward one-off job-economics call per session brief; no precedent-setting risk to existing bands.
- **Drawing terminology drift documented.** Drawing reads "1 mil clear vinyl overlay" — per Nick's account context note, this is account spec drift for the standard 1-mil polyester (Mylar) overlaminate. Nick is actively working with Elliott to standardize spec sheet verbiage. Documented as a tagged warning block in Notes and Warnings.
- **NOT a benchmark.** Six warning blocks added to Notes and Warnings: ONE-OFF ORDER, DO NOT BENCHMARK, DO NOT SURFACE PER-LABEL MATH, REORDER PRICING, ACCOUNT FLOOR, LAMINATE TERMINOLOGY, ARTWORK PREP. Future tiny labels and one-offs rebuild job economics from scratch — do NOT extrapolate from this item's per-label number.
- **Pricing Profile band NOT contaminated.** Added a new "Standalone Tiny One-Offs" subsection to `categories/printed-laminated-orajet.md`, distinct from both the outrigger switch program subsection and the singles Pricing Profile band. Singles band scope (~0.5–2.0 sq ft) and kit band remain intact and unchanged.

**Files Updated:**
- `items/3017583.md` — new item file with all required frontmatter and all 10 required sections
- `categories/printed-laminated-orajet.md` — added "Standalone Tiny One-Offs" ### subsection with 3017583 table and job-economics breakdown; singles Pricing Profile band untouched
- `.claude/ARCHITECTURE.md` — added 3017583 to catalog (item count 11 → 12); category registry count 7 → 8 for Printed + Laminated; precedent chain updated with standalone one-off note
- `.claude/STATE.yml` — incremented item_count 11 → 12; last_session and next_action updated
- `.claude/PROGRESS.md` — this entry

**Status:** Quoted. Ready to send to Sean as a single program line — "one-time minimum program charge: $55.00 total" — for qty 6 of P/N 3017583. validate.py passes 0 errors, 0 warnings.

---

### 2026-05-27 — Frontend: Materials Tab + Sticky Header + Red Purge + Badge Removal

**What:** Three-part frontend overhaul.

**Part 1 — Materials data layer.** Created new `materials/` directory at repo root with 7 material files (YAML frontmatter only, no prose). One file per material — pure data layer for the frontend:
- `orajet-3951-white.md` (print_media)
- `1mil-polyester-overlaminate.md` (laminate)
- `3m-180mc-cardinal-red.md`, `3m-180mc-olympic-blue.md`, `3m-180mc-white-24in.md`, `3m-180mc-white-48in.md` (cut_vinyl)
- `transferrite-582u.md` (tape)

Each material file carries: manufacturer, product name/code, dimensions (roll width, length), full cost breakdown (per roll, per yard, per sq ft, per MSI where applicable), verified date, compatibility links to other materials, and `used_in_items` list mapping each material to the items that use it. All values sourced from `governance/PRODUCTION.md` — no invented data. Empty fields left as empty strings or null.

Created `scripts/build_materials.py` following the exact same pattern as `build_frontend.py`. Reads `materials/*.md` frontmatter, writes `frontend/materials.json` with structure: `{generated, material_count, materials: {material_id: {frontmatter}}}`. No fields stripped — Nick is the sole user. Updated `.github/workflows/build-frontend.yml` to run `build_materials.py` and include `frontend/materials.json` in the auto-commit.

**Part 2 — Frontend overhaul — red purge + badge removal.** Elliott red (`#E8000D`) now appears in exactly one place: the ELLIOTT wordmark in the top-left header. Removed red from gross profit cells (now white/light gray), from the qty 20 row highlight (now `rgba(255,255,255,0.06)` subtle dark highlight), from the Copy for Email button (now dark gray surface-3 with white text and border-medium border), from the One-Off Program badge (now dark gray inline tag), from selected-item sidebar indicator (now white), from filter pills (now surface-3 + border-strong), from stat-block hover bars (removed entirely), and from search-input focus glow (now subtle white glow). Replaced `--accent` and all `--accent-dim`/`--accent-glow` CSS vars with `--brand-red` (used only on `.brand`), `--row-highlight`, and neutral surface vars.

Removed all status badges system-wide:
- Sidebar item list no longer shows FA ACCEPTED / QUOTED / ONE-OFF PROGRAM chips
- Item detail sticky header no longer shows the status badge next to the P/N (kept only the One-Off tag, redesigned as a neutral dark-gray inline tag)
- The Status row in the Specifications panel is retained as a plain data row (not a badge)

**Part 3 — Frontend overhaul — sticky header + materials tab.** Item detail layout now has a sticky top block (`position: sticky; top: 0`) that contains: P/N + title + breadcrumb on the left, spec sheet thumbnail on the right (PDF rendered via pdf.js to canvas at scale 0.5, capped at 120px height, opens in new tab on click), and the 4-card stat bar below spanning full width. Below the sticky block, a `.scroll-area` div scrolls everything else: volume pricing table, specifications card, and a full-width notes panel. Notes panel uses `white-space: pre-wrap` with 40px+ bottom padding to guarantee no truncation. If no spec sheet exists for an item, the right side of the sticky header is simply empty — no placeholder.

Added a tab bar in the topbar with two tabs: Items (default) and Materials. The Materials tab swaps the sidebar to a grouped material list (sectioned by Cut Vinyl / Print Media / Laminate / Application Tape, alphabetical within group) and swaps the main panel to a material detail view with the same sticky-header pattern: name + manufacturer + code on the left, stat bar (Cost/Sq Ft, Roll Width, Thickness, Verified Date) below, then a scrollable area with Specifications (left, only fields with values are rendered) and Connections (right, listing items that use the material plus the related material type — tape for cut vinyl, laminate for print media, substrate for laminate, cut vinyls for tape). Every item link in the Materials tab calls `selectItem(pn)` which switches back to the Items tab and loads the item detail. Every material link calls `selectMaterial(mid)`. Notes panel renders only if non-empty.

**Validation:** `python scripts/build_materials.py` clean (7 materials). `python scripts/build_frontend.py` clean (11 items). `python scripts/validate.py` — 0 errors, 0 warnings.

**Files touched:** `materials/*.md` (7 new), `scripts/build_materials.py` (new), `frontend/index.html` (full rewrite), `frontend/materials.json` (built), `.github/workflows/build-frontend.yml`, `.claude/PROGRESS.md`, `.claude/STATE.yml`.

---

### 2026-05-27 — Price Lock + System Audit: P/N 1277970, 1277980, 1277990, 1278000 — Final $55 Program Locked, Full Repo Audit Clean

**What:** Two-part session.

**Part 1 — Price Lock.** Locked the validated $55 program pricing for the 4-label outrigger switch program into all four item files with full documentation of the 4-round, 6-model AI validation process (24 total model runs).

- Round 1 (Build): **Unanimous $55** across all 6 models — each independently anchored to the account FA floor (P/N 1230820 FA at $55).
- Round 2 (Destruction): **5 of 6 Yes / Yes with modifications**. One outlier proposed $38 program total on cost-plus reasoning. Outlier rejected — reason: cost-plus logic ignores account floor and relationship context; the $17 spread is below buyer sensitivity threshold; $38 would undercut the account's own price structure for future one-offs.
- Round 3 (Buyer Simulation): **All 6 models approved without questions.** Instant-approval threshold confirmed at $75 or under; $55 lands comfortably inside it. No buyer pushback predicted.
- Round 4 (Final Synthesis): **All 6 unanimous — yes, send as shown.** No tier-level concerns, no precedent concerns, no discomfort flags.

Validated quote language captured verbatim in P/N 1277970 Pricing Derivation; program peers reference it. The quote frames the price as a single "one-time minimum program charge for custom build support: $55.00 total" and explicitly disclaims any catalog/reorder rate, floating an expected $0.35–$0.55/label range at qty 250+ for any future repeat-production request.

**Notes and Warnings restructured** on all four item files into six discrete, non-negotiable warning blocks: (1) ONE-OFF PROGRAM, (2) DO NOT BENCHMARK, (3) DO NOT SURFACE PER-LABEL MATH, (4) REORDER PRICING, (5) ACCOUNT FLOOR, (6) ARTWORK PREP.

**Part 2 — Full System Audit.** Audited every file in the repo for sync after today's heavy activity (artwork prep purge, multiple reprice cycles, new governance rules).

| Audit Check | Result |
|-------------|--------|
| Zero file-prep / artwork-prep cost references in repo | 7 stale Process-Step entries in existing items (1230820, 1278930, 1245130, 1205720, 3017435, 3018378, 1186310) had "File prep" as step 1; rewrote each to "File import/setup — ~5 min mechanical, NOT billable labor (see PRICING_RULES.md §22)." 3018378 production-time table had a 20-min "File prep" row; rewrote to match the account rule and recomputed per-unit billable total. All remaining file-prep references in the repo are rule-reinforcing language (e.g., "$0 file prep — Elliott provides production-ready DWG"), not cost inputs. |
| PRICING_RULES.md §22-24 present and correctly numbered | Confirmed. §22-24 under "Account-Level Cost Inputs" heading. No conflict with existing rules. |
| categories/printed-laminated-orajet.md integrity | Singles band, Kit band, and Tiny Printed Labels subsection all intact. Pricing Profile band is NOT contaminated by tiny-label pricing — tiny labels carry their own callout box and are explicitly excluded from the singles band by scope note. All 7 Orajet items present. |
| ARCHITECTURE.md integrity | All 11 items present with correct status, pricing, and margin. Precedent chain correctly separates the tiny label program (one-off, do-NOT-benchmark) from the main printed/laminated chain (1230820 → 1278930 → 1245130). |
| Item file consistency (11 items) | All required frontmatter fields present; sq_ft math correct; per_label_at_qty_20 = price_20_49 / label_count for all 11; all status values valid; no item references file prep as a cost input. |
| STATE.yml | item_count = 11, last_session and next_action updated. |
| validate.py | **0 errors, 0 warnings** across all 11 items. |

**Items Affected:**
- 1277970, 1277980, 1277990, 1278000 — Pricing Derivation rewritten with 4-round/6-model validation table, rejected $38 alternative, verbatim validated quote language. Notes and Warnings restructured into the six required warning blocks.
- 1230820, 1278930, 1245130, 1205720, 3017435, 3018378, 1186310 — Process Steps step 1 relabeled from "File prep" to "File import/setup — ~5 min mechanical, NOT billable labor." Documentation-only; no pricing changes.

**Files Modified:**
- `items/1277970.md` — Pricing Derivation (AI Validation section), Notes and Warnings (rewritten with six warning blocks)
- `items/1277980.md`, `items/1277990.md`, `items/1278000.md` — Pricing Derivation (AI Validation section now inherits 4-round validation from 1277970), Notes and Warnings (rewritten with six warning blocks)
- `items/1230820.md`, `items/1278930.md`, `items/1245130.md`, `items/1205720.md`, `items/3017435.md`, `items/1186310.md` — Process Steps step 1 relabeled
- `items/3018378.md` — Process Steps step 1 relabeled; per-unit time table file-prep row rewritten to match account rule
- `.claude/PROGRESS.md` — this entry
- `.claude/STATE.yml` — last_session and next_action updated

**Key Decisions:**
- Price stays at $55 program total ($2.75/label). 4-round validation closed; no further reprice cycle warranted.
- Six warning blocks in Notes and Warnings are non-negotiable structure. Future sessions touching these items must preserve all six.
- Verbatim validated quote language lives in P/N 1277970's Pricing Derivation only (program peers reference it). Single source of truth prevents drift.
- Process Steps relabel on the 7 existing catalog items is documentation-only and does not change any price, margin, or band. The pricing on those items did not use file-prep as a stated cost driver, so no margin reasoning is affected.

**Status:** Complete. Ready to send the $55 quote to Sean. validate.py passes 0 errors, 0 warnings.

---

### 2026-05-27 — Reprice: P/N 1277970, 1277980, 1277990, 1278000 — $55 Program Total (Post Artwork-Prep Purge)

**What:** Repriced the 4-label outrigger switch program from $15/label = $300 program total down to **$2.75/label = $55 program total**. The previous $15/label reprice was built on a labor-heavy reconstruction that used "file prep × 4 unique designs" as a major cost driver — an assumption now purged account-wide (see entry below). With file prep at $0, the true job inputs are ~$6.94 material + ~25 min production time. The worthwhile-charge floor is the account's lowest first article price ($55, P/N 1230820 FA), treated as a program-level minimum-worthwhile-charge floor — NOT as a per-label comparable.

**New pricing (all four items):**
- Per label (all six tiers, flat): **$2.75**
- Per P/N (qty 5): **$13.75**
- Program total (4 P/Ns × qty 5): **$55**
- per_label_at_qty_20: $2.75
- margin_at_qty_20: "N/A — one-off program, flat $55 total, see Pricing Derivation"

**Reprice trajectory (full history of this program):**

| Stage | Per Label | Program Total | Notes |
|-------|-----------|---------------|-------|
| Initial (AM) | $7 | $140 | Job-floor estimate. |
| 1st reprice (PM) | $15 | $300 | Used file-prep labor as cost driver. INCORRECT for this account. |
| **Current (evening, post-purge)** | **$2.75** | **$55** | Anchors to account FA floor; file prep is $0 per account rule. |

**Documentation requirements applied to all four items:**

- frontmatter `pricing_logic`: rewritten with ONE-OFF PROGRAM PRICE warning and "Never use as benchmark" language
- frontmatter `notes`: rewritten with ONE-OFF designation and Sean's verbatim quote
- frontmatter `margin_at_qty_20`: "N/A — one-off program, flat $55 total, see Pricing Derivation"
- **Pricing section:** prominent callout box at top warning against benchmarking
- **Pricing Derivation section:** prominent callout box at top warning against benchmarking; full job-economics reconstruction; explicit "why this is NOT a benchmark" subsection
- **Notes and Warnings section:** prominent callout box at top with Sean's verbatim quote, ~$343/sq ft artifact warning, "STOP and re-read this section" instruction for future sessions
- **categories/printed-laminated-orajet.md:** Tiny Printed Labels subsection rewritten with callout box warning against benchmarking; pricing table updated; pricing rule #2 updated

**Files Updated:**
- `items/1277970.md`, `items/1277980.md`, `items/1277990.md`, `items/1278000.md` — full rewrite of frontmatter pricing fields, Production Process, Pricing, Pricing Derivation, Margin Analysis, Notes and Warnings sections
- `categories/printed-laminated-orajet.md` — Tiny Printed Labels subsection rewritten with callout box; pricing rule #2 updated
- `.claude/ARCHITECTURE.md` — catalog rows updated (flat $2.75 / N/A margin); precedent chain replaced "founding data point" framing with "ONE-OFF PROGRAM — DO NOT BENCHMARK"; category registry updated
- `.claude/STATE.yml` — last_session updated to system + reprice
- `.claude/PROGRESS.md` — this entry

**Status:** Repriced. Ready to send to Sean as a single program email at $55 program total.

---

### 2026-05-27 — System: Account-Wide Artwork-Prep Cost Purge

**What:** Permanent account-level correction. Elliott Equipment Company provides production-ready DWG files for every item on this account, without exception. File prep, artwork preparation, design time, and pre-press labor are zero-cost, zero-time inputs on every Elliott job — past, present, and future. This is a permanent account-level truth, not a per-job assumption.

Recent pricing sessions (notably the 2026-05-27 PM reprice of the outrigger switch program from $7 → $15/label) used file-prep labor as a cost driver. That input is now purged everywhere it appears or could be inferred. No prices on the existing catalog change as part of this purge (those prices stand); only the cost reasoning documentation is corrected.

**Files Updated:**
- `.claude/MASTER_CONTEXT.md` — Added Core Rule #7: Elliott provides production-ready DWG files; file prep cost is always zero on this account
- `governance/PRICING_RULES.md` — Added §22-24 under new "Account-Level Cost Inputs" heading: explicit rule that Elliott provides production-ready DWG, do not include file prep in any cost build, prior sessions that did so were incorrect
- `governance/PRODUCTION.md` — Process Steps by Category: prepended account-level rule callout, redefined step 1 for both Cut Vinyl and Printed + Laminated as "File import/setup — ~5 min mechanical, NOT billable labor"
- `governance/SPEC_EXTRACTION.md` — Account-Specific Defaults table: added "Artwork / File Prep" row stating production-ready DWG is provided by Elliott; zero cost; zero time
- `items/1277970.md`, `items/1277980.md`, `items/1277990.md`, `items/1278000.md` — added artwork row to Spec Extraction blocks; added "No file prep" callout above Production Process; explicit "$0 file prep" row in Pricing Derivation job-inputs table; repricing history bullet in Notes and Warnings documenting the purge correction (these items are also being repriced as part of the same session — see entry above)

**Key Decisions:**
- **No existing item prices changed.** The purge is documentation-only for already-quoted items (1230820, 1278930, 1245130, 1205720, 3017435, 3018378, 1186310). Their pricing did not use file prep as a stated cost driver, so no margin reasoning was affected.
- **The four outrigger switch items (1277970-1278000) had their pricing changed**, because the $15/label reprice from earlier in the day was explicitly built on file-prep labor. That reprice is reversed; see the reprice entry above.
- **Account rule is permanent, not a session note.** Future Claude Code sessions reading any of `MASTER_CONTEXT.md`, `PRICING_RULES.md`, `PRODUCTION.md`, or `SPEC_EXTRACTION.md` will see the rule and apply it.

**Status:** Purge complete. Account is clean of file-prep-as-cost-driver assumptions.

---

### 2026-05-27 — Reprice: P/N 1277970, 1277980, 1277990, 1278000 — Corrected Production Footprint

**What:** Repriced the 4-label outrigger switch program after Nick provided the actual Nick-verified production footprint. The initial $7/label price was based on a job-floor estimate that materially understated actual production effort.

**Nick-Verified Production Footprint (full 20-label job):**
- Print vinyl (Orajet 3951): 15" × 30" = 450 sq in = 3.125 sq ft → $3.78
- Laminate (1-mil polyester): 13.5" × 30" = 405 sq in = 2.8125 sq ft → $2.76
- Ink (eco-solvent, low coverage on tiny circles): 20 × ~$0.02 = $0.40
- **Total material cost for the 20-label job: $6.94**
- Per label: $0.35 | Per P/N (qty 5): $1.74

**Job cost reconstruction:** Material $6.94 + labor (file prep × 4 unique designs, print run, lam pass, kiss-cut, inspect, package) ~$130 + overhead ~$45 = **~$182 total job cost**.

**Repricing:**
- Per label (qty 1-9): $7 → **$15**
- Per P/N (qty 5): $35 → **$75**
- Program total (4 P/Ns × qty 5): $140 → **$300**
- Original $140 revenue vs $182 cost = ~$42 loss avoided
- Recommended $300 revenue → ~$118 gross profit → **~39% fully-loaded job-level margin** (healthy for a one-off)

**Tier table updated across all four items:**

| Tier | Old | New |
|------|-----|-----|
| 1-9 | $7 | $15 |
| 10-19 | $5 | $11 |
| 20-49 | $3.50 | $8 |
| 50-99 | $2.50 | $6 |
| 100-199 | $2 | $4.50 |
| 200+ | $1.50 | $3.50 |

**Files Updated:**
- `items/1277970.md` — frontmatter prices/material_cost/pricing_logic/notes; full rewrite of Nesting and Material Cost, Pricing, Pricing Derivation, Margin Analysis, Notes and Warnings sections
- `items/1277980.md`, `items/1277990.md`, `items/1278000.md` — same pattern (program peer references to 1277970)
- `categories/printed-laminated-orajet.md` — tiny printed labels subsection: prices updated, production footprint table added, reprice note documented
- `.claude/ARCHITECTURE.md` — catalog price column updated for all four items (qty 1-9 $15, qty 20 $8); margin annotation updated; precedent chain annotation updated
- `.claude/STATE.yml` — last_session updated to reprice event (item_count unchanged at 11)

**Key Decisions:**
- **Sq ft band still inapplicable.** At 0.008 sq ft per label or even 3.125 sq ft of production footprint, the singles band yields prices below the one-off job floor. Documented.
- **Anchor reference:** P/N 1278930 (3-label kit) at $15/label qty 1-9. Outrigger program lands at parity per-label at qty 1-9 — defensible because 4 unique designs in a one-off carry comparable setup effort to a single-design 3-label kit.
- **Tier compression ~77%** — variable per-label cost is near-zero at this size, so volume amortizes setup.
- **Spec Extraction, Item Overview, Material Specification, Production Process, Production Debrief sections NOT touched** per session brief.
- **Pricing Profile band NOT contaminated** — tiny-labels subsection in the category file remains separate from the singles band.

**Status:** Repriced. Ready to send to Sean as a single program email at $300 program total.

---

### 2026-05-27 — New Items: P/N 1277970, 1277980, 1277990, 1278000 — 4-Label Outrigger Switch Program (18T)

**What:** Priced and documented a 4-label outrigger switch program for a one-off 18T crane build. Sean requested qty 5 of each of 4 labels (20 labels total) as a single program. All four labels are dimensionally and materially identical (Ø1-3/16" circle, Orajet 3951 cast 4-mil vinyl + 1-mil polyester Mylar overlay, kiss cut, Helvetica Bold black text on white). Only the directional content differs:

- 1277970 — EXTEND/RETRACT, OUTRIGGER, HORIZONTAL FRONT
- 1277980 — EXTEND/RETRACT, OUTRIGGER, VERTICAL FRONT
- 1277990 — EXTEND/RETRACT, OUTRIGGER, HORIZONTAL REAR
- 1278000 — EXTEND/RETRACT, OUTRIGGER, VERTICAL REAR

**Items Created:** `items/1277970.md`, `items/1277980.md`, `items/1277990.md`, `items/1278000.md`

**Files Updated:**
- `categories/printed-laminated-orajet.md` — added new "Tiny Printed Labels — Sub-0.1 Sq Ft Size Class" subsection with all four items; added band scope note clarifying the singles band applies to ~0.5–2.0 sq ft only; added Pricing Rule #2 for tiny labels (job economics, not sq ft)
- `.claude/ARCHITECTURE.md` — added all four items to catalog; updated Printed + Laminated category count 3 → 7 with size-class breakdown; added founding-data-point precedent chain for the tiny printed label class
- `.claude/STATE.yml` — incremented item_count 7 → 11

**Pricing:** $7/label at qty 1-9 (Sean's order tier). Full tier table populated for structural completeness: $7 / $5 / $3.50 / $2.50 / $2.00 / $1.50. Program total at qty 5 each = $140 (4 × 5 × $7). Material cost ~$0.05/label — effectively zero relative to the job floor.

**Key Decisions:**
- **Sq ft band explicitly NOT applied.** At 0.008 sq ft, the singles band ($15.43/sq ft at qty 20) yields $0.12/label — nonsensical, does not cover setup. Documented in every item's Pricing Derivation.
- **Priced on minimum run / job economics.** Setup, file prep, print registration, kiss-cut definition, lamination, inspection, packaging are fixed costs regardless of label size. Job-floor estimate ~$130-170 for the 4-design / 20-label program; adopted $7/label = $140 program total.
- **Founding data point for the sub-0.1 sq ft printed label size class.** P/N 1277970 designated as the founding item; 1277980/1277990/1278000 reference it as program peers.
- **Pricing Profile band NOT contaminated.** New tiny-labels subsection in the category file is separate from the singles band. Band scope note added explicitly limiting it to ~0.5–2.0 sq ft items.
- **Each P/N is a separate line item** (not a kit). All four are single labels with their own P/N and distinct content — they happened to be ordered together for one machine build. Per-label parity logic does not apply; this is not a matched-set kit.
- **No first article** — one-off custom build at qty 5, not applicable.
- **No AI model validation** — straightforward minimum-run / job-economics call per the session brief; no reorder expectation, no precedent-setting risk for the existing bands.
- **Margin note:** ~99% gross-of-material margin is structurally honest but operationally misleading. Documented in each item that the price is contribution to fixed costs at minimum run, not 99% profit; effective job-level margin is ~20-45%.

**Status:** Quoted. Ready to send to Sean as a single program email.

---

### 2026-05-26 — New Item: P/N 1186310 — E160 Cardinal Red Model Designation

**What:** Priced and documented P/N 1186310 — cut vinyl model designation label for the E160 model. Cardinal Red, 33-9/16" × 11". Direct dimensional and material clone of FA-accepted P/N 1205720 (E190 Cardinal Red) — only the model number content differs ("E160" vs "E190").

**Item Created:** `items/1186310.md`

**Files Updated:**
- `categories/cut-vinyl-3m-180mc.md` — added 1186310 to catalog table, updated Pricing Profile to 4 data points
- `.claude/ARCHITECTURE.md` — added 1186310 to item catalog and precedent chain; category registry count 3 → 4
- `.claude/STATE.yml` — incremented item_count 6 → 7

**Pricing:** $35 at qty 20 (sq ft parity with P/N 1205720). Material cost $7.62 (length-based Cardinal Red, 24" roll). Margin ~78% at qty 20, ~65% floor at 200+.

**Key Decisions:**
- Direct parity case — dimensionally identical to P/N 1205720 (33-9/16" × 11"), same material (3M 180mC-53 Cardinal Red), same process (Cut/Weed/Mask).
- 3-decimal sq ft precision (2.564) used; 1205720 uses 2-decimal (2.56). Documented the rounding artifact: $13.65/sq ft at 3-decimal vs $13.67/sq ft at 2-decimal — same underlying item.
- No first article offered — not requested; process and tooling proven from 1205720.
- No AI model validation — direct parity exemption per PRICING_VALIDATION.md.
- Rule 14 deviation explicitly acknowledged (1205720 is a Relationship Concession; this prices within the concession-phase band by deliberate strategic choice).

**Status:** Quoted. Ready to send to Sean.

---

### 2026-05-22 — Audit Remediation: Full System Audit — 3 Critical, 10 Warnings, 9 Info

**What:** Completed remediation of all findings from the full system audit. Documentation accuracy corrections, tooling improvements, and sync fixes. No prices changed, no items changed status.

**Items Affected:**
- 1205720 — Material cost corrected from $7.01 (area method) to $7.62 (length-based method). Margin updated ~80% → ~78%. Price unchanged.
- 1278930 — override_type made more specific; laminator feed notation corrected.
- 1245130 — Added FA note, nesting causality, rounding note for $43 tier.
- 3017435 — Added FA note; Rule 14 deviation formally documented in Pricing Derivation.
- 3018378 — Rule 14 deviation formally documented in Pricing Derivation.

**Files Modified:**
- `.claude/MASTER_CONTEXT.md` — File map updated (3018378, images/, frontend/, build_frontend.py)
- `.claude/COMPLETION_TEMPLATES.md` — Added build_frontend.py triggers; added Drawing revision and Item discontinued trigger rows
- `.claude/ARCHITECTURE.md` — Corrected descriptions (3018378, 1230820); 1205720 margin ~80%→~78%; added Discontinued status
- `scripts/validate.py` — Added check_category_registry(), check_state_item_count(); fixed Pricing section detection; added Discontinued to valid statuses
- `scripts/profile.py` — Band summaries now split by item_type within each material family
- `scripts/build_frontend.py` — Added STRIP_FIELDS; replaced os.popen with datetime.now()
- `categories/cut-vinyl-3m-180mc.md` — Margin floor corrected ~64–68%→~62–65%; margin at qty 20 ~76–80%→~76–78%; $13.94→$13.93; Cardinal Red material cost note updated; Rule 14 status note added
- `categories/printed-laminated-orajet.md` — Added step 2a (laminator width check) to singles decision tree
- `items/1205720.md` — Material cost, margin table, nesting section corrected; correction note added
- `items/1278930.md` — override_type specificity; laminator feed notation corrected in notes and Nesting section
- `items/1245130.md` — FA note, nesting causality, rounding note
- `items/3017435.md` — FA note; Rule 14 deviation note
- `items/3018378.md` — Rule 14 deviation note
- `governance/SPEC_EXTRACTION.md` — Added Engineer/Drafter field to Identity and output format
- `governance/PRICING_VALIDATION.md` — Clarified "materially identical" for color variants
- `governance/PRICING_RULES.md` — Rule 14: clarified range → use midpoint as benchmark
- `governance/PRODUCTION.md` — Material cost tables: added Verified dates; 1278930 laminator description corrected; Cardinal Red cost updated to $7.62 (length-based)
- `frontend/index.html` — copyForEmail now includes first article price
- `frontend/data.json` — Rebuilt; internal fields stripped (pricing_logic, benchmark_item, downstream_items, material_cost_per_unit, cost_version_date, override_type, margin_at_qty_20)

**Key Decisions:**
- Cut vinyl margin floor band corrected to ~62–65% (floor driven by 3017435/24" roll at 61.5%; ceiling driven by corrected 1205720 at 65.4%)
- 1205720 material cost correction is documentation-only — price unchanged, relationship concession remains in effect
- validate.py now uses prefix-match for section headings (allows "(Reconstructed)" subtitles), exact-match only for "Pricing" to prevent false match on "Pricing Derivation"

**Status:** Complete. All 3 critical, 10 warning, and 9 info findings resolved. validate.py passes 0 errors, 0 warnings.

---

### 2026-05-22 — New Item: P/N 3018378 — D115 Olympic Blue Model Designation

**What:** Priced and documented P/N 3018378 — cut vinyl model designation label for the D115 model. Olympic Blue, 32.88" × 11.00", single color block lettering ("D115").

**Item Created:** `items/3018378.md`

**Files Updated:**
- `categories/cut-vinyl-3m-180mc.md` — added 3018378 to catalog table, updated Pricing Profile to 3 data points
- `.claude/ARCHITECTURE.md` — added 3018378 to item catalog and precedent chain; updated category registry count
- `governance/PRODUCTION.md` — added 3M 180mC-57 Olympic Blue to material costs table and quick reference
- `.claude/STATE.yml` — updated session state

**Pricing:** $35 at qty 20 (sq ft parity with P/N 1205720). Margin ~78% (Olympic Blue roll cost $162.78 vs Cardinal Red $153.60 drives slight material cost increase: $7.88 vs $7.01).

**Key Decisions:**
- Material: 3M Controltac 180mC-57 Olympic Blue — confirmed in session brief, not in prior repo data. Added to PRODUCTION.md.
- PMS caveat documented: Olympic Blue is visual approximation of PMS 2386 C, not a certified Pantone match. Must be disclosed in quote.
- Sq ft parity: 2.512 sq ft vs 2.56 sq ft benchmark — <2% difference, same tier structure.
- Labels per roll corrected: session brief stated "5 positions" (10 labels/roll). Verified: 10 positions → 20 labels/roll. Material cost unaffected.
- No first article pricing — not requested or offered.
- No AI model validation — direct parity with FA-accepted item.

**Status:** Quoted. Ready to send to Sean.

---

### 2026-05-22 — System Build: Notion → GitHub Migration

**What:** Migrated the entire Elliott Equipment pricing system from Notion to a structured GitHub repo (`tacctile/elliott`). Source data was validated through a 3-round audit in Claude Chat before migration.

**Items Affected:**
- All 5 items (1230820, 1278930, 1245130, 1205720, 3017435) — converted to structured markdown with YAML frontmatter

**Files Created:**
- Full `.claude/` context system (MASTER_CONTEXT, ARCHITECTURE, CHAT_CONTEXT, COMPLETION_TEMPLATES, STATE, PROGRESS, settings.json)
- Full `governance/` doc set (SPEC_EXTRACTION, STRUCTURE_RULES, PRICING_VALIDATION, PRICING_RULES, PRODUCTION)
- 2 category files with Pricing Profiles
- 5 item files with complete frontmatter + all 10 required sections
- Validation and profile scripts
- README, .gitignore

**Key Decisions:**
- MASTER_CONTEXT kept lean — account identity and routing only, no narrative
- Governance split into 5 files (was 1 Notion page) for single-responsibility
- Equipment/production details in their own file (PRODUCTION.md) — changes on different cadence than pricing rules
- CHAT_CONTEXT designed for dual-path operation (Claude Code prompts + direct conversation)
- Pricing Profiles embedded in category files, not separate documents

**Status:** Complete. System ready for first new item.
