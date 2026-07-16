# Install

This package follows the [Agent Skills](https://agentskills.io/) format: a folder with `SKILL.md` plus supporting markdown. Same files work across tools; only the install path changes.

Canonical source in this repo:

```text
skills/university-partner-outreach/
```

## Paste into any coding agent

Use this when you want Claude Code, Codex, Cursor, or another agent to install the skill for you:

```text
Install the university-partner-outreach agent skill from
https://github.com/0ffffff/university-partner-outreach

1. Clone or sparse-checkout that repo (or download the skills/university-partner-outreach folder).
2. Detect which tool you are (Claude Code, Cursor, Codex, Copilot, OpenCode, or other).
3. Copy skills/university-partner-outreach/ (SKILL.md plus niche-roles.md, email-accuracy.md, sources.md, examples.md) into the correct skills directory for this tool:
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

## Manual install by tool

| Tool | Personal (all projects) | Project (this repo only) |
|------|-------------------------|--------------------------|
| Claude Code | `~/.claude/skills/university-partner-outreach/` | `.claude/skills/university-partner-outreach/` |
| Cursor | `~/.cursor/skills/university-partner-outreach/` | `.cursor/skills/` or `.agents/skills/` |
| Codex | `~/.agents/skills/` or `~/.codex/skills/` | `.agents/skills/university-partner-outreach/` |
| GitHub Copilot | `~/.copilot/skills/` | `.github/skills/university-partner-outreach/` |
| OpenCode | `~/.agents/skills/` or `~/.config/opencode/skills/` | `.agents/skills/` or `.opencode/skills/` |

Example (Claude Code, personal):

```bash
git clone https://github.com/0ffffff/university-partner-outreach.git
mkdir -p ~/.claude/skills
cp -R university-partner-outreach/skills/university-partner-outreach ~/.claude/skills/
```

Example (Codex, user):

```bash
mkdir -p ~/.agents/skills
cp -R university-partner-outreach/skills/university-partner-outreach ~/.agents/skills/
```

After copying, start a new agent session (or restart the tool) if the skill does not show up.

## Using this repo as the working directory

Open the cloned repo in your agent. Symlinks under `.agents/skills/`, `.claude/skills/`, and `.cursor/skills/` point at `skills/university-partner-outreach/`, so discovery works without a separate copy step.
