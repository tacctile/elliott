# Calculator — Governance Reference

> **Authoritative reference for the Elliott calculator system.**
> The HTML calculator at `frontend/index.html` is the implementation; this document is the contract.
>
> Last Updated: 2026-07-16 (**F28 application tape width resolution** — P/N 3023921 exposed a structural gap: cut-vinyl tape selection was hardcoded to the 24" TransferRite 582U material regardless of label size, and any deviation depended on a pre-built Combinations row existing for that exact vinyl-color x tape-width pairing. A label needing a wider tape than its color's existing combination produced $undefined/yd -> $NaN material cost instead of a clear error. Fixed: `computeCutVinylMaterial` now calls new `resolveApplicationTape()`, which picks the NARROWEST application tape roll on file (`application_tape_rolls`, new derived config list, sourced from every tape material on file independent of vinyl color) whose `roll_width_in` is >= the label's narrow (across-roll) dimension. A saved Combination's own tape choice (or an inline per-quote override) still takes precedence when supplied. New STOP flag **F28** fires when nothing on file is wide enough (flag count 25->26; F1-F17, F20-F28). `runSanityChecks()` gains 2 new cases (21->23). See `governance/PRICING_RULES.md` §33. No item file touched, no locked price changed — a companion audit of every existing cut-vinyl item's documented label width against its documented tape roll width found zero mismatches (P/N 3010704's 15"/30" pairing confirmed deliberate: 2-up nesting efficiency, not a fallback of this gap). Previously 2026-07-16 (F27 nearest-neighbor chain-consistency — **live engine implementation**, following up the same-day governance-spec-only addition below. `frontend/index.html` gains `findNearestLargerChainNeighbor()` + `checkChainConsistency()`, called from `runCalculator()` immediately after tier-build for the `single_standard`, `single_sub_scope`, and `cut_vinyl` routes (kits, `no_profile`, and `invalid_input` are structurally out of scope — kits carry an intentional per-sq-ft premium per the "Per-Sq-Ft Kit Premium" note in `governance/PRICING_RULES.md`). For each new item, the engine finds its nearest LARGER validated same-family neighbor by sq ft and checks the new item's $/sq ft against that neighbor's at all six tiers (Direction B, per §32), firing **F27** (REVIEW) only where closing the gap needs ≥2 $0.25 increments on the new item's own price. New `chain_consistency` config block (`calculator_config.json`, seeded by new `CHAIN_CONSISTENCY_*` constants in `scripts/build_calculator_config.py`): `excluded_pn` (25 curated direct-parity/owner-judgment/floor-governed-clone/one-off-job-economics P/Ns — a *different* exclusion set than `do_not_benchmark`, since e.g. 1210810/1082570 are do-not-benchmark for band-data-point reasons but remain valid §32 comparables), `permanent_exceptions` (1230820, 1205720), `tolerance_increments` (2), `increment_size` (0.25), and `tested_range` per family (Orajet 0.019–1.296 sq ft, cut vinyl 0.969–7.069 sq ft, per the audit's §7 scope limits). Items below the F26 per-label-floor threshold are excluded from the neighbor pool *structurally* (any candidate under `per_label_floor_threshold_sq_ft` that isn't one of the two governing floor comparables), so a future F26-routed item is automatically exempt without a rule update, matching §32's "Categorical exception" language. **Permanent exceptions apply in both directions**, not just as a neighbor target: re-running the calculator against 1230820's or 1205720's own dimensions never fires F27 against it either — this is a deliberate reading of the fuller audit (§13.3 keeps 1205720 in the permanent/structural exception group despite being the smaller side of a real, documented gap against 1146650; §16.1 removes both roots from the chain entirely before simulating), broader than a literal one-line restatement of the rule would suggest. When no validated neighbor exists inside the family's tested range, the engine reports a distinct `chain_consistency.status: 'gap'` (data-coverage gap) rather than firing F27 — the two are never conflated. §3 flag table: **F27** now **live** (flag count of engine-implemented flags 24→25; F1–F17, F20–F27). A new "Chain Consistency (§32)" section appears in the validation brief text (always present for applicable routes — `ok`/`gap`/`exempt_permanent`/`violation`) and in the Band Positioning UI panel. `runSanityChecks()` gains 5 new cases (16→21 — correcting the prior entry's "17" claim below, which never matched the implemented suite: case 7's `1277970` tiny-route case was retired under §28 and removed from the code without the count being corrected at the time). `python scripts/validate.py` re-run clean (0 errors, 0 warnings) — unaffected, as expected, since no `items/` file was touched. **No item file touched, no locked price changed, and the audit's illustrative 38-cell fix set was NOT applied to any item** — same out-of-scope boundary as the spec-only session below; turning any of the audit's findings (1101250, 3024595, 3017572, or any other flagged pair) into an actual price change remains separate, Nick-directed work. Previously 2026-07-16 (nearest-neighbor chain-consistency rule — `governance/PRICING_RULES.md` §32 added, sourced from `audits/2026-07-16-deep-tier-chain-consistency.md`, a full nearest-neighbor $/sq ft audit across all independently-validated Orajet and cut-vinyl single-label items at all six tiers. §3 flag table: new flag **F27** added (REVIEW) for future items whose $/sq ft violates the §32 chain-consistency constraint beyond its 2-increment tolerance; flag count 24→25. **Documentation only — no engine change in that session:** F27 was defined there as governance spec only, before the live engine session above. No item file touched and no locked price changed; the audit's illustrative 38-cell fix set was intentionally not applied to any item.) Previously 2026-07-15 (governance drift remediation — audits/2026-07-15-governance-drift-audit.md: three live-risk gaps fixed in the engine. (1) §31 sub-scope root floor — `buildPrintLamSinglesTiers` now clamps any tier of a `single_sub_scope` item that would price below $15.43/sq ft, and every deeper tier, flat to the cheapest $0.25 increment clearing the floor (new `sub_scope_root_floor_psf` constant); previously no floor check existed and the algorithmic output could — and did — recommend below-floor deep tiers. (2) Per-label floor doctrine — `buildPrintLamMicroTiers` now refuses to compute the linear $30.86/sq ft formula below 0.06 sq ft (new `per_label_floor_threshold_sq_ft` constant) and fires a new STOP flag, **F26**, naming the two governing comparables (P/N 3024592 ANSI, P/N 3024140 non-ANSI) instead of emitting a silent wrong number; confirmed live on P/N 1205870, whose own brief had been silently computing $1.50 against a correct $2.50. (3) Cut vinyl tape costing — `computeCutVinylForRollWidth`/`computeCutVinylMaterial` now cost tape length-based (`(label length + 6" spacing) ÷ labels per row × $/linear yd`, new `cut_vinyl_row_spacing_in` constant), matching `categories/cut-vinyl-3m-180mc.md`'s 2026-06-09 method note; previously tape used the deprecated `sq_ft × $0.5911/sq ft` pseudo-rate (vinyl costing was already correct and untouched). §3 flag table: F9 description corrected (was stale — described pre-§28 REVIEW behavior; engine has it retired/INFO); F26 added; flag count 23→24. §2/§6.3/§9 updated to match; `runSanityChecks()` raised from 14 to 17 cases. `scripts/build_calculator_config.py` updated to source the new constants (plus `cost_per_linear_yd` now read dynamically for all tape/laminate materials, not just cut-vinyl colors). No item files touched — this was an engine/tooling fix only, not a pricing change to any filed item. Previously 2026-06-29 — ANSI hardcoded at account level (§29): ANSI checkbox removed from calculator UI; ANSI = true is fixed for all Orajet/lam items; validation brief now shows "ANSI: Yes — account rule (all Orajet/lam items)" as a fixed statement. Previously 2026-06-22 — $55 floor removed from routing framing and account rule description; no-floor job-economics doctrine applied throughout; deep-tier standing instruction added to VALIDATION_PROMPTS.md §3. Previously 2026-06-09 Session I — §7 Step 9: §27 $50 rush/favor floor reference added. Previously Session H — audit C-1/H-1/H-2/H-4/H-5 + W1–W6 remediation: tier-boundary enforcement is now REPORT-ONLY (briefs are band-anchored; F23 reports cliffs, §26 resolves at billing, tables are never mutated); ink coverage is full-bleed-only per §25 (dropdown removed); kit material costing uses the §25 canonical formula (legacy $2.99/$5.16 hardcodes removed); F18/F19 ghost rows deleted and the flag table corrected (23 definitions, F24/F25 added, F11/F12/F16 documented unreachable); §6.3 regression checklist rewritten to current truth; singles routing ceiling corrected to 1.5 sq ft; data source is Supabase-first with static-JSON fallback; the material-family/color dropdowns are replaced by the material-combination selector)

---

## 1. What the Calculator Is — and Is Not

The Calculator is a **first-round pricing brief generator**. Given dimensions, material family, item type, ink coverage, color (cut vinyl), and order quantity, it produces:

- A routing decision and reason
- A full 6-tier price ladder with margins
- Material cost breakdown
- Band positioning
- Lamination-pass and laminator-fit derivation
- A list of comparable items (filtered by `do_not_benchmark`)
- A flag set (STOP / REVIEW / INFO)
- A plain-text **validation brief** ready to paste into a 4-round AI validation prompt

**The Calculator IS:**

- A deterministic pricing brief generator that reads **Supabase first** (`elliott_pricing_bands`, `elliott_account_settings`, `elliott_materials`, `elliott_material_combinations`, `elliott_items`) and falls back to the static JSONs (`calculator_config.json`, `data.json`, `materials.json`, `combinations.json`) with a visible offline banner when Supabase is unreachable
- The input to **Round 1** of the `governance/PRICING_VALIDATION.md` 4-round AI validation process — its tier tables are **band-anchored** (report-only enforcement since Session H; the pre-Session-H cascade that compressed briefs 29–46% below catalog is retired)
- A consistency tool — re-running the same inputs always produces the same output
- A self-auditing surface — flags surface staleness, scope violations, missing profiles, margin floor breaches, boundary cliffs (with their §26 resolution), and invalid inputs

**The Calculator is NOT:**

- A quote tool. The calculator produces a brief; Nick produces the quote.
- A replacement for AI validation. It produces the Round 1 starting point, not a final price.
- A file writer. The calculator never writes to `items/`, `categories/`, or any governance file. Claude Code writes files after the 4-round validation is complete and Nick has locked the price.
- A buyer-facing artifact. The brief is internal — never paste raw calculator output to Sean or any buyer.
- A precedent setter. A calculator output is not a price until it survives the 4 rounds.

---

## 2. Routing Decision Tree (Canonical)

Every input is dispatched to exactly one route. The route determines which band, which tier template, which flags are eligible, and what the output structure looks like.

```
                    ┌──────────────────────────────────────┐
                    │   inputs: material_family,           │
                    │   width_in, height_in, item_type,    │
                    │   label_count, order_qty, ...        │
                    └──────────────────┬───────────────────┘
                                       │
                          sq_ft = (width × height) / 144
                                       │
                       ┌───────────────┴───────────────┐
                       │                               │
              material_family =                 material_family =
              "3M 180mC Cut Vinyl"            "Orajet 3951 Cast +
                       │                       Polyester Lam"
                       │                               │
                       ▼                               │
              ┌────────────────┐                       │
              │ route =        │                       │
              │   cut_vinyl    │              not Orajet or 180mC?
              └────────────────┘                       │
                                                       ▼
                                              ┌────────────────┐
                                              │ route =        │
                                              │   no_profile   │
                                              │ (STOP — F17)   │
                                              └────────────────┘

      (Orajet 3951 path continues)
                       │
              sq_ft ≤ 0.1?
                       │
              ┌────────┴────────┐
              │                 │
             yes                no
              │                 │
              ▼                 │
      ┌──────────────┐          │
      │ route =      │          │
      │   tiny       │          │
      │ (no floor)   │          │
      └──────────────┘          │
                                │
                       label_count > 1
                       OR item_type =
                       "Printed/Laminated Kit"?
                                │
                       ┌────────┴────────┐
                       │                 │
                      yes                no
                       │                 │
                       ▼                 │
              ┌────────────────┐         │
              │ route =        │         │
              │   kit          │         │
              └────────────────┘         │
                                         │
                                sq_ft ≤ 0.5?
                                         │
                                ┌────────┴────────┐
                                │                 │
                               yes                no
                                │                 │
                                ▼                 ▼
                       ┌────────────────┐  ┌──────────────────┐
                       │ route =        │  │ route =          │
                       │ single_sub_    │  │ single_standard  │
                       │   scope        │  │                  │
                       └────────────────┘  └──────────────────┘
```

### Route Definitions

| Route | Material Family | Sq Ft | Item Type | Band Applied | Floor Logic |
|-------|-----------------|-------|-----------|--------------|-------------|
| `cut_vinyl` | 3M 180mC Cut Vinyl | any | any | Cut Vinyl Lettering — size-class routed: sq ft ≥ 5.0 → Band B (Large-Format, $11.03/sq ft anchor, 3010704 founding); 1.0 ≤ sq ft < 5.0 → Band A (Small-Format, concession_phase, $13.65–$13.94/sq ft); sq ft < 1.0 → Band C (Sub-1 sq ft, $20.64/sq ft anchor, 3010707 founding cluster) | No MOQ. Invoice protection (§26) applies at all tier boundaries. |
| `tiny` | Orajet 3951 | ≤ 0.1 sq ft | any | None | Elliott sub-0.1 sq ft: production catalog items route to the Micro-Format Band (set `production_override: true` → `single_sub_scope`); one-off field service requests price from material footprint and production time with no floor. |
| `kit` | Orajet 3951 | > 0.1 sq ft | label_count > 1 OR `Printed/Laminated Kit` | Printed/Laminated Kits | No MOQ. Invoice protection (§26) applies at all tier boundaries. |
| `single_sub_scope` | Orajet 3951 | 0.1–0.5 sq ft *(standard route)* OR ≤ 0.1 sq ft *(via production-override path)* | single | Printed/Laminated Singles (band-consistent, item excluded from band DATA POINTS) for 0.1–0.5 sq ft. **Sub-0.1 sq ft Micro-Format Band ($30.86/sq ft anchor, 1279000 founding data point)** when `production_override: true` is set on a sub-0.1 sq ft Orajet 3951 single — uses the validated tier template directly when the item's sq ft is within ±30% of the founding anchor sq ft (0.097). | No MOQ. Invoice protection (§26) applies at all tier boundaries. **§31 sub-scope root floor (governance drift remediation, 2026-07-15):** for 0.1–0.5 sq ft items (`buildPrintLamSinglesTiers`), no tier at any quantity may price below $15.43/sq ft (P/N 1230820). Where a raw ratio-scaled tier would fall below the floor, that tier and every deeper (higher-quantity) tier is clamped flat to the cheapest $0.25-increment price that clears the floor — `sub_scope_floor_applied`/`sub_scope_floor_price` on the tier-build result, surfaced in the brief via `template_source`. Does NOT apply to `single_standard`. **Per-label floor (below ~0.06 sq ft, via `buildPrintLamMicroTiers`):** the linear $30.86/sq ft formula is not applied — F26 STOPs instead (see §3). |
| `single_standard` | Orajet 3951 | > 0.5 sq ft | single | Printed/Laminated Singles | No MOQ. Invoice protection (§26) applies at all tier boundaries. |
| `no_profile` | Convex High Bond, Lexan/Polycarbonate, or any other | any | any | None | STOP — F17 fires, output suppressed, Required Inputs checklist shown |

### Routing guards (Session H)

- **W2 input sanity:** width ≤ 0, height ≤ 0, or label_count < 1 → route `invalid_input`, F24 STOP, output suppressed. Both the UI form and the engine enforce this (programmatic callers cannot bypass it).
- **W3 one-label "kit":** a kit item type with `label_count = 1` is re-routed to the single path (sub-scope/standard/tiny by sq ft) and F21 REVIEW fires — a 1-label kit is a single label; verify the intended label count.

### Sq Ft Thresholds (from `routing` — Supabase `elliott_account_settings.routing_thresholds`, mirrored in `calculator_config.json`)

- `tiny_threshold_sq_ft`: **0.1** (≤ this → `tiny`)
- `sub_scope_floor_sq_ft`: **0.1**
- `sub_scope_ceiling_sq_ft`: **0.5** (0.1–0.5 → `single_sub_scope`)
- `singles_band_floor_sq_ft`: **0.5** (used in the band-scope F8 proximity flag)
- `singles_band_ceiling_sq_ft`: **1.5** — a ROUTING THRESHOLD, not the band's calibrated range. The singles band is CALIBRATED on data points at 0.503–1.296 sq ft; 1.5 covers them plus a safe buffer. Items above 1.5 sq ft still route `single_standard` (the route is unbounded above) but are NOT band-confirmed without 4-wave validation. (Was 2.0 until 2026-06-09 — audit H-5/M-4: the old value overstated calibrated coverage.)
- `laminator_max_width_in`: **13.5** (narrow dim > 13.5 → F3 STOP)
- `roland_max_print_width_in`: **28.0**
- `parity_max_lam_passes`: **2** (kit lam passes > 2 → F16 REVIEW)
- `cut_vinyl_band_thresholds.band_b_floor_sq_ft`: **5.0** (sq ft ≥ this → Band B Large-Format)
- `cut_vinyl_band_thresholds.band_c_ceiling_sq_ft`: **1.0** (sq ft < this → Band C Sub-1 sq ft)
- `bands.printed_laminated_micro.threshold_sq_ft`: **0.1** (sq ft ≤ this AND production override → Micro-Format Band, $30.86/sq ft anchor, 1279000 founding data point)
- `bands.printed_laminated_micro.anchor_sq_ft`: **0.097** (founding anchor; templates used directly when item sq ft is within ±30% of this value)
- `sub_scope_root_floor_psf`: **15.43** (governance drift remediation, 2026-07-15 — governance/PRICING_RULES.md §31: hard floor at every tier of a `single_sub_scope` item, not just qty 20. Same value as `bands.printed_laminated_singles.anchor_psf` — both trace to P/N 1230820.)
- `cut_vinyl_row_spacing_in`: **6** (governance drift remediation, 2026-07-15 — feed-length row-spacing allowance added to the label's wide dimension for cut-vinyl **tape** costing only; length-based per categories/cut-vinyl-3m-180mc.md 2026-06-09 method note. Vinyl feed length does not add this spacing.)
- `bands.printed_laminated_micro.per_label_floor_threshold_sq_ft`: **0.06** (governance drift remediation, 2026-07-15 — below this, `buildPrintLamMicroTiers` refuses the linear formula and fires F26 STOP instead; see §3.)

---

## 3. Flag Definitions (Canonical)

**26** of the flag definitions below live in `frontend/index.html` (calculator engine `FLAG_DEFS`): **F1–F17 and F20–F28**. F18 and F19 (MOQ-era flags) were removed from the engine in Session B (2026-06-05) when MOQ was purged from the account; their rows were deleted from this table in Session H (they had survived here as ghost documentation — audit H-2/H-4). F26 was added in the 2026-07-15 governance drift remediation session (see below). F27 was added as governance spec alongside `governance/PRICING_RULES.md` §32 and wired into the live engine (`checkChainConsistency()`/`findNearestLargerChainNeighbor()`) both on 2026-07-16 (see the Last Updated header). F28 was added the same day alongside `governance/PRICING_RULES.md` §33 (application tape width resolution — see the Last Updated header). Four defined flags are currently **unreachable by design** and documented as such below: F9 (retired under the §28 no-floor doctrine), F11 (retired with report-only enforcement), F12 (reserved — ink is always full bleed per §25), F16 (`computeLamPasses` can only return 1, 2, or STOP, never >2).

**Severity legend:**

- **STOP** — output is invalid; engine suppresses the price table when `suppresses_output: true`; banner shown.
- **REVIEW** — output is shown, but Nick should review before quoting; mandates AI validation in some cases.
- **INFO** — informational; no action required to proceed, but should appear in the validation brief.

| ID | Severity | Suppresses Output | Description |
|----|----------|:-----------------:|-------------|
| F1 | STOP | no | Material cost stale (>365 days from `verified_date`) — reverify before quoting. |
| F2 | REVIEW | no | Material cost approaching stale (>180 days) — verify or note in brief. |
| F3 | STOP | yes | Label narrow dimension exceeds 13.5" laminator max — wider laminator required; route to Nick. |
| F4 | STOP | no | Margin below 50% at one or more tiers — work is not worth doing at the floor. |
| F5 | REVIEW | no | Margin at qty 20 below category warn threshold — review. |
| F6 | REVIEW | no | Margin at 200+ approaching floor — verify intentional volume reward, not error. |
| F7 | REVIEW | no | Per-sq-ft rate outside band tolerance (±15%). Either complexity, new material, or repricing needed. (With band-anchored briefs this fires only on genuine deviations — the pre-Session-H 100% alarm saturation is gone.) |
| F8 | INFO | no | Item at low end of singles band scope — band-consistent pricing applies; small-label fixed cost premium acknowledged. |
| F9 | INFO | no | **RETIRED (§28 no-floor doctrine).** Was: "Tiny item (≤0.1 sq ft) — REVIEW, AI validation recommended." The tiny one-off route was removed when §28 established no job floor on this account — all sub-0.1 sq ft items now route unconditionally to the Micro-Format Band (or F26, below ~0.06 sq ft). Definition kept for ID stability; description corrected 2026-07-15 governance drift remediation (was stale — still described the pre-§28 REVIEW behavior). |
| F10 | REVIEW | no | Sub-scope single (0.1–0.5 sq ft) — below band scope. Excluded from band DATA POINTS until production-volume acceptance. |
| F11 | INFO | no | **RETIRED (Session H).** Was: "cliff auto-fixed at the 10-19 boundary." Post-Session-C it could fire only when `checkInvoiceProtection()`'s 10-19 autofix mutated a tier — which never happened after `enforceTierBoundaries()` ran (0 residual violations), making it dead code (audit H-4). With report-only enforcement no code path mutates tiers at all, so F11 can never fire. Definition kept for ID stability. |
| F12 | INFO | no | **RESERVED (Session H).** Was: "ink cost is an unverified placeholder." Unreachable while ink is always `full_bleed_flood_coat` per §25 (H-1 fix) — the legacy placeholder rates are no longer routing targets. |
| F13 | INFO | no | Color PMS caveat — visual approximation only; disclose in quote that this is not a certified Pantone match. |
| F14 | INFO | no | Alternate roll width available — efficiency scenario surfaced (do NOT pass savings to buyer; internal margin lever). |
| F15 | REVIEW | no | Rule 14 deviation: this item is benchmarked against a Relationship Concession band. AI consensus band is higher — document the strategic choice. |
| F16 | REVIEW | no | Kit requires >2 lamination passes — parity boundary exceeded. **Unreachable in the current engine** (audit H-4): `computeLamPasses` returns 1, 2, or STOP(F20) only. Kept as the documented guard should the pass model ever change. |
| F17 | STOP | yes | No Pricing Profile band for this material family yet — first item establishes the band. Cost-build and run AI validation (all 4 rounds). |
| F20 | STOP | yes | Cannot fit kit in ≤2 lam-pass orientation groups — exceeds current equipment routing. Requires Nick review (mixed-dim or special handling). |
| F21 | REVIEW | no | Per-label parity does NOT apply — fires on (a) mixed-dimension kits (cost-build from scratch, AI validation Rounds 1+2 minimum) and (b) kit item type with `label_count = 1`, which is re-routed to the single path (W3 guard, Session H) — verify the intended label count. |
| F22 | INFO | no | Item below band — verify intentional. Smaller labels carry higher fixed cost per sq ft, not lower; below-scope position does NOT justify below-band $/sq ft. |
| F23 | INFO | no | Tier boundary cliff detected — **REPORT-ONLY (Session H)**: the tier table is NOT modified. One flag per boundary that would invert; detail text carries the cliff math and the §26 resolution (buyer billed the lesser adjacent-tier total). Multi-tier band templates cliff at all 5 boundaries by design, so F23×5 on a standard run is expected and documented in the brief. |
| F24 | STOP | yes | Invalid input — width, height, and label count must all be positive (W2 input-sanity guard, Session H). |
| F25 | STOP | yes | Unknown cut vinyl color — no verified material cost exists for this color key (W6 guard, Session H). Add the material in the Materials tab or pick a configured color. |
| F26 | STOP | yes | **Added 2026-07-15 (governance drift remediation).** Sub-0.06 sq ft — per-label floor governs, complexity-dependent (ANSI hazard/danger vs. non-ANSI instructional per the doctrine established via P/N 3024592/3024140). `buildPrintLamMicroTiers` refuses to compute the linear $30.86/sq ft Micro-Format formula below this threshold — the engine cannot auto-classify complexity from dimensions alone, so a wrong silent number is not an option. Output blocked; brief names the two governing comparables (P/N 3024592 ANSI $2.75/qty 20, P/N 3024140 non-ANSI $2.50/qty 20) and points to the per-label floor doctrine in `governance/PRICING_RULES.md`. |
| F27 | REVIEW | no | **Added 2026-07-16 (nearest-neighbor chain-consistency rule, `governance/PRICING_RULES.md` §32); live in the engine since the same date.** New item's $/sq ft, at one or more of the six tiers, undercuts its nearest larger validated same-family neighbor's $/sq ft by 2 or more $0.25 increments (a Direction B violation beyond the §32 tolerance) — the class of deep-tier chain break the account's qty-20-only validation process does not otherwise catch (`audits/2026-07-16-deep-tier-chain-consistency.md`). Fires for the `single_standard`, `single_sub_scope`, and `cut_vinyl` routes only (kits carry an intentional per-sq-ft premium and are structurally out of scope). Does not fire against the two permanent root benchmarks (P/N 1230820, 1205720) — in either direction, including when the calculator is re-run against one of their own dimensions, not just when one is the comparison target — or against any item routed through the F26 per-label floor (checked both when the new item itself is F26-STOPped and when a *candidate neighbor* would itself be F26-governed, the latter derived structurally from `per_label_floor_threshold_sq_ft` so future F26 items are exempt automatically). When no validated neighbor exists inside the family's tested sq ft range (`chain_consistency.tested_range`, Orajet 0.019–1.296 / cut vinyl 0.969–7.069), the engine reports a `chain_consistency.status: 'gap'` (data-coverage gap) instead of firing F27 — visible in the brief's "Chain Consistency (§32)" section and the Band Positioning UI panel, never conflated with a real violation. Acknowledge in the validation prompt before proceeding — per §32, closing a flagged gap is a pricing decision, not an automatic recalculation. **Implementation:** `findNearestLargerChainNeighbor()` + `checkChainConsistency()` in `frontend/index.html`, called from `runCalculator()` right after tier-build; all comparable data, exclusion classes, and thresholds are sourced from the `chain_consistency` block in `calculator_config.json` (seeded by `scripts/build_calculator_config.py`), never hardcoded in the HTML — same convention as `do_not_benchmark` and the F26 per-label-floor constants. |
| F28 | STOP | yes | **Added 2026-07-16 (application tape width resolution, `governance/PRICING_RULES.md` §33), following the P/N 3023921 tape-selection gap.** No application tape roll on file (`application_tape_rolls`, sourced from every tape material registered in Materials, independent of vinyl color) has a `roll_width_in` >= the label's narrow (across-roll) dimension. `computeCutVinylMaterial`'s `resolveApplicationTape()` throws before any material cost is computed, so the return is a clean `null` (blocked), never `$undefined`/`$NaN` — the original P/N 3023921 failure mode (its Round 1 brief was blocked by an undefined 30" tape rate before Nick supplied it manually). A saved Combination's own tape component, or an inline per-quote override, bypasses this check entirely (both are supplied via `inp.tape_override`/`config.tape_override` and take precedence over the dynamic default) — this flag only fires when no such override exists AND no tape roll on file is wide enough. Output blocked; add a wider tape roll to Materials, or pair the item with a Combination that supplies one. |

### STOP Banner Behavior

When any STOP flag fires:

- The output panel shows a `⛔ Output blocked by STOP flag` banner at the top of the Flags section.
- The Volume Pricing Table is suppressed for `F3`, `F17`, and `F20`.
- F1 and F4 fire as STOP severity but do not suppress output — Nick can still see the price ladder but must clear the flag before proceeding to validation.

---

## 4. What the Calculator Must NOT Do (Canonical)

1. **It must NOT write to any file in `items/`, `categories/`, `materials/`, `governance/`, or the frontend JSONs — and it must NOT write to `elliott_items`, `elliott_pricing_bands`, or `elliott_account_settings` in Supabase.** The calculator is a read-only consumer of its data sources (Supabase first; static JSON fallback). The Materials Manager tab — a separate surface — writes materials and combinations to Supabase; item/band/settings writes are exclusively Claude Code's job through `scripts/migrate_to_supabase.py`, after Nick has approved the final price. RLS enforces this split (anon key has SELECT-only on items/bands/settings).

2. **It must NOT replace the 4-round AI validation process.** A calculator output is a Round 1 starting point. Rounds 2 (Destruction), 3 (Buyer Simulation), and 4 (Final Synthesis) still apply per `governance/PRICING_VALIDATION.md`. The "Ready for Round 1: YES/NO" badge on the Validation Brief section indicates the brief is structurally complete — not that the price is validated.

3. **It must NOT be quoted to the buyer.** The brief is internal scratch. Nick converts brief → quote email by hand or with another tool, applying judgment, override types, and account context. Calculator language ("route_reason", "single_sub_scope", "F10 REVIEW") does not appear in any buyer-facing artifact.

4. **It must NOT bypass `do_not_benchmark` filtering.** The comparable-items lookup must exclude every P/N in `CALCULATOR_CONFIG.do_not_benchmark`. Benchmarking against an outrigger-program peer (1277970–1278000), a standalone tiny one-off (3017583, 3017584), a sub-scope single before production-volume acceptance (1210810), or an initial-order job-economics price (1082570) is a structural error the calculator must prevent.

5. **It must NOT hardcode pricing constants.** All bands, tier ratios, snap granularity, ink rates, the 13.5" laminator constraint, the 0.1/0.5/1.5 sq ft scope thresholds, the §31 sub-scope root floor (`sub_scope_root_floor_psf`), the per-label floor threshold (`per_label_floor_threshold_sq_ft`) and its two governing comparables, the cut-vinyl tape row-spacing allowance (`cut_vinyl_row_spacing_in`), the do-not-benchmark list, the §32 chain-consistency data (`chain_consistency.excluded_pn`, `chain_consistency.permanent_exceptions`, `chain_consistency.tolerance_increments`, `chain_consistency.increment_size`, `chain_consistency.tested_range`), and the verified material costs come from the data layer (Supabase `elliott_pricing_bands` / `elliott_account_settings` / `elliott_materials`, mirrored in `calculator_config.json` as the offline fallback). The HTML carries the engine only. When a constant changes: update `scripts/build_calculator_config.py` constants, re-run it, and re-run `scripts/migrate_to_supabase.py` to push the change to Supabase — do not edit the HTML. (Session H removed the last hardcodes: the legacy $2.99/$5.16 kit material totals. 2026-07-15 governance drift remediation added the three per-label-floor/tape constants. 2026-07-16 added the five §32 chain-consistency constants.)

6. **It must NOT propagate stale material cost without flagging.** Every material in `material_constants` and `cut_vinyl_colors` carries a `verified_date`. The calculator computes `days_since(verified_date)` for each material consumed by the active route and fires F2 (>180 days) or F1 (>365 days). A stale cost without a flag is a Self-Healing Rule violation.

7. **It must NOT smooth over `do_not_benchmark` arithmetic.** Tiny-route output suppresses the per-label cost card in favor of a `.oneoff-block` showing "$55 program total / per-label suppressed" — the per-label is a minimum-run artifact, not a catalog rate. Never display tiny-route per-label numbers as if they were a real price.

8. **It must NOT skip never-pay-more verification.** Every adjacent tier pair (1-9→10-19, 10-19→20-49, 20-49→50-99, 50-99→100-199, 100-199→200+) is checked. If the total at the top of the lower tier exceeds the total at the bottom of the upper tier, the lower tier price is auto-capped.

9. **It must NOT invent a band for a material family that has none.** Convex High Bond + Poly Lam and Lexan/Polycarbonate both route to `no_profile` (F17 STOP). The first item in a new material family establishes the band — that requires a cost-build, all 4 validation rounds, and Nick's lock.

10. **It must NOT modify the band data for existing items, even if their tier table fails a cliff check.** The 4 cut vinyl items have cliffs at every tier boundary by design (no invoice protection rule on cut vinyl). The engine surfaces this as informational context only; the existing items' `categories/cut-vinyl-3m-180mc.md` band data is the source of truth.

11. **After every tier generation, `enforceTierBoundaries()` runs in REPORT-ONLY mode (Session H, audit C-1 / decision fork D1).** The function still walks boundaries bottom-up and computes what a strict never-pay-more cascade WOULD cap — but the result is never applied. Rationale: every Nick-locked catalog tier table keeps intentional boundary cliffs that §26 invoice protection resolves at billing time, so a brief generator that rewrote tiers could never agree with the catalog it feeds (the pre-Session-H strict cascade drove every brief 29–46% below catalog/band, with a self-contradictory anchor-vs-table presentation). Behavior now: the tier table is band-anchored; each boundary that would invert fires one F23 INFO flag carrying the cliff math and the §26 resolution; the brief's invoice-protection section lists every such boundary with "§26: bill the lesser total." `checkInvoiceProtection()` is the live check on the unmodified table — its violations ARE the §26 worklist, not a bug. Runs on every tiered route including the micro-band template (the former `skip_enforcement` special case is retired — reporting can't damage a locked table). Does NOT run on `tiny` (flat $55) or `no_profile` (no tiers). The pre-Session-H 10-19 autofix is removed; nothing mutates tiers (F11 retired).

---

## 5. Relationship to `governance/PRICING_VALIDATION.md`

The calculator is the **Round 1 brief generator**. It does not replace any of the 4 rounds.

```
┌──────────────────────────────────────────────────────────────────┐
│                        Calculator (HTML)                         │
│                                                                  │
│   Reads:  calculator_config.json + data.json + materials.json    │
│   Output: Validation Brief (plain text, scrollable, copy button) │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           │ Nick copies the brief
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                  Round 1 — Build Round (6 models)                │
│   The validation brief becomes the prompt input. Models propose  │
│   tier tables, margin estimates, and risk flags.                 │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│              Round 2 — Destruction Round (6 models)              │
│   Attack vectors: Buyer/Procurement, Competitor, Cost Auditor,   │
│   Strategic. Severity rated L/M/H per vector.                    │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│             Round 3 — Buyer Simulation (6 models)                │
│   Role-played buyer (industrial procurement, ~$140K spend).      │
│   Pushback threshold, instant-approval number.                   │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│             Round 4 — Final Synthesis (6 models)                 │
│   Send-as-shown verdict. Long-term precedent check.              │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
                  Nick locks the final price
                           │
                           ▼
       Claude Code writes the item file + propagates per
       .claude/COMPLETION_TEMPLATES.md Self-Healing Rule
```

**Key consequences:**

- The "Ready for Round 1: YES/NO" badge on the calculator's Validation Brief section verifies brief completeness (all required fields populated, no STOP flag suppressing output), not pricing correctness.
- Direct-parity exemption still applies. Per `PRICING_VALIDATION.md`, items dimensionally and materially identical to an already-quoted item skip multi-round AI validation (Rule 15 — band check — still applies). The calculator still produces a brief for direct-parity items; Nick may bypass Rounds 2–4 when the parity is unambiguous.
- The calculator's F9 (tiny one-off), F10 (sub-scope), F15 (Rule 14 deviation), F16 (kit >2 lam passes), F17 (no profile), F20 (lam routing fail), F21 (mixed-dim kit) flags all explicitly call for AI validation in their text. When any of these fire, Nick runs the rounds even if he would otherwise consider the item a parity case.

---

## 6. Updating the Calculator When Pricing Rules Change

The calculator has three update mechanisms depending on what changed:

### 6.1 Constant Change Only — Re-Run Build Script

For changes to:

- Band thresholds (`min_per_sq_ft_qty_20`, `max_per_sq_ft_qty_20`)
- Tier ratios or tier templates
- Snap granularity
- Ink rate (`full_bleed_flood_coat` — the only routing target per §25; legacy keys are historical reference only)
- Sq-ft scope thresholds (tiny, sub-scope, singles)
- Cut vinyl size-class thresholds (`cut_vinyl_band_thresholds.band_b_floor_sq_ft`, `band_c_ceiling_sq_ft`)
- Band B / Band C anchor PSF and tier templates
- Equipment limits (laminator, Roland print bed)
- Quote language templates
- `do_not_benchmark` list
- Override type precedent
- Flag thresholds

**Procedure:**

1. Edit the named constants at the top of `scripts/build_calculator_config.py`.
2. Re-run: `python scripts/build_calculator_config.py`
3. Re-run: `python scripts/migrate_to_supabase.py` (pushes the change to the
   Supabase tables the deployed app reads first).
4. Commit `frontend/calculator_config.json` (regenerated) alongside the script change.

**No code change to `frontend/index.html` is required.** The HTML reads the data layer; the build-script constants are the seed source of truth for these values (Supabase primary, JSON fallback).

### 6.2 Material Cost Change — Two Paths (Session H)

**Path A — Materials Manager (Nick, day-to-day):** edit the material in the
Materials tab; the change writes to `elliott_materials` directly and the
calculator picks it up immediately (the in-memory config re-hydrates on
save — no reload, no build). Then, to keep the repo in sync: run
`python scripts/sync_from_supabase.py` (regenerates the fallback JSONs) and
have a Claude Code session backfill the change into `materials/*.md` +
`governance/PRODUCTION.md` per the COMPLETION_TEMPLATES material-cost
trigger.

**Path B — repo-first (Claude Code session):**

1. Edit the relevant `materials/*.md` file (frontmatter only).
2. Re-run all three build scripts:
   - `python scripts/build_frontend.py`
   - `python scripts/build_materials.py`
   - `python scripts/build_calculator_config.py`
3. Re-run `python scripts/migrate_to_supabase.py` (upserts the new cost into
   `elliott_materials`).
4. Commit the generated JSON files plus the materials file.

Material staleness flags F1 (>365 days) and F2 (>180 days) re-evaluate automatically on every calculator run against the new `verified_date`.

### 6.3 Engine Behavior Change — HTML Edit Required

For changes to:

- The routing decision tree itself (adding a new route, moving a threshold from constant to logic)
- A new flag (F23+)
- A new calculator output section
- A change to the validation brief format
- A change to how lam passes are computed
- A change to material-cost computation methodology

These require editing the `<!-- CALCULATOR ENGINE -->` script block in `frontend/index.html`. After the edit:

1. Verify both inline `<script>` blocks parse cleanly (Node `new Function(blockSrc)` check).
2. Run `python scripts/validate.py` (should be 0 errors, 0 warnings — calculator changes do not affect item validation).
3. Re-run all three build scripts (timestamp regeneration only).
4. Run `runSanityChecks()` (browser console, or the Node harness used in
   audits) — **all 21 implemented cases must pass** (16→21 in the 2026-07-16
   F27 live-engine session — see cases 18–22 below; the prior "17" figure
   here was stale — the actual pre-F27 suite had only 16 cases, since case 7
   (`1277970` tiny-route) was retired under §28 and removed from the code
   without this count being corrected at the time). The full expected matrix
   is §9; the quick regression list (post-Session-H truth — this list
   previously held stale MOQ-era expectations, audit H-4):
   - 1230820 → `single_standard`, **$20.00** (band-anchored), F23×5 report-only, NO F7/F11/F12/F18/F27 (permanent §32 exception — never fires on itself, either direction)
   - Convex High Bond 10×6 → `no_profile`, F17 STOP, output suppressed
   - 1245130 (5-label kit) → `kit`, $50, per-label $10.00, W1 lam-pass advisory present
   - 1205720 → `cut_vinyl` Band A, $35, F15 + F23×5, tape material cost **$7.88** (length-based, corrected 2026-07-15 — was $8.74 under the deprecated area pseudo-rate), NO F5/F27 (permanent §32 exception)
   - 1210810 → `single_sub_scope`, **$4.75** (§31 root floor clamp, 2026-07-15 — the algorithmic anchor now matches the catalog-locked price exactly; was $4.50, below the $15.43/sq ft floor, pre-fix), F10 + F8 + F23×2
   - 3024595 → `single_sub_scope`, $7.75 at 20-49 through 200+ **flat natively** (§31 floor clamp, 2026-07-15 — was $7.50/$6.50/$5.25/$4.25, all below floor, pre-fix), F10 + F27 (vs nearest larger neighbor 3017572, 1-9/10-19 tiers) + F8 + F23×2
   - 1205870 → `single_sub_scope`, **STOP (F26)**, output suppressed (per-label floor, 2026-07-15 — was a silent $1.50 @ qty 20, no flag, pre-fix), NO F27 (F26-routed items never evaluate §32)
   - 1101250 → `single_sub_scope`, $2.25, **F27 REVIEW** fires against nearest larger neighbor 1279130 (0.148 sq ft) — 3 of 6 tiers (1-9/10-19/20-49) exceed the 2-increment tolerance; 50-99 sits within tolerance and correctly does not fail (2026-07-16, F27 live-engine session)

All routes must continue to produce correct routing badge, band-anchored price ladder, band positioning visual, comparable items (filtered by do_not_benchmark, self-excluded), and a copyable validation brief whose anchor line, tier table, and quote stub all carry the SAME price.

---

## 7. Session Sequence — Adding a New Item Using the Calculator

The calculator slots into the existing new-item workflow at the front. The downstream sequence is unchanged.

### Step 1 — Spec Extraction (Pre-Calculator)

Run `governance/SPEC_EXTRACTION.md` extraction on the engineering PDF. Capture all 14 mandatory fields. The calculator requires width, height, label count, material family, item type, ink coverage (printed/lam), and cut vinyl color (cut vinyl) as a minimum.

### Step 2 — Calculator Run (Round 0 — Brief Generation)

1. Open `frontend/index.html`, click the **Calculator** tab.
2. Pick the **Material Combination** in the left rail (Session H — this replaced the material-family and cut-vinyl-color dropdowns): one selection resolves every component cost. The component breakdown below the dropdown shows each material's cost and verified date; any component can be overridden inline for this quote without changing the saved combination.
3. Fill in the remaining form fields. Optional fields (Part Number, Description, Model, Notes) can be skipped for an unassigned item. Ink coverage is a read-only display — full bleed $0.50/sq ft per §25, always. **ANSI status is not a user input** — all Orajet 3951 + polyester lam items on this account are ANSI by account rule (§29). The validation brief automatically shows "ANSI: Yes — account rule (all Orajet/lam items)." The ANSI checkbox was removed 2026-06-29.
4. Click **Run Calculator**.
5. Review the output panel:
   - **Routing & Summary** — confirm the route matches expectation (`single_standard`, `cut_vinyl`, etc.)
   - **Flags** — read every flag. STOP flags must be cleared before proceeding. REVIEW flags must be acknowledged in the validation prompt. F23 entries are report-only cliff notices with the §26 resolution — expected on every multi-tier run.
   - **Volume Pricing Table** — sanity-check the band-anchored tier ladder.
   - **Material Cost Breakdown** — confirm the §25 canonical build. The breakdown text is verbatim what goes into the validation brief.
   - **Band Positioning** — confirm $/sq ft lands in the expected band. F7 fires if outside ±15% tolerance.
   - **Production Summary** — confirm lam passes and laminator fit; heed the W1 lam-pass advisory when it appears (verify pass count against PRODUCTION.md before quoting lead time).
   - **Validation Brief** — verify "Ready for Round 1" badge is YES. If NO, the brief is incomplete and Round 1 should not start.
6. Click **Copy Validation Brief**. The plain-text brief is now on the clipboard.

### Step 3 — Round 1 (Build Round, 6 Models)

Open 6 fresh chats with 6 different top-tier reasoning models. Paste the validation brief into each. Capture all 6 responses per `governance/PRICING_VALIDATION.md` Round 1 output schema (Interpreted Specs, Benchmark Match, Cost Drivers, Proposed Tiers, Per-Label Math, Margin Estimate, Risk Flags, Kill Criteria).

### Step 4 — Round 2 (Destruction Round, 6 Models)

Per `PRICING_VALIDATION.md` Round 2. Fresh chats; provide Round 1 outputs + the original brief. Capture 4 attack-vector severities and verdicts.

### Step 5 — Round 3 (Buyer Simulation, 6 Models)

Per `PRICING_VALIDATION.md` Round 3. Role-play buyer. Capture pushback thresholds and instant-approval numbers.

### Step 6 — Round 4 (Final Synthesis, 6 Models)

Per `PRICING_VALIDATION.md` Round 4. Verdict on send-as-shown. Adjustments documented.

### Step 7 — Nick Locks the Price

Nick selects the final tier table, override type (if any), and any deviations from the calculator's initial output. The locked price may differ from the calculator's output — the calculator is the starting point, not the verdict.

### Step 8 — Claude Code Writes the Files

A new Claude Code session is initiated with:

- The locked price
- The full 4-round validation record
- The original calculator brief
- All session context per `.claude/MASTER_CONTEXT.md` Reading Order — New Item Pricing

Claude Code then:

- Writes the new `items/[PN].md` with all required frontmatter and the 10 required sections per `governance/STRUCTURE_RULES.md`
- Updates `categories/[relevant].md` (items table + Pricing Profile if band shifts)
- Updates `.claude/ARCHITECTURE.md` (catalog row + precedent chain + category registry counts)
- Updates `.claude/PROGRESS.md` (full session entry)
- Updates `.claude/STATE.yml` (item_count + last_session + next_action)
- Updates relevant `materials/*.md` `used_in_items` lists
- Runs all build scripts (`build_frontend.py`, `build_materials.py`, `build_calculator_config.py`) and commits the regenerated JSON
- Runs `python scripts/validate.py` — must end at 0 errors, 0 warnings

**The calculator does not write any of these files.** Claude Code is the sole author.

### Step 9 — Quote to Sean

Nick composes the quote email by hand, using the calculator's quote-language stubs (anchor line + PMS caveat where applicable — MOQ language no longer exists on this account, purged 2026-06-05) as a starting point but applying judgment for account context, recent conversations, and the strategic framing this item needs. For rush or favor jobs, apply the §27 $50 rush/favor floor if applicable (`governance/PRICING_RULES.md` §27). Document as One-Time Exception. The calculator output is internal scratch — Sean never sees a route name, a flag ID, or a "validation brief" reference.

---

## 8. Files in the Calculator System

| File / Surface | Role | Source of Truth For |
|------|------|---------------------|
| Supabase `elliott_pricing_bands` / `elliott_account_settings` / `elliott_materials` / `elliott_material_combinations` / `elliott_items` | **PRIMARY data layer** (Session H) | Live band constants, account settings, material costs, combinations, item catalog the deployed app reads first |
| `frontend/index.html` | Calculator engine + UI + Materials Manager | Routing logic, flag firing logic, brief format, render output, Supabase hydration (anon key constants at top of the UI script block) |
| `frontend/calculator_config.json` | Constants config (generated — OFFLINE FALLBACK) | Band thresholds, tier ratios, ink rates, do_not_benchmark, chain_consistency (§32 excluded_pn/permanent_exceptions/tolerance/tested_range), quote language when Supabase is unreachable |
| `frontend/data.json` | Items database (generated — fallback + prose) | Items tab sections/images; comparable items lookup offline |
| `frontend/materials.json` | Materials database (generated — fallback) | Materials View offline |
| `frontend/combinations.json` | Combinations snapshot (generated by sync — fallback) | Calculator combination selector offline |
| `scripts/build_calculator_config.py` | Build script + **seed constants** | Generates `calculator_config.json` from repo state; its named constants are what `migrate_to_supabase.py` seeds into Supabase |
| `scripts/build_frontend.py` | Build script | Generates `data.json` |
| `scripts/build_materials.py` | Build script | Generates `materials.json` |
| `scripts/migrate_to_supabase.py` | Migration (service_role) | Repo → Supabase: materials, items, bands, settings, default combinations. Idempotent. RLS/auth approach documented in its header. **MANDATORY at end of every new-item Claude Code session.** Run after `validate.py` passes. Confirm row count before committing. Never defer. |
| `scripts/sync_from_supabase.py` | Sync (anon key suffices) | Supabase → repo: regenerates all four fallback JSONs from live DB state |
| `governance/CALCULATOR.md` | This file | The contract — what the calculator is, is not, and how to extend it |
| `governance/PRICING_VALIDATION.md` | Companion governance | The 4-round AI validation process the calculator feeds into |
| `governance/PRICING_RULES.md` | Companion governance | The constraints the calculator encodes (full bleed ink rule (§25), invoice protection (§26), file prep = $0 (§22-24)) |

---

## 9. Sanity Check Reference Cases

The reference cases below are the calculator's regression test surface. The table documents 24 cases; the `runSanityChecks()` suite in the engine block currently implements **23** of them and reports pass/fail per case — row 7 (`1277970`, the `tiny` route) was retired from the live suite under the §28 no-floor doctrine and is kept here only as a historical reference, not actually run (this table's earlier "all 17" claim never matched the code once row 7 was removed; corrected 2026-07-16 alongside the F27 addition, and again alongside the F28 addition below). Any engine change must keep all 23 implemented cases passing. With **report-only enforcement** (Rule 11, Session H), tier tables are **band-anchored**: where the catalog value and the engine's algorithmic snap differ, the divergence is a documented snap/premium artifact (noted per row), not cascade compression. All printed/laminated cases run at full-bleed ink per §25 (ink is no longer an input).

All expected values below were verified live via the Node `vm` harness on 2026-06-09 (Session H); cases 15–17 (and the row 3 / row 6 corrections) were verified live via the same Node `vm` harness method on 2026-07-15 (governance drift remediation — see `audits/2026-07-15-governance-drift-audit.md`); cases 18–22 (F27 nearest-neighbor chain consistency) were verified live via the same method on 2026-07-16, alongside re-verifying rows 1–17 still pass unchanged; cases 23–24 (F28 application tape width resolution) were verified live via the same method on 2026-07-16, alongside re-verifying rows 1–22 still pass unchanged (22/23 implemented cases pass — the one pre-existing failure, row 4 / 1278930, predates this session and is unrelated to cut vinyl or tape).

| # | Input | Route | Price@20 (engine) | Required Flags | STOP? |
|---|-------|-------|---------:|---------------|:-----:|
| 1 | 1230820 — Orajet single, 15"×12.44" | `single_standard` | **$20.00** (band-anchored = catalog) | F23×5 (report-only); NO F7/F11/F12 | no |
| 2 | 1082570 — Orajet single, 10"×7.25" | `single_standard` | $7.75 (0.503 × $15.43 = $7.76 → snap $7.75; catalog locked $8.00 — documented snap divergence since Session B) | F8, F23×5 | no |
| 3 | 1210810 — Orajet single, 10.5"×4" | `single_sub_scope` | **$4.75 flat from 20-49 through 200+** (§31 sub-scope root floor clamp, 2026-07-15 — the $4.50 pre-clamp anchor priced at $15.41/sq ft, below the $15.43/sq ft floor; clamped to $4.75 = $16.27/sq ft, now an EXACT match with the catalog-locked Wave 4 price — previously documented as a divergence, no longer one) | F10, F8, F23×2 | no |
| 4 | 1278930 — Orajet 3-label kit, 11.13"×7.88" | `kit` | **$30.00** ($10.00/label — per-label table consistent with kit totals) | F23×5 | no |
| 5 | 1245130 — Orajet 5-label kit, 11.13"×7.88" | `kit` | **$50.00** ($10.00/label) + **W1 lam-pass advisory** (5 × 7.88" > 28" print bed; production reality 2 passes) | F23×5 | no |
| 6 | 1205720 — Cut vinyl Cardinal Red, 33.5625"×11" (Band A) | `cut_vinyl` | **$35.00** (band-anchored = catalog); material cost **$7.88** (tape now length-based, 2026-07-15 — was $8.74 under the deprecated `sq_ft × $0.5911` area pseudo-rate; matches `categories/cut-vinyl-3m-180mc.md`'s $7.88–$8.82 documented range) | F15, F23×5; NO F5 | no |
| 7 | 1277970 — Orajet single, 1.1875"×1.1875" (Ø1-3/16) — **RETIRED from the live suite** (§28 no-floor doctrine; historical reference only, not implemented in the current `runSanityChecks()`) | `tiny` | $55.00 (flat program total — enforcement/reporting does not run on tiny) | F9 | no |
| 8 | 3010704 — Cut vinyl Cardinal Red 15", 70.8125"×14.375" (Band B) | `cut_vinyl` | **$78.00** (Band B template direct — within ±30% of founding anchor) | F15, F23×5 | no |
| 9 | 3010707 — Cut vinyl Cardinal Red, 34.887"×4" (Band C) | `cut_vinyl` | **$20.00** (Band C template direct) | F15, F23×5 | no |
| 10 | Sub-0.1 production override — Orajet single, 8"×1.75", `production_override: true` | `single_sub_scope` | **$3.00** (Micro-Format Band template direct, 1279000 anchor). The template cliffs at ALL 5 boundaries (e.g. 9×$4.50 = $40.50 > 10×$3.50 = $35.00) — **F23×5 fires (report-only)**, table preserved verbatim. (Pre-Session-H doc claimed "no 9/10 inversion / F23 fires fewer times" — wrong on both counts, audit H-4.) | F10, F8, F23×5 | no |
| 11 | Convex High Bond single, 10"×6" | `no_profile` | n/a (output suppressed) | F17 | YES |
| 12 | **NEW (Session H)** — 1278890, Orajet 2-label kit, 7.88"×11.13" | `kit` | **$20.00 / $10.00 per label** via the **cost-build path** (no 2-label template exists; per-label parity $10.00 × 2 — matches catalog at qty 20; the algorithmic 200+ lands $11 vs catalog $12, snap artifact) | F23×5 | no |
| 13 | **NEW (Session H)** — 1068270, Orajet single, 7.25"×10.00" | `single_standard` | $7.75 — **byte-identical engine output to 1082570** (orientation-flip parity; catalog $8.00, same documented snap) | F8, F23×5 | no |
| 14 | **NEW (Session H)** — 3010701, Cut vinyl Cardinal Red, 49.16"×9.38", 3.202 sq ft (Band A) | `cut_vinyl` | $45.00 (Band A algorithmic: 3.202 × $13.795 mid-band = $44.17 → snap $45; catalog locked $44 — Band A has no MED template; documented divergence) | F15, F23×5 | no |
| 15 | **NEW (2026-07-15 governance drift remediation)** — 3024595, Orajet single, 15"×4.687", 0.488 sq ft (sub-scope) | `single_sub_scope` | **$7.75 flat from 20-49 through 200+** — §31 root floor clamp now natively produces the flat structure the catalog had to be hand-corrected to (pre-fix engine: $7.50/$6.50/$5.25/$4.25, all below the $15.43/sq ft floor). 1-9/10-19 ($11.50/$9.00) remain algorithmic ratio-scaled — NOT expected to match the catalog's Wave-1-judged $10.75/$9.25 (those reflect AI benchmark interpolation the formula cannot reproduce; §31 governs the floor, not the premium). | F10, F8, F23×2 | no |
| 16 | **NEW (2026-07-15 governance drift remediation)** — 1205870, Orajet single, 4"×1.75", 0.049 sq ft (sub-0.06) | `single_sub_scope` | n/a (output suppressed) — pre-fix the engine silently computed **$1.50** at qty 20 via the linear formula (catalog-locked correct price: $2.50, non-ANSI per-label floor); F26 now STOPs instead of emitting the wrong number | F26 | YES |
| 17 | **NEW (2026-07-15 governance drift remediation)** — 1205720 material-cost re-check, Cut vinyl Cardinal Red, 33.5625"×11" | `cut_vinyl` | Material cost **$7.88** ($7.23 vinyl + $0.65 tape) — exact match with `categories/cut-vinyl-3m-180mc.md`'s documented figure; tape is now `(label length + 6" spacing) in yd × $1.1821/yd ÷ labels per row`, not the deprecated `sq_ft × $0.5911/sq ft` pseudo-rate (pre-fix: $8.74, a ~2.7× tape overstatement) | F15, F23×5; NO F5 | no |
| 18 | **NEW (2026-07-16, F27 live-engine session)** — 1101250, Orajet single, sub-scope, 0.132 sq ft | `single_sub_scope` | $2.25 (engine's own fresh sub-scope computation, not 1101250's filed/One-Time-Exception price) — `chain_consistency.status = 'violation'` vs nearest larger neighbor 1279130 (0.148 sq ft): 3 of 6 tiers (1-9, 10-19, 20-49) exceed the §32 2-increment tolerance; 50-99 sits within tolerance and correctly does not fail (tolerance mechanism verified live); 100-199/200+ hold | F10, F27, F8, F23×2 | no |
| 19 | **NEW (2026-07-16, F27 live-engine session)** — SYNTHETIC Orajet single, 24"×12", 2.0 sq ft (no P/N) | `single_standard` | $31.00 — `chain_consistency.status = 'gap'` (2.0 sq ft is above the family's §32 tested range, 0.019–1.296 sq ft; no validated neighbor exists above the ceiling) — data-coverage gap, distinct from a real F27 violation | F23×5; NO F27 | no |
| 20 | **NEW (2026-07-16, F27 live-engine session)** — SYNTHETIC cut vinyl, 12"×6", 0.5 sq ft (no P/N) | `cut_vinyl` | $10.00 — `chain_consistency.status = 'gap'` (0.5 sq ft is below the family's §32 tested range, 0.969–7.069 sq ft — no cut-vinyl data exists at any smaller size) — data-coverage gap | F15, F23×5; NO F27 | no |
| 21 | **NEW (2026-07-16, F27 live-engine session)** — SYNTHETIC Orajet single, 12"×12", 1.0 sq ft (no P/N) | `single_standard` | $15.50 — `chain_consistency.status = 'exempt_permanent'`: nearest larger validated neighbor resolves to the root benchmark 1230820 (1.296 sq ft) — never re-evaluated regardless of gap size | F23×5; NO F27 | no |
| 22 | **NEW (2026-07-16, F27 live-engine session)** — 1230820 re-run (self-exception probe) | `single_standard` | $20.00 (identical to row 1) — `chain_consistency.status = 'exempt_permanent'`: the root benchmark is excluded from §32 in either direction (audit §16.1/§13.3) — re-running the calculator against 1230820's own dimensions must never fire F27 against it | F23×5; NO F27 | no |
| 23 | **NEW (2026-07-16, F28 tape-width resolution session)** — SYNTHETIC cut vinyl, 40"×32" (no P/N) | `cut_vinyl` | $78.00 (Band B tier math is untouched — routing/pricing formulas do not depend on tape) but `material.total_per_kit` is **null**, not `NaN`: the 32" narrow dimension exceeds every application tape roll on file (24"/30") | F28 (STOP) | YES |
| 24 | **NEW (2026-07-16, F28 tape-width resolution session)** — 3023921 re-run, no Combination/override supplied | `cut_vinyl` | $23.00 (identical to catalog) — `resolveApplicationTape()` dynamically resolves the 8.5" narrow dimension to the narrowest tape on file that fits (24"), with no Combinations row required and no STOP; the filed item separately uses the 30" tape via its own already-validated Combination, unaffected by this default | NO F28 | no |

If a route doesn't match for any of these cases, the change is incorrect — either the change has a bug or the reference case needs explicit reconsideration with Nick before proceeding. Prices are documented for traceability; snap-rounding variance is tolerated where noted — routes, flags, and the report-only invariant (tier tables never mutated) are hard requirements. Rows 18/21/22 illustrate a general property of the F27 check worth stating explicitly: it always compares the ENGINE'S OWN freshly-computed tiers for "the item being priced" against a real neighbor's FILED tiers — for an existing P/N re-run through the calculator, that fresh computation can diverge from the item's own catalog price (the same documented snap/premium-artifact pattern rows 2/3/13/15 already establish for band-anchored pricing generally), so F27's live behavior on an existing item is not a re-derivation of that item's locked price or of the audit's own filed-price-based findings.

**Note on flag counts:** F23 fires once per boundary that WOULD invert (report-only — the table is not modified). Multi-tier band templates cliff at all 5 boundaries by design, so F23×5 on a standard run is expected; the brief's invoice-protection section lists each boundary with its §26 resolution. Sub-scope items whose §31 floor clamp flattens 20-49 through 200+ into a single price (rows 3 and 15) can only cliff at the 1-9/10-19 and 10-19/20-49 boundaries — F23×2, not F23×5 — since identical adjacent tier prices cannot invert against each other. F7 no longer fires on routine runs (briefs are band-anchored — a fire now means a genuine band deviation). F9, F11, and F12 cannot fire (see §3). The W2/W3/W6 guards (F24 STOP, F21 reroute, F25 STOP) are additionally probed by the harness outside this table, alongside the F26 STOP (row 16), the F27 REVIEW (row 18) / gap and permanent-exception non-fires (rows 19–22), and the new F28 STOP (row 23) / non-fire (row 24).
