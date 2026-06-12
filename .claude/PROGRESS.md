# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> **Rolling window: 10 entries max. When adding an 11th, remove the oldest. Git retains all history.**
>
> This file is the session memory layer: why decisions were made, what changed strategically, what a future session needs to know. It is not a commit log and not a validation archive — full validation records live in `items/*.md` (Pricing Derivation), file-level changes live in git history, and structure/math compliance is enforced by `scripts/validate.py`. Entry format (template in `.claude/COMPLETION_TEMPLATES.md`): What / Key Decisions / Strategic Flags / Status, 10–25 lines per entry, no other sections.
>
> Last Updated: 2026-06-12 (Session O — new item P/N 1278980, singles band fourth data point, $9.50 at qty 20, 4-wave validated.)

---

### 2026-06-12 — Session O (new item): P/N 1278980 — singles band fourth data point, $9.50 at qty 20, 4-wave validated

**What:** New printed/laminated single label (LABEL-PLTFM RANGE CAPACITY CHART MODEL E160 V3) at 7.88" × 11.13" = 0.609 sq ft, priced $9.50 at qty 20 = $15.60/sq ft — the singles band's fourth confirmed data point and the first item at exactly 0.609 sq ft. Band $/sq ft is now monotonic across four positions (0.503 / 0.560 / 0.609 / 1.296 → $15.91 / $15.63 / $15.60 / $15.43). Full 4-wave atomic validation (24 responses): Wave 1 landed 5/6 at exactly $9.50, all anchored to 1267140; Wave 3 sent the PO as-is 6/6 with zero questions.

**Key Decisions:**
- Wave 2's single structural finding adopted: a 200+ floor below $6.50 inverts against 1267140's validated floor on a $/sq ft basis — floor set at $6.75 (strongest Wave 2 clustering), 100-199 held at $7.50 for tier separation. Wave 4 split 4 YES / 2 NO (the 2 NO argued $7.07–$7.25 on $/sq ft parity); Nick accepted $6.75 — the residual $/sq ft step vs 1267140's floor ($11.08 vs $11.61) is theoretical given Sean's 20–50 batch pattern, and $6.75 stays above the $6.50 dollar threshold he'd notice on an invoice. No override — engine consensus accepted.
- Routed as a SINGLE to the singles band despite exact kit-family label geometry: kit per-label parity does not apply to singles; $9.50 vs the $10.00/label kit rate is the documented intentional kit premium, not an inconsistency.

**Strategic Flags:**
- INTERNAL ONLY: likely the first of several singles at exactly 0.609 sq ft — every tier in this table becomes the permanent reference for future items at this size. January 2027 normalization from $9.50 requires ~$1.46–$3.90/label uplift to $18–$22/sq ft; anchor to relationship-phase transition, NOT per-label rate arguments — Sean now has four accepted/quoted data points at $15.43–$15.91/sq ft.
- Wave 3 quote email anchor line locked: "Pricing is based on the same cast vinyl/polyester overlaminate construction as your prior Pro Label orders." (Reference 1267140/1230820 if helpful.)

**Status:** Complete — validate.py 0/0; quote pending ($9.50 at qty 20); Supabase seed for 1278980 deferred to a follow-up run (scripts/migrate_to_supabase.py).

---

### 2026-06-12 — Session N (ops): Supabase seed — P/N 1267140 + 1278220 into `elliott_items` / `elliott_items_internal`

**What:** Seeded the two items added earlier today (Session L: 1267140; Session M: 1278220) into the shared `prolabel` Supabase project, clearing the carry-over flagged by both sessions. Pure seed run of the existing source-of-truth files — no repo item, governance, or pricing changes. Both tables went 23 → 25 rows; the deployed Supabase-first UI now serves both items (1267140 in singles_standard, 1278220 in singles_micro, verified row-level in the live DB).

**Key Decisions:**
- The remote session env had no Supabase service-role credentials, so the documented alternate path was used: `migrate_to_supabase.py --emit-sql` executed through the service-role-backed Supabase MCP in batches — semantically identical to live mode, and the sanctioned pattern for credential-less environments.

**Strategic Flags:**
- D4 security routing re-verified live: `pricing_logic`/`notes` blank on the anon-readable `elliott_items` rows; full strategy text (including the 1267140 INTERNAL ONLY normalization note) lives only in `elliott_items_internal`, which has no anon policies.
- The seed is idempotent — materials/bands/settings/combinations re-upserted with zero value drift; the repo remains the source of truth.

**Status:** Complete — next action is Nick sending Sean both quotes (1267140 $8.75 at qty 20, 1278220 $3.00 at qty 20).

---

### 2026-06-12 — Session M (new item): P/N 1278220 — direct parity clone of 1279000 (Micro-Format Band, $3.00 at qty 20)

**What:** Created P/N 1278220 (LBL-MAX JIB CAP 1500 TIP HZRD) as a direct parity clone of 1279000, the Micro-Format Band founding data point — identical dimensions (0.097 sq ft), material, process, tier table, and margins; only the P/N and artwork content differ. The direct parity exemption per `governance/PRICING_VALIDATION.md` applies: 1279000's full 4-wave validation is inherited, no new AI validation run (same pattern as 1068270 ← 1082570, Session F). Rule 15 band check satisfied: $3.00 at qty 20 = $30.86/sq ft, exactly the Micro-Format Band anchor.

**Key Decisions:**
- Parallel-session collision with Session L (1267140) resolved at merge: both sessions had independently claimed "Session L," category footnote ⁶, and item #24. Resolution — 1267140 keeps Session L / ⁶ / #24 (first to main); this session relabeled Session M with footnote ⁷; final item count 25. Both sessions' content verified intact; the collisions were namespace-only.
- 1278220 is NOT a band data point — founding status stays with 1279000 alone, and the band's data-point count is unchanged. The band's ~0.08–0.12 sq ft boundary caution governs dimensionally NEW items, not exact-dimension parity clones.

**Strategic Flags:**
- Permanent lockstep link: any future change to 1279000's dimensions, material cost, process, or band parameters must update 1278220 in lockstep (same convention as 1068270 ↔ 1082570).

**Status:** Complete — validate.py 0/0 on the merged tree; quote pending ($3.00 at qty 20); the deferred Supabase seed was completed in Session N.

---

### 2026-06-12 — Session L (new item): P/N 1267140 — third singles-band data point, $8.75 at qty 20, 4-wave validated

**What:** New printed/laminated single label at 15.00" × 5.38" = 0.560 sq ft, priced $8.75 at qty 20 = $15.63/sq ft — the singles band's third confirmed data point and first interior point, between 1082570/1068270 ($15.91 at 0.503 sq ft) and root benchmark 1230820 ($15.43 at 1.296 sq ft), making the band's $/sq ft monotonic by size. Full 4-wave atomic validation (24 responses): Wave 1 built to $8.75 independently (6/6); Wave 4 unanimously rejected the draft 200+ tier while keeping $8.75.

**Key Decisions:**
- Validation's primary structural finding adopted: the draft 200+ tier ($4.75 = $8.48/sq ft) sat 45% below the band floor and would have handed Sean an indefensible procurement anchor. Nick raised 200+ to $6.50 and 100-199 to $7.25 (avoiding a §26 cascade inversion), deliberately setting the 200+ margin floor above the legacy volume-reward floor as band protection. $8.75 at qty 20 unchanged; engine consensus accepted, no override.
- The drawing's description/model title-block fields are blank and were filed as blank per Nick's instruction — never invented; the P/N is the identifier.

**Strategic Flags:**
- The third data point cements the singles band ($15.43–$15.91/sq ft at qty 20) — Wave 2/3 consensus: Sean logs it as his permanent procurement baseline, complicating January 2027 normalization. INTERNAL ONLY normalization note carried in the item file.
- 1267140 is a full band data point — NOT on any do_not_benchmark list.

**Status:** Complete — validate.py 0/0; quote pending (Wave 3 anchor line locked in the item file); the deferred Supabase seed was completed in Session N.

---

### 2026-06-09 — Session K (fix+cleanup): Drop zone scoped to main panel + Session-I deferred-work verification + Supabase drift closure

**What:** Replaced Session J's always-visible fixed bottom drop strip — which overlapped the left rail and blocked clicks — with a drag-activated overlay scoped to the main content panel plus an always-visible 📎 attach button; all upload, association-priority, and paste logic unchanged, calculator engine block zero diff hunks. Separately verified that Session I's deferred work (D2-full, D3, D4, D5) was already complete in commit 4435eff — no re-edits needed — and closed the one real remnant: the empty Supabase `transferrite-582u` notes field flagged by Session J was backfilled and round-trip verified, so sync runs no longer blank the repo's D3 usage note.

**Key Decisions:**
- The overlay's translucency uses `color-mix()` over existing tokens rather than the spec's rgba approach, which would have required a new color token — prohibited by the frontend's token discipline.

**Status:** Complete — validate.py 0/0; Session J drift closed; carry-over: Nick tests the drop-zone fix in the browser.

---

### 2026-06-09 — Session J (feature): Global spec sheet drop zone + Supabase Storage

**What:** Added global drag-and-drop / paste / click-to-browse spec sheet upload across all tabs. Files land in the private Supabase Storage bucket `spec-sheets` (reads via signed URLs only), link to items through the new `elliott_items.spec_sheet_paths` column, and render in a new in-app viewer; `sync_from_supabase.py` signs stored paths into regenerated data.json. No pricing logic, routing, governance, band, or price changes — engine block zero diff hunks.

**Key Decisions:**
- Upload association priority: selected Items-tab item → Calculator P/N field → typeahead modal with an "unlinked" fallback folder. Duplicate filenames get timestamp suffixes — revision history, never overwrite.
- Security catch fixed live: `elliott_items` carried a dormant table-level anon UPDATE grant that the new RLS policy would have activated for every column, prices included — revoked and re-granted column-scoped to `spec_sheet_paths` only, role-tested both ways.

**Strategic Flags:**
- Drift flagged for Nick: the Supabase `elliott_materials.transferrite-582u` row had empty notes, so any sync run would overwrite the repo's Session-I D3 usage-method note (closed in Session K).

**Status:** Complete — validate.py 0/0; storage + RLS live and role-tested; next: Nick drops a real spec sheet in the browser.

---

### 2026-06-09 — Session I (cleanup): §25 costing normalization + tape method fix + security hardening + §27 rush floor

**What:** Resolved the remaining decision forks from the 2026-06-09 full-system audit (D2-full, D3, D4, D5, D7) — documentation and security only; zero sell prices, tiers, band anchors, or statuses changed. The legacy-overstated costing era is fully retired: the whole printed/laminated catalog (minus the documented job-based one-offs) now sits on the single §25 canonical basis, margin strings are cross-comparable, and one length-based tape convention governs all cut vinyl.

**Key Decisions:**
- Root benchmark 1230820 recosted to §25 canonical ($2.60 material, ~87% at qty 20) — ~87% is now the canonical reference margin for every wave session embedding this benchmark.
- D7 resolved: ink is always the §25 $0.50/sq ft full-bleed rate regardless of color — Sean's pending color selection on 1082570 affects production setup only, no recosting on selection; 1068270 recosted in lockstep per the parity link.
- Tape costing uses the length-based method everywhere; the 582U $0.5911/sq ft figure is a derived convenience value never to be used in per-label builds. The calculator engine still consumes it as an area rate (audit M-2) — engine harmonization deliberately deferred.
- §27 codified: $50 rush/favor floor per job, separate from and non-stacking with the $55 one-off job-economics floor ($55 governs when both apply); replaces the previously undocumented $100 figure.
- D4 security: `pricing_logic` and frontmatter `notes` stripped from data.json; all internal text moved to the new service-role-only `elliott_items_internal` table, with `migrate_to_supabase.py` routing there on every future seed so re-running can never re-expose.

**Strategic Flags:**
- D4-residual open fork for Nick: `sections.notes` prose — including 3 items' INTERNAL ONLY Jan-2027 subsections — still ships in deployed data.json behind the Vercel password; stripping it would blank the UI's Notes panel, so deliberately left undone pending a decision.

**Status:** Complete — validate.py 0/0; D2-full, D3, D4 (with documented residual), D5, D7 all resolved.

---

### 2026-06-09 — Session H (system v2): Supabase data layer + Materials Manager + calculator overhaul

**What:** Built system v2 off the same-day audit: a Supabase data layer (7 `elliott_`-prefixed tables in the shared `prolabel` project, seeded idempotently by the new `migrate_to_supabase.py`, mirrored back by the new `sync_from_supabase.py`), a Materials Manager tab with full CRUD, and a calculator overhaul that hydrates from Supabase first with static-JSON fallback. Resolved audit findings C-1, H-1–H-5, and W1–W6. No sell price changed anywhere.

**Key Decisions:**
- Supabase is primary; the four JSONs are fallback (visible banner). Category files remain the governance source of truth for band definitions; `build_calculator_config.py` constants remain the seed source.
- Tables are `elliott_`-prefixed because `prolabel` hosts unrelated apps — never touch co-tenant tables.
- RLS write split: the Materials Manager (anon key) may write materials/combinations/components only; items, bands, and settings change only through governed Claude Code sessions via the migration script. Soft deletes everywhere.
- D1 resolved as report-only enforcement: `enforceTierBoundaries()` computes but never mutates tiers — catalog tables keep their intentional cliffs, §26 resolves them at billing, and briefs are band-anchored again (eliminating C-1's 29–46%-low briefs).
- H-4: kit material costs normalized to §25 canonical (1278930 $2.99 → $3.60; 1245130 $5.16 → $5.95) — documentation-only recost; kit-family margins now cross-comparable (~88% at qty 20, ~80% floor).
- §25 full bleed is the only reachable ink mode from the calculator (H-1); the engine's `inputs._config` hook is the ONLY supported way to vary constants per run.
- Materials added via the Manager exist in the DB first — a follow-up session must backfill `materials/*.md` before any CI rebuild overwrites the fallback JSONs.

**Status:** Complete — validate.py 0/0 with 4 new structural checks active; Supabase seeded and RLS role-tested; next was Nick's browser review of v2.

---

### 2026-06-09 — Full System Audit: 1 CRITICAL, 5 HIGH, 15 MEDIUM, 11 LOW, 7 INFO

**What:** Hostile read-and-report audit of the entire system with maximum depth on the calculator; every number independently recomputed. Verdict: SAFE TO QUOTE FROM — WITH CAVEATS. The catalog (item tier tables — what Sean is invoiced against) is arithmetically immaculate and band-coherent, but calculator briefs landed 29–46% below locked catalog/band on every standard route (C-1), VALIDATION_PROMPTS.md §3's embedded band table was missing 3 bands and 5 anchors, and three §25 costing eras coexisted, making margin strings non-comparable. Full report: `audits/2026-06-09-full-system-audit.md`.

**Key Decisions:**
- Read-and-report only — zero fixes applied, not even typos; all remediation deferred to follow-up sessions gated on Nick resolving seven decision forks (D1 cascade design, D2 legacy §25 recost, D3 tape method, D4 data.json internal exposure, D5 rush-floor codification, D6 lam-pass model, D7 ink-lineage lockstep).
- Calculator tier tables, margins, and quote stubs were declared unfit as Wave-1 inputs, and 4-wave sessions off §3's band table suspended, until the forks resolved (done in Sessions H and I).

**Strategic Flags:**
- Deployed data.json shipped INTERNAL ONLY Jan-2027 normalization notes behind a single Vercel password (M-15) — became fork D4.

**Status:** Complete — findings handed to Session H (C-1, H-1–H-5, W1–W6) and Session I (D2-full, D3, D4, D5, D7), which resolved them.

---

### 2026-06-09 — Session G (new item): P/N 1278890 — 2-label E160 V3 kit, per-label parity with 1278930, 4-wave validated

**What:** New 2-label lifting-capacity-chart kit (0.609 sq ft/label) priced at $10.00/label at qty 20 ($20/kit) — exactly the $16.42/sq ft kit band anchor — completing per-label parity across the kit family (2/3/5 labels: 1278890, 1278930, 1245130). Full 4-wave atomic validation: Wave 4 unanimous YES, no modifications adopted, no override — engine consensus accepted.

**Key Decisions:**
- The 200+ tier's near-breakeven fully-loaded margin was ACCEPTED as a structural condition inherited from 1278930/1245130 — fixing it here by breaking parity would corrupt the three-way per-label triangulation, which is worth more than the tier's margin.
- The per-label parity boundary stays tied to lamination passes (≤2), not label count — beyond 2 passes or mixed dimensions, cost-build from scratch.

**Strategic Flags:**
- Sean now holds THREE accepted data points at $10.00/label — the per-label rate is permanently locked. January 2027 normalization on the kit family must anchor to material cost, process complexity, or relationship-phase language, NOT per-label rate; the $6.00/label floor at 200+ is the hardest number to move. INTERNAL ONLY; never surfaced to Sean.
- Track actual cycle time on the first 200+ run — cumulative kit-family cycle-time data is the documented operational anchor for the 2027 normalization discussion.
- LABEL-B's ECO# 28830 revision (06/08/26) is artwork-only; the first production run doubles as the de facto QA check on it.

**Status:** Complete — validate.py 0/0; quote pending with Sean ($20/kit at qty 20).

---

*Entries older than Session G (2026-06-09) were removed per the 10-entry rolling window — git history retains them in full.*
