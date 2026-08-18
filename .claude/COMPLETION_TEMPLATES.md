# Elliott Equipment — Completion Templates

> **What gets updated when. No exceptions. No "I'll update that next time."**
>
> Last Updated: 2026-07-30 (Session BI — mandatory Supabase sync step added to the New Item Completion Checklist; MCP fallback documented; the "create a .env file" instruction removed as unworkable in Claude Code sessions, which never carry local service-role credentials)

---

## The Self-Healing Rule

This repo is a living, interconnected set of documents. When anything changes, **every affected file must be updated in the same session.** No file is allowed to fall out of sync.

---

## Update Triggers

| Change Type | Files That Must Be Updated |
|-------------|---------------------------|
| New item quoted | `items/[PN].md` (all sections), `.claude/ARCHITECTURE.md` (item catalog row), `categories/[relevant].md` (items table + Pricing Profile), `.claude/PROGRESS.md` (session entry), `.claude/STATE.yml`, `frontend/data.json` (run `python scripts/build_frontend.py` — rebuild `frontend/data.json`) — then run `python scripts/migrate_to_supabase.py --pn [PN] --verify` for every new P/N this session (see **Mandatory Supabase Sync**, below). A passing `--verify` result is required before the session can close. NOT deferrable, and credentials are NOT required — see the MCP fallback path. |
| Price change on existing item | `items/[PN].md` (pricing + margin sections), `.claude/ARCHITECTURE.md` (price/margin columns), `categories/[relevant].md` (items table + Pricing Profile if band shifts), `.claude/PROGRESS.md`, check all downstream items in the precedent chain, `frontend/data.json` (run `python scripts/build_frontend.py` — rebuild `frontend/data.json`) |
| Material cost change | `governance/PRODUCTION.md` (material costs), `categories/[relevant].md` (Pricing Profile material cost band), every `items/*.md` in the affected material family (recalculate margins), `.claude/ARCHITECTURE.md` (margin columns), `.claude/PROGRESS.md`, `.claude/STATE.yml`, `frontend/data.json` (run `python scripts/build_frontend.py` — rebuild `frontend/data.json`) |
| Sean feedback received | `.claude/PROGRESS.md`, relevant `items/[PN].md` (Notes section if item-specific) |
| New material family introduced | `.claude/MASTER_CONTEXT.md` (material families table), `.claude/ARCHITECTURE.md` (category registry), new `categories/[name].md`, `governance/STRUCTURE_RULES.md` (material family definitions) |
| Equipment change | `governance/PRODUCTION.md`, every `categories/*.md` affected (lamination pass calculations, nesting rules), every `items/*.md` affected (production process, margin analysis if passes change) |
| Override applied | `items/[PN].md` (frontmatter override_type + Pricing Derivation), `.claude/PROGRESS.md` |
| Production debrief logged | `items/[PN].md` (Production Debrief section) |
| Drawing revision received | `items/[PN].md` (Spec Extraction, Item Overview, dimensions, sq ft, material cost if changed), `.claude/ARCHITECTURE.md`, `categories/[relevant].md`, `.claude/PROGRESS.md`, `frontend/data.json` (via build_frontend.py) |
| Calculator constants change (band thresholds, tier ratios, ink rates, account floor) | Re-run `python scripts/build_calculator_config.py`, commit updated `frontend/calculator_config.json`. No code change to index.html required. |
| New material added to materials/*.md | Re-run all build scripts including `build_calculator_config.py` — verify new material appears in `cut_vinyl_colors` or `material_constants` as appropriate |
| Pricing band shifts (new item, band normalization) | Update `categories/*.md` first (source of truth), then re-run `build_calculator_config.py` to propagate to calculator |
| New item pricing validation complete (4 waves done, price locked by Nick) | Claude Code writes item file per `governance/STRUCTURE_RULES.md`; updates `categories/*.md`, `.claude/ARCHITECTURE.md`, `.claude/PROGRESS.md`, `.claude/STATE.yml`, runs all build scripts |
| Validation wave prompts need updating (band shift, relationship phase change, new benchmark item) | Update `governance/VALIDATION_PROMPTS.md` — specifically Section 3 benchmark anchors, Section 3 band values, and Section 5 Sean profile if relationship status changes |
| Supabase seed required | Every session that adds, modifies, or discontinues an item | Run `python scripts/migrate_to_supabase.py --pn [PN] --verify` (or the full unscoped run, if credentials happen to be available) after `validate.py` passes. A passing `--verify` result is required — see **Mandatory Supabase Sync**, below. |

---

## Mandatory Supabase Sync (New Item Completion Checklist)

**A session that files an item to the repo without a confirmed Supabase sync is incomplete. Do not commit, do not push, do not mark done.**

The frontend reads live item data from Supabase's `elliott_items` table first (`DATA_SOURCE = 'supabase'` in `frontend/index.html`) — `frontend/data.json` is fetched only for prose sections and as an offline fallback. An item that exists in the repo, in `frontend/data.json`, and even on `main` after a merge, is **still invisible on the live platform** until it also exists in `elliott_items`. This has happened at least four times (P/N 1257750, 1001530, 1277630, 3024180) because `scripts/migrate_to_supabase.py`'s live-sync path requires a local `SUPABASE_SERVICE_ROLE_KEY`, which Claude Code sessions do not have — the sync was silently deferred to Nick every time, and every time it was missed until a later session had to diagnose the gap after the fact.

**This is no longer optional and no longer credential-gated.** For every new item filed in a session:

1. Run:
   ```
   python scripts/migrate_to_supabase.py --pn [PN] --verify
   ```
   (comma-separate or repeat `--pn` for multiple new items in one session.)

2. **If `SUPABASE_SERVICE_ROLE_KEY` is available** (rare in Claude Code sessions): the command syncs and verifies in one step. If `--verify` passes, proceed.

3. **If no credentials are available** (the normal case): the command detects this automatically and prints the exact, scoped upsert SQL for just the P/N(s) passed — it does not touch any other item's row. Execute that SQL immediately via the `mcp__Supabase__execute_sql` MCP tool (Supabase MCP access is available in every Claude Code session on this account), then re-run the exact same command with `--verify` to confirm the row(s) landed.

4. **`--verify` failure is a hard stop.** The script exits non-zero and prints which part number(s) are missing from `elliott_items`. Do not proceed to commit/push/close the session until `--verify` passes. Do not defer this to Nick, do not create a `.env` file, and do not mark the session done on the strength of `frontend/data.json` alone — none of that step ever confirms the item is live.

5. Log the confirmed `--verify` result in the session's `.claude/PROGRESS.md` entry and `.claude/STATE.yml` update, same as any other completion step.

To check the whole account against known drift (not part of a normal new-item session, but useful after any suspected gap): `python scripts/migrate_to_supabase.py --verify --all` checks every `items/*.md` P/N against `elliott_items` with no writes. It treats the documented P/N 1001530 orphan row (real, quoted, Supabase-only — see `.claude/PROGRESS.md` Session BE) as a known exception, not a failure; any other missing or unexplained-extra row is reported and should be investigated before the session closes.

---

## Session Completion

Every session that modifies the repo ends with:

1. All affected files updated per the table above.
2. `.claude/PROGRESS.md` entry added (newest first).
3. `.claude/STATE.yml` updated with session outcome.
4. `python scripts/validate.py` passes (0 errors, 0 warnings).
5. **`python scripts/migrate_to_supabase.py --pn [PN] --verify` passes for every
   new/changed item this session (see **Mandatory Supabase Sync**, above). This
   step is BLOCKING — the session is not complete until `--verify` confirms the
   row(s) in `elliott_items`. No local credentials are required: use the MCP
   fallback (`mcp__Supabase__execute_sql`) when `SUPABASE_SERVICE_ROLE_KEY` is
   absent, which is the normal case. Never defer this step to Nick.**
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

blockers: "none | description"
item_count: N
```
