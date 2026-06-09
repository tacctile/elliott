#!/usr/bin/env python3
"""
Elliott Pricing Engine v2 — Supabase Migration (Session H, 2026-06-09)

Seeds the elliott_* tables in the shared `prolabel` Supabase project from
the repo's source-of-truth files:

  1. materials/*.md (11 files)  -> elliott_materials
     (+ 1 synthetic row for eco-solvent ink so combinations can carry an
      `ink` component — ink is a rate in governance, not a repo file)
  2. items/*.md (23 files)      -> elliott_items (frontmatter mirrored;
     band_class + do_not_benchmark derived). EXCEPTION (Session I,
     2026-06-09 / audit D4): the internal strategy fields pricing_logic
     and notes are NOT written to the anon-readable elliott_items columns
     (they are nulled there) — they are routed to elliott_items_internal
     (part_number, pricing_logic, notes), which has RLS enabled with NO
     anon policies (service_role only). Never write internal strategy
     text to any anon-readable column.
  3. build_calculator_config.py constants -> elliott_pricing_bands
     (6 rows: cut_vinyl_a/b/c, printed_lam_singles/micro/kits)
  4. build_calculator_config.py constants -> elliott_account_settings
  5. Default material combinations from the documented item->material
     relationships (used_in_items)        -> elliott_material_combinations
                                            + components, and links each
                                            item's material_combination_id

Idempotent: upserts on material_key (materials), part_number (items),
band_key (bands), account_id (settings), (account_id, name) (combinations).
Combination components are replaced atomically per combination.

AUTH / RLS APPROACH (documented per Phase 1.4):
  - The deployed frontend uses the `anon` key (constants at the top of
    frontend/index.html). RLS gives anon SELECT on all elliott_* tables,
    and INSERT/UPDATE/DELETE only on the three Materials-Manager tables
    (elliott_materials, elliott_material_combinations,
    elliott_material_combination_components) with account_id = 'elliott'.
    The app itself sits behind Vercel password protection; no JWT-claim
    machinery is used for this single-user tool.
  - This script runs with the `service_role` key (full access, bypasses
    RLS). Items, pricing bands, and account settings are frontend-read-only
    by design — they change only through governed Claude Code sessions
    that run this script (or targeted service-role SQL).
  - Credentials come from the environment (or a local .env file):
        SUPABASE_URL=https://<project-ref>.supabase.co
        SUPABASE_SERVICE_ROLE_KEY=<service role key>
    Never hardcode the service role key anywhere in this repo, and never
    put it in frontend code.

Usage:
    python scripts/migrate_to_supabase.py             # live run (supabase-py)
    python scripts/migrate_to_supabase.py --dry-run   # report only, no writes
    python scripts/migrate_to_supabase.py --emit-sql  # print idempotent SQL
                                                      # (for psql / MCP runs)
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
MATERIALS_DIR = REPO_ROOT / "materials"
ITEMS_DIR = REPO_ROOT / "items"

sys.path.insert(0, str(Path(__file__).parent))
import build_calculator_config as bcc  # noqa: E402  (constants source of truth)

ACCOUNT_ID = "elliott"

# Repo material file stem -> calculator engine lookup key. Mirrors the
# static maps in build_calculator_config.py so the Supabase-hydrated
# config keeps the exact shape the engine already reads.
ENGINE_KEYS = {
    "3m-180mc-cardinal-red": "cardinal_red",
    "3m-180mc-cardinal-red-15in": "cardinal_red_15in",
    "3m-180mc-olympic-blue": "olympic_blue",
    "3m-180mc-white-24in": "white_24in",
    "3m-180mc-white-48in": "white_48in",
    "3m-180mc-black": "black",
    "3m-180mc-white-24in-50yd": "white_24in_50yd",
    "orajet-3951-white": "orajet_3951",
    "1mil-polyester-overlaminate": "polyester_lam_1mil",
    "transferrite-582u": "transferrite_582u",
    "transferrite-582u-30in": "transferrite_582u_30in",
    "eco-solvent-ink-full-bleed": "eco_solvent_ink",
}

# Synthetic material row: §25 full-bleed eco-solvent ink. Governance holds
# ink as a rate (PRICING_RULES.md §25, $0.50/sq ft, established 2026-06-01),
# not a roll SKU — this row exists so material combinations can carry an
# `ink` component with a real cost_per_sq_ft.
INK_MATERIAL = {
    "material_id": "eco-solvent-ink-full-bleed",
    "material_type": "other",
    "manufacturer": "Roland",
    "product_name": "Eco-Solvent Ink — Full Bleed (§25)",
    "product_code": "",
    "cost_per_sq_ft": 0.50,
    "verified_date": "2026-06-01",
    "distributor": "",
    "used_in_items": [],
    "notes": ("Account-wide full bleed / full coverage ink rate per "
              "PRICING_RULES.md §25 — $0.50/sq ft × full label sq ft on every "
              "printed/laminated item. Synthetic material row (rate, not a "
              "roll SKU) so combinations can carry an ink component."),
}

MATERIAL_NUMERIC_FIELDS = {
    "film_thickness_mil", "thickness_mil", "roll_width_in", "roll_length_yd",
    "roll_length_ft", "cost_per_roll", "cost_per_sq_ft", "cost_per_linear_yd",
    "cost_per_linear_ft", "cost_per_msi", "max_laminator_width_in",
}
MATERIAL_LIST_FIELDS = {
    "compatible_laminates", "compatible_substrates", "compatible_tapes",
    "compatible_cut_vinyls", "used_in_items",
}

ITEM_NUMERIC_FIELDS = {
    "label_count", "width_in", "height_in", "sq_ft_per_label", "sq_ft_per_kit",
    "material_cost_per_unit", "price_1_9", "price_10_19", "price_20_49",
    "price_50_99", "price_100_199", "price_200_plus", "first_article_price",
    "per_label_at_qty_20", "lamination_passes", "cut_runs",
}

# Default combination per item, when the used_in_items mapping is ambiguous
# (3017435 is listed on both White rolls; the 24" roll is the frontmatter-
# canonical higher-cost scenario per STRUCTURE_RULES conservative-cost rule).
ITEM_COMBO_PREFERENCE = {"3017435": "3m-180mc-white-24in"}


# ---------------------------------------------------------------------------
# Parsing (same conventions as build_materials.py / build_frontend.py)
# ---------------------------------------------------------------------------

def parse_list(val):
    val = val.strip()
    if not val or val == "[]":
        return []
    if val.startswith("[") and val.endswith("]"):
        return [x.strip().strip('"').strip("'")
                for x in val[1:-1].split(",") if x.strip().strip('"').strip("'")]
    return []


def coerce_numeric(val):
    if val in ("", None):
        return None
    try:
        return float(val) if "." in str(val) else int(val)
    except (ValueError, TypeError):
        return None


def parse_frontmatter(filepath, list_fields=(), numeric_fields=()):
    content = filepath.read_text()
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    fm = {}
    for line in match.group(1).strip().split("\n"):
        if ":" not in line:
            continue
        key = line.split(":", 1)[0].strip()
        raw = line.split(":", 1)[1].strip()
        if key in list_fields:
            fm[key] = parse_list(raw)
            continue
        if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
            val = raw[1:-1].replace('\\"', '"').replace("\\'", "'")
        else:
            val = raw
        if key in numeric_fields:
            fm[key] = coerce_numeric(val)
        else:
            fm[key] = val
    return fm


# ---------------------------------------------------------------------------
# Row builders
# ---------------------------------------------------------------------------

def build_material_rows():
    rows, skipped = [], []
    for f in sorted(MATERIALS_DIR.glob("*.md")):
        fm = parse_frontmatter(f, MATERIAL_LIST_FIELDS, MATERIAL_NUMERIC_FIELDS)
        if fm is None:
            skipped.append((f.name, "no frontmatter"))
            continue
        rows.append(material_row_from_fm(fm))
    rows.append(material_row_from_fm(dict(INK_MATERIAL)))
    return rows, skipped


def material_row_from_fm(fm):
    mid = fm["material_id"]
    compatible = {}
    for k in ("compatible_laminates", "compatible_substrates",
              "compatible_tapes", "compatible_cut_vinyls"):
        if fm.get(k):
            compatible[k] = fm[k]
    pms_note = None
    if mid == "3m-180mc-olympic-blue":
        pms_note = ("Visual approximation of PMS 2386 C — not a certified "
                    "Pantone match. Disclose in quote.")
    return {
        "account_id": ACCOUNT_ID,
        "material_key": mid,
        "engine_key": ENGINE_KEYS.get(mid),
        "material_family": fm.get("material_type", "other"),
        "manufacturer": fm.get("manufacturer", ""),
        "product_name": fm.get("product_name", ""),
        "product_code": fm.get("product_code", ""),
        "item_number": fm.get("item_number", ""),
        "color_name": fm.get("color_name") or fm.get("color", ""),
        "color_code": fm.get("color_code", ""),
        "film_type": fm.get("film_type", ""),
        "film_thickness_mil": fm.get("film_thickness_mil"),
        "thickness_mil": fm.get("thickness_mil"),
        "adhesive_type": fm.get("adhesive_type", ""),
        "finish": fm.get("finish", ""),
        "roll_width_in": fm.get("roll_width_in"),
        "roll_length_yd": fm.get("roll_length_yd"),
        "roll_length_ft": fm.get("roll_length_ft"),
        "cost_per_roll": fm.get("cost_per_roll"),
        "cost_per_linear_yd": fm.get("cost_per_linear_yd"),
        "cost_per_linear_ft": fm.get("cost_per_linear_ft"),
        "cost_per_sq_ft": fm.get("cost_per_sq_ft"),
        "cost_per_msi": fm.get("cost_per_msi"),
        "max_laminator_width_in": fm.get("max_laminator_width_in"),
        "pms_note": pms_note,
        "distributor": fm.get("distributor", ""),
        "verified_date": fm.get("verified_date"),
        "compatible_with": compatible,
        "used_in_items": fm.get("used_in_items", []),
        "notes": fm.get("notes", "") or "",
        "is_active": True,
    }


def derive_band_class(fm):
    family = fm.get("material_family", "")
    sq = fm.get("sq_ft_per_label") or 0
    flat = (fm.get("price_1_9") is not None
            and fm.get("price_1_9") == fm.get("price_200_plus"))
    if family.startswith("Orajet") and flat and (fm.get("label_count") or 1) == 1:
        return "tiny_one_off"   # 1277970-1278000, 3017583, 3017584
    if fm.get("item_type") == "Printed/Laminated Kit":
        return "kit"
    if family == "3M 180mC Cut Vinyl":
        if sq >= 5.0:
            return "cut_vinyl_b"
        if sq >= 1.0:
            return "cut_vinyl_a"
        return "cut_vinyl_c"
    # printed/laminated singles
    if sq < 0.1:
        return "singles_micro"      # 1279000 (production catalog item)
    if sq <= 0.5:
        return "singles_sub_scope"  # 1210810
    return "singles_standard"


def build_item_rows():
    rows, internal_rows, skipped = [], [], []
    dnb = dict(bcc.DO_NOT_BENCHMARK)
    for f in sorted(ITEMS_DIR.glob("*.md")):
        fm = parse_frontmatter(f, (), ITEM_NUMERIC_FIELDS)
        if fm is None:
            skipped.append((f.name, "no frontmatter"))
            continue
        pn = fm.get("part_number", f.stem)
        # Internal strategy fields -> service-role-only side table (D4).
        internal_rows.append({
            "account_id": ACCOUNT_ID,
            "part_number": pn,
            "pricing_logic": fm.get("pricing_logic", ""),
            "notes": fm.get("notes", ""),
        })
        rows.append({
            "account_id": ACCOUNT_ID,
            "part_number": pn,
            "description": fm.get("description", ""),
            "model": fm.get("model", ""),
            "item_type": fm.get("item_type", ""),
            "material_family": fm.get("material_family", ""),
            "label_count": int(fm.get("label_count") or 1),
            "width_in": fm.get("width_in"),
            "height_in": fm.get("height_in"),
            "sq_ft_per_label": fm.get("sq_ft_per_label"),
            "sq_ft_per_kit": fm.get("sq_ft_per_kit"),
            "material_cost_per_unit": fm.get("material_cost_per_unit"),
            "cost_version_date": fm.get("cost_version_date") or None,
            "price_1_9": fm.get("price_1_9"),
            "price_10_19": fm.get("price_10_19"),
            "price_20_49": fm.get("price_20_49"),
            "price_50_99": fm.get("price_50_99"),
            "price_100_199": fm.get("price_100_199"),
            "price_200_plus": fm.get("price_200_plus"),
            "first_article_price": fm.get("first_article_price"),
            "per_label_at_qty_20": fm.get("per_label_at_qty_20"),
            "margin_at_qty_20": fm.get("margin_at_qty_20", ""),
            # pricing_logic / notes deliberately blanked on the anon-readable
            # row (columns are NOT NULL) — content lives in
            # elliott_items_internal (D4).
            "pricing_logic": "",
            "benchmark_item": fm.get("benchmark_item", ""),
            "downstream_items": fm.get("downstream_items", ""),
            "process": fm.get("process", ""),
            "lamination_passes": (int(fm["lamination_passes"])
                                  if fm.get("lamination_passes") is not None else None),
            "cut_runs": (int(fm["cut_runs"])
                         if fm.get("cut_runs") is not None else None),
            "status": fm.get("status", "Quoted"),
            "date_quoted": fm.get("date_quoted") or None,
            "override_type": fm.get("override_type", ""),
            "notes": "",
            "band_class": derive_band_class(fm),
            "do_not_benchmark": pn in dnb,
            "do_not_benchmark_reason": dnb.get(pn, ""),
            "is_active": True,
        })
    return rows, internal_rows, skipped


def build_band_rows():
    cv = bcc.CUT_VINYL_LETTERING_BAND
    singles = bcc.PRINTED_LAMINATED_SINGLES_BAND
    micro = bcc.PRINTED_LAMINATED_MICRO_BAND
    kits = bcc.PRINTED_LAMINATED_KITS_BAND
    conc = cv["concession_phase"]
    return [
        {
            "band_key": "cut_vinyl_a",
            "anchor_psf_qty_20": None,
            "min_psf_qty_20": conc["min_per_sq_ft_qty_20"],
            "max_psf_qty_20": conc["max_per_sq_ft_qty_20"],
            "anchor_pn": conc["anchor_pn"],
            "anchor_price_qty_20": 35.00,
            "anchor_sq_ft": 2.56,
            "tier_ratios": None,
            "tier_template": cv["default_tier_template"],
            "snap_granularity": cv["snap_granularity"],
            "margin_floor_warn_pct": cv["margin_floor_warn_pct"],
            "margin_floor_stop_pct": cv["margin_floor_stop_pct"],
            "extra": {
                "active_band": cv["active_band"],
                "ai_consensus": cv["ai_consensus"],
                "margin_target_qty_20_min_pct": cv["margin_target_qty_20_min_pct"],
                "margin_target_qty_20_max_pct": cv["margin_target_qty_20_max_pct"],
                "tier_compression_pct": cv["tier_compression_pct"],
                "calibration_note": cv["calibration_note"],
                "concession_note": conc["note"],
            },
            "note": "Band A — Small-Format cut vinyl (1.0–5.0 sq ft), concession phase.",
        },
        {
            "band_key": "cut_vinyl_b",
            "anchor_psf_qty_20": cv["large_format"]["anchor_psf_qty_20"],
            "min_psf_qty_20": None,
            "max_psf_qty_20": None,
            "anchor_pn": cv["large_format"]["anchor_pn"],
            "anchor_price_qty_20": cv["large_format"]["anchor_price_qty_20"],
            "anchor_sq_ft": cv["large_format"]["anchor_sq_ft"],
            "tier_ratios": None,
            "tier_template": cv["large_format"]["tier_template"],
            "snap_granularity": cv["snap_granularity"],
            "margin_floor_warn_pct": cv["margin_floor_warn_pct"],
            "margin_floor_stop_pct": cv["margin_floor_stop_pct"],
            "extra": {"threshold_sq_ft": cv["large_format"]["threshold_sq_ft"]},
            "note": cv["large_format"]["note"],
        },
        {
            "band_key": "cut_vinyl_c",
            "anchor_psf_qty_20": cv["sub_1_sqft"]["anchor_psf_qty_20"],
            "min_psf_qty_20": None,
            "max_psf_qty_20": None,
            "anchor_pn": cv["sub_1_sqft"]["anchor_pn"],
            "anchor_price_qty_20": cv["sub_1_sqft"]["anchor_price_qty_20"],
            "anchor_sq_ft": cv["sub_1_sqft"]["anchor_sq_ft"],
            "tier_ratios": None,
            "tier_template": cv["sub_1_sqft"]["tier_template"],
            "snap_granularity": cv["snap_granularity"],
            "margin_floor_warn_pct": cv["margin_floor_warn_pct"],
            "margin_floor_stop_pct": cv["margin_floor_stop_pct"],
            "extra": {"threshold_sq_ft": cv["sub_1_sqft"]["threshold_sq_ft"]},
            "note": cv["sub_1_sqft"]["note"],
        },
        {
            "band_key": "printed_lam_singles",
            "anchor_psf_qty_20": singles["anchor_psf"],
            "min_psf_qty_20": singles["min_per_sq_ft_qty_20"],
            "max_psf_qty_20": singles["max_per_sq_ft_qty_20"],
            "anchor_pn": singles["anchor_pn"],
            "anchor_price_qty_20": 20.00,
            "anchor_sq_ft": 1.296,
            "tier_ratios": singles["tier_ratios"],
            "tier_template": None,
            "snap_granularity": singles["snap_granularity"],
            "margin_floor_warn_pct": singles["margin_floor_warn_pct"],
            "margin_floor_stop_pct": singles["margin_floor_stop_pct"],
            "extra": {
                "margin_target_qty_20_min_pct": singles["margin_target_qty_20_min_pct"],
                "margin_target_qty_20_max_pct": singles["margin_target_qty_20_max_pct"],
            },
            "note": singles["note"],
        },
        {
            "band_key": "printed_lam_micro",
            "anchor_psf_qty_20": micro["anchor_psf_qty_20"],
            "min_psf_qty_20": None,
            "max_psf_qty_20": None,
            "anchor_pn": micro["anchor_pn"],
            "anchor_price_qty_20": micro["anchor_price_qty_20"],
            "anchor_sq_ft": micro["anchor_sq_ft"],
            "tier_ratios": micro["tier_ratios"],
            "tier_template": micro["tier_template"],
            "snap_granularity": micro["snap_granularity"],
            "margin_floor_warn_pct": micro["margin_floor_warn_pct"],
            "margin_floor_stop_pct": micro["margin_floor_stop_pct"],
            "extra": {
                "threshold_sq_ft": micro["threshold_sq_ft"],
                "margin_target_qty_20_min_pct": micro["margin_target_qty_20_min_pct"],
                "margin_target_qty_20_max_pct": micro["margin_target_qty_20_max_pct"],
            },
            "note": micro["note"],
        },
        {
            "band_key": "printed_lam_kits",
            "anchor_psf_qty_20": kits["per_sq_ft_qty_20"],
            "min_psf_qty_20": None,
            "max_psf_qty_20": None,
            "anchor_pn": "1278930",
            "anchor_price_qty_20": 30.00,
            "anchor_sq_ft": 1.827,
            "tier_ratios": None,
            "tier_template": None,
            "snap_granularity": bcc.PRINTED_LAMINATED_SINGLES_BAND["snap_granularity"],
            "margin_floor_warn_pct": kits["margin_floor_warn_pct"],
            "margin_floor_stop_pct": kits["margin_floor_stop_pct"],
            "extra": {
                "per_label_qty_20": kits["per_label_qty_20"],
                "per_sq_ft_premium_over_singles_pct": kits["per_sq_ft_premium_over_singles_pct"],
                "parity_applies_when": kits["parity_applies_when"],
                "tier_compression_pct": kits["tier_compression_pct"],
                "tier_template_3label": kits["tier_template_3label"],
                "tier_template_5label": kits["tier_template_5label"],
            },
            "note": kits["note"],
        },
    ]


def build_account_settings_row():
    floor_fm = parse_frontmatter(ITEMS_DIR / f"{bcc.FLOOR_SOURCE_PN}.md",
                                 (), ITEM_NUMERIC_FIELDS)
    return {
        "account_id": ACCOUNT_ID,
        "floor_value": floor_fm["first_article_price"],
        "floor_source_pn": bcc.FLOOR_SOURCE_PN,
        "floor_label": bcc.FLOOR_LABEL,
        "ink_rate_per_sq_ft": bcc.INK_RATES["full_bleed_flood_coat"]["cost_per_sq_ft"],
        "laminate_rate_per_sq_ft": 0.2389,
        "invoice_protection_enabled": True,
        "routing_thresholds": bcc.ROUTING,
        "extra": {
            "version": bcc.VERSION,
            "moq": {"printed_laminated": bcc.MOQ_PRINTED_LAMINATED},
            "ink_rates": bcc.INK_RATES,
            "quote_language": bcc.QUOTE_LANGUAGE,
            "flag_thresholds": bcc.FLAG_THRESHOLDS,
            "override_type_precedent": bcc.OVERRIDE_TYPE_PRECEDENT,
        },
    }


def build_combinations(material_rows, item_rows):
    """Default combinations from documented item->material relationships."""
    mats = {m["material_key"]: m for m in material_rows}
    combos = []

    combos.append({
        "name": "Orajet 3951 + 1-mil Poly Lam — Printed/Laminated",
        "process_type": "printed_laminated",
        "description": ("Account-standard printed/laminated stack: Orajet 3951 "
                        "white cast vinyl + Flexcon 1-mil polyester overlaminate "
                        "+ full-bleed eco-solvent ink ($0.50/sq ft per §25)."),
        "components": [
            ("orajet-3951-white", "substrate", 1.0),
            ("1mil-polyester-overlaminate", "laminate", 1.0),
            ("eco-solvent-ink-full-bleed", "ink", 1.0),
        ],
    })

    cv_combo_for_material = {}
    for mk, m in mats.items():
        if m["material_family"] != "cut_vinyl":
            continue
        tapes = (m["compatible_with"] or {}).get("compatible_tapes", ["transferrite-582u"])
        # 15" large-format roll pairs with the 30" tape (2-up nesting per
        # PRODUCTION.md); every 24"/48" roll pairs with the 24" tape.
        tape = ("transferrite-582u-30in"
                if mk == "3m-180mc-cardinal-red-15in" and "transferrite-582u-30in" in tapes
                else "transferrite-582u")
        label = f"{m['product_name']} {m['color_name']} {int(m['roll_width_in'])}\""
        if m["roll_length_yd"]:
            label += f" × {int(m['roll_length_yd'])}yd"
        name = f"{label} + 582U {int(mats[tape]['roll_width_in'])}\" — Cut Vinyl"
        combos.append({
            "name": name,
            "process_type": "cut_vinyl",
            "description": (f"Cut/Weed/Mask: {label} with TransferRite 582U "
                            f"{int(mats[tape]['roll_width_in'])}\" application tape."),
            "components": [(mk, "substrate", 1.0), (tape, "tape", 1.0)],
        })
        cv_combo_for_material[mk] = name

    # item -> combination link
    item_combo = {}
    for it in item_rows:
        pn = it["part_number"]
        if it["material_family"].startswith("Orajet"):
            item_combo[pn] = combos[0]["name"]
            continue
        if it["material_family"] == "3M 180mC Cut Vinyl":
            pref = ITEM_COMBO_PREFERENCE.get(pn)
            if pref and pref in cv_combo_for_material:
                item_combo[pn] = cv_combo_for_material[pref]
                continue
            for mk, m in mats.items():
                if m["material_family"] == "cut_vinyl" and pn in (m["used_in_items"] or []):
                    item_combo[pn] = cv_combo_for_material[mk]
                    break
    return combos, item_combo


# ---------------------------------------------------------------------------
# SQL emission (idempotent; used by --emit-sql and by MCP-driven runs)
# ---------------------------------------------------------------------------

def sql_lit(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, (dict, list)):
        return "'" + json.dumps(v).replace("'", "''") + "'::jsonb"
    return "'" + str(v).replace("'", "''") + "'"


def multirow_upsert(table, rows, conflict_key):
    cols = list(rows[0].keys())
    tuples = ",\n".join("(" + ", ".join(sql_lit(r[c]) for c in cols) + ")" for r in rows)
    sets = ", ".join(f"{c} = excluded.{c}" for c in cols if c != conflict_key)
    return (f"insert into {table} ({', '.join(cols)}) values\n{tuples}\n"
            f"on conflict ({conflict_key}) do update set {sets};")


def emit_sql(material_rows, item_rows, internal_rows, band_rows, settings_row,
             combos, item_combo):
    out = ["begin;"]
    out.append(multirow_upsert("elliott_materials", material_rows, "material_key"))
    out.append(multirow_upsert("elliott_items", item_rows, "part_number"))
    # Internal strategy fields -> service-role-only table (D4). RLS on
    # elliott_items_internal has NO anon policies; only service_role reads.
    out.append(multirow_upsert("elliott_items_internal", internal_rows, "part_number"))
    out.append(multirow_upsert(
        "elliott_pricing_bands",
        [dict(b, account_id=ACCOUNT_ID, is_active=True) for b in band_rows],
        "band_key"))
    out.append(multirow_upsert("elliott_account_settings", [settings_row], "account_id"))
    for c in combos:
        out.append(
            "insert into elliott_material_combinations (account_id, name, process_type, description, is_active) "
            f"values ({sql_lit(ACCOUNT_ID)}, {sql_lit(c['name'])}, {sql_lit(c['process_type'])}, "
            f"{sql_lit(c['description'])}, true) "
            "on conflict (account_id, name) do update set process_type = excluded.process_type, "
            "description = excluded.description, is_active = excluded.is_active;")
        out.append(
            "delete from elliott_material_combination_components where combination_id = "
            f"(select id from elliott_material_combinations where account_id = {sql_lit(ACCOUNT_ID)} "
            f"and name = {sql_lit(c['name'])});")
        for (mk, role, mult) in c["components"]:
            out.append(
                "insert into elliott_material_combination_components "
                "(combination_id, material_id, component_role, usage_sq_ft_multiplier) values ("
                f"(select id from elliott_material_combinations where account_id = {sql_lit(ACCOUNT_ID)} and name = {sql_lit(c['name'])}), "
                f"(select id from elliott_materials where material_key = {sql_lit(mk)}), "
                f"{sql_lit(role)}, {sql_lit(mult)});")
    for pn, combo_name in item_combo.items():
        out.append(
            f"update elliott_items set material_combination_id = "
            f"(select id from elliott_material_combinations where account_id = {sql_lit(ACCOUNT_ID)} "
            f"and name = {sql_lit(combo_name)}) where part_number = {sql_lit(pn)};")
    out.append("commit;")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Live run via supabase-py
# ---------------------------------------------------------------------------

def run_live(material_rows, item_rows, internal_rows, band_rows, settings_row,
             combos, item_combo):
    import os
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not (url and key):
        env_file = REPO_ROOT / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if "=" in line and not line.strip().startswith("#"):
                    k, v = line.split("=", 1)
                    if k.strip() == "SUPABASE_URL":
                        url = url or v.strip()
                    if k.strip() == "SUPABASE_SERVICE_ROLE_KEY":
                        key = key or v.strip()
    if not (url and key):
        print("ERROR: SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY not set "
              "(env or .env). Use --emit-sql to generate SQL instead.")
        sys.exit(1)
    from supabase import create_client
    sb = create_client(url, key)

    sb.table("elliott_materials").upsert(material_rows, on_conflict="material_key").execute()
    sb.table("elliott_items").upsert(
        [dict(r) for r in item_rows], on_conflict="part_number").execute()
    sb.table("elliott_items_internal").upsert(
        [dict(r) for r in internal_rows], on_conflict="part_number").execute()
    sb.table("elliott_pricing_bands").upsert(
        [dict(b, account_id=ACCOUNT_ID, is_active=True) for b in band_rows],
        on_conflict="band_key").execute()
    sb.table("elliott_account_settings").upsert(
        settings_row, on_conflict="account_id").execute()
    for c in combos:
        sb.table("elliott_material_combinations").upsert(
            {"account_id": ACCOUNT_ID, "name": c["name"],
             "process_type": c["process_type"], "description": c["description"],
             "is_active": True},
            on_conflict="account_id,name").execute()
        combo_id = (sb.table("elliott_material_combinations").select("id")
                    .eq("account_id", ACCOUNT_ID).eq("name", c["name"])
                    .single().execute().data["id"])
        sb.table("elliott_material_combination_components").delete().eq(
            "combination_id", combo_id).execute()
        for (mk, role, mult) in c["components"]:
            mat_id = (sb.table("elliott_materials").select("id")
                      .eq("material_key", mk).single().execute().data["id"])
            sb.table("elliott_material_combination_components").insert(
                {"combination_id": combo_id, "material_id": mat_id,
                 "component_role": role, "usage_sq_ft_multiplier": mult}).execute()
    for pn, combo_name in item_combo.items():
        combo_id = (sb.table("elliott_material_combinations").select("id")
                    .eq("account_id", ACCOUNT_ID).eq("name", combo_name)
                    .single().execute().data["id"])
        sb.table("elliott_items").update(
            {"material_combination_id": combo_id}).eq("part_number", pn).execute()


# ---------------------------------------------------------------------------
# Report + main
# ---------------------------------------------------------------------------

def print_report(material_rows, item_rows, band_rows, combos, item_combo,
                 skipped_materials, skipped_items, mode, out=sys.stdout):
    def p(line=""):
        print(line, file=out)
    p("=" * 64)
    p(f"Elliott -> Supabase migration report ({mode}, {date.today().isoformat()})")
    p("=" * 64)
    n_synth = sum(1 for m in material_rows if m["material_key"] == INK_MATERIAL["material_id"])
    p(f"elliott_materials:        {len(material_rows)} rows "
      f"({len(material_rows) - n_synth} from materials/*.md + {n_synth} synthetic ink rate)")
    p(f"elliott_items:            {len(item_rows)} rows")
    by_band = {}
    for it in item_rows:
        by_band[it["band_class"]] = by_band.get(it["band_class"], 0) + 1
    for k in sorted(by_band):
        p(f"    band_class {k:<20} {by_band[k]}")
    p(f"    do_not_benchmark      {sum(1 for i in item_rows if i['do_not_benchmark'])}")
    p(f"elliott_pricing_bands:    {len(band_rows)} rows "
      f"({', '.join(b['band_key'] for b in band_rows)})")
    p("elliott_account_settings: 1 row (account_id=elliott)")
    p(f"elliott_material_combinations: {len(combos)} rows")
    p(f"    item->combination links: {len(item_combo)} of {len(item_rows)} items")
    unlinked = [i["part_number"] for i in item_rows if i["part_number"] not in item_combo]
    if unlinked:
        p(f"    UNLINKED items: {', '.join(unlinked)}")
    for name, reason in skipped_materials + skipped_items:
        p(f"  SKIPPED {name}: {reason}")
    if not (skipped_materials or skipped_items):
        p("  Skipped rows: none")


def main():
    mode = "live"
    if "--emit-sql" in sys.argv:
        mode = "emit-sql"
    elif "--dry-run" in sys.argv:
        mode = "dry-run"

    material_rows, skipped_m = build_material_rows()
    item_rows, internal_rows, skipped_i = build_item_rows()
    band_rows = build_band_rows()
    settings_row = build_account_settings_row()
    combos, item_combo = build_combinations(material_rows, item_rows)

    if mode == "emit-sql":
        print(emit_sql(material_rows, item_rows, internal_rows, band_rows,
                       settings_row, combos, item_combo))
        print_report(material_rows, item_rows, band_rows, combos, item_combo,
                     skipped_m, skipped_i, mode, out=sys.stderr)
        return
    if mode == "live":
        run_live(material_rows, item_rows, internal_rows, band_rows,
                 settings_row, combos, item_combo)
    print_report(material_rows, item_rows, band_rows, combos, item_combo,
                 skipped_m, skipped_i, mode)


if __name__ == "__main__":
    main()
