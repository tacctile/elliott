# Spec Extraction Protocol

> **Mandatory. Runs BEFORE any pricing. No exceptions.**
>
> Last Updated: 2026-06-09 (Session H — Ink Coverage default corrected to full bleed per §25; the stale "Assumed: medium coverage" default contradicted the 2026-06-01 account-wide rule)

---

## Purpose

Every new engineering spec sheet (PDF) must have every field below populated and tagged as **Confirmed**, **Assumed**, or **Blocked** before any pricing math starts.

- **Confirmed** — explicitly stated on the drawing, no interpretation required.
- **Assumed** — not stated, but a documented default exists and is being applied.
- **Blocked** — not stated, no safe default exists. Pricing stops. Ask Nick.

If any field is tagged Blocked, pricing does not proceed. Period.

---

## Extraction Fields

### Identity

| Field | Source | Default Rule If Missing |
|-------|--------|------------------------|
| Part Number | Title block | **Blocked** — never assume a P/N |
| Drawing Revision / Date | Title block or revision block | Assumed: Rev A / current date |
| Model | Title block or callout | **Blocked** if not inferable from P/N or drawing context |
| Description | Title block | Confirmed from drawing title. If missing, write one from content. Tag as Assumed. |
| Engineer / Drafter | Title block | Assumed: not captured (informational only, does not affect pricing) |

### Dimensions

| Field | Source | Default Rule If Missing |
|-------|--------|------------------------|
| Width | Dimension callout | **Blocked** — never estimate dimensions |
| Height | Dimension callout | **Blocked** — never estimate dimensions |
| Tolerances | Dimension callout or general notes | Assumed: ±1/16" |
| Corner Spec | Detail callout or general notes | Assumed: square corners unless radius called out |
| Unit of Measure | Drawing convention | Assumed: inches (all Elliott drawings to date) |

### Label / Kit Structure

| Field | Source | Default Rule If Missing |
|-------|--------|------------------------|
| Label Count | BOM, callout, or sheet count | **Blocked** if ambiguous — never guess kit label count |
| Labels Same Size? | Dimension comparison | Confirmed if all match. **Blocked** if mixed — mixed-size kits need special handling. |
| Label Identifiers | Callouts (A, B, C, etc.) | Assumed: sequential alpha if labels are distinct but not labeled |

### Material

| Field | Source | Default Rule If Missing |
|-------|--------|------------------------|
| Substrate / Material Callout | Material notes, general notes | **Blocked** if no indication at all. If generic ("white vinyl"), map to closest family and tag Assumed. |
| Substrate Mapped to Shop Material | Claude maps callout → category | Confirmed if exact match. Assumed if interpreted. **Blocked** if no reasonable mapping. |
| Film Thickness | Material spec or general notes | Assumed: standard for mapped family (2-mil for 3M 180mC, cast for Orajet 3951) |
| Adhesive Type | Material spec or general notes | Assumed: permanent, pressure-sensitive |
| Laminate / Overlay Callout | Material notes or general notes | Printed: Assumed 1-mil clear polyester. Cut vinyl: N/A. **Blocked** if drawing calls out unknown type. |
| Laminate Mapped to Shop Material | Claude maps callout → category | Same logic as substrate mapping |
| Application Tape | Process notes | Assumed: TransferRite Ultra 582U for cut vinyl. N/A for printed/laminated. |

### Print and Color

| Field | Source | Default Rule If Missing |
|-------|--------|------------------------|
| Color Count / Description | Artwork, color callouts | Printed: Assumed full-color CMYK. Cut vinyl: Confirmed single color from material spec. |
| Ink Coverage Estimate | Account rule — not a per-drawing assessment | Assumed: full bleed ($0.50/sq ft) — account standard per PRICING_RULES.md §25, always. No medium/low/partial coverage assumption is permitted on any Elliott printed/laminated item. |
| White Ink / Backer Required | Substrate + artwork analysis | Assumed: no (white substrate). **Blocked** if clear substrate or reverse-print indicated. |
| Barcode / QR / Variable Data | Artwork or general notes | Assumed: none. Flag if variable data detected — changes production process. |

### Durability and Environment

| Field | Source | Default Rule If Missing |
|-------|--------|------------------------|
| Environmental / Durability Callout | General notes or spec reference | Assumed: 5-7 year outdoor industrial |
| Regulatory Markings | Artwork or general notes | Confirmed if ANSI/UL/CSA visible. Assumed: none if not present. |

### Finish and Delivery

| Field | Source | Default Rule If Missing |
|-------|--------|------------------------|
| Finish | General notes or material spec | Assumed: gloss for printed/laminated. Standard vinyl finish for cut vinyl. |
| Packaging / Delivery Format | General notes or PO | Assumed: flat, individually cut, stacked. Kits: collated as matched sets. |
| Application Method | General notes | Assumed: hand-applied on equipment |

---

## Account-Specific Defaults

These defaults apply unless the drawing explicitly states otherwise:

| Default | Value | Basis |
|---------|-------|-------|
| Unit of measure | Inches | All Elliott drawings to date |
| Adhesive | Permanent, pressure-sensitive | All Elliott items to date |
| Cut vinyl substrate | 3M Controltac 180mC | Established material family |
| Printed substrate | Orajet 3951 cast vinyl | Established material family |
| Overlaminate (printed) | 1-mil clear polyester | Established material family |
| Application tape (cut vinyl) | TransferRite Ultra 582U | Established material family |
| Ink coverage (printed/laminated) | Full bleed ($0.50/sq ft × full label sq ft) | Account-wide standard per `PRICING_RULES.md` §25 (established 2026-06-01) — applies always; never assume medium/low/partial |
| Corners | Square unless radiused | Elliott drawings specify radius when needed |
| Durability | 5-7 year outdoor industrial | Account standard |
| Application | Hand-applied on equipment | Elliott production process |
| Packaging | Flat, stacked, kits collated | Account standard |
| Tolerances | ±1/16" | Industry standard for this product class |
| Artwork / File Prep | Production-ready DWG provided by Elliott | Zero-cost, zero-time input on every Elliott job — past, present, and future. NEVER a cost factor. See `PRICING_RULES.md` §22-24. |

---

## Output Format

```
SPEC EXTRACTION — P/N [number]

Identity:
  Part Number: [value] — Confirmed
  Revision: [value] — Confirmed / Assumed (Rev A)
  Model: [value] — Confirmed
  Description: [value] — Confirmed
  Engineer/Drafter: [value] — Confirmed / Assumed (not captured)

Dimensions:
  Width: [value] — Confirmed
  Height: [value] — Confirmed
  Tolerances: [value] — Confirmed / Assumed (±1/16")
  Corners: [value] — Confirmed / Assumed (square)

Structure:
  Label Count: [value] — Confirmed
  Labels Same Size: [yes/no] — Confirmed

Material:
  Substrate Callout: [exact drawing text] — Confirmed
  Mapped To: [shop material] — Confirmed / Assumed
  Laminate: [value] — Confirmed / Assumed / N/A
  Application Tape: [value] — Confirmed / Assumed / N/A

Print:
  Colors: [description] — Confirmed / Assumed
  Coverage: Full bleed ($0.50/sq ft) — account standard per §25 — Assumed/Confirmed
  Variable Data: [none/yes — describe] — Confirmed / Assumed

Environment:
  Durability: [value] — Confirmed / Assumed
  Regulatory: [value] — Confirmed / Assumed (none)

Finish & Delivery:
  Finish: [value] — Assumed
  Packaging: [value] — Assumed
  Application: [hand-applied] — Assumed

BLOCKED FIELDS: [list any, or "None"]
ASSUMPTIONS: [numbered list of every Assumed field with the default applied]
```

---

## Rules

1. This extraction is Step 0. Runs before anything else.
2. Every new item gets a full extraction. No exceptions.
3. The completed extraction is stored in the item file under the **Spec Extraction** section (before Item Overview).
4. If a drawing produces 2+ reasonable material mappings, it is **Blocked**, not Assumed.
5. Claude never prices a Blocked item. The conversation stops at extraction until Nick resolves the block.
6. When account-specific defaults change, update the defaults table in this file immediately.
