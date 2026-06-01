# Elliott Equipment — Pro Label Pricing Engine

> **Single source of truth. Read first, every session. No exceptions.**
>
> Last Updated: 2026-06-01

---

## What This Repo Is

This is the AI-directed pricing engine for Elliott Equipment Company's label and decal program. Every file in this repo exists to ensure that any AI session — given a spec sheet and this context — arrives at the same price, every time, with zero ambiguity.

This is not a codebase. It is a knowledge system with the same architectural discipline as one.

---

## Account Identity

| Field | Value |
|-------|-------|
| Company | Elliott Equipment Company (subsidiary of Stellar Industries) |
| Location | Omaha, NE (~8 miles from Pro Label) |
| Contact | Sean Finn — Buyer / Data Specialist (Employee-Owner) |
| Email | sean.finn@elliottequip.com |
| Phone | Work: 531.867.3557 · Direct: 402.932.9483 |
| Annual Spend | ~$140,000 (labels and decals) |
| Status | Actively displacing incumbent (Pro Sign & Screen Printing) |

---

## Material Families

| Family | Description | Category File |
|--------|-------------|---------------|
| 3M 180mC Cut Vinyl | All 3M Controltac 180mC colors. Cut/weed/mask. No printing. | `categories/cut-vinyl-3m-180mc.md` |
| Orajet 3951 Cast + Polyester Lam | Orajet 3951 base + 1-mil polyester overlaminate. Printed full-color. | `categories/printed-laminated-orajet.md` |
| Convex High Bond + Poly Lam | Convex 6-mil high bond + polycarbonate overlaminate. Panel decals. | No category file yet — first item establishes it. |
| Lexan/Polycarbonate | Direct print on polycarbonate substrate. Legacy Elliott spec. | No category file yet — first item establishes it. |

---

## Reading Order by Session Type

### New Item Pricing

1. `.claude/MASTER_CONTEXT.md` (this file)
2. `governance/SPEC_EXTRACTION.md` — run extraction on the PDF
3. `governance/STRUCTURE_RULES.md` — confirm documentation requirements
4. The relevant `categories/*.md` — read the Pricing Profile first, then material system and decision tree
5. The relevant `items/*.md` — comparable items filtered by material family and item type
6. `governance/PRICING_RULES.md` — the constraints on every pricing decision
7. `governance/PRICING_VALIDATION.md` — determine if multi-round AI validation is warranted
8. `.claude/PROGRESS.md` — recent context that affects this quote

Only after reading all eight does pricing begin.

### Material Cost Update

1. `.claude/MASTER_CONTEXT.md`
2. `governance/PRODUCTION.md` — current material costs and roll specs
3. The relevant `categories/*.md` — update the Pricing Profile material cost band
4. All `items/*.md` in the affected material family — recalculate margins
5. `.claude/COMPLETION_TEMPLATES.md` — verify every affected location is updated

### Status Change / Sean Feedback

1. `.claude/MASTER_CONTEXT.md`
2. The relevant `items/*.md`
3. `.claude/PROGRESS.md` — log the event
4. `.claude/COMPLETION_TEMPLATES.md` — verify sync

### System Audit

1. Read every file in the repo
2. Check every item against `governance/STRUCTURE_RULES.md`
3. Verify Pricing Profile bands match item data
4. Flag inconsistencies

---

## Core Rules (Apply to Every Session)

1. Claude is the sole author and maintainer of all content in this repo.
2. Nick provides inputs (spec sheets, material costs, strategic direction) and makes final pricing decisions.
3. Claude recommends, validates, and documents. Claude does not send quotes.
4. All pricing decisions are Nick's. Overrides are classified and logged.
5. The system stays in sync at all times. See `COMPLETION_TEMPLATES.md`.
6. No file is allowed to fall out of sync with any other file. Ever.
7. **Elliott provides production-ready DWG files for every item on this account, without exception.** File prep, artwork preparation, design time, and pre-press labor are zero-cost, zero-time inputs on every Elliott job — past, present, and future. Step 1 of every process (file import/setup) is a ~5-minute mechanical operation, NOT a billable labor input. Any cost reasoning that uses file prep as a pricing driver on this account is incorrect and must be corrected immediately. This is a permanent account-level truth, not a per-job assumption.
8. **Printed/laminated items on this account are subject to MOQ 10 and $55 minimum order charge rules.** See Account-Level Order Rules section below. Cut vinyl items are NOT subject to these rules at this time.

---

## Account-Level Order Rules

> **Established 2026-06-01. Apply to printed/laminated items (Orajet 3951 + polyester lam). Cut vinyl items (3M 180mC) are NOT subject to these rules at this time.**
>
> Full rule codification: `governance/PRICING_RULES.md` §25–29 and `categories/printed-laminated-orajet.md` Account-Level Order Rules block.

### Printed/Laminated MOQ: 10 Units

All printed/laminated catalog items on this account have a minimum order quantity of 10 units. This applies to all new items quoted going forward. Existing item tier tables are not retroactively restructured — existing items retain their current pricing structure.

### $55 Minimum Order Charge

Any order on a printed/laminated item where the buyer orders fewer than 10 units is subject to a **$55.00 minimum order charge**. This is a flat total — it is NOT a per-unit rate and NOT $55 × quantity. The $55.00 floor is the established account minimum-worthwhile-charge, consistent with all prior one-off job handling on this account (3017583, 3017584, outrigger switch program).

### Invoice Protection

No buyer on this account will ever be invoiced more for ordering a smaller quantity than they would pay for a larger quantity at the next tier. At tier boundaries where math creates a cliff, invoice protection applies automatically — the buyer is charged whichever total is lower.

### Required Quote Language

All quotes for printed/laminated items must include the following language exactly:

> "Minimum order for printed labels is 10 units. Orders below 10 units are subject to a $55.00 minimum order charge. You will never be invoiced more for a smaller quantity."

### Sub-10 Handling

Requests for fewer than 10 units of a printed/laminated catalog item are handled as one-off flat-rate jobs at the $55.00 account minimum order charge. Same treatment as all prior field service one-offs (3017583, 3017584, outrigger switches). No per-unit rate applies below MOQ.

### Cut Vinyl Exception

3M 180mC cut vinyl items are NOT subject to MOQ 10 or the $55 minimum order charge at this time. Cut vinyl MOQ structure will be addressed separately as that program matures.

### 2028 Context — Beginning of MOQ Formalization Plan

The printed/laminated MOQ 10 rule established in this session is the beginning of Nick's plan to formalize MOQ structure across the full account beginning **January 1, 2028**.

- Business justification: COGS increases and overhead increases anticipated by that date.
- January 2027: one conversation will cover MOQ formalization, pricing normalization toward industry standard, and full 2028 structure simultaneously.
- The 2028 date represents full-account MOQ formalization — printed/laminated MOQ 10 is already in effect from this session.

> **INTERNAL NOTE (DO NOT SURFACE TO BUYER):** The current account band ($15.43–$15.91/sq ft at qty 20) is a relationship concession below industry standard (~$18–$22/sq ft for premium cast vinyl + polyester lam ANSI safety labels at qty 20). Nick's plan is to normalize pricing toward industry standard by January 1, 2027 as Pro Label has established technical partnership status. This is strategic context for future pricing sessions only.

---

## File Map

```
elliott/
├── .claude/
│   ├── MASTER_CONTEXT.md          # This file — project DNA
│   ├── ARCHITECTURE.md            # Living registry of all items, categories, families
│   ├── CHAT_CONTEXT.md            # How to generate prompts and run sessions
│   ├── COMPLETION_TEMPLATES.md    # Self-healing rule, update triggers
│   ├── STATE.yml                  # Last session state
│   ├── PROGRESS.md                # Chronological session log
│   └── settings.json              # Claude Code permissions
├── governance/
│   ├── SPEC_EXTRACTION.md         # Mandatory field extraction from engineering PDFs
│   ├── STRUCTURE_RULES.md         # Item documentation standard, database schema
│   ├── PRICING_VALIDATION.md      # 4-round, 6-model validation methodology
│   ├── PRICING_RULES.md           # Non-negotiable pricing constraints
│   └── PRODUCTION.md              # Equipment, materials, nesting, process
├── categories/
│   ├── cut-vinyl-3m-180mc.md      # Material system + pricing profile + decision tree
│   └── printed-laminated-orajet.md
├── items/
│   ├── 1230820.md                 # One file per item, YAML frontmatter + 9 sections
│   ├── 1278930.md
│   ├── 1245130.md
│   ├── 1205720.md
│   ├── 3017435.md
│   ├── 3018378.md
│   └── images/                    # Spec sheet PDFs and reference images
├── scripts/
│   ├── validate.py                # Structure compliance + math verification
│   ├── profile.py                 # Recompute pricing profiles from item data
│   └── build_frontend.py          # Build frontend/data.json from item frontmatter
├── frontend/
│   ├── index.html
│   ├── data.json
│   └── images/
├── .gitignore
└── README.md
```
