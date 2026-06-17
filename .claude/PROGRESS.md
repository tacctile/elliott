# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> **Rolling window: 10 entries max. When adding an 11th, remove the oldest. Git retains all history.**
>
> This file is the session memory layer: why decisions were made, what changed strategically, what a future session needs to know. It is not a commit log and not a validation archive — full validation records live in `items/*.md` (Pricing Derivation), file-level changes live in git history, and structure/math compliance is enforced by `scripts/validate.py`. Entry format (template in `.claude/COMPLETION_TEMPLATES.md`): What / Key Decisions / Strategic Flags / Status, 10–25 lines per entry, no other sections.
>
> Last Updated: 2026-06-17 (Session V — P/N 1278930: updated from 3-label kit → 2-label kit. label_count 3 → 2, sq_ft_per_kit 1.827 → 1.218, material_cost_per_unit $3.60 → $2.40, tiers now match 1278890 exactly ($30/$24/$20/$17/$14/$12). ~88% margin at qty 20 unchanged. Item count unchanged at 31.)

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

### 2026-06-12 — Session O (new item): P/N 1278980 — singles band fourth data point, $9.50 at qty 20, 4-wave validated

**What:** New printed/laminated single label (LABEL-PLTFM RANGE CAPACITY CHART MODEL E160 V3) at 7.88" × 11.13" = 0.609 sq ft, priced $9.50 at qty 20 = $15.60/sq ft — the singles band's fourth confirmed data point and the first item at exactly 0.609 sq ft. Band $/sq ft is now monotonic across four positions (0.503 / 0.560 / 0.609 / 1.296 → $15.91 / $15.63 / $15.60 / $15.43). Full 4-wave atomic validation (24 responses): Wave 1 landed 5/6 at exactly $9.50, all anchored to 1267140; Wave 3 sent the PO as-is 6/6 with zero questions.

**Key Decisions:**
- Wave 2's single structural finding adopted: a 200+ floor below $6.50 inverts against 1267140's validated floor on a $/sq ft basis — floor set at $6.75 (strongest Wave 2 clustering), 100-199 held at $7.50 for tier separation. Wave 4 split 4 YES / 2 NO (the 2 NO argued $7.07–$7.25 on $/sq ft parity); Nick accepted $6.75 — the residual $/sq ft step vs 1267140's floor ($11.08 vs $11.61) is theoretical given Sean's 20–50 batch pattern, and $6.75 stays above the $6.50 dollar threshold he'd notice on an invoice. No override — engine consensus accepted.
- Routed as a SINGLE to the singles band despite exact kit-family label geometry: kit per-label parity does not apply to singles; $9.50 vs the $10.00/label kit rate is the documented intentional kit premium, not an inconsistency.

**Strategic Flags:**
- INTERNAL ONLY: likely the first of several singles at exactly 0.609 sq ft — every tier in this table becomes the permanent reference for future items at this size. January 2027 normalization from $9.50 requires ~$1.46–$3.90/label uplift to $18–$22/sq ft; anchor to relationship-phase transition, NOT per-label rate arguments — Sean now has four accepted/quoted data points at $15.43–$15.91/sq ft.
- Wave 3 quote email anchor line locked: "Pricing is based on the same cast vinyl/polyester overlaminate construction as your prior Pro Label orders." (Reference 1267140/1230820 if helpful.)

**Status:** Complete — validate.py 0/0; quote pending ($9.50 at qty 20); Supabase seed for 1278980 deferred to a follow-up run (scripts/migrate_to_supabase.py).

---

### 2026-06-12 — Session N (ops): Supabase seed — P/N 1267140 + 1278220 into `elliott_items` / `elliott_items_internal`

**What:** Seeded the two items added earlier today (Session L: 1267140; Session M: 1278220) into the shared `prolabel` Supabase project, clearing the carry-over flagged by both sessions. Pure seed run of the existing source-of-truth files — no repo item, governance, or pricing changes. Both tables went 23 → 25 rows; the deployed Supabase-first UI now serves both items (1267140 in singles_standard, 1278220 in singles_micro, verified row-level in the live DB).

**Key Decisions:**
- The remote session env had no Supabase service-role credentials, so the documented alternate path was used: `migrate_to_supabase.py --emit-sql` executed through the service-role-backed Supabase MCP in batches — semantically identical to live mode, and the sanctioned pattern for credential-less environments.

**Strategic Flags:**
- D4 security routing re-verified live: `pricing_logic`/`notes` blank on the anon-readable `elliott_items` rows; full strategy text (including the 1267140 INTERNAL ONLY normalization note) lives only in `elliott_items_internal`, which has no anon policies.
- The seed is idempotent — materials/bands/settings/combinations re-upserted with zero value drift; the repo remains the source of truth.

**Status:** Complete — next action is Nick sending Sean both quotes (1267140 $8.75 at qty 20, 1278220 $3.00 at qty 20).

---

### 2026-06-12 — Session M (new item): P/N 1278220 — direct parity clone of 1279000 (Micro-Format Band, $3.00 at qty 20)

**What:** Created P/N 1278220 (LBL-MAX JIB CAP 1500 TIP HZRD) as a direct parity clone of 1279000, the Micro-Format Band founding data point — identical dimensions (0.097 sq ft), material, process, tier table, and margins; only the P/N and artwork content differ. The direct parity exemption per `governance/PRICING_VALIDATION.md` applies: 1279000's full 4-wave validation is inherited, no new AI validation run (same pattern as 1068270 ← 1082570, Session F). Rule 15 band check satisfied: $3.00 at qty 20 = $30.86/sq ft, exactly the Micro-Format Band anchor.

**Key Decisions:**
- Parallel-session collision with Session L (1267140) resolved at merge: both sessions had independently claimed "Session L," category footnote ⁶, and item #24. Resolution — 1267140 keeps Session L / ⁶ / #24 (first to main); this session relabeled Session M with footnote ⁷; final item count 25. Both sessions' content verified intact; the collisions were namespace-only.
- 1278220 is NOT a band data point — founding status stays with 1279000 alone, and the band's data-point count is unchanged. The band's ~0.08–0.12 sq ft boundary caution governs dimensionally NEW items, not exact-dimension parity clones.

**Strategic Flags:**
- Permanent lockstep link: any future change to 1279000's dimensions, material cost, process, or band parameters must update 1278220 in lockstep (same convention as 1068270 ↔ 1082570).

**Status:** Complete — validate.py 0/0 on the merged tree; quote pending ($3.00 at qty 20); the deferred Supabase seed was completed in Session N.

---

*Entries older than Session M (2026-06-12) were removed per the 10-entry rolling window — git history retains them in full.*
