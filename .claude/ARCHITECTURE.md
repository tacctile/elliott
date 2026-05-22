# Elliott Equipment — Architecture Registry

> **Living document — updated every session that changes structure.**
>
> Last Updated: 2026-05-22

---

## Item Catalog

All quoted items. Updated when items are added, repriced, or status changes.

| P/N | Description | Material Family | Item Type | Label Count | Sq Ft/Label | Price (qty 20) | Per Label (qty 20) | Margin (qty 20) | Status | Item File |
|-----|-------------|-----------------|-----------|-------------|-------------|-----------------|---------------------|------------------|--------|-----------| 
| 1230820 | Load Chart Label, D105 | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Label | 1 | 1.296 | $20 | $20.00 | ~80% | FA Accepted | `items/1230820.md` |
| 1278930 | 3-Label Lifting Capacity Chart Kit, E190 | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Kit | 3 | 0.609 | $30 | $10.00 | ~88% | FA Accepted | `items/1278930.md` |
| 1245130 | 5-Label Lifting Capacity Chart Kit, E160 | Orajet 3951 Cast + Polyester Lam | Printed/Laminated Kit | 5 | 0.609 | $50 | $10.00 | ~88% | Quoted | `items/1245130.md` |
| 1205720 | E190 Cardinal Red Model Designation | 3M 180mC Cut Vinyl | Vinyl Cut Lettering | 1 | 2.56 | $35 | $35.00 | ~80% | FA Accepted | `items/1205720.md` |
| 3017435 | ELLIOTT White Vinyl Cut Lettering | 3M 180mC Cut Vinyl | Vinyl Cut Lettering | 1 | 2.56 | $35 | $35.00 | ~76% (24" roll) / ~81% (48" roll) | Quoted | `items/3017435.md` |

---

## Category Registry

| Category | Material Family | Category File | Item Count | Profile Status |
|----------|-----------------|---------------|------------|----------------|
| Cut Vinyl Lettering | 3M 180mC Cut Vinyl | `categories/cut-vinyl-3m-180mc.md` | 2 | Moderate — 2 data points at same sq ft |
| Printed + Laminated | Orajet 3951 Cast + Polyester Lam | `categories/printed-laminated-orajet.md` | 3 | Singles: Wide (1 data point). Kits: Moderate (2 data points) |
| Panel Decals | Convex High Bond + Poly Lam | Not yet created | 0 | No profile — first item establishes it |
| Polycarbonate | Lexan/Polycarbonate | Not yet created | 0 | No profile — first item establishes it |

---

## Precedent Chain (Historical Record)

How prices were originally established. New items validate against Category Pricing Profiles, not this chain. The chain is for understanding price origins and defending the structure.

```
P/N 1230820 (ROOT BENCHMARK — $20/ea at qty 20)
├── P/N 1278930 (1.5x → $30/kit at qty 20)
│   └── P/N 1245130 (5/3 parity → $50/kit at qty 20)
└── [future printed/laminated items validate against Pricing Profile band]

P/N 1205720 (CUT VINYL BASELINE — $35/ea at qty 20, Override: Relationship Concession)
├── P/N 3017435 (sq ft parity → $35/ea at qty 20)
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
