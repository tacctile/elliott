# Deep-Tier Chain-Consistency Audit — Orajet + Cut Vinyl

**Date:** 2026-07-16
**Scope:** `categories/printed-laminated-orajet.md` + all 41 `items/*.md` in the Orajet 3951 Cast + Polyester Lam family; `categories/cut-vinyl-3m-180mc.md` + all 15 `items/*.md` in the 3M 180mC Cut Vinyl family. All 57 item files in these two families were read (frontmatter + pricing derivation + notes). Convex High Bond + Polycarbonate (`items/3017557.md`) was **not** read for testing purposes — held out per the prior session's insufficient-sample call.
**Files modified:** none. This is a read-only audit.
**Reasoning effort:** increased, per request.

---

## 1. Method

### 1.1 The hypothesis, tested exactly as specified

> At every tier (1-9, 10-19, 20-49, 50-99, 100-199, 200+), does each item's $/sq ft hold **at or above its nearest smaller-sq-ft neighbor's** $/sq ft, at that same tier?

Concretely: sort the independently-tested items in a family by sq ft, ascending. For every adjacent pair, let **S** = the smaller-sq-ft item, **L** = the larger-sq-ft item (its nearest smaller neighbor is S). At each of the six tiers, check `L.$/sqft ≥ S.$/sqft`. This is **Direction A** below.

This direction was tested first, literally, with no adjustment — see §3.2 and §4.2. It fails at a majority of tier-pairs in both families, and the reason is structural, not accidental: both categories are deliberately built on a **small-format premium** — smaller items are priced at a *higher* $/sq ft than larger ones (explicitly, e.g. footnote ² on `1210810`: *"A smaller label must carry equal or higher $/sq ft than a larger label at the same tier"*). Under that design, $/sq ft is expected to **fall** as sq ft rises, so `L ≥ S` (a larger item priced at or above a smaller one) is the atypical case, not the norm — Direction A mostly fails by design, and the docs' own "root benchmark exemption" is simply the largest, most visible instance of that same pattern (§3.2).

Because a literal reading of Direction A mostly just re-detects the account's own small-format-premium design rather than surfacing errors, this audit **also** runs the mirror-image check that the account's own governance actually asserts (Direction B: S.$/sqft ≥ L.$/sqft — the smaller item must not be *cheaper* per sq ft than its larger neighbor). Both directions are reported in full. Direction B is what §7 proposes as the standing constraint, because it is what the account's own Wave 4 verdicts and §31 floor doctrine already claim to enforce — this audit checks whether that claim holds at all six tiers, not just qty 20 (the only tier the account's own validation waves routinely check).

### 1.2 Inclusion: "independently-validated" items

Per the task's instruction, direct-parity clones are excluded because they inherit pricing rather than test it. The account's governance uses the literal term **"Direct Parity Exemption / Direct parity clone"** for eight items; this audit also extends the same *principle* ("inherits rather than tests") to four further patterns found in the files, all disclosed below so the classification is auditable rather than assumed:

- **"Color parity" clones** (cut vinyl) — identical dimensions, identical tier table, price fixed to a sibling P/N's material cost, "not separately validated" — functionally the same act as a Direct Parity clone, just a different governance label.
- **"Sq ft parity" / "Direct sq ft parity"** clones (cut vinyl) — item files that say verbatim *"AI Validation: Not separately run... direct parity with an accepted item at the same sq ft."*
- **Verbatim floor-governed tier-table copies** (Orajet) — items priced with **no AI validation run** whose six-tier ladder is copied exactly from another item's floor anchor, and whose own file explicitly disclaims the resulting $/sq ft as "a mathematical artifact... NOT a pricing rate, never use as a benchmark."
- **Owner Judgment ladder adoption** (Orajet, one item) — tier table adopted verbatim from another item "by Nick's direction," explicitly "No AI validation waves run on this item."

Kits (multi-label, priced per-kit not per-label-sq-ft) and one-off job-economics items (explicitly flagged in their own files as "DO NOT BENCHMARK" / "arithmetic artifact only," priced flat from labor floor, not sq ft) were read but are **excluded** from the chain test — they are not testing the same $/sq ft scaling logic the hypothesis is about, and the account's own docs forbid using them as $/sq ft references.

**All 57 items were read.** The full accounting:

| Family | Total items | Independently-tested (chain-check set) | Excluded — parity/inherited | Excluded — kit | Excluded — one-off job economics |
|---|---|---|---|---|---|
| Orajet | 41 | **20** | 12 | 3 | 6 |
| Cut vinyl | 15 | **8** | 7 | 0 | 0 |
| Convex/polycarbonate | 1 | — (out of scope, prior session) | — | — | — |

**Orajet exclusions (12 parity/inherited):**

| P/N | Excluded as | Inherits from |
|---|---|---|
| 1068270 | Direct Parity Exemption (literal) | 1082570 |
| 1062390 | Direct Parity Exemption (literal) | 1068270 |
| 1132950 | Direct Parity Exemption (literal) | 1068270 |
| 1278220 | Direct Parity Exemption (literal) | 1279000 |
| 1277300 | Direct Parity Exemption (literal) | 1278980 |
| 1279020 | Direct Parity Exemption (literal) | 1278980 |
| 3020336 | Direct Parity Exemption (literal) | 3020335 |
| 3020482 | Direct Parity Exemption (literal) | 3020335 |
| 1205870 | Verbatim floor-table copy, no AI validation | 3024140 |
| 1279260 | Verbatim floor-table copy, no AI validation; own file: "$83.33/sq ft... is NOT a pricing rate" | 3024592 |
| 1279270 | Verbatim floor-table copy, no AI validation; identical to 1279260 | 3024592 |
| 3020370 | Owner Judgment — ladder adopted verbatim, "No AI validation waves run" | 1247120 |

**Orajet kits (3, excluded — kit $/sq ft is a per-kit rate carrying an intentional ~6% kit premium, not comparable to single-label scaling):** 1278890, 1278930, 1245130.
**Orajet one-offs (6, excluded — job-economics pricing, explicitly non-benchmarkable):** 1277970, 1277980, 1277990, 1278000, 3017583, 3017584.

**Cut vinyl exclusions (7 parity/inherited):**

| P/N | Excluded as | Inherits from |
|---|---|---|
| 1186310 | "Direct sq ft parity... Not separately run" | 1205720 |
| 3017435 | "Direct parity with an accepted item at the same sq ft. No ambiguity." | 1205720 |
| 3018378 | "Direct sq ft parity... Not separately run" | 1205720 |
| 3010708 | "Color-parity pricing" | 3010707 |
| 3010709 | "Color-parity pricing" | 3010707 |
| 3010723 | "Color parity with P/N 3010722... identical pricing" | 3010722 |
| 3010724 | "Color parity with P/N 3010722... identical pricing" | 3010722 |

**Notable side-finding:** the category page markets the "~2.51–2.56 sq ft cluster" (1205720, 1186310, 3017435, 3018378) as four converging data points confirming the Band A rate, and Band C (3010707/3010708/3010709) as "three founding data points." Once clones are excluded, **each of those is actually one independently-tested item wearing three price tags.** This doesn't make the price wrong (color/geometry-parity pricing is legitimate and clearly disclosed in each clone's own file), but it means the account's confidence narrative overstates its own sample size — 4 "data points" is 1, and 3 "founding data points" is 1.

---

## 2. Full dataset — $/sq ft at every tier, sorted by sq ft

### 2.1 Orajet — 20 independently-tested items

| P/N | Description | Sq Ft | $/sqft 1-9 | $/sqft 10-19 | $/sqft 20-49 | $/sqft 50-99 | $/sqft 100-199 | $/sqft 200+ |
|---|---|---|---|---|---|---|---|---|
| 3024140 | LBL-WRK LGHTS | 0.019 | $210.53 | $157.89 | $131.58 | $118.42 | $105.26 | $92.11 |
| 3024592 | LBL-FALL PRTCT ANCHRG 1 PERSON | 0.054 | $78.70 | $60.19 | $50.93 | $46.30 | $41.67 | $37.04 |
| 1012080 | LABEL, PTE SINGLE STICK CONTROLLER | 0.077 | $48.70 | $37.66 | $32.47 | $28.57 | $25.32 | $24.68 |
| 1279000 | LBL-MAX PLTF CAP 1200 TIP HZRD | 0.097 | $46.39 | $36.08 | $30.93 | $26.80 | $23.71 | $21.65 |
| 1247120 | LBL-DNGR TIP-OVER HAZARD | 0.122 | $34.84 | $26.64 | $22.54 | $18.44 | $16.39 | $14.34 |
| 3020477 | LBL-MODULAR BOOM CONTROL | 0.130 | $32.69 | $25.00 | $21.15 | $17.31 | $15.38 | $13.46 |
| 1101250 | LBL-DNGR MAX PLAT. 2100 | 0.132 | $30.30 | $22.73 | $17.05 | $13.26 | $11.36 | $9.47 |
| 1279130 | LBL-MOVING OR WARNING E-SERIES | 0.148 | $32.09 | $23.65 | $20.95 | $17.23 | $15.54 | $13.51 |
| 3018808 | LBL-GREER SETUP INST | 0.222 | $31.53 | $24.77 | $18.02 | $16.89 | $16.89 | $16.89 |
| 1001220 | DANGER ELECTROCUTION HAZARD | 0.231 | $30.30 | $23.81 | $17.32 | $16.23 | $16.23 | $16.23 |
| 1210810 | LBL - DANGER FALLING JIB | 0.292 | $24.83 | $19.69 | $16.27 | $13.70 | $11.99 | $9.42 |
| 3017572 | LBL - HYDAC VLV OVERRIDE | 0.365 | $23.97 | $19.86 | $16.44 | $15.75 | $15.07 | $14.38 |
| 3024595 | LBL-DNGR TIP, ELEC, CRUSH | 0.488 | $22.03 | $18.95 | $15.88 | $15.88 | $15.88 | $15.88 |
| 1073950 | CHART-TOP MOUNT JIB 500# | 0.503 | $32.80 | $20.87 | $15.90 | $12.43 | $10.44 | $8.45 |
| 1082570 | Load Chart, I70 EZR Mount 3.6K | 0.503 | $32.80 | $20.87 | $15.90 | $12.43 | $10.44 | $8.45 |
| 1267140 | *(blank on drawing)* | 0.560 | $23.21 | $18.75 | $15.62 | $13.39 | $12.95 | $11.61 |
| 1278980 | LABEL-PLTFM RANGE CAPACITY CHART E160 V3 | 0.609 | $23.81 | $18.88 | $15.60 | $13.55 | $12.32 | $11.08 |
| 3020335 | E145 - LOWER TERMINAL STRIP BOX | 0.625 | $23.20 | $19.20 | $15.60 | $13.60 | $12.40 | $11.20 |
| 1277020 | CHRT-D100i FG PLTF | 0.635 | $22.83 | $18.90 | $15.75 | $13.39 | $12.60 | $11.42 |
| **1230820** | **Load Chart, Model D105 (root benchmark, FA Accepted)** | **1.296** | $23.15 | $18.52 | **$15.43** | $13.12 | $10.80 | $8.49 |

### 2.2 Cut vinyl — 8 independently-tested items

| P/N | Description | Sq Ft | $/sqft 1-9 | $/sqft 10-19 | $/sqft 20-49 | $/sqft 50-99 | $/sqft 100-199 | $/sqft 200+ |
|---|---|---|---|---|---|---|---|---|
| 3010707 | ElliottEquip.com Wordmark — Cardinal Red (Band C) | 0.969 | $28.90 | $24.77 | $20.64 | $17.03 | $13.93 | $11.87 |
| 3010736 | LBL-I50 MED WHT | 1.012 | $19.52 | $17.05 | $14.33 | $13.34 | $13.09 | $12.85 |
| 3010722 | G50 - CARDINAL RED | 1.167 | $18.85 | $16.50 | $14.35 | $13.07 | $12.64 | $12.43 |
| 3010698 | LBL-ELLIOTT SML RED | 1.582 | $18.02 | $15.64 | $13.91 | $12.33 | $10.90 | $9.48 |
| **1205720** | **E190 Cardinal Red (Band A root, FA Accepted)** | **2.560** | $17.58 | $15.62 | **$13.67** | $11.72 | $10.16 | $8.59 |
| 1146650 | 40142 Cardinal Red Model Designation | 2.971 | $17.50 | $15.65 | $13.72 | $11.95 | $10.27 | $8.92 |
| 3010701 | LBL-ELLIOTT MED RD | 3.202 | $17.80 | $15.62 | $13.74 | $13.12 | $12.49 | $12.18 |
| 3010704 | LBL-ELLIOTT LRG RED (Band B, sole point) | 7.069 | $14.85 | $13.01 | $11.03 | $9.62 | $8.49 | $7.36 |

---

## 3. Orajet — chain-check results

### 3.1 Direction A (literal): does the larger item hold at or above its nearest smaller neighbor?

19 adjacent pairs × 6 tiers = **114 tier-tests. 73 violate (64.0%), 41 hold (36.0%).** Only two of the 19 pairs hold cleanly at all six tiers: the exact 0.503-sq-ft tie (1073950 ↔ 1082570, byte-identical tables) and 0.132→0.148 (1101250→1279130 — see §3.3, this "hold" under Direction A is itself the flag, because it means 1279130 is *not* cheaper than the smaller 1101250; see below).

The **root benchmark's known exemption is real and correctly identified — but it is one of 73, not one of one.** 1230820 (1.296 sq ft, $15.43/sq ft at qty 20) fails Direction A against its nearest smaller neighbor, 1277020 (0.635 sq ft, $15.75/sq ft), at 5 of 6 tiers (all but 1-9). That is exactly the exemption the account's own footnote ²⁰ gestures at ("staying above the 1.296 sq ft root benchmark floor" while 1277020 sits above it). But the same failure mode — a larger item settling below its immediately-smaller neighbor's $/sq ft — recurs at 15 of the other 18 pairs too, because it is the *designed* behavior of a small-format-premium curve, not a one-off. Examples: 3024140→3024592 fails at all 6 tiers ($210.53 → $78.70 at 1-9); 1210810→3017572 fails at 5 of 6; 1082570→1267140 fails at 3 of 6. **Direction A, taken literally, is not a useful error-detector for this pricing model** — it mostly just re-confirms that small-format premium pricing is doing what it was designed to do. It is documented here in full because the task asked for it explicitly, not because it is the more informative test — see §3.2 vs §3.3.

### 3.2 Direction B (the account's own stated rule): does the smaller item hold at or above its larger neighbor?

This is the rule the account's own governance actually asserts (footnote ², Wave 4: *"a smaller label must carry equal or higher $/sq ft than a larger label"*; §31: the root floor "applies at every quantity tier... not just the qty-20 rate"). Testing it at all six tiers — not just qty 20, which is the only tier the account's own validation waves routinely check — gives:

**114 tier-tests. 35 violate (30.7%), 79 hold (69.3%).**

Filtering out sub-1%/sub-$0.10 rounding noise, the **material** (>2% or >$0.10/sq ft) violations are:

| Smaller (S) | Larger (L) | Tiers violated | Worst gap | Documented as an accepted exception? |
|---|---|---|---|---|
| **1101250** (0.132, $2.25@20) | **1279130** (0.148, $3.10@20) | **All 6 tiers** | 200+: $9.47 vs $13.51/sq ft (**+42.7%**) | **No.** 1279130 was validated 2026-06-22 against 1247120/1210810 only; 1101250 was validated 2026-07-14 against 1230820 only ("P/N 1210810 is explicitly NOT used as a benchmark"). Neither validation record checked the other, despite sitting only 0.016 sq ft apart. This is the single clearest, largest, entirely undocumented inversion in the family. |
| **1210810** (0.292, $4.75@20) | **3017572** (0.365, $6.00@20) | 5 of 6 (all but 1-9) | 200+: $9.42 vs $14.38/sq ft (**+52.7%**) | No. 3017572's governing comparable is 3024595 only; 1210810 (the nearer smaller neighbor at the time) is not checked. |
| **1082570 / 1068270-family** (0.503) | **1267140** (0.560, $8.75@20) | 3 of 6 (50-99 through 200+) | 200+: $8.45 vs $11.61/sq ft (+37.4%) | No — 1267140's own footnote ⁶ raised its 200+ tier specifically to avoid falling below the *band floor*, but never checked it against the 0.503-position deep tiers directly. |
| **3024595** (0.488, $7.75@20) | **1073950/1082570** (0.503, $8.00@20) | 1-9, 10-19 (20-49 is a $0.02/sq ft rounding artifact) | 1-9: $22.03 vs $32.80/sq ft (**+48.9%**) | Partially explainable, not documented: 3024595 carries a **flat** ladder (§31 floor doctrine forces $7.75 at every tier from 20-49 up, so its 1-9/10-19 are compressed relative to a normal declining ladder); 1073950/1082570 use a normal steep ladder. The two tier-shaping philosophies were never reconciled against each other. |
| **3020335** (0.625, $9.75@20) | **1277020** (0.635, $10.00@20) | 20-49, 100-199, 200+ | 200+: $11.20 vs $11.42/sq ft (+1.9%) | **Yes** — this is the account's own documented exception (footnote ²⁰): "breaks strict $/sq ft monotonicity-by-size at this one point in the gradient — documented here as an accepted exception, not an error." |
| 1278980→3020335, 1267140→1278980, 3017572→3024595 | | scattered, ≤$0.32/sqft | | Sub-2% noise around adjacent 0.5–0.65 sq ft cluster boundaries; not economically material. |

**Bottom line for Orajet:** the account's own claimed chain rule ("smaller ≥ larger, always") holds at qty 20 almost everywhere it was actually checked. It **breaks down materially at the deep tiers (100-199, 200+)** in three places the account has never validated against each other (1101250↔1279130, 1210810↔3017572, 1082570-family↔1267140) — because each item's tier-compression ratio (how steeply price falls from 1-9 to 200+) was chosen independently per-item, and nobody re-checked that the resulting deep-tier numbers still respect the neighbor ordering established at qty 20. 1101250↔1279130 is the standout: a **flat, undocumented, 22.9%–42.7% inversion across every volume tier**, not a rounding artifact and not a disclosed exception.

### 3.3 Sq ft gaps in the tested Orajet chain

| Gap (sq ft) | Between | |
|---|---|---|
| **0.661** | **1277020 (0.635) → 1230820 (1.296)** | **The largest gap in the family — flagged explicitly by the task.** Nothing independently tested exists between 0.635 and 1.296 sq ft. (3020335/3020336/3020482 sit at 0.625, still below the gap; the kits 1278890/1278930 sit at a *kit* sq ft of 1.218 but are excluded as a different pricing basis — see §1.2.) |
| 0.123 | 3017572 (0.365) → 3024595 (0.488) | |
| 0.074 | 1279130 (0.148) → 3018808 (0.222) | |
| 0.073 | 1210810 (0.292) → 3017572 (0.365) | |
| 0.061 | 1001220 (0.231) → 1210810 (0.292) | |
| 0.057 | 1082570 (0.503) → 1267140 (0.560) | |
| 0.049 | 1267140 (0.560) → 1278980 (0.609) | |
| ≤0.035 | (remaining 12 gaps, all sub-scope/singles-band interior points) | densely tested |

**Tested range: 0.019 – 1.296 sq ft.** Below 0.019 or above 1.296, there is no independently-validated Orajet single-label data point at all — the tiny one-off items (down to 0.00174 sq ft) are explicitly non-benchmarkable job-economics pricing, not $/sq ft data.

---

## 4. Cut vinyl — chain-check results

### 4.1 Direction A (literal)

7 adjacent pairs × 6 tiers = **42 tier-tests. 30 violate (71.4%), 12 hold.** Same structural cause as Orajet — Band A/B/C are explicitly designed with a 51% $/sq ft step-up from Band A to Band C and a 19.3% step-down from Band A to Band B (both documented, intentional), so a literal "larger ≥ smaller neighbor" test fails constantly by design. Not a distinct finding from §3.1; not re-tabulated pair-by-pair here for brevity — full detail available on request, same computation method as §3.1.

### 4.2 Direction B (account's stated rule)

**42 tier-tests. 12 violate (28.6%), 30 hold.** Material (>2%/>$0.10) violations:

| Smaller | Larger | Tiers violated | Worst gap | Documented? |
|---|---|---|---|---|
| **1205720** (2.560, Band A root, $35@20) | **1146650** (2.971, $40.75@20) | 5 of 6 (10-19 through 200+) | 200+: $8.59 vs $8.92/sq ft (+3.8%) | **No — contradicted.** The category page states outright: *"$40.75 at qty 20 = $13.72/sq ft — inside the concession-phase band and between both neighboring anchors, **no size/price inversion**."* That claim is true at qty 20 only (13.67 vs 13.72, a 0.4% rounding-level gap, immaterial). It is **not checked, and does not hold**, at 50-99 (+2.0%), 100-199 (+1.1%), and 200+ (+3.8%) — a genuine, if modest, deep-tier inversion the account's own text asserts doesn't exist. |
| **1146650** (2.971, $40.75@20) | **3010701** (3.202, $44@20) | 1-9, 50-99, 100-199, 200+ | 200+: $8.92 vs $12.18/sq ft (**+36.6%**) | No. 3010701 was validated 2026-06-09, before 1146650 existed (2026-07-14) — 1146650's own validation record checked it against the 2.51–2.56 cluster and 3010701, and found "no size/price inversion" **at qty 20** (13.72 vs 13.74, immaterial) — but 3010701's own deep tiers were deliberately held flat-ish for Band B separation (200+ at $12.18/sq ft vs a normal declining curve), and nobody re-checked that against 1146650's steeper decline. Same pattern as the Orajet 3024595 case (§3.2): two different tier-compression philosophies colliding at a boundary, unvalidated. |
| 3010707 → 3010736 | — | 200+ only | $11.87 vs $12.85/sq ft (+8.2%) | Band C → Band A boundary; this is the crossing the account's own docs single out as "the closest-to-Band-C-boundary" transition and 4-wave validated the qty-20 rate specifically for it — but the 200+ tier was not part of that comparison. Minor. |

3010722→3010698 and 3010698→1205720 hold cleanly at all six tiers.

### 4.3 Sq ft gaps and untested ranges

| Gap (sq ft) | Between | |
|---|---|---|
| **3.867** | **3010701 (3.202) → 3010704 (7.069)** | **This is cut vinyl's equivalent of the Orajet 0.635–1.296 gap — larger, in fact.** Band B (5+ sq ft) rests on a **single confirmed data point** (3010704 at 7.069 sq ft); the entire 3.2–5.0 sq ft range and the entire 5.0–7.0 sq ft range are unvalidated, and there is nothing at all above 7.069 sq ft. The category doc itself flags this ("Band width: Single data point... will tighten as additional large-format items are quoted"), so this gap is *known* to the account, just not previously framed as a chain-consistency gap. |
| 0.978 | 3010698 (1.582) → 1205720 (2.560) | Documented in the account's own text as "the 1.5–2.5 sq ft interior gap zone" — 3010698 is its sole founding point. |
| 0.415 | 3010722 (1.167) → 3010698 (1.582) | |
| 0.411 | 1205720 (2.560) → 1146650 (2.971) | |
| 0.231 | 1146650 (2.971) → 3010701 (3.202) | |
| 0.155 | 3010736 (1.012) → 3010722 (1.167) | |
| 0.043 | 3010707 (0.969) → 3010736 (1.012) | |

**Tested range: 0.969 – 7.069 sq ft.** Below 0.969 sq ft, there is **no cut-vinyl data at any sq ft** — not even a single point (unlike Orajet, which has tested data down to 0.019 sq ft). The category's own Decision Tree already requires 4-wave validation for anything below ~1.0 sq ft (Band C threshold) or between 4.5–5.5 sq ft (Band B boundary) — this audit confirms those cautions are warranted and, for the sub-0.969 sq ft range, actually understated (there is no floor data down there at all, whereas Orajet has floor data all the way to 0.019 sq ft).

---

## 5. Answering the specific questions asked

1. **Root benchmark's known exemption — confirmed, and not the only one.** Under the literal hypothesis (Direction A), 1230820 fails against 1277020 at 5/6 tiers — real, matches the account's own framing. But 72 other tier-tests fail the same literal check elsewhere in Orajet (64.0% overall), and 29 more in cut vinyl (71.4%), because Direction A is structurally opposed to the account's own small-format-premium pricing design. It is not a rare exemption; it is the norm under a literal reading. The account's own actually-intended rule runs the other direction (§1.1) — under that direction (Direction B), 1230820 vs 1277020 isn't a violation at all (§3.2), and the real, previously-undocumented violations are the ones catalogued in §3.2/§4.2.
2. **0.635–1.296 sq ft Orajet gap** — confirmed, and it is the largest gap in the tested Orajet chain (0.661 sq ft, §3.3).
3. **Equivalent cut-vinyl gap** — confirmed and larger in absolute terms: 3.202–7.069 sq ft (3.867 sq ft, §4.3), where Band B's entire large-format range rests on one point.

---

## 6. What "holds" vs "violates" means here, in one table

| | Direction A (literal: larger ≥ nearest smaller neighbor) | Direction B (account's stated rule: smaller ≥ nearest larger neighbor) |
|---|---|---|
| Orajet | 41/114 hold (36.0%) | 79/114 hold (69.3%) |
| Cut vinyl | 12/42 hold (28.6%) | 30/42 hold (71.4%) |
| What a "violation" means | Expected — small-format premium working as designed | A genuine deep-tier neighbor-ordering break, mostly undocumented |

---

## 7. Proposed constraint (not a ratio formula)

**The chain-check that should actually govern future pricing:** for any two independently-validated items in the same material family, if item S has a smaller sq ft than item L, then at **every** tier (not just qty 20), S's $/sq ft must be **at or above** L's $/sq ft — a nearest-neighbor floor, re-checked at all six tiers, applied against the item's immediate neighbors on both sides (not just against the single root benchmark, and not just at the tier the item happened to be validated at).

This is exactly the account's own documented Wave 4 rule (§1.1) — the contribution of this audit is establishing that it has only ever actually been checked at qty 20, and proposing it be checked at all six tiers going forward, since §3.2/§4.2 show that's where it actually breaks.

**Tested range — do not extrapolate outside these bounds:**

| Family | Constraint verified between | Unverified below | Unverified above |
|---|---|---|---|
| Orajet | **0.019 – 1.296 sq ft** | — (floor data exists down to 0.019) | Anything > 1.296 sq ft — no data point exists above the root benchmark |
| Cut vinyl | **0.969 – 7.069 sq ft** | Anything < 0.969 sq ft — **no data at any size**, not even one point | Anything > 7.069 sq ft — Band B is a single point; treat 3.202–7.069 as effectively unverified interior too |

Any new item outside these bounds needs its own validation pass; any new item *inside* these bounds should be checked against its actual nearest neighbors at all six tiers before filing, not just at qty 20.

---

## 8. Held out of scope (per prior session)

Convex High Bond + Polycarbonate (`categories/convex-high-bond-polycarbonate.md`, 1 item file — `3017557`) — insufficient sample (single item), not read for chain-testing purposes in this audit, consistent with the prior session's determination.

---

## 9. Override/status trace for every violating pair (Direction A, §3.1/§4.1)

Appended per follow-up request. This does not change any finding above — it adds the frontmatter `override_type` and `status` for both items in every pair that fails the literal hypothesis (Direction A: larger item L's $/sq ft < smaller neighbor S's $/sq ft, at one or more tiers) at 17/19 Orajet pairs and 7/7 cut-vinyl pairs.

**Caveat on reading `override_type`:** the field records whether *that item's own price* carries a logged override (e.g. `One-Time Exception` on a below-floor deep tier, `Relationship Concession` on a qty-20 anchor, `Owner Judgment` on a ladder adopted without AI validation) — it is **not** a per-pair field and does not mean the account ever logged *this specific neighbor comparison* as a reviewed exception. A blank `override_type` on both sides of a pair means the pair's violation has no exception trail anywhere in the frontmatter — i.e. it was never flagged, reviewed, or accepted; it is simply present in the data. A non-blank `override_type` on one side means that item's price was deliberately overridden for *some* documented reason, which may or may not be the reason it also produces this chain violation (see per-pair notes in §3.2/§4.2 for the cases where the connection is direct, e.g. 3020335→1277020).

### Orajet (17 violating pairs of 19)

| Smaller item (S) | S sq ft | S status | S override_type | Larger item (L) | L sq ft | L status | L override_type | Tiers where L < S |
|---|---|---|---|---|---|---|---|---|
| 3024140 | 0.019 | Quoted | — | 3024592 | 0.054 | Quoted | — | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |
| 3024592 | 0.054 | Quoted | — | 1012080 | 0.077 | Quoted | — | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |
| 1012080 | 0.077 | Quoted | — | 1279000 | 0.097 | Quoted | — | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |
| 1279000 | 0.097 | Quoted | — | 1247120 | 0.122 | Quoted | — | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |
| 1247120 | 0.122 | Quoted | — | 3020477 | 0.130 | Quoted | — | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |
| 3020477 | 0.130 | Quoted | — | 1101250 | 0.132 | Quoted | **One-Time Exception** | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |
| 1279130 | 0.148 | Quoted | — | 3018808 | 0.222 | Quoted | — | 1-9, 20-49, 50-99 |
| 3018808 | 0.222 | Quoted | — | 1001220 | 0.231 | Quoted | — | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |
| 1001220 | 0.231 | Quoted | — | 1210810 | 0.292 | Quoted | — | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |
| 1210810 | 0.292 | Quoted | — | 3017572 | 0.365 | Quoted | **One-Time Exception** | 1-9 |
| 3017572 | 0.365 | Quoted | **One-Time Exception** | 3024595 | 0.488 | Quoted | — | 1-9, 10-19, 20-49 |
| 3024595 | 0.488 | Quoted | — | 1073950 | 0.503 | Quoted | — | 50-99, 100-199, 200+ |
| 1082570 | 0.503 | Quoted | — | 1267140 | 0.560 | Quoted | — | 1-9, 10-19, 20-49 |
| 1267140 | 0.560 | Quoted | — | 1278980 | 0.609 | Quoted | — | 20-49, 100-199, 200+ |
| 1278980 | 0.609 | Quoted | — | 3020335 | 0.625 | Quoted | — | 1-9 |
| 3020335 | 0.625 | Quoted | — | 1277020 | 0.635 | Quoted | — | 1-9, 10-19, 50-99 |
| 1277020 | 0.635 | Quoted | — | 1230820 | 1.296 | **FA Accepted** | — | 10-19, 20-49, 50-99, 100-199, 200+ |

**14 of these 17 pairs have `—` (blank) `override_type` on *both* sides** — no exception trail at all in the frontmatter for either item. The remaining 3 (3020477↔1101250, 1210810↔3017572, 3017572↔3024595) each touch one of the two Orajet items carrying a `One-Time Exception` flag (1101250, 3017572) — both flags are about those items' own deep-tier floor overrides (§31), not a logged review of these specific neighbor pairs.

### Cut vinyl (7 violating pairs of 7)

| Smaller item (S) | S sq ft | S status | S override_type | Larger item (L) | L sq ft | L status | L override_type | Tiers where L < S |
|---|---|---|---|---|---|---|---|---|
| 3010707 | 0.969 | Quoted | — | 3010736 | 1.012 | Quoted | — | 1-9, 10-19, 20-49, 50-99, 100-199 |
| 3010736 | 1.012 | Quoted | — | 3010722 | 1.167 | Quoted | — | 1-9, 10-19, 50-99, 100-199, 200+ |
| 3010722 | 1.167 | Quoted | — | 3010698 | 1.582 | Quoted | — | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |
| 3010698 | 1.582 | Quoted | — | 1205720 | 2.560 | **FA Accepted** | **Relationship Concession** | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |
| 1205720 | 2.560 | **FA Accepted** | **Relationship Concession** | 1146650 | 2.971 | Quoted | **Owner Judgment** | 1-9 |
| 1146650 | 2.971 | Quoted | **Owner Judgment** | 3010701 | 3.202 | Quoted | — | 10-19 |
| 3010701 | 3.202 | Quoted | — | 3010704 | 7.069 | Quoted | — | 1-9, 10-19, 20-49, 50-99, 100-199, 200+ |

**4 of these 7 pairs have `—` on both sides** (3010707↔3010736, 3010736↔3010722, 3010722↔3010698, 3010701↔3010704) — no exception trail. The other 3 touch 1205720 (`Relationship Concession` — the deliberate below-consensus root anchor, §1205720's own record) or 1146650 (`Owner Judgment` — only on its 1-9/10-19 tiers, per its own file) on one side; neither override was logged as a review of the specific neighbor-pair violation shown here.

**Rollup:** 18 of the 24 violating pairs across both families (14 Orajet + 4 cut vinyl) have zero override trail on either item — the chain-check flags them, but nothing in the account's own records shows anyone ever checked, flagged, or accepted that specific comparison. The remaining 6 pairs each touch at least one item that carries *some* documented override, but in every case that override was granted for a different, narrower reason (a below-floor deep-tier exception, a root-anchor concession, a skipped-validation ladder adoption) than "this neighbor pair is consistent" — so even those 6 should be read as override-adjacent, not override-explained.
