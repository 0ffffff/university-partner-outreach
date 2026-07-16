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

Build a verified outreach CSV for a target company: people with **leverage** who are also **plausible cold responders** for *this* university organization. Role targeting follows the org’s niche (technical club ≠ consulting club ≠ marketing org).

Do not invent people, titles, or mailboxes. Hit the user’s row count by **keeping the research loop going**, not by loosening accuracy.

**Hard gate:** If you do not yet have a university org profile, **stop and ask** before sourcing people. A company name alone is not enough.

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
- [ ] 1. Collect university org profile (blocking) + company domain + row count
- [ ] 2. Derive niche → role targeting plan; confirm briefly with user if ambiguous
- [ ] 3. Discover + lock email pattern from evidence only (see email-accuracy.md)
- [ ] 4. Pull USA-based candidates matching the niche role plan
- [ ] 5. Verify each row (employer + title + USA location)
- [ ] 6. Score leverage + reply likelihood for this org; filter conservatively
- [ ] 7. Assign emails: verified, or pattern-derived only after lock
- [ ] 8. If under target → more USA passes on niche roles; only then open non-US
- [ ] 9. Write CSV; report org niche, role plan, counts, US vs non-US, pattern confidence, gaps
```

### 1. Collect the university org profile (blocking)

When the user asks to research a company and you do **not** already know their university org, ask before any people search. Accept any of:

- Link to the org website / LinkedIn / Notion / Linktree
- A file (PDF, doc, deck, README)
- A short description in chat (mission, audience, what they want from companies)

Ask for enough to answer: **What does this org do, who is it for, and what partnership would look like?** One crisp question is enough, for example:

> Before I research {Company}, what’s your university org? Drop a website link, a file, or a short description (e.g. “SWE club running technical workshops” or “strategy consulting org placing analysts”). I’ll target roles to that niche.

Do **not** invent an org profile. Do **not** default to a generic “university + partners” mix when the niche is knowable. If the user already stated the niche in the first message, skip the ask and state the profile you inferred.

**From the profile, extract:**

| Field | Why it matters |
|-------|----------------|
| Niche / domain | Technical, consulting, product, design, finance, healthcare, policy, etc. |
| Technical vs non-technical | Whether eng/TPM/DevRel lanes are primary or secondary |
| Audience | Undergrads, grads, career switchers, researchers |
| Ask type | Speakers, mentorship, recruiting, sponsorship, case collab, research, product feedback |
| Explicit role hints | Honor any titles the user names |

### 2. Map org niche → role targeting

Build a short **role plan** before sourcing. Partner / university / campus owners stay useful across niches, but the **primary** cold list should match the org.

| Org niche (examples) | Primary roles to chase | Usually secondary / skip unless user asks |
|----------------------|------------------------|-------------------------------------------|
| **Technical / SWE / CS club**, hackathon org, robotics | TPMs, engineering managers/directors (relevant stack), DevRel, developer advocates, university recruiting (tech), solutions eng managers | Brand marketers, generic sales, finance |
| **Product / PM club** | Product managers/directors, PMM, product ops, university/early careers for PM tracks | Deep infrastructure eng with no product surface |
| **Strategy / management consulting club** | Strategy & ops, management consultants (firm side), business development, product marketing managers, program managers, university recruiting (non-tech) | IC software engineers, deep eng managers |
| **Marketing / communications org** | Marketing managers/directors, brand, growth, content, PMM, campus marketing | Pure eng delivery, tax/finance |
| **Finance / investment club** | Corporate development, IR (only if they own campus/programs), FP&A leaders who sponsor case comps, university recruiting (finance) | Eng managers, DevRel |
| **Design / HCI / creative** | Design managers/directors, design systems leads, UX research managers, creative brand leads | Backend eng managers |
| **Data / analytics / AI (applied)** | Data science/ML managers, analytics leads, AI product managers, applied science managers, DevRel for ML | Pure quota AE with no program remit |
| **Entrepreneurship / VC club** | Startup program leads, venture/platform partners, campus innovation, bizdev | Individual contributor eng |
| **Healthcare / bio / pre-med** | Medical affairs education, clinical partnerships, university relations (health), relevant product leads | Unrelated consumer brand marketers |
| **Policy / public interest / law** | Public policy, government affairs education outreach, legal community programs, university relations | Product eng |

**Also apply ask-type overlays** (stack on top of niche):

| Ask type | Prefer roles |
|----------|----------------|
| Campus / talent / recruiting | University recruiting, early careers, TA partners, academic alliances, DevRel education |
| Partnership / ecosystem / sponsorship | Partners, alliances, channels, ISV/GSI, partner marketing, community/education sponsors |
| Client / commercial intro | Partner sales, solutions engineering mgrs, customer success directors (not pure finance) |
| Speakers / workshops | Practitioners + program owners in the niche (EM/TPM for SWE; PM/PMM for consulting/marketing) |

If the niche is mixed or unclear after the profile, ask one clarifying question (“more technical hiring/speakers, or business/strategy?”). If still unclear, default to a **balanced niche mix** and say so in the summary — still not a blind generic list.

State the role plan in one short paragraph before the first source pass (or confirm it if you asked a clarifying question).

**Company size → seniority ceiling (cold outreach):** Infer roughly from headcount, funding stage, or household-name scale. Senior titles are worth emailing at small companies; at giants they are noise.

| Size band | Rough signals | Cold-include | Cold-avoid / second-touch only |
|-----------|---------------|--------------|--------------------------------|
| **Startup / small** | ~≤200–500 employees, early/growth stage, thin partner org | Founders, C-suite, VPs, directors, hands-on managers — often the same people own partnerships | Almost nobody by title alone; still skip pure internal finance/legal unless they own the motion |
| **Mid-market** | ~500–5k, named directors/VPs per function | Directors, senior managers, partner/university owners; selective VPs who own the motion | CEO/CRO-level unless no mid-level owners exist |
| **Large enterprise** | ~5k–50k+ employees, deep functional orgs | Managers → senior directors in partner/university/SE/CS; motion-owning VPs as **second-touch** | Tippy-top C-suite / presidents / EVPs as cold openers |
| **Hyperscale** | Amazon, Google, Microsoft, Meta-scale headcount and layers | Managers, senior managers, directors who own a narrow slice (campus, partner segment, or niche function) | SVP / VP / C-suite cold email — do not include as primary targets (warm intro only) |

When size is ambiguous, prefer the **more conservative** (larger-company) ceiling. State the band you assumed in the delivery summary.

**Geography (default):** **USA only.** Include someone only when public evidence puts them in the United States (city/state, “United States” / “USA”, or a US metro HQ/remote-US signal). Titles like “EMEA”, “APJ”, “UKI”, “Benelux”, “ANZ”, country names outside the US → exclude while the US pool still has runway. Global/Americas titles are OK **only if** the person themselves is US-based. Open other countries/regions **only after** US-qualified keepers are exhausted and you still need rows for the target count; note non-US rows in the delivery summary.

### 3. Lock the email pattern before bulk generation

**No default pattern.** Do not assume `first.last`, `flast`, `firstl`, `firstlast`, `first_last`, `last.first`, or any other scheme until evidence for *this* company locks one.

Follow [email-accuracy.md](email-accuracy.md). Minimum bar before patterned emails:

1. Identify corporate domain(s) (exclude personal Gmail etc.).
2. Collect **≥3 independent examples** of real employee addresses **or** a strong aggregator consensus (≥~80% on one pattern) plus ≥1 public example.
3. Document the winning pattern and edge-case rules (hyphens, particles, middle initials).
4. If pattern confidence is still low: keep researching the pattern in parallel with people research; use only **personally verified** addresses until a pattern locks. Do not fill the Email column with guesses.

### 4. Source candidates (loop until count)

Use [sources.md](sources.md). Prefer primary company pages and recent public profiles over stale directories. **Bias every search toward the role plan from §2**, not a generic partner dump.

**Phase A — USA only.** Bias searches with US location cues (`"United States" OR "USA" OR "San Francisco" OR "New York" OR Austin OR Chicago OR Denver OR Seattle OR Atlanta OR "Bay Area"` / LinkedIn location United States). Skip profiles that clearly sit outside the US.

Search loops that work (swap niche titles from the role plan):

- `"{Company}" leadership` / company About + Leadership (keep US-based names that match niche or campus/partner ownership)
- `"{Company}" "Partner" OR "Alliances" OR "University" OR "Campus" director OR manager` + US location
- Niche title passes, e.g. technical org: `"{Company}" ("Engineering Manager" OR TPM OR "Technical Program" OR DevRel OR "Developer Advocate")`; consulting org: `"{Company}" ("Product Marketing" OR "Strategy" OR "Business Development" OR "Marketing Manager")`
- `site:linkedin.com/in "{Company}"` + niche titles from the role plan + US location
- Company blog authors, newsroom quotes, conference speaker lists in the niche (drop non-US)
- Org-chart aggregators only as leads — re-verify employer + **location** elsewhere

**Undershoot rule (ordered):**

1. Still under target and US candidates remain → another **USA** pass on the niche role plan first (widen within niche: adjacent titles, blog/newsroom, speakers). Then add shared lanes (partner sales, SE, CS, university recruiting, US regional alliances) if still short. Re-verify, merge, dedupe.
2. US pool genuinely exhausted and still under target → **Phase B:** open other countries/regions, same accuracy bar. Mark them clearly in the summary (and optionally sort US rows first).
3. If still short after that → report shortfall and what you tried. Never invent rows.

### 5. Verify employment + location

For each keep candidate, require:

- Current employer is the target company (or majority-owned subsidiary the user accepted).
- Title is plausible and not clearly outdated (prefer sources from last ~12–18 months; flag older).
- **Location:** USA for Phase A. If location is unknown, do not assume US — dig once (LinkedIn location, speaker bio, newsroom); if still unclear, skip or park until confirmed. Phase B (non-US) only after US exhaustion.
- Exclude board-only, advisors, alumni “ex-Company”, contractors mislabeled as employees unless user wants them.

### 6. Leverage + reply likelihood (niche- and size-aware)

**Keep by function — shared lanes** (high value across niches when they exist):

- Partner / alliances / channel / ecosystem managers → directors (→ VPs per size table)
- University / campus / early careers / academic programs
- Partner sales, SE managers, CS enterprise directors, partner success (when ask is commercial or sponsorship)

**Keep by function — niche lanes** (primary for the matching org; see §2):

- Technical orgs: TPMs, eng managers/directors in a relevant domain, DevRel / developer ecosystem, solutions eng managers
- Product orgs: PMs, PMM, product ops
- Consulting / business orgs: strategy & ops, BD, marketing/PMM managers, program managers
- Marketing orgs: marketing, brand, growth, content leads
- Other fields: the domain table in §2

A title that looks “wrong lane” for a generic partnership list can be **correct** for a niche org (e.g. Engineering Manager for an SWE club). Score against the org profile, not a one-size partnership heuristic.

**Seniority** — apply the size table from §2. Examples:

- Small startup: including the CEO or Head of Partnerships is reasonable; they often *are* the partnership desk.
- Mid-size: directors and motion-owning VPs are fair cold targets; skip celebrity C-suite if mid-level owners exist.
- Large / hyperscale: do **not** cold-target SVPs or generic VPs; go after the manager/director who owns campus, a partner segment, the niche function, or SE for that slice.

**Remove regardless of size** (wrong for *this* org, not merely “too senior”):

- Pure HR ops / internal finance / tax / audit (unless the org niche is finance and they own campus/programs)
- Roles outside the niche with no partnership, campus, or education remit (e.g. brand marketers for a hard-tech robotics club; IC backend eng for a strategy consulting org)
- People/TA generalists when the ask is commercial partnership (keep when ask is campus/talent)
- Deep eng delivery with no external/education surface — **except** when the org is technical and that manager is a plausible speaker/mentor/hiring owner

When filtering an existing list: remove only clear non-responders / wrong niche; keep borderline names. Do not strip startup C-suite just because a large-co heuristic says so.

**Cold-first wave order:**

- **Startup / small:** niche motion owners first (often founder/C-suite/VP) → directors/managers who run the program or function day to day
- **Mid → large:** niche function managers/directors → university & academic program owners → territory/regional partner managers → partner sales / SE → alliance directors → VPs as second-touch
- **Hyperscale:** narrow-scope managers/directors in the niche (or campus slice) only; VPs/SVPs off the cold list

### 7. Emails

Per row:

1. Use a **publicly verified** address if found (must match the corporate domain you confirmed).
2. Else generate only from a **locked** pattern + documented name normalization — never from an assumed industry default.
3. If the pattern is not locked yet, or the name cannot be normalized safely, leave Email blank and keep researching — or hold the row out of the ship set until the address is solid. Do not guess.
4. Never mix personal and corporate domains in the Email column.

A blank email on an otherwise good row is better than a wrong inbox; replace blanks as verification comes in while you continue toward the row count.

### 8. Deliver

Write the CSV only when row count ≥ target (or sources exhausted). Summarize:

- **University org niche** inferred + **role plan** used (primary titles chased)
- Row count vs target, unique people, unique emails
- **US vs non-US counts** (non-US should be 0 unless Phase B was required)
- Locked pattern + confidence (high / medium / low) and evidence used — or “no pattern locked; verified emails only”
- Assumed **company size band** and seniority ceiling applied
- Role mix vs plan (niche function / partners / university / sales-SE-CS / other)
- Who was excluded and why (short) — include off-niche skips, non-US skips, and “too senior for this company size” if relevant
- Remaining risk (catch-all domain, pattern-derived vs verified share, stale titles, weak location signals)
- If under target: passes attempted and why you stopped

## Quality bar

- Do not start people research without an org profile (asked or already provided).
- Meet the user’s count with **accurate**, preferably **USA-based** records that fit the niche role plan; close gaps by more US research first, then non-US only if needed — never by fabrications or off-niche padding.
- Spot-check ≥5 random rows (including location + niche fit) against a fresh search before delivery.
- Deduplicate; fix obvious title/company inconsistencies.
- Sort: US rows first; within that, niche-primary roles → partners/alliances → university/talent → sales/SE-CS → other.

## Additional resources

- [sources.md](sources.md) — where to look; trust tiers
- [email-accuracy.md](email-accuracy.md) — pattern discovery, normalization, confidence gates
- [examples.md](examples.md) — profile types, validation examples, anti-patterns
