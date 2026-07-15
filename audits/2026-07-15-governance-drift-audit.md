# Elliott Equipment — Governance Drift Audit

**Date:** 2026-07-15
**Type:** Read-and-report only. No source files modified, no build scripts run, no Supabase access.
**Scope:** `.claude/MASTER_CONTEXT.md`, all 7 `governance/*.md` files, all 3 `categories/*.md` files, `frontend/index.html` (calculator engine, 6754 lines), `frontend/calculator_config.json`, `scripts/validate.py`, `scripts/profile.py`, `scripts/build_calculator_config.py`, `.claude/ARCHITECTURE.md`, `.claude/PROGRESS.md`, `.claude/STATE.yml`, and the 47 `items/*.md` files (spot-checked where a session's own notes flagged a process gap).

**Trigger for this audit:** three confirmed instances this week of the same failure pattern — a pricing rule gets established inside an individual item's validation session and written into `governance/PRICING_RULES.md` and/or a `categories/*.md` file, but never propagates back into `governance/CALCULATOR.md`, `frontend/calculator_config.json`, `frontend/index.html`, or `governance/VALIDATION_PROMPTS.md`. Each gap so far was found reactively, by hitting the exact item that exposed it. This audit finds the rest systematically.

---

## 1. Executive Summary

### Verdict: SAFE TO QUOTE FROM THE CATALOG — CALCULATOR AND VALIDATION TOOLING REMAIN UNSAFE FOR THIS ENTIRE SIZE CLASS

The **catalog layer** (`items/*.md`, `categories/*.md`) is internally consistent for every item audited. Every one of the doctrine gaps below has already been caught and hand-corrected, item by item, by Nick and Claude Code at file-write time — the item files themselves document the correction in their own Notes/Pricing Derivation sections. **No wrong price has reached — or is currently sitting in — the catalog.**

The **tooling layer** — the calculator engine (`frontend/index.html`), its config (`frontend/calculator_config.json`), the calculator's own contract (`governance/CALCULATOR.md`), and the 4-wave validation prompt template (`governance/VALIDATION_PROMPTS.md`) — has not absorbed any of the three governance doctrines named in this audit's charter, despite each one being confirmed, live, and load-bearing on the account for two to six weeks. This is the same shape of gap the 2026-06-09 full-system audit found in a different rule set (ink coverage, tape costing, MOQ purge) — it recurred, on schedule, for the next three rules that got established.

**All three confirmed gaps from the audit charter are STILL OPEN as of this session.** None were silently fixed since being flagged in individual item sessions.

### Top Risks

1. **[STOP-equivalent]** The sub-scope tier-generation code (`buildPrintLamSinglesTiers`) has no floor check at all — any new 0.1–0.5 sq ft item run through the calculator today gets a brief with 50-99/100-199/200+ tiers priced below the $15.43/sq ft §31 floor, with zero flag warning anyone. Every §31-compliant item on file today (3024595, 3017572 partially, 1101250 partially, 1001220) was hand-corrected by a human catching the violation after the fact — the tool that is supposed to prevent this has never once caught it itself.
2. **[STOP-equivalent]** The Micro-Format tier code (`buildPrintLamMicroTiers`) has no per-label floor check for sub-0.06 sq ft items. It will silently emit a linear-formula price 40–60% below the correct $2.75/$2.50 floor for any new item in that size class, exactly reproducing the bug the prior audit flagged (M-6) — confirmed live in production as recently as today's session (P/N 1205870's own item file documents the calculator brief computing $1.50 when the correct locked price was $2.50).
3. **[STOP-equivalent]** Cut vinyl tape costing in the engine still uses the deprecated area pseudo-rate (`sq_ft × $0.5911/sq ft`) with no 6" row-spacing allocation — overstating tape cost ~2.7× on every cut-vinyl brief the calculator produces, for old and new items alike, directly contradicting `governance/PRODUCTION.md`'s explicit instruction never to use that field this way.
4. **[REVIEW]** `governance/VALIDATION_PROMPTS.md` is not just silent on §31, §29's ANSI-hardcode, and the per-label floor doctrine — its own "Deep Volume Tier Instruction," embedded in every Wave 1 prompt, actively instructs models toward exactly the below-floor deep-tier structure §31 was written to prohibit. This has already caused two real, documented post-hoc corrections (1101250, 3017572) and will keep happening on every future sub-scope item until fixed.
5. **[REVIEW]** `governance/CALCULATOR.md` — the calculator's own contract document — never mentions §31 or the per-label floor doctrine anywhere in its 479 lines, and its flag table still describes F9 as a live REVIEW flag when the engine has it hardcoded as retired/unreachable.

---

## 2. Verification of the Three Named Gaps

### Gap 1 — §31 "sub-scope root floor applies at every tier, not just qty-20"

**Established:** 2026-07-01, via P/N 3024595 (`governance/PRICING_RULES.md` §31). Reinforced by two subsequent One-Time Exception cases (3017572, 2026-07-10; 1101250, 2026-07-14) and one fully-compliant item (1001220, 2026-07-14).

**Status: STILL OPEN.**

- `governance/CALCULATOR.md` — zero mentions of "§31," "root floor," or any related concept anywhere in the document (routing tree, flag table, or the 14-case sanity-check reference matrix in §9).
- `governance/VALIDATION_PROMPTS.md` §3 — zero mentions. Worse: the "Deep Volume Tier Instruction" embedded in every Wave 1 prompt (lines 168–169) tells models "the only hard requirement is that the ladder never inverts — each tier must be less than or equal to the tier above it," which is the exact permissive framing that produced the below-floor Wave 4 recommendations Nick then had to override on 3017572 and 1101250.
- `frontend/index.html` — `buildPrintLamSinglesTiers` (lines 5473–5489) scales the 6-tier ladder from `tier_ratios` (`50_99: 0.85`, `100_199: 0.7`, `200_plus: 0.55`) against the $15.43/sq ft anchor with `snapPrice()` only rounding, never flooring. $15.43 × 0.55 = $8.49/sq ft at 200+ — well below the $15.43 floor — with no clamp, no `Math.max`, and no flag (`FLAG_DEFS`, lines 5987–6011, has no §31-floor flag).
- `frontend/calculator_config.json` / `scripts/build_calculator_config.py` — no `sub_scope_root_floor` constant or equivalent exists anywhere.
- `scripts/validate.py` — `BAND_EXCEPTIONS` (lines 91–112) correctly documents the 3017572/1101250 One-Time Exceptions in prose, but there is no programmatic §31 check anywhere in the script — compliance depends entirely on a human remembering to add a truthful exception-string entry.

**What it would cause if hit:** any new 0.1–0.5 sq ft item run through the live calculator today produces a validation brief whose 50-99/100-199/200+ tiers sit below the account's own hard floor, with the tool itself reporting nothing wrong — precisely the pattern that produced the two live One-Time-Exception corrections already on file, except with no human review step guaranteed to catch it before the brief reaches Wave 1.

**Proposed fix (not applied):** add a `sub_scope_root_floor_per_sqft` constant (15.43) to `build_calculator_config.py`/`calculator_config.json`; clamp every tier in `buildPrintLamSinglesTiers` to `max(computed_price, floor × sq_ft)` before snapping; add a new flag (next free ID) that fires REVIEW when the clamp engages; add the §31 doctrine and the floor-clamp behavior to `governance/CALCULATOR.md` §2/§3; rewrite the Deep Volume Tier Instruction in `VALIDATION_PROMPTS.md` §3 to state the floor explicitly as a hard constraint above the "ladder never inverts" language.

### Gap 2 — Per-label floor doctrine, complexity-dependent (sub-0.06 sq ft)

**Established:** 2026-06-16, via P/N 3024592 (ANSI, $2.75 floor) and P/N 3024140 (non-ANSI, $2.50 floor). Reconfirmed as a reusable classification 2026-07-15 via P/N 1205870.

**Status: STILL OPEN — and freshly re-confirmed live in production today.**

- `frontend/index.html` — `buildPrintLamMicroTiers` (lines 5491–5533) only branches on whether `sq_ft` is within ±30% of the 0.097 sq ft `anchor_sq_ft` (line 5503) to decide template-direct vs. linear scaling. There is no ~0.06 sq ft threshold check and no per-label floor value anywhere in the function. For a sub-0.06 sq ft item outside the anchor window, it falls straight to `raw_anchor = sq_ft × 30.86` (line 5510) with no floor clamp.
- `frontend/calculator_config.json`'s `bands.printed_laminated_micro` block (lines 121–146) has no `per_label_floor`, `threshold_sub_0_06`, or complexity-classification key of any kind.
- `governance/CALCULATOR.md` — zero mentions of the per-label floor, "complexity-dependent," 3024592, or 3024140 anywhere in the document.
- `governance/VALIDATION_PROMPTS.md` §3's benchmark-anchor table lists only the $30.86/sq ft Micro-Format anchor (1279000) — it does not embed the per-label floor table or either floor anchor item.
- **Direct, first-party confirmation:** P/N 1205870's own item file (`items/1205870.md`, Pricing Derivation Step 1 and the Process Note) states that today's session's own Round 0 calculator brief computed **$1.50 at qty 20** via the linear formula for this 0.049 sq ft item, while the correct, locked price is **$2.50** — a 40% miss, produced by the live tool, in the same session this audit was requested. This is not a theoretical risk; it happened again this week.

**What it would cause if hit:** exactly what it caused on 1205870, and on 3024140/3024592 before the floor doctrine existed to catch it — a calculator brief that quietly recommends a price 40–60% below the correct number for the entire sub-0.06 sq ft item class, with no flag distinguishing it from a normal Micro-Format run.

**Proposed fix (not applied):** add a `per_label_floor_sub_0_06` object to `calculator_config.json` (`ansi: 2.75, non_ansi: 2.50`) plus a `complexity_class` input (or a manual override field) to the calculator UI for sub-0.1 sq ft items; in `buildPrintLamMicroTiers`, clamp to the appropriate floor whenever `sq_ft < ~0.06`; add a dedicated flag (e.g. reuse/repurpose the retired F9 slot or add a new ID) that fires REVIEW and states which floor applies; document both in `governance/CALCULATOR.md` and embed the floor table in `VALIDATION_PROMPTS.md` §3.

### Gap 3 — Tape cost method (length-based, not area-based) for cut vinyl

**Established/corrected:** 2026-06-09, for the 4-item small-format cluster (1205720, 1186310, 3017435, 3018378) — documentation-only correction at the time (`categories/cut-vinyl-3m-180mc.md`, `governance/PRODUCTION.md`).

**Status: STILL OPEN in the engine — partially fixed (vinyl only).**

- `frontend/index.html` — `computeCutVinylForRollWidth` (lines 5325–5343): vinyl cost (line 5330–5332) is correctly length-based (`feed length in yd × $/yd ÷ labels-across`) — this half of the 2026-06-09 M-2 finding is fixed. But tape cost (line 5333) is still `sq_ft_per_label × tape_psf`, pulling `tape_psf` directly from `calculator_config.json`'s `material_constants.transferrite_582u.cost_per_sq_ft` (value `0.5911`, line 196) — the exact deprecated pseudo-rate. There is no 6" row-spacing term and no labels-per-row divisor applied to tape at all.
- This directly contradicts `governance/PRODUCTION.md:212`, which states in as many words: *"The 582U `cost_per_sq_ft` field is a derived convenience value — never use it in a per-label cost build."*
- The engine's own generated brief text (line ~5383) presents this deprecated computation as the legitimate basis in the actual customer-facing-adjacent output: `` "Tape (TransferRite 582U): {sq_ft} sq ft × ${tape_psf}/sq ft" ``.

**What it would cause if hit:** for every cut-vinyl item quoted via the calculator today — old or new — the material-cost breakdown overstates tape cost by roughly 2.7×, understating true margin on every cut-vinyl brief. It is the same class of error the small-format cluster carried for weeks before the 2026-06-09 documentation fix — except that fix only ever touched the four catalog item files, never the tool that generates new quotes.

**Proposed fix (not applied):** rewrite the tape line in `computeCutVinylForRollWidth` to mirror the vinyl calculation — `feed_length_yd = (wide + 6/36) ` (i.e., add 6" row spacing before converting to yards) `× tape_cost_per_linear_yd ÷ labels_across` — sourcing `cost_per_linear_yd` (already present in `materials/transferrite-582u*.md`) instead of `cost_per_sq_ft`; update the brief text template to match; add a regression case to `runSanityChecks()` that would have caught this.

---

## 3. Additional Findings

### [REVIEW] `governance/CALCULATOR.md` flag table is stale on F9 in addition to being silent on §31/per-label-floor

Per the code-verification agent's read of the engine, F9 is hardcoded as retired/unreachable under the §28 no-floor doctrine, but `governance/CALCULATOR.md`'s flag table still documents F9 as a live "Tiny item (≤0.1 sq ft) — REVIEW" flag with normal firing conditions. A session reading the contract document alone would expect F9 to fire on tiny items; it cannot. Same class of doc/engine divergence the 2026-06-09 audit found with F11/F16/F18/F19 (H-4) — that finding was about ghost/dead flags; this is a fresh instance of the identical failure mode two sessions of drift later.

**Proposed fix:** correct F9's description in `governance/CALCULATOR.md` §3 to state it is retired, matching the treatment already given to F11/F12/F18/F19.

### [REVIEW] `governance/VALIDATION_PROMPTS.md` is now three governance rules behind, not one

The document's own header states "Last Updated: 2026-06-22" — which predates §29 (ANSI-by-default, 2026-06-29), §30 ($0.25 increment rule, 2026-06-29), and §31 (sub-scope floor, 2026-07-01) entirely. The 2026-06-09 audit's H-3 finding (band fence three bands and five anchors out of date) was addressed at some point between then and 2026-06-22 for the *bands* — the document's Section 3 does now embed all current bands and most current benchmark anchors correctly. But the *doctrine layer* (ANSI hardcode, $0.25 increments as a hard requirement rather than a schema note, the §31 floor) has not been touched since, and the account has added a new material family (Convex/polycarbonate), a per-label floor system, and eleven more benchmark items in the interim without a corresponding Section 3 update. This is the same COMPLETION_TEMPLATES.md trigger ("Validation wave prompts need updating... update governance/VALIDATION_PROMPTS.md Sections 3 and 5") that the 2026-06-09 audit found had been skipped five times in a row (S6) — it has now been skipped for every governance rule established since, without exception.

**Proposed fix:** a dedicated documentation-only session to rebuild `VALIDATION_PROMPTS.md` §3 against current `governance/PRICING_RULES.md` §1–§31 line by line, embedding every doctrine (not just band tables) that a Wave 1–4 prompt needs to avoid re-litigating.

### [INFO] `.claude/ARCHITECTURE.md` Category Registry table is stale against its own item catalog and its own change-log header

The Category Registry table (`.claude/ARCHITECTURE.md`, "Item Count" column) lists **Printed + Laminated: 33** and **Cut Vinyl Lettering: 9**. The Item Catalog table immediately above it, and the file's own session-log header (Session AQ: "Printed/Laminated category: 35 → 36 items"), both confirm the current counts are **36** and **10** respectively (the cut-vinyl catalog table lists ten P/Ns: 1205720, 3017435, 3018378, 1186310, 1146650, 3010701, 3010704, 3010707, 3010708, 3010709). The registry table appears to have last been hand-updated several sessions ago and was not touched on at least the 1146650 (cut vinyl) and several printed/laminated additions since. No pricing impact — this table is descriptive, not a data source any script or the calculator reads — but it is exactly the "living document" self-consistency this repo's Core Rule 6 exists to guarantee, and it has quietly drifted by 3–4 items.

**Proposed fix:** update the two Item Count cells in the Category Registry table to 36 and 10.

### [INFO] `.claude/MASTER_CONTEXT.md` File Map understates the `items/` file count

The File Map section still reads "40 item files" under `items/`; the actual current count is 47 (confirmed via `ls items/*.md`, matching `STATE.yml item_count: 47`). This was already flagged as a low-severity drift in the 2026-06-09 audit (L-5, which focused on the missing `audits/` directory entry — since fixed, the current File Map does list `audits/`) but the item-file-count comment itself has continued to drift in the five weeks since and was not part of that finding.

**Proposed fix:** update the comment to the current count or remove the specific number in favor of "one file per item — see `.claude/STATE.yml item_count`."

### [INFO] `do_not_benchmark` / `BAND_EXCEPTIONS` lists — current, no drift found

Cross-checked `frontend/calculator_config.json`'s `do_not_benchmark` list (8 entries: 1277970/1277980/1277990/1278000, 3017583/3017584, 1210810, 1082570) and `scripts/validate.py`'s `BAND_EXCEPTIONS` dict against the current 47-item catalog, including every item added since the 2026-06-09 audit (1205870, 1001220, 1146650, 1132950, 1101250, 1062390, 3017572, 3024595, 3020477). Every item that should be excluded is excluded; every item that should NOT be excluded (the newer sub-scope data points, which are `do_not_benchmark: false` by governance design) correctly stays off both lists. `BAND_EXCEPTIONS` in particular is being actively and correctly maintained through the most recent session (1205870, 2026-07-15) — this is the one piece of tooling in this audit that has kept pace with governance. No finding here; noted as a positive control.

### [INFO] `scripts/validate.py` has no programmatic §30 or §31 check

Confirmed via the code-verification agent: `validate.py` contains no logic testing tier prices for $0.25-increment compliance (§30) or for per-tier compliance against the §31 sub-scope floor — `check_band_membership` only tests whether an item is *listed* in `BAND_EXCEPTIONS`, never whether the underlying math is actually correct or whether an exception is honestly documented. Both rules currently depend entirely on a human writing an accurate prose exception string at file-write time. This is not a rule that has drifted (there was never a check to drift from) but it is the structural reason gaps 1–3 above can exist silently — the repo's one automated gate (the 2026-06-09 audit's own "Working Well" #13) does not know about either doctrine.

**Proposed fix:** add a `check_sub_scope_floor()` pass to `validate.py` that recomputes `$/sq ft` per tier for every sub-scope item and either confirms it clears $15.43/sq ft or confirms a matching, dated `BAND_EXCEPTIONS`/override_type entry exists; add a `check_quarter_increment()` pass that verifies every `price_*` field is a multiple of $0.25 for items dated after 2026-06-29.

### [INFO] `scripts/profile.py` — no drift, no exposure

Confirmed no hardcoded pricing formulas, thresholds, or rates exist in `profile.py`; it aggregates frontmatter only. Not a carrier of any of this audit's risk classes.

---

## 4. Priority-Ordered List

### Live risks — could produce a wrong price on the next relevant item, right now

1. **§31 floor not enforced in `buildPrintLamSinglesTiers`** (frontend/index.html:5473–5489) — the next new sub-scope item (0.1–0.5 sq ft) run through the calculator without a human catching it will get a below-floor deep-tier recommendation in the Round 0 brief.
2. **Per-label floor not enforced in `buildPrintLamMicroTiers`** (frontend/index.html:5491–5533) — the next new sub-0.06 sq ft item will get a 40–60% low linear-formula price, exactly as happened again this session on P/N 1205870.
3. **Cut vinyl tape costing still area-based in the engine** (frontend/index.html:5325–5343, specifically line 5333) — every cut-vinyl brief generated today, for any item, overstates tape cost ~2.7×, corrupting the margin figures Wave 1–4 models see.
4. **`VALIDATION_PROMPTS.md`'s Deep Volume Tier Instruction actively contradicts §31** — any 4-wave session run today on a sub-scope item will reproduce the two documented One-Time-Exception incidents (3017572, 1101250) a third time, because the standing prompt instruction tells models the wrong hard requirement.
5. **`validate.py` has no independent §31/§30 check** — this is what allows risk #1 above to reach a committed item file undetected if a future session forgets to hand-write a `BAND_EXCEPTIONS` entry.

### Documentation-only drift — wrong, but has not caused (and structurally cannot by itself cause) a bad number

6. `governance/CALCULATOR.md` silent on §31 and the per-label floor doctrine (contract document, not itself executable).
7. `governance/CALCULATOR.md` F9 flag description stale (describes a retired flag as live).
8. `governance/VALIDATION_PROMPTS.md` header timestamp and doctrine coverage generally three rules behind (§29/§30/§31 all unaddressed beyond the Deep Volume Tier Instruction contradiction called out above).
9. `.claude/ARCHITECTURE.md` Category Registry item counts stale by 3–4 items (Printed/Laminated 33→36, Cut Vinyl 9→10).
10. `.claude/MASTER_CONTEXT.md` File Map item-file count stale (40→47).

No finding in this audit involves a currently-quoted, currently-locked catalog price being wrong. Every gap found lives in the tooling that generates *future* recommendations — which is precisely why it keeps getting caught one item late instead of before the item is priced.
