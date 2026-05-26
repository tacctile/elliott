# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> Last Updated: 2026-05-26

---

### 2026-05-26 — Material Cost Update + Status Change + Frontend Enhancement

**What:** Three coordinated updates: (1) Cardinal Red 24" × 10yd price increased $153.60 → $162.78 and 24" × 50yd added at $775.10 as the preferred roll for current volume; (2) P/N 1186310 moved Quoted → In Production after first PO (qty 20, $700.00) — nesting method updated to 2-wide canonical reflecting production reality; (3) frontend dashboard exposed `material_cost_per_unit` and `margin_at_qty_20` for internal margin visibility and added a tooltip/legend system so every field is self-documenting.

**Items Affected:**
- 1205720 — Material cost recalculated using single-nest length-based method at new Cardinal Red price: $7.62 → $15.86. Margin @ qty 20: ~78% → ~55%. Conservative figure pending E190's first production run; expected to converge to ~$8.16 once 2-wide nesting is confirmed in production. Methodology divergence from 1186310 documented.
- 1186310 — Status Quoted → In Production (first PO: qty 20, $700.00). Nesting corrected to 2-wide canonical (actual production reality). Material cost: $7.62 → $8.16 (combines Cardinal Red price increase + methodology). Margin @ qty 20: ~78% → ~77%.
- 3018378 — Olympic Blue price reverified 2026-05-26 at $162.78/roll — unchanged. No material cost change. Verification note added.

**Files Modified:**
- `governance/PRODUCTION.md` — Cardinal Red 10yd updated to $162.78; 50yd added at $775.10 as preferred roll; Verified dates → 2026-05-26 for both Cardinal Red rows and Olympic Blue (reverification); Cut Vinyl quick reference rewritten to reflect single-nest (1205720), 2-wide canonical (1186310), and 50yd improvement
- `items/1205720.md` — frontmatter material_cost_per_unit 7.62 → 15.86, margin_at_qty_20 ~78% → ~55%, cost_version_date → 2026-05-26; Material Spec roll sizes updated; Nesting and Material Cost section rewritten with single-nest methodology; Margin Analysis split into conservative (single-nest) and projected (2-wide) tables; methodology divergence note added in Notes and Warnings
- `items/1186310.md` — frontmatter status Quoted → In Production, material_cost_per_unit 7.62 → 8.16, margin_at_qty_20 ~78% → ~77%, cost_version_date → 2026-05-26, date_in_production added; Item Overview status updated; Material Spec roll sizes updated; Nesting and Material Cost section rewritten with 2-wide canonical methodology and explicit divergence from 1205720; Margin Analysis updated with first-production-order detail; notes updated
- `items/3018378.md` — Material Spec roll-size verification note; Notes and Warnings reverification confirmation
- `categories/cut-vinyl-3m-180mc.md` — Items table status for 1186310 → In Production; Pricing Profile bands updated to reflect new material costs and methodology split; Key variables section expanded with roll-length and nesting-confirmation guidance
- `.claude/ARCHITECTURE.md` — 1205720 margin column updated to reflect dual figures (conservative/projected); 1186310 margin → ~77%, status → In Production; Last Updated → 2026-05-26
- `scripts/build_frontend.py` — removed `material_cost_per_unit` and `margin_at_qty_20` from STRIP_FIELDS; added explanatory comment
- `frontend/index.html` — added Legend panel with full field-definition table; added title-attribute tooltips throughout (header, stat row, pricing table, info cards); rendering functions made null-safe for items where `material_cost_per_unit` is missing
- `frontend/data.json` — rebuilt; material_cost_per_unit and margin_at_qty_20 now present in item output (item_count = 7)
- `.claude/STATE.yml` — session state updated; 1186310 removed from pending_quotes (now In Production)

**Key Decisions:**
- 1205720 (no production run yet) carries the conservative single-nest figure ($15.86) until E190 confirms 2-wide in production. 1186310 (production-confirmed) uses 2-wide canonical ($8.16). Documentation discipline, not a real production difference — same drawing, same dimensions.
- Cardinal Red 24" × 50yd preferred for current volume but canonical material cost retains 10yd figure per Structure Rules ("higher cost scenario / smaller roll"). 50yd improvement (~4.8%) documented in prose, not frontmatter.
- Frontend: kept tooltips minimal and consistent with existing UI (title attributes + dotted-underline visual cue). Added a collapsible Legend panel as the canonical field reference. No UI redesign.
- Build script: `cost_version_date` and `override_type` remain stripped (per explicit task constraint: only material_cost_per_unit and margin_at_qty_20 unstripped). Stat row's "as of {cost_version_date}" subtitle dropped because the field is no longer in data.json.

**Status:** Complete. validate.py 0 errors, 0 warnings.

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
