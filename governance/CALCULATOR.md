# Calculator — Governance Reference

> **Authoritative reference for the Elliott calculator system.**
> The HTML calculator at `frontend/index.html` is the implementation; this document is the contract.
>
> Last Updated: 2026-06-05 (Session C — tier boundary constraint enforcement (F23), Band B/C cut vinyl routing, sub-0.1 production override, 1-9 auto-generation at 1.5×; Section 3 F23 added; Section 9 sanity matrix extended; Section 4 Rule 11 added)

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

- A deterministic pricing brief generator that reads `frontend/calculator_config.json` and `frontend/data.json`
- The input to **Round 1** of the `governance/PRICING_VALIDATION.md` 4-round AI validation process
- A consistency tool — re-running the same inputs always produces the same output
- A self-auditing surface — flags surface staleness, scope violations, missing profiles, margin floor breaches, MOQ language obligations, and known-unverified inputs

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
| `single_sub_scope` | Orajet 3951 | 0.1–0.5 sq ft | single | Printed/Laminated Singles (band-consistent, item excluded from band DATA POINTS) | No MOQ. Invoice protection (§26) applies at all tier boundaries. |
| `single_standard` | Orajet 3951 | > 0.5 sq ft | single | Printed/Laminated Singles | No MOQ. Invoice protection (§26) applies at all tier boundaries. |
| `no_profile` | Convex High Bond, Lexan/Polycarbonate, or any other | any | any | None | STOP — F17 fires, output suppressed, Required Inputs checklist shown |

### Sq Ft Thresholds (from `calculator_config.json` `routing`)

- `tiny_threshold_sq_ft`: **0.1** (≤ this → `tiny`)
- `sub_scope_floor_sq_ft`: **0.1**
- `sub_scope_ceiling_sq_ft`: **0.5** (0.1–0.5 → `single_sub_scope`)
- `singles_band_floor_sq_ft`: **0.5** (used in the band-scope F8 proximity flag)
- `singles_band_ceiling_sq_ft`: **2.0**
- `laminator_max_width_in`: **13.5** (narrow dim > 13.5 → F3 STOP)
- `roland_max_print_width_in`: **28.0**
- `parity_max_lam_passes`: **2** (kit lam passes > 2 → F16 REVIEW)
- `cut_vinyl_band_thresholds.band_b_floor_sq_ft`: **5.0** (sq ft ≥ this → Band B Large-Format)
- `cut_vinyl_band_thresholds.band_c_ceiling_sq_ft`: **1.0** (sq ft < this → Band C Sub-1 sq ft)

---

## 3. Flag Definitions (Canonical)

All 22 flag definitions live in `frontend/index.html` (calculator engine `FLAG_DEFS`). This is the canonical specification of each flag's severity, suppression behavior, and intent.

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
| F7 | REVIEW | no | Per-sq-ft rate outside band tolerance (±15%). Either complexity, new material, or repricing needed. |
| F8 | INFO | no | Item at low end of singles band scope — band-consistent pricing applies; small-label fixed cost premium acknowledged. |
| F9 | REVIEW | no | Tiny one-off (≤0.1 sq ft) — $55 flat program total, NOT a catalog rate. Per-sq-ft math is a minimum-run artifact. Do NOT benchmark. AI validation recommended (Rounds 1+2 minimum) for any tiny one-off. |
| F10 | REVIEW | no | Sub-scope single (0.1–0.5 sq ft) — below band scope. Excluded from band DATA POINTS until production-volume acceptance. |
| F11 | INFO | no | Never-pay-more cliff detected; engine auto-fixed lower tier(s) — review the adjusted tier table. |
| F12 | INFO | no | Ink cost is an UNVERIFIED placeholder ($0.25 flood coat). Realistic range $0.40–$0.60. Confirm after first production run and update `material_cost_per_unit`. |
| F13 | INFO | no | Color PMS caveat — visual approximation only; disclose in quote that this is not a certified Pantone match. |
| F14 | INFO | no | Alternate roll width available — efficiency scenario surfaced (do NOT pass savings to buyer; internal margin lever). |
| F15 | REVIEW | no | Rule 14 deviation: this item is benchmarked against a Relationship Concession band. AI consensus band is higher — document the strategic choice. |
| F16 | REVIEW | no | Kit requires >2 lamination passes — parity boundary exceeded; cost-build from scratch and run AI validation. |
| F17 | STOP | yes | No Pricing Profile band for this material family yet — first item establishes the band. Cost-build and run AI validation (all 4 rounds). |
| F18 | INFO | no | Printed/laminated MOQ 10 applies. Sub-10 orders billed at $55.00 flat minimum order charge. Required quote language must be included. |
| F19 | INFO | no | Cut vinyl item — printed/laminated MOQ 10 and $55 minimum order charge do NOT apply at this time. |
| F20 | STOP | yes | Cannot fit kit in ≤2 lam-pass orientation groups — exceeds current equipment routing. Requires Nick review (mixed-dim or special handling). |
| F21 | REVIEW | no | Mixed-dimension kit — per-label parity does NOT apply. Cost-build from scratch and run AI validation (Rounds 1+2 minimum). |
| F22 | INFO | no | Item below band — verify intentional. Smaller labels carry higher fixed cost per sq ft, not lower; below-scope position does NOT justify below-band $/sq ft. |
| F23 | INFO | no | Tier boundary auto-capped for never-pay-more compliance. One flag per boundary that fires; detail text identifies the boundary, the original price, and the capped price. |

### STOP Banner Behavior

When any STOP flag fires:

- The output panel shows a `⛔ Output blocked by STOP flag` banner at the top of the Flags section.
- The Volume Pricing Table is suppressed for `F3`, `F17`, and `F20`.
- F1 and F4 fire as STOP severity but do not suppress output — Nick can still see the price ladder but must clear the flag before proceeding to validation.

---

## 4. What the Calculator Must NOT Do (Canonical)

1. **It must NOT write to any file in `items/`, `categories/`, `materials/`, `governance/`, `.claude/`, or `frontend/data.json` / `frontend/materials.json`.** It is a read-only consumer of `calculator_config.json`, `data.json`, and `materials.json`. File writes are exclusively Claude Code's job, after Nick has approved the final price.

2. **It must NOT replace the 4-round AI validation process.** A calculator output is a Round 1 starting point. Rounds 2 (Destruction), 3 (Buyer Simulation), and 4 (Final Synthesis) still apply per `governance/PRICING_VALIDATION.md`. The "Ready for Round 1: YES/NO" badge on the Validation Brief section indicates the brief is structurally complete — not that the price is validated.

3. **It must NOT be quoted to the buyer.** The brief is internal scratch. Nick converts brief → quote email by hand or with another tool, applying judgment, override types, and account context. Calculator language ("route_reason", "single_sub_scope", "F10 REVIEW") does not appear in any buyer-facing artifact.

4. **It must NOT bypass `do_not_benchmark` filtering.** The comparable-items lookup must exclude every P/N in `CALCULATOR_CONFIG.do_not_benchmark`. Benchmarking against an outrigger-program peer (1277970–1278000), a standalone tiny one-off (3017583, 3017584), a sub-scope single before production-volume acceptance (1210810), or an initial-order job-economics price (1082570) is a structural error the calculator must prevent.

5. **It must NOT hardcode pricing constants.** All bands, tier ratios, snap granularity, ink rates, the $55 floor, the 13.5" laminator constraint, the 0.1/0.5/2.0 sq ft scope thresholds, the do-not-benchmark list, and the verified material costs come from `calculator_config.json`. The HTML carries the engine only. When a constant changes, regenerate the config via `scripts/build_calculator_config.py` — do not edit the HTML.

6. **It must NOT propagate stale material cost without flagging.** Every material in `material_constants` and `cut_vinyl_colors` carries a `verified_date`. The calculator computes `days_since(verified_date)` for each material consumed by the active route and fires F2 (>180 days) or F1 (>365 days). A stale cost without a flag is a Self-Healing Rule violation.

7. **It must NOT smooth over `do_not_benchmark` arithmetic.** Tiny-route output suppresses the per-label cost card in favor of a `.oneoff-block` showing "$55 program total / per-label suppressed" — the per-label is a minimum-run artifact, not a catalog rate. Never display tiny-route per-label numbers as if they were a real price.

8. **It must NOT skip never-pay-more verification.** Every adjacent tier pair (1-9→10-19, 10-19→20-49, 20-49→50-99, 50-99→100-199, 100-199→200+) is checked. If the total at the top of the lower tier exceeds the total at the bottom of the upper tier, the lower tier price is auto-capped.

9. **It must NOT invent a band for a material family that has none.** Convex High Bond + Poly Lam and Lexan/Polycarbonate both route to `no_profile` (F17 STOP). The first item in a new material family establishes the band — that requires a cost-build, all 4 validation rounds, and Nick's lock.

10. **It must NOT modify the band data for existing items, even if their tier table fails a cliff check.** The 4 cut vinyl items have cliffs at every tier boundary by design (no invoice protection rule on cut vinyl). The engine surfaces this as informational context only; the existing items' `categories/cut-vinyl-3m-180mc.md` band data is the source of truth.

11. **After every tier generation, `enforceTierBoundaries()` runs automatically.** Every tier table is guaranteed never-pay-more compliant before it reaches the output panel. The function walks boundaries bottom-up (200+ is the anchor; check 100-199→200+, then 50-99→100-199, etc.) and floor-caps any lower tier whose boundary total exceeds the upper tier's boundary total. Cascades — a capped tier becomes the upper for the next iteration. Runs after every tier builder (`buildPrintLamSinglesTiers`, `buildPrintLamKitTiers`, `buildCutVinylTiers`), BEFORE margin calculation. Does NOT run on `tiny` (all 6 tiers flat at $55) or `no_profile` (no tiers). Each cap fires one F23 INFO flag with boundary-specific detail text. The existing `checkInvoiceProtection()` function remains as a secondary verification step — it should report zero violations after `enforceTierBoundaries()` has run; if it ever finds a violation, that is a bug.

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
- Ink rates (low/medium/high/flood_coat/flood_coat_safety_red)
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
3. Commit `frontend/calculator_config.json` (regenerated) alongside the script change.

**No code change to `frontend/index.html` is required.** The HTML reads the config; the config is the source of truth for these values.

### 6.2 Material Cost Change — Update Material File + Re-Run

For changes to a material's `cost_per_sq_ft`, `cost_per_linear_yd`, or `verified_date`:

1. Edit the relevant `materials/*.md` file (frontmatter only).
2. Re-run all three build scripts:
   - `python scripts/build_frontend.py`
   - `python scripts/build_materials.py`
   - `python scripts/build_calculator_config.py`
3. Commit all three generated JSON files plus the materials file.

The calculator picks up the new cost dynamically — `build_calculator_config.py` reads `materials/*.md` frontmatter at build time and embeds the cost + verified_date into the config.

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
4. Test end-to-end with the existing sanity-check P/Ns:
   - 1230820 → `single_standard`, $20, F18 + F11
   - 1277970 → `tiny`, $55, F9 + F18
   - Convex High Bond → `no_profile`, F17 STOP
   - 5-label same-dim kit → `kit`, $50, F18
   - 1205720 → `cut_vinyl`, $35, F19 + F15
   - 1210810 → `single_sub_scope`, $4.50, F10 + F8 + F18

All routes must continue to produce correct routing badge, price ladder, MOQ row when applicable, band positioning visual, comparable items (filtered by do_not_benchmark), and a copyable validation brief.

---

## 7. Session Sequence — Adding a New Item Using the Calculator

The calculator slots into the existing new-item workflow at the front. The downstream sequence is unchanged.

### Step 1 — Spec Extraction (Pre-Calculator)

Run `governance/SPEC_EXTRACTION.md` extraction on the engineering PDF. Capture all 14 mandatory fields. The calculator requires width, height, label count, material family, item type, ink coverage (printed/lam), and cut vinyl color (cut vinyl) as a minimum.

### Step 2 — Calculator Run (Round 0 — Brief Generation)

1. Open `frontend/index.html`, click the **Calculator** tab.
2. Fill in the form fields. Optional fields (Part Number, Description, Model, Notes) can be skipped for an unassigned item.
3. Click **Run Calculator**.
4. Review the output panel:
   - **Routing & Summary** — confirm the route matches expectation (`single_standard`, `cut_vinyl`, etc.)
   - **Flags** — read every flag. STOP flags must be cleared before proceeding. REVIEW flags must be acknowledged in the validation prompt.
   - **Volume Pricing Table** — sanity-check the tier ladder. Note any never-pay-more auto-fix (F11).
   - **Material Cost Breakdown** — confirm the cost numbers match the bottom-up calculation. The breakdown text is verbatim what goes into the validation brief.
   - **Band Positioning** — confirm $/sq ft lands in the expected band. F7 fires if outside ±15% tolerance.
   - **Production Summary** — confirm lam passes and laminator fit.
   - **Validation Brief** — verify "Ready for Round 1" badge is YES. If NO, the brief is incomplete and Round 1 should not start.
5. Click **Copy Validation Brief**. The plain-text brief is now on the clipboard.

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

Nick composes the quote email by hand, using the calculator's quote-language stubs (anchor line + MOQ language + PMS caveat where applicable) as a starting point but applying judgment for account context, recent conversations, and the strategic framing this item needs. The calculator output is internal scratch — Sean never sees a route name, a flag ID, or a "validation brief" reference.

---

## 8. Files in the Calculator System

| File | Role | Source of Truth For |
|------|------|---------------------|
| `frontend/index.html` | Calculator engine + UI | Routing logic, flag firing logic, brief format, render output |
| `frontend/calculator_config.json` | Constants config (generated) | Band thresholds, tier ratios, ink rates, $55 floor, do_not_benchmark, quote language |
| `frontend/data.json` | Items database (generated) | Comparable items lookup, do_not_benchmark filtering |
| `frontend/materials.json` | Materials database (generated) | Material cost lookup (calculator uses calculator_config.json's embedded copy at runtime) |
| `scripts/build_calculator_config.py` | Build script | Generates `calculator_config.json` from governance + materials + items |
| `scripts/build_frontend.py` | Build script | Generates `data.json` |
| `scripts/build_materials.py` | Build script | Generates `materials.json` |
| `governance/CALCULATOR.md` | This file | The contract — what the calculator is, is not, and how to extend it |
| `governance/PRICING_VALIDATION.md` | Companion governance | The 4-round AI validation process the calculator feeds into |
| `governance/PRICING_RULES.md` | Companion governance | The constraints the calculator encodes (full bleed ink rule (§25), invoice protection (§26), file prep = $0 (§22-24)) |

---

## 9. Sanity Check Reference Cases

The reference cases below are the calculator's regression test surface. Any engine change must continue to produce the correct ROUTE for each case. With strict tier boundary enforcement (Rule 11), the calculator's algorithmic tier prices may differ from the catalog tier values stored in `items/*.md` — the calculator compresses tier tables aggressively to guarantee never-pay-more compliance, while the catalog tier tables retain cliffs that are handled by §26 invoice protection at billing time. The Price@20 column below documents the calculator's expected output, not the catalog price.

| Input | Route | Price@20 (calculator) | Required Flags | STOP? |
|-------|-------|---------:|---------------|:-----:|
| 1230820 — Orajet single, 15"×12.44", high ink | `single_standard` | ~$11.38 (algorithmic; anchor $20 capped by enforcement cascade from upper-tier ratios) | F23 (×5 boundaries), F7 | no |
| 1082570 — Orajet single, 10"×7.25", flood coat | `single_standard` | ~$4.39 (algorithmic; anchor $7.75 capped by cascade) | F8, F23 (×5), F7, F12 | no |
| 1210810 — Orajet single, 10.5"×4", flood Safety Red | `single_sub_scope` | ~$2.58 (algorithmic; anchor $4.50 capped by cascade) | F10 (REVIEW), F8, F22, F23 (×5), F7, F12 | no |
| 1278930 — Orajet 3-label kit, 11.13"×7.88" | `kit` | ~$18.64 (algorithmic; anchor $30 capped by cascade) | F23 (×5), F7 | no |
| 1245130 — Orajet 5-label kit, 11.13"×7.88" | `kit` | ~$31.07 (algorithmic; anchor $50 capped by cascade) | F23 (×5), F7 | no |
| 1205720 — Cut vinyl Cardinal Red, 33.5625"×11" (Band A) | `cut_vinyl` | ~$22.78 (algorithmic; anchor $35 capped by cascade) | F15 (Rule 14), F23 (×5), F7, F5 | no |
| 1277970 — Orajet single, 1.1875"×1.1875" (Ø1-3/16) | `tiny` | $55.00 (flat — enforcement does not run on tiny) | F9 (REVIEW) | no |
| Convex High Bond single, 10"×6" | `no_profile` | n/a (output suppressed) | F17 (STOP) | yes |
| **NEW** — 3010704 equivalent (Cut vinyl Cardinal Red, 70.8125"×14.375", 7.069 sq ft, Band B) | `cut_vinyl` | ~$53.85 (algorithmic; Band B template $78 capped by cascade) | F15, F23 (×5), F7, F5 | no |
| **NEW** — 3010707 equivalent (Cut vinyl Cardinal Red, 34.887"×4", 0.969 sq ft, Band C) | `cut_vinyl` | ~$11.89 (algorithmic; Band C template $20 capped by cascade) | F15, F23 (×5), F7 | no |
| **NEW** — Sub-0.1 sq ft production override (Orajet single, 8"×1.75", 0.0972 sq ft, `production_override: true`) | `single_sub_scope` | ~$0.76 (algorithmic; anchor $1.50 capped by cascade) | F10, F8, F22, F23 (×5), F7, F12 | no |

If a route doesn't match for any of these cases, the change is incorrect — either the change has a bug or the reference case needs explicit reconsideration with Nick before proceeding. Prices are documented for traceability but the spec explicitly tolerates snap-rounding variance — only routes are hard requirements.

**Note on flag counts:** F23 fires once per boundary that is auto-capped. On any tier table whose template has cliffs at all 5 boundaries (Band A/B/C templates with 1.5×/1.2×/1.0×/0.85×/0.7×/0.55× compression do), F23 fires 5 times. This is by design and documented in the brief output. F11 no longer fires on routine cliff fixes — `enforceTierBoundaries()` handles cliffs upstream, so `checkInvoiceProtection()` finds zero violations and does not run its 10-19 autofix path.
