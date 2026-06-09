# Pricing Rules

> **Non-negotiable constraints. Apply to every pricing decision on this account.**
>
> Last Updated: 2026-06-09 (§27 rush/favor job floor added — $50 per job, separate from and non-stacking with the $55 one-off job-economics floor; audit decision fork D5)

---

## Parity Rules

1. **Per-label parity** is the default for kits with same material, same label size, same process. Price the program, not the part.
2. **Parity boundary is tied to lamination passes, not label count.** Per-label parity applies when: all labels are the same dimensions, same material system, and the kit requires ≤2 lamination passes. Beyond 2 lam passes or mixed dimensions, cost-build from scratch.
3. **The Pricing Profile is the primary validation tool.** The precedent chain is the backward-looking record. The Profile is how you price. The Chain is how you defend.

## Communication Rules

4. **Never justify kit pricing with area or material cost.** Frame as "separately finished safety labels supplied as a controlled matched set."
5. **Never expose any multiplier to the buyer.** Use process language: "second lamination pass," "matched-set inspection," "additional finishing labor."
6. **Never expose the 13.5" laminator constraint.** Frame as process, not limitation.
7. **Never volunteer cost breakdowns, material costs, or multiplier math.** Defend on value and process, not cost-plus.

## Pricing Discipline

8. **Benchmark chain must stay intact.** If P/N 1230820 is challenged, the entire kit structure is at risk. Defend on value (ANSI compliance, durability, zero-drama fulfillment).
9. **Volume tiers signal professionalism** even if Sean never orders 200+.
10. **Never price below the margin floor where the work isn't worth doing.** Relationship pricing is not charity pricing.
11. **Never let a single item's pricing undermine the structure of every other item on the account.**

## Override Rules

12. **Every override is logged** with the type, the engine's original recommendation, and Nick's final number.
13. **Overrides typed as Relationship Concession or One-Time Exception are non-precedent-setting.** Future items should NOT benchmark against an overridden price unless the override type is Strategic Anchor.
14. **When encountering an overridden item as a potential benchmark:** check the Override Type. If concession or exception, use the engine's original recommendation as the benchmark, not the overridden price. If the engine's recommendation was a range, use the midpoint as the reference benchmark.

## Profile Rules

15. **Every new item validates against the category Pricing Profile band.** Not against a single anchor item.
16. **If an item falls outside the band:** either the item has a legitimate reason (complexity, new material, process exception) or the price needs adjustment. Document the reason either way.
17. **Every quoted and accepted item feeds back into the Profile.** The band must reflect the full catalog.

## Mixed-Dimension Kit Rules

18. **Mixed-dimension kits are cost-built from bottom up.** Do not apply flat per-label parity across labels of different sizes.
19. **Do not average label sizes and pretend the kit is uniform.**
20. **Do not anchor to the same-dimension kit multiplier chain.** It doesn't apply to mixed kits.
21. **Always run AI model validation on mixed-dimension kits** — minimum Rounds 1 and 2. All 4 rounds if annual spend is significant.

## Account-Level Cost Inputs

22. **Elliott provides production-ready DWG files for every item on this account, without exception.** File prep, artwork preparation, design time, and pre-press labor are NEVER a cost factor on Elliott pricing. Past, present, and future. Step 1 of every documented process (file import/setup) is a ~5-minute mechanical operation, not a billable labor input.
23. **Do not include file prep, artwork prep, design time, or pre-press labor in any cost build, job reconstruction, or margin analysis on this account.** If you find yourself adding minutes or dollars for "file prep × N unique designs," stop — that input is zero on Elliott. Use only material + machine-time labor (print, lam, cut, weed, inspect, package).
24. **If a prior session used file prep as a cost driver, that pricing rationale was incorrect.** Document the correction in the affected item's Notes and Warnings section. Do not propagate the incorrect input forward into future quotes.

§25 — **All printed/laminated items on this account are priced assuming full bleed / full coverage ink at all times.** Rate: **$0.50/sq ft × full label sq ft**. No medium, low, or partial coverage assumptions are permitted on any Elliott printed/laminated item — past, present, or future. An incidental buffer is applied to round the calculated material total conservatively upward, accounting for setup scrap, registration pulls, and minor production waste. The buffer is judgment-applied, not a fixed number. The canonical material cost formula is: `(Orajet 3951 sq ft × $1.21) + (laminate sq ft × $0.2389) + (label sq ft × $0.50) + incidental buffer`. The frontmatter `material_cost_per_unit` field on every printed/laminated item reflects the buffered total, not the pure calculation. Established 2026-06-01. See `governance/PRODUCTION.md` Account-Wide Ink Coverage Standard and `.claude/MASTER_CONTEXT.md` Core Rules.

§26 — **Invoice protection: the buyer will never be invoiced more for ordering a smaller quantity than they would pay for a larger quantity at the next tier.** At tier boundaries where math creates a cliff, the buyer is charged whichever total is lower. This principle applies to all items on this account — printed/laminated and cut vinyl. New tier structures must verify never-pay-more compliance at all boundaries before quoting.

§27 — **Rush / Favor Job Floor.** One-off rush requests or favor jobs for existing accounts that fall outside normal catalog pricing are subject to a **$50 rush/favor floor**. This applies regardless of label size, material cost, or quantity. The $50 floor is separate from the $55 one-off job-economics floor (1230820 FA-anchored) — rush/favor jobs that would otherwise be quoted at the $55 one-off floor are not subject to an additional $50 rush charge; the $55 floor governs. The $50 rush floor applies to jobs that have a real catalog rate but are being expedited or handled as a favor outside the normal order cycle. Document any rush charge applied as a One-Time Exception override in the item file or order notes. Codified 2026-06-09 (Session I / audit D5 — updated from the originally undocumented $100 figure).

---

## Per-Sq-Ft Kit Premium

Kit labels price at ~$16.42/sq ft vs singles at ~$15.43/sq ft. This ~6% premium is intentional — it reflects matched-set collation, multi-label inspection, and controlled-set packaging. This is NOT a pricing error. It is documented so future sessions don't flag it as an inconsistency.
