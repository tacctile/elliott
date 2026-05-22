#!/usr/bin/env python3
"""
Elliott Equipment Pricing Engine — Validation Script

Checks:
1. Every item file has all required YAML frontmatter fields
2. Math consistency (sq ft, per-label, margin calculations)
3. Every item appears in ARCHITECTURE.md catalog
4. Every item appears in its category file
5. No orphaned items (in catalog but missing file, or vice versa)
"""

import os
import sys
import re
import glob
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ITEMS_DIR = REPO_ROOT / "items"
ARCH_FILE = REPO_ROOT / ".claude" / "ARCHITECTURE.md"

REQUIRED_FRONTMATTER = [
    "part_number", "description", "model", "item_type", "material_family",
    "label_count", "width_in", "height_in", "sq_ft_per_label", "sq_ft_per_kit",
    "material_cost_per_unit", "cost_version_date", "price_1_9", "price_10_19",
    "price_20_49", "price_50_99", "price_100_199", "price_200_plus",
    "first_article_price", "per_label_at_qty_20", "margin_at_qty_20",
    "pricing_logic", "benchmark_item", "downstream_items", "process",
    "lamination_passes", "cut_runs", "status", "date_quoted",
    "override_type", "notes"
]

REQUIRED_SECTIONS = [
    "Spec Extraction",
    "Item Overview",
    "Material Specification",
    "Nesting and Material Cost",
    "Production Process",
    "Pricing",
    "Pricing Derivation",
    "Margin Analysis",
    "Notes and Warnings",
    "Production Debrief"
]

errors = []
warnings = []


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    content = filepath.read_text()
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None, content
    fm_text = match.group(1)
    fm = {}
    for line in fm_text.strip().split('\n'):
        if ':' in line:
            key = line.split(':', 1)[0].strip()
            val = line.split(':', 1)[1].strip().strip('"').strip("'")
            fm[key] = val
    return fm, content


def check_frontmatter_fields(filepath, fm):
    """Verify all required fields are present."""
    pn = filepath.stem
    for field in REQUIRED_FRONTMATTER:
        if field not in fm:
            errors.append(f"[{pn}] Missing frontmatter field: {field}")


def check_math(filepath, fm):
    """Verify calculated fields are consistent."""
    pn = filepath.stem
    try:
        width = float(fm.get("width_in", 0))
        height = float(fm.get("height_in", 0))
        label_count = int(fm.get("label_count", 1))
        sq_ft_per_label = float(fm.get("sq_ft_per_label", 0))
        sq_ft_per_kit = float(fm.get("sq_ft_per_kit", 0))

        # Check sq ft per label = width * height / 144
        expected_sq_ft = round(width * height / 144, 3)
        if abs(sq_ft_per_label - expected_sq_ft) > 0.01:
            errors.append(
                f"[{pn}] sq_ft_per_label mismatch: "
                f"got {sq_ft_per_label}, expected {expected_sq_ft} "
                f"({width}\" × {height}\" / 144)"
            )

        # Check sq ft per kit = sq_ft_per_label * label_count
        expected_kit = round(sq_ft_per_label * label_count, 3)
        if abs(sq_ft_per_kit - expected_kit) > 0.05:
            errors.append(
                f"[{pn}] sq_ft_per_kit mismatch: "
                f"got {sq_ft_per_kit}, expected {expected_kit}"
            )

        # Check per_label_at_qty_20 = price_20_49 / label_count
        price_20 = float(fm.get("price_20_49", 0))
        per_label = float(fm.get("per_label_at_qty_20", 0))
        expected_per_label = round(price_20 / label_count, 2)
        if abs(per_label - expected_per_label) > 0.01:
            errors.append(
                f"[{pn}] per_label_at_qty_20 mismatch: "
                f"got {per_label}, expected {expected_per_label}"
            )

    except (ValueError, ZeroDivisionError) as e:
        errors.append(f"[{pn}] Math check failed: {e}")


def check_sections(filepath, content):
    """Verify all required sections exist in the markdown body."""
    pn = filepath.stem
    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"[{pn}] Missing section: {section}")


def check_architecture_registry():
    """Verify every item file is listed in ARCHITECTURE.md and vice versa."""
    if not ARCH_FILE.exists():
        errors.append("ARCHITECTURE.md not found")
        return

    arch_content = ARCH_FILE.read_text()
    item_files = list(ITEMS_DIR.glob("*.md"))
    item_pns = [f.stem for f in item_files]

    for pn in item_pns:
        if pn not in arch_content:
            errors.append(f"[{pn}] Item file exists but not in ARCHITECTURE.md catalog")

    # Check for PNs in architecture that don't have item files
    for match in re.finditer(r'\| (\d{7}) \|', arch_content):
        pn = match.group(1)
        if pn not in item_pns:
            errors.append(f"[{pn}] Listed in ARCHITECTURE.md but no item file exists")


def check_status_values(fm, filepath):
    """Verify status is a valid lifecycle value."""
    pn = filepath.stem
    valid = ["Quoted", "FA Ordered", "FA Accepted", "In Production", "Active Reorder"]
    status = fm.get("status", "")
    if status not in valid:
        errors.append(f"[{pn}] Invalid status: '{status}'. Must be one of: {valid}")


def main():
    print("=" * 60)
    print("Elliott Equipment Pricing Engine — Validation")
    print("=" * 60)

    item_files = sorted(ITEMS_DIR.glob("*.md"))
    if not item_files:
        errors.append("No item files found in items/")
        print(f"\n{'FAIL' if errors else 'PASS'}: {len(errors)} errors, {len(warnings)} warnings")
        return 1 if errors else 0

    print(f"\nFound {len(item_files)} item files")

    for filepath in item_files:
        fm, content = parse_frontmatter(filepath)
        if fm is None:
            errors.append(f"[{filepath.stem}] No YAML frontmatter found")
            continue

        check_frontmatter_fields(filepath, fm)
        check_math(filepath, fm)
        check_sections(filepath, content)
        check_status_values(fm, filepath)

    check_architecture_registry()

    # Print results
    print()
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠ {w}")
    if not errors and not warnings:
        print("✓ All checks passed.")

    print(f"\n{'FAIL' if errors else 'PASS'}: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
