# University partner outreach (Cursor skill)

A Cursor Agent skill for researching a company, finding people with real leverage who may partner with a university organization, validating employment and email patterns, and writing a CSV.

## What it does

1. Clarifies the outreach motion (campus/talent, partnerships, commercial intro).
2. Infers **company size** so cold seniority is appropriate (startup C-suite can be fine; hyperscale SVPs are not).
3. Defaults to **USA-based** contacts; opens other countries only if the US pool is exhausted.
4. Discovers the company’s email pattern from **evidence only** — never assumes `first.last`, `flast`, `first_last`, etc.
5. Keeps researching until the user’s **row count** is met with accurate records (no padding, no guessed inboxes).
6. Writes: `First Name, Last Name, Title, Company Name, Email`.

## Install

### Option A — use this repo as the project

Open this folder in Cursor. The skill lives at:

```text
.cursor/skills/university-partner-outreach/
```

Project skills load from that path automatically.

### Option B — install as a personal skill

```bash
cp -R .cursor/skills/university-partner-outreach ~/.cursor/skills/university-partner-outreach
```

Restart or start a new agent chat so the skill is picked up.

## Usage

Ask the agent something like:

> Research Acme for 100+ USA-based people who could partner with our university org. Write a CSV with First Name, Last Name, Title, Company Name, Email.

Point at a sample CSV if you have a preferred shape. The agent should follow `SKILL.md` and the linked reference files.

## Layout

```text
.cursor/skills/university-partner-outreach/
  SKILL.md              # Main workflow
  sources.md            # Where to look; trust tiers
  email-accuracy.md     # Pattern discovery + validation gates
  examples.md           # Fictional shape / archetype examples
examples/
  sample-outreach-schema.csv
scripts/
  validate_outreach_csv.py
```

## Validate a CSV

```bash
python3 scripts/validate_outreach_csv.py path/to/outreach.csv
```

Checks required headers, non-empty fields, basic email shape, and duplicate name/email rows. It does **not** prove mailboxes exist.

## Privacy

Example names and addresses in the skill docs are fictional. Do not commit real outreach lists with personal data to this repo unless you intend to; keep generated CSVs local or gitignored.

## License

MIT — see [LICENSE](LICENSE).
