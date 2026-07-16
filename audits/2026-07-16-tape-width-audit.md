# Cut-Vinyl Application Tape Width Audit

**Date:** 2026-07-16
**Scope:** All 16 `items/*.md` files with `material_family: "3M 180mC Cut Vinyl"`.
**Trigger:** P/N 3023921 (LABEL D100i) produced a $undefined/yd -> $NaN material cost in its calculator Round 1 brief because no Combinations row paired its vinyl color (Cardinal Red, 24" roll) with the 30" application tape the session brief specified. Root cause and engine fix are documented in `governance/PRICING_RULES.md` §33 and `governance/CALCULATOR.md` (flag F28). This audit is the companion check requested alongside that fix: does any *other* filed cut-vinyl item have the same latent problem — a label whose across-roll (narrow) dimension exceeds the width of the application tape roll it's actually priced against — even if it never threw an error at the time it was priced?
**Files modified:** none. This is a read-only audit.

---

## Method

For each item, two figures were pulled directly from the item's own "Material Specification" / "Nesting and Material Cost" prose (not re-derived): the label's narrow (across-roll) dimension — the dimension the item's own notes use for vinyl nesting ("labels across the roll") — and the width of the TransferRite 582U application tape roll the item is documented as using (24" or 30"). A mismatch means narrow dimension > tape roll width, i.e. the tape as filed could not physically span even one label's across-roll footprint.

This is a **documentation audit**, not a re-run of the (now-fixed) calculator engine — it checks what's written in each item file against physical reality, independent of how the live tool would price a fresh run today.

## Findings

| P/N | Label (W" x H") | Narrow dim (across roll) | Vinyl roll | Tape roll used | Fits? |
|---|---|---|---|---|---|
| 1146650 | 40.75 x 10.5 | 10.5" | 24" Cardinal Red | 24" | Yes (2-across, 3" clearance) |
| 1186310 | 33.5625 x 11 | 11" | 24" Cardinal Red | 24" | Yes |
| 1205720 | 33.5625 x 11 | 11" | 24" Cardinal Red | 24" | Yes |
| 3010698 | 33.4375 x 6.8125 | 6.8125" | 24" Cardinal Red | 24" | Yes |
| 3010701 | 49.16 x 9.38 | 9.38" | 24" Cardinal Red | 24" | Yes (2-across, 5.24" clearance) |
| 3010704 | 70.8125 x 14.375 | 14.375" | 15" Cardinal Red | **30"** | Yes (2-up, 28.75" of 30", 1.25" waste) — see confirmation below |
| 3010707 | 34.887 x 4 | 4" | 24" Cardinal Red | 24" | Yes (5-across, 4" clearance) |
| 3010708 | 34.887 x 4 | 4" | 24" Black | 24" | Yes |
| 3010709 | 34.887 x 4 | 4" | 24" White (50yd) | 24" | Yes |
| 3010722 | 21 x 8 | 8" | 24" Cardinal Red | 24" | Yes (3-across, **zero clearance** — already flagged in-file as a manufacturing-tolerance note, not a width mismatch) |
| 3010723 | 21 x 8 | 8" | 24" Black | 24" | Yes (same zero-clearance note as 3010722) |
| 3010724 | 21 x 8 | 8" | 24" White (50yd) | 24" | Yes (same zero-clearance note) |
| 3010736 | 19.18 x 7.6 | 7.6" | 24" White (50yd) | 24" | Yes (3-across, 1.2" clearance) |
| 3017435 | 43.91 x 8.38 | 8.38" | 24" White | 24" | Yes |
| 3018378 | 32.88 x 11 | 11" | 24" Olympic Blue | 24" | Yes |
| 3023921 | 28.0625 x 8.5 | 8.5" | 24" Cardinal Red | **30"** | Yes (2-across, 13" clearance — see note below) |

**Result: zero tape-width mismatches.** Every filed cut-vinyl item's narrow (across-roll) dimension is comfortably within the width of the tape roll it's documented as using. No item needs correction.

## Notes on the two non-standard pairings found

Two items use the 30" tape rather than the account's usual matching 24"/24" pairing. Neither is a mismatch — both are already flagged in their own files for reasons unrelated to fit:

- **P/N 3010704** — uses the 15" Cardinal Red vinyl roll (not 24") with the 30" tape, run 2-up (2 x 14.375" = 28.75" of the 30" width). This is the account's founding Large-Format (Band B) item, full 4-wave AI validated, and both `items/3010704.md` and `categories/cut-vinyl-3m-180mc.md` document the reasoning explicitly: the 15" vinyl roll avoids wasting 9.625" per row that the 24" roll would waste at this label height, and the 30" tape amortizes tape cost over 2 labels per pass instead of 1. **Confirmed deliberate — not a leftover of the Combinations gap.** See "Confirmation on P/N 3010704" below.
- **P/N 3023921** — uses the standard 24" Cardinal Red vinyl roll but the 30" tape (not the matching 24" tape most other Band A items use at this width). Per the item's own Material Specification note, this pairing "is not the zero-waste 24"/24" pairing convention used elsewhere in Band A... flagged for production-run confirmation that the 30" tape is the intended SKU and not a substitution that should be reconciled to the matching 24" tape in a future session." This was directed by the 2026-07-16 session brief and sourced from Grimco; the label's 8.5" narrow dimension would in fact fit the 24" tape just as well (2-across, 7" clearance vs. the 30" tape's 13" clearance) — the 30" choice was a sourcing/brief decision, not a physical requirement. **Already flagged in-file; not a new finding from this audit, and not something this session's engine fix or audit corrects** (per the "do not silently fix" instruction — see below).

## Confirmation on P/N 3010704

Checked specifically per this session's instructions:

- **Label width:** 70.8125" x 14.375" (7.069 sq ft) — confirmed against `items/3010704.md` frontmatter and Spec Extraction.
- **Narrow (across-roll) dimension:** 14.375" (the height). Vinyl uses the 15" Cardinal Red roll (1-across, 0.625" clearance); tape uses the 30" roll (2-up, 2 x 14.375" = 28.75", 1.25" waste strip).
- **Verdict: the 15"-vinyl / 30"-tape pairing is deliberate, not a leftover of the Combinations gap.** It is the founding, fully 4-wave AI-validated data point for the Large-Format (Band B, 5+ sq ft) cut-vinyl band. The 30" tape is not required for the tape to physically fit (a 24" tape would also fit, 1-across, same as the vinyl) — it is a documented cost-efficiency choice: running 2 labels per tape pass instead of 1 lowers tape cost per label (`items/3010704.md`: "the 30" application tape enables 2-up nesting, which is required to amortize the tape cost"). No correction needed.

## What this audit does NOT do

Per this session's explicit instructions, this audit reports findings only. It does not modify any `items/*.md` pricing, material cost, or tier table. Since no mismatch was found, there is nothing to flag for a Nick pricing decision under item 4 of the session's deliverables — the one non-standard pairing worth Nick's attention (3023921's 30" vs. 24" tape choice) was already flagged by a prior session, not newly discovered here, and remains exactly as previously documented (a production-run confirmation item, not a cost-basis error).
