# Elliott Equipment — Completion Templates

> **What gets updated when. No exceptions. No "I'll update that next time."**
>
> Last Updated: 2026-06-01 (VALIDATION_PROMPTS triggers added)

---

## The Self-Healing Rule

This repo is a living, interconnected set of documents. When anything changes, **every affected file must be updated in the same session.** No file is allowed to fall out of sync.

---

## Update Triggers

| Change Type | Files That Must Be Updated |
|-------------|---------------------------|
| New item quoted | `items/[PN].md` (all sections), `.claude/ARCHITECTURE.md` (item catalog row), `categories/[relevant].md` (items table + Pricing Profile), `.claude/PROGRESS.md` (session entry), `.claude/STATE.yml`, `frontend/data.json` (run `python scripts/build_frontend.py` — rebuild `frontend/data.json`) |
| Price change on existing item | `items/[PN].md` (pricing + margin sections), `.claude/ARCHITECTURE.md` (price/margin columns), `categories/[relevant].md` (items table + Pricing Profile if band shifts), `.claude/PROGRESS.md`, check all downstream items in the precedent chain, `frontend/data.json` (run `python scripts/build_frontend.py` — rebuild `frontend/data.json`) |
| Material cost change | `governance/PRODUCTION.md` (material costs), `categories/[relevant].md` (Pricing Profile material cost band), every `items/*.md` in the affected material family (recalculate margins), `.claude/ARCHITECTURE.md` (margin columns), `.claude/PROGRESS.md`, `.claude/STATE.yml`, `frontend/data.json` (run `python scripts/build_frontend.py` — rebuild `frontend/data.json`) |
| Status change | `items/[PN].md` (frontmatter status + Item Overview), `.claude/ARCHITECTURE.md` (status column), `.claude/PROGRESS.md`, `frontend/data.json` (run `python scripts/build_frontend.py` — rebuild `frontend/data.json`) |
| Sean feedback received | `.claude/PROGRESS.md`, relevant `items/[PN].md` (Notes section if item-specific) |
| New material family introduced | `.claude/MASTER_CONTEXT.md` (material families table), `.claude/ARCHITECTURE.md` (category registry), new `categories/[name].md`, `governance/STRUCTURE_RULES.md` (material family definitions) |
| Equipment change | `governance/PRODUCTION.md`, every `categories/*.md` affected (lamination pass calculations, nesting rules), every `items/*.md` affected (production process, margin analysis if passes change) |
| Override applied | `items/[PN].md` (frontmatter override_type + Pricing Derivation), `.claude/PROGRESS.md` |
| Production debrief logged | `items/[PN].md` (Production Debrief section) |
| Drawing revision received | `items/[PN].md` (Spec Extraction, Item Overview, dimensions, sq ft, material cost if changed), `.claude/ARCHITECTURE.md`, `categories/[relevant].md`, `.claude/PROGRESS.md`, `frontend/data.json` (via build_frontend.py) |
| Item discontinued | `items/[PN].md` (status → Discontinued), `.claude/ARCHITECTURE.md` (status column), `.claude/PROGRESS.md`, `frontend/data.json` (via build_frontend.py) |
| Calculator constants change (band thresholds, tier ratios, ink rates, account floor) | Re-run `python scripts/build_calculator_config.py`, commit updated `frontend/calculator_config.json`. No code change to index.html required. |
| New material added to materials/*.md | Re-run all build scripts including `build_calculator_config.py` — verify new material appears in `cut_vinyl_colors` or `material_constants` as appropriate |
| Pricing band shifts (new FA-Accepted item, band normalization) | Update `categories/*.md` first (source of truth), then re-run `build_calculator_config.py` to propagate to calculator |
| New item pricing validation complete (4 waves done, price locked by Nick) | Claude Code writes item file per `governance/STRUCTURE_RULES.md`; updates `categories/*.md`, `.claude/ARCHITECTURE.md`, `.claude/PROGRESS.md`, `.claude/STATE.yml`, runs all build scripts |
| Validation wave prompts need updating (band shift, relationship phase change, new benchmark item) | Update `governance/VALIDATION_PROMPTS.md` — specifically Section 3 benchmark anchors, Section 3 band values, and Section 5 Sean profile if relationship status changes |

---

## Session Completion

Every session that modifies the repo ends with:

1. All affected files updated per the table above.
2. `.claude/PROGRESS.md` entry added (newest first).
3. `.claude/STATE.yml` updated with session outcome and next action.
4. `python scripts/validate.py` passes (when applicable).
5. Commit with the appropriate message format (see `CHAT_CONTEXT.md`).

---

## PROGRESS.md Entry Format

Newest entries at the top.

```markdown
### YYYY-MM-DD — [Session Type]: [Summary]

**What:** [1-2 sentence summary]

**Items Affected:**
- [P/N] — [what changed]

**Files Modified:**
- [file path] — [what changed]

**Key Decisions:**
- [any decisions that affect future sessions]

**Status:** [complete / partial — what's left]
```

---

## STATE.yml Format

```yaml
last_session:
  date: "YYYY-MM-DD"
  type: "new_item | material_update | status_change | audit | other"
  summary: "One sentence."

next_action: "What to do next."
blockers: "none | description"
item_count: N
pending_quotes: "list of P/Ns awaiting Sean response, or none"
```
