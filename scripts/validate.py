#!/usr/bin/env python3
"""
Elliott Equipment Pricing Engine — Validation Script

Checks:
1. Every item file has all required YAML frontmatter fields
2. Math consistency (sq ft, per-label, margin calculations)
3. Every item appears in ARCHITECTURE.md catalog
4. Every item appears in its category file
5. No orphaned items (in catalog but missing file, or vice versa)
6. Tier monotonicity — every tier ladder is non-increasing (Session H)
7. §25 canonical material-cost compliance for printed/laminated items,
   with a documented-exception list for legacy/job-based costings (Session H)
8. Material cross-reference bidirectionality (used_in_items ↔ item files;
   combination components ↔ material files when combinations.json exists)
   (Session H)
9. Band membership — every item's $/sq ft at qty 20 lands in its band
   (reads bands from frontend/calculator_config.json) or is a documented
   exception (Session H)
"""

import os
import sys
import re
import glob
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ITEMS_DIR = REPO_ROOT / "items"
ARCH_FILE = REPO_ROOT / ".claude" / "ARCHITECTURE.md"
STATE_FILE = REPO_ROOT / ".claude" / "STATE.yml"

CATEGORY_MAP = {
    "3M 180mC Cut Vinyl": "categories/cut-vinyl-3m-180mc.md",
    "Orajet 3951 Cast + Polyester Lam": "categories/printed-laminated-orajet.md",
    "Convex High Bond + Poly Lam": "categories/convex-high-bond-polycarbonate.md",
}

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
    "Production Debrief",
]

errors = []
warnings = []
info = []

TIER_FIELDS = ["price_1_9", "price_10_19", "price_20_49", "price_50_99",
               "price_100_199", "price_200_plus"]

# §25 canonical rate: Orajet $1.21 + laminate $0.2389 + full-bleed ink $0.50
S25_RATE_PER_SQFT = 1.21 + 0.2389 + 0.50
# Buffer must round UP and stay modest: filed − canonical raw in [-0.005, +0.15]
S25_BUFFER_MIN = -0.005
S25_BUFFER_MAX = 0.15

# Documented §25 exceptions (audit 2026-06-09 H-5/S1 adjudication). Listed
# items are reported informationally; any UNLISTED printed/lam item outside
# the buffer window is an ERROR — new costing-era mixing cannot land silently.
# 1230820 / 1082570 / 1068270 removed 2026-06-09 (Session I): rebuilt to the
# §25 canonical formula (D2-full + D7) — they now pass the compliance check.
S25_EXCEPTIONS = {
    "1277970": "job-based one-off costing (production-footprint method, documented)",
    "1277980": "job-based one-off costing (production-footprint method, documented)",
    "1277990": "job-based one-off costing (production-footprint method, documented)",
    "1278000": "job-based one-off costing (production-footprint method, documented)",
    "3017583": "job-based one-off costing (production-footprint method, documented)",
    "3017584": "job-based one-off costing (production-footprint method, documented)",
}

# Documented band-membership exceptions
BAND_EXCEPTIONS = {
    "1210810": "sub-scope single — intentionally ABOVE singles band (Wave 4 small-format premium); excluded from band data points",
    "1277970": "one-off job-economics floor — excluded from all bands",
    "1277980": "one-off job-economics floor — excluded from all bands",
    "1277990": "one-off job-economics floor — excluded from all bands",
    "1278000": "one-off job-economics floor — excluded from all bands",
    "3017583": "one-off job-economics floor — excluded from all bands",
    "3017584": "one-off job-economics floor — excluded from all bands",
    "3024592": "per-label floor governs — first sub-0.06 sq ft production item; linear Micro band formula ($30.86/sq ft × 0.054 = $1.67) overridden by per-label floor at $2.75/qty 20; $/sq ft ($50.93) is an arithmetic artifact, not the pricing basis; 4-wave validated 2026-06-16",
    "1247120": "sub-scope single (0.122 sq ft) — intentionally ABOVE singles band per sub-scope premium doctrine; $22.54/sq ft at qty 20 is above governing comparable 1210810 ($16.27/sq ft); 4-wave validated 2026-06-16; excluded from singles band data points until production-volume acceptance",
    "3024140": "per-label floor governs AND is complexity-dependent — at 0.019 sq ft the linear Micro band formula ($30.86/sq ft × 0.019 = $0.59) is inapplicable; non-ANSI simple control label floors at $2.50/qty 20 (below 3024592 ANSI DANGER floor of $2.75); $/sq ft ($131.58) is a mathematical artifact, not the pricing basis; 4-wave validated 2026-06-16; smallest item on account",
    "1279130": "sub-scope single (0.148 sq ft) — $20.95/sq ft at qty 20 intentionally above singles band ($15.43–$15.91/sq ft) per sub-scope premium doctrine; 4-wave validated 2026-06-22; excluded from singles band data points until production-volume acceptance. NOTE: 100–199 tier at $2.30 ($15.54/sq ft) clears singles band floor by $0.11/sq ft — intentional, tight but clean per Wave 2/4 validation.",
    "1012080": "Micro-Format Band item at 0.077 sq ft — parity-governed at $2.50/qty 20 ($32.47/sq ft), intentionally above the $30.86/sq ft linear formula output; qty-20 price set by parity with P/N 3024140 (non-ANSI control label family). Floor governs below ~0.06 sq ft only; at 0.077 sq ft the formula produces $2.38 but parity with the existing non-ANSI control label family is the governing logic. 4-wave validated 2026-06-22.",
    "1279260": "per-label floor governs at $2.75/qty 20 (ANSI, §29) — at 0.033 sq ft the linear Micro-Format Band formula ($30.86/sq ft × 0.033 = $1.02) is inapplicable; implied $/sq ft ($83.33) is an arithmetic artifact of per-label floor governance, not the pricing basis; tier table parity with 3024592; pricing locked per session prompt 2026-06-29",
    "1279270": "per-label floor governs at $2.75/qty 20 (ANSI, §29) — at 0.033 sq ft the linear Micro-Format Band formula ($30.86/sq ft × 0.033 = $1.02) is inapplicable; implied $/sq ft ($83.33) is an arithmetic artifact of per-label floor governance, not the pricing basis; tier table parity with 3024592; pricing locked per session prompt 2026-06-29",
    "3020477": "sub-scope single (0.130 sq ft) — fourth sub-scope data point; $21.15/sq ft at qty 20 intentionally above singles band ($15.43–$15.91/sq ft) per sub-scope premium doctrine, sitting between 1279130 ($20.95/sq ft) and 1247120 ($22.54/sq ft); independently 4-wave validated 2026-06-30 — NOT a parity exemption (tier ladder matches 1247120 by deliberate decision, not inheritance); excluded from singles band data points until production-volume acceptance",
    "3024595": "sub-scope single (0.488 sq ft) — largest sub-scope data point on file, sitting at the boundary with the singles band; $15.88/sq ft at qty 20 intentionally above the $15.43/sq ft root floor (1230820) per sub-scope premium doctrine, interpolating between 1210810 (0.292 sq ft, $16.27/sq ft) and the 0.503 sq ft singles-band neighbor (1068270/1073950, $15.91/sq ft); 4-wave validated 2026-07-01; flat tier structure (20-49 through 200+ all $7.75) establishes the floor-applies-at-every-tier doctrine (governance/PRICING_RULES.md §31); excluded from singles band data points until production-volume acceptance",
    "3017572": "sub-scope single (0.365 sq ft) — $16.44/sq ft at qty 20 intentionally above the $15.43/sq ft root floor (1230820) per sub-scope premium doctrine, priced above governing comparable 3024595 (0.488 sq ft, $15.88/sq ft) reflecting the smaller area; 4-wave validated 2026-07-10 for the 1-9 through 50-99 tiers (all §31-compliant); 100-199 ($5.50, $15.07/sq ft) and 200+ ($5.25, $14.38/sq ft) are a Nick-directed One-Time Exception override BELOW the §31 floor, non-precedent-setting per Core Rule 13 — see items/3017572.md Pricing Derivation Step 7; excluded from singles band data points until production-volume acceptance",
    "1101250": "sub-scope single (0.132 sq ft) — seventh sub-scope data point; $17.05/sq ft at qty 20 intentionally above the $15.43/sq ft root floor (1230820) per sub-scope premium doctrine (+10.5%); independently 4-wave validated 2026-07-14 — governing benchmark 1230820 only, P/N 1210810 explicitly excluded as a benchmark (do_not_benchmark list); 50-99 ($1.75, $13.26/sq ft), 100-199 ($1.50, $11.36/sq ft), and 200+ ($1.25, $9.47/sq ft) are a Nick-directed One-Time Exception override BELOW the §31 floor, non-precedent-setting per Core Rule 13 — see items/1101250.md Pricing Derivation Step 5; excluded from singles band data points until production-volume acceptance",
    "1001220": "sub-scope single (0.231 sq ft) — eighth sub-scope data point; $17.32/sq ft at qty 20 intentionally above the $15.43/sq ft root floor (1230820) per sub-scope premium doctrine (+12.3%); 4-wave validated 2026-07-14, sits between 1279130 (0.148 sq ft) and 1210810 (0.292 sq ft) on the gradient; Wave 4's step-down recommendation on 50-99/100-199/200+ priced below the §31 floor and was corrected post-synthesis (§31 postdated this item's wave prompts) to a flat $3.75/ea ($16.23/sq ft) — first sub-scope item to reach a fully §31-compliant flat structure directly, without a One-Time Exception override; see items/1001220.md Pricing Derivation Step 5; excluded from singles band data points until production-volume acceptance",
    "1205870": "per-label floor governs at $2.50/qty 20 (non-ANSI, classification-governed) — at 0.049 sq ft the linear Micro-Format Band formula ($30.86/sq ft × 0.049 = $1.51) is inapplicable; content classified non-ANSI/instructional (LEVEL SENSOR QUICK START GUIDE) from direct spec-sheet artwork review, matching 3024140's category; implied $/sq ft ($51.02) is an arithmetic artifact of per-label floor governance, not the pricing basis; tier table matches 3024140 exactly; price locked per session prompt 2026-07-15, no AI validation run — second sub-0.06 sq ft non-ANSI floor data point on file",
    "3018808": "sub-scope single (0.222 sq ft) — ninth sub-scope data point; $18.02/sq ft at qty 20 intentionally above the $15.43/sq ft root floor (1230820) per sub-scope premium doctrine (+16.8%); price pre-locked via a full 4-wave, 6-model AI validation process (24 independent model passes) run externally in ChatHub and synthesized in Claude Chat 2026-07-15; nearest neighbor to 1001220 (0.231 sq ft, 0.961 size ratio) on the sub-scope gradient — Wave 4 decision-fork consensus locked full parity with 1001220 (byte-identical ladder: $7.00/$5.50/$4.00/$3.75/$3.75/$3.75) over an independent size-based floor-hold at $3.50, to avoid a smaller-cheaper-than-larger inversion against 1001220; all six tiers clear the §31 floor natively, no post-synthesis correction needed — see items/3018808.md Pricing Derivation Step 5; excluded from singles band data points until production-volume acceptance",
    "3010722": "cut vinyl Band A (1.167 sq ft) — new lower edge of Band A; $14.36/sq ft at qty 20 intentionally above the $13.65-$13.94/sq ft concession corridor as a deliberate small-format premium established by full 4-wave, 24-model AI validation (Waves 1-4, 6 models/wave), NOT a benchmark scale-off; below the $14.84-$16.41/sq ft AI-consensus normalized band; price locked by Nick 2026-07-15; color-parity set with 3010723/3010724, identical pricing; material cost ($3.70/label) not independently verified — see items/3010722.md",
    "3010723": "cut vinyl Band A (1.167 sq ft) — color parity with 3010722 (Cardinal Red); identical $14.36/sq ft small-format premium rationale; see BAND_EXCEPTIONS['3010722'] and items/3010723.md",
    "3010724": "cut vinyl Band A (1.167 sq ft) — color parity with 3010722 (Cardinal Red); identical $14.36/sq ft small-format premium rationale; see BAND_EXCEPTIONS['3010722'] and items/3010724.md",
    "3010736": "cut vinyl Band A (1.012 sq ft) — closest-to-Band-C-boundary Band A item on the account (1.2% above the 1.0 sq ft threshold); $14.33/sq ft at qty 20 intentionally above the $13.65-$13.94/sq ft concession corridor as a deliberate small-format premium established by full 4-wave, 24-model AI validation (Waves 1-4, 6 models/wave), NOT a benchmark scale-off; Wave 2 explicitly corrected a 'premium stacked on a premium' risk against 3010722, landing just under 3010722's $14.36/sq ft; price locked by Nick 2026-07-15; material cost ($2.47/label) independently verified this session via direct calculator engine execution — see items/3010736.md",
}


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
    """Verify all required sections exist as standalone headings.

    Most sections allow a subtitle suffix (e.g. 'Spec Extraction (Reconstructed)').
    'Pricing' must be an exact heading to avoid matching 'Pricing Derivation'.
    """
    pn = filepath.stem
    # Prepend \n so the regex can match headings at the very start of the body
    padded = '\n' + content
    for section in REQUIRED_SECTIONS:
        if section == "Pricing":
            # Exact match: disallow any non-whitespace after 'Pricing' on the same line
            pattern = r'\n# Pricing[ \t]*\n'
        else:
            # Prefix match: allows subtitles like '(Reconstructed)' or '— The Full Story'
            pattern = r'\n# ' + re.escape(section)
        if not re.search(pattern, padded):
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
    valid = ["Quoted", "FA Ordered", "FA Accepted", "In Production", "Active Reorder", "Discontinued"]
    status = fm.get("status", "")
    if status not in valid:
        errors.append(f"[{pn}] Invalid status: '{status}'. Must be one of: {valid}")


def check_category_registry():
    """Verify each item appears in its expected category file."""
    item_files = list(ITEMS_DIR.glob("*.md"))
    for filepath in item_files:
        fm, _ = parse_frontmatter(filepath)
        if fm is None:
            continue
        pn = filepath.stem
        family = fm.get("material_family", "")
        if family not in CATEGORY_MAP:
            # Unknown family — no category file expected yet
            warnings.append(f"[{pn}] No category file mapped for material_family: '{family}'")
            continue
        cat_path = REPO_ROOT / CATEGORY_MAP[family]
        if not cat_path.exists():
            warnings.append(
                f"[{pn}] Category file missing for family '{family}': {CATEGORY_MAP[family]}"
            )
            continue
        cat_content = cat_path.read_text()
        if pn not in cat_content:
            errors.append(
                f"[{pn}] Item P/N not found in category file: {CATEGORY_MAP[family]}"
            )


def check_tier_monotonicity(filepath, fm):
    """Tier ladder must be non-increasing (price_1_9 >= ... >= price_200_plus)."""
    pn = filepath.stem
    prices = []
    for f in TIER_FIELDS:
        v = fm.get(f, "")
        if v in ("", None):
            continue
        try:
            prices.append((f, float(v)))
        except ValueError:
            errors.append(f"[{pn}] Non-numeric tier value {f}: '{v}'")
            return
    for (fa, a), (fb, b) in zip(prices, prices[1:]):
        if b > a + 1e-9:
            errors.append(
                f"[{pn}] Tier monotonicity violation: {fb} (${b}) > {fa} (${a})")


def check_s25_compliance(filepath, fm):
    """Printed/laminated items: filed material cost vs §25 canonical formula."""
    pn = filepath.stem
    if fm.get("material_family") != "Orajet 3951 Cast + Polyester Lam":
        return
    try:
        kit_sqft = float(fm.get("sq_ft_per_kit", 0))
        filed = float(fm.get("material_cost_per_unit", 0))
    except ValueError:
        return
    canonical = kit_sqft * S25_RATE_PER_SQFT
    diff = filed - canonical
    if S25_BUFFER_MIN <= diff <= S25_BUFFER_MAX:
        return
    if pn in S25_EXCEPTIONS:
        info.append(f"[{pn}] §25 exception (filed ${filed:.2f} vs canonical "
                    f"${canonical:.2f}): {S25_EXCEPTIONS[pn]}")
        return
    errors.append(
        f"[{pn}] §25 canonical compliance: material_cost_per_unit ${filed:.2f} "
        f"vs canonical ${canonical:.2f} (diff ${diff:+.2f} outside "
        f"[{S25_BUFFER_MIN:+.3f}, {S25_BUFFER_MAX:+.2f}]) — costing-era mixing; "
        f"rebuild under §25 or add a documented exception")


def parse_material_frontmatter(filepath):
    """Material frontmatter incl. inline lists (used_in_items etc.)."""
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
        if raw.startswith('[') and raw.endswith(']'):
            inner = raw[1:-1].strip()
            fm[key] = ([x.strip().strip('"').strip("'") for x in inner.split(',') if x.strip()]
                       if inner else [])
        else:
            fm[key] = raw.strip('"').strip("'")
    return fm


def check_material_crossrefs():
    """used_in_items <-> item files bidirectionality + combinations.json refs."""
    material_files = sorted((REPO_ROOT / "materials").glob("*.md"))
    item_pns = {f.stem for f in ITEMS_DIR.glob("*.md")}
    mats = {}
    for fp in material_files:
        fm = parse_material_frontmatter(fp)
        if fm is None:
            continue
        mats[fm.get("material_id", fp.stem)] = fm
        for pn in fm.get("used_in_items", []):
            if pn not in item_pns:
                errors.append(
                    f"[{fp.stem}] used_in_items references P/N {pn} with no item file")

    # every item must be reachable from its family's component materials
    for fp in sorted(ITEMS_DIR.glob("*.md")):
        fm, _ = parse_frontmatter(fp)
        if fm is None:
            continue
        pn = fp.stem
        fam = fm.get("material_family", "")
        if fam == "Orajet 3951 Cast + Polyester Lam":
            for mid in ("orajet-3951-white", "1mil-polyester-overlaminate"):
                if pn not in mats.get(mid, {}).get("used_in_items", []):
                    errors.append(f"[{pn}] not listed in materials/{mid}.md used_in_items")
        elif fam == "3M 180mC Cut Vinyl":
            in_vinyl = any(pn in m.get("used_in_items", []) for m in mats.values()
                           if m.get("material_type") == "cut_vinyl")
            in_tape = any(pn in m.get("used_in_items", []) for m in mats.values()
                          if m.get("material_type") == "tape")
            if not in_vinyl:
                errors.append(f"[{pn}] cut vinyl item not in any cut_vinyl material's used_in_items")
            if not in_tape:
                errors.append(f"[{pn}] cut vinyl item not in any tape material's used_in_items")

    # combinations.json (Supabase sync artifact) — components must resolve
    combos_path = REPO_ROOT / "frontend" / "combinations.json"
    if combos_path.exists():
        try:
            combos = __import__("json").loads(combos_path.read_text())
        except Exception as e:
            warnings.append(f"combinations.json unreadable: {e}")
            return
        synthetic = {"eco-solvent-ink-full-bleed"}
        for c in combos.get("combinations", []):
            roles = set()
            for comp in c.get("components", []):
                mk = comp.get("material_key")
                roles.add(comp.get("component_role"))
                if mk not in mats and mk not in synthetic:
                    errors.append(
                        f"[combination '{c.get('name')}'] component material "
                        f"'{mk}' has no materials/*.md file and is not a "
                        f"documented synthetic rate")
            if "substrate" not in roles:
                errors.append(f"[combination '{c.get('name')}'] has no substrate component")
    else:
        warnings.append("frontend/combinations.json missing — run "
                        "scripts/sync_from_supabase.py (combination cross-ref skipped)")


def check_band_membership():
    """Every item's $/sq ft at qty 20 lands in its band or is a documented exception."""
    config_path = REPO_ROOT / "frontend" / "calculator_config.json"
    if not config_path.exists():
        warnings.append("frontend/calculator_config.json missing — band membership check skipped")
        return
    import json as _json
    cfg = _json.loads(config_path.read_text())
    bands = cfg["bands"]
    cv = bands["cut_vinyl_lettering"]
    tol = 0.015  # ±1.5% covers documented rounding presentation (e.g. 1279000 30.93 vs 30.86)

    def in_range(psf, lo, hi):
        return lo * (1 - tol) <= psf <= hi * (1 + tol)

    for fp in sorted(ITEMS_DIR.glob("*.md")):
        fm, _ = parse_frontmatter(fp)
        if fm is None:
            continue
        pn = fp.stem
        if pn in BAND_EXCEPTIONS:
            info.append(f"[{pn}] band exception: {BAND_EXCEPTIONS[pn]}")
            continue
        try:
            price20 = float(fm.get("price_20_49", 0))
            sqft = float(fm.get("sq_ft_per_label", 0))
            kit_sqft = float(fm.get("sq_ft_per_kit", 0))
            label_count = int(fm.get("label_count", 1))
        except ValueError:
            continue
        fam = fm.get("material_family", "")
        if fam == "3M 180mC Cut Vinyl":
            psf = price20 / sqft if sqft else 0
            if sqft >= 5.0:
                anchor = cv["large_format"]["anchor_psf_qty_20"]
                ok, label = in_range(psf, anchor, anchor), "Band B"
            elif sqft >= 1.0:
                a = cv["concession_phase"]
                ok = in_range(psf, a["min_per_sq_ft_qty_20"], a["max_per_sq_ft_qty_20"])
                label = "Band A"
            else:
                anchor = cv["sub_1_sqft"]["anchor_psf_qty_20"]
                ok, label = in_range(psf, anchor, anchor), "Band C"
        elif fam == "Orajet 3951 Cast + Polyester Lam":
            if label_count > 1:
                per_label = price20 / label_count
                k = bands["printed_laminated_kits"]
                ok = (abs(per_label - k["per_label_qty_20"]) < 0.01
                      or in_range(price20 / kit_sqft if kit_sqft else 0,
                                  k["per_sq_ft_qty_20"], k["per_sq_ft_qty_20"]))
                label, psf = "Kit band", price20 / kit_sqft if kit_sqft else 0
            elif sqft < 0.1:
                anchor = bands["printed_laminated_micro"]["anchor_psf_qty_20"]
                psf = price20 / sqft if sqft else 0
                ok, label = in_range(psf, anchor, anchor), "Micro band"
            elif sqft <= 0.5:
                # sub-scope items must be documented exceptions (above-band premium)
                psf = price20 / sqft if sqft else 0
                errors.append(f"[{pn}] sub-scope single (${psf:.2f}/sq ft) without a "
                              f"documented band exception — add to BAND_EXCEPTIONS with rationale")
                continue
            else:
                s = bands["printed_laminated_singles"]
                psf = price20 / sqft if sqft else 0
                ok = in_range(psf, s["min_per_sq_ft_qty_20"], s["max_per_sq_ft_qty_20"])
                label = "Singles band"
        else:
            continue
        if not ok:
            errors.append(f"[{pn}] band membership: ${psf:.2f}/sq ft at qty 20 outside "
                          f"{label} — document the exception or fix the data")


def check_state_item_count():
    """Verify STATE.yml item_count matches actual item file count."""
    if not STATE_FILE.exists():
        warnings.append("STATE.yml not found — cannot check item_count")
        return
    state_text = STATE_FILE.read_text()
    match = re.search(r'^item_count:\s*(\d+)', state_text, re.MULTILINE)
    if not match:
        warnings.append("STATE.yml missing item_count field")
        return
    stated = int(match.group(1))
    actual = len(list(ITEMS_DIR.glob("*.md")))
    if stated != actual:
        warnings.append(
            f"STATE.yml item_count is {stated} but {actual} item files exist"
        )


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
        check_tier_monotonicity(filepath, fm)
        check_s25_compliance(filepath, fm)

    check_architecture_registry()
    check_category_registry()
    check_material_crossrefs()
    check_band_membership()
    check_state_item_count()

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
    if info:
        print(f"\nDOCUMENTED EXCEPTIONS ({len(info)}):")
        for i in info:
            print(f"  ℹ {i}")
    if not errors and not warnings:
        print("✓ All checks passed.")

    print(f"\n{'FAIL' if errors else 'PASS'}: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
