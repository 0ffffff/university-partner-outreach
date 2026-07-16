# Email accuracy

Bad addresses waste the list and burn sender reputation. There is **no overall default** email scheme — not `first.last`, not `flast` / first-initial+lastname, not `firstlast`, not `first_last`, not `last.first`, not anything else — until evidence for *this company* locks one.

**Pattern discovery and name normalization are mandatory** before any bulk generation. Prefer a blank Email cell over a fabricated mailbox. Hitting the user’s row count means finding more real people (and real/locked-pattern addresses), not guessing inboxes.

## Goal

For every Email cell, either:

1. **Verified**: address seen in a trustworthy public source for that person, or
2. **Pattern-safe**: generated from a **locked company pattern** with high confidence and unambiguous name mapping.

If neither applies, leave Email blank (or hold the row) and keep researching. Do not invent an address.

## Step A — Domain

1. Confirm the corporate mail domain (usually the company’s primary website domain, sometimes a variant like `company.com` vs `company.co.uk`).
2. Note subsidiaries / acquired brands: people may still use a legacy domain or the parent domain — verify with examples, do not assume.
3. Reject `@gmail.com` / personal domains for the Email column unless the user explicitly wants personal outreach.

## Step B — Discover the prevailing pattern

Do this even if the user suggests a pattern; user hints are hypotheses to test.

### Evidence to collect (stack until confident)

| Evidence | Weight |
|----------|--------|
| Multiple public pages showing `someone@domain` for current employees | High |
| Email-format aggregator pages showing one dominant % | Medium-high (corroborate with ≥1 real example) |
| Press releases, support docs, Git commits, research papers listing company emails | High |
| Single contact-info scrape or one random directory hit | Low alone |
| “Everyone uses first.last” folklore with zero examples | None |

### Candidate patterns (reference only — never a prior)

These are labels for what you might *observe*. None is preferred a priori:

| Pattern | Example |
|---------|---------|
| `first.last` | `jane.doe@acme.com` |
| `flast` | `jdoe@acme.com` |
| `firstl` | `janed@acme.com` |
| `firstlast` | `janedoe@acme.com` |
| `first` | `jane@acme.com` (collision-prone) |
| `first_last` | `jane_doe@acme.com` |
| `last.first` | `doe.jane@acme.com` |

If two patterns appear in the wild, do not “pick the SaaS-typical one.” Collect more examples until one dominates, or stick to per-person verified addresses only.

### Lock criteria

| Confidence | Requirement | Bulk generate? |
|------------|-------------|----------------|
| **High** | ≥3 real employee addresses on the same pattern, **or** aggregator ≥~80% on one pattern **plus** ≥1 corroborating public address | Yes |
| **Medium** | Aggregator consensus without public examples, **or** only 1–2 public examples | Yes only with explicit user accept of risk; flag in delivery notes |
| **Low** | Conflicting patterns, zero examples, or only industry folklore | **No** — keep researching the pattern; ship verified emails only (blank otherwise)

Record the locked pattern in your working notes and the final summary. If nothing locks, say so explicitly.

## Step C — Name → local-part normalization

Apply rules consistently. Document company-specific exceptions when public examples show them.

| Name situation | Default rule | Verify with examples when possible |
|----------------|--------------|-------------------------------------|
| Simple `Jane Doe` | Apply **only** the locked pattern (e.g. `jane.doe` *if* locked to `first.last`) | No lock → no generated local-part |
| Hyphenated last (`Fitz-Gerald`) | keep hyphen: `jane.fitz-gerald` | Some strip hyphens — only strip if examples show it |
| Multiple first names / preferred name | Use the name they use professionally publicly | Don’t expand nicknames (`Joe`↛`joseph`) unless verified |
| Particles (`van Ryn`, `de Vries`) | Often concatenated or first particle only — **needs examples** | e.g. `alex.vanryn` vs `alex.van.ryn` |
| Accents (`Ortuño`) | Usually ASCII-fold: `ortuno` | Match public examples |
| Apostrophes (`O'Keefe`) | Often removed: `okeefe` | Confirm |
| Initials / suffixes (`Jr`, `III`) | Omit suffixes | — |
| Very long / compound surnames | Prefer verified address; else skip email | Do not truncate randomly |

**Collision rule:** If two people would generate the same address, do not emit both as patterned emails; find verified addresses or drop the ambiguous one.

## Step D — Per-address verification (best effort)

True SMTP mailbox probe is often blocked and can look abusive. Prefer passive checks:

1. **Exact-string web search**: `"jane.doe@acme.com"` — hits on company site, talks, PDFs, GitHub → verified.
2. **Consistency**: address matches locked pattern and domain.
3. **Staleness**: email on an old slide is weak if they may have left — pair with current employment check.
4. **Catch-all domains**: if the domain accepts all local parts, patterned emails won’t bounce but may never be read. Note this risk; still prefer correct pattern.
5. Do **not** claim “mailbox exists” unless you have a real verifier result the user authorized. Say “pattern-derived” vs “publicly listed”.

### Confidence labels (internal; optional column only if user asks)

| Label | Meaning |
|-------|---------|
| `verified` | Public listing or authoritative doc for that person |
| `pattern_high` | Locked high-confidence pattern + clean name mapping |
| `pattern_medium` | Medium pattern confidence or awkward name |
| `unverified` | Should not appear in the CSV Email column |

Default CSV includes only `verified` and `pattern_high` (and `pattern_medium` only with user risk accept).

## Step E — Overrides

Maintain a small override map while building:

```text
(first_lower, last_lower) -> email
```

Use when a public source shows a non-default local part (e.g. `alex.kim@` instead of `alex.kimlee@`). Overrides always beat generation.

## Anti-patterns

- Assuming any scheme up front (`first.last`, `flast`, `firstlast`, `first_last`, etc.) because “most companies do X”
- Treating a user-suggested pattern as fact without testing it against real addresses
- Copying emails from SEO spam pages that list every permutation
- Using `@company.io` when employees actually use `@company.com`
- Generating emails for people whose employment you have not verified
- Homegrown “smart” guesses (`j.doe`, `jane.d`) without evidence that pattern exists at the company
- Stopping under the row target because pattern research is hard — keep finding people; use verified/blank emails until the pattern locks

## Minimal research script (agent checklist)

```text
[ ] Domain confirmed
[ ] Zero prior on pattern (no assumed scheme)
[ ] ≥3 example addresses OR (aggregator dominant % + ≥1 example)
[ ] Pattern locked; conflicts resolved — OR verified-only mode
[ ] Normalization rules written for hyphens/particles (from examples)
[ ] Sample 3 patterned emails searched as "quoted" strings
[ ] Only then generate patterned Email cells for the rest
```
