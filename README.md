# University partner outreach

An [Agent Skills](https://agentskills.io/) package for researching a company, finding people with real leverage who may partner with a university organization, validating employment and email patterns, and writing a CSV.

Works with Cursor, Claude Code, Codex, and other tools that load `SKILL.md` skills.

## What it does

1. Asks for the **university org profile** (website, file, or description) if unknown, then targets technical / non-technical / field-specific roles to that niche.
2. Clarifies the outreach motion (campus/talent, partnerships, commercial intro, speakers).
3. Infers **company size** so cold seniority is appropriate (startup C-suite can be fine; hyperscale SVPs are not).
4. Defaults to **USA-based** contacts; opens other countries only if the US pool is exhausted.
5. Discovers the company’s email pattern from **evidence only** — never assumes `first.last`, `flast`, `first_last`, etc.
6. Keeps researching until the user’s **row count** is met with accurate records (no padding, no guessed inboxes).
7. Writes: `First Name, Last Name, Title, Company Name, Email`.

## Install

### Option A — paste this into any coding agent

Copy the block below into Claude Code, Codex, Cursor, or similar. Tell it where you want the skill (personal vs this project) if you care; otherwise it picks a sensible default for the tool it’s running in.

```text
Install the university-partner-outreach agent skill from
https://github.com/0ffffff/university-partner-outreach

1. Clone or sparse-checkout that repo (or download the skills/university-partner-outreach folder).
2. Detect which tool you are (Claude Code, Cursor, Codex, Copilot, OpenCode, or other).
3. Copy skills/university-partner-outreach/ (SKILL.md plus references/ and scripts/) into the correct skills directory for this tool:
   - Claude Code personal: ~/.claude/skills/university-partner-outreach/
   - Claude Code project:  .claude/skills/university-partner-outreach/
   - Cursor personal:      ~/.cursor/skills/university-partner-outreach/
   - Cursor project:       .cursor/skills/university-partner-outreach/ (also accepts .agents/skills/)
   - Codex user:           ~/.agents/skills/university-partner-outreach/ (or ~/.codex/skills/)
   - Codex repo:           .agents/skills/university-partner-outreach/
   - Copilot personal:     ~/.copilot/skills/university-partner-outreach/
   - Copilot project:      .github/skills/university-partner-outreach/
   - OpenCode:             ~/.agents/skills/ or .agents/skills/ (also ~/.config/opencode/skills/)
   Prefer personal install unless I say this is for one repo only.
4. Confirm the install path exists and contains SKILL.md. Tell me the path and how to invoke the skill.
5. Do not modify the skill contents unless I ask.
```

More detail (manual paths, repo layout): [INSTALL.md](INSTALL.md).

### Option B — use this repo as the project

Clone and open this folder in your coding agent. Canonical skill files live at:

```text
skills/university-partner-outreach/
```

This repo also exposes the same folder via symlinks under `.agents/skills/`, `.claude/skills/`, and `.cursor/skills/` so Cursor, Claude Code, and Codex can auto-discover it.

### Option C — manual copy

```bash
git clone https://github.com/0ffffff/university-partner-outreach.git
# pick one destination for your tool, e.g. Claude Code personal:
cp -R university-partner-outreach/skills/university-partner-outreach ~/.claude/skills/university-partner-outreach
```

Restart or start a new agent chat if the skill does not appear immediately.

## Usage

Ask the agent something like:

> Research Acme for 100+ USA-based people who could partner with our university org. Write a CSV with First Name, Last Name, Title, Company Name, Email.

If you have not described the org yet, the agent should ask for a website, file, or short description first (e.g. SWE club vs strategy consulting), then chase matching roles (TPMs/eng directors vs marketing/PMs, etc.).

Point at a sample CSV if you have a preferred shape. The agent should follow `SKILL.md` and the linked reference files.

## Layout

```text
skills/university-partner-outreach/
  SKILL.md                 # Main workflow (+ token hygiene)
  references/
    niche-roles.md         # Org niche → titles (load matching rows only)
    sources.md             # Where to look; trust tiers
    email-accuracy.md      # Pattern discovery + validation gates
    examples.md            # Fictional shape / archetype examples
  scripts/
    track.py               # Run signal (stdlib)
.agents/skills/…           # Symlink → skills/… (Codex / portable)
.claude/skills/…           # Symlink → skills/… (Claude Code)
.cursor/skills/…           # Symlink → skills/… (Cursor)
examples/
  sample-outreach-schema.csv
scripts/
  validate_outreach_csv.py # Repo-level CSV validator (not the skill script)
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
