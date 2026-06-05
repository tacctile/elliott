#!/usr/bin/env python3
"""
Elliott Equipment Pricing Engine — Calculator Config Builder

Reads governance documents, category files, item frontmatter, and material
frontmatter; extracts all calculator constants; and writes
frontend/calculator_config.json. This file is the single source of truth
for the calculator's logic — no calculator constants are hardcoded in the
HTML.

When pricing rules change, update the named constants at the top of this
file (or update the upstream material/item files for fields that are read
dynamically) and re-run.

Usage:
    python scripts/build_calculator_config.py
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
MATERIALS_DIR = REPO_ROOT / "materials"
ITEMS_DIR = REPO_ROOT / "items"
OUTPUT_FILE = REPO_ROOT / "frontend" / "calculator_config.json"

VERSION = "1.0"

# ---------------------------------------------------------------------------
# ACCOUNT-LEVEL CONSTANTS
# Source: governance/PRICING_RULES.md §25 (full bleed ink), §26 (invoice protection)
# Floor value itself is read dynamically from items/1230820.md.
# ---------------------------------------------------------------------------

FLOOR_SOURCE_PN = "1230820"
FLOOR_LABEL = "One-off job-economics floor (1230820 FA price)"

MOQ_PRINTED_LAMINATED = {
    "applies": False,
    "note": "No MOQ on this account. All items priced at real per-unit rates starting at qty 1.",
}

# ---------------------------------------------------------------------------
# ROUTING THRESHOLDS
# Source: categories/printed-laminated-orajet.md (band scope),
#         governance/PRODUCTION.md (equipment limits).
# ---------------------------------------------------------------------------

ROUTING = {
    "tiny_threshold_sq_ft": 0.1,
    "sub_scope_floor_sq_ft": 0.1,
    "sub_scope_ceiling_sq_ft": 0.5,
    "singles_band_floor_sq_ft": 0.5,
    "singles_band_ceiling_sq_ft": 2.0,
    "laminator_max_width_in": 13.5,
    "roland_max_print_width_in": 28.0,
    "parity_max_lam_passes": 2,
    "cut_vinyl_band_thresholds": {
        "band_c_ceiling_sq_ft": 1.0,
        "band_b_floor_sq_ft": 5.0,
    },
}

# ---------------------------------------------------------------------------
# BAND CONSTANTS
# Source: categories/cut-vinyl-3m-180mc.md, categories/printed-laminated-orajet.md
# ---------------------------------------------------------------------------

CUT_VINYL_LETTERING_BAND = {
    "concession_phase": {
        "min_per_sq_ft_qty_20": 13.65,
        "max_per_sq_ft_qty_20": 13.94,
        "anchor_pn": "1205720",
        "note": "Relationship Concession phase — Rule 14 deviation acknowledged. All 4 current cut vinyl items priced within this band by design.",
    },
    "ai_consensus": {
        "min_per_sq_ft_qty_20": 14.84,
        "max_per_sq_ft_qty_20": 16.41,
        "note": "Would-be normalized band per AI consensus. Normalization planned January 2027.",
    },
    "active_band": "concession_phase",
    "margin_floor_warn_pct": 57.0,
    "margin_floor_stop_pct": 50.0,
    "margin_target_qty_20_min_pct": 73.0,
    "margin_target_qty_20_max_pct": 78.0,
    "tier_compression_pct": 51.0,
    "default_tier_template": {
        "price_1_9": 45,
        "price_10_19": 40,
        "price_20_49": 35,
        "price_50_99": 30,
        "price_100_199": 26,
        "price_200_plus": 22,
    },
    "snap_granularity": {
        "above_50": 5,
        "25_to_50": 5,
        "10_to_25": 1,
        "below_10": 0.25,
    },
    "calibration_note": "Band calibrated at 2.51-2.56 sq ft. Items at significantly different sq ft require validation.",
    "large_format": {
        "threshold_sq_ft": 5.0,
        "anchor_psf_qty_20": 11.03,
        "anchor_pn": "3010704",
        "anchor_price_qty_20": 78.00,
        "anchor_sq_ft": 7.069,
        "tier_template": {
            "price_1_9": 105,
            "price_10_19": 92,
            "price_20_49": 78,
            "price_50_99": 68,
            "price_100_199": 60,
            "price_200_plus": 52,
        },
        "note": "Band B — founding data point 3010704 at 7.069 sq ft. 19.3% step-down from Band A. 4-wave AI validated.",
    },
    "sub_1_sqft": {
        "threshold_sq_ft": 1.0,
        "anchor_psf_qty_20": 20.64,
        "anchor_pn": "3010707",
        "anchor_price_qty_20": 20.00,
        "anchor_sq_ft": 0.969,
        "tier_template": {
            "price_1_9": 28,
            "price_10_19": 24,
            "price_20_49": 20,
            "price_50_99": 16.50,
            "price_100_199": 13.50,
            "price_200_plus": 11.50,
        },
        "note": "Band C — founding data point cluster 3010707/08/09 at 0.969 sq ft. 51% step-up from Band A. 4-wave AI validated + final industry audit.",
    },
}

PRINTED_LAMINATED_SINGLES_BAND = {
    "min_per_sq_ft_qty_20": 15.43,
    "max_per_sq_ft_qty_20": 15.91,
    "anchor_pn": "1230820",
    "anchor_psf": 15.43,
    "margin_floor_warn_pct": 64.0,
    "margin_floor_stop_pct": 50.0,
    "margin_target_qty_20_min_pct": 83.0,
    "margin_target_qty_20_max_pct": 84.0,
    "tier_ratios": {
        "1_9": 1.50,
        "10_19": 1.20,
        "20_49": 1.00,
        "50_99": 0.85,
        "100_199": 0.70,
        "200_plus": 0.55,
    },
    "snap_granularity": {
        "above_50": 5,
        "25_to_50": 1,
        "10_to_25": 0.50,
        "below_10": 0.25,
    },
    "note": "Band anchored at 1230820 ($15.43/sq ft). 1082570 AI-validated at $15.91/sq ft. Band is narrowing.",
}

PRINTED_LAMINATED_MICRO_BAND = {
    "anchor_psf_qty_20": 30.86,
    "anchor_pn": "1279000",
    "anchor_price_qty_20": 3.00,
    "anchor_sq_ft": 0.097,
    "threshold_sq_ft": 0.1,
    "margin_floor_warn_pct": 85.0,
    "margin_floor_stop_pct": 50.0,
    "margin_target_qty_20_min_pct": 90.0,
    "margin_target_qty_20_max_pct": 95.0,
    "tier_ratios": {
        "1_9": 1.50,
        "10_19": 1.167,
        "20_49": 1.00,
        "50_99": 0.867,
        "100_199": 0.767,
        "200_plus": 0.70,
    },
    "tier_template": {
        "price_1_9": 4.50,
        "price_10_19": 3.50,
        "price_20_49": 3.00,
        "price_50_99": 2.60,
        "price_100_199": 2.30,
        "price_200_plus": 2.10,
    },
    "snap_granularity": {
        "above_50": 5,
        "25_to_50": 1,
        "10_to_25": 0.50,
        "below_10": 0.10,
    },
    "note": "Sub-0.1 sq ft micro-format band — founding data point 1279000 at 0.097 sq ft. 100% step-up from singles band. Fixed-labor dominance. 4-wave AI validated + final 6-model comprehensive review. Per-label floor ~$2.50-$3.00 overrides $/sq ft scaling below ~0.06 sq ft.",
}

PRINTED_LAMINATED_KITS_BAND = {
    "per_label_qty_20": 10.00,
    "per_sq_ft_qty_20": 16.42,
    "per_sq_ft_premium_over_singles_pct": 6.0,
    "margin_floor_warn_pct": 83.0,
    "margin_floor_stop_pct": 50.0,
    "parity_applies_when": "same_dimensions AND same_material AND lam_passes <= 2",
    "tier_compression_pct": 60.0,
    "tier_template_3label": {
        "price_1_9": 45,
        "price_10_19": 36,
        "price_20_49": 30,
        "price_50_99": 26,
        "price_100_199": 21,
        "price_200_plus": 18,
    },
    "tier_template_5label": {
        "price_1_9": 75,
        "price_10_19": 60,
        "price_20_49": 50,
        "price_50_99": 43,
        "price_100_199": 35,
        "price_200_plus": 30,
    },
    "note": "Per-label parity at $10.00/label qty 20. Kit premium ~6% over singles intentional — matched-set collation, multi-label inspection, controlled-set packaging.",
}

# ---------------------------------------------------------------------------
# MATERIAL CONSTANTS
# cost_per_sq_ft and verified_date are read dynamically from materials/*.md.
# Static fields (material_id, roll_width_in, max_width_in) listed here.
# ---------------------------------------------------------------------------

MATERIAL_CONSTANTS_STATIC = {
    "orajet_3951": {
        "material_id": "orajet-3951-white",
        "extra": {"roll_width_in": 30},
    },
    "polyester_lam_1mil": {
        "material_id": "1mil-polyester-overlaminate",
        "extra": {"max_width_in": 13.5},
    },
    "transferrite_582u": {
        "material_id": "transferrite-582u",
        "extra": {},
    },
    "transferrite_582u_30in": {
        "material_id": "transferrite-582u-30in",
        "extra": {"roll_width_in": 30},
    },
}

# ---------------------------------------------------------------------------
# CUT VINYL COLORS
# cost_per_linear_yd and verified_date read dynamically from materials/*.md.
# ---------------------------------------------------------------------------

CUT_VINYL_COLORS_STATIC = {
    "cardinal_red": {
        "material_id": "3m-180mc-cardinal-red",
        "extra": {
            "roll_width_in": 24,
            "roll_width_ft": 2.0,
            "available_widths_in": [24],
        },
    },
    "cardinal_red_15in": {
        "material_id": "3m-180mc-cardinal-red-15in",
        "extra": {
            "roll_width_in": 15,
            "roll_width_ft": 1.25,
            "available_widths_in": [15],
        },
    },
    "olympic_blue": {
        "material_id": "3m-180mc-olympic-blue",
        "extra": {
            "roll_width_in": 24,
            "roll_width_ft": 2.0,
            "available_widths_in": [24],
            "pms_note": "Visual approximation of PMS 2386 C — not a certified Pantone match. Disclose in quote.",
        },
    },
    "white_24in": {
        "material_id": "3m-180mc-white-24in",
        "extra": {
            "roll_width_in": 24,
            "roll_width_ft": 2.0,
            "available_widths_in": [24, 48],
        },
    },
    "white_48in": {
        "material_id": "3m-180mc-white-48in",
        "extra": {
            "roll_width_in": 48,
            "roll_width_ft": 4.0,
            "available_widths_in": [48],
        },
    },
    "black": {
        "material_id": "3m-180mc-black",
        "extra": {
            "roll_width_in": 24,
            "roll_width_ft": 2.0,
            "available_widths_in": [24],
        },
    },
    "white_24in_50yd": {
        "material_id": "3m-180mc-white-24in-50yd",
        "extra": {
            "roll_width_in": 24,
            "roll_width_ft": 2.0,
            "available_widths_in": [24],
        },
    },
}

# ---------------------------------------------------------------------------
# INK RATES
# Source: governance/PRODUCTION.md (Account-Wide Ink Coverage Standard),
#         governance/PRICING_RULES.md §25 (full bleed account-wide rule),
#         .claude/MASTER_CONTEXT.md Core Rule 9.
#
# ACCOUNT-WIDE DEFAULT (established 2026-06-01):
#   `full_bleed_flood_coat` is the account default for ALL Elliott
#   printed/laminated items. No medium / low / partial coverage routing
#   is permitted on this account. The other rate keys (low/medium/high,
#   flood_coat, flood_coat_safety_red) are retained for historical/audit
#   visibility only — they are NOT routing targets for new pricing.
#
# Rate values are NOT changed in this session — only the default
# assumption documentation is updated. The account-wide rate is
# $0.50/sq ft × full label sq ft; an incidental buffer is then applied
# to round material totals conservatively upward (judgment, not fixed).
# ---------------------------------------------------------------------------

INK_RATES = {
    "default_coverage": "full_bleed_flood_coat",
    "default_note": "Account-wide standard for ALL Elliott printed/laminated items. Established 2026-06-01. See PRICING_RULES.md §25 and PRODUCTION.md Account-Wide Ink Coverage Standard.",
    "full_bleed_flood_coat": {
        "account_default": True,
        "cost_per_sq_ft": 0.50,
        "incidental_buffer": "judgment-applied; round material total conservatively upward (setup scrap, registration pulls, minor waste). Not a fixed value.",
        "applies_to": "All Elliott printed/laminated items — past, present, and future. No partial coverage routing permitted.",
        "canonical_formula": "(Orajet 3951 sq ft × $1.21) + (laminate sq ft × $0.2389) + (label sq ft × $0.50) + incidental buffer",
        "note": "Full bleed / full coverage at $0.50/sq ft. This is the only ink routing on this account.",
    },
    "low": {
        "cost_per_label_typical": 0.10,
        "note": "DEPRECATED for routing — historical reference only. Account uses full_bleed_flood_coat exclusively.",
    },
    "medium": {
        "cost_per_sq_ft": 0.44,
        "note": "DEPRECATED for routing — historical reference only. Account uses full_bleed_flood_coat exclusively.",
    },
    "high": {
        "cost_per_label_typical": 0.40,
        "note": "DEPRECATED for routing — historical reference only. Account uses full_bleed_flood_coat exclusively.",
    },
    "flood_coat": {
        "cost_per_label_min": 0.40,
        "cost_per_label_max": 0.60,
        "placeholder": 0.25,
        "placeholder_note": "Historical placeholder reference. Account-wide standard is full_bleed_flood_coat at $0.50/sq ft (see default_coverage above).",
        "unverified": True,
    },
    "flood_coat_safety_red": {
        "cost_per_label_min": 0.40,
        "cost_per_label_max": 0.50,
        "placeholder": 0.25,
        "unverified": True,
        "note": "Historical reference for the 1210810 placeholder period. Superseded by full_bleed_flood_coat account-wide standard (2026-06-01).",
    },
}

# ---------------------------------------------------------------------------
# DO NOT BENCHMARK
# Source: ARCHITECTURE.md Precedent Chain warnings,
#         categories/printed-laminated-orajet.md tiny-label callout.
# ---------------------------------------------------------------------------

DO_NOT_BENCHMARK = {
    "1277970": "One-off program peer — $55 floor pricing, not a catalog rate",
    "1277980": "One-off program peer — $55 floor pricing, not a catalog rate",
    "1277990": "One-off program peer — $55 floor pricing, not a catalog rate",
    "1278000": "One-off program peer — $55 floor pricing, not a catalog rate",
    "3017583": "Standalone one-off — $55 floor pricing, not a catalog rate",
    "3017584": "Standalone one-off — $55 floor pricing, not a catalog rate",
    "1210810": "Sub-scope single — excluded from band data points until production-volume acceptance",
    "1082570": "Initial order was $42 flat job-economics (not a catalog rate). Production tier table is valid for reorder volumes.",
}

# ---------------------------------------------------------------------------
# OVERRIDE TYPE PRECEDENT
# Source: ARCHITECTURE.md Override Types table, PRICING_RULES.md §13.
# ---------------------------------------------------------------------------

OVERRIDE_TYPE_PRECEDENT = {
    "Relationship Concession": False,
    "One-Time Exception": False,
    "Capacity Fill": False,
    "Owner Judgment": "case_by_case",
    "Competitive Defense": True,
    "Strategic Anchor": True,
}

# ---------------------------------------------------------------------------
# QUOTE LANGUAGE
# Source: categories/printed-laminated-orajet.md tiny-label / one-off framing.
# ---------------------------------------------------------------------------

QUOTE_LANGUAGE = {
    "tiny_one_off_program": "One-time minimum program charge: $55.00 total",
    "anchor_line_template": "Label measures {width}\" × {height}\" ({sq_ft} sq ft) in {material} — priced at ${price} at your projected monthly volume.",
    "pms_caveat_template": "{color} is a visual approximation of {pms_code} — not a certified Pantone match.",
    "ink_unverified_note": "Ink cost is a placeholder pending first production run. Update material_cost_per_unit after run.",
    "sub_scope_note": "Dimensional scope exclusion: this item is below the 0.5 sq ft singles band floor. Band-consistent $/sq ft applies. Excluded from band data points until production-volume acceptance confirmed.",
    "rule_14_note": "Rule 14 deviation: benchmarked against a Relationship Concession item. AI consensus band: ${min}-${max}/sq ft.",
}

# ---------------------------------------------------------------------------
# FLAG THRESHOLDS
# Source: governance/PRICING_RULES.md (margin discipline),
#         PRICING_VALIDATION.md (band tolerance).
# ---------------------------------------------------------------------------

FLAG_THRESHOLDS = {
    "material_staleness_warn_days": 180,
    "material_staleness_stop_days": 365,
    "margin_stop_any_tier_pct": 50.0,
    "margin_warn_200plus_pct": 57.0,
    "margin_warn_qty20_pct": 64.0,
    "band_tolerance_pct": 15.0,
}


# ---------------------------------------------------------------------------
# Frontmatter parsing — adapted from build_materials.py / build_frontend.py
# ---------------------------------------------------------------------------

def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file as a flat dict."""
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
        if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
            val = raw[1:-1]
        else:
            val = raw
        fm[key] = val
    return fm


def read_material(material_id):
    """Load a material's frontmatter by material_id (file stem)."""
    fm = parse_frontmatter(MATERIALS_DIR / f"{material_id}.md")
    if fm is None:
        raise FileNotFoundError(f"Material file not found or has no frontmatter: {material_id}")
    return fm


def to_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return val


# ---------------------------------------------------------------------------
# Build sections
# ---------------------------------------------------------------------------

def build_account_section():
    item_1230820 = parse_frontmatter(ITEMS_DIR / f"{FLOOR_SOURCE_PN}.md")
    if item_1230820 is None:
        raise FileNotFoundError(f"items/{FLOOR_SOURCE_PN}.md not found or has no frontmatter")
    floor = to_float(item_1230820["first_article_price"])
    return {
        "floor": floor,
        "floor_source_pn": FLOOR_SOURCE_PN,
        "floor_label": FLOOR_LABEL,
        "moq": {
            "printed_laminated": MOQ_PRINTED_LAMINATED,
        },
    }


def build_material_constants():
    out = {}
    for key, spec in MATERIAL_CONSTANTS_STATIC.items():
        fm = read_material(spec["material_id"])
        entry = {
            "cost_per_sq_ft": to_float(fm["cost_per_sq_ft"]),
            "material_id": spec["material_id"],
            "verified_date": fm["verified_date"],
        }
        entry.update(spec["extra"])
        out[key] = entry
    return out


def build_cut_vinyl_colors():
    out = {}
    for key, spec in CUT_VINYL_COLORS_STATIC.items():
        fm = read_material(spec["material_id"])
        entry = {
            "material_id": spec["material_id"],
            "cost_method": "length_based",
            "cost_per_linear_yd": to_float(fm["cost_per_linear_yd"]),
        }
        entry.update(spec["extra"])
        entry["verified_date"] = fm["verified_date"]
        out[key] = entry
    return out


def build_config():
    return {
        "generated": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "version": VERSION,
        "account": build_account_section(),
        "routing": ROUTING,
        "bands": {
            "cut_vinyl_lettering": CUT_VINYL_LETTERING_BAND,
            "printed_laminated_singles": PRINTED_LAMINATED_SINGLES_BAND,
            "printed_laminated_micro": PRINTED_LAMINATED_MICRO_BAND,
            "printed_laminated_kits": PRINTED_LAMINATED_KITS_BAND,
        },
        "material_constants": build_material_constants(),
        "ink_rates": INK_RATES,
        "cut_vinyl_colors": build_cut_vinyl_colors(),
        "do_not_benchmark": DO_NOT_BENCHMARK,
        "override_type_precedent": OVERRIDE_TYPE_PRECEDENT,
        "quote_language": QUOTE_LANGUAGE,
        "flag_thresholds": FLAG_THRESHOLDS,
    }


def main():
    config = build_config()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(config, indent=2))
    n_materials = len(config["material_constants"])
    n_bands = len(config["bands"])
    n_dnb = len(config["do_not_benchmark"])
    print(
        f"✓ Built frontend/calculator_config.json — "
        f"{n_materials} material constants, {n_bands} bands, {n_dnb} do_not_benchmark items"
    )


if __name__ == "__main__":
    main()
