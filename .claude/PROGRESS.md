# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> Last Updated: 2026-05-22

---

### 2026-05-22 — New Item: P/N 3018378 — D115 Olympic Blue Model Designation

**What:** Priced and documented P/N 3018378 — cut vinyl model designation label for the D115 model. Olympic Blue, 32.88" × 11.00", single color block lettering ("D115").

**Item Created:** `items/3018378.md`

**Files Updated:**
- `categories/cut-vinyl-3m-180mc.md` — added 3018378 to catalog table, updated Pricing Profile to 3 data points
- `.claude/ARCHITECTURE.md` — added 3018378 to item catalog and precedent chain; updated category registry count
- `governance/PRODUCTION.md` — added 3M 180mC-57 Olympic Blue to material costs table and quick reference
- `.claude/STATE.yml` — updated session state

**Pricing:** $35 at qty 20 (sq ft parity with P/N 1205720). Margin ~78% (Olympic Blue roll cost $162.78 vs Cardinal Red $153.60 drives slight material cost increase: $7.88 vs $7.01).

**Key Decisions:**
- Material: 3M Controltac 180mC-57 Olympic Blue — confirmed in session brief, not in prior repo data. Added to PRODUCTION.md.
- PMS caveat documented: Olympic Blue is visual approximation of PMS 2386 C, not a certified Pantone match. Must be disclosed in quote.
- Sq ft parity: 2.512 sq ft vs 2.56 sq ft benchmark — <2% difference, same tier structure.
- Labels per roll corrected: session brief stated "5 positions" (10 labels/roll). Verified: 10 positions → 20 labels/roll. Material cost unaffected.
- No first article pricing — not requested or offered.
- No AI model validation — direct parity with FA-accepted item.

**Status:** Quoted. Ready to send to Sean.

---

### 2026-05-22 — System Build: Notion → GitHub Migration

**What:** Migrated the entire Elliott Equipment pricing system from Notion to a structured GitHub repo (`tacctile/elliott`). Source data was validated through a 3-round audit in Claude Chat before migration.

**Items Affected:**
- All 5 items (1230820, 1278930, 1245130, 1205720, 3017435) — converted to structured markdown with YAML frontmatter

**Files Created:**
- Full `.claude/` context system (MASTER_CONTEXT, ARCHITECTURE, CHAT_CONTEXT, COMPLETION_TEMPLATES, STATE, PROGRESS, settings.json)
- Full `governance/` doc set (SPEC_EXTRACTION, STRUCTURE_RULES, PRICING_VALIDATION, PRICING_RULES, PRODUCTION)
- 2 category files with Pricing Profiles
- 5 item files with complete frontmatter + all 10 required sections
- Validation and profile scripts
- README, .gitignore

**Key Decisions:**
- MASTER_CONTEXT kept lean — account identity and routing only, no narrative
- Governance split into 5 files (was 1 Notion page) for single-responsibility
- Equipment/production details in their own file (PRODUCTION.md) — changes on different cadence than pricing rules
- CHAT_CONTEXT designed for dual-path operation (Claude Code prompts + direct conversation)
- Pricing Profiles embedded in category files, not separate documents

**Status:** Complete. System ready for first new item.
