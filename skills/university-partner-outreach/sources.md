# Sources for verified people

Use multiple tiers. Promote a person to the CSV only when a **Tier A or B** source supports current employment (or two weaker sources agree).

## Tier A — primary / high trust

| Source | What to take | Caveats |
|--------|----------------|---------|
| Company leadership / team pages | Names, titles for execs and sometimes VPs | Incomplete for mid-level; still gold for top roles |
| Company newsroom / press releases | New hires, role announcements, quotes with title | Check date; people move |
| Company blog author pages | Name + title + employer | Titles lag; confirm still there |
| SEC filings / earnings / IR bios | Executives | Exec-heavy only |
| Conference / webinar speaker bios on company or major event sites | Name, title, company | Event may be months old |
| Official partner / marketplace / academic program pages | Named program owners | Rare but high signal |

## Tier B — strong secondary

| Source | What to take | Caveats |
|--------|----------------|---------|
| LinkedIn (current experience shows company) | Title, tenure dates | Hard to fetch at scale; use search snippets + public posts; watch for title inflation |
| GitHub/GitLab org members with company email or clear company affiliation | Engineering/DevRel leads | Not partnership-heavy |
| Patent assignments, standards bodies (IETF, etc.) with affiliation | Technical leads | Slow-moving titles |
| Reputable trade press interviews | Name + role | Confirm still current |

## Tier C — leads only (must re-verify)

| Source | Use | Do not |
|--------|-----|--------|
| Public org-chart sites | Seed names | Trust titles blindly |
| People-data / email-finder **person** records | Pattern hints, candidate names | Treat emails as verified without corroboration |
| Old conference decks, 2+ year articles | Historical names | Assume still employed |
| Aggregator “employees” lists / data scrapes | Volume | Ship without re-check |

## Geography

Default: **United States only.** Non-US (EMEA, APJ, UK, Canada, LatAm, etc.) only after the US keeper pool is exhausted and the row target still needs filling.

Location signals (need at least one credible cue for USA):

- LinkedIn / bio location: city + US state, “United States”, “USA”, “US”
- US metro named with the person (SF, NYC, Austin, Seattle, Chicago, Denver, Atlanta, Boston, etc.)
- Speaker/newsroom copy that places them in a US office

Not enough alone: “Americas” or “Global” in the title without a person-level US location. Exclude clear non-US territory titles (`EMEA`, `UKI`, `APJ`, `ANZ`, `Benelux`, country-specific outside US) during Phase A.

## Search recipes

Replace `{Company}` and `{Domain}`. Prefer US-biased queries first:

```text
{Company} leadership team
{Company} "Vice President" OR "Senior Director" OR "Director," partners OR alliances ("United States" OR USA OR "San Francisco" OR "New York" OR Austin OR Seattle)
{Company} "University Recruiting" OR "Early Career" OR "Campus" OR "Academic" (USA OR "United States")
{Company} "Alliance Manager" OR "Partner Manager" OR "Channel" OR "GSI" ("United States" OR USA)
"{Company}" "Partner" (Director OR Manager) ("United States" OR "San Francisco" OR "New York") site:linkedin.com
site:{Domain}/blog/ author OR "posted by"
site:{Domain}/newsroom OR site:{Domain}/press
"{name}" "{Company}" (Director OR Manager OR "Vice President")
"{name}" "{Company}" (location OR based OR "United States" OR "San Francisco" OR Austin)
```

Add recent-year filters when noise is high. Phase B (only if US exhausted): drop the US filters; add region keywords as needed.

For email pattern discovery specifically, see [email-accuracy.md](email-accuracy.md).

## Role keywords that correlate with leverage for university partnerships

**First wave / high reply odds**

- Partner Territory / Regional Alliance Manager
- Partner Alliance Manager (GSI / ISV / strategic)
- University Recruiting / Campus / Early Careers Manager or Director
- Academic Alliances / Education partnerships
- Partner Sales Manager / Director
- Manager, Partner Solutions Engineering
- Director, Customer Success (Enterprise) — for expansion intros
- DevRel / Developer Education lead

**Second wave / routing power** (first wave at startups if no mid-level owners)

- Director / Senior Director, Global Partnerships or Alliances
- VP, Partners / Channels / Cloud Alliances
- Head of Technology Partnerships
- Director, Partner Marketing (program amplification)
- Product Manager / Director owning integration network or partner APIs
- Founders / C-suite / VPs at **small** companies who still own external partnerships

**Skip for cold asks — depends on size**

- **Hyperscale / large enterprise:** CEO, COO, CRO, SVP, generic VP — warm intro only (e.g. do not cold-email a hyperscale SVP)
- **Startup / small:** those same titles can be primary targets if they own the motion
- **Any size (wrong lane):** pure accounting, tax, internal audit, treasury; infra/SRE with no external surface; brand/comms unless CSR/university remit is explicit

## Currency + location checks

Before keeping a row:

1. Prefer evidence dated within **18 months** (12 when possible).
2. If only older evidence exists, search `"{Full Name}" {Company}` and `"{Full Name}"` + a competitor; drop if they left.
3. If two sources disagree on title, prefer the newer source; put the conservative (more recent public) title in the CSV.
4. Confirm **USA** location for Phase A; if unknown after a quick check, skip rather than assume.
