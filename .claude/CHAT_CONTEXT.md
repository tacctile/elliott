# Elliott Equipment — Chat Context

> **Guide for Claude Chat when generating prompts for Claude Code, and for operating directly in conversation.**
>
> Last Updated: 2026-05-22

---

## What This File Is

Nick uses Claude Chat for two purposes:

1. **Generating prompts for Claude Code** — new item pricing, bulk updates, system changes. The prompt is pasted into Claude Code (Opus 4.7, max effort) which has the full repo mounted.
2. **Operating directly in conversation** — status changes, Sean feedback logging, quick audits, material cost checks. Lighter tasks that don't need Claude Code.

This file defines how both paths work.

---

## Path 1: Claude Code Prompt Generation (New Item Pricing)

### The Workflow

1. Sean sends Nick a spec sheet (PDF).
2. Nick drops the spec sheet + the `.claude/` folder (or the full repo) into this Claude Chat session.
3. Claude Chat reads CHAT_CONTEXT, runs through the Pre-Quote Checklist mentally, and **presents the prompt plan to Nick for approval before generating anything.**
4. Nick reviews. Confirms or corrects.
5. Claude Chat generates the self-contained prompt.
6. Nick pastes the prompt into Claude Code (Opus 4.7, max effort) with the repo mounted.
7. Claude Code outputs: spec extraction, pricing recommendation, complete item `.md` file, updated category profile, updated ARCHITECTURE.md.
8. Claude Code runs `python scripts/migrate_to_supabase.py` in live mode. Confirms `elliott_items` row count = N+1. This is a required completion step, not a follow-up task. Session is not done until this passes.
9. Nick reviews the output.
10. Nick opens a fresh Claude Chat session with the full repo loaded (minus item files and frontend).
11. Nick pastes the validation brief from the calculator.
12. Claude Chat generates Wave 1 prompt (per `governance/VALIDATION_PROMPTS.md`).
13. Nick runs Wave 1 across 6 models in ChatHub, pastes all 6 responses back into Claude Chat.
14. Claude Chat generates Wave 2 prompt incorporating Wave 1 findings.
15. Nick runs Wave 2, pastes all 6 responses.
16. Claude Chat generates Wave 3 prompt.
17. Nick runs Wave 3, pastes all 6 responses.
18. Claude Chat generates Wave 4 prompt.
19. Nick runs Wave 4, pastes all 6 responses.
20. Claude Chat produces the Final Synthesis Table.
21. Nick and Claude Chat discuss and lock the final price.
22. Nick commits and sends the quote.

### Critical Rule

**Claude Chat NEVER generates a prompt without walking Nick through what's in it first.** Bad data into Claude Code means bad pricing out. Every prompt is reviewed before it's handed off.

### Prompt Structure

Every prompt pasted into Claude Code follows this structure:

```
## Session: New Item — P/N [number]

### Context Files to Read First
1. `.claude/MASTER_CONTEXT.md`
2. `governance/SPEC_EXTRACTION.md`
3. `governance/STRUCTURE_RULES.md`
4. `categories/[relevant-category].md`
5. `governance/PRICING_RULES.md`
6. `governance/PRICING_VALIDATION.md`
7. `governance/PRODUCTION.md`
8. `.claude/PROGRESS.md`

### Spec Sheet Data
[Extracted spec data from the PDF — Nick and Claude Chat verified this]

### Comparable Items
[Which existing items Claude Code should reference, and why]

### What You Are Doing
[1-3 sentence summary]

### Specific Instructions
[Numbered list of exactly what to produce]

### Acceptance Criteria
[What "done" looks like — testable]

### Do NOT
[Scope boundaries]

### On Completion
1. Create the item file at `items/[PN].md` with all required sections
2. Update `categories/[relevant].md` — add item to catalog table + update Pricing Profile
3. Update `.claude/ARCHITECTURE.md` — add item to catalog registry
4. Update `.claude/PROGRESS.md` — add session entry
5. Update `.claude/STATE.yml` — record what was done
6. Run `python scripts/validate.py` — all checks must pass
7. Run `python scripts/migrate_to_supabase.py` (live). Confirm `elliott_items` row count incremented. This is blocking — do not commit until seed is confirmed.
8. Commit with message: `item([PN]): [short description]`
```

### Prompt Writing Rules

1. **Self-contained.** Claude Code starts fresh every session. The prompt references every file it needs.
2. **Read-first.** Always starts with "Context Files to Read First."
3. **One item per prompt.** Never combine two new items into one prompt.
4. **Explicit file paths.** Always full paths from repo root.
5. **No ambiguity.** If there are two approaches, pick one.
6. **Include the "Do NOT" section.** Prevents scope creep.
7. **Acceptance criteria are testable.** Not "it should be correct" — specific checks.
8. **Spec data is pre-verified.** Nick confirmed the extraction before it goes into the prompt.
9. **Every new-item prompt must include in its Acceptance Criteria:** "`python scripts/migrate_to_supabase.py` completed successfully — `elliott_items` row count = [expected count]." The session is not complete until this check passes. Never mark this step as deferred, optional, or a follow-up.

---

## Path 2: Direct Conversation (Lighter Tasks)

### When to Use This Path

- Status changes (item moved from Quoted to FA Accepted)
- Sean feedback logging
- Material cost updates
- Quick sanity checks on pricing logic
- Audits of specific items or the full system
- Strategy discussions that don't produce a commit

### How It Works

1. Nick describes the task.
2. Claude Chat reads the relevant files from the repo (if the repo is in context) or works from the data Nick provides.
3. Claude Chat produces the updated content directly — updated item frontmatter, new PROGRESS.md entry, revised category profile data, etc.
4. Nick applies the changes (either by pasting into the repo files or by committing via Claude Code).

### Rules

- Claude Chat always specifies exactly which files need to change and what the changes are.
- Claude Chat never makes pricing recommendations without the full context (category profile + comparable items + pricing rules).
- For material cost updates, Claude Chat flags every downstream item that needs margin recalculation.

---

## What Claude Chat Needs From Nick — Every New Item

### Always Required

1. The spec sheet / engineering drawing (PDF or extracted data)
2. Quantity Sean is requesting — or confirmation that we're quoting standard volume tiers
3. Whether Sean asked for a first article

### Required If Not Already in the System

1. Material roll pricing — exact cost per roll, roll dimensions, supplier (Claude Chat checks existing data first)
2. Application tape pricing — if it's a new product or the roll has changed
3. Laminate pricing — if it's a new product or pricing has changed

### Required If Strategically Relevant

1. Context about this specific item (test item, reorder, new product line, rush)
2. Feedback from Sean on previous quotes
3. Changes to the relationship status

### Claude Chat's Responsibility

- If Nick doesn't provide something from "Always Required," ask before proceeding.
- If material pricing data exists in the repo and is less than 90 days old, use it. If older, flag it.
- Never assume material pricing. If stale, ask: "The last material cost I have for [product] is from [date] at [price]. Still current?"

---

## Commit Message Format

```
item([PN]): [short description]          # New item or item update
category([name]): [short description]    # Category profile update
governance([file]): [short description]  # Governance doc change
system: [short description]              # Cross-cutting system change
audit: [short description]               # Audit findings
```

Examples:
- `item(1245130): initial pricing — 5-label kit, 5/3 parity, $50 at qty 20`
- `category(printed-laminated): update profile with 1245130 data point`
- `governance(production): update laminator width after equipment purchase`
- `system: material cost update — Orajet 3951 price increase $1.21 → $1.35/sq ft`
