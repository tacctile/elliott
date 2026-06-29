# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> **Rolling window: 10 entries max. When adding an 11th, remove the oldest. Git retains all history.**
>
> This file is the session memory layer: why decisions were made, what changed strategically, what a future session needs to know. It is not a commit log and not a validation archive — full validation records live in `items/*.md` (Pricing Derivation), file-level changes live in git history, and structure/math compliance is enforced by `scripts/validate.py`. Entry format (template in `.claude/COMPLETION_TEMPLATES.md`): What / Key Decisions / Strategic Flags / Status, 10–25 lines per entry, no other sections.
>
> Last Updated: 2026-06-29 (Session Z — tiny route + $55 floor removed from calculator engine; inkComponent crash fixed; §28 fully implemented in calculator. Item count unchanged at 33.)

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

### 2026-06-22 — Session X (new item): P/N 1012080 — LABEL, PTE SINGLE STICK CONTROLLER, Micro-Format Band parity-governed, $2.50 at qty 20, 4-wave validated

**What:** New printed/laminated single label (LABEL, PTE SINGLE STICK CONTROLLER) at 2.8125" × 3.9375" = 0.077 sq ft. Micro-Format Band, parity-governed at qty 20. At 0.077 sq ft, above the ~0.06 sq ft per-label floor threshold — floor does NOT govern. Linear Micro-Format Band formula ($30.86/sq ft × 0.077 = $2.38); qty-20 price set to $2.50 by parity with P/N 3024140 (non-ANSI control label family, $2.50 at qty 20). First controller/panel label on the Elliott account. Model blank on drawing — P/N is the identifier. 4-wave atomic AI validated (24 independent responses, 6 models × 4 waves). Wave 4: 6/6 unanimous YES. Tier table: $3.75/$2.90/$2.50/$2.20/$1.95/$1.90. Material cost $0.16 (§25 canonical: $0.1501 calculated + $0.0099 buffer). Margin ~93.6% at qty 20.

**Key Decisions:**
- Parity governs over the linear formula at 0.077 sq ft: $2.50 (parity with 3024140) over $2.38 (linear formula output). The per-label floor (sub-0.06 sq ft) does NOT apply at 0.077 sq ft — above the threshold.
- 200+ raised from initial $1.75 to $1.90 per Wave 2 structural finding: $1.75 sat 30% below the $2.50 anchor and would have anchored the controller/panel label catalog family below floor. Wave 4 unanimous YES on the corrected table.
- Added to BAND_EXCEPTIONS in validate.py: $32.47/sq ft (= $2.50 ÷ 0.077) exceeds band anchor upper bound ($30.86 × 1.015 = $31.32). Exception documented with parity rationale and 4-wave validation date.
- NOT a new independent Micro-Format Band data point — band anchor stays at 1279000 at $30.86/sq ft. Parity governed from 3024140.

**Strategic Flags:**
- First controller/panel label on the Elliott account. Future controller/panel labels should reference both 3024140 ($2.50, non-ANSI floor anchor) and 1012080 ($2.50 at 0.077 sq ft, parity-governed above the floor threshold) as the two data points for this family.
- The $2.50 price point is inherited from the non-ANSI control label floor — if 3024140 ever changes, 1012080's parity basis changes with it.
- Item count: 32 → 33. Printed/Laminated category: 21 → 22 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 33 rows confirmed in Supabase.

---

### 2026-06-22 — Session W (new item): P/N 1279130 — LBL-MOVING OR WARNING E-SERIES, sub-scope single, $3.10 at qty 20, 4-wave validated

**What:** New printed/laminated single label (LBL-MOVING OR WARNING E-SERIES) at 10.00" × 2.13" = 0.148 sq ft. Sub-scope routing (0.1–0.5 sq ft range). Third confirmed sub-scope data point, joining 1247120 (0.122 sq ft, $22.54/sq ft) and 1210810 (0.292 sq ft, $16.27/sq ft). $3.10 at qty 20 = $20.95/sq ft — sits correctly between the two brackets. Sub-scope $/sq ft gradient now monotonic across three points: $22.54 → $20.95 → $16.27. 4-wave atomic AI validated (24 independent responses, 6 models × 4 waves). Wave 4 unanimous YES 6/6. Tier table: $4.75/$3.50/$3.10/$2.55/$2.30/$2.00. Material cost $0.29 (§25 canonical: $0.2885 calculated + incidental buffer). Margin ~90.6% at qty 20. Model blank on drawing — P/N is the identifier.

**Key Decisions:**
- Wave 2 structural finding adopted: 100–199 raised $2.25→$2.30 to clear singles band floor ($15.43/sq ft); at $2.30 the implied $/sq ft is $15.54 — clears by $0.11/sq ft. Internal tripwire documented. 200+ raised $1.85→$2.00 to eliminate anchor risk.
- do_not_benchmark = false (valid sub-scope data point); excluded from singles band DATA POINTS until production-volume acceptance.
- Added to BAND_EXCEPTIONS in validate.py with rationale documenting the sub-scope premium and the 100-199 tripwire.
- Quote email anchor line: "Pricing is consistent with the 1247120 and 1210810 brackets you've already approved."

**Strategic Flags:**
- Three-point sub-scope gradient now established — sufficient for interpolation on future items between 0.1–0.5 sq ft. The curve is calibrated at 0.122, 0.148, and 0.292 sq ft.
- The 100-199 tier at $2.30 ($15.54/sq ft) operates with minimal headroom above the singles band floor ($15.43/sq ft). Any material cost increase on this account requires checking this tier first.
- Item count: 31 → 32. Printed/Laminated category: 20 → 21 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 32 rows confirmed in Supabase.

---

### 2026-06-17 — Session V (item update): P/N 1278930 — 3-label kit → 2-label kit, tiers now match 1278890

**What:** Updated P/N 1278930 (CHRT-E190 V3, Lifting Capacity Chart Kit) from a 3-label kit to a 2-label kit. Label dimensions unchanged (11.13" × 7.88" = 0.609 sq ft/label). sq_ft_per_kit updated 1.827 → 1.218. material_cost_per_unit updated $3.60 → $2.40 (§25 canonical: 1.218 × $1.9489 = $2.374 + incidental buffer = $2.40, identical to 1278890). All 6 tier prices updated to match 1278890 exactly ($30/$24/$20/$17/$14/$12 vs prior $45/$36/$30/$26/$21/$18). per_label_at_qty_20 unchanged at $10.00; margin_at_qty_20 unchanged at ~88%. Documentation and pricing update only — no items added or removed.

**Key Decisions:**
- Per-label parity governs: same label dimensions (11.13" × 7.88"), same material (Orajet 3951 + 1-mil polyester lam), ≤2 lam passes — per-label parity applies per PRICING_RULES.md §1–§2. Tier table identical to 1278890, validated by 1278890's 4-wave atomic AI process (24 runs, 6 models × 4 waves, Wave 4 unanimous YES at $10.00/label).
- Material cost per §25 canonical formula for 1.218 sq ft: Orajet 1.218 × $1.21 = $1.474 + lam 1.218 × $0.2389 = $0.291 + ink 1.218 × $0.50 = $0.609 = $2.374 + incidental buffer = $2.40 (matching 1278890 exactly).
- Historical 3-label derivation (25 model runs / 6 rounds, 1.5x off 1230820) preserved in Pricing Derivation section as superseded reference.
- First article price ($65) and status (FA Accepted) unchanged — FA was for the original structure and is historical.

**Strategic Flags:**
- All three kit-family members (1278890, 1278930, 1245130) now explicitly maintain three-way per-label parity at $10.00/label at qty 20. 1278930 now matches 1278890's tier table exactly. January 2027 normalization strategy unchanged.
- Item count unchanged at 31. No new Supabase rows required — updating existing row for 1278930.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 31 rows confirmed in Supabase.

---

### 2026-06-17 — Session U (new items): P/Ns 1277300 and 1279020 — direct parity clones of 1278980, $9.50 at qty 20, singles band

**What:** Created P/N 1277300 (LABEL-LIFTING CAPACITY CHART MODEL E160 V3 NO WINCH) and P/N 1279020 (LABEL-RANGE CAPACITY CHART MODEL E190 V3) as direct parity clones of 1278980 (LABEL-PLTFM RANGE CAPACITY CHART MODEL E160 V3). All three items share identical dimensions (7.88" × 11.13" = 0.609 sq ft), material family (Orajet 3951 Cast + Polyester Lam), process (Print/Lam/Cut, 1 pass), material cost ($1.19/label, §25 canonical), and tier table ($14.50/$11.50/$9.50/$8.25/$7.50/$6.75). Only part numbers, descriptions, and artwork content differ.

**Key Decisions:**
- Direct parity exemption applied per `governance/PRICING_VALIDATION.md` — no multi-round AI validation run for either clone; 1278980's 4-wave atomic validation (24 independent responses, 6 models × 4 waves) is inherited by both.
- Rule 15 (Pricing Profile band check) satisfied for both: $9.50 at qty 20 = $15.60/sq ft lands within the singles band ($15.43–$15.91/sq ft).
- Neither clone is a new independent band data point — the 0.609 sq ft position is anchored by 1278980 exclusively. Band data point count remains 4.
- Permanent three-way lockstep established: any future change to 1278980's dimensions, material cost, process, or tier table must be applied to both 1277300 and 1279020 in the same session.
- Lockstep note added to 1278980.md Notes and Warnings section per governance requirement.

**Strategic Flags:**
- Three items now share the 0.609 sq ft / $9.50 tier table. Sean has multiple singles at this exact size — the table is the permanent reference for all E160 V3/E190 V3 capacity chart singles at this geometry.
- Item count: 29 → 31. Printed/Laminated category: 20 → 22 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 31 rows confirmed in Supabase.

---

### 2026-06-16 — Session T (new item): P/N 3024140 — LBL-WRK LGHTS, smallest item on account (0.019 sq ft), $2.50 at qty 20, 4-wave validated, complexity-dependent floor

**What:** New printed/laminated single label (LBL-WRK LGHTS) at 2.000" × 1.375" = 0.019 sq ft — the smallest production catalog item on the Elliott account. Drawing dated 10/23/24, engineer LKM, model blank. Non-ANSI equipment control label (+ WORK LIGHTS / ON / OFF, black on white, interior Ø1/2" circle cutout). Sub-0.06 sq ft: per-label floor governs AND is complexity-dependent. 4-wave atomic AI validated (24 independent responses, 6 models × 4 waves). $2.50 at qty 20 — intentionally below 3024592 ($2.75, ANSI Z535.6 DANGER) per complexity differentiation. Tier table: $4.00/$3.00/$2.50/$2.25/$2.00/$1.75. Material cost $0.10 (§25 canonical: $0.038 calculated + incidental buffer). Margin ~96.0% at qty 20.

**Key Decisions:**
- Wave 1 (6/6) initially proposed $2.75 mirroring 3024592, citing complexity offset (interior Ø1/2" cutout vs simpler color scheme). Wave 2 (6/6 H on all four attack vectors) rejected: cutout adds ~5–10 sec weeding; eliminated ANSI compliance labor (multi-color registration, compliance inspection) exceeds cutout labor. True non-ANSI floor is below 3024592.
- Wave 3: 3/6 approved at $2.75; 3/6 pushed back (threshold $2.25–$2.50, instant approval $1.50–$2.25).
- Wave 4: 6/6 unanimous NO on $2.75; 6/6 unanimous YES on $2.50. Engine consensus accepted, no override.
- Complexity-dependent per-label floor now confirmed with two live data points: ANSI regulated → $2.75 (3024592); simple non-ANSI → $2.50 (3024140). Documented in categories/printed-laminated-orajet.md.
- do_not_benchmark = false. Added to BAND_EXCEPTIONS in validate.py ($/sq ft artifact, $131.58, is inapplicable).

**Strategic Flags:**
- Per-label floor is now formally complexity-dependent — this is a doctrinal addition. Future sub-0.06 sq ft items must classify complexity (ANSI vs non-ANSI) before applying the floor.
- Item count: 28 → 29. Printed/Laminated category: 19 → 20 items.
- The $/sq ft implied rate ($131.58 at qty 20) is a mathematical artifact. Never benchmark against it.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 29 rows confirmed in Supabase.

---

### 2026-06-16 — Session S (new item): P/N 1247120 — LBL-DNGR TIP-OVER HAZARD, sub-scope single, $2.75 at qty 20, 4-wave validated

**What:** New printed/laminated single label (LBL-DNGR TIP-OVER HAZARD) at 4.0000" × 4.3750" = 0.122 sq ft, ANSI Z535.6 DANGER class. Sub-scope routing (0.1–0.5 sq ft range). Governing comparable: 1210810 ($16.27/sq ft at qty 20). $2.75 at qty 20 = $22.54/sq ft — intentionally above 1210810 per sub-scope premium doctrine (smaller label carries higher $/sq ft). Closes absolute-price inversion against 3024592 ($2.75 for 0.054 sq ft) — both at $2.75 per unit; larger label not cheaper. 4-wave atomic AI validated (24 responses, 6 models × 4 waves). Tier table: $4.25/$3.25/$2.75/$2.25/$2.00/$1.75. Material cost $0.25 (§25 canonical, $0.2377 calculated + incidental buffer). Margin at qty 20: ~90.9%.

**Key Decisions:**
- Sub-scope routing confirmed (0.122 sq ft, 0.1–0.5 sq ft range) — not singles band, not Micro-Format Band.
- Wave 4 consensus: 4 NO (all recommending $2.75 at qty 20) / 2 YES on as-shown table; Nick accepted the $2.75 correction.
- do_not_benchmark = false (unlike 1210810 which is in DO_NOT_BENCHMARK) — 1247120 is a valid sub-scope data point; future sub-scope items in the 0.1–0.5 sq ft range may reference it.
- Excluded from singles band DATA POINTS until production-volume acceptance confirmed by Nick.
- 1247120 added to BAND_EXCEPTIONS in validate.py (sub-scope singles require documented exception per band-membership check logic).

**Strategic Flags:**
- Second confirmed sub-scope data point (0.1–0.5 sq ft range) on the account. Sub-scope $/sq ft gradient now confirmed monotonic: $22.54 (0.122 sq ft) > $16.27 (0.292 sq ft) > $15.43–$15.91 (singles band).
- Item count: 27 → 28. Printed/Laminated category: 18 → 19 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 28 rows confirmed in Supabase.

---

### 2026-06-16 — Session R (new item): P/N 3024592 — first sub-0.06 sq ft production item, per-label floor $2.75 at qty 20, 4-wave validated

**What:** New printed/laminated single label (LBL-FALL PRTCT ANCHRG 1 PERSON) at 4.750" × 1.625" = 0.054 sq ft, ANSI Z535.6 DANGER class. First production catalog item below 0.06 sq ft on the Elliott account. The Micro-Format Band linear formula ($30.86/sq ft × 0.054 = $1.67) is overridden by the per-label floor documented in 1279000. Floor anchor confirmed at $2.75 at qty 20 by 4-wave atomic AI validation (24 responses, 6 models × 4 waves). Tier table: $4.25/$3.25/$2.75/$2.50/$2.25/$2.00. Material cost $0.20 (§25 canonical, same as 1279000 despite smaller area). Margin at qty 20: ~92.7%. This item IS a band data point for the sub-0.06 sq ft floor.

**Key Decisions:**
- Per-label floor ($2.75 at qty 20) governs over the linear $/sq ft formula ($1.67) — documented with full derivation in items/3024592.md Pricing Derivation section.
- 200+ tier at $2.00 is below the ~$2.50–$3.00 per-label floor band minimum — accepted as structural completeness; Sean orders 20–50 batches; same pattern as 1279000's 200+ at $2.10.
- This item IS a band data point (do_not_benchmark = false) — the floor of $2.75 at qty 20 anchors future sub-0.06 sq ft items. Future items must validate fresh against job economics; do NOT clone $2.75 mechanically.
- Quote email anchor (Wave 4 validated): "Same material and process as P/N 1279000/1278220 — no file prep charge, no first article."
- Sub-0.06 sq ft floor caution in categories/printed-laminated-orajet.md updated from anticipated to confirmed.

**Strategic Flags:**
- First time the per-label floor has been invoked on a live production item at this account. The $2.75 anchor is now visible to Sean — he will log it alongside 1279000's $3.00 and compare when future sub-0.1 sq ft items arrive.
- Item count: 26 → 27. Printed/Laminated category: 17 → 18 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 27 rows confirmed in Supabase.

---

### 2026-06-12 — Session Q (governance): Prompt template hardening — On Completion block, Prompt Writing Rule 9, Acceptance Criteria Rules section

**What:** Hardened the new-item prompt template in `CHAT_CONTEXT.md` so every Claude Chat–generated prompt is self-contained and self-enforcing, with no human judgment required to remember build, seed, or count steps. Three targeted edits: On Completion block now has an explicit 9-step sequence (build scripts at step 6, validate at step 7, blocking seed with confirmed count at step 8, commit at step 9); Prompt Writing Rule 9 now requires Claude Chat to read `STATE.yml` and resolve seed count to a real number before generating any prompt; Acceptance Criteria Rules section added with 10 binary checks that every generated prompt must include.

**Key Decisions:**
- On Completion step 5 now explicitly requires updating `item_count` to N+1 in STATE.yml — previously implied but not stated.
- The three build scripts are now a numbered step (step 6), not buried in session-completion boilerplate — this ensures they appear in every generated prompt's completion checklist.
- Acceptance Criteria Rules formalized as a standalone section (not a subset of Prompt Writing Rules) so the 10 checks are always visible as a discrete reference.

**Strategic Flags:**
- Next session is a new item. Claude Chat must read STATE.yml, see item_count = 26, and resolve seed count to 27 in the Acceptance Criteria before generating the prompt.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 26 rows confirmed, no drift.

---

### 2026-06-12 — Session P (governance): Mandatory Supabase seed enforcement — four governance docs updated, 1278980 seeded, all 26 items live

**What:** Governance hardening — added mandatory, blocking, non-deferrable Supabase seed step to four governance documents (`COMPLETION_TEMPLATES.md`, `CHAT_CONTEXT.md`, `CALCULATOR.md`, `VALIDATION_PROMPTS.md`). Created `.env` at repo root with service-role credentials so future sessions can run `migrate_to_supabase.py` live without manual intervention. Seeded P/N 1278980 (the item written in Session O but left unseeded), and confirmed all three carry-over P/Ns (1278980, 1267140, 1278220) are live in Supabase. `elliott_items` row count 25 → 26; all 26 items verified.

**Key Decisions:**
- Root cause of three consecutive unseeded sessions: no `.env` present + seed was treated as optional/deferrable. Both causes addressed: `.env` created, seed codified as blocking step 5 in the Session Completion checklist and step 7 in On Completion, with explicit language that the session is NOT complete until the seed is confirmed.
- Seed executed via Supabase MCP (service-role SQL path — semantically identical to live mode, the sanctioned pattern when `supabase-py` is unavailable), consistent with Session N precedent.

**Strategic Flags:**
- `.env` is in `.gitignore` and must never be committed — confirmed pre-flight.

**Status:** Complete — validate.py 0/0; all three build scripts clean; `elliott_items` = 26 rows; P/Ns 1278980, 1267140, 1278220 all confirmed present in Supabase.

---

*Entries older than Session P (2026-06-12) were removed per the 10-entry rolling window — git history retains them in full.*
