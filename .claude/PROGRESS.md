# Elliott Equipment — Progress Log

> **Newest entries at the top. Updated every session.**
>
> **Rolling window: 10 entries max. When adding an 11th, remove the oldest. Git retains all history.**
>
> This file is the session memory layer: why decisions were made, what changed strategically, what a future session needs to know. It is not a commit log and not a validation archive — full validation records live in `items/*.md` (Pricing Derivation), file-level changes live in git history, and structure/math compliance is enforced by `scripts/validate.py`. Entry format (template in `.claude/COMPLETION_TEMPLATES.md`): What / Key Decisions / Strategic Flags / Status, 10–25 lines per entry, no other sections.
>
> Last Updated: 2026-06-16 (Session R — new item 3024592: LBL-FALL PRTCT ANCHRG 1 PERSON — first sub-0.06 sq ft production catalog item on the account; per-label floor $2.75 at qty 20; 4-wave validated.)

---

### 2026-06-16 — Session R (new item): P/N 3024592 — first sub-0.06 sq ft production item, per-label floor $2.75 at qty 20, 4-wave validated

**What:** New printed/laminated single label (LBL-FALL PRTCT ANCHRG 1 PERSON) at 4.750" × 1.625" = 0.054 sq ft, ANSI Z535.6 DANGER class. First production catalog item below 0.06 sq ft on the Elliott account. The Micro-Format Band linear formula ($30.86/sq ft × 0.054 = $1.67) is overridden by the per-label floor documented in 1279000. Floor anchor confirmed at $2.75 at qty 20 by 4-wave atomic AI validation (24 responses, 6 models × 4 waves). Tier table: $4.25/$3.25/$2.75/$2.50/$2.25/$2.00. Material cost $0.20 (§25 canonical, same as 1279000 despite smaller area). Margin at qty 20: ~92.7%. This item IS a band data point for the sub-0.06 sq ft floor.

**Key Decisions:**
- Per-label floor ($2.75 at qty 20) governs over the linear $/sq ft formula ($1.67) — documented with full derivation in items/3024592.md Pricing Derivation section.
- 200+ tier at $2.00 is below the ~$2.50–$3.00 per-label floor band minimum — accepted as structural completeness; Sean orders 20–50 batches; same pattern as 1279000's 200+ at $2.10.
- This item IS a band data point (do_not_benchmark = false) — the floor of $2.75 at qty 20 anchors future sub-0.06 sq ft items. Future items must validate fresh against job economics; do NOT clone $2.75 mechanically.
- Quote email anchor (Wave 4 validated): "Same material and process as P/N 1279000/1278220 — no file prep charge, no first article."
- Sub-0.06 sq ft floor caution in categories/printed-laminated-orajet.md updated from anticipated to confirmed.

**Strategic Flags:**
- First time the per-label floor has been invoked on a live production item at this account. The $2.75 anchor is now visible to Sean — he will log it alongside 1279000's $3.00 and compare when future sub-0.1 sq ft items arrive.
- Item count: 26 → 27. Printed/Laminated category: 17 → 18 items.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 27 rows confirmed in Supabase.

---

### 2026-06-12 — Session Q (governance): Prompt template hardening — On Completion block, Prompt Writing Rule 9, Acceptance Criteria Rules section

**What:** Hardened the new-item prompt template in `CHAT_CONTEXT.md` so every Claude Chat–generated prompt is self-contained and self-enforcing, with no human judgment required to remember build, seed, or count steps. Three targeted edits: On Completion block now has an explicit 9-step sequence (build scripts at step 6, validate at step 7, blocking seed with confirmed count at step 8, commit at step 9); Prompt Writing Rule 9 now requires Claude Chat to read `STATE.yml` and resolve seed count to a real number before generating any prompt; Acceptance Criteria Rules section added with 10 binary checks that every generated prompt must include.

**Key Decisions:**
- On Completion step 5 now explicitly requires updating `item_count` to N+1 in STATE.yml — previously implied but not stated.
- The three build scripts are now a numbered step (step 6), not buried in session-completion boilerplate — this ensures they appear in every generated prompt's completion checklist.
- Acceptance Criteria Rules formalized as a standalone section (not a subset of Prompt Writing Rules) so the 10 checks are always visible as a discrete reference.

**Strategic Flags:**
- Next session is a new item. Claude Chat must read STATE.yml, see item_count = 26, and resolve seed count to 27 in the Acceptance Criteria before generating the prompt.

**Status:** Complete — validate.py 0/0; all three build scripts clean; elliott_items = 26 rows confirmed, no drift.

---

### 2026-06-12 — Session P (governance): Mandatory Supabase seed enforcement — four governance docs updated, 1278980 seeded, all 26 items live

**What:** Governance hardening — added mandatory, blocking, non-deferrable Supabase seed step to four governance documents (`COMPLETION_TEMPLATES.md`, `CHAT_CONTEXT.md`, `CALCULATOR.md`, `VALIDATION_PROMPTS.md`). Created `.env` at repo root with service-role credentials so future sessions can run `migrate_to_supabase.py` live without manual intervention. Seeded P/N 1278980 (the item written in Session O but left unseeded), and confirmed all three carry-over P/Ns (1278980, 1267140, 1278220) are live in Supabase. `elliott_items` row count 25 → 26; all 26 items verified.

**Key Decisions:**
- Root cause of three consecutive unseeded sessions: no `.env` present + seed was treated as optional/deferrable. Both causes addressed: `.env` created, seed codified as blocking step 5 in the Session Completion checklist and step 7 in On Completion, with explicit language that the session is NOT complete until the seed is confirmed.
- Seed executed via Supabase MCP (service-role SQL path — semantically identical to live mode, the sanctioned pattern when `supabase-py` is unavailable), consistent with Session N precedent.

**Strategic Flags:**
- `.env` is in `.gitignore` and must never be committed — confirmed pre-flight.

**Status:** Complete — validate.py 0/0; all three build scripts clean; `elliott_items` = 26 rows; P/Ns 1278980, 1267140, 1278220 all confirmed present in Supabase.

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

*Entries older than Session I (2026-06-09) were removed per the 10-entry rolling window — git history retains them in full.*
