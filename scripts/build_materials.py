#!/usr/bin/env python3
"""
Elliott Equipment Pricing Engine — Materials Data Builder

Reads all material YAML frontmatter from materials/*.md and writes
frontend/materials.json.

SUPABASE-PRIMARY ARCHITECTURE (Session H, 2026-06-09): the deployed
frontend now reads material data from Supabase (elliott_materials) first;
the Materials Manager tab writes to Supabase directly. frontend/
materials.json is a SECONDARY artifact — the offline fallback (used when
Supabase is unreachable, with a visible banner) and the validate.py /
audit compatibility surface. Keep it current via this script (repo state)
or scripts/sync_from_supabase.py (live DB state).

Usage:
    python scripts/build_materials.py
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
MATERIALS_DIR = REPO_ROOT / "materials"
OUTPUT_FILE = REPO_ROOT / "frontend" / "materials.json"


NUMERIC_FIELDS = {
    'film_thickness_mil', 'thickness_mil', 'roll_width_in', 'roll_length_yd',
    'roll_length_ft', 'cost_per_roll', 'cost_per_sq_ft', 'cost_per_linear_yd',
    'cost_per_linear_ft', 'cost_per_msi', 'max_laminator_width_in',
}

LIST_FIELDS = {
    'compatible_laminates', 'compatible_substrates', 'compatible_tapes',
    'compatible_cut_vinyls', 'used_in_items',
}


def coerce_numeric(val):
    if val == '' or val.lower() == 'null':
        return None
    try:
        if '.' in val:
            return float(val)
        return int(val)
    except (ValueError, TypeError):
        return val


def parse_list(val):
    """Parse a YAML inline list like ["a", "b", "c"] or []."""
    val = val.strip()
    if not val or val == '[]':
        return []
    if val.startswith('[') and val.endswith(']'):
        inner = val[1:-1].strip()
        if not inner:
            return []
        items = []
        for item in inner.split(','):
            item = item.strip().strip('"').strip("'")
            if item:
                items.append(item)
        return items
    return []


def parse_frontmatter(filepath):
    """Extract YAML frontmatter fields from a material markdown file."""
    content = filepath.read_text()
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    fm = {}
    for line in match.group(1).strip().split('\n'):
        if ':' not in line:
            continue
        key = line.split(':', 1)[0].strip()
        raw = line.split(':', 1)[1].strip()

        if key in LIST_FIELDS:
            fm[key] = parse_list(raw)
            continue

        if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
            val = raw[1:-1].replace('\\"', '"').replace("\\'", "'")
        else:
            val = raw

        if val.lower() == 'null':
            fm[key] = None
            continue
        if val == '':
            fm[key] = ''
            continue

        if key in NUMERIC_FIELDS:
            fm[key] = coerce_numeric(val)
        else:
            fm[key] = val
    return fm


def main():
    material_files = sorted(MATERIALS_DIR.glob("*.md"))
    materials = {}

    for filepath in material_files:
        fm = parse_frontmatter(filepath)
        if fm is None:
            continue
        mid = fm.get('material_id', filepath.stem)
        materials[mid] = {'frontmatter': fm}

    output = {
        'generated': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'material_count': len(materials),
        'materials': materials,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(output, indent=2))
    print(f"✓ Built frontend/materials.json — {len(materials)} materials")


if __name__ == "__main__":
    main()
