# Examples

Load only if CSV shape, niche targeting, or validation edge cases are unclear. Illustrative only — names and addresses are **fictional**.

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

## Org profile → role targeting

Same company, different university orgs → different cold lists.

| University org (fictional) | Profile input | Primary roles at Acme |
|----------------------------|---------------|------------------------|
| Bits & Bytes SWE Club | “Undergrad SWE club; workshops + mentorship” | TPM, Eng Manager/Director, DevRel, university recruiting (tech) |
| Crest Strategy Group | Link to consulting club site; case competitions | Strategy & ops, BD, PMM, marketing managers, university recruiting (non-tech) |
| Pixel Product Society | Chat: “PM club, product teardown nights” | PM, PMM, product ops, early careers (PM) |
| Harbor FinTech Forum | File: club one-pager, finance + markets focus | Corp dev / finance campus sponsors, university recruiting (finance), relevant PMs |

**Flow**

1. User: “Research Acme for 100+ outreach contacts.”
2. Agent: asks for org profile (link, file, or description) — does not invent one.
3. Agent: states niche + role plan, then researches.

## Profile archetypes

### A — Keep: high leverage + plausible reply

| Profile | Why |
|---------|-----|
| Partner Territory Alliance Manager | Owns partner relationships in a territory; used to inbound; can route or start a program conversation |
| Director, University Recruiting | Direct owner of campus/university motion |
| Manager, Partner Solutions Engineering | Technical + partner facing; often replies; can intro commercial owners |
| Sr. Director, Partner Success / PS | Operates post-sale partner motions; good for structured programs |
| Engineering Manager (SWE club ask) | Niche fit for technical orgs; speaker/mentor/hiring owner even without “partner” in title |
| Product Marketing Manager (consulting club ask) | Niche fit for strategy/business orgs; often owns narratives and campus-facing content |

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

### C — Remove for wrong lane (depends on org niche)

| Profile | Why |
|---------|-----|
| Corporate Controller / Tax Director | Cannot initiate university or partner programs (unless finance-club campus sponsor — rare) |
| Engineering Manager, internal platform | Wrong for consulting/marketing orgs; **keep** for SWE/technical clubs when they can speak, mentor, or hire |
| Brand Designer / internal Comms | Wrong for hard-tech clubs; **keep** for design/marketing orgs |
| Quota AE with no program remit | Sales pressure without partnership/campus ownership |

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

- Started people research without an org profile, then shipped a generic partner list for a technical club (or eng managers for a consulting club).
- Defaulted to `first.last` (or `flast` / `first_last`) before collecting company-specific examples.
- Built 200 rows as `flast@company.com` because one intern’s GitHub used that — meanwhile leadership pages show `first.last@`.
- Used a legacy acquired-brand domain without checking whether employees now use the parent domain.
- Kept an old speaker-bio email after public profiles show the person left for a competitor.
- Stopped at 60 rows when the user asked for 100+, instead of another source pass.
- Padded to count with off-niche titles instead of another niche source pass.

## End-to-end mini run (what “done” looks like)

1. User: “100+ people at {Company} who could partner with our university org.”
2. Agent asks for university org profile (link, file, or description) if missing. User: “We’re a strategy consulting club — case comps and alumni mentorship.”
3. Agent states role plan (e.g. strategy/ops, BD, PMM, marketing managers, university recruiting) and confirms domain.
4. Agent gathers real addresses until a pattern locks (no scheme assumed). Per [email-accuracy.md](email-accuracy.md).
5. Agent pulls **USA-based** niche roles + campus/partner owners from [sources.md](sources.md); verifies employment + location + niche fit.
6. Agent infers size band; applies seniority ceiling (e.g. keep startup CEO; drop hyperscale SVP). Drops off-niche titles (e.g. IC eng for a consulting club) and non-US territory roles.
7. If under 100 US keepers → another **USA** pass on the niche plan first, then shared partner/university lanes. Repeat until US pool is exhausted.
8. Only if still short → Phase B non-US; sort US first.
9. Agent writes `{Company Name}.csv` (for example, `Stripe.csv`) once count is met.
10. Agent reports: org niche + role plan, N vs target, US vs non-US, size band + seniority ceiling, pattern + confidence (or verified-only), role mix vs plan, residual risk.

## Optional user knobs

Honor if present:

- University org profile (link, file, or description) — **required** before research if not already known
- Explicit role list or “technical only” / “non-technical only”
- Sample CSV path (schema/style)
- Minimum row count
- Force-include or force-exclude C-suite / SVP (overrides size heuristic)
- Override geography (default remains USA-first; user may force EMEA-only, global, etc.)
- Talent-only vs partnership-only vs mixed
- Accept medium-confidence patterned emails
- Explicit company size band if inference would be wrong
