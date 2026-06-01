# Elliott Equipment — Architecture Registry

> **Living document — updated every session that changes structure.**
>
> Last Updated: 2026-06-01

---

## Item Catalog

All quoted items. Updated when items are added, repriced, or status changes.

| P/N | Description | Material Family | Item Type | Label Count | Sq Ft/Label | Price (qty 20) | Per Label (qty 20) | Margin (qty 20) | Status | Item File |
|-----|-------------|-----------------|-----------|-------------|-------------|-----------------|---------------------|------------------|--------|-----------| 
| 1230820 | Load Chart Label, Model D105 | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Label | 1 | 1.296 | $20 | $20.00 | ~84% | FA Accepted | `items/1230820.md` |
| 1278930 | 3-Label Lifting Capacity Chart Kit, E190 | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Kit | 3 | 0.609 | $30 | $10.00 | ~90% | FA Accepted | `items/1278930.md` |
| 1245130 | 5-Label Lifting Capacity Chart Kit, E160 | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Kit | 5 | 0.609 | $50 | $10.00 | ~90% | Quoted | `items/1245130.md` |
| 1205720 | E190 Cardinal Red Model Designation | 3M 180mC Cut Vinyl | Vinyl Cut Lettering | 1 | 2.56 | $35 | $35.00 | ~75% | FA Accepted | `items/1205720.md` |
| 3017435 | ELLIOTT White Vinyl Cut Lettering | 3M 180mC Cut Vinyl | Vinyl Cut Lettering | 1 | 2.56 | $35 | $35.00 | ~73% (24" roll) / ~78% (48" roll) | Quoted | `items/3017435.md` |
| 3018378 | Label D115 Blue — Model Designation | 3M 180mC Cut Vinyl | Vinyl Cut Lettering | 1 | 2.512 | $35 | $35.00 | ~75% | Quoted | `items/3018378.md` |
| 1186310 | E160 Cardinal Red Model Designation | 3M 180mC Cut Vinyl | Vinyl Cut Lettering | 1 | 2.564 | $35 | $35.00 | ~75% | Quoted | `items/1186310.md` |
| 1277970 | Outrigger Switch — Horizontal Front (18T) ⚠ one-off, do NOT benchmark | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Label | 1 | 0.008 | $2.75 (flat — one-off) | $2.75 | N/A (one-off, $55 program) | Quoted | `items/1277970.md` |
| 1277980 | Outrigger Switch — Vertical Front (18T) ⚠ one-off, do NOT benchmark | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Label | 1 | 0.008 | $2.75 (flat — one-off) | $2.75 | N/A (one-off, $55 program) | Quoted | `items/1277980.md` |
| 1277990 | Outrigger Switch — Horizontal Rear (18T) ⚠ one-off, do NOT benchmark | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Label | 1 | 0.008 | $2.75 (flat — one-off) | $2.75 | N/A (one-off, $55 program) | Quoted | `items/1277990.md` |
| 1278000 | Outrigger Switch — Vertical Rear (18T) ⚠ one-off, do NOT benchmark | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Label | 1 | 0.008 | $2.75 (flat — one-off) | $2.75 | N/A (one-off, $55 program) | Quoted | `items/1278000.md` |
| 3017583 | LBL - PTO Engage Process (ANSI Z535) ⚠ one-off, do NOT benchmark | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Label | 1 | 0.026 | $9.17 (flat — one-off) | $9.17 | ~97% (structural — one-off, $55 program at qty 6) | Quoted | `items/3017583.md` |
| 3017584 | LBL - PTO Active (smallest item on account) ⚠ one-off, do NOT benchmark | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Label | 1 | 0.00174 | $9.17 (flat — one-off) | $9.17 | ~99% (structural — one-off, $55 program at qty 6) | Quoted | `items/3017584.md` |
| 1082570 | Load Chart, I70 EZR Mount 3.6K ⚠ color conflict open (samples delivered, awaiting selection) | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Label | 1 | 0.503 | $8 (prod. rate at qty 20) | $8.00 | ~83% (at prod. vol.; current order $42 flat, job economics) | Quoted | `items/1082570.md` |
| 1210810 | LBL - DANGER FALLING JIB (ANSI Z535) ⚠ ink unverified ($0.25 placeholder, confirm after first run); do NOT benchmark until production-volume acceptance | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Label | 1 | 0.292 | $4.50 | $4.50 | ~80–85% (ink unverified; $0.25→85%, $0.40→82%, $0.50→80%) | Quoted — 1-9: $55 flat MOQ floor / 10-19: $4.75 / initial order $47.50 | `items/1210810.md` |

---

## Category Registry

| Category | Material Family | Category File | Item Count | Profile Status |
|----------|-----------------|---------------|------------|----------------|
| Cut Vinyl Lettering | 3M 180mC Cut Vinyl | `categories/cut-vinyl-3m-180mc.md` | 4 | Narrowing — 4 data points at 2.51–2.564 sq ft, all at $35/qty 20 |
| Printed + Laminated | Orajet 3951 Cast + Polyester Lam | `categories/printed-laminated-orajet.md` | 11 | **MOQ 10 now in effect for all new printed/laminated items (established 2026-06-01). $55 minimum order charge on sub-10 orders. Invoice protection applies.** Singles (≥0.5 sq ft): Narrowing — 2 confirmed band data points (1230820 at 1.296 sq ft FA Accepted; 1082570 at 0.503 sq ft quoted, $15.91/sq ft — band-consistent, AI validated). Sub-scope single (0.1–0.5 sq ft): 1210810 at 0.292 sq ft, $4.50 ($15.41/sq ft — band-consistent, AI validated, 4-round 6-model; 1-9 tier revised to $55 flat MOQ floor, 10-19 revised to $4.75); excluded from band DATA POINTS on dimensional scope until production-volume acceptance. Kits: Moderate (2 data points). Tiny labels (≤0.1 sq ft): 4 one-off outrigger program peers ($55 program total / $2.75 per label) + 2 standalone one-offs (3017583 at 0.026 sq ft and 3017584 at 0.00174 sq ft — smallest item on the account; both $55 program total / $9.17 per label at qty 6) — explicitly excluded from any band; do NOT benchmark |
| Panel Decals | Convex High Bond + Poly Lam | Not yet created | 0 | No profile — first item establishes it |
| Polycarbonate | Lexan/Polycarbonate | Not yet created | 0 | No profile — first item establishes it |

---

## Precedent Chain (Historical Record)

How prices were originally established. New items validate against Category Pricing Profiles, not this chain. The chain is for understanding price origins and defending the structure.

```
P/N 1230820 (ROOT BENCHMARK — $20/ea at qty 20)
├── P/N 1278930 (1.5x → $30/kit at qty 20)
│   └── P/N 1245130 (5/3 parity → $50/kit at qty 20)
├── P/N 1082570 (singles band → $8/label at qty 20, $15.91/sq ft — within band)
│       0.503 sq ft — low end of singles scope. Proportional sq ft scaling from 1230820.
│       Current order qty 2 (SO 20125600): $42 flat (job economics, setup recovery).
│       4-round, 6-model AI validation complete (24 runs): $55 floor rejected, $42 adopted.
│       Tiers: $16.50/$10.50/$8.00/$6.25/$5.25/$4.25. No MOQ — Elliott strategic account.
│       Open color conflict — samples delivered (~26 hrs), awaiting Sean's PO selection.
│       Status: Quoted.
├── P/N 1210810 (sub-scope single → $4.50/label at qty 20, $15.41/sq ft — band-consistent by design)
│       0.292 sq ft — BELOW singles band scope (~0.5 sq ft floor). Band exclusion is DIMENSIONAL,
│       not pricing: validated $/sq ft ($15.41) is essentially at the band floor ($15.43).
│       4-round, 6-model AI validation complete (24 runs, 2026-06-01):
│         Option A (preliminary $3.50 at qty 20) rejected 0/6 — unanimously.
│         Option B ($4.50 at qty 20, band-aligned) adopted with 10-19 adjusted $5.50→$5.00.
│         Fundamental correction: below-scope dimensional position does NOT justify below-band $/sq ft.
│       TIER RESTRUCTURE (2026-06-01): never-pay-more cliff eliminated at 1-9/10-19 boundary.
│         1-9: $55.00 flat minimum order charge (NOT per-unit) — never-pay-more compliance + MOQ 10.
│         10-19: $4.75 (revised from $5.00) — never-pay-more compliant: 19×$4.75=$90.25≈20×$4.50=$90.00 ✓
│         20-49 and below: unchanged.
│       Tiers: $55 flat/$4.75/$4.50/$3.50/$2.75/$2.50. Initial order qty 10: $47.50 (10-19 tier).
│       Ink ($0.25) UNVERIFIED — Safety Red flood coat; confirm after first run ($0.40–$0.50 realistic).
│       Do NOT benchmark until production-volume acceptance confirmed by Nick.
│       MOQ 10 — printed/laminated account rule (2026-06-01). $55 min order charge on sub-10 orders.
│       2028 MOQ plan: this session begins formalization; full account MOQ structure Jan 1, 2028.
│       Status: Quoted.
└── [future printed/laminated singles validate against Pricing Profile band]

P/N 1277970 (ONE-OFF PROGRAM — $55 program total / $2.75 per label — DO NOT BENCHMARK)
├── P/N 1277980 (program peer — identical specs, same one-off program)
├── P/N 1277990 (program peer — identical specs, same one-off program)
└── P/N 1278000 (program peer — identical specs, same one-off program)
    Note: $55 = lowest account FA price (1230820 FA) used as program-level
    minimum-worthwhile-charge floor, NOT as a per-label comparable.
    NEVER use any of these four items as a benchmark for any future Elliott item.

P/N 3017583 (STANDALONE ONE-OFF — $55 program total / $9.17 per label at qty 6 — DO NOT BENCHMARK)
    LBL - PTO Engage Process, 2.5" × 1.5" ANSI Z535 NOTICE, qty 6 for a unit in the field.
    Same $55 account minimum-worthwhile-charge floor anchor. Per-label rate is the
    arithmetic byproduct of $55 ÷ 6 and scales inversely with quantity — not a property
    of the label. Sq ft band inapplicable at 0.026 sq ft. File prep $0 (account rule).
    NEVER use as a benchmark for any future Elliott item.

P/N 3017584 (STANDALONE ONE-OFF — $55 program total / $9.17 per label at qty 6 — DO NOT BENCHMARK)
    LBL - PTO Active, 0.5" × 0.5" black-text-on-white, qty 6 for a field service request.
    Smallest item on the entire Elliott account at 0.00174 sq ft. Arrived alongside
    P/N 3017583 as part of the same next-day-rush field service request (separate line
    items, not a kit). Same $55 account minimum-worthwhile-charge floor anchor. Implied
    ~$5,270/sq ft is the most extreme arithmetic artifact on the account — meaningless
    as a reference. Sq ft band structurally inapplicable. File prep $0 (account rule).
    "Mylar overlay" drawing wording = standard 1-mil polyester laminate (Mylar is a
    polyester trade name). NEVER use as a benchmark for any future Elliott item.

P/N 1205720 (CUT VINYL BASELINE — $35/ea at qty 20, Override: Relationship Concession)
├── P/N 3017435 (sq ft parity → $35/ea at qty 20)
├── P/N 3018378 (sq ft parity → $35/ea at qty 20; new color Olympic Blue)
├── P/N 1186310 (direct dimensional + material clone → $35/ea at qty 20; E160 vs E190 content only)
└── [future cut vinyl items validate against Pricing Profile band]
```

---

## Status Lifecycle

Every item moves through these stages in order:

1. **Quoted** — Quote email sent to Sean
2. **FA Ordered** — Sean has requested or ordered a first article
3. **FA Accepted** — First article approved, production pricing is live
4. **In Production** — First production order placed
5. **Active Reorder** — Item has been reordered at least once
6. **Discontinued** — Item no longer ordered, removed from active quoting

---

## Override Types

When Nick overrides the pricing engine's recommendation:

| Type | Description | Precedent-Setting? |
|------|-------------|-------------------|
| Relationship Concession | Priced below engine output to build trust | No |
| Competitive Defense | Priced to match or beat a known competitor | Yes |
| Strategic Anchor | Priced to set a precedent for future items | Yes |
| Capacity Fill | Priced to win work during a slow period | No |
| Owner Judgment | Nick's gut override — documented for pattern learning | Case-by-case |
| One-Time Exception | Non-repeatable situation (rush, favor, comp) | No |
