# Calculator — Governance Reference

> **Authoritative reference for the Elliott calculator system.**
> The HTML calculator at `frontend/index.html` is the implementation; this document is the contract.
>
> Last Updated: 2026-06-09 (Session I — §7 Step 9: §27 $50 rush/favor floor reference added. Previously Session H — audit C-1/H-1/H-2/H-4/H-5 + W1–W6 remediation: tier-boundary enforcement is now REPORT-ONLY (briefs are band-anchored; F23 reports cliffs, §26 resolves at billing, tables are never mutated); ink coverage is full-bleed-only per §25 (dropdown removed); kit material costing uses the §25 canonical formula (legacy $2.99/$5.16 hardcodes removed); F18/F19 ghost rows deleted and the flag table corrected (23 definitions, F24/F25 added, F11/F12/F16 documented unreachable); §6.3 regression checklist rewritten to current truth; singles routing ceiling corrected to 1.5 sq ft; data source is Supabase-first with static-JSON fallback; the material-family/color dropdowns are replaced by the material-combination selector)

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
      │ ($55 floor)  │          │
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
| `tiny` | Orajet 3951 | ≤ 0.1 sq ft | any | None | All 6 tiers flatten to $55 one-off job-economics floor (1230820 FA-anchored) |
| `kit` | Orajet 3951 | > 0.1 sq ft | label_count > 1 OR `Printed/Laminated Kit` | Printed/Laminated Kits | No MOQ. Invoice protection (§26) applies at all tier boundaries. |
| `single_sub_scope` | Orajet 3951 | 0.1–0.5 sq ft *(standard route)* OR ≤ 0.1 sq ft *(via production-override path)* | single | Printed/Laminated Singles (band-consistent, item excluded from band DATA POINTS) for 0.1–0.5 sq ft. **Sub-0.1 sq ft Micro-Format Band ($30.86/sq ft anchor, 1279000 founding data point)** when `production_override: true` is set on a sub-0.1 sq ft Orajet 3951 single — uses the validated tier template directly when the item's sq ft is within ±30% of the founding anchor sq ft (0.097). | No MOQ. Invoice protection (§26) applies at all tier boundaries. |
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

---

## 3. Flag Definitions (Canonical)

All **23** flag definitions live in `frontend/index.html` (calculator engine `FLAG_DEFS`): **F1–F17 and F20–F25**. F18 and F19 (MOQ-era flags) were removed from the engine in Session B (2026-06-05) when MOQ was purged from the account; their rows were deleted from this table in Session H (they had survived here as ghost documentation — audit H-2/H-4). Three defined flags are currently **unreachable by design** and documented as such below: F11 (retired with report-only enforcement), F12 (reserved — ink is always full bleed per §25), F16 (`computeLamPasses` can only return 1, 2, or STOP, never >2).

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
| F9 | REVIEW | no | Tiny one-off (≤0.1 sq ft) — $55 flat program total, NOT a catalog rate. Per-sq-ft math is a minimum-run artifact. Do NOT benchmark. AI validation recommended (Rounds 1+2 minimum) for any tiny one-off. |
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

5. **It must NOT hardcode pricing constants.** All bands, tier ratios, snap granularity, ink rates, the $55 floor, the 13.5" laminator constraint, the 0.1/0.5/1.5 sq ft scope thresholds, the do-not-benchmark list, and the verified material costs come from the data layer (Supabase `elliott_pricing_bands` / `elliott_account_settings` / `elliott_materials`, mirrored in `calculator_config.json` as the offline fallback). The HTML carries the engine only. When a constant changes: update `scripts/build_calculator_config.py` constants, re-run it, and re-run `scripts/migrate_to_supabase.py` to push the change to Supabase — do not edit the HTML. (Session H removed the last hardcodes: the legacy $2.99/$5.16 kit material totals.)

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
- The $55 floor source PN
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
   audits) — **all 14 cases must pass.** The full expected matrix is §9; the
   quick regression list (post-Session-H truth — this list previously held
   stale MOQ-era expectations, audit H-4):
   - 1230820 → `single_standard`, **$20.00** (band-anchored), F23×5 report-only, NO F7/F11/F12/F18
   - 1277970 → `tiny`, $55 flat, F9 only
   - Convex High Bond 10×6 → `no_profile`, F17 STOP, output suppressed
   - 1245130 (5-label kit) → `kit`, $50, per-label $10.00, W1 lam-pass advisory present
   - 1205720 → `cut_vinyl` Band A, $35, F15 + F23×5, NO F5
   - 1210810 → `single_sub_scope`, $4.50 (catalog locked $4.75 — documented snap/premium divergence), F10 + F8 + F23×5

All routes must continue to produce correct routing badge, band-anchored price ladder, band positioning visual, comparable items (filtered by do_not_benchmark, self-excluded), and a copyable validation brief whose anchor line, tier table, and quote stub all carry the SAME price.

---

## 7. Session Sequence — Adding a New Item Using the Calculator

The calculator slots into the existing new-item workflow at the front. The downstream sequence is unchanged.

### Step 1 — Spec Extraction (Pre-Calculator)

Run `governance/SPEC_EXTRACTION.md` extraction on the engineering PDF. Capture all 14 mandatory fields. The calculator requires width, height, label count, material family, item type, ink coverage (printed/lam), and cut vinyl color (cut vinyl) as a minimum.

### Step 2 — Calculator Run (Round 0 — Brief Generation)

1. Open `frontend/index.html`, click the **Calculator** tab.
2. Pick the **Material Combination** in the left rail (Session H — this replaced the material-family and cut-vinyl-color dropdowns): one selection resolves every component cost. The component breakdown below the dropdown shows each material's cost and verified date; any component can be overridden inline for this quote without changing the saved combination.
3. Fill in the remaining form fields. Optional fields (Part Number, Description, Model, Notes) can be skipped for an unassigned item. Ink coverage is a read-only display — full bleed $0.50/sq ft per §25, always.
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

Nick composes the quote email by hand, using the calculator's quote-language stubs (anchor line + PMS caveat where applicable — MOQ language no longer exists on this account, purged 2026-06-05) as a starting point but applying judgment for account context, recent conversations, and the strategic framing this item needs. For rush or favor jobs, apply the §27 $50 rush/favor floor if applicable (`governance/PRICING_RULES.md` §27 — separate from and non-stacking with the $55 one-off floor). Document as One-Time Exception. The calculator output is internal scratch — Sean never sees a route name, a flag ID, or a "validation brief" reference.

---

## 8. Files in the Calculator System

| File / Surface | Role | Source of Truth For |
|------|------|---------------------|
| Supabase `elliott_pricing_bands` / `elliott_account_settings` / `elliott_materials` / `elliott_material_combinations` / `elliott_items` | **PRIMARY data layer** (Session H) | Live band constants, account settings, material costs, combinations, item catalog the deployed app reads first |
| `frontend/index.html` | Calculator engine + UI + Materials Manager | Routing logic, flag firing logic, brief format, render output, Supabase hydration (anon key constants at top of the UI script block) |
| `frontend/calculator_config.json` | Constants config (generated — OFFLINE FALLBACK) | Band thresholds, tier ratios, ink rates, $55 floor, do_not_benchmark, quote language when Supabase is unreachable |
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

The reference cases below are the calculator's regression test surface — the `runSanityChecks()` suite in the engine block runs **all 14** and reports pass/fail per case. Any engine change must keep all 14 passing. With **report-only enforcement** (Rule 11, Session H), tier tables are **band-anchored**: where the catalog value and the engine's algorithmic snap differ, the divergence is a documented snap/premium artifact (noted per row), not cascade compression. All printed/laminated cases run at full-bleed ink per §25 (ink is no longer an input).

All expected values below were verified live via the Node `vm` harness on 2026-06-09 (Session H).

| # | Input | Route | Price@20 (engine) | Required Flags | STOP? |
|---|-------|-------|---------:|---------------|:-----:|
| 1 | 1230820 — Orajet single, 15"×12.44" | `single_standard` | **$20.00** (band-anchored = catalog) | F23×5 (report-only); NO F7/F11/F12 | no |
| 2 | 1082570 — Orajet single, 10"×7.25" | `single_standard` | $7.75 (0.503 × $15.43 = $7.76 → snap $7.75; catalog locked $8.00 — documented snap divergence since Session B) | F8, F23×5 | no |
| 3 | 1210810 — Orajet single, 10.5"×4" | `single_sub_scope` | $4.50 (band-anchored; catalog locked $4.75 — Wave 4 small-format premium, documented) | F10, F8, F23×5 | no |
| 4 | 1278930 — Orajet 3-label kit, 11.13"×7.88" | `kit` | **$30.00** ($10.00/label — per-label table consistent with kit totals) | F23×5 | no |
| 5 | 1245130 — Orajet 5-label kit, 11.13"×7.88" | `kit` | **$50.00** ($10.00/label) + **W1 lam-pass advisory** (5 × 7.88" > 28" print bed; production reality 2 passes) | F23×5 | no |
| 6 | 1205720 — Cut vinyl Cardinal Red, 33.5625"×11" (Band A) | `cut_vinyl` | **$35.00** (band-anchored = catalog) | F15, F23×5; NO F5 | no |
| 7 | 1277970 — Orajet single, 1.1875"×1.1875" (Ø1-3/16) | `tiny` | $55.00 (flat program total — enforcement/reporting does not run on tiny) | F9 | no |
| 8 | 3010704 — Cut vinyl Cardinal Red 15", 70.8125"×14.375" (Band B) | `cut_vinyl` | **$78.00** (Band B template direct — within ±30% of founding anchor) | F15, F23×5 | no |
| 9 | 3010707 — Cut vinyl Cardinal Red, 34.887"×4" (Band C) | `cut_vinyl` | **$20.00** (Band C template direct) | F15, F23×5 | no |
| 10 | Sub-0.1 production override — Orajet single, 8"×1.75", `production_override: true` | `single_sub_scope` | **$3.00** (Micro-Format Band template direct, 1279000 anchor). The template cliffs at ALL 5 boundaries (e.g. 9×$4.50 = $40.50 > 10×$3.50 = $35.00) — **F23×5 fires (report-only)**, table preserved verbatim. (Pre-Session-H doc claimed "no 9/10 inversion / F23 fires fewer times" — wrong on both counts, audit H-4.) | F10, F8, F23×5 | no |
| 11 | Convex High Bond single, 10"×6" | `no_profile` | n/a (output suppressed) | F17 | YES |
| 12 | **NEW (Session H)** — 1278890, Orajet 2-label kit, 7.88"×11.13" | `kit` | **$20.00 / $10.00 per label** via the **cost-build path** (no 2-label template exists; per-label parity $10.00 × 2 — matches catalog at qty 20; the algorithmic 200+ lands $11 vs catalog $12, snap artifact) | F23×5 | no |
| 13 | **NEW (Session H)** — 1068270, Orajet single, 7.25"×10.00" | `single_standard` | $7.75 — **byte-identical engine output to 1082570** (orientation-flip parity; catalog $8.00, same documented snap) | F8, F23×5 | no |
| 14 | **NEW (Session H)** — 3010701, Cut vinyl Cardinal Red, 49.16"×9.38", 3.202 sq ft (Band A) | `cut_vinyl` | $45.00 (Band A algorithmic: 3.202 × $13.795 mid-band = $44.17 → snap $45; catalog locked $44 — Band A has no MED template; documented divergence) | F15, F23×5 | no |

If a route doesn't match for any of these cases, the change is incorrect — either the change has a bug or the reference case needs explicit reconsideration with Nick before proceeding. Prices are documented for traceability; snap-rounding variance is tolerated where noted — routes, flags, and the report-only invariant (tier tables never mutated) are hard requirements.

**Note on flag counts:** F23 fires once per boundary that WOULD invert (report-only — the table is not modified). Multi-tier band templates cliff at all 5 boundaries by design, so F23×5 on a standard run is expected; the brief's invoice-protection section lists each boundary with its §26 resolution. F7 no longer fires on routine runs (briefs are band-anchored — a fire now means a genuine band deviation). F11 and F12 cannot fire (see §3). The W2/W3/W6 guards (F24 STOP, F21 reroute, F25 STOP) are additionally probed by the harness outside this table.
