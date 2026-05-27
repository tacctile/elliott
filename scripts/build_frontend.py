#!/usr/bin/env python3
"""
Elliott Equipment Pricing Engine — Frontend Data Builder

Reads all item YAML frontmatter, detects all files in items/images/,
copies them into frontend/images/, and writes frontend/data.json.

Run after any item or file change. Also runs via GitHub Action on push.

Usage:
    python scripts/build_frontend.py
"""

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ITEMS_DIR = REPO_ROOT / "items"
SOURCE_IMAGES = REPO_ROOT / "items" / "images"
FRONTEND_DIR = REPO_ROOT / "frontend"
FRONTEND_IMAGES = FRONTEND_DIR / "images"
OUTPUT_FILE = FRONTEND_DIR / "data.json"

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', '.bmp', '.tiff'}
DOC_EXTS = {'.pdf'}
ALL_EXTS = IMAGE_EXTS | DOC_EXTS

# Internal fields that must never be exposed in the public data.json
STRIP_FIELDS = {
    'benchmark_item',
    'downstream_items',
    'override_type',
}


def sync_images():
    """Mirror items/images/ → frontend/images/. Copies new/changed, removes deleted."""
    FRONTEND_IMAGES.mkdir(parents=True, exist_ok=True)

    source_files = {}
    if SOURCE_IMAGES.exists():
        for f in SOURCE_IMAGES.iterdir():
            if f.is_file() and f.suffix.lower() in ALL_EXTS:
                source_files[f.name] = f

    # Copy new or updated files
    copied = 0
    for name, src in source_files.items():
        dest = FRONTEND_IMAGES / name
        src_mtime = src.stat().st_mtime
        if not dest.exists() or dest.stat().st_mtime < src_mtime:
            shutil.copy2(src, dest)
            copied += 1

    # Remove files in frontend/images/ that no longer exist in source
    removed = 0
    for f in FRONTEND_IMAGES.iterdir():
        if f.is_file() and f.name not in source_files and f.name != '.gitkeep':
            f.unlink()
            removed += 1

    return len(source_files), copied, removed


def find_files_for_item(part_number):
    """Find all files in frontend/images/ matching a part number.
    
    Matches:
      {PN}.pdf, {PN}.png, etc.         — exact match
      {PN}_1.png, {PN}_2.png, etc.     — multi-page
    
    Returns list of {type, path} relative to frontend/.
    """
    files = []

    if not FRONTEND_IMAGES.exists():
        return None

    for f in sorted(FRONTEND_IMAGES.iterdir()):
        if not f.is_file():
            continue
        stem = f.stem
        ext = f.suffix.lower()

        # Match exact PN or PN_N pattern
        if stem == part_number or (stem.startswith(part_number + '_') and stem[len(part_number)+1:].isdigit()):
            if ext == '.pdf':
                files.append({"type": "pdf", "path": f"images/{f.name}"})
            elif ext in IMAGE_EXTS:
                files.append({"type": "image", "path": f"images/{f.name}"})

    return files if files else None


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
    body = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    sections = {}
    parts = re.split(r'\n# ', body)
    for part in parts[1:]:
        lines = part.split('\n', 1)
        heading = lines[0].strip()
        body_text = lines[1].strip() if len(lines) > 1 else ''
        sections[heading] = body_text
    return sections


def coerce_numeric(val):
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
    fm = parse_frontmatter(filepath)
    if fm is None:
        return None

    pn = fm.get('part_number', filepath.stem)
    sections = extract_sections(filepath)

    for key in NUMERIC_FIELDS:
        if key in fm and fm[key] != '':
            fm[key] = coerce_numeric(fm[key])

    for field in STRIP_FIELDS:
        fm.pop(field, None)

    item = {
        'frontmatter': fm,
        'image': find_files_for_item(pn),
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
    # Step 1: Sync files from items/images/ → frontend/images/
    total_files, copied, removed = sync_images()
    print(f"✓ Synced images: {total_files} files ({copied} copied, {removed} removed)")

    # Step 2: Build data.json
    item_files = sorted(ITEMS_DIR.glob("*.md"))
    items = {}

    for filepath in item_files:
        item = build_item(filepath)
        if item:
            pn = item['frontmatter']['part_number']
            items[pn] = item

    output = {
        'generated': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'item_count': len(items),
        'items': items
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(output, indent=2))
    print(f"✓ Built frontend/data.json — {len(items)} items")


if __name__ == "__main__":
    main()
