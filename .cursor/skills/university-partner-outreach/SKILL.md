---
name: university-partner-outreach
description: >-
  Research a company for people with real leverage who may partner with a
  university organization; prefer USA-based contacts (other countries only if
  US pool is exhausted); discover email patterns from evidence only (never
  assume first.last / flast / first_last / etc.); keep researching until the
  user's row count with accurate records; write CSV (First Name, Last Name,
  Title, Company Name, Email). Use when building outreach lists, finding
  partnership/alliances/university contacts, cold email targets, or company
  leverage CSVs.
---

# University partner outreach research

Build a verified outreach CSV for a target company: people with **leverage** who are also **plausible cold responders** for a university partnership (programs, research, talent, ecosystem, sponsorship, or commercial intro).

Do not invent people, titles, or mailboxes. Hit the user’s row count by **keeping the research loop going**, not by loosening accuracy.

## Output schema

Default columns (match sample CSVs if the user provides one):

```text
First Name,Last Name,Title,Company Name,Email
```

- Quote titles that contain commas.
- One person per row; dedupe on normalized `(first, last)`.
- Filename: `{company-slug}-leverage-outreach.csv` unless the user names one.
- Target size: whatever the user specifies (default **100+** if they say “100+” / don’t name a number). **Do not stop under that count** while accurate candidates still exist in public sources — open new source passes and role slices until you reach it.

## Workflow checklist

Copy and track:

```text
Progress:
- [ ] 1. Clarify ask + company domain + target row count
- [ ] 2. Discover + lock email pattern from evidence only (see email-accuracy.md)
- [ ] 3. Pull USA-based candidates from primary sources
- [ ] 4. Verify each row (employer + title + USA location)
- [ ] 5. Score leverage + reply likelihood; filter conservatively
- [ ] 6. Assign emails: verified, or pattern-derived only after lock
- [ ] 7. If under target → more USA passes; only then open non-US
- [ ] 8. Write CSV; report counts, US vs non-US, pattern confidence, gaps
```

### 1. Clarify the ask

Infer from the user; ask only if blocking:

| Signal | Prefer roles |
|--------|----------------|
| University / campus / talent | University recruiting, early careers, TA partners, academic alliances, DevRel education |
| Partnership / ecosystem | Partners, alliances, channels, ISV/GSI, partner marketing, integration network PM |
| Client / commercial intro | Partner sales, solutions engineering mgrs, customer success directors, deal desk (not pure finance) |

If unclear, default to **university + partnership** mix (seniority still follows company size below).

**Company size → seniority ceiling (cold outreach):** Infer roughly from headcount, funding stage, or household-name scale. Senior titles are worth emailing at small companies; at giants they are noise.

| Size band | Rough signals | Cold-include | Cold-avoid / second-touch only |
|-----------|---------------|--------------|--------------------------------|
| **Startup / small** | ~≤200–500 employees, early/growth stage, thin partner org | Founders, C-suite, VPs, directors, hands-on managers — often the same people own partnerships | Almost nobody by title alone; still skip pure internal finance/legal unless they own the motion |
| **Mid-market** | ~500–5k, named directors/VPs per function | Directors, senior managers, partner/university owners; selective VPs who own the motion | CEO/CRO-level unless no mid-level owners exist |
| **Large enterprise** | ~5k–50k+ employees, deep functional orgs | Managers → senior directors in partner/university/SE/CS; motion-owning VPs as **second-touch** | Tippy-top C-suite / presidents / EVPs as cold openers |
| **Hyperscale** | Amazon, Google, Microsoft, Meta-scale headcount and layers | Managers, senior managers, directors who own a narrow slice (campus, partner segment) | SVP / VP / C-suite cold email — do not include as primary targets (warm intro only) |

When size is ambiguous, prefer the **more conservative** (larger-company) ceiling. State the band you assumed in the delivery summary.

**Geography (default):** **USA only.** Include someone only when public evidence puts them in the United States (city/state, “United States” / “USA”, or a US metro HQ/remote-US signal). Titles like “EMEA”, “APJ”, “UKI”, “Benelux”, “ANZ”, country names outside the US → exclude while the US pool still has runway. Global/Americas titles are OK **only if** the person themselves is US-based. Open other countries/regions **only after** US-qualified keepers are exhausted and you still need rows for the target count; note non-US rows in the delivery summary.

### 2. Lock the email pattern before bulk generation

**No default pattern.** Do not assume `first.last`, `flast`, `firstl`, `firstlast`, `first_last`, `last.first`, or any other scheme until evidence for *this* company locks one.

Follow [email-accuracy.md](email-accuracy.md). Minimum bar before patterned emails:

1. Identify corporate domain(s) (exclude personal Gmail etc.).
2. Collect **≥3 independent examples** of real employee addresses **or** a strong aggregator consensus (≥~80% on one pattern) plus ≥1 public example.
3. Document the winning pattern and edge-case rules (hyphens, particles, middle initials).
4. If pattern confidence is still low: keep researching the pattern in parallel with people research; use only **personally verified** addresses until a pattern locks. Do not fill the Email column with guesses.

### 3. Source candidates (loop until count)

Use [sources.md](sources.md). Prefer primary company pages and recent public profiles over stale directories.

**Phase A — USA only.** Bias searches with US location cues (`"United States" OR "USA" OR "San Francisco" OR "New York" OR Austin OR Chicago OR Denver OR Seattle OR Atlanta OR "Bay Area"` / LinkedIn location United States). Skip profiles that clearly sit outside the US.

Search loops that work:

- `"{Company}" leadership` / company About + Leadership (keep US-based names)
- `"{Company}" "Partner" OR "Alliances" OR "University" OR "Campus" director OR manager ("United States" OR USA OR "San Francisco" OR "New York")`
- `site:linkedin.com/in "{Company}" "Alliance Manager" OR "Partner Manager" OR "University Recruiting"` + US location
- Company blog authors, newsroom quotes, conference speaker lists (drop non-US)
- Org-chart aggregators only as leads — re-verify employer + **location** elsewhere

**Undershoot rule (ordered):**

1. Still under target and US candidates remain → another **USA** pass (widen roles: partner sales, SE, CS, DevRel, US regional alliances; blog/newsroom; speakers). Re-verify, merge, dedupe.
2. US pool genuinely exhausted and still under target → **Phase B:** open other countries/regions, same accuracy bar. Mark them clearly in the summary (and optionally sort US rows first).
3. If still short after that → report shortfall and what you tried. Never invent rows.

### 4. Verify employment + location

For each keep candidate, require:

- Current employer is the target company (or majority-owned subsidiary the user accepted).
- Title is plausible and not clearly outdated (prefer sources from last ~12–18 months; flag older).
- **Location:** USA for Phase A. If location is unknown, do not assume US — dig once (LinkedIn location, speaker bio, newsroom); if still unclear, skip or park until confirmed. Phase B (non-US) only after US exhaustion.
- Exclude board-only, advisors, alumni “ex-Company”, contractors mislabeled as employees unless user wants them.

### 5. Leverage + reply likelihood (size-aware filter)

**Keep by function** (always high value when they exist):

- Partner / alliances / channel / ecosystem managers → directors (→ VPs per size table)
- University / campus / early careers / academic programs
- Partner sales, SE managers, CS enterprise directors, partner success
- Product owners of partner/integration surfaces (e.g. integration network)
- DevRel / developer ecosystem leads tied to education or partners

**Seniority** — apply the size table from §1. Examples:

- Small startup: including the CEO or Head of Partnerships is reasonable; they often *are* the partnership desk.
- Mid-size: directors and motion-owning VPs are fair cold targets; skip celebrity C-suite if mid-level owners exist.
- Large / hyperscale: do **not** cold-target SVPs or generic VPs; go after the manager/director who owns campus, a partner segment, or SE for that slice.

**Remove regardless of size** (wrong lane, not “too senior”):

- Pure HR ops / internal finance / tax / audit / IR
- Deep eng delivery managers with no GTM/partner surface
- Comms/brand with no partnership remit
- People/TA generalists when the ask is commercial partnership (keep when ask is campus/talent)

When filtering an existing list: remove only clear non-responders / wrong lane; keep borderline names. Do not strip startup C-suite just because a large-co heuristic says so.

**Cold-first wave order:**

- **Startup / small:** motion owners first (often founder/C-suite/VP) → directors/managers who run the program day to day
- **Mid → large:** territory/regional partner managers → partner sales / SE managers → university & academic program owners → alliance directors → VPs as second-touch
- **Hyperscale:** narrow-scope managers/directors only; VPs/SVPs off the cold list

### 6. Emails

Per row:

1. Use a **publicly verified** address if found (must match the corporate domain you confirmed).
2. Else generate only from a **locked** pattern + documented name normalization — never from an assumed industry default.
3. If the pattern is not locked yet, or the name cannot be normalized safely, leave Email blank and keep researching — or hold the row out of the ship set until the address is solid. Do not guess.
4. Never mix personal and corporate domains in the Email column.

A blank email on an otherwise good row is better than a wrong inbox; replace blanks as verification comes in while you continue toward the row count.

### 7. Deliver

Write the CSV only when row count ≥ target (or sources exhausted). Summarize:

- Row count vs target, unique people, unique emails
- **US vs non-US counts** (non-US should be 0 unless Phase B was required)
- Locked pattern + confidence (high / medium / low) and evidence used — or “no pattern locked; verified emails only”
- Assumed **company size band** and seniority ceiling applied
- Role mix (partners / university / sales-SE-CS / product / other)
- Who was excluded and why (short) — include non-US skips and “too senior for this company size” if relevant
- Remaining risk (catch-all domain, pattern-derived vs verified share, stale titles, weak location signals)
- If under target: passes attempted and why you stopped

## Quality bar

- Meet the user’s count with **accurate**, preferably **USA-based** records; close gaps by more US research first, then non-US only if needed — never by fabrications.
- Spot-check ≥5 random rows (including location) against a fresh search before delivery.
- Deduplicate; fix obvious title/company inconsistencies.
- Sort: US rows first; within that, partners/alliances → university/talent → sales/SE/CS → product → other.

## Additional resources

- [sources.md](sources.md) — where to look; trust tiers
- [email-accuracy.md](email-accuracy.md) — pattern discovery, normalization, confidence gates
- [examples.md](examples.md) — profile types, validation examples, anti-patterns
