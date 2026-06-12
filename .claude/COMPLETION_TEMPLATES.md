# Elliott Equipment — Completion Templates

> **What gets updated when. No exceptions. No "I'll update that next time."**
>
> Last Updated: 2026-06-12 (PROGRESS.md 10-entry rolling window codified + compact entry format adopted)

---

## The Self-Healing Rule

This repo is a living, interconnected set of documents. When anything changes, **every affected file must be updated in the same session.** No file is allowed to fall out of sync.

---

## Update Triggers

| Change Type | Files That Must Be Updated |
|-------------|---------------------------|
| New item quoted | `items/[PN].md` (all sections), `.claude/ARCHITECTURE.md` (item catalog row), `categories/[relevant].md` (items table + Pricing Profile), `.claude/PROGRESS.md` (session entry), `.claude/STATE.yml`, `frontend/data.json` (run `python scripts/build_frontend.py` — rebuild `frontend/data.json`) — then run `python scripts/migrate_to_supabase.py` (live, blocking). Confirm `elliott_items` row count = previous count + 1 before closing the session. NOT deferrable. |
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
| Supabase seed required | Every session that adds, modifies, or discontinues an item | Run `python scripts/migrate_to_supabase.py` after `validate.py` passes. Confirm row count. If credentials missing, create `.env` first. |

---

## Session Completion

Every session that modifies the repo ends with:

1. All affected files updated per the table above.
2. `.claude/PROGRESS.md` entry added (newest first).
3. `.claude/STATE.yml` updated with session outcome and next action.
4. `python scripts/validate.py` passes (0 errors, 0 warnings).
5. **`python scripts/migrate_to_supabase.py` runs successfully (live mode).
   Confirm `elliott_items` row count incremented by the number of new items
   this session. This step is BLOCKING — the session is not complete until
   the seed is confirmed. If service-role credentials are missing, the .env
   file at repo root must be created before proceeding. Never defer this step.**
6. Commit with the appropriate message format (see `CHAT_CONTEXT.md`).

> PROGRESS.md enforces a 10-entry rolling window. When adding a new entry, remove the oldest if the count exceeds 10.

---

## PROGRESS.md Entry Format

Newest entries at the top. **Rolling window: 10 entries max — when adding an 11th, remove the oldest. Git retains all history.** Target length per entry: 10–25 lines. No sections beyond these five. PROGRESS.md is the session memory layer only — full validation records live in `items/*.md` (Pricing Derivation), file-level changes live in git history, and acceptance criteria are enforced by `scripts/validate.py`. Do not log file-modified lists, acceptance checklists, wave transcripts, margin tables, or §26 cliff math here.

```markdown
### YYYY-MM-DD — [Session Label]: [One-line summary]

**What:** 2–4 sentences max. What was done and why. Strategic framing only — not a file list.

**Key Decisions:** Only decisions that are non-obvious, override something, or affect future sessions. Engine consensus with no override = omit. If nothing notable: omit this section entirely.
- Decision + one-sentence rationale

**Strategic Flags:** Internal-only context, band implications, January 2027 normalization anchors, precedent risks, parity links, do-not-benchmark designations. If nothing: omit this section.
- Flag + implication

**Status:** One sentence. Complete / partial + what remains.
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
