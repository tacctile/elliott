# Elliott Equipment — Pro Label Pricing Engine

> **Single source of truth. Read first, every session. No exceptions.**
>
> Last Updated: 2026-06-09 (Session I — $50 rush/favor floor reference added to Internal Pricing Notes, see `governance/PRICING_RULES.md` §27. Previously 2026-06-05: MOQ 10 / $55 minimum order charge purged from this account — Core Rule 8 removed, Core Rule 9 renumbered to 8; Account-Level Order Rules section removed; internal pricing-normalization note relocated to its own section)

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

> **Note:** For new item pricing, the Calculator tab in the frontend can be used to generate an initial pricing brief before beginning the Claude Code session. The calculator output (validation brief) is the input to Round 1 of the 4-round AI validation process. The calculator does NOT write files — Claude Code does. See `governance/CALCULATOR.md` for the calculator's scope, routing tree, flag definitions, and full session sequence.
>
> **Note:** After the calculator generates the validation brief, the 4-wave AI validation process begins per `governance/VALIDATION_PROMPTS.md`. Claude Chat generates one wave prompt at a time. Nick runs each wave across 6 models in ChatHub. After Wave 4, Claude Chat produces the Final Synthesis Table. Nick locks the final price before Claude Code writes any files.

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
5. The system stays in sync at all times. See `.claude/COMPLETION_TEMPLATES.md`.
6. No file is allowed to fall out of sync with any other file. Ever.
7. **Elliott provides production-ready DWG files for every item on this account, without exception.** File prep, artwork preparation, design time, and pre-press labor are zero-cost, zero-time inputs on every Elliott job — past, present, and future. Step 1 of every process (file import/setup) is a ~5-minute mechanical operation, NOT a billable labor input. Any cost reasoning that uses file prep as a pricing driver on this account is incorrect and must be corrected immediately. This is a permanent account-level truth, not a per-job assumption.
8. **All printed/laminated items are priced at full bleed / full coverage ink ($0.50/sq ft × full label sq ft) at all times.** No partial, medium, or low coverage assumptions are permitted on any Elliott printed/laminated item — past, present, or future. Material cost always includes an incidental buffer rounded conservatively upward to account for setup scrap, registration pulls, and minor waste. Canonical formula: `(Orajet sq ft × $1.21) + (lam sq ft × $0.2389) + (label sq ft × $0.50) + incidental buffer`. The frontmatter `material_cost_per_unit` field reflects the buffered total. Established 2026-06-01. See `governance/PRICING_RULES.md` §25 and `governance/PRODUCTION.md` Account-Wide Ink Coverage Standard.

---

## Internal Pricing Notes

Rush/favor floor: $50 per job — see `governance/PRICING_RULES.md` §27. (Separate from and does not stack with the $55 one-off job-economics floor.)

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
│   ├── PRODUCTION.md              # Equipment, materials, nesting, process
│   ├── CALCULATOR.md              # Calculator routing, flags, scope, relationship to AI validation
│   └── VALIDATION_PROMPTS.md      # 4-wave AI validation prompt system — wave structure, attack angles, output schemas, behavioral rules
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
├── materials/
│   ├── orajet-3951-white.md        # Orafol Orajet 3951 cast vinyl (print media)
│   ├── 1mil-polyester-overlaminate.md  # Flexcon FLX000233 1-mil polyester overlaminate
│   ├── 3m-180mc-cardinal-red.md    # 3M Controltac 180mC-53 Cardinal Red
│   ├── 3m-180mc-olympic-blue.md    # 3M Controltac 180mC-57 Olympic Blue
│   ├── 3m-180mc-white-24in.md      # 3M Controltac 180mC-10 White, 24" roll
│   ├── 3m-180mc-white-48in.md      # 3M Controltac 180mC-10 White, 48" roll
│   └── transferrite-582u.md        # TransferRite Ultra 582U application tape
├── scripts/
│   ├── validate.py                # Structure compliance + math verification
│   ├── profile.py                 # Recompute pricing profiles from item data
│   ├── build_frontend.py          # Build frontend/data.json from item frontmatter
│   ├── build_materials.py         # Build frontend/materials.json from material frontmatter
│   └── build_calculator_config.py # Build script for frontend/calculator_config.json
├── frontend/
│   ├── index.html
│   ├── data.json
│   ├── materials.json
│   ├── calculator_config.json     # Generated calculator constants (do not edit manually)
│   └── images/
├── .gitignore
└── README.md
```
