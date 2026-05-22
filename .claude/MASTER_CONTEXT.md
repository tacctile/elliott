# Elliott Equipment — Pro Label Pricing Engine

> **Single source of truth. Read first, every session. No exceptions.**
>
> Last Updated: 2026-05-22

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
│   └── 3017435.md
├── scripts/
│   ├── validate.py                # Structure compliance + math verification
│   └── profile.py                 # Recompute pricing profiles from item data
├── .gitignore
└── README.md
```
