# Examples

Illustrative only. Names, companies, and addresses below are **fictional** placeholders for shape and validation logic—not real contacts.

## Good CSV row shape

University / talent oriented:

```csv
First Name,Last Name,Title,Company Name,Email
Alex,Rivera,"Manager, University Recruiting and Intern Program",Acme Corp,alex.rivera@acme.com
Sam,Okada,Head of Social Impact,Acme Corp,sam.okada@acme.com
```

Partnership oriented (cold-first wave):

```csv
First Name,Last Name,Title,Company Name,Email
Jordan,Lee,Partner Territory Alliance Manager,Acme Corp,jordan.lee@acme.com
Riley,Chen,"Director of Product Management, Integration Network",Acme Corp,riley.chen@acme.com
Casey,Nguyen,"Director, University Talent Acquisition",Acme Corp,casey.nguyen@acme.com
```

## Profile archetypes

### A — Keep: high leverage + plausible reply

| Profile | Why |
|---------|-----|
| Partner Territory Alliance Manager | Owns partner relationships in a territory; used to inbound; can route or start a program conversation |
| Director, University Recruiting | Direct owner of campus/university motion |
| Manager, Partner Solutions Engineering | Technical + partner facing; often replies; can intro commercial owners |
| Sr. Director, Partner Success / PS | Operates post-sale partner motions; good for structured programs |

**Validation sketch**

1. LinkedIn/newsroom/blog shows current company + title.
2. Company email pattern locked via multiple public examples / aggregator consensus (no scheme assumed up front).
3. Email: patterned from the **locked** scheme unless a public override exists.

### B — Seniority is company-size dependent

| Profile | Large / hyperscale | Startup / small |
|---------|--------------------|-----------------|
| VP, Americas Partners & Alliances | Second-touch / warm intro | Fair cold target if they own partners |
| CEO / founder | Do not cold-email | Often the right inbox |
| Global Alliance Director, GSIs | Often second wave | First wave if no managers below |
| SVP | Exclude from cold list | Rare title; treat like C-suite at small cos — include if hands-on |

### C — Remove for wrong lane (any size)

| Profile | Why |
|---------|-----|
| Corporate Controller / Tax Director | Cannot initiate university or partner programs |
| Engineering Manager, internal platform | Leverage on delivery, not on external partnership intake |
| Brand Designer / internal Comms | No contract or program authority |

## Email validation examples

### Pattern lock (illustrative)

**Evidence gathered**

- Format aggregators report a dominant share for `firstname.lastname@acme.com`
- Corroborating public strings / docs consistent with that pattern

**Locked pattern:** `first.last@acme.com` (ASCII, lowercase)

**Normalization examples** (fictional)

| Public name | Email used | Rule |
|-------------|------------|------|
| Jane Fitz-Gerald | `jane.fitz-gerald@acme.com` | keep hyphen |
| Pat O'Keefe | `pat.okeefe@acme.com` | drop apostrophe |
| Alex van Ryn | `alex.vanryn@acme.com` | particle concatenated only when examples show that form — if unknown, skip |
| Morgan Belmonte Ortuño | `morgan.belmonte@acme.com` | verified/override shorter local-part; do not invent a longer guess |

**Delivery language**

> No pattern assumed up front. Evidence locked `firstname.lastname@acme.com` (high confidence). Most rows are pattern-derived after that lock, not mailbox-probed. Compound names use documented overrides.

### Verified vs patterned

| Situation | Email column | Notes to user |
|-----------|--------------|---------------|
| Press PDF lists `sara.nguyen@acme.com` and they still work there | `sara.nguyen@acme.com` | Verified |
| No public email; pattern high; name is `Sara Nguyen` | `sara.nguyen@acme.com` | Pattern-derived |
| Only evidence is `snguyen@acme.com` for others, but aggregators say `first.last` dominates | Research more | Do not mix patterns in one CSV without proof both are valid |
| Name is compound with particles and no custom local-part examples | Prefer omit Email or omit row | Ambiguous mapping |

### Failed validation (do not ship)

- Defaulted to `first.last` (or `flast` / `first_last`) before collecting company-specific examples.
- Built 200 rows as `flast@company.com` because one intern’s GitHub used that — meanwhile leadership pages show `first.last@`.
- Used a legacy acquired-brand domain without checking whether employees now use the parent domain.
- Kept an old speaker-bio email after public profiles show the person left for a competitor.
- Stopped at 60 rows when the user asked for 100+, instead of another source pass.

## End-to-end mini run (what “done” looks like)

1. User: “100+ people at {Company} who could partner with our university org.”
2. Agent confirms domain; gathers real addresses until a pattern locks (no scheme assumed). Per [email-accuracy.md](email-accuracy.md).
3. Agent pulls **USA-based** partners + university + SE/CS from [sources.md](sources.md); verifies employment + location.
4. Agent infers size band; applies seniority ceiling (e.g. keep startup CEO; drop hyperscale SVP). Drops finance / pure internal eng / non-US territory roles; keeps US motion owners.
5. If under 100 US keepers → another **USA** pass (roles, blog authors, speakers). Repeat until US pool is exhausted.
6. Only if still short → Phase B non-US; sort US first.
7. Agent writes `{company}-leverage-outreach.csv` once count is met.
8. Agent reports: N vs target, US vs non-US, size band + seniority ceiling, pattern + confidence (or verified-only), role mix, residual risk.

## Optional user knobs

Honor if present:

- Sample CSV path (schema/style)
- Minimum row count
- Force-include or force-exclude C-suite / SVP (overrides size heuristic)
- Override geography (default remains USA-first; user may force EMEA-only, global, etc.)
- Talent-only vs partnership-only vs mixed
- Accept medium-confidence patterned emails
- Explicit company size band if inference would be wrong
