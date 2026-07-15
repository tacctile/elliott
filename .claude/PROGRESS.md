# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> **Rolling window: 10 entries max. When adding an 11th, remove the oldest. Git retains all history.**
>
> This file is the session memory layer: why decisions were made, what changed strategically, what a future session needs to know. It is not a commit log and not a validation archive — full validation records live in `items/*.md` (Pricing Derivation), file-level changes live in git history, and structure/math compliance is enforced by `scripts/validate.py`. Entry format (template in `.claude/COMPLETION_TEMPLATES.md`): What / Key Decisions / Strategic Flags / Status, 10–25 lines per entry, no other sections.
>
> Last Updated: 2026-07-15 (Session AP — P/N 1001220 added, eighth sub-scope data point at 0.231 sq ft; full 4-wave AI validation followed by a post-synthesis §31 compliance correction on the deep tiers, since §31 postdated this item's wave prompts — first sub-scope item to reach a fully §31-compliant flat structure directly, without a One-Time Exception override. Previously Session AO — P/N 1146650 added, second Band A interior data point at 2.971 sq ft, between the 2.512–2.564 sq ft cluster and 3010701; full 4-wave AI validation on 20-49 through 200+, Owner Judgment override on 1-9/10-19 after discovering P/N 3018378 was omitted from the wave benchmark set. Previously Session AN — P/N 1132950 added, fifth item at the established 0.503 sq ft singles-band position, alongside 1082570/1068270/1073950/1062390; Direct Parity Exemption applied per governance/PRICING_VALIDATION.md — no new AI validation session run, precedent inherited from 1073950's independent 4-wave validation and 1062390's direct-parity filing.)

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

*Entries older than Session AG (2026-06-30) were removed per the 10-entry rolling window — git history retains them in full.*
