#!/usr/bin/env python3
"""
Elliott Equipment Pricing Engine — Profile Calculator

Reads all item YAML frontmatter and computes pricing profile bands
by material family. Outputs a summary that can be compared against
the category files to verify consistency.

Usage:
    python scripts/profile.py                 # All families
    python scripts/profile.py "3M 180mC"      # Filter by family substring
"""

import os
import sys
import re
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).parent.parent
ITEMS_DIR = REPO_ROOT / "items"


def parse_frontmatter(filepath):
    """Extract YAML frontmatter fields."""
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


def safe_float(val, default=0.0):
    try:
        return float(val)
    except (ValueError, TypeError):
        return default


def safe_int(val, default=0):
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return default


def main():
    filter_family = sys.argv[1] if len(sys.argv) > 1 else None

    items_by_family = defaultdict(list)
    item_files = sorted(ITEMS_DIR.glob("*.md"))

    for filepath in item_files:
        fm = parse_frontmatter(filepath)
        if fm is None:
            continue
        family = fm.get("material_family", "Unknown")
        if filter_family and filter_family.lower() not in family.lower():
            continue
        items_by_family[family].append(fm)

    if not items_by_family:
        print("No items found" + (f" matching '{filter_family}'" if filter_family else ""))
        return

    for family, items in sorted(items_by_family.items()):
        print("=" * 60)
        print(f"PRICING PROFILE: {family}")
        print(f"Data points: {len(items)}")
        print("=" * 60)

        # Collect items by type for per-type band summaries
        items_by_type = defaultdict(list)

        for item in items:
            pn = item.get("part_number", "???")
            label_count = safe_int(item.get("label_count"), 1)
            sq_ft = safe_float(item.get("sq_ft_per_label"))
            sq_ft_kit = safe_float(item.get("sq_ft_per_kit"))
            price_20 = safe_float(item.get("price_20_49"))
            price_200 = safe_float(item.get("price_200_plus"))
            material = safe_float(item.get("material_cost_per_unit"))
            per_label = safe_float(item.get("per_label_at_qty_20"))
            status = item.get("status", "")
            item_type = item.get("item_type", "")
            lam_passes = safe_int(item.get("lamination_passes"))

            # Computed metrics
            price_per_sq_ft_20 = price_20 / sq_ft_kit if sq_ft_kit > 0 else 0
            margin_20 = (price_20 - material) / price_20 * 100 if price_20 > 0 else 0
            margin_200 = (price_200 - material) / price_200 * 100 if price_200 > 0 else 0
            price_1_9 = safe_float(item.get("price_1_9"))
            compression = (1 - price_200 / price_1_9) * 100 if price_1_9 > 0 else 0

            print(f"\n  P/N {pn} — {item_type}")
            print(f"    Status: {status}")
            print(f"    Labels: {label_count} | Sq ft/label: {sq_ft:.3f} | Sq ft/unit: {sq_ft_kit:.3f}")
            print(f"    Material cost: ${material:.2f}")
            print(f"    Price @ qty 20: ${price_20:.2f} | Per label: ${per_label:.2f}")
            print(f"    $/sq ft @ qty 20: ${price_per_sq_ft_20:.2f}")
            print(f"    Margin @ qty 20: {margin_20:.1f}%")
            print(f"    Margin @ 200+: {margin_200:.1f}%")
            print(f"    Tier compression (1-9 → 200+): {compression:.0f}%")
            print(f"    Lam passes: {lam_passes}")

            items_by_type[item_type].append(item)

        # Band summaries split by item_type
        for itype in sorted(items_by_type.keys()):
            type_items = items_by_type[itype]
            prices_per_sqft = []
            margins_20 = []
            margins_200 = []
            compressions = []

            for item in type_items:
                sq_ft_kit = safe_float(item.get("sq_ft_per_kit"))
                price_20 = safe_float(item.get("price_20_49"))
                price_200 = safe_float(item.get("price_200_plus"))
                price_1_9 = safe_float(item.get("price_1_9"))
                material = safe_float(item.get("material_cost_per_unit"))

                if sq_ft_kit > 0 and price_20 > 0:
                    prices_per_sqft.append(price_20 / sq_ft_kit)
                    margins_20.append((price_20 - material) / price_20 * 100)
                if price_200 > 0:
                    margins_200.append((price_200 - material) / price_200 * 100)
                if price_1_9 > 0 and price_200 > 0:
                    compressions.append((1 - price_200 / price_1_9) * 100)

            if prices_per_sqft:
                print(f"\n  --- BAND SUMMARY: {itype} ---")
                print(f"  $/sq ft @ qty 20: ${min(prices_per_sqft):.2f} – ${max(prices_per_sqft):.2f}")
                print(f"  Margin @ qty 20:  {min(margins_20):.1f}% – {max(margins_20):.1f}%")
                print(f"  Margin @ 200+:    {min(margins_200):.1f}% – {max(margins_200):.1f}%")
                print(f"  Tier compression: {min(compressions):.0f}% – {max(compressions):.0f}%")
        print()


if __name__ == "__main__":
    main()
