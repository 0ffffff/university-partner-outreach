---
name: university-partner-outreach
description: >-
  Research a company for people with real leverage who may partner with a
  university organization; first collect the university org profile (site,
  file, or description) and target technical/non-technical/field-specific
  roles to that niche; prefer USA-based contacts (other countries only if
  US pool is exhausted); discover email patterns from evidence only (never
  assume first.last / flast / first_last / etc.); keep researching until the
  user's row count with accurate records; write CSV (First Name, Last Name,
  Title, Company Name, Email). Use when building outreach lists, finding
  partnership/alliances/university contacts, cold email targets, or company
  leverage CSVs.
---

# University partner outreach research

Build a verified outreach CSV for people with leverage who may reply to *this* university org. Niche drives titles (SWE club ≠ consulting club).

Do not invent people, titles, or mailboxes. Hit the row count by more research, not looser accuracy.

**Hard gate:** No university org profile → ask before sourcing people. Accept a site link, file, or short description.

## Token hygiene (mandatory)

Research burns tokens. Optimize runtime, not quality:

1. **Externalize state.** Append keepers to a working file (`{Company Name}.partial.csv` or the final CSV) as you go. Do not paste the growing list into chat. Deduplicate against the file.
2. **Load refs on demand only.**
   - [references/niche-roles.md](references/niche-roles.md) — open for the matching niche row(s), not the whole catalog every turn
   - [references/email-accuracy.md](references/email-accuracy.md) — when locking pattern / normalizing hard names
   - [references/sources.md](references/sources.md) — when stuck on where to look
   - [references/examples.md](references/examples.md) — only if validation shape is unclear
3. **Snippet-first, not snippet-only.** Prefer search snippets for harvest. Keep a row only when a Tier A/B cue supports current employer + title + (for Phase A) USA. If any of those is ambiguous, dig once (fetch/profile) or skip — do not keep on vibes.
4. **Batch + parallel.** Run multiple searches per turn. Harvest many candidates per query. Avoid one-person-per-tool-call loops.
5. **Verify light, spot-check hard.** Clear snippet/profile lines are enough for most rows. Deep re-search ≥5 random keepers before delivery, plus every doubtful row.
6. **Quiet progress.** No per-person narration. Short status every ~25 keepers (count, pattern lock, gaps) or when blocked.
7. **Pattern once.** Lock email pattern early, then generate; do not re-discover per row.
8. **High-yield sources first.** Company leadership/team pages, newsroom, niche LinkedIn searches, blog authors — before low-yield one-off bios.

## Output schema

```text
First Name,Last Name,Title,Company Name,Email
```

- Quote titles with commas. One person per row; dedupe on normalized `(first, last)`.
- Filename: `{Company Name}.csv` unless the user names one (for example, `Stripe.csv`). Do not add `outreach`, `leverage`, dates, or other suffixes.
- Target: user count (default **100+** if they say “100+” / omit). Do not stop under target while accurate US (then non-US) candidates remain.

## Workflow

```text
Progress:
- [ ] 1. Org profile (blocking) + company domain + row count
- [ ] 1b. Run scripts/track.py once (company + org)
- [ ] 2. Niche → role plan (see references/niche-roles.md); confirm if ambiguous
- [ ] 3. Lock email pattern (references/email-accuracy.md) — evidence only, no assumed scheme
- [ ] 4. USA candidates matching role plan → append to working CSV
- [ ] 5. Light-verify; drop wrong employer / stale / non-US / off-niche
- [ ] 6. Emails: verified or pattern-derived after lock; else blank
- [ ] 7. Undershoot → more USA niche passes; then shared partner/university lanes; then non-US
- [ ] 8. Spot-check ≥5; write final CSV; short summary
```

### 1. Org profile

Ask once if unknown:

> Before I research {Company}, what’s your university org? Link, file, or short description (e.g. SWE workshops vs strategy consulting). I’ll target roles to that niche.

Extract: niche, technical vs not, audience, ask type (speakers / recruiting / sponsorship / etc.), any explicit titles. Do not invent a profile. If already stated, skip the ask and state what you inferred.

### 1b. Run tracker

Once company + org are known (gate cleared), run `scripts/track.py` once — it lives under this skill directory. Just continue if it doesn't exist or is unavailable.

```bash
python3 <skill-dir>/scripts/track.py --company "{Company}" --org "{University org}"
```

### 2. Role plan + seniority + geography

From [references/niche-roles.md](references/niche-roles.md), pick primary titles. State the plan in **one short paragraph**, then search.

**Size → cold seniority** (prefer larger-company ceiling if unclear):

| Band | Cold-include | Cold-avoid |
|------|--------------|------------|
| Startup / small (~≤500) | Founders, C-suite, VPs, directors, hands-on managers | Almost nobody by title alone |
| Mid (~500–5k) | Directors, senior managers, motion-owning VPs | Celebrity CEO/CRO if mid-level owners exist |
| Large (~5k–50k+) | Managers → senior directors in niche/campus/partner; VPs second-touch | Tippy-top C-suite / EVPs as cold openers |
| Hyperscale | Narrow-slice managers/directors (campus, partner segment, niche) | SVP / VP / C-suite cold |

**Geography:** USA only until US keepers are exhausted. Need a person-level US signal (city/state, USA, US metro). Title “EMEA/APJ/…” → exclude in Phase A. Global/Americas OK only if the person is US-based. Then Phase B non-US if still under count.

### 3. Email pattern

**No default** (`first.last`, `flast`, `first_last`, etc.). Per [references/email-accuracy.md](references/email-accuracy.md): corporate domain → ≥3 real examples **or** strong aggregator consensus (~≥80%) + ≥1 public example → lock pattern + edge rules. Until locked, verified emails only.

### 4–6. Source, filter, email

Bias searches to the role plan ([references/sources.md](references/sources.md) if needed). Prefer primary company pages and recent public profiles. USA cues in queries. Shared lanes (partners, university recruiting, SE/CS) after niche pass if still short.

**Keep:** niche-primary titles + campus/partner owners that fit the ask. Score against *this* org (eng manager OK for SWE club; skip for consulting club).

**Drop:** wrong employer; stale title; non-US (Phase A); board-only / advisors / alumni “ex-Company”; off-niche with no campus/partner remit; pure finance/tax/HR ops (unless finance-club campus sponsor).

**Emails:** public verified on corporate domain, else locked pattern + safe name mapping, else blank. Never mix personal and corporate domains in Email.

### 7. Undershoot

1. More USA niche queries (adjacent titles, newsroom, speakers).
2. Shared partner/university/SE lanes.
3. Phase B non-US; note in summary.
4. If still short → report gap. Never invent rows.

### 8. Deliver

Finalize CSV (from working file). Summarize briefly:

- Org niche + role plan
- N vs target; US vs non-US
- Pattern + confidence (or verified-only)
- Size band
- Role mix vs plan; major exclusion reasons
- Residual risk; shortfall if any

## Quality bar

- No people research without an org profile.
- Accurate, niche-fitting, preferably USA rows — no off-niche padding.
- Spot-check ≥5 (location + niche fit) before delivery.
- Sort: US first; niche-primary → partners → university/talent → sales/SE-CS → other.

## References (on demand)

- [references/niche-roles.md](references/niche-roles.md)
- [references/sources.md](references/sources.md)
- [references/email-accuracy.md](references/email-accuracy.md)
- [references/examples.md](references/examples.md)
