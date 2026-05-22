#!/usr/bin/env python3
"""
Elliott Equipment Pricing Engine — Frontend Data Builder

Reads all item YAML frontmatter and exports a single JSON file
for the static HTML frontend. Run after any item change.

Usage:
    python scripts/build_frontend.py
"""

import json
import re
import os
from pathlib import Path
from collections import OrderedDict

REPO_ROOT = Path(__file__).parent.parent
ITEMS_DIR = REPO_ROOT / "items"
IMAGES_DIR = REPO_ROOT / "items" / "images"
OUTPUT_FILE = REPO_ROOT / "frontend" / "data.json"


def parse_frontmatter(filepath):
    """Extract YAML frontmatter fields from an item markdown file."""
    content = filepath.read_text()
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    fm = {}
    for line in match.group(1).strip().split('\n'):
        if ':' in line:
            key = line.split(':', 1)[0].strip()
            val = line.split(':', 1)[1].strip().strip('"').strip("'")
            fm[key] = val
    return fm


def extract_sections(filepath):
    """Extract key prose sections from the markdown body."""
    content = filepath.read_text()
    # Strip frontmatter
    body = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)

    sections = {}
    # Extract each H1 section
    parts = re.split(r'\n# ', body)
    for part in parts[1:]:  # skip content before first heading
        lines = part.split('\n', 1)
        heading = lines[0].strip()
        body_text = lines[1].strip() if len(lines) > 1 else ''
        sections[heading] = body_text

    return sections


def check_image(part_number):
    """Check if an image exists for this part number."""
    for ext in ['png', 'jpg', 'jpeg', 'webp', 'svg']:
        img_path = IMAGES_DIR / f"{part_number}.{ext}"
        if img_path.exists():
            return f"items/images/{part_number}.{ext}"
    return None


def coerce_numeric(val):
    """Try to convert string to int or float."""
    try:
        if '.' in val:
            return float(val)
        return int(val)
    except (ValueError, TypeError):
        return val


NUMERIC_FIELDS = {
    'label_count', 'width_in', 'height_in', 'sq_ft_per_label', 'sq_ft_per_kit',
    'material_cost_per_unit', 'price_1_9', 'price_10_19', 'price_20_49',
    'price_50_99', 'price_100_199', 'price_200_plus', 'first_article_price',
    'per_label_at_qty_20', 'lamination_passes', 'cut_runs'
}


def build_item(filepath):
    """Build a complete item data object."""
    fm = parse_frontmatter(filepath)
    if fm is None:
        return None

    pn = fm.get('part_number', filepath.stem)
    sections = extract_sections(filepath)

    # Coerce numeric fields
    for key in NUMERIC_FIELDS:
        if key in fm and fm[key] != '':
            fm[key] = coerce_numeric(fm[key])

    item = {
        'frontmatter': fm,
        'image': check_image(pn),
        'sections': {
            'item_overview': sections.get('Item Overview', ''),
            'material_spec': sections.get('Material Specification', ''),
            'nesting': sections.get('Nesting and Material Cost', ''),
            'production': sections.get('Production Process', ''),
            'pricing_derivation': sections.get('Pricing Derivation', ''),
            'margin_analysis': sections.get('Margin Analysis', ''),
            'notes': sections.get('Notes and Warnings', ''),
            'production_debrief': sections.get('Production Debrief', ''),
        }
    }
    return item


def main():
    item_files = sorted(ITEMS_DIR.glob("*.md"))
    items = {}

    for filepath in item_files:
        item = build_item(filepath)
        if item:
            pn = item['frontmatter']['part_number']
            items[pn] = item

    output = {
        'generated': str(Path(os.popen('date -u +%Y-%m-%dT%H:%M:%SZ').read().strip())),
        'item_count': len(items),
        'items': items
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(output, indent=2))
    print(f"✓ Built frontend/data.json — {len(items)} items")


if __name__ == "__main__":
    main()
