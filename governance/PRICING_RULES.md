# Pricing Rules

> **Non-negotiable constraints. Apply to every pricing decision on this account.**
>
> Last Updated: 2026-07-01 (§31 sub-scope root floor applies at every tier doctrine added — P/N 3024595. Previously 2026-06-29: §30 $0.25 increment rule added. Previously §29 ANSI account rule added. Previously 2026-06-22: §28 no-floor job-economics doctrine added)

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

§27 — **Rush / Favor Job Floor.** One-off rush requests or favor jobs for existing accounts that fall outside normal catalog pricing are subject to a **$50 rush/favor floor**. This applies regardless of label size, material cost, or quantity. The $50 rush floor applies to jobs that have a real catalog rate but are being expedited or handled as a favor outside the normal order cycle. Document any rush charge applied as a One-Time Exception override in the item file or order notes. Codified 2026-06-09 (Session I / audit D5 — updated from the originally undocumented $100 figure).

§28 — **Elliott Account — No Job Floor.** Every job is priced from actual job economics: material cost (§25 canonical for printed/laminated; length-based for cut vinyl) plus realistic production time. There is no minimum order charge and no job floor on this account. For sub-0.1 sq ft production catalog items, the Micro-Format Band governs. For one-off field service requests at any size, price from material footprint and production time; Nick makes the final call on whether the job is worth doing.

§29 — **All items printed on Orajet 3951 with polyester laminate on this account are ANSI by default.** The per-label floor for new production items is $2.75 at qty 20 (ANSI). The $2.50 non-ANSI floor is a historical data point only — applicable solely to 3024140 and 1012080, which were priced under the prior framework. The ANSI checkbox has been removed from the calculator; ANSI = true is hardcoded for all Orajet/lam items. Established 2026-06-29.

§30 — **All tier prices must be in $0.25 increments.** All tier table prices across all items, all material families, and all band classes must be expressed in $0.25 increments (e.g. $2.75, $3.00, $4.25). This rule is forward-looking only — items priced prior to this session are grandfathered and not subject to retroactive correction. Applies to every new item from this session forward, without exception. Established 2026-06-29.

§31 — **Sub-scope root floor applies at every tier, not just the qty-20 comparable rate.** The $15.43/sq ft root benchmark (P/N 1230820, ROOT BENCHMARK, FA Accepted) is a hard floor that governs every quantity tier on every sub-scope item (0.1–0.5 sq ft band) — not merely the qty-20 rate used for band positioning. No tier on any sub-scope item, at any quantity including 200+, may price below $15.43/sq ft. Where a sub-scope item's material-cost economics reach the floor within the standard 6-tier ladder, a flat tier structure (holding a single $/sq ft rate across the tiers at and above that point) is the correct and only $0.25-compliant (§30) outcome — stepping the price down further at volume would breach the floor and teach the buyer the floor is negotiable, which is prohibited. Established 2026-07-01 (P/N 3024595 — the largest sub-scope item on file at 0.488 sq ft, sitting at the boundary with the singles band; Wave 2 unanimous ruling, 6/6, during 4-wave AI validation). This doctrine governs all future sub-scope items approaching the ~0.5 sq ft boundary without re-litigation. See `categories/printed-laminated-orajet.md` and `items/3024595.md` for the full validation record. This rule is forward-looking only — items priced prior to 2026-07-01 are grandfathered and not subject to retroactive correction under §31. Grandfathered tiers: 1210810 (50-99, 100-199, 200+), 1247120 (200+), 1279130 (200+), 3020477 (100-199, 200+). These grandfathered tiers should be brought into §31 compliance the next time that item is independently revised for any other reason (material cost update, status change, etc.) — not proactively. 3024595 remains the only fully §31-compliant sub-scope item on file, as established.

---

## Per-Sq-Ft Kit Premium

Kit labels price at ~$16.42/sq ft vs singles at ~$15.43/sq ft. This ~6% premium is intentional — it reflects matched-set collation, multi-label inspection, and controlled-set packaging. This is NOT a pricing error. It is documented so future sessions don't flag it as an inconsistency.
