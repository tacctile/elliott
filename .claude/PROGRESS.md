# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> **Rolling window: 10 entries max. When adding an 11th, remove the oldest. Git retains all history.**
>
> This file is the session memory layer: why decisions were made, what changed strategically, what a future session needs to know. It is not a commit log and not a validation archive — full validation records live in `items/*.md` (Pricing Derivation), file-level changes live in git history, and structure/math compliance is enforced by `scripts/validate.py`. Entry format (template in `.claude/COMPLETION_TEMPLATES.md`): What / Key Decisions / Strategic Flags / Status, 10–25 lines per entry, no other sections.
>
> Last Updated: 2026-07-15 (Session AR — governance drift remediation: fixed the 3 live-risk engine gaps confirmed still open by audits/2026-07-15-governance-drift-audit.md. Previously Session AQ — P/N 1205870 added, second sub-0.06 sq ft non-ANSI per-label floor data point at 0.049 sq ft, joining P/N 3024140; price locked directly against 3024140's floor and tier table, no 4-wave AI validation run, per the same session-prompt locking convention used for 1279260/1279270. Previously Session AP — P/N 1001220 added, eighth sub-scope data point at 0.231 sq ft; full 4-wave AI validation followed by a post-synthesis §31 compliance correction on the deep tiers, since §31 postdated this item's wave prompts — first sub-scope item to reach a fully §31-compliant flat structure directly, without a One-Time Exception override. Previously Session AO — P/N 1146650 added, second Band A interior data point at 2.971 sq ft, between the 2.512–2.564 sq ft cluster and 3010701; full 4-wave AI validation on 20-49 through 200+, Owner Judgment override on 1-9/10-19 after discovering P/N 3018378 was omitted from the wave benchmark set.)

---

### 2026-07-15 — Session AR (governance drift remediation): 3 live-risk engine gaps fixed — §31 sub-scope floor clamp, per-label floor STOP flag (F26), cut vinyl tape costing

**What:** Fixed the 3 live-risk findings from `audits/2026-07-15-governance-drift-audit.md` in `frontend/index.html` (engine) and `frontend/calculator_config.json`/`scripts/build_calculator_config.py` (config source of truth). (1) `buildPrintLamSinglesTiers` now clamps any tier of a `single_sub_scope` item that would price below the $15.43/sq ft §31 root floor, and every deeper tier, flat to the cheapest $0.25 increment clearing the floor — verified to natively reproduce P/N 3024595's flat $7.75 structure (was $7.50/$6.50/$5.25/$4.25, all below floor). (2) `buildPrintLamMicroTiers` now refuses the linear $30.86/sq ft formula below 0.06 sq ft and fires a new STOP flag, F26, naming the two governing comparables (3024592 ANSI, 3024140 non-ANSI) — verified against P/N 1205870, whose own brief had been silently computing $1.50 against a correct $2.50. (3) Cut-vinyl tape costing is now length-based (`(label length + 6" spacing) ÷ labels per row × $/linear yd`), not the deprecated `sq_ft × $0.5911/sq ft` pseudo-rate — verified against P/N 1205720, now reproducing the filed $7.88 material cost exactly (was $8.74). No `items/*.md` file was touched — this is a tooling fix, not a pricing change to any filed item.

**Key Decisions:**
- §31 clamp applies only to `single_sub_scope` (0.1–0.5 sq ft), not `single_standard` — confirmed no regression on the 1230820 root benchmark itself, which is allowed to price below $15.43/sq ft at deep tiers by design (that's simply volume-tier compression on the root item, not a §31 violation).
- Per-label floor threshold (0.06 sq ft) and both governing comparables (3024592/3024140, with their $2.75/$2.50 prices) are now named config constants (`bands.printed_laminated_micro.per_label_floor_*`), not hardcoded strings, per CALCULATOR.md rule 5.
- Vinyl costing was left untouched (already length-based and correct per the audit and the task scope) — only tape's formula changed.
- `governance/VALIDATION_PROMPTS.md` §3 Deep Volume Tier Instruction rewritten: §31 is now a stated hard precondition for sub-scope items, checked before the "clean round number" step-down guidance — the prior unconditional wording produced two real Nick-directed One-Time-Exception corrections after the fact (P/N 3017572, P/N 1101250).
- `governance/CALCULATOR.md` updated in full: §31/per-label-floor doctrines documented, F26 added to the flag table, F9's stale description corrected (was still describing pre-§28 REVIEW behavior; engine has it retired/INFO), flag count 23→24, new config constants documented, `runSanityChecks()` raised from 14 to 17 cases (added 3024595/1205870/1205720-material-cost regression cases; corrected the pre-existing 1210810 case's expected price from $4.50 to $4.75 now that the §31 clamp makes the algorithmic output match the catalog exactly for the first time).
- `.claude/ARCHITECTURE.md` Category Registry item counts corrected (Printed/Laminated 33→36, Cut Vinyl 9→10, independently verified against `frontend/data.json`) and `.claude/MASTER_CONTEXT.md` item-file count corrected (40→47) — both were stale relative to the actual catalog and the files' own session-log headers.

**Strategic Flags:**
- **Noticed, not actioned (out of scope this session):** `runSanityChecks()` case "1278930" expects a 3-label kit price ($30) but the catalog has carried a 2-label kit ($20) since an earlier session — this drift is unrelated to any of the 3 fixes above (kit-tier code was not touched) and predates this session; flagging for a future kit-focused session rather than fixing here.
- **Noticed, not actioned:** the length-based tape fix uses a single tape roll rate (`transferrite_582u`, the 24" roll) for all cut-vinyl items, matching the engine's pre-existing (unfixed) behavior of never modeling the alternate 30"-roll/Band-B-specific tape rate or Band C's 5-up (vs. naive floor-division 6-up) nesting choice — both are separate, pre-existing simplifications unrelated to the area-vs-length defect this session fixed; Band B/C material-cost figures from the calculator will still diverge from `governance/PRODUCTION.md`'s hand-computed worked examples for those bands specifically. P/N 1205720 (the required verification target, Band A) matches exactly.
- Verified via a Node `vm` harness (extracting the calculator engine's `<script>` block, stubbing `window.CALCULATOR_CONFIG`/`window.ITEMS_DATA`) rather than a browser — no UI regression testing was performed; the engine has no DOM dependencies in the audited block, so this is a faithful test of the actual shipped logic.

**Status:** Complete — `python scripts/validate.py` 0 errors/0 warnings (no item files touched, unaffected); `runSanityChecks()` 15/16 pass in the Node harness (the one failure is the pre-existing, unrelated 1278930 drift noted above — same result before and after this session's changes). `scripts/build_calculator_config.py` re-run; diff against the pre-run manually-edited config confirmed clean (only the new constants plus incidentally-more-complete `cost_per_linear_yd` values for two other materials, no unexpected reversions). Not run: `migrate_to_supabase.py` (no item data changed, nothing to seed, per session instruction).

---

### 2026-07-15 — Session AQ (new item): P/N 1205870 — LBL-RADIO QUICK START IFM TILT, second sub-0.06 sq ft non-ANSI per-label floor data point, price locked directly against 3024140, no AI validation

**What:** New printed/laminated single label at 4.000" × 1.750" = 0.049 sq ft — the second sub-0.06 sq ft **non-ANSI** per-label floor data point on file, joining P/N 3024140. Content reviewed directly from the spec sheet artwork (not the calculator's generic title-block description): "LEVEL SENSOR QUICK START GUIDE," a plain black-on-white 4-step bulleted procedure for zeroing a level sensor via the radio remote — no signal word, no ANSI color header, no hazard pictogram. Classified non-ANSI/instructional, matching 3024140's category exactly rather than 3024592's ANSI hazard/danger category. Price locked directly against 3024140's existing $2.50 floor and full tier table ($4.00/$3.00/$2.50/$2.25/$2.00/$1.75) — no 4-wave AI validation run this session, per the same session-prompt locking convention used for P/N 1279260/1279270 (which matched 3024592's $2.75 ANSI floor without revalidation). Material cost $0.10/label (§25 canonical: $0.0955 calculated + incidental buffer, matches 3024140's filed cost exactly).

**Key Decisions:**
- The controlling judgment this session was the **classification call** (non-ANSI instructional vs. ANSI hazard/danger), made from direct review of the spec sheet artwork image rather than the calculator's generic title-block description — the calculator's Round 0 brief had surfaced 3024592 (0.054 sq ft, near-identical size) as the nearest comparable at $2.75 but never applied it.
- No AI validation run — price and tier table locked directly by Nick against existing floor precedent. Claude Code did not re-derive or second-guess the tier table.
- `categories/printed-laminated-orajet.md`'s Pricing Profile section previously stated the $2.50 non-ANSI floor was "historical only... applies solely to 3024140 and 1012080... do not apply to any new item" (written under `governance/PRICING_RULES.md` §29's ANSI-by-default rule). Updated the category file this session to reflect that a direct, artwork-based non-ANSI classification is a valid basis to apply the $2.50 floor to a new item — 1205870 is now the second independent confirmation, not a one-off exception. `governance/PRICING_RULES.md` §29 itself was **not** edited this session — out of scope; the tension between §29's literal text and this session's locked price is documented in the item file and here for future sessions to reconcile if it recurs.
- Model field blank on the drawing/title block — documented as blank per account convention (the P/N is the identifier, never invented).

**Strategic Flags:**
- **Process finding, not actioned this session:** the calculator's own Round 0 brief computed this item using the linear Micro-Format Band formula ($30.86/sq ft × 0.049 = $1.50 at qty 20) despite surfacing 3024592 as the nearest comparable at $2.75 — that number was never used. This is the same category of gap as the §31 miss flagged in Session AP (calculator/validation tooling not yet updated for a routing rule — here, the ~0.06 sq ft per-label-floor threshold — that the tooling doesn't apply automatically). Worth a process note; out of scope to fix this session. Per session instruction, `governance/VALIDATION_PROMPTS.md` and the calculator's routing logic were not touched.
- First article not confirmed with Sean — flag for follow-up. Order quantity not specified — standard 6-tier ladder quoted.
- do_not_benchmark = false — valid classification-governed floor data point; added to `scripts/validate.py` BAND_EXCEPTIONS (sub-0.1 sq ft Micro band membership check would otherwise fail against the $30.86/sq ft linear anchor).
- Item count: 46 → 47. Printed/Laminated category: 35 → 36 items. Sub-0.06 sq ft non-ANSI floor data points: 1 → 2.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 47 rows confirmed in Supabase.

---

### 2026-07-15 — Session AP (new item): P/N 1001220 — DANGER ELECTROCUTION HAZARD, UNINSULATED PLATFORM, eighth sub-scope data point, post-synthesis §31 compliance correction

**What:** New printed/laminated single ANSI danger label at 7.00" × 4.75" = 0.231 sq ft — the eighth sub-scope (0.1–0.5 sq ft) data point on file, sitting between 1279130 (0.148 sq ft, $20.95/sq ft) and 1210810 (0.292 sq ft, $16.27/sq ft) on the gradient. Full 4-wave AI validation (6 models × 4 waves, run in Claude Chat) produced a step-down ladder at Wave 4 ($4.00/$3.50/$3.00/$2.75 at 20-49 through 200+) that priced three deep tiers below the $15.43/sq ft §31 root floor — a violation none of the waves could catch because `governance/PRICING_RULES.md` §31 (established 2026-07-01) postdates `governance/VALIDATION_PROMPTS.md`'s last update and was never in this item's wave prompts. Corrected post-synthesis to hold flat at $3.75/ea ($16.23/sq ft) from 50-99 through 200+, mirroring 3024595's structure. Nick locked the corrected ladder: $7.00/$5.50/$4.00/$3.75/$3.75/$3.75. Material cost $0.46/label (§25 canonical: $0.4502 calculated + minimal buffer).

**Key Decisions:**
- Wave 1 (Build): no convergence — qty-20 prices ranged $3.25–$5.50.
- Wave 2 (Destruction): median-based ladder attacked, 4/6 No — the small-format premium over root benchmark 1230820 widened with volume instead of shrinking (~19% at qty 20 → ~53% at 200+), backwards from genuine fixed-cost economics; deep tiers split flat-hold (~$3.75) vs step-down (~$3.00/$2.75).
- Wave 3 (Buyer Simulation): unanimous 6/6 preferred the step-down path — a flat-hold structure would read to Sean Finn as "no volume curve exists" and trigger pushback at 100-199.
- Wave 4 (Final Synthesis): 5/6 No on the step-down ladder, unanimously flagging a premium "wobble" at 50-99, recommending a corrected step-down ladder ($4.00/$3.50/$3.00/$2.75).
- **Post-synthesis §31 correction:** before locking, the Wave 4 step-down ladder was checked against §31 and found in direct violation on 50-99/100-199/200+ (all priced below the $15.43/sq ft floor). Corrected to a flat $3.75/ea from 50-99 through 200+ — the cheapest $0.25-increment price clearing the floor, mirroring 3024595's own flat-ladder structure. This is the **first sub-scope item to reach a fully §31-compliant flat structure directly**, without a Nick-directed One-Time Exception override (unlike 3017572 and 1101250).
- Editorial correction (no pricing impact): the session prompt described 1001220 as "larger than 1210810" — at 0.231 sq ft it is actually smaller than 1210810 (0.292 sq ft); corrected in the item file's Notes and Warnings.

**Strategic Flags:**
- **Process finding, not actioned this session:** `governance/VALIDATION_PROMPTS.md` Section 3 should embed §31 in the band-context block so future sub-scope wave prompts don't repeat this gap — this is the second consecutive sub-scope item (after 1101250) whose validation predated a governance rule that had to be applied post-hoc.
- First article not confirmed with Sean — flag for follow-up. Order quantity not specified — standard 6-tier ladder quoted.
- do_not_benchmark = false — valid sub-scope data point, excluded from singles band DATA POINTS until production-volume acceptance.
- Item count: 45 → 46. Printed/Laminated category: 34 → 35 items. Sub-scope data points: 7 → 8.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 46 rows confirmed in Supabase.

---

### 2026-07-14 — Session AO (new item): P/N 1146650 — LABEL "40142" MODEL DESIGNATION, second Band A interior data point, full 4-wave validation + Owner Judgment override on shallow tiers

**What:** New Vinyl Cut Lettering single label at 40.75" × 10.5" = 2.971 sq ft — a new interior Band A data point sitting between the 2.512–2.564 sq ft small-format cluster (1205720, 1186310, 3017435, 3018378) and 3010701 (3.202 sq ft, $44/qty 20). Full 4-wave AI validation (24 attempted responses, 6 models × 4 waves, Wave 4 5/6) locked $40.75 at qty 20 = $13.72/sq ft on the 20-49 through 200+ tiers — inside the concession-phase band ($13.65–$13.94/sq ft) and between both neighboring anchors, no size/price inversion. Material cost $10.83/label (vinyl $10.07 + tape $0.77), computed with the account-standard length-based nesting method — this corrects the Round 0 calculator brief's $10.53 filing, which used raw label width with no row-spacing allocation and area-based tape costing (see items/3010701.md for the governing method).

**Key Decisions:**
- Wave 1 (Build): 5/6 models converged on proportional interpolation between the cluster and 3010701 ($40.75–$41.25); 1 outlier at flat cluster parity ($35.00) rejected as internally inconsistent.
- Wave 2 (Destruction): unanimous HIGH severity — the Wave 1 build's $41.00 ($13.80/sq ft) inverted against both the cluster and 3010701; corrected to $40.75 ($13.72/sq ft). 1-9 also reduced from a raw-interpolation ~$52.68 to $50.00 at this stage.
- Wave 3 (Buyer Simulation): 5/6 instant PO approval, pushback threshold $41.60–$44.00; 1/6 pushed back specifically on the 1-9 tier ($50.00) as suspiciously low.
- Wave 4 (Final Synthesis): 4/5 YES send-as-shown ($50.00/$45.00 at 1-9/10-19); 1/5 NO flagged that $50.00 sits below the full Band A comp range (not just the two anchors supplied), recommending $52.00.
- **Owner Judgment override:** reviewing the wave prompts post-Wave-4 found P/N 3018378 (2.512 sq ft, same tier table as the cluster, already Quoted) was never included as a benchmark anchor in any wave prompt — a template omission. Incorporating the full five-item comp set confirmed the Wave 4 dissent was correct; Nick raised 1-9 to $52.00 and 10-19 to $46.50. 20-49 through 200+ ($40.75/$35.50/$30.50/$26.50) held unchanged — no dissent at any wave on those four tiers.

**Strategic Flags:**
- **Process finding, not actioned this session:** `governance/VALIDATION_PROMPTS.md` Section 3's cut vinyl benchmark anchor set should add P/N 3018378 going forward, so future wave prompts don't repeat this omission.
- Spec Extraction gap: revision, drawing number, engineer, DTR, and tolerances are BLOCKED — priced from a Round 0 calculator brief, not a full drawing review; documented as blocked, not invented, per the account convention (items/1267140.md precedent).
- Weed labor complexity for the 40.75" run NOT independently measured against the 33.5"-and-under cluster benchmark — flagged for a 90-day post-production timing check (~2026-10-12).
- First article and order quantity not specified — standard 6-tier ladder quoted, flagged for Sean follow-up.
- Item count: 44 → 45. Cut Vinyl category: 9 → 10 items. Band A data points: 5 → 6.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 45 rows confirmed in Supabase.

---

### 2026-07-14 — Session AN (new item): P/N 1132950 — CHRT JIB-I50 TP JIB 500# PLATFORM 600#, fifth item at the 0.503 sq ft singles-band position, Direct Parity Exemption, no wave validation

**What:** New printed/laminated single label at 7.25" × 10.00" = 0.503 sq ft — the identical footprint already held by P/N 1082570, P/N 1068270, P/N 1073950, and P/N 1062390. Filed under the Direct Parity Exemption per `governance/PRICING_VALIDATION.md` (dimensionally and materially identical to items already quoted) — no new 4-wave AI validation session was run. Benchmark: P/N 1068270 (identical 0.503 sq ft area, identical process/material stack); precedent reinforced by P/N 1073950 (independent 4-wave validation, unanimous 6/6 exact parity) and by P/N 1062390 (filed at the same parity with no re-validation). Tier table cloned exactly: $16.50/$10.50/$8.00/$6.25/$5.25/$4.25. Material cost $0.98/label (§25 canonical, filed at the cent).

**Key Decisions:**
- Direct Parity Exemption invoked rather than running a fresh 4-wave validation — 1073950's independent Wave 1–4 unanimous convergence on exact parity with 1068270 at this identical 0.503 sq ft footprint (reinforced by 1062390's own exemption filing) is the governing precedent cited for this exemption.
- Model/load-class distinction flagged but ruled non-blocking: 1132950 (I50, Platform 600# / Top Jib 500#) differs from the other three (G85/G85R, Basket 500#) in both model family and load-rating class — a bigger artwork difference than the mount-only variation between 1068270 and 1073950. Parity holds because cost is driven by dimensions, material stack, and process (all identical), not load-chart content; full-bleed ink is priced flat at $0.50/sq ft regardless of what's printed.
- Rule 15 (Pricing Profile band check) still applies and is satisfied — $15.90/sq ft at qty 20 lands cleanly within the singles band ($15.43–$15.91/sq ft).
- No override — engine consensus (parity) accepted, override_type blank.

**Strategic Flags:**
- Open taxonomy item: model field reads I50 / Platform 600# / Top Jib 500# (vs plain G85 Basket 500# on 1068270/1073950 and G85R Basket 500# on 1062390) — flagged for Nick/Sean follow-up alongside the quote; does not affect pricing under the exemption.
- First article NOT specified this session — flagged for follow-up, does not block filing. Order quantity not specified — standard 6-tier ladder quoted.
- This item does NOT add a new independent singles-band data point — the 0.503 sq ft position remains anchored where it already was, now shared by five items. Band stays at 5 confirmed data points.
- Item count: 43 → 44. Printed/Laminated category: 33 → 34 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 44 rows confirmed in Supabase.

---

### 2026-07-14 — Session AM (new item): P/N 1101250 — LBL-DNGR MAX PLAT. 2100, seventh sub-scope data point, $2.25/qty 20, independently 4-wave validated, §31 One-Time Exception on deep tiers

**What:** New printed/laminated single ANSI danger-class label at 4.00" × 4.75" = 0.132 sq ft — the seventh sub-scope (0.1–0.5 sq ft) data point on file. Full 4-wave atomic AI validation (24 independent responses, 6 models × 4 waves) run per `governance/PRICING_VALIDATION.md` / `governance/VALIDATION_PROMPTS.md` locked $2.25 at qty 20 = $17.05/sq ft — +10.5% over the sole governing benchmark, P/N 1230820 ($15.43/sq ft). Material cost $0.26/label (§25 canonical: $0.2572 calculated, filed at the cent).

**Key Decisions:**
- Wave 1 (Build): qty-20 prices ranged $2.35–$2.75, center of mass ~$2.50; all 6 models anchored heavily on P/N 1210810 — a process finding, not a benchmark citation. 1210810 is on the account's `do_not_benchmark` list and is NOT cited as a comp anywhere in the filed item; Waves 2-4 corrected course.
- Wave 2 (Destruction): 5/6 No verdicts on $2.50; unanimous High-severity Cost Auditor finding (small-format premium modeled, not measured) and Strategic finding (this item becomes the account's sole official reference point below the 0.5 sq ft band floor); 1 dissent argued for $2.75 to avoid a ceiling too low for future interpolation. Consensus moved to $2.00–$2.25 at 20-49, $1.75/$1.50/$1.25 at 50-99/100-199/200+.
- Wave 3 (Buyer Simulation as Sean Finn): 5/6 instant PO approval at $2.25, no friction; 1 dissent wanted $1.95. Pushback threshold ~$2.50 (+22-23%); instant-approval ~$2.00 (benchmark parity). Multiple models flagged pricing below $2.00 as the worse long-term outcome — it would anchor a floor Sean defends indefinitely.
- Wave 4 (Final Synthesis): 5/6 YES send as shown; 1 dissent proposed raising 50-99/100-199/200+ by $0.25 each to smooth a "U-shaped" per-tier premium curve vs 1230820 (+10.5% at 20-49, narrowing to +1.1%/+5.2% at 50-199, widening to +11.6% at 200+). **Nick locked the table as shown** — the dissent's fix would have pushed 200+ to +33.9% over benchmark instead of +11.6%, a worse outcome at a tier Sean is unlikely to transact.
- **Override:** the 50-99/100-199/200+ tiers ($13.26/$11.36/$9.47 per sq ft) price below the $15.43/sq ft absolute floor established by §31. Classified as a Nick-directed **One-Time Exception** per Core Rule 12/13 — non-precedent-setting, consistent with the P/N 3017572 precedent.

**Strategic Flags:**
- This item is now the account's **sole official reference point below the 0.5 sq ft band floor at this small a footprint** (0.132 sq ft) — future micro-format items will be compared against it. Flagged unanimously as High-severity by Wave 2.
- First article NOT required — not requested by Sean this session. Order quantity not specified — standard 6-tier ladder quoted, flagged for follow-up.
- do_not_benchmark = false — valid sub-scope data point, excluded from singles band DATA POINTS until production-volume acceptance, same status as P/N 1210810.
- Item count: 42 → 43. Printed/Laminated category: 32 → 33 items. Sub-scope data points: 6 → 7.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 43 rows confirmed in Supabase.

---

### 2026-07-14 — Session AL (new item): P/N 1062390 — CHART-EZR WORKING RANGE G85R (80°) BASKET 500#, fourth item at the 0.503 sq ft singles-band position, Direct Parity Exemption, no wave validation

**What:** New printed/laminated single label at 7.25" × 10.00" = 0.503 sq ft — the identical footprint already held by P/N 1082570, P/N 1068270, and P/N 1073950. Filed under the Direct Parity Exemption per `governance/PRICING_VALIDATION.md` (dimensionally and materially identical to items already quoted) — no new 4-wave AI validation session was run. Benchmark: P/N 1068270 (identical 0.503 sq ft area, identical G85/G85R Basket 500# load-chart class); precedent reinforced by P/N 1073950, which independently ran the full 4-wave process and converged unanimous 6/6 on exact parity with 1068270 at this same footprint. Tier table cloned exactly: $16.50/$10.50/$8.00/$6.25/$5.25/$4.25. Material cost $0.98/label (§25 canonical, filed at the cent — matches 1073950's filing convention).

**Key Decisions:**
- Direct Parity Exemption invoked rather than running a fresh 4-wave validation — per governance/PRICING_VALIDATION.md, items dimensionally and materially identical to something already quoted are exempt from multi-round AI validation. 1073950's independent Wave 1–4 unanimous convergence on exact parity with 1068270 at this identical 0.503 sq ft footprint is the governing precedent cited for this exemption.
- Rule 15 (Pricing Profile band check) still applies and is satisfied — $15.90/sq ft at qty 20 lands cleanly within the singles band ($15.43–$15.91/sq ft).
- No override — engine consensus (parity) accepted, override_type blank.

**Strategic Flags:**
- Open taxonomy item: model field reads G85R (vs plain G85 on 1068270/1073950) and drawing content is "WORKING RANGE" (vs BASKET JIB / TOP MOUNT JIB) — same 80° jib angle and Basket 500# load class. Does not affect pricing under the Direct Parity Exemption; flagged for Nick/Sean follow-up alongside the quote.
- First article NOT specified this session — flagged for follow-up, does not block filing. Order quantity not specified — standard 6-tier ladder quoted.
- This item does NOT add a new independent singles-band data point — the 0.503 sq ft position remains anchored where it already was, now shared by four items. Band stays at 5 confirmed data points.
- Also backfilled a pre-existing sync gap: P/N 3017572 (Session AK) was missing from the ARCHITECTURE.md Item Catalog table — added this session, no data changed.
- Item count: 41 → 42. Printed/Laminated category: 31 → 32 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 42 rows confirmed in Supabase.

---

### 2026-07-10 — Session AK (new item): P/N 3017572 — LBL - HYDAC VLV OVERRIDE, sixth sub-scope data point, 4-wave validated 1-9 through 50-99, One-Time Exception override on 100-199/200+ below the §31 floor

**What:** New printed/laminated single hydraulic valve manual override control-direction label at 7.5" × 7.0" = 0.365 sq ft — the sixth sub-scope (0.1–0.5 sq ft) data point on file. Full 4-wave atomic AI validation (24 independent responses, 6 models × 4 waves, run in Claude Chat) locked the 1-9 through 50-99 tiers at $8.75/$7.25/$6.00/$5.75 — all fully §31-compliant. Material cost computed fresh at $0.75/label (§25 canonical: $0.7114 calculated + $0.0386 buffer). Unlike 3024595, both label dimensions (7.0"/7.5") fit the 13.5" laminator independently, so orientation is a nesting-efficiency choice rather than a forced constraint — 7.0" across the 28" print bed nests 4 labels per row with zero waste.

**Key Decisions:**
- Wave 1 (Build): unanimous 6/6 on the §31 floor ($5.75 = 0.365 × $15.43 rounded up per §30) and flat termination from at least 50-99 onward; split 4/6 (flat $5.75 from 20-49) vs 2/6 (one step at $6.00 for 20-49, flat from 50-99).
- Wave 2 (Destruction): unanimous 6/6 rejection of the flat-from-20-49 structure — it priced this smaller label at a LOWER $/sq ft ($15.75) than the larger governing comparable 3024595 (0.488 sq ft, $15.88/sq ft), a size-cost inversion. Unanimous fix: raise 20-49 to $6.00 ($16.44/sq ft), hold 50-99 flat at $5.75.
- Wave 3 (Buyer Simulation): split verdict — 3/6 models had Sean question the $6.00 20-49 price and ask for ~$5.75-$5.80; 3/6 had Sean approve without friction, reading the premium as proportionate to the 25% smaller area vs 3024595. Universal finding: landing exactly at the $5.75 floor at Sean's real qty-20 order volume would let him permanently defend $15.75/sq ft as the class price — worse long-term than a contested $6.00.
- Wave 4 (Final Synthesis): 5/6 YES ship $6.00 as-is; 1/6 NO recommending $5.80 to eliminate friction. No model at any wave proposed a 100-199 or 200+ tier below $5.75.
- **Override:** Nick accepted the Wave 4 majority for 1-9 through 50-99, then separately directed a One-Time Exception override lowering 100-199 to $5.50 ($15.07/sq ft) and 200+ to $5.25 ($14.38/sq ft) — both below the §31 sub-scope root floor ($15.43/sq ft), against the unanimous validated recommendation of $5.75 for both tiers. Classified and logged per Core Rule 12/13 — non-precedent-setting; future sub-scope items must benchmark the deep tiers against the validated $5.75, not this item's overridden figures.

**Strategic Flags:**
- This is the first item where the §31 floor doctrine (established 9 days earlier on 3024595) was directly overridden by Nick. The doctrine itself is unweakened — the override is logged as item-specific and non-precedent-setting per Core Rule 13. `governance/PRICING_RULES.md` §31 and `categories/printed-laminated-orajet.md` both note this as the first tested exception.
- First article NOT confirmed with Sean — flagged for follow-up. Order quantity not specified — standard 6-tier ladder quoted.
- Item count: 40 → 41. Printed/Laminated category: 30 → 31 items. Sub-scope data points: 5 → 6.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 41 rows confirmed in Supabase.

---

### 2026-07-01 — Session AJ (new item + governance): P/N 3024595 — LBL-DNGR TIP, ELEC, CRUSH, largest sub-scope data point on file, flat tier structure, floor-applies-at-every-tier doctrine established

**What:** New printed/laminated single ANSI danger label at 15" × 4.687" = 0.488 sq ft — the largest sub-scope (0.1–0.5 sq ft) data point on file, sitting at the boundary with the singles band (~0.5 sq ft). Full 4-wave atomic AI validation (24 independent responses, 6 models × 4 waves, run in Claude Chat) locked a flat tier table: $10.75/$9.25/$7.75/$7.75/$7.75/$7.75 — the price holds flat from qty 20 through 200+. Material cost computed fresh from actual verified material files at $0.96/label (§25 canonical) — no invented figures from the validation record were carried forward, per session instruction. Lamination orientation is forced (only the 4.687" dimension fits the laminator; the 15" dimension does not), documented with process-neutral language in the production section per session instruction.

**Key Decisions:**
- Wave 1 (Build): 5/6 models converged on $7.75 at qty 20 ($15.88/sq ft), interpolating between 1210810 (0.292 sq ft, $16.27/sq ft) and the 0.503 sq ft singles-band neighbor (1068270/1073950, $15.91/sq ft); 1 outlier at $8.00 rejected as a gradient inversion.
- Wave 2 (Destruction): presented two competing deep-tier structures — a flat $7.75 ladder from qty 20–200+ vs. stepping the price below the $15.43/sq ft root floor (1230820) at higher volumes. **Unanimous 6/6 ruling: the root floor applies at every tier, at every quantity — not just qty 20.** The stepped-down structure was rejected outright as precedent-damaging (it would teach the buyer the floor is negotiable at volume). This ruling is now codified as **governance/PRICING_RULES.md §31** — the account's first explicit doctrine on this question, established because 3024595 is the first sub-scope item large enough (closest to the singles-band boundary) to force it.
- Wave 3 (Buyer Simulation): Sean approves the flat structure without pushback (threshold $8.00–$8.25/label), but flagged that the bare quote-language stub risked a clarifying email about volume step-downs. Wave 4 (Final Synthesis): 4/5 YES send-as-shown with the stronger anchor line required; 1/5 NO solely over the missing anchor line (not a pricing objection). Locked quote language adopted (cost-floor framing, not the bare stub).
- No override — Nick locked the tier table prior to file-write per the 4-wave record; Claude Code did not re-derive or second-guess the price.

**Strategic Flags:**
- **New governance precedent:** §31 added to `governance/PRICING_RULES.md` — the $15.43/sq ft root floor applies at every quantity tier on every sub-scope item, not just the qty-20 comparable rate. Future sub-scope items approaching the ~0.5 sq ft boundary inherit this doctrine without re-litigating it.
- First article NOT confirmed with Sean — flagged for follow-up. Order quantity not specified — standard 6-tier ladder quoted.
- Item count: 39 → 40. Printed/Laminated category: 29 → 30 items. Sub-scope data points: 4 → 5.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 40 rows confirmed in Supabase.

---

### 2026-07-01 — Session AI (new item): P/N 1277020 — CHRT-D100i FG PLTF, fifth confirmed singles-band data point at a new 0.635 sq ft position, $10.00/qty 20, 4-wave validated

**What:** New printed/laminated single label at 8.5" × 10.75" = 0.635 sq ft — a genuinely new sq ft position in the singles band (≥0.5 sq ft), between the 0.609 sq ft cluster (1278980/1277300/1279020, $15.60/sq ft) and the 1.296 sq ft root benchmark (1230820, $15.43/sq ft — hard floor). Full 4-wave atomic AI validation (24 independent responses, 6 models × 4 waves, run in Claude Chat) locked $10.00/qty 20 = $15.75/sq ft — the fifth confirmed singles-band data point, not a parity exemption. Material cost computed fresh from the §25 canonical formula at $1.24/label using actual verified rates in `governance/PRODUCTION.md` — no invented cost figures from the validation record were carried forward, per session instruction.

**Key Decisions:**
- Wave 1 (Build): 5/6 models converged on $10.00 at qty 20, interpolating between the 0.609 sq ft cluster and root benchmark. Wave 2 (Destruction): unanimous 6/6 HIGH — flagged a minor inversion of $10.00 against the 0.609 sq ft point; the team moved to $9.75 mid-process. Wave 3 (Buyer Simulation): unanimous instant approval of $9.75, but flagged that it undercuts the root benchmark floor. Wave 4 (Final Synthesis): unanimous 6/6 NO on $9.75 — $10.00 is the only value simultaneously $0.25-compliant (§30), above the root benchmark floor, and inside Sean's confirmed pushback threshold. $10.00 locked; $9.75 explicitly rejected, do not revive in any future session.
- Band positioning: $15.75/sq ft is the highest $/sq ft point in the band above 0.609 sq ft — an accepted small-format-premium variance per Wave 4 consensus (only 0.026 sq ft past that data point). Breaks strict monotonicity-by-size at this one point, but stays safely above the root benchmark floor. Documented as a deliberate exception, not an error.
- No override — Wave 4 correction is the accepted engine outcome (override_type blank).

**Strategic Flags:**
- First article NOT confirmed with Sean — open item, flagged for follow-up alongside the quote. Order quantity not specified — standard 6-tier ladder quoted.
- $9.75 was explored and unanimously rejected in Wave 4 — future sessions must not treat it as a candidate or benchmark for this item.
- Item count: 38 → 39. Printed/Laminated category: 28 → 29 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 39 rows confirmed in Supabase.

---

*Entries older than Session AI (2026-07-01) were removed per the 10-entry rolling window — git history retains them in full.*
