---
background: The vault's skill catalog and each skill's trigger — the one place a skill is registered
---

# skills-index.md — The Skill Catalog

> Agents read this table, not the skills. A skill is loaded only when a request matches its
> trigger, so the agent's context holds the rules for the task at hand and nothing else.

Each skill is a folder in the [agentskills.io](https://agentskills.io) format:
`.claude/skills/<name>/SKILL.md`, with optional `references/` and `scripts/` next to it.
Adding a capability = one folder + one row below.

| Skill | Trigger | Role |
|-------|---------|------|
| `example-skill` | "when the user says…" | One line on what it does |

The other Digital Brain repos each add a row here when you install them (for example
`wiki-librarian` and `vault-search`). Delete the example row once you have a real skill.

## Rules

- One row per skill; the trigger is what the user says, not what the skill does internally.
- Personal domain skills (investing, fitness, styling) follow the same pattern.
- Links: [[me]] · [[vault-map]] · [[AGENTS]]
