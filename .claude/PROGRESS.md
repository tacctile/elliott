# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> Last Updated: 2026-05-27

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
