# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> **Rolling window: 10 entries max. When adding an 11th, remove the oldest. Git retains all history.**
>
> This file is the session memory layer: why decisions were made, what changed strategically, what a future session needs to know. It is not a commit log and not a validation archive — full validation records live in `items/*.md` (Pricing Derivation), file-level changes live in git history, and structure/math compliance is enforced by `scripts/validate.py`. Entry format (template in `.claude/COMPLETION_TEMPLATES.md`): What / Key Decisions / Strategic Flags / Status, 10–25 lines per entry, no other sections.
>
> Last Updated: 2026-07-14 (Session AL — P/N 1062390 added, fourth item at the established 0.503 sq ft singles-band position, alongside 1082570/1068270/1073950; Direct Parity Exemption applied per governance/PRICING_VALIDATION.md — no new AI validation session run, precedent inherited from 1073950's independent 4-wave validation converging on exact parity with 1068270 at this same footprint. Previously Session AK — P/N 3017572 added, sixth sub-scope data point at 0.365 sq ft; 4-wave AI validation locked the 1-9 through 50-99 tiers ($8.75/$7.25/$6.00/$5.75), all §31-compliant; Nick then directed a One-Time Exception override lowering 100-199 to $5.50 and 200+ to $5.25, both below the §31 sub-scope root floor — classified and logged, non-precedent-setting. Previously Session AJ — P/N 3024595 added, largest sub-scope data point on file at 0.488 sq ft, sitting at the boundary with the singles band; 4-wave validated flat tier structure ($10.75/$9.25/$7.75/$7.75/$7.75/$7.75); Wave 2 unanimous ruling that the $15.43/sq ft root floor applies at every tier, not just qty 20, now codified as governance/PRICING_RULES.md §31.)

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

*Entries older than Session AC (2026-06-29) were removed per the 10-entry rolling window — git history retains them in full.*
