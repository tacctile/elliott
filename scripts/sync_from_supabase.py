#!/usr/bin/env python3
"""
Elliott Pricing Engine v2 — Supabase -> repo JSON sync (Session H, 2026-06-09)

The inverse of scripts/migrate_to_supabase.py. Reads the live elliott_*
tables and regenerates the frontend's OFFLINE FALLBACK artifacts so the
repo stays current with Supabase state:

    frontend/materials.json          (elliott_materials, synthetic rows excluded)
    frontend/data.json               (elliott_items frontmatter + local prose
                                      sections/images from items/*.md)
    frontend/calculator_config.json  (elliott_pricing_bands + elliott_account_
                                      settings + elliott_materials, assembled
                                      into the exact shape the engine reads)
    frontend/combinations.json       (elliott_material_combinations + components
                                      — NEW artifact; the calculator's offline
                                      fallback for the combination selector)

Used for: offline audits, validate.py compatibility, plane-mode backup.

Field-order parity: data.json / materials.json are regenerated through the
build_frontend / build_materials code paths with DB values overlaid in
place, so when repo .md files and Supabase agree the output is identical
to the build scripts' (timestamps aside). DB-only records (added via the
Materials Manager and not yet backfilled into .md files) are appended; a
follow-up Claude Code session should backfill them into materials/*.md.
NOTE: the CI auto-rebuild regenerates these JSONs from repo .md state —
if Supabase has records the repo lacks, run the backfill session before
pushing .md changes, or the fallback files will revert to repo state.

INTERNAL-FIELD SECURITY (Session I, 2026-06-09 / audit D4):
This script does not WRITE anything to Supabase — it only reads. The
internal strategy fields `pricing_logic` and `notes` are handled as
follows account-wide:
  - data.json: STRIPPED by build_frontend.STRIP_FIELDS (this script
    inherits the strip — the field-overlay loops skip STRIP_FIELDS).
  - Supabase: the anon-readable `elliott_items` columns pricing_logic /
    notes are kept blank ('' — the columns are NOT NULL). The content
    lives in `elliott_items_internal`
    (part_number, pricing_logic, notes) — RLS enabled with NO anon
    policies, so it is readable/writable by service_role only.
    `scripts/migrate_to_supabase.py` routes those two fields there and
    nulls them on the public row; the deployed app (anon key) never
    receives internal strategy text.
  - Ground truth for the prose remains items/*.md in this repo.

Auth: reads SUPABASE_URL + SUPABASE_ANON_KEY (anon is sufficient — all
elliott_* tables grant anon SELECT) or SUPABASE_SERVICE_ROLE_KEY from the
environment / .env, or --url/--key args. --from-file <dump.json> skips the
network and regenerates from a table dump (used in sandboxes without
egress; the dump shape is {materials:[...], items:[...], bands:[...],
settings:[...], combinations:[...]}).

Usage:
    python scripts/sync_from_supabase.py
    python scripts/sync_from_supabase.py --url https://X.supabase.co --key <anon>
    python scripts/sync_from_supabase.py --from-file /tmp/dump.json
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
FRONTEND = REPO_ROOT / "frontend"

sys.path.insert(0, str(Path(__file__).parent))
import build_frontend  # noqa: E402
import build_materials  # noqa: E402

now_iso = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

# Canonical frontmatter field order (STRUCTURE_RULES.md schema) for any
# DB-only item appended to data.json.
ITEM_FIELD_ORDER = [
    "part_number", "description", "model", "item_type", "material_family",
    "label_count", "width_in", "height_in", "sq_ft_per_label", "sq_ft_per_kit",
    "material_cost_per_unit", "cost_version_date", "price_1_9", "price_10_19",
    "price_20_49", "price_50_99", "price_100_199", "price_200_plus",
    "first_article_price", "per_label_at_qty_20", "margin_at_qty_20",
    "pricing_logic", "benchmark_item", "downstream_items", "process",
    "lamination_passes", "cut_runs", "status", "date_quoted",
    "override_type", "notes",
]

MATERIAL_FIELD_MAP = {
    # DB column -> materials.json frontmatter field (1:1 unless noted)
    "material_key": "material_id",
    "material_family": "material_type",
    "manufacturer": "manufacturer",
    "product_name": "product_name",
    "product_code": "product_code",
    "item_number": "item_number",
    "color_name": "color_name",
    "color_code": "color_code",
    "film_type": "film_type",
    "film_thickness_mil": "film_thickness_mil",
    "thickness_mil": "thickness_mil",
    "adhesive_type": "adhesive_type",
    "finish": "finish",
    "roll_width_in": "roll_width_in",
    "roll_length_yd": "roll_length_yd",
    "roll_length_ft": "roll_length_ft",
    "cost_per_roll": "cost_per_roll",
    "cost_per_linear_yd": "cost_per_linear_yd",
    "cost_per_linear_ft": "cost_per_linear_ft",
    "cost_per_sq_ft": "cost_per_sq_ft",
    "cost_per_msi": "cost_per_msi",
    "max_laminator_width_in": "max_laminator_width_in",
    "distributor": "distributor",
    "verified_date": "verified_date",
    "notes": "notes",
}

SYNTHETIC_MATERIAL_KEYS = {"eco-solvent-ink-full-bleed"}


def fetch_rest(url, key, table, select="*"):
    req = urllib.request.Request(
        f"{url}/rest/v1/{table}?select={select}",
        headers={"apikey": key, "Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def load_dump(args):
    if "--from-file" in args:
        path = args[args.index("--from-file") + 1]
        return json.loads(Path(path).read_text())
    import os
    url = key = None
    if "--url" in args:
        url = args[args.index("--url") + 1]
    if "--key" in args:
        key = args[args.index("--key") + 1]
    url = url or os.environ.get("SUPABASE_URL")
    key = (key or os.environ.get("SUPABASE_ANON_KEY")
           or os.environ.get("SUPABASE_SERVICE_ROLE_KEY"))
    if not (url and key):
        env_file = REPO_ROOT / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if "=" in line and not line.strip().startswith("#"):
                    k, v = line.split("=", 1)
                    k = k.strip()
                    if k == "SUPABASE_URL":
                        url = url or v.strip()
                    if k in ("SUPABASE_ANON_KEY", "SUPABASE_SERVICE_ROLE_KEY"):
                        key = key or v.strip()
    if not (url and key):
        print("ERROR: need --from-file, or SUPABASE_URL + SUPABASE_ANON_KEY "
              "(env, .env, or --url/--key).")
        sys.exit(1)
    return {
        # creds kept for Storage signed-URL generation (Session J); absent in
        # --from-file mode, where signing is skipped and repo images are used.
        "_creds": {"url": url, "key": key},
        "materials": fetch_rest(url, key, "elliott_materials"),
        "items": fetch_rest(url, key, "elliott_items"),
        "bands": fetch_rest(url, key, "elliott_pricing_bands"),
        "settings": fetch_rest(url, key, "elliott_account_settings"),
        "combinations": fetch_rest(
            url, key, "elliott_material_combinations",
            select=("id,name,process_type,description,is_active,"
                    "elliott_material_combination_components("
                    "component_role,usage_sq_ft_multiplier,"
                    "elliott_materials(material_key,engine_key,material_family,"
                    "product_name,color_name,roll_width_in,cost_per_sq_ft,"
                    "cost_per_linear_yd,verified_date))")),
    }


def norm(v):
    """DB null -> '' to match the build scripts' frontmatter conventions."""
    return "" if v is None else v


# ---------------------------------------------------------------------------
# materials.json
# ---------------------------------------------------------------------------

def sync_materials(db_materials):
    files = sorted((REPO_ROOT / "materials").glob("*.md"))
    materials = {}
    for fp in files:
        fm = build_materials.parse_frontmatter(fp)
        if fm is None:
            continue
        materials[fm.get("material_id", fp.stem)] = {"frontmatter": fm}

    db_by_key = {m["material_key"]: m for m in db_materials
                 if m.get("is_active", True) and m["material_key"] not in SYNTHETIC_MATERIAL_KEYS}

    for mkey, row in db_by_key.items():
        if mkey in materials:
            fm = materials[mkey]["frontmatter"]
            for db_col, fm_field in MATERIAL_FIELD_MAP.items():
                if fm_field in fm and row.get(db_col) is not None:
                    fm[fm_field] = row[db_col]
        else:
            fm = {}
            for db_col, fm_field in MATERIAL_FIELD_MAP.items():
                if row.get(db_col) not in (None, ""):
                    fm[fm_field] = row[db_col]
            compat = row.get("compatible_with") or {}
            for k, v in compat.items():
                fm[k] = v
            fm["used_in_items"] = row.get("used_in_items") or []
            materials[mkey] = {"frontmatter": fm}

    # drop repo materials soft-deleted in the DB
    inactive = {m["material_key"] for m in db_materials if not m.get("is_active", True)}
    for mkey in inactive:
        materials.pop(mkey, None)

    out = {"generated": now_iso, "material_count": len(materials), "materials": materials}
    (FRONTEND / "materials.json").write_text(json.dumps(out, indent=2))
    return len(materials)


# ---------------------------------------------------------------------------
# data.json
# ---------------------------------------------------------------------------

SPEC_BUCKET = "spec-sheets"

IMAGE_EXT_TYPES = {"png", "jpg", "jpeg", "webp", "gif", "svg", "bmp"}


def sign_spec_sheet_urls(creds, paths):
    """Batch-sign Storage paths (24h expiry — offline-fallback freshness
    window; the live app signs its own 1h URLs). Returns {path: url} for
    every path that signed cleanly. Empty dict on any failure or in
    --from-file mode (no creds) — callers fall back to repo images."""
    if not creds or not paths:
        return {}
    try:
        req = urllib.request.Request(
            f"{creds['url']}/storage/v1/object/sign/{SPEC_BUCKET}",
            data=json.dumps({"expiresIn": 86400, "paths": paths}).encode(),
            headers={"apikey": creds["key"],
                     "Authorization": f"Bearer {creds['key']}",
                     "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as r:
            rows = json.loads(r.read())
        return {row["path"]: f"{creds['url']}/storage/v1{row['signedURL']}"
                for row in rows
                if not row.get("error") and row.get("signedURL")}
    except Exception as e:  # noqa: BLE001 — network/storage issues are non-fatal
        print(f"  WARN: spec sheet URL signing failed ({e}) — "
              "keeping repo image fallbacks")
        return {}


def spec_sheet_image_field(paths, signed):
    files = []
    for p in paths:
        url = signed.get(p)
        if not url:
            return None  # partial signing — keep the repo fallback intact
        ext = p.rsplit(".", 1)[-1].lower() if "." in p else ""
        ftype = "pdf" if ext == "pdf" else (
            "image" if ext in IMAGE_EXT_TYPES else "file")
        files.append({"type": ftype, "path": url})
    return files or None


def sync_items(db_items, creds=None):
    item_files = sorted((REPO_ROOT / "items").glob("*.md"))
    items = {}
    for fp in item_files:
        item = build_frontend.build_item(fp)
        if item:
            items[item["frontmatter"]["part_number"]] = item

    db_by_pn = {r["part_number"]: r for r in db_items if r.get("is_active", True)}

    # Session J: items with uploaded spec sheets get their `image` field
    # populated from Supabase Storage signed URLs (24h expiry) — Storage takes
    # priority over frontend/images/ repo files. Items without uploads keep
    # the repo render path untouched.
    all_spec_paths = sorted({p for row in db_by_pn.values()
                             for p in (row.get("spec_sheet_paths") or [])})
    signed = sign_spec_sheet_urls(creds, all_spec_paths)

    for pn, row in db_by_pn.items():
        if pn in items:
            fm = items[pn]["frontmatter"]
            for field in ITEM_FIELD_ORDER:
                if field in build_frontend.STRIP_FIELDS:
                    continue
                if field in fm and row.get(field) is not None:
                    fm[field] = row[field]
        else:
            fm = {}
            for field in ITEM_FIELD_ORDER:
                if field in build_frontend.STRIP_FIELDS:
                    continue
                fm[field] = norm(row.get(field))
            items[pn] = {"frontmatter": fm, "image": None, "sections": {
                k: "" for k in ("item_overview", "material_spec", "nesting",
                                "production", "pricing_derivation",
                                "margin_analysis", "notes", "production_debrief")}}
        spec_paths = row.get("spec_sheet_paths") or []
        if spec_paths:
            image = spec_sheet_image_field(spec_paths, signed)
            if image:
                items[pn]["image"] = image

    inactive = {r["part_number"] for r in db_items if not r.get("is_active", True)}
    for pn in inactive:
        items.pop(pn, None)

    out = {"generated": now_iso, "item_count": len(items), "items": items}
    (FRONTEND / "data.json").write_text(json.dumps(out, indent=2))
    return len(items)


# ---------------------------------------------------------------------------
# calculator_config.json — assemble the exact engine-facing shape from DB
# rows. This mirrors hydrateConfigFromSupabase() in frontend/index.html;
# keep the two in lockstep.
# ---------------------------------------------------------------------------

def assemble_config(bands, settings, materials):
    b = {row["band_key"]: row for row in bands if row.get("is_active", True)}
    s = settings[0]
    extra = s.get("extra") or {}
    mats = {m["engine_key"]: m for m in materials if m.get("engine_key")}

    def fnum(v):
        return float(v) if v is not None else None

    cv_a, cv_b, cv_c = b["cut_vinyl_a"], b["cut_vinyl_b"], b["cut_vinyl_c"]
    singles, micro, kits = (b["printed_lam_singles"], b["printed_lam_micro"],
                            b["printed_lam_kits"])
    a_extra = cv_a.get("extra") or {}
    s_extra = singles.get("extra") or {}
    m_extra = micro.get("extra") or {}
    k_extra = kits.get("extra") or {}

    cut_vinyl_band = {
        "concession_phase": {
            "min_per_sq_ft_qty_20": fnum(cv_a["min_psf_qty_20"]),
            "max_per_sq_ft_qty_20": fnum(cv_a["max_psf_qty_20"]),
            "anchor_pn": cv_a["anchor_pn"],
            "note": a_extra.get("concession_note", ""),
        },
        "ai_consensus": a_extra.get("ai_consensus"),
        "active_band": a_extra.get("active_band", "concession_phase"),
        "margin_floor_warn_pct": fnum(cv_a["margin_floor_warn_pct"]),
        "margin_floor_stop_pct": fnum(cv_a["margin_floor_stop_pct"]),
        "margin_target_qty_20_min_pct": a_extra.get("margin_target_qty_20_min_pct"),
        "margin_target_qty_20_max_pct": a_extra.get("margin_target_qty_20_max_pct"),
        "tier_compression_pct": a_extra.get("tier_compression_pct"),
        "default_tier_template": cv_a["tier_template"],
        "snap_granularity": cv_a["snap_granularity"],
        "calibration_note": a_extra.get("calibration_note", ""),
        "large_format": {
            "threshold_sq_ft": (cv_b.get("extra") or {}).get("threshold_sq_ft"),
            "anchor_psf_qty_20": fnum(cv_b["anchor_psf_qty_20"]),
            "anchor_pn": cv_b["anchor_pn"],
            "anchor_price_qty_20": fnum(cv_b["anchor_price_qty_20"]),
            "anchor_sq_ft": fnum(cv_b["anchor_sq_ft"]),
            "tier_template": cv_b["tier_template"],
            "note": cv_b.get("note", ""),
        },
        "sub_1_sqft": {
            "threshold_sq_ft": (cv_c.get("extra") or {}).get("threshold_sq_ft"),
            "anchor_psf_qty_20": fnum(cv_c["anchor_psf_qty_20"]),
            "anchor_pn": cv_c["anchor_pn"],
            "anchor_price_qty_20": fnum(cv_c["anchor_price_qty_20"]),
            "anchor_sq_ft": fnum(cv_c["anchor_sq_ft"]),
            "tier_template": cv_c["tier_template"],
            "note": cv_c.get("note", ""),
        },
    }

    singles_band = {
        "min_per_sq_ft_qty_20": fnum(singles["min_psf_qty_20"]),
        "max_per_sq_ft_qty_20": fnum(singles["max_psf_qty_20"]),
        "anchor_pn": singles["anchor_pn"],
        "anchor_psf": fnum(singles["anchor_psf_qty_20"]),
        "margin_floor_warn_pct": fnum(singles["margin_floor_warn_pct"]),
        "margin_floor_stop_pct": fnum(singles["margin_floor_stop_pct"]),
        "margin_target_qty_20_min_pct": s_extra.get("margin_target_qty_20_min_pct"),
        "margin_target_qty_20_max_pct": s_extra.get("margin_target_qty_20_max_pct"),
        "tier_ratios": singles["tier_ratios"],
        "snap_granularity": singles["snap_granularity"],
        "note": singles.get("note", ""),
    }

    micro_band = {
        "anchor_psf_qty_20": fnum(micro["anchor_psf_qty_20"]),
        "anchor_pn": micro["anchor_pn"],
        "anchor_price_qty_20": fnum(micro["anchor_price_qty_20"]),
        "anchor_sq_ft": fnum(micro["anchor_sq_ft"]),
        "threshold_sq_ft": m_extra.get("threshold_sq_ft"),
        "margin_floor_warn_pct": fnum(micro["margin_floor_warn_pct"]),
        "margin_floor_stop_pct": fnum(micro["margin_floor_stop_pct"]),
        "margin_target_qty_20_min_pct": m_extra.get("margin_target_qty_20_min_pct"),
        "margin_target_qty_20_max_pct": m_extra.get("margin_target_qty_20_max_pct"),
        "tier_ratios": micro["tier_ratios"],
        "tier_template": micro["tier_template"],
        "snap_granularity": micro["snap_granularity"],
        "note": micro.get("note", ""),
    }

    kits_band = {
        "per_label_qty_20": k_extra.get("per_label_qty_20"),
        "per_sq_ft_qty_20": fnum(kits["anchor_psf_qty_20"]),
        "per_sq_ft_premium_over_singles_pct": k_extra.get("per_sq_ft_premium_over_singles_pct"),
        "margin_floor_warn_pct": fnum(kits["margin_floor_warn_pct"]),
        "margin_floor_stop_pct": fnum(kits["margin_floor_stop_pct"]),
        "parity_applies_when": k_extra.get("parity_applies_when"),
        "tier_compression_pct": k_extra.get("tier_compression_pct"),
        "tier_template_3label": k_extra.get("tier_template_3label"),
        "tier_template_5label": k_extra.get("tier_template_5label"),
        "note": kits.get("note", ""),
    }

    mc_specs = {
        "orajet_3951": ["roll_width_in"],
        "polyester_lam_1mil": ["max_laminator_width_in"],
        "transferrite_582u": [],
        "transferrite_582u_30in": ["roll_width_in"],
    }
    material_constants = {}
    for ek, extras in mc_specs.items():
        m = mats.get(ek)
        if not m:
            continue
        entry = {
            "cost_per_sq_ft": fnum(m["cost_per_sq_ft"]),
            "material_id": m["material_key"],
            "verified_date": m["verified_date"],
        }
        for col in extras:
            target = "max_width_in" if col == "max_laminator_width_in" else col
            if m.get(col) is not None:
                entry[target] = fnum(m[col])
        material_constants[ek] = entry

    # available widths: all active roll widths sharing product_code+color_code
    cv_mats = [m for m in materials
               if m.get("material_family") == "cut_vinyl" and m.get("is_active", True)]
    widths_by_color = {}
    for m in cv_mats:
        k = (m.get("product_code"), m.get("color_code"))
        widths_by_color.setdefault(k, set()).add(int(float(m["roll_width_in"])))

    def available_widths(m):
        # own width + any WIDER active roll of the same product+color (an
        # efficiency alternate); narrower rolls are not alternates. Engine
        # efficiency scenarios stay gated by CUT_VINYL_ALT_LOOKUP in index.html.
        own = int(float(m["roll_width_in"]))
        fam = widths_by_color[(m.get("product_code"), m.get("color_code"))]
        return sorted(w for w in fam if w >= own)
    cut_vinyl_colors = {}
    for m in cv_mats:
        if not m.get("engine_key"):
            continue
        entry = {
            "material_id": m["material_key"],
            "cost_method": "length_based",
            "cost_per_linear_yd": fnum(m["cost_per_linear_yd"]),
            "roll_width_in": fnum(m["roll_width_in"]),
            "roll_width_ft": round(float(m["roll_width_in"]) / 12.0, 4),
            "available_widths_in": available_widths(m),
        }
        if m.get("pms_note"):
            entry["pms_note"] = m["pms_note"]
        entry["verified_date"] = m["verified_date"]
        cut_vinyl_colors[m["engine_key"]] = entry

    return {
        "generated": now_iso,
        "version": extra.get("version", "1.0"),
        "source": "supabase",
        "account": {
            "floor": fnum(s["floor_value"]),
            "floor_source_pn": s["floor_source_pn"],
            "floor_label": s.get("floor_label", ""),
            "moq": extra.get("moq", {}),
        },
        "routing": s["routing_thresholds"],
        "bands": {
            "cut_vinyl_lettering": cut_vinyl_band,
            "printed_laminated_singles": singles_band,
            "printed_laminated_micro": micro_band,
            "printed_laminated_kits": kits_band,
        },
        "material_constants": material_constants,
        "ink_rates": extra.get("ink_rates", {}),
        "cut_vinyl_colors": cut_vinyl_colors,
        "do_not_benchmark": None,  # filled by caller from items
        "override_type_precedent": extra.get("override_type_precedent", {}),
        "quote_language": extra.get("quote_language", {}),
        "flag_thresholds": extra.get("flag_thresholds", {}),
    }


def sync_config(bands, settings, materials, items):
    config = assemble_config(bands, settings, materials)
    config["do_not_benchmark"] = {
        r["part_number"]: (r.get("do_not_benchmark_reason") or "do_not_benchmark")
        for r in items if r.get("do_not_benchmark")}
    (FRONTEND / "calculator_config.json").write_text(json.dumps(config, indent=2))
    return len(config["bands"])


# ---------------------------------------------------------------------------
# combinations.json
# ---------------------------------------------------------------------------

def sync_combinations(combos):
    out_rows = []
    for c in combos:
        comps = c.get("components") or c.get("elliott_material_combination_components") or []
        flat = []
        for comp in comps:
            mat = comp.get("elliott_materials") or comp
            flat.append({
                "material_key": mat.get("material_key"),
                "engine_key": mat.get("engine_key"),
                "component_role": comp.get("component_role"),
                "usage_sq_ft_multiplier": comp.get("usage_sq_ft_multiplier"),
                "material_family": mat.get("material_family"),
                "product_name": mat.get("product_name"),
                "color_name": mat.get("color_name"),
                "roll_width_in": mat.get("roll_width_in"),
                "cost_per_sq_ft": mat.get("cost_per_sq_ft"),
                "cost_per_linear_yd": mat.get("cost_per_linear_yd"),
                "verified_date": mat.get("verified_date"),
            })
        out_rows.append({
            "id": c.get("id"),
            "name": c["name"],
            "process_type": c["process_type"],
            "description": c.get("description", ""),
            "is_active": c.get("is_active", True),
            "components": flat,
        })
    out_rows.sort(key=lambda r: (r["process_type"], r["name"]))
    out = {"generated": now_iso, "combination_count": len(out_rows),
           "combinations": out_rows}
    (FRONTEND / "combinations.json").write_text(json.dumps(out, indent=2))
    return len(out_rows)


def main():
    dump = load_dump(sys.argv[1:])
    n_mat = sync_materials(dump["materials"])
    n_items = sync_items(dump["items"], dump.get("_creds"))
    n_bands = sync_config(dump["bands"], dump["settings"], dump["materials"],
                          dump["items"])
    n_combos = sync_combinations(dump["combinations"])
    print(f"✓ Synced from Supabase — materials.json: {n_mat} materials, "
          f"data.json: {n_items} items, calculator_config.json: {n_bands} bands, "
          f"combinations.json: {n_combos} combinations")


if __name__ == "__main__":
    main()
