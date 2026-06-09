# Elliott Equipment — Full System Audit (Pricing Engine + Calculator)

**Date:** 2026-06-09
**Type:** Read-and-report only. No source files modified.
**Scope:** Entire repo — all 23 items, all 11 materials, both categories, all 7 governance docs, all 5 scripts, both `index.html` script blocks (engine executed via Node vm harness), all 3 frontend JSONs, CI workflow, prior audits. Every number below was independently recomputed from raw inputs; no PROGRESS.md claim was accepted as evidence.

---

## 1. Executive Summary

### Verdict: **SAFE TO QUOTE FROM — WITH CAVEATS (catalog yes, calculator brief no)**

The **catalog layer** — the 23 item files whose tier tables are what Sean is actually invoiced against — is arithmetically immaculate. Every tier ladder, margin, sq-ft computation, band anchor, and kit-parity claim recomputes exactly. All six bands agree across category files ↔ ARCHITECTURE ↔ item math ↔ calculator config to the penny on every anchor. No path exists today by which a wrong *catalog* price reaches Sean.

The **calculator layer** is not currently fit for its documented purpose. The strict tier-boundary cascade (Session C) drives every brief 29–46% below the locked catalog and the band, the brief stamps itself "READY FOR ROUND 1: YES" while internally contradicting itself (anchor line $20.00 vs tier table $11.38 on the same page), the kit UI table shows pre-enforcement per-label prices next to post-enforcement kit totals, and the buyer-language stub embeds the crushed price. A fresh session that follows the documented workflow (calculator brief → Wave 1) would anchor the entire validation ~40% low.

**Caveats in force until fixed:**
1. Do not use any calculator tier table, margin, or quote stub as a price input — catalog `items/*.md` is the only safe price source (this matches Session C's own framing, but the engine's "READY: YES" badge and stub language actively contradict it).
2. Do not run a 4-wave session off `VALIDATION_PROMPTS.md` §3's embedded band table — it is missing 3 of the 6 bands and 5 benchmark anchors.
3. Margin strings across the printed/lam catalog are not cross-comparable — three costing eras coexist (§25 canonical / legacy-overstated / legacy-understated), including inside the kit family.

**Finding counts:** 1 CRITICAL / 5 HIGH / 15 MEDIUM / 11 LOW / 7 INFO / 14 WORKING WELL.

### Top 5 Risks
1. **[C-1]** Calculator brief is presented as safe ("READY: YES") while its numbers sit 29–46% below catalog/band on every route, with self-contradictory anchor-vs-table presentation and a buyer-facing stub carrying the wrong price.
2. **[H-3]** A wave session run today operates with an incomplete band fence — `VALIDATION_PROMPTS.md` §3 omits the Micro-Format Band, Band B, Band C, and the expanded Band A, plus 5 benchmark anchors.
3. **[H-5]** Costing-era mixing: the kit family mixes a §25-canonical member (1278890, $2.40) with two legacy-understated members (1278930 $2.99 vs canonical ≈$3.60; 1245130 $5.16 vs ≈$5.97), and 1068270 — created 8 days *after* §25 — claims §25 compliance while filing 1082570's legacy $1.33 via a ~$0.35 "incidental buffer" (10× the convention).
4. **[H-2]** The calculator UI cannot express the account's only permitted ink assumption — the dropdown offers low/medium/high/flood-coat with **medium as default**; `full_bleed_flood_coat` is unreachable. Every UI-driven brief computes material cost on a deprecated rate, in direct violation of §25.
5. **[H-4]** `CALCULATOR.md` is internally contradictory: §6.3's regression checklist still expects MOQ-era behavior ($20/F18+F11) that §9 says is wrong, ghost flags F18/F19 remain documented, and two documented flags (F11, F16) are provably unreachable in the engine.

### Top 5 Strengths
1. **Catalog arithmetic is perfect** — 23/23 items recompute exactly (sq ft, per-label, margins, monotonic ladders); the kit family's three-way parity holds to four decimals ($16.4204/sq ft on all three).
2. **`enforceTierBoundaries()` / `checkInvoiceProtection()` are mathematically correct** — penny-precision in both, bottom-up cascade verified, zero residual violations on every enforced route, F23 detail math exact.
3. **Routing boundary semantics match documentation exactly** at every probed edge (0.1 / 0.5 / 1.0 / 5.0, inclusive/exclusive as documented), and orientation-flipped inputs (1068270 vs 1082570) produce identical engine output.
4. **Band-anchor sync is real**: every anchor value (13.65–13.94, 11.03, 20.64, 15.43–15.91, 30.86, $10.00/$16.42) matches across all four sources.
5. **The do-not-benchmark fence works** — engine-side filtering verified, and the 6 one-off item files carry exhaustive, correctly framed warnings.

---

## 2. Phase 0 — Baseline

- **Branch:** `claude/trusting-goodall-1tk1pp`, clean tree at start. `git log -1`: `7f3f698 system: auto-rebuild frontend data + sync images`.
- **`python scripts/validate.py`** → `PASS: 0 errors, 0 warnings` (23 items).
- **`python scripts/build_frontend.py`** → `✓ Synced images: 4 files … ✓ Built frontend/data.json — 23 items`.
- **`python scripts/build_materials.py`** → `✓ Built frontend/materials.json — 11 materials`.
- **`python scripts/build_calculator_config.py`** → `✓ 4 material constants, 4 bands, 8 do_not_benchmark items`.
- **`python scripts/profile.py`** → runs clean; output used as cross-check (note: it reports 1279000 at **$30.93**/sq ft from frontmatter 0.097, vs the documented band anchor **$30.86** from unrounded 0.0972 — see L-2).
- **Script-block parse check (Node `new Function(blockSrc)`):** 2 inline blocks found (UI 50,113 chars; engine 66,558 chars) — **both parse OK**.
- **Counts:** 23 item files = ARCHITECTURE catalog rows (23) = STATE.yml `item_count: 23` = data.json `item_count: 23`. 11 material files = materials.json. Category registry: cut vinyl 9 + printed/lam 14 = 23. **No count mismatches.**
- Build scripts regenerate timestamp-only diffs in the 3 frontend JSONs; reverted via `git checkout -- frontend/*.json` before commit per audit rules.

---

## 3. Findings by Severity

### CRITICAL

```
[C-1] CRITICAL — Calculator brief presents cascade-crushed prices as validation-ready,
      contradicts itself in one document, and embeds the wrong price in buyer-facing stub language
Files: frontend/index.html (engine block: enforceTierBoundaries ~3482, generateBrief ~3932,
       generateQuoteStubs ~3876, ready badge ~4047); governance/CALCULATOR.md §9
Evidence (all from live engine runs, Node vm harness):
  • Engine @qty 20 vs locked catalog: 1230820 $11.38 vs $20 (−43.1%); 1082570/1068270 $4.39 vs $8
    (−45.1%); 1210810 $2.58 vs $4.75 (−45.7%); 1278890 $11.38 vs $20 (−43.1%); 1278930 $18.64 vs
    $30 (−37.9%); 1245130 $31.07 vs $50 (−37.9%); 1205720 $22.78 vs $35 (−34.9%); 3010701 $31.07
    vs $44 (−29.4%); 3010704 $53.85 vs $78 (−31.0%); 3010707 $11.89 vs $20 (−40.5%).
  • Brief $/sq ft: 1230820 lands at $8.78/sq ft vs the $15.43 band floor it is supposed to seed.
  • Same brief, same page (1278890 run): "Anchor (qty 20-49): $20.00 ($16.42/sq ft)" directly above
    a tier table whose 20-49 row reads $11.38 (79.2% margin) — two contradictory prices, no warning.
  • Quote stub emitted: "…priced at $11.38 at your projected monthly volume." for a $20/kit item.
  • Badge: "READY FOR ROUND 1 AI VALIDATION: YES" (badge tests only for STOP flags).
  • F7 + F23×5 fire on 11 of 12 standard runs — 100% alarm saturation, zero signal.
Impact: The documented workflow (MASTER_CONTEXT reading order; CALCULATOR.md §7 step 2-3) feeds
  this brief to Wave 1. A fresh session, or Nick on a busy day copying the stub, propagates a
  ~40%-low anchor. Catalog itself is unaffected — but the tool whose entire purpose is "same
  price every time" produces a different, wrong, self-assured number.
Blast radius: every future new-item session; every re-run on an existing item; Wave 1–4 inputs.
Recommended fix: resolve Decision Fork D1, then make the brief self-consistent: one price story
  per brief, badge must reflect F7/cascade state, stub must source the band/template price (or be
  suppressed when enforcement mutated tiers).
Effort: M (engine) — but gated on D1.
Decision required from Nick: YES — D1 (cascade design, see §8).
```

### HIGH

```
[H-1] HIGH — Kit per-label tiers desync from enforced kit totals (UI table shows $10.00/label
      beside $11.38/kit on the same row)
Files: frontend/index.html — buildPrintLamKitTiers (~3312: per_label_tiers built pre-enforcement),
       runCalculator step 5b (~4138: enforcement overwrites tiers/kit_totals but NOT per_label_tiers),
       renderCalcPricingTable (~2688: perLabelTiers preferred over price/label_count)
Evidence: 1278890 probe → pricing.kit_totals 20-49 = $11.38, pricing.per_label_tiers 20-49 = $10.00
  (pre-enforcement). UI kit table renders "Per Label $10.00 | Per Kit $11.38" — $10.00 × 2 ≠ $11.38.
  Same desync on 3-label ($10.00 vs $18.64) and 5-label ($10.00 vs $31.07) template runs. The brief
  text itself is internally consistent (it recomputes per-label = total/lc → $5.69), which means
  brief and UI table disagree with each other too.
Impact: wrong per-label reasoning displayed in the official tool on every kit run.
Blast radius: all kit quoting sessions.
Recommended fix: rebuild per_label_tiers after enforcement (or derive in renderer from enforced
  totals). One-line class of fix; falls out automatically if D1 makes enforcement report-only.
Effort: S
Decision required: no (but sequencing depends on D1).
```

```
[H-2] HIGH — §25 full-bleed is unreachable from the calculator UI; engine defaults to the
      forbidden 'medium' assumption
Files: frontend/index.html — ink select (lines 1490–1496: low/medium[selected]/high/flood_coat/
       flood_coat_safety_red — no full_bleed option), engine default ink_coverage:'medium'
       (~3158, ~4067); frontend/calculator_config.json ink_rates (medium marked "DEPRECATED for
       routing — historical reference only")
Evidence: §25 / MASTER_CONTEXT Core Rule 8: "No medium, low, or partial coverage assumptions are
  permitted on any Elliott printed/laminated item — past, present, or future." Config names
  full_bleed_flood_coat the account default. The UI cannot select it; the engine falls back to
  medium ($0.44/sq ft) when unset; sanity cases pin legacy rates ('high', 'flood_coat').
  Material-cost lines in every UI-driven brief are computed on deprecated rates.
Impact: brief material costs / margins violate the account's only ink rule; Wave 1–2 cost-auditor
  reasoning starts from non-canonical numbers. Tier prices are band-anchored so the price number
  is unaffected — the margin story is what's wrong.
Blast radius: every printed/laminated brief generated from the UI.
Recommended fix: make full_bleed_flood_coat the only (or default+preselected) option for this
  account; keep legacy keys for historical sanity cases only.
Effort: S
Decision required: no.
```

```
[H-3] HIGH — VALIDATION_PROMPTS.md §3 band fence is three bands and five anchors out of date;
      one MOQ reference survived the purge (S6)
Files: governance/VALIDATION_PROMPTS.md §3 (lines 118–151), §5 (line 235)
Evidence:
  • "Current Pricing Bands to Embed" lists 4 bands: singles, kits, cut vinyl concession, cut vinyl
    AI-consensus. Missing: Micro-Format Band ($30.86, est. 2026-06-05), Band B ($11.03, 2026-06-05),
    Band C ($20.64, 2026-06-05), and Band A's expansion to 1.0–5.0 sq ft with the 3010701 data point.
  • Cut vinyl row note: "All 4 current cut vinyl items inside" — there are 9, 5 of them in Band A.
  • Benchmark anchors omit 3010704, 3010707, 1279000, 3010701, and kit member 1278890.
  • Embedded 1230820 tier table ($30/$24/$20/$17/$14/$11) — verified CORRECT vs item frontmatter.
  • §5 Wave-3 inclusion list still says "anchor line + MOQ language (printed/laminated)" — MOQ
    language no longer exists anywhere downstream (Session A/B purge).
  • COMPLETION_TEMPLATES.md has an explicit trigger ("Validation wave prompts need updating (band
    shift … new benchmark item) → update VALIDATION_PROMPTS.md Sections 3 and 5"). Sessions that
    established Band B, Band C, the Micro band (D), Band A expansion (E), and the kit third anchor
    (G) — five sessions — all logged "No VALIDATION_PROMPTS.md changes." Each is a Self-Healing
    Rule violation against a then-existing trigger.
Impact: a wave session run today on a sub-1 sq ft cut vinyl, large-format, micro, or 3–5 sq ft
  Band A item gives 6 external models the wrong/missing fence — exactly the failure mode the
  document exists to prevent.
Blast radius: all future 4-wave validations until fixed.
Recommended fix: rebuild §3 to embed all six bands + all current anchors (1230820, 1278930/1245130/
  1278890, 1205720+3010701, 3010704, 3010707, 1279000); drop the MOQ phrase in §5; add band table
  to the §6.1-style constant-sync checklist.
Effort: S–M (documentation only)
Decision required: no.
```

```
[H-4] HIGH — CALCULATOR.md diverges from the engine: ghost flags, dead flags, contradictory
      regression expectations, surviving MOQ text, and a Rule 11 claim the engine intentionally breaks
Files: governance/CALCULATOR.md §1 (line 28), §3 (lines 144, 171–172), §4 Rule 11 (line 210),
       §6.3 (lines 332–339), §7 Step 9 (line 410), §9 (line 447, 451)
Evidence (engine FLAG_DEFS read + live probes):
  • Engine has 21 flags (F1–F17, F20–F23). Doc says "All 22 flag definitions" and tabulates 23
    rows including F18/F19, removed from the engine in Session B (ghost rows, S4).
  • F11 is unreachable: post-enforcement checkInvoiceProtection always finds 0 violations
    (verified on all 12 routes); on the only path that skips enforcement (micro template), the
    autofix that sets F11 is explicitly disabled. F11 fired on zero probes.
  • F16 is unreachable: it requires lam passes > 2, but computeLamPasses can only return 1, 2, or
    STOP(null) — verified by code path and 7-label probe (returned 1 pass, no F16/F20).
  • §4 Rule 11: "checkInvoiceProtection … should report zero violations after enforceTierBoundaries
    has run; if it ever finds a violation, that is a bug." The Session-D micro-template path skips
    enforcement and reports 5 violations BY DESIGN (probe: violations=5, informational). Rule 11
    doesn't document the skip_enforcement exception it now has.
  • §6.3 regression checklist still expects MOQ-era results: "1230820 → single_standard, $20,
    F18 + F11", "MOQ row when applicable" — flatly contradicting §9 of the same document
    (~$11.38, F23×5, F7). A fresh session following §6.3 would conclude the engine is broken.
  • §9 PROD-OVERRIDE row claims "micro template has no 9/10 inversion at template values, so F23
    fires fewer times" — wrong twice: the template has cliffs at ALL 5 boundaries (9×$4.50=$40.50 >
    10×$3.50=$35.00, …), and F23 fires ZERO times (enforcement skipped). Probe: flags = F10, F8 only.
  • §1 still lists "MOQ language obligations" as a calculator self-audit surface; §7 Step 9 still
    tells Nick to use "MOQ language" stubs.
  • §3 header: doc count wrong under any interpretation (21 in engine, 23 in table, "22" in prose).
Impact: the document that calls itself "the contract" cannot be trusted by a fresh session;
  two documented safety flags are dead code.
Blast radius: any engine-change session (uses §6.3 as its test list), any flag-triage session.
Recommended fix: delete F18/F19 rows; correct count; rewrite §6.3 to match §9; document
  skip_enforcement in Rule 11; fix §9 PROD-OVERRIDE row; strip residual MOQ text; either remove
  F11/F16 from the engine+doc or document them as reserved/unreachable.
Effort: S (documentation) + S (optional dead-flag removal)
Decision required: no.
```

```
[H-5] HIGH — Mixed §25 costing eras across the printed/lam catalog, including inside the kit
      family; newest single (1068270) claims §25 while filing a non-§25 number; PRODUCTION.md
      still declares the legacy kit costs "canonical" (S1)
Files: items/1230820.md (~line 115 "$0.91 waste/setup"), items/1278930.md (114–119),
       items/1245130.md (114–119), items/1082570.md (162–176), items/1068270.md (158–169),
       governance/PRODUCTION.md (Material Cost Quick Reference, line 163)
Evidence (canonical = kit_sq_ft × $1.9489 + buffer; recomputed):
  | P/N     | filed  | canonical raw | Δ       | class               | margin filed→canonical |
  | 1230820 | $3.23  | $2.526        | +$0.70  | LEGACY-OVERSTATED   | 83.9% → 87.4% (+3.5)   |
  | 1082570 | $1.33  | $0.980        | +$0.35  | LEGACY-OVERSTATED   | 83.4% → 87.7% (+4.4)   |
  | 1068270 | $1.33  | $0.980        | +$0.35  | LEGACY-OVERSTATED   | 83.4% → 87.7% (+4.4)   |
  | 1278930 | $2.99  | $3.561        | −$0.57  | LEGACY-UNDERSTATED  | 90.0% → 88.1% (−1.9)   |
  | 1245130 | $5.16  | $5.934        | −$0.77  | LEGACY-UNDERSTATED  | 89.7% → 88.1% (−1.6)   |
  | 1210810 | $0.60  | $0.569        | +$0.03  | CANONICAL           | —                       |
  | 1278890 | $2.40  | $2.374        | +$0.03  | CANONICAL           | —                       |
  | 1279000 | $0.20  | $0.189        | +$0.01  | CANONICAL           | —                       |
  | one-offs (1277970–1278000, 3017583/84): JOB-BASED (production-footprint method, documented)   |
  • 1068270 (created 2026-06-09, §25 est. 2026-06-01) Nesting section: subtotal $0.98 + "Incidental
    buffer (conservative) ~$0.35" = $1.33 — a buffer 10× the account convention ($0.01–$0.03
    elsewhere), used to make §25 reproduce the legacy parity number while citing §25 three times.
  • 1278930 breakdown doesn't sum: $2.21 + $0.21 + $0.81 = $3.23 stated as "Total ~$2.99".
    1245130: $3.68 + $0.28 + $1.35 = $5.31 stated as "Total ~$5.16".
  • PRODUCTION.md line 163: "Always use the kit-level totals ($2.99 and $5.16) as canonical
    material costs" — direct contradiction of §25's formula and of how Session G built 1278890.
  • §25's own text: "The frontmatter material_cost_per_unit field on EVERY printed/laminated item
    reflects the buffered total" — false for 5 of 14 items.
  • No sell price changes under either basis; margin-floor sweep shows zero floor crossings under
    either cost basis (see §5 sweep).
Impact: margin strings are not comparable across the catalog; the kit family's "~88% vs ~90%"
  story inverts under canonical costing (all three ≈88.1%); a future session computing kit costs
  per PRODUCTION.md vs §25 gets different numbers from two "canonical" sources.
Blast radius: 5 item files, PRODUCTION.md, ARCHITECTURE margin columns, category margin bands,
  every future margin argument (incl. Jan-2027 normalization math).
Recommended fix: Decision Fork D2 — rebuild the five legacy costs to §25 (documentation-only,
  no sell-price changes) or formally grandfather them with an explicit exemption note in §25 and
  PRODUCTION.md. Either way, fix the PRODUCTION.md "canonical" sentence and the two non-summing
  breakdowns.
Effort: S–M (documentation only)
Decision required: YES — D2.
```

### MEDIUM

```
[M-1] MEDIUM — Tape cost on the small-format cut vinyl cluster uses an area × pseudo-rate method,
      overstating tape ~2.7× (conservative) (S2)
Files: items/1205720.md (~113), items/1186310.md, items/3017435.md, items/3018378.md (Nesting);
       materials/transferrite-582u.md (cost_per_sq_ft 0.5911)
Evidence: $0.5911 = $1.1821/yd ÷ 2 ft — dimensionally $/yd·ft, not $/sq ft (true area rate:
  $1.1821 / 6 sq ft = $0.197). Filed tape: 1205720/3017435 2.56 × 0.5911 = $1.513; 1186310 $1.516;
  3018378 $1.485. True length-based (method used by 3010701/04/07/08/09): 1205720/1186310
  0.9323 yd × $1.1821 ÷ 2 = $0.55; 3018378 $0.54; 3017435 1.22 × 1.1821 ÷ 2 = $0.72.
  Restated true margins @20: 1205720/1186310 77.8% (filed 75.0%); 3018378 77.2% (74.5%);
  3017435 75.1% (72.8%). Direction: conservative (costs overstated, margins understated).
  Note: vinyl on these items is length-based and correct — there is no compensating vinyl error;
  the totals are simply ~$0.77–$0.96 high. The 2026-05-28 audit endorsed this method at the time.
Impact: no sell price affected; erodes "same math every time" — two tape conventions now coexist
  by item age, and the 200+ warn-floor on 3017435 (56.8% filed) clears comfortably (64.5%) under
  the true method.
Recommended fix: Decision Fork D3 — harmonize the 4 cluster items to the length method
  (documentation-only) or declare the pseudo-rate a deliberate conservative convention in
  PRODUCTION.md. Newer items already use length; harmonizing is the consistency-preserving choice.
Effort: S
Decision required: YES — D3.
```

```
[M-2] MEDIUM — The calculator engine consumes the 0.5911 pseudo-rate as an area rate for ALL cut
      vinyl tape, and ignores per-row feed spacing (S3 fragility realized)
Files: frontend/index.html computeCutVinylMaterial (~3090: tape = sq_ft × material_constants.
       transferrite_582u.cost_per_sq_ft), computeCutVinylForRollWidth (~3064: length = wide/36,
       no 6" row spacing)
Evidence: 3010701 probe — engine vinyl $10.58 (filed $11.87, no 6" spacing), engine tape $1.89
  (filed length-based $0.91), engine total $12.48 vs filed $12.78. Two opposite errors happen to
  nearly cancel here; on Band C geometry they would not (engine has no multi-up tape amortization).
  Also contradicts material-file notes ("Item pricing uses cost_per_linear_yd directly").
Impact: engine cut-vinyl material costs/margins are method-wrong even when numerically close;
  margins drive F4/F5/F6 firing.
Recommended fix: engine tape should use feed-length × $/yd ÷ labels_across (same loop as vinyl);
  decide whether to model the 6" spacing. Pair with D3.
Effort: S–M
Decision required: no (method), but pairs with D3.
```

```
[M-3] MEDIUM — Hand-synced band constants in build_calculator_config.py have drifted from the
      category files in five places (S10)
Files: scripts/build_calculator_config.py (71–224) vs categories/*.md
Evidence (full number-by-number diff in §5): anchors, templates, ratios, thresholds, snap
  granularities all MATCH. Drifted:
  1. calibration_note "Band calibrated at 2.51-2.56 sq ft" vs category Band A "1.0–5.0 sq ft"
     (calibrated 2.512–3.202).
  2. concession note "All 4 current cut vinyl items priced within this band" — 9 items now, 5 in A.
  3. Band A margin_target 73.0–78.0 vs category "~70.9–78%" (3010701 at 70.9%).
  4. Band A tier_compression_pct 51.0 vs category "31.6–51%" (3010701 at 31.6%).
  5. Kits: margin_floor_warn_pct 83.0 vs category "~80–83%" (1278890 at ~80%); no
     tier_template_2label for the now-validated 2-label kit; singles note omits 1068270.
  Mitigating: items 3–5 are decorative today — the engine reads only the global flag_thresholds
  (the per-band margin_floor_warn/stop values are never consumed by index.html).
Impact: silent drift channel exactly as designed-against; the unused per-band floors invite a
  future session to "fix" the wrong constant.
Recommended fix: sync the five values; add a 2-label kit template (Decision: template vs cost-build
  is also part of D1's scope); either wire per-band floors into the engine or delete them.
Effort: S
Decision required: no (template addition noted under D1).
```

```
[M-4] MEDIUM — singles_band_ceiling_sq_ft: 2.0 contradicts the category's calibrated 0.5–1.3
      scope, and single_standard routing is unbounded above (S9)
Files: scripts/build_calculator_config.py:56; frontend/calculator_config.json routing;
       categories/printed-laminated-orajet.md ("calibrated 0.5–1.3 sq ft")
Evidence: the constant appears only in route_reason text ("within the singles band scope (0.5-2)").
  A 3.0 sq ft printed item routes single_standard with text claiming a 0.5–2.0 scope; the category
  says the band is calibrated only to 1.296. No F-flag exists for "above calibrated range."
Impact: brief text overstates band coverage; a >1.3 sq ft item gets band-anchored pricing with no
  "requires validation" signal.
Recommended fix: set ceiling to the calibrated 1.3 (or band max data point), and fire F8-equivalent
  above it; at minimum make the route_reason cite the calibrated range.
Effort: S
Decision required: no.
```

```
[M-5] MEDIUM — CI never runs validate.py and never rebuilds on categories/ or governance/ changes
Files: .github/workflows/build-frontend.yml (paths: items/**, materials/**, 3 build scripts)
Evidence: workflow has no validate step; a band change in categories/*.md triggers nothing (and
  since band constants are hand-synced in the build script, a category edit without a script edit
  silently diverges with no CI surface at all).
Impact: the repo's only automated gate (validate.py) is local-discipline-only; drift class M-3 has
  no tripwire.
Recommended fix: add validate.py as a required CI step on all pushes; add categories/** and
  governance/** to path triggers; consider a config-drift assertion script (compare config bands
  to category-file numbers).
Effort: S
Decision required: no.
```

```
[M-6] MEDIUM — Micro-band algorithmic path ignores the documented per-label floor below ~0.06 sq ft
Files: frontend/index.html buildPrintLamMicroTiers (~3245); categories/printed-laminated-orajet.md
       ("DO NOT linearly extrapolate below ~0.06 sq ft… per-label floor (~$2.50–$3.00 at qty 20)")
Evidence: probe 0.05 sq ft + production_override → algorithmic scaling → $1.03 @ qty 20 (enforced),
  no floor, no dedicated flag. The category file says this number is structurally wrong and a
  fresh job-economics validation is required below 0.06.
Impact: an unsafe number presented with only generic flags (F10/F8/F7/F22) on the exact size class
  the governance singles out.
Recommended fix: clamp algorithmic micro output at the documented per-label floor or fire a
  dedicated REVIEW flag below 0.06 sq ft.
Effort: S
Decision required: no.
```

```
[M-7] MEDIUM — Engine input robustness gaps: W2 (zero dims), W3 (1-label "kit"), W6 (unknown color)
      all still open from the 2026-06-01 audit
Files: frontend/index.html runCalculator/determineRoute/computeCutVinylMaterial
Evidence (probes):
  • W2: width=0/height=0/label_count=0 → route tiny, $55 flat table, no STOP (UI guards w/h but
    not the engine; label_count=0 not guarded anywhere).
  • W3: item_type=kit_same_dim with label_count=1 → kit route, cost-builds $10×1 → $5.68@20
    (enforced) with no review flag.
  • W6: cut_vinyl_color='nonexistent' → breakdown_text "Unknown cut vinyl color key", but tiers
    continue ($19.67@20), margins null, no STOP flag.
Impact: nonsense numbers render without a blocking signal if inputs arrive programmatically or a
  future UI change relaxes guards.
Recommended fix: add an input-sanity STOP (dims ≤ 0, label_count < 1), re-route lc=1 kits to
  single with INFO flag, fire a STOP on unknown color.
Effort: S
Decision required: no.
```

```
[M-8] MEDIUM — Validation brief still incomplete vs PRICING_VALIDATION.md Round 1 input spec (W4)
Files: frontend/index.html generateBrief (~3932); governance/PRICING_VALIDATION.md Round 1
Evidence (field-by-field, 1278890 brief):
  ✓ full specs, ✓ material breakdown, ✓ tier table with margins, ✓ band positioning + comparables,
  ✗ "Production process step by step, including equipment constraints" — brief carries only the
    lam-pass line;
  ✗ "Accepted benchmark item(s) with full pricing tiers" — comparables show price_20_49 only;
  ✗ "Key comparisons (sq ft, production touches, material cost ratio)" — sq ft only.
  "Ready for Round 1: YES" badge thus certifies a brief the methodology doc defines as incomplete.
Impact: Wave 1 models get a thinner input than the methodology requires; cost-auditor wave
  reasoning starts under-informed.
Recommended fix: add process-steps block (from PRODUCTION.md per route), full 6-tier tables for
  top-N comparables, and a key-comparisons section.
Effort: M
Decision required: no.
```

```
[M-9] MEDIUM — inferOverrideType() is still route-based (W5) and now actively mislabels every
      cut vinyl comparable as "Relationship Concession"
Files: frontend/index.html (~3657–3660)
Evidence: function ignores fm.override_type entirely; returns 'Relationship Concession' for ALL
  cut vinyl. Probe: 3010701's comparables table lists itself as "Relationship Concession" —
  3010701, 3010704, 3010707/08/09 have override_type "" (engine-consensus, no override). Rule 14
  workflows key off override type; data.json can't help because build_frontend STRIPS
  override_type (the engine literally cannot read the truth today).
Impact: briefs misstate the override status of 5 of 9 cut vinyl items — a Rule 14 misread risk in
  benchmark selection.
Recommended fix: stop stripping override_type from data.json (it's internal-facing anyway — see
  M-15 fork) and read fm.override_type; or at minimum return 'Unknown'.
Effort: S
Decision required: couples to M-15/D4.
```

```
[M-10] MEDIUM — benchmark/downstream chains are stale in 5 item files; the 1082570→1068270
       lockstep link exists only outside the item file
Files: items/1230820.md, items/1278930.md, items/1245130.md, items/1205720.md, items/1082570.md
Evidence: 1230820 downstream omits 1278890 (and pricing_logic names only 1278930/1245130);
  1278930 downstream omits 1278890; 1245130 says "None yet. End of current chain." (1278890 now
  exists); 1205720 downstream lists only 3017435 (1186310, 3018378 benchmark it; 3010701 anchors
  on it); 1082570 downstream = "None" while Session F declared the parity link "structural and
  permanent — update in lockstep" (the lockstep instruction lives only in ARCHITECTURE/PROGRESS).
Impact: a future 1082570 material/cost session that follows the item file alone will not see the
  1068270 lockstep obligation — the exact drift S-class the parity rule warned about.
Recommended fix: update the five downstream/benchmark fields; add the lockstep note to both item
  files' Notes sections.
Effort: S
Decision required: no.
```

```
[M-11] MEDIUM — §26 cliff documentation is inconsistent: every multi-tier item has cliffs at all
       5 boundaries, but only 3 item files document them fully (S14 adjudication detail)
Files: all multi-tier items
Evidence: recomputed inventory (§5): 17 multi-tier items × 5 boundaries = 85 real inversions, all
  resolved by §26 at billing. Fully documented in-file: 1278890 (table, all 5), 3010701 (table,
  all 5), 1279000 (all 5). Partially: 1210810 (2 of 5 — 9/10, 19/20 only). Not documented in-file:
  1230820, 1278930, 1245130, 1082570, 1068270 (generic inheritance note only), 1205720, 1186310,
  3017435, 3018378, 3010704, 3010707/08/09 (anchor-reference only). No undocumented-and-unknown
  cliff exists (the §26 principle is global), but "documented at every boundary" is true for only
  3 of 17.
Impact: doc-consistency erosion; a billing question on, e.g., 1245130 at 99/100 ($757 inversion)
  has no in-file answer.
Recommended fix: backfill the 1278890-style §26 table into the remaining multi-tier files
  (documentation-only); make it part of the new-item template.
Effort: M (mechanical)
Decision required: no.
```

```
[M-12] MEDIUM — Prior-audit prose-drift findings never fixed (I2 family), plus one new instance
Files: items/1277970.md:167, items/3017583.md:164, items/3017583.md:233
Evidence: 1277970 line 167: "Frontmatter material_cost_per_unit carries the per-label figure
  ($0.35)" — frontmatter is 0.24 (flagged as I2 on 2026-06-01, still present). 3017583 line 164:
  same pattern, "$0.28" vs frontmatter 0.22. NEW: 3017583 line 233 contribution-margin bullet says
  "Material cost: ~$1.70" while the job-inputs table (line 222) and Margin Analysis (line 274) say
  ~$1.33 (the 2026-06-01 housekeeping fixed pricing_logic but not this bullet). Also 3017583
  frontmatter margin "~97%" vs computed 97.6% (body table says ~98%).
Impact: none on price ($55 program totals are floor-anchored), but it is exactly the "prose
  contradicts frontmatter" class this repo keeps re-finding; third audit to carry it.
Recommended fix: three one-line edits + margin string.
Effort: S
Decision required: no.
```

```
[M-13] MEDIUM — SPEC_EXTRACTION.md ink default still "Assumed: medium coverage", contradicting §25
Files: governance/SPEC_EXTRACTION.md (Ink Coverage Estimate row, line 68; Output Format
       "Coverage: [low/medium/high]" line 140)
Evidence: §25 (2026-06-01): full bleed always; SPEC_EXTRACTION (Last Updated 2026-05-22) still
  instructs extractors to assume medium and to emit low/medium/high. Its own Rule 6 says "When
  account-specific defaults change, update the defaults table in this file immediately." 1278890's
  extraction correctly recorded "Full bleed — Confirmed (account standard)" — sessions are
  working around the doc.
Impact: a fresh extraction session following the doc verbatim tags the forbidden assumption.
Recommended fix: change default to "Full bleed per §25 — always"; update output format enum.
Effort: S
Decision required: no.
```

```
[M-14] MEDIUM — Category files contradict themselves: cut vinyl Decision Tree step 8 voids part of
       Band A's claimed range; printed/lam singles Pricing Profile wasn't updated for 1068270
Files: categories/cut-vinyl-3m-180mc.md (Band A header "1.0–5.0" + band-width note "calibrated
       2.512–3.202" vs step 8 "items significantly outside all three bands (e.g., 1.5–2.5 sq ft…)");
       categories/printed-laminated-orajet.md (Pricing Profile "Data points: 1 confirmed…",
       "Band width: … 2 consistent data points" vs items table footnote ⁴ and ARCHITECTURE's
       "3 confirmed band data points")
Evidence: step 3 routes 1.5–2.5 sq ft to Band A; step 8 calls the same range "significantly
  outside all three bands" requiring full 4-wave — mutually exclusive instructions for the same
  item. Singles profile prose predates Session F; the registry layer (ARCHITECTURE) and the table
  layer disagree with the profile layer inside one file.
Impact: a fresh session pricing a 2.0 sq ft cut vinyl item gets two contradictory instructions
  from the declared source of truth.
Recommended fix: rewrite step 8's example to the actually-uncovered gaps (e.g., 3.3–4.99 sq ft,
  10+); update the singles Data points/Band width lines for 1068270.
Effort: S
Decision required: no.
```

```
[M-15] MEDIUM — Deployed data.json ships full internal pricing intelligence, including the
       INTERNAL-ONLY Jan-2027 normalization notes, behind only Vercel password protection (S12/S15)
Files: scripts/build_frontend.py (STRIP_FIELDS = 3 fields; sections.notes ships Notes and
       Warnings bodies); frontend/data.json
Evidence: STRIP_FIELDS today = {benchmark_item, downstream_items, override_type}. The 2026-05-22
  remediation log claims 7 fields were stripped (also pricing_logic, material_cost_per_unit,
  cost_version_date, margin_at_qty_20) — 4 were re-exposed at some point; the 2026-06-01 audit
  (I9) blessed field exposure as by-design. Since then the exposure grew: verified by grep of the
  built file, data.json['1278890'].sections.notes contains "INTERNAL ONLY — January 2027
  normalization anchor… near-breakeven fully-loaded at $85/hr… Sean now has three accepted data
  points at $10.00/label", and equivalents ship for 3010701/1210810. The script's own comment
  ("Internal fields that must never be exposed") contradicts what it ships.
Impact: a single password is the only barrier between the buyer-side strategy file and the buyer
  it must never reach; quote stubs and wave prompts remain clean (verified), so the leak path is
  the deployed app itself.
Recommended fix: Decision Fork D4 — formally accept (document the by-design state and fix the
  STRIP_FIELDS comment) or strip `sections.notes`/`pricing_logic` (and re-expose override_type
  internally per M-9). Recommend stripping at least the Internal Only subsection.
Effort: S
Decision required: YES — D4.
```

### LOW

```
[L-1] LOW — sq-ft precision inconsistencies: 1205720 files 2.56 vs 1186310's 2.564 for identical
      33.5625×11 dims; 3017435 files 2.56 (calc 2.5553). All inside validate.py's 0.01 tolerance.
[L-2] LOW — 1279000 band anchor is quoted as $30.86 (from unrounded 0.0972) everywhere, while
      frontmatter sq_ft 0.097 yields $30.93 (profile.py prints 30.93). Engine band check lands
      "above_band" by $0.07 — cosmetic but the same number is "the anchor" in two slightly
      different values.
[L-3] LOW — Naive YAML parsers ship escaped quotes as literal \" in 6 items' fields (1186310,
      3010701, 3017435, 3017583, 3017584, 3018378 — e.g. 3017435 margin renders
      '~73% (24\" roll)…' in the UI). No truncation anywhere (1468-char pricing_logic survives
      minus outer quotes). (S13 detail.)
[L-4] LOW — Engine comment/code mismatches: F8 comment says "within 30% of singles floor" but code
      tests sf ≤ floor×1.4; micro-template band position reads "above_band" (30.93 vs 30.86+0.05).
[L-5] LOW — MASTER_CONTEXT.md File Map omits the audits/ directory (now a real workflow surface)
      and still shows only 6 illustrative item files.
[L-6] LOW — CHAT_CONTEXT.md Last Updated stamp still 2026-05-22 despite the 2026-06-01 step 9–21
      rewrite; references "Opus 4.7" as the engine of record.
[L-7] LOW — materials/transferrite-582u-30in.md compatible_cut_vinyls omits 3m-180mc-black and
      3m-180mc-white-24in-50yd (the 24" tape lists all 7; asymmetric).
[L-8] LOW — runSanityChecks() covers 10 of the 11 documented §9 cases — the Convex no_profile case
      is absent from the engine suite (run manually: route no_profile, F17 STOP, output suppressed,
      tiers null — PASSES).
[L-9] LOW — comparableItemsFromData includes the probed item itself when re-running a catalog P/N
      (1278890's comparables list 1278890).
[L-10] LOW — quote_language.rule_14_note / sub_scope_note / ink_unverified_note exist in config but
      generateQuoteStubs never emits them; VALIDATION_PROMPTS §5 expects the Rule-14 note in the
      stub package.
[L-11] LOW — 3017583/84 "$55.02 → quoted $55.00" rounding artifact is documented in-file (fine);
      3017583 margin string "~97%" vs computed 97.6% (~98% in its own table).
```

### INFO

```
[I-1] INFO — Material staleness (S11): Orajet 3951 at 48 days is the oldest (third consecutive
      audit flag). Full table in §5. F2 fires at 180 days (2026-10-19); recommend reverify by
      ~2026-07-21 (90-day cadence per CHAT_CONTEXT's own freshness rule).
[I-2] INFO — Single-points-of-failure: hand-synced build-script constants (no CI tripwire);
      the 13.5" laminator (every printed/lam route + parity boundary depends on it); one-person
      validation pipeline (Nick runs all 24 model passes); the unverified $0.60 Safety-Yellow ink
      lineage baked into 1082570 AND 1068270's filed costs (F12 still fires); the 1082570↔1068270
      lockstep (see M-10).
[I-3] INFO — The "$100 minimum for Sean rush/favor jobs" remains undocumented (backlog item b).
      Decision Fork D5.
[I-4] INFO — do_not_benchmark currency adjudicated: the 8-item list is CORRECT as-is. Nothing from
      Sessions D–G belongs on it (1279000, 3010701, 1068270, 1278890 are band data points /
      inherited data points by design); nothing should be removed (1210810 still pre-acceptance;
      1082570's reason text correctly scopes the exclusion to the initial order).
[I-5] INFO — Deep-tier $/sq-ft curve nuances the "monotonic" claims don't cover: at 200+,
      3010701 (3.202 sq ft) carries $12.18/sq ft vs Band C's $11.87 (smaller item cheaper per
      sq ft — crosses the size-class hierarchy) and vs its own cluster's $8.59; 1082570 at 200+
      is $8.45 vs benchmark $8.49 (−0.5%). All deliberate outcomes of validated tier tables
      (3010701's tight 31.6% compression protects the LRG floor), but "no inversion at any tier"
      is only true band-anchor-to-band-anchor, not item-to-item at deep tiers.
[I-6] INFO — F1 STOP does not suppress output (tiers still render) — verified; this matches
      CALCULATOR.md §3's documented exception. F3/F17/F20 suppression verified live.
[I-7] INFO — W2 partial mitigation: the UI blocks empty width/height before the engine is called;
      the engine-level gap (M-7) matters for programmatic use only.
```

---

## 4. Seeded Findings Adjudication (S1–S15)

| # | Verdict | Evidence summary |
|---|---------|------------------|
| **S1** | **CONFIRMED** (quantified) | See H-5 table. 1278930 filed $2.99 vs canonical $3.56–3.60 (margin overstated ~1.9 pts); 1245130 $5.16 vs $5.93–6.00 (~1.6 pts); 1230820 $3.23 vs ≈$2.53–2.60 (legacy $0.91 waste/setup line confirmed at items/1230820.md:115; margin understated ~3.5 pts); 1082570/1068270 $1.33 vs ≈$0.98–1.05 (legacy $0.60 Safety-Yellow ink; 1068270 reproduces it under a §25 banner via a ~$0.35 buffer). 1210810/1279000/1278890 canonical; one-offs job-based. No sell price changes either way; zero margin-floor crossings under either basis. Decision fork D2. Aggravators found beyond the seed: PRODUCTION.md still declares $2.99/$5.16 "canonical"; the 1278930/1245130 breakdowns don't internally sum. |
| **S2** | **CONFIRMED** | Tape filed as area × $0.5911 on 1205720 ($1.513), 1186310 ($1.516), 3017435 ($1.513), 3018378 ($1.485); true length method gives $0.55/$0.55/$0.72/$0.54 — overstatement 2.75×/2.75×/2.1×/2.75×. True margins restated in M-1. Band C/3010701/3010704 use the true length method (quoted from Nesting sections). Conservative direction throughout. Decision fork D3. |
| **S3** | **CONFIRMED** | Length-derived pseudo-rates: cardinal-red 24" 7.751 (=15.502/2), black 6.5926, white-24-50yd 6.1921, 582U-24" 0.5911. Area-derived: olympic-blue 2.71 (=162.78/60), white-24" 2.19, white-48" 2.15, CR-15" 2.3134 (=433.77/187.5), 582U-30" 0.1891 (=141.86/750). Two semantics in one field name across 11 files. The seed's "nothing consumes cut-vinyl cost_per_sq_ft programmatically" is **REFUTED in one place**: the ENGINE consumes 582U-24's 0.5911 as an area rate for all cut vinyl tape (M-2). Cut-vinyl *color* cost_per_sq_ft is indeed unconsumed (engine uses cost_per_linear_yd). |
| **S4** | **CONFIRMED** | F18/F19 ghost rows at CALCULATOR.md:171–172; engine FLAG_DEFS has 21 flags (F1–F17, F20–F23); §3 header says "All 22". F11 definition-vs-behavior: F11 can never fire (proven by probes — post-enforcement violations always 0; the one skip-enforcement path disables the autofix). Bonus: F16 also unreachable. See H-4. |
| **S5** | **CONFIRMED** | Quantified on 12 routes: briefs 29.4%–45.7% below catalog (table in C-1); 1230820 brief = $11.38 vs $20 catalog vs $15.43/sq ft band floor ($8.78/sq ft actual). F7 + F23×5 on 11/12 standard runs (the sole exception is the micro template, which skips enforcement). Signal-to-noise: zero — flags that fire on every run cannot flag anything. Adjudication and recommendation in Decision Fork D1 (recommend: enforcement becomes report-only for the brief). |
| **S6** | **CONFIRMED** | §3 table has 4 bands; Micro/Band B/Band C/expanded Band A missing; anchors missing 3010704, 3010707, 1279000, 3010701, 1278890; "All 4 current cut vinyl items" stale. Embedded 1230820 tier table verified CORRECT ($30/24/20/17/14/11 = frontmatter). COMPLETION_TEMPLATES trigger existed since 2026-06-01; Sessions B-C-era Band B/C additions, D, E, and G each skipped it (5 Self-Healing violations). Severity rated HIGH (H-3). |
| **S7** | **CONFIRMED** | runSanityChecks contains no 1278890, 1068270, or 3010701 case (and is also missing the documented Convex case — L-8). Probes run this audit: 1278890 → kit, cost-build path (no 2-label template exists), pre-enforcement $30/24/**20**/17/14/11 (lands $20/kit, $10/label — parity path works), post-enforcement $11.38; per-label desync exposed (H-1). 1068270 ↔ 1082570: byte-identical engine output (orientation symmetry holds). 3010701 → cut_vinyl Band A, $31.07 enforced vs $44 catalog (−29.4%), F5+F7+F23×5+F15. |
| **S8** | **CONFIRMED (all six retested)** | W1 **STILL OPEN** (5-label kit → 1 pass; first branch returns 1 whenever wide ≤ 13.5", print-bed logic unreachable; catalog/PRODUCTION say 2). W2 **STILL OPEN** engine-level (0×0×0 → tiny $55, no STOP; UI guards dims only). W3 **STILL OPEN** (kit_same_dim lc=1 → kit, $5.68@20, no flag). W4 **STILL OPEN** (field-by-field diff in M-8). W5 **STILL OPEN and WORSE** (now mislabels all 5 no-override cut vinyl items as Relationship Concession — M-9). W6 **STILL OPEN** (error string, tiers continue, no STOP). |
| **S9** | **CONFIRMED** | Constant 2.0 in script line 56 + config; category says calibrated 0.5–1.3. Used in route_reason text only; single_standard is unbounded above. M-4. |
| **S10** | **CONFIRMED (5 drifts; anchors clean)** | Number-by-number diff in §5. All anchors/templates/ratios/snap/thresholds match. Drifted: calibration_note, "All 4" note, Band A margin-target floor (73 vs 70.9), Band A compression (51 vs 31.6–51), kit margin floor (83 vs 80–83) + missing 2-label template. No CI guard (M-5). Mitigant: per-band margin floors are dead config (engine reads global flag_thresholds only). |
| **S11** | **CONFIRMED** | Orajet 3951 verified 2026-04-22 = 48 days, oldest of 11; third consecutive flag. Full age table §5. Recommend reverify by ~2026-07-21. |
| **S12** | **CONFIRMED** | STRIP_FIELDS = 3 (script lines 32–36) vs the 2026-05-22 log's 7; pricing_logic, material_cost_per_unit, margin_at_qty_20, cost_version_date all ship; sections.notes ships INTERNAL ONLY content (grep-verified in built data.json: 1278890's Jan-2027/$85-hr/breakeven text present). 2026-06-01 I9 declared field exposure by-design; the INTERNAL-ONLY-section exposure goes beyond what I9 reviewed. Deliberate-state question → Decision Fork D4. |
| **S13** | **PARTIALLY CONFIRMED** | No truncation or numeric mangling anywhere (longest value 1468 chars survives intact minus outer quotes; all numeric fields parse exactly). Confirmed artifact: embedded `\"` sequences ship literally in 6 items' pricing_logic/notes/margin fields and render in the UI (L-3). Colons/commas inside values are safe (split limit 1). |
| **S14** | **PARTIALLY CONFIRMED** | Full 23×5 inventory recomputed (§5): every multi-tier item has inversions at ALL five boundaries (85 total); one-offs have none. The three target items: 3010701 — all 5 documented in-file (table) ✓; 1278890 — all 5 documented ✓; 1068270 — cliffs exist (5), file carries only the generic "§26 inherited" note. No *unknown* cliffs (the global §26 principle covers all), but in-file documentation is full on only 3 of 17 multi-tier items and partial (2 of 5) on 1210810 → M-11. |
| **S15** | **CONFIRMED CLEAN at buyer-facing surfaces; exposure confined to deployed data.json** | Quote stubs (all routes probed): only dimensions/sq ft/material/price — no band names, route names, flag IDs, laminator width, multipliers, normalization (3.10 ✓). Briefs/wave prompts include AI-consensus + "Normalization planned January 2027" by design (they go to external AI models — accepted methodology). Every Jan-2027 / breakeven / cycle-time note in items/ARCHITECTURE/MASTER_CONTEXT is flagged INTERNAL ONLY at every occurrence (verified by agents). The one reachable-by-buyer-credentials surface is data.json (M-15/D4). |

---

## 5. Phase Matrices

### 5.1 Phase 1 — 23-Item Matrix

Math ✓ = sq ft, kit sq ft, per-label, and margin all recompute (validate.py tolerance noted in L-1). Band = position at qty 20. Cliffs = recomputed boundary inversions. Doc = §26 in-file documentation (Full/Partial/Generic/n-a).

| P/N | Math | Margin (filed→recomputed) | Band @20 | §25 class | Cliffs | §26 doc | Drift found |
|-----|------|---------------------------|----------|-----------|--------|---------|-------------|
| 1230820 | ✓ | ~84% → 83.9% ✓ | $15.43 anchor ✓ | LEGACY-OVER (+$0.70) | 5 | none | $0.91 waste/setup legacy build; downstream omits 1278890 |
| 1278890 | ✓ | ~88% → 88.0% ✓ | $16.42 exact ✓ | CANONICAL | 5 | **Full (5/5)** | none — gold standard |
| 1278930 | ✓ | ~90% → 90.0% ✓ | $16.42 exact ✓ | LEGACY-UNDER (−$0.57) | 5 | none | breakdown sums $3.23 vs $2.99 claim; downstream omits 1278890 |
| 1245130 | ✓ | ~90% → 89.7% ✓ | $16.42 exact ✓ | LEGACY-UNDER (−$0.77) | 5 | none | breakdown sums $5.31 vs $5.16; "End of current chain" stale |
| 1082570 | ✓ | ~83% → 83.4% ✓ | $15.90 in-band ✓ | LEGACY-OVER (+$0.35) | 5 | generic | $0.60 ink legacy; downstream omits 1068270 (lockstep!); color conflict open |
| 1068270 | ✓ | ~83% → 83.4% ✓ | $15.90 in-band ✓ | LEGACY-OVER (+$0.35) | 5 | generic | claims §25, files legacy $1.33 via ~$0.35 buffer (H-5) |
| 1210810 | ✓ | ~87% → 87.4% ✓ | $16.27 above-band (doc'd exception) | CANONICAL | 5 | Partial (2/5) | $47.50 staleness FIXED (verified) |
| 1279000 | ✓ | ~93% → 93.3% ✓ | $30.86 anchor ✓ | CANONICAL | 5 | **Full (5/5)** | 30.86 vs 30.93 presentation (L-2) |
| 1277970 | ✓ (circle area, doc'd) | N/A (one-off) ✓ 91.3% | excluded (one-off) | JOB-BASED | 0 | n/a | stale "$0.35" body ref (I2, still open) |
| 1277980 | ✓ | N/A ✓ | excluded | JOB-BASED | 0 | n/a | clean |
| 1277990 | ✓ | N/A ✓ | excluded | JOB-BASED | 0 | n/a | clean |
| 1278000 | ✓ | N/A ✓ | excluded | JOB-BASED | 0 | n/a | clean |
| 3017583 | ✓ | ~97% → 97.6% (≈98) | excluded | JOB-BASED | 0 | n/a | stale "$0.28" + "~$1.70" body refs; margin string −1pt |
| 3017584 | ✓ | ~99% → 99.3% ✓ | excluded | JOB-BASED | 0 | n/a | clean |
| 1205720 | ✓ | ~75% → 75.0% (true-tape 77.8%) | $13.67 in-band ✓ | n/a (CV) | 5 | none | tape pseudo-rate; downstream lists only 3017435; sq ft 2.56 vs 2.5638 |
| 1186310 | ✓ | ~75% → 75.0% (77.8%) | $13.65 in-band ✓ | n/a | 5 | none | tape pseudo-rate; 2.564 vs sibling 2.56 rounding |
| 3017435 | ✓ | ~73/78% → 72.8/77.7% ✓ | $13.67 in-band ✓ | n/a | 5 | none | tape pseudo-rate; 200+ 56.8% vs 57% warn (doc'd floor item) |
| 3018378 | ✓ | ~75% → 74.5% ✓ | $13.93 in-band ✓ | n/a | 5 | none | tape pseudo-rate; PMS caveat ✓ |
| 3010701 | ✓ | ~71% → 70.9% ✓ | $13.74 in-band ✓ | n/a | 5 | **Full (5/5)** | length tape ✓; deep-tier curve nuance (I-5) |
| 3010704 | ✓ | ~74% → 74.3% ✓ | $11.03 anchor ✓ | n/a | 5 | none (anchor-ref) | validation-height note documented ✓ |
| 3010707 | ✓ | ~81% → 81.1% ✓ | $20.64 anchor ✓ | n/a | 5 | anchor-ref | clean |
| 3010708 | ✓ | ~84% → 83.7% ✓ | $20.64 ✓ | n/a | 5 | anchor-ref | clean |
| 3010709 | ✓ | ~85% → 84.6% ✓ | $20.64 ✓ | n/a | 5 | anchor-ref | clean |

Tier ladders: all 23 monotonic non-increasing ✓. Compression recomputed: kit family 60.0%×3 ✓; Band A cluster 51.1% ✓; 3010701 31.6% ✓; Band B 50.5% ✓; Band C 58.9% ✓; micro 53.3% ✓; benchmark 63.3% ✓; 1210810 62.1%; 1082570/1068270 74.2% — all match category/ARCHITECTURE claims.

### 5.2 Phase 2 — Six-Band Four-Source Diff

| Band | Category file | ARCHITECTURE | Item math | Config/build script | Verdict |
|------|--------------|--------------|-----------|---------------------|---------|
| Cut vinyl A (1.0–5.0) | $13.65–13.94; margins ~70.9–78%; compression 31.6–51% | same | 13.65/13.67/13.67/13.93/13.74 ✓ | 13.65–13.94 ✓; **margin target 73–78 ✗; compression 51.0 ✗; calibration_note "2.51–2.56" ✗; "All 4 items" ✗** | anchors ✓ / 4 note-level drifts |
| Cut vinyl B (≥5.0) | $11.03; template 105/92/78/68/60/52 | same | 78/7.069=11.034 ✓ | identical ✓ | **clean** |
| Cut vinyl C (<1.0) | $20.64; 28/24/20/16.5/13.5/11.5 | same | 20/0.969=20.64 ✓ | identical ✓ | **clean** |
| P/L singles (≥0.5) | $15.43–15.91; ratios 1.5/1.2/1.0/0.85/0.7/0.55; **profile prose says 1-confirmed/2-data-points** | **"3 confirmed data points"** | 15.43 / 15.90 / 15.90 ✓ | 15.43–15.91 ✓; note omits 1068270; **ceiling 2.0 vs calibrated 1.3 (S9)** | anchors ✓ / internal prose split (M-14) + S9 |
| P/L sub-scope (0.1–0.5) | band-consistent + premium; 1210810 $16.27 above-band documented | same | 4.75/0.292=16.27 ✓ | routed via singles constants (by design) | clean (documented exception) |
| P/L micro (<0.1) | $30.86; ratios 1.5/1.167/1.0/0.867/0.767/0.70; template 4.5/3.5/3.0/2.6/2.3/2.1 | same | 3.00/0.0972=30.86 ✓ (frontmatter-rounded 30.93 — L-2) | identical ✓ | clean (presentation nit) |
| Kit per-label parity | $10.00 / $16.42; ~6% premium; floor "~80–83%" | same | 20/2, 30/3, 50/5 = 10.00 ✓; 16.4204×3 ✓ | 10.00/16.42 ✓; **floor 83.0 ✗; no 2-label template ✗** | anchors ✓ / 2 drifts |

Monotonic curve checks: at qty 20, B→A→C ($11.03 < $13.67 < $20.64) ✓ and singles→sub-scope→micro ($15.43–15.91 < $16.27 < $30.86) ✓. Verified per-tier band-anchor-to-band-anchor ✓ at all 6 tiers; item-level deep-tier crossings documented in I-5. Band isolation: no cross-band data leaks found in category math, config constants, or engine routing (each band's tiers derive solely from its own anchor/template — code-verified). Kit three-way parity: exact at every metric; per-label material band ~$1.00–$1.20 holds ($1.20 / $0.997 / $1.032).

### 5.3 Phase 3 — Engine Regression + Probe Matrix (all live runs)

§9 documented cases (11) vs actual:

| Case | §9 expects | Actual | Verdict |
|------|-----------|--------|---------|
| 1230820 | ~$11.38, F23×5+F7 | $11.38, F7+F23×5 | ✓ |
| 1082570 | ~$4.39, F8/F23×5/F7/F12 | $4.39, F8+F7+F23×5+F12 | ✓ |
| 1210810 | ~$2.58, F10/F8/F22/F23×5/F7/F12 | $2.58, exact | ✓ |
| 1278930 | ~$18.64, F23×5+F7 | $18.64, exact | ✓ |
| 1245130 | ~$31.07 | $31.07, exact | ✓ |
| 1205720 | ~$22.78, F15/F23×5/F7/F5 | $22.78, exact | ✓ |
| 1277970 | $55 flat, F9 | $55×6, F9 | ✓ |
| Convex 10×6 | no_profile, F17 STOP, suppressed | no_profile, F17 STOP, tiers null | ✓ (but case absent from runSanityChecks — L-8) |
| 3010704 | ~$53.85, F15/F23×5/F7/F5 | $53.85, exact | ✓ |
| 3010707 | ~$11.89, F15/F23×5/F7 | $11.89, exact | ✓ |
| PROD-OVERRIDE 8×1.75 | ~$3.00, "F10, F8, F23 (fewer)" | $3.00 template-direct, **F10+F8 only, F23×0**; 5 cliffs recorded informationally | ✗ doc wrong (H-4) — template HAS 5 cliffs; F23 can't fire on skip path |

New probes (S7): 1278890 → kit/cost-build, pre-enforcement $20/kit ($10/label parity ✓), enforced $11.38, per-label desync (H-1) | 1068270 ≡ 1082570 outputs ✓ | 3010701 → Band A, $31.07 enforced.

Boundary truth table (engine = docs at every edge): 0.099→tiny; **0.1→tiny (≤)**; 0.101→sub_scope; 0.499→sub_scope; **0.5→sub_scope (≤)**; 0.501→single_standard; override at 0.0999/0.1 → sub_scope(micro); 0.1001+override → sub_scope via NORMAL path (singles tiers — micro unreachable above 0.1: **dead zone 0.1–0.126 confirmed**, window 0.068–0.126 truncated by the route gate). Cut vinyl: 0.999→C; **1.0→A (inclusive)**; 4.999→A; **5.0→B (inclusive)**.

Micro band: 0.097 → template-direct (catalog table verbatim, enforcement skipped, 5 cliffs surfaced informationally, stub $3.00 ✓). 0.05 → algorithmic $1.03@20 — **violates documented sub-0.06 per-label floor** (M-6). Micro band deleted from config → defensive fallback to singles path, $0.76@20, no crash ✓.

Enforcement internals (3.4): penny-rounding present in both functions (engine lines ~3490, ~3521); bottom-up cascade verified via F23 detail text (e.g. 1230820: 199×$14.00=$2786.00 > 200×$11.00=$2200.00 → cap $11.05; then 99×$17=…); floor-cap to the cent (2200/199=11.0552→11.05) ✓; checkInvoiceProtection = 0 violations on all 11 enforced runs ✓; skips tiny/no_profile ✓; F23 once per capped boundary ✓ (5×11 runs + 0 on micro/tiny/no_profile).

Flag audit (3.9): F1/F2 staleness day-math verified by simulation (220d → F2 "(220 days since verification)"; >365d → F1 STOP, output NOT suppressed — matches doc) ✓. F13 fires on olympic_blue (pms_note) ✓, not on others ✓. F14 fires on white_24in (48" alt exists), not white_48in ✓. F3 STOP at narrow 14" ✓ (suppressed). F20: requires narrow ≤13.5 < wide AND overflow of both orientations — 7-label 11.13×7.88 returns 1 pass (first branch), F20 not reachable for any same-dim kit whose wide ≤13.5. F9 on tiny ✓. F17 ✓. **F11 and F16 unreachable (H-4)**. F18/F19 absent from engine ✓ (ghost-doc only).

Stub leakage (3.10): stubs across all routes contain only dims/sq ft/material/price (+PMS caveat, +tiny program line). No internal vocabulary. Risk is the *price value* itself post-cascade (C-1), not vocabulary.

`effectivePriceTiers` / kit handling (3.11): C1 fix intact — `tiers: kit_totals` present; summary stat cards, pricing table, band positioning, margins all consume enforced kit totals ✓; the one stale consumer is `per_label_tiers` (H-1).

### 5.4 Material Age Table (as of 2026-06-09) — S11

| Material | verified_date | Age (days) |
|----------|---------------|-----------|
| orajet-3951-white | 2026-04-22 | **48 — oldest, 3rd consecutive flag** |
| 3m-180mc-white-24in | 2026-05-21 | 19 |
| 3m-180mc-white-48in | 2026-05-21 | 19 |
| 3m-180mc-olympic-blue | 2026-05-22 | 18 |
| 3m-180mc-cardinal-red | 2026-05-28 | 12 |
| transferrite-582u | 2026-05-28 | 12 |
| 1mil-polyester-overlaminate | 2026-05-28 | 12 |
| 3m-180mc-black | 2026-06-05 | 4 |
| 3m-180mc-white-24in-50yd | 2026-06-05 | 4 |
| 3m-180mc-cardinal-red-15in | 2026-06-05 | 4 |
| transferrite-582u-30in | 2026-06-05 | 4 |

All within the 180-day F2 threshold. Orajet recommendation: reverify by **2026-07-21** (90-day CHAT_CONTEXT freshness rule; F2 not until 2026-10-19).

### 5.5 §26 Cliff Inventory (recomputed)

Every multi-tier item (17) has inversions at **all 5 boundaries** — 85 total, largest single inversion $1,540 (3010704 at 199/200: 199×$60=$11,940 vs 200×$52=$10,400). One-offs (6) have none (flat tables). Spot examples: 1210810 9/10 $65.25 vs $57.50 (Δ$7.75) and 19/20 $109.25 vs $95.00 (Δ$14.25) — match the documented figures exactly; 1278890's in-file table matches recomputation at all 5. In-file documentation coverage: Full 3 / Partial 1 / Generic-or-none 13 (M-11). No inversion exists that §26's blanket principle does not cover.

### 5.6 §25 Compliance Inventory

See H-5 table (S1). Classes: CANONICAL ×3 (1210810, 1278890, 1279000), LEGACY-OVERSTATED ×3 (1230820, 1082570, 1068270), LEGACY-UNDERSTATED ×2 (1278930, 1245130), JOB-BASED ×6 (one-offs). Margin-floor sweep (every item × every tier, filed AND canonical): **zero tiers cross the 50% stop under either basis; zero classification divergences between bases**; sole warn-level touch: 3017435 200+ at 56.8% filed vs the 57% cut-vinyl warn line (documented band-floor item; clears to 64.5% under true-tape costing).

### 5.7 January-2027 Normalization Exposure Map (S15 / Phase 6.3)

| Surface | Current anchor | Normalization target | Argument basis | What Sean has locked | Internal-only flagged? |
|---------|---------------|---------------------|----------------|---------------------|----------------------|
| Cut vinyl Band A cluster (1205720/1186310/3017435/3018378, $35) | $13.65–13.94/sq ft | AI consensus $14.84–16.41 (~9%) | relationship-phase transition | $13.67–13.74/sq ft pattern-matched; Wave 3: logs $13.74 as permanent | ✓ category override note, MASTER_CONTEXT Internal Pricing Notes, ARCHITECTURE |
| 3010701 ($44) | $13.74/sq ft | ~$48 (~9% uplift) | moves with Band A | $13.74 logged permanent; expects ~4.0 sq ft at $54–56 | ✓ item INTERNAL ONLY + ARCHITECTURE + category |
| Kit family 200+ floor (1278890/1278930/1245130) | $6.00/label at 200+ | material-cost / process-complexity arguments ONLY (rate arguments dead) | $85/hr × 7.5–8.5 min/kit near-breakeven (structural) | THREE accepted data points at $10.00/label; $6.00 floor "hardest number to move" | ✓ item + ARCHITECTURE + STATE, all flagged |
| Singles band concession | $15.43–15.91/sq ft | industry ~$18–22 (MASTER_CONTEXT note) | technical-partnership status | $15.43/$15.91 + $16.27 sub-scope premium logged | ✓ MASTER_CONTEXT Internal Pricing Notes; 1210810 internal note |
| Cycle-time anchors | n/a | first 200+ runs on kit family = operational evidence | documented tracking instruction | n/a | ✓ 1278890 + ARCHITECTURE, flagged |
| Bands B / C / micro | $11.03 / $20.64 / $30.86 | exempt (survive normalization; C premium compresses 51%→26–39%) | n/a | founding anchors logged by Wave-3 sims | ✓ |

**Reachability:** absent from quote stubs ✓; present in wave briefs by design (external AI models — accepted); present in deployed data.json behind one password (M-15 / D4).

---

## 6. Working Well (do not churn)

1. **Catalog arithmetic** — 23/23 perfect recomputation across every frontmatter field; monotonic ladders everywhere.
2. **Kit-family triangulation** — $10.00/label, $16.4204/sq ft, 60.0% compression, identical §26 behavior across 2/3/5-label members; the strategic asset is mathematically real.
3. **Band-anchor synchronization** — every anchor and tier template identical across category ↔ ARCHITECTURE ↔ item math ↔ config.
4. **enforceTierBoundaries / checkInvoiceProtection mathematics** — cascade, penny-precision, F23 detail math: all verified correct (the *design question* is D1; the *code* is right).
5. **Routing boundary semantics** — every probed edge matches the documented ≤/< conventions, including the production-override gating and the band-threshold inclusivity.
6. **Orientation symmetry** — flipped W/H produces identical engine output (1068270 ≡ 1082570).
7. **The C1 kit fix is intact** — kit_totals drive summary, table, margins, and band math.
8. **Micro-band template-direct + skip-enforcement** — the one place the engine preserves a Nick-locked table verbatim works exactly as intended ($3.00 with cliffs surfaced informationally).
9. **do_not_benchmark fence** — correct 8-item list, enforced in engine comparables, redundantly fenced in VALIDATION_PROMPTS Rule 10 and in the item files themselves.
10. **One-off item hygiene** — exhaustive DO-NOT-BENCHMARK warnings, job-economics framing, circle-area geometry documented, reorder-repricing instructions in place.
11. **1278890 as the item-file gold standard** — §25 build shown, §26 table complete, INTERNAL ONLY section properly fenced; use it as the template for backfills.
12. **Material file discipline** — bidirectional used_in_items verified 11/11; derivation-method notes present; costs traceable to invoices.
13. **validate.py + CI rebuild loop** — catches registry/category/count drift; ran 0/0 before and after this audit; the auto-rebuild commit loop works.
14. **Internal-only segregation at buyer-facing surfaces** — stubs are clean; every normalization note found is explicitly flagged at every occurrence.

---

## 7. Prioritized Fix Plan (proposed sessions)

| # | Session | Scope | Files | Effort | Depends on |
|---|---------|-------|-------|--------|-----------|
| 1 | **Calculator brief integrity** (C-1, H-1, H-2, parts of M-6/M-7) | Implement D1 outcome; rebuild/derive per-label after enforcement; one price story per brief; READY badge reflects cascade/F7 state; stub sources band/template price; ink select → full_bleed default; input-sanity STOPs; micro floor clamp | frontend/index.html, governance/CALCULATOR.md §9 | M | **D1** |
| 2 | **Governance truth pass** (H-3, H-4, M-13, L-5, L-6) | VALIDATION_PROMPTS §3 full band/anchor rebuild + §5 MOQ phrase; CALCULATOR.md F18/F19 removal, count fix, §6.3 rewrite, Rule 11 skip_enforcement note, §9 PROD-OVERRIDE row, §1/§7 MOQ residue; SPEC_EXTRACTION ink default; MASTER_CONTEXT file map (audits/); CHAT_CONTEXT stamp | 5 governance/.claude docs | M | none — can run immediately |
| 3 | **Costing-truth normalization** (H-5, M-1, M-2) | Execute D2 + D3: rebuild or grandfather the 5 legacy costs; fix PRODUCTION.md "canonical" sentence + non-summing kit breakdowns; harmonize cluster tape method; align engine tape computation | 5 item files, PRODUCTION.md, categories, ARCHITECTURE margins, index.html (tape) | M | **D2, D3** |
| 4 | **Cross-reference & prose hygiene** (M-10, M-11, M-12, M-14, L-1, L-2, L-7, L-11) | downstream chains + lockstep notes; §26 table backfill (1278890 pattern); I2-family prose fixes; category internal contradictions; rounding harmonization | ~14 item files, 2 categories | M (mechanical) | none |
| 5 | **Pipeline hardening** (M-3, M-4, M-5, L-3) | Sync 5 drifted config constants (+2-label template per D1); ceiling → calibrated value; CI: validate.py gate + categories/governance triggers + optional drift-assert; parser escape handling (or real YAML lib) | build_calculator_config.py, workflow, build scripts | S–M | D1 (template only) |
| 6 | **Engine robustness round** (M-7 remainder, M-8, M-9, L-8, L-9, L-10) | W4 brief completeness; override_type from data (per D4 scope); W1 lam-pass rule (needs Nick's production decision); runSanityChecks: add Convex + 1278890 + 1068270 + 3010701 cases; comparables self-exclusion | index.html, build_frontend.py | M | **D4, D6** |
| 7 | **Exposure decision** (M-15) | Execute D4: strip INTERNAL ONLY sections (and chosen fields) from data.json, or codify by-design state | build_frontend.py, CALCULATOR.md §8 | S | **D4** |

Sessions 2 and 4 are safe to run before any fork is resolved. Session 1 is the highest-value blocked item.

---

## 8. Decision Forks for Nick

| ID | Fork | Options | Recommendation (one sentence) |
|----|------|---------|-------------------------------|
| **D1** | Cascade design (backlog item d — forced to verdict) | (a) keep strict cascade; (b) enforce only the customer-facing 10-19→20-49 boundary; (c) re-tune upper-tier ratios so templates don't self-cliff; (d) make enforcement **report-only** (flags, no tier mutation) | **(d)** — every Nick-locked catalog table keeps intentional cliffs resolved by §26 at billing, so a brief generator that *rewrites* tiers can never agree with the system it feeds; report-only restores band-anchored briefs ($20, not $11.38), kills the F7/F23 alarm saturation, and erases H-1 as a side effect. |
| **D2** | S1 costing eras | (a) rebuild 1230820/1278930/1245130/1082570/1068270 costs to §25 (documentation-only); (b) formally grandfather with an explicit §25 exemption note | **(a)** — §25 itself says "past, present, and future," the kit family's margin story currently inverts under canonical costing, and the rebuild changes zero sell prices. |
| **D3** | S2 tape convention | (a) harmonize the 4 cluster items to the length method (documentation-only, margins +2.3–2.8 pts); (b) declare the area×0.5911 pseudo-rate a deliberate conservative convention | **(a)** — five newer items and PRODUCTION.md's own derivation notes already treat length as truth; one convention, one math. |
| **D4** | data.json exposure (S12) | (a) accept by-design and document it (fix the STRIP_FIELDS comment); (b) strip INTERNAL ONLY note sections only; (c) strip notes + pricing_logic + margins + material costs (restore the 2026-05-22 posture) and re-expose override_type internally for M-9 | **(b) minimum, (c) preferred** — the Jan-2027 playbook and breakeven math are the only contents whose leak is unrecoverable; everything else is arguably useful to Nick in the UI. |
| **D5** | $100 rush/favor minimum (backlog b) | (a) codify as a one-line pricing rule (new §27); (b) declare intentionally informal in PROGRESS | **(a)** — it's the only price Sean has actually *heard* that the repo can't see; one sentence ends the risk. |
| **D6** | W1 lam-pass model | (a) teach the engine the print-bed/orientation choice (needs your production rule for when mixed orientation is chosen); (b) keep geometric model and label lam_passes "advisory — confirm against PRODUCTION.md" in the brief | **(b) now, (a) when the rule is articulable** — the 5-label kit's 2-pass reality was a production choice, not pure geometry, and guessing it in code invites quiet wrongness. |
| **D7** | 1082570/1068270 ink lineage | (a) on Sean's color selection, re-cost BOTH items in lockstep (ties into D2); (b) leave until reorder | **(a)** — the F12 placeholder and the parity-lockstep rule both point at the same single edit; do it once, together. |

---

## Session-end state (audit integrity)

- `python scripts/validate.py` at session end: **PASS — 0 errors, 0 warnings** (23 items).
- Regenerated frontend JSONs reverted via `git checkout -- frontend/data.json frontend/materials.json frontend/calculator_config.json` (build scripts were run for verification only).
- `git status` at commit time shows ONLY: `audits/2026-06-09-full-system-audit.md` (new), `.claude/PROGRESS.md`, `.claude/STATE.yml`. Stated per acceptance criteria and verified before commit.
- No file in `items/`, `categories/`, `governance/`, `materials/`, `scripts/`, `frontend/`, or `.github/` was modified.
