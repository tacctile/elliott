# Elliott Equipment — Pro Label Pricing Engine

AI-directed pricing system for Elliott Equipment Company's label and decal program (~$140K/year).

## What This Is

A structured knowledge repository that ensures any AI session — given a spec sheet and this context — arrives at the same price, every time, with zero ambiguity.

## How to Use

1. Read `.claude/MASTER_CONTEXT.md` first. Always.
2. Follow the reading order for your session type.
3. Never price without reading the governance docs.

## Structure

- `.claude/` — Session context, architecture registry, state tracking
- `governance/` — Pricing rules, spec extraction protocol, validation methodology, production specs
- `categories/` — Material family profiles with rolling pricing bands
- `items/` — One file per item with YAML frontmatter + full documentation
- `scripts/` — Validation and profile computation

## Validation

```bash
python scripts/validate.py    # Structure compliance + math checks
python scripts/profile.py     # Recompute pricing profile bands
```

## Rules

- Claude is the sole author and maintainer.
- Nick provides inputs and makes final pricing decisions.
- The system stays in sync at all times. See `.claude/COMPLETION_TEMPLATES.md`.
