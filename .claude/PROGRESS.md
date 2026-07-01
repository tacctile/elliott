# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> **Rolling window: 10 entries max. When adding an 11th, remove the oldest. Git retains all history.**
>
> This file is the session memory layer: why decisions were made, what changed strategically, what a future session needs to know. It is not a commit log and not a validation archive — full validation records live in `items/*.md` (Pricing Derivation), file-level changes live in git history, and structure/math compliance is enforced by `scripts/validate.py`. Entry format (template in `.claude/COMPLETION_TEMPLATES.md`): What / Key Decisions / Strategic Flags / Status, 10–25 lines per entry, no other sections.
>
> Last Updated: 2026-07-01 (Session AH — P/N 1073950 added, third item at the established 0.503 sq ft singles-band position, $8.00/qty 20, independently 4-wave validated to exact parity with governing benchmark 1068270 — explicitly NOT a parity exemption. Previously Session AG — P/N 3020477 added, fourth sub-scope singles data point, $2.75/qty 20, 4-wave validated — explicitly NOT a parity exemption. Previously Session AF — bug fix: hydrateFromDb() variants drop — dual-variant display now renders on live Supabase path.)

---

### 2026-07-01 — Session AH (new item): P/N 1073950 — CHART-TOP MOUNT JIB 500# G85 (80°) BASKET 500#, third item at the 0.503 sq ft singles-band position, $8.00/qty 20, independently 4-wave validated to exact parity with 1068270

**What:** New printed/laminated single label at 7.25" × 10.00" = 0.503 sq ft — the identical footprint already held in the singles band. Rather than applying a direct parity exemption, ran the full 4-wave atomic AI validation (24 independent responses, 6 models × 4 waves); the process independently converged on exact parity with governing benchmark P/N 1068270 at $8.00/qty 20 = $15.90/sq ft. Tier table locked identical to 1068270 across all six tiers: $16.50/$10.50/$8.00/$6.25/$5.25/$4.25.

**Key Decisions:**
- Wave 1 split 4/6 at $7.75 (proportional scaling from root benchmark 1230820) vs 2/6 at $8.00 (direct nearest-neighbor parity). Wave 2 unanimously killed the $7.75 path — High-severity Buyer/Procurement, Cost Auditor, and Strategic-Precedent attacks all found that identical area to an already-quoted item makes parity the only defensible position. Waves 3 and 4 unanimous on $8.00, no modifications.
- Material cost filed at $0.98/label (§25 canonical, rounded to the cent) rather than 1068270's $1.00 (rounded to the dollar) — same underlying $0.9803 calculation; filing-convention difference only, does not affect tier pricing.
- No override — engine consensus accepted (Override Type: None).

**Strategic Flags:**
- Artwork/mount-designation relationship to 1068270 (Top Mount Jib vs EZR mount, same G85 Basket 500# load rating) is unresolved as of filing — flagged for Nick/Sean follow-up alongside the quote; does not affect pricing per unanimous Wave 1-4 findings.
- Internal-only context, not part of the formal validation record and not citable to Sean: P/N 1082570 (a do-not-benchmark item — its current order is priced at $42 flat job-economics, not a catalog rate) happens to share the identical 0.503 sq ft footprint. This same-size confirmation supports internal pricing confidence but was deliberately excluded from the formal validation record.
- This item does NOT add a new independent singles-band data point — the 0.503 sq ft position remains anchored where it already was, now shared by three items (1082570, 1068270, 1073950). Band stays at 4 confirmed data points.
- First article confirmed NOT required (per Sean). Order quantity not yet specified — standard 6-tier ladder quoted.
- Item count: 37 → 38. Printed/Laminated category: 25 → 26 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 38 rows confirmed in Supabase.

---

### 2026-06-30 — Session AG (new item): P/N 3020477 — LBL-MODULAR BOOM CONTROL HYDRAULIC CONTROL, fourth sub-scope data point, $2.75/qty 20, independently 4-wave validated

**What:** New printed/laminated single label (title block: LBL-MODULAR BOOM CONTROL HYDRAULIC CONTROL; in-label artwork reads "CONTROL SELECTOR") at 11.50" × 1.63" = 0.130 sq ft. Single continuous rounded-rectangle outer cut, 1 piece — the two visually grouped icon clusters in the artwork are printed borders, not separate die cuts. Routes to sub-scope (0.1–0.5 sq ft). Ran full 4-wave atomic AI validation (24 independent responses, 6 models × 4 waves) and arrived at $2.75 at qty 20 = $21.15/sq ft, sitting correctly between 1279130 (0.148 sq ft, $20.95/sq ft) and 1247120 (0.122 sq ft, $22.54/sq ft) — now the fourth confirmed sub-scope data point. The resulting tier ladder is identical to 1247120's, but this is documented explicitly as NOT a direct parity exemption — both items were priced independently and happened to converge.

**Key Decisions:**
- Wave 1: 4/6 models independently landed at $2.75 (matching 1247120); 2/6 at $3.00 (steeper). Wave 2 (5/6 responded): unanimous kill of $3.00 — it produced $23.08/sq ft, exceeding 1247120's $22.54/sq ft despite 3020477 being the larger label, a gradient inversion. Surviving candidates split 3/5 $2.75 vs 2/5 $2.85 (strict interpolation).
- Wave 3: 6/6 unanimous instant approval on $2.75; $2.85 drew a polite (non-blocking) clarification question in every simulation that saw it.
- Wave 4: 6/6 unanimous YES on $2.75. Decisive reasoning: $2.85's tighter mathematical fit was outweighed by (a) introduced buyer friction for an immaterial $0.10/label difference, and (b) exposing Pro Label's interpolation methodology to Sean, who is actively co-developing a procurement/engineering labeling standard — a real strategic cost for no real benefit. $2.75 locked, no override.
- Material cost $0.25/label (§25 canonical: $0.2534 calculated, filed $0.25). Margin ~90.9% at qty 20.

**Strategic Flags:**
- Sub-scope gradient now monotonic across four points: $22.54 (0.122 sq ft) → $21.15 (0.130 sq ft) → $20.95 (0.148 sq ft) → $16.27 (0.292 sq ft).
- First article not requested by Sean — status unconfirmed, not a confirmed "No." Order quantity also not specified. Both flagged for follow-up alongside the quote.
- Item count: 36 → 37. Printed/Laminated category: 24 → 25 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 37 rows confirmed in Supabase.

---

### 2026-06-30 — Session AF (bug fix): hydrateFromDb() variants drop — dual-variant display now renders on live Supabase path

**What:** One-line fix in `frontend/index.html` `hydrateFromDb()`. The merge block that assembles the runtime `items` object was copying `image` and `sections` from static `data.json` but omitting `variants`. Because Supabase has no variants column, `data.json` is the sole source of variant data — so on the live Supabase path `item.variants` was always `undefined`, causing `renderPricing()` and `renderItemStats()` to fall through to single-variant rendering for P/N 3017557. Added `variants: st.variants || null` to the merge block alongside `image` and `sections`.

**Key Decisions:**
- Fix is entirely in `hydrateFromDb()` — no changes to `renderPricing()`, `renderItemStats()`, `build_frontend.py`, Supabase schema, or any item/category/pricing files.
- Null fallback matches existing code style for `image` and `sections`; single-variant items unaffected (get `variants: null`, which the renderer already handles).

**Strategic Flags:**
- Any future multi-variant item will automatically benefit from this fix — `variants` will now be hydrated for all items that have it in `data.json`.

**Status:** Complete — minimal targeted fix, no pricing or schema changes.

---

### 2026-06-30 — Session AE (item update): P/N 3017557 — added dual-variant display (5-mil + 10-mil), per-variant Copy for Email

**What:** Structural update to P/N 3017557 (LBL-BASKET CONTROL BOX SINGLE AXIS). The frontend dashboard was only displaying ONE variant (Variant B, 10-mil). Sean requested pricing for BOTH 5-mil and 10-mil polycarbonate overlaminate options. Added variant-specific frontmatter fields (variant_count: 2, variant_a_*, variant_b_*) to the item file. Updated build_frontend.py to detect and extract variant data into data.json. Updated the dashboard to render two clearly separated pricing sections — "Variant A — 5-mil Polycarbonate Overlaminate" and "Variant B — 10-mil Polycarbonate Overlaminate" — each with its own stat cards, volume pricing table, and independent "Copy for Email" button. Multi-variant schema pattern documented in governance/STRUCTURE_RULES.md. Category file updated to note both variant bands ($24.27/sq ft for 5-mil, $27.90/sq ft for 10-mil). No pricing changes — both tier tables are locked.

**Key Decisions:**
- Variant frontmatter uses flat-key prefixes (variant_a_*, variant_b_*) for compatibility with the simple YAML parser. Primary `price_*` fields still hold Variant B (primary) for backward compatibility with validate.py and migration scripts.
- First Article ($75.00) is shared across both variants — displayed once with a note, not duplicated per variant.
- Each variant has its own Copy for Email button producing output with ONLY that variant's tier table.
- This is a display/structure fix, not a new item — item_count remains 36.

**Strategic Flags:**
- The multi-variant schema pattern is now documented in governance/STRUCTURE_RULES.md and available for future items that need multiple pricing variants on a single P/N.
- No pricing recalculation — both tier tables were locked by Nick in Session AD.
- Item count unchanged at 36.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 36 rows confirmed in Supabase.

---

### 2026-06-30 — Session AD (new item): P/N 3017557 — founding Convex/polycarbonate item, material-proportional scaling, $30.75/$26.75 at qty 20

**What:** New panel decal — LBL-BASKET CONTROL BOX SINGLE AXIS at 17.75" × 8.9375" = 1.102 sq ft. FOUNDING item for the Convex High Bond + Polycarbonate material family. Two laminate variants quoted on one P/N: Variant B (10-mil Kapco, primary, in stock) at $30.75/qty 20 = $27.90/sq ft, material cost $4.00; Variant A (5-mil PC, supplier provisional) at $26.75/qty 20 = $24.27/sq ft, material cost $3.50. Pricing derived by material-proportional scaling from the Orajet singles band: interpolated Orajet $/sq ft at 1.102 sq ft (~$15.48) × material cost ratio (1.800× Var B, 1.569× Var A) = Convex/PC $/sq ft. Category file `categories/convex-high-bond-polycarbonate.md` transformed from SHELL to active with full Pricing Profile, band data, tier ratios, decision tree. Three material files updated (`used_in_items` → ["3017557"]). First article $75.00. Lifetime warranty embedded in margin.

**Key Decisions:**
- Pricing LOCKED by Nick — no multi-round AI validation run. Override type: Strategic Anchor.
- Material-proportional scaling is the governing methodology. The Orajet band ($15.43–$15.91/sq ft) does NOT apply directly — the Convex/PC band is a scaled derivative.
- §29 (ANSI account rule for Orajet/lam) does NOT extend to the Convex/PC family. This item is not ANSI — it is a control panel overlay.
- Rollsroller flat laminating table handles all Convex/PC lamination (NOT the 13.5" polyester laminator). Lamination passes: 1.
- Frontmatter uses Variant B (primary) pricing. Both variants documented in Pricing, Material Cost, and Margin sections.

**Strategic Flags:**
- Strategic Anchor — this price establishes the founding $/sq ft band for the entire Convex/polycarbonate material family. Every future Convex/PC item scales from this data point.
- External market research ($40–$70/sq ft) confirmed price sits ~30% below market floor — consistent with the ~25–30% relationship concession on the Orajet band.
- Combination B (10-mil Kapco) is in stock. Combination A (5-mil) supplier is provisional.
- Item count: 35 → 36. Panel Decals category: 0 → 1 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 36 rows confirmed in Supabase.

---

### 2026-06-29 — Session AC (audit + new material family): Convex/polycarbonate material family shell — 3 new material files + category shell

**What:** Read-only audit of full repo (9-section structured report: §25 formula, band routing, per-label floor, tier table construction, ANSI rule, validation tiers, calculator role, Supabase sync, gaps/inconsistencies). New material family shell: (1) `materials/convex-6mil-high-bond.md` — 30" × 150 ft = 375 sq ft, $599.13/roll, $1.5976/sq ft, supplier Convex (provisional); (2) `materials/5mil-polycarbonate-overlaminate.md` — 51" × 150 ft = 637.5 sq ft, $612.00/roll, $0.9600/sq ft, supplier provisional; (3) `materials/10mil-polycarbonate-overlaminate.md` — Kapco KJ10VPC/38/150, 38" × 150 ft = 475 sq ft, $670.00/roll, $1.4105/sq ft, in stock at Kapco, single-roll buying. Category shell: `categories/convex-high-bond-polycarbonate.md` (SHELL — no items, no pricing profile). MASTER_CONTEXT.md Convex row updated. ARCHITECTURE.md Panel Decals row updated. PRODUCTION.md Convex/polycarbonate material costs added. Item count unchanged at 35.

**Key Decisions:**
- Two laminate combinations documented: Combination A (5-mil) = $3.0576/sq ft combined; Combination B (10-mil Kapco) = $3.5081/sq ft combined. Both vs Orajet/lam at $1.9489/sq ft — panel decals price significantly higher.
- §25 ink ($0.50/sq ft) applies to Convex items. §29 (ANSI by account rule) does not extend to Convex family — ANSI status evaluated per item. §30 ($0.25 increment rule) applies.
- No pricing this session. Band anchors, decision tree, pricing profile = PLACEHOLDER until first item spec received from Sean.
- The 13.5" polyester laminator cannot handle 30" Convex base material. Polycarbonate lamination method (wide-format process) TBD at first item quote.

**Strategic Flags:**
- Supplier status provisional on Convex base and 5-mil lam — replacement suppliers may be evaluated before first production run.
- Combination B (10-mil Kapco) is in stock and ready to source. Combination A (5-mil) supplier unconfirmed.
- Audit finding: CALCULATOR.md still references `production_override: true` path removed in Session Z — documentation artifact, low priority.
- Item count: unchanged at 35.

**Status:** Complete — validate.py 0/0; build_materials.py 3 new materials; no Supabase migration (no new items).

---

### 2026-06-29 — Session AB (new items + governance): P/Ns 1279260 and 1279270 — FRONT/REAR TIRE PRESSURE labels; §30 $0.25 increment rule

**What:** Two new printed/laminated single labels: 1279260 (FRONT TIRE PRESSURE 120 PSI, UNIT 8835) and 1279270 (REAR TIRE PRESSURE 90 PSI, UNIT 8825). Both 4.750" × 1.000" = 0.033 sq ft, Orajet 3951 Cast + Polyester Lam, Print/Lam/Cut 1 pass. Sub-0.06 sq ft — per-label floor governs at $2.75/qty 20 per §29 (ANSI account rule). Tier table locked: $4.25/$3.25/$2.75/$2.50/$2.25/$2.00 — parity with 3024592. Material cost $0.10 (§25 canonical: $0.0643 calculated + incidental buffer). Margin ~96.4% at qty 20. Primary comparable: 3024592 (identical tier table, same per-label floor governance). Pricing locked per session prompt — no 4-wave AI validation run. §30 added to governance/PRICING_RULES.md: all tier prices must be in $0.25 increments (forward-looking only, existing items grandfathered). §30 requirement also added to governance/VALIDATION_PROMPTS.md Wave 1 Required Output Schema.

**Key Decisions:**
- Per-label floor governs at $2.75/qty 20 per §29 ANSI account rule. Linear Micro-Format Band formula ($30.86/sq ft × 0.033 = $1.02) is inapplicable — overridden by floor.
- Tier table matches 3024592 exactly. All tiers in $0.25 increments per new §30 rule.
- Material cost $0.10 — same as 3024140 despite different dimensions; material negligible at this size class.
- No first article price on either item. No 4-wave AI validation — pricing locked per session prompt.

**Strategic Flags:**
- Both items are band data points for the sub-0.06 sq ft per-label floor (ANSI). The $2.75 floor at qty 20 is now confirmed across three independent items (3024592, 1279260, 1279270).
- §30 ($0.25 increment rule) applies to all new items from this session forward. Existing items are grandfathered.
- Item count: 33 → 35. Printed/Laminated category: 22 → 24 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 35 rows confirmed in Supabase.

---

### 2026-06-29 — Session AA (governance): Hardcode ANSI for all Orajet/lam items; remove calc-ansi checkbox; §29 added

**What:** Account-level rule change — all items printed on Orajet 3951 with polyester laminate are ANSI by definition going forward. Removed the `calc-ansi` checkbox and its `calc-ansi-wrap` wrapper from the calculator UI entirely. Removed `is_ansi_safety` from `gatherCalcInputs()`, `runCalculator()` defaults, `inputsForPN()` sanity-check helper, and two inline sanity test objects. Added fixed line "ANSI: Yes — account rule (all Orajet/lam items)" to `generateBrief()` for all printed/lam routes. Added §29 to `governance/PRICING_RULES.md` documenting the account-level ANSI rule. Updated `governance/CALCULATOR.md` Step 2 and Last Updated header. Updated `categories/printed-laminated-orajet.md` per-label floor section: $2.75 is the governing floor for all future sub-0.06 sq ft items; $2.50 floor is historical (3024140 / 1012080 only). No items added or repriced. No Supabase seed required (no item data changed).

**Key Decisions:**
- `is_ansi_safety` was collected from the checkbox but never used in any ANSI/non-ANSI branching in the per-label floor logic — removal is purely UI/brief cleanup, no engine routing changes.
- The `calc-ansi-wrap` div and all references to `calc-ansi` / `is_ansi_safety` removed exhaustively: HTML, `gatherCalcInputs()`, `runCalculator()` defaults, `inputsForPN()` helper, and two inline test objects.
- Brief now shows fixed "ANSI: Yes — account rule (all Orajet/lam items)" in the FUNDAMENTALS section for all printed/lam routes.
- §29 codifies: all Orajet/lam items are ANSI by default; $2.75 floor governs new items; $2.50 non-ANSI floor is historical data only (3024140 and 1012080 only).

**Strategic Flags:**
- The $2.50 per-label floor (3024140, 1012080) remains unchanged — those two items were priced under the prior framework and are grandfathered. Do NOT apply $2.50 to any future item.
- The governing floor for all new sub-0.06 sq ft production items is $2.75 (ANSI), per §29.
- Item count unchanged at 33. No Supabase changes needed.

**Status:** Complete — validate.py 0/0; all three build scripts clean; item_count = 33.

---

### 2026-06-29 — Session Z (bug-fix + governance): Remove tiny route + $55 floor from engine; fix inkComponent crash; §28 fully implemented in calculator

**What:** Two-part calculator fix. FIX 1: inkComponent() crash on production_override inputs — two-part fix: (1A) added canonical ink_rates fallback in assembleConfigFromDb() so the full_bleed_flood_coat entry is always present even when Supabase settings.extra doesn't include it; (1B) added null guard in inkComponent() with `config.ink_rates || {}` and improved !def fallback to `r(sq_ft_per_label * 0.50, 4)`. FIX 2: §28 no-floor doctrine fully implemented in calculator — removed the tiny route and $55 floor entirely. Removed buildTinyTiers() function, production_override checkbox UI, all `route === 'tiny'` guards throughout engine (renderCalcOutput, renderCalcSummary, lam passes, tier build, tier enforcement, never-pay-more check, generateBrief). F9 flag definition changed to RETIRED/INFO (suppresses_output: false). All sub-0.1 sq ft items now unconditionally route to single_sub_scope (Micro-Format Band). Sanity test 1277970 (tiny route) removed; PROD-OVERRIDE test renamed MICRO-BAND. build_calculator_config.py: account.floor→null, DO_NOT_BENCHMARK updated to remove "$55 floor pricing" language, tiny_one_off_program marked RETIRED. Supabase elliott_account_settings: floor_value seeded to 0 (column NOT NULL), floor_label updated to §28 text. validate.py 0/0; all three build scripts clean; elliott_items = 33 confirmed.

**Key Decisions:**
- FIX 1 root cause: previous hydrateFromDb() patch (21937f6) was a post-assembly workaround; FIX 1A fixes assembleConfigFromDb() directly; FIX 1B adds defensive guard in inkComponent() as belt-and-suspenders.
- FIX 2 approach: single unconditional branch for sub-0.1 sq ft items — no production_override escape hatch. §28 doctrine means ALL items price from job economics or Micro-Format Band, never from a flat floor.
- F9 flag kept in flag registry (as RETIRED/INFO) for historical audit trail; suppresses_output: false so it can be surfaced for diagnostic purposes but no longer emitted on any live route.
- Supabase floor_value set to 0 (not NULL) due to NOT NULL column constraint; floor_label updated to §28 text. The 0 value is semantically correct — "no floor."

**Strategic Flags:**
- Calculator engine is now §28-compliant. Any sub-0.1 sq ft item is priced from Micro-Format Band, not from a flat floor.
- DO_NOT_BENCHMARK entries for 1277970/1277980/1277990/1278000/3017583/3017584 now reference "historical job-economics pricing" rather than "$55 floor pricing" — accurate framing post-§28.
- Item count unchanged at 33. No new items added this session.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 33 confirmed.

---

### 2026-06-22 — Session Y (governance): Remove $55 floor — no-floor job-economics doctrine + deep-tier standing instruction

**What:** Two targeted governance-only changes — no items added or changed. (1) Removed the $55 one-off job-economics floor as a forward-looking rule from all five governance/category docs (PRICING_RULES.md, CALCULATOR.md, VALIDATION_PROMPTS.md, categories/printed-laminated-orajet.md, MASTER_CONTEXT.md). Added the no-floor job-economics doctrine as §28 in PRICING_RULES.md. §27 rush/favor floor ($50) is intact and unchanged. (2) Added deep-tier standing instruction to VALIDATION_PROMPTS.md §3 Wave 1 prompt template: the 100-199 and 200+ tiers are structural scaffolding only — clean round numbers stepping down monotonically from the 50-99 tier are sufficient; these tiers rarely transact (Sean's pattern is batches of 20-50). Historical pricing records in items/ untouched. validate.py 0/0; all three build scripts clean; elliott_items = 33 confirmed.

**Key Decisions:**
- No-floor doctrine: Every job priced from actual job economics (material cost + realistic production time). No minimum order charge, no job floor. For sub-0.1 sq ft production items → Micro-Format Band. For one-off field service → job economics only; Nick decides.
- $55 removed only as a forward-looking rule. Historical records in items/ and category files (outrigger program 1277970-1278000, standalone one-offs 3017583/3017584) are accurate history and were NOT altered.
- Calculator CALCULATOR.md: `tiny` route retained; $55 output is a technical implementation placeholder, not documented as an Elliott account floor. Route table, F9 flag, constants list, and Step 9 all updated.
- VALIDATION_PROMPTS.md: deep-tier standing instruction positioned between rush/favor floor and Required Output Schema in Section 3.

**Strategic Flags:**
- §28 is now the canonical reference for the no-floor doctrine on this account. All future sessions that encounter a one-off or field service request should route here.
- Deep-tier instruction applies to every Wave 1 prompt going forward — models should no longer obsess over exact cents at the 100-199/200+ tiers.
- Item count unchanged at 33. No Supabase structural changes — only governance docs updated.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 33 rows confirmed in Supabase.

---

*Entries older than Session Y (2026-06-22) were removed per the 10-entry rolling window — git history retains them in full.*
