# Agentic Vault Skeleton

**An Obsidian vault laid out so that any AI agent can find its way around without reading everything.**

Point an agent at a notes vault and it usually does one of two things: it reads far too much and
fills its context, or it guesses. This skeleton gives it a map instead. A few short files tell
the agent who you are, which folder holds what, which skills exist, and what happened last
session. Everything else is loaded only when a task needs it.

Part of [Digital Brain](https://github.com/OferBlum/personal-digital-brain-with-ai). The other
repos all drop into this layout.

## The idea

- **I write; agents read and enrich.** Your own notes are yours. Agents link them and summarize
  sources next to them, but never rewrite them.
- **One rules file for every agent.** `AGENTS.md` holds the working rules. `CLAUDE.md` only
  imports it, so Claude Code, Codex, Hermes or any other runtime follow the same rules.
- **A map, not a scan.** Three small core files in `0 - System/` answer the agent's first
  questions: `me.md` (who you are), `vault-map.md` (which folder holds what, and what's
  off limits), `skills-index.md` (what it can do).
- **Lazy-loaded skills.** The agent reads the skill catalog, not the skills. A skill's full
  instructions load only when a request matches its trigger, so the context holds the rules
  for the current task and nothing else. A new capability = one skill folder + one row.
- **Memory between sessions.** At session start the agent reads `_cache.md`; at session end it
  writes what it did. `trim_cache.py` keeps the last two sessions and archives the rest, so the
  cache stays short.
- **Privacy is a folder.** Private content stays in the private folder, enforced by
  [vault-privacy-guard](https://github.com/OferBlum/vault-privacy-guard).

## How information gets in

| What | Where | Who writes it |
|------|-------|---------------|
| Your ideas and notes | `2 - Notes/`, started from `4 - Templates/` | You |
| Topic hubs, one per life domain | `1 - Topics/` | You |
| Summaries of videos, articles, PDFs | `7 - Wikipedia/` | The agent, through the wiki skill |
| A summary you asked for | `2 - Notes/` | The agent |
| Journal and anything private | the private folder | You, and only you |

## Files

```text
AGENTS.md                    # the rules every agent follows: context, boundaries, execution
CLAUDE.md                    # Claude Code layer: imports AGENTS.md
0 - System/
  me.md                      # template: who you are, how AI should work with you
  vault-map.md               # folders, permissions, where to write what
  skills-index.md            # skill catalog: name, trigger, role
  _cache.md                  # last sessions, newest first
  hooks.json                 # session start: read the cache; session end: update + trim it
  scripts/trim_cache.py      # keeps N sessions in the cache, archives the rest (+ tests)
1 - Topics/  2 - Notes/      # your knowledge
3 - …/                       # the private folder (ships empty)
4 - Templates/               # Standard_Note.md with OKF frontmatter
5 - Tables/  6 - Images/     # Bases/Dataview tables, attachments
7 - Wikipedia/               # the AI-maintained wiki
```

`hooks.json` is written in plain language, so it works with any runtime: `AGENTS.md` tells
every agent to follow it.

## Quickstart

1. Copy this repo into your vault root (or open it as a new Obsidian vault).
2. Fill in `0 - System/me.md`, and rename folders in `vault-map.md` if yours differ.
3. Run `claude` (or any agent that reads `AGENTS.md`) at the vault root and ask it something.
   It reads the map first.

Tests: `python3 -m unittest discover -s "0 - System/scripts" -p "test_*.py"` (Python 3.8+,
standard library only).

## Add the other pieces

| Repo | Adds |
|------|------|
| [vault-privacy-guard](https://github.com/OferBlum/vault-privacy-guard) | a pre-tool hook that keeps every agent out of the private folder |
| [okf-frontmatter-standard](https://github.com/OferBlum/okf-frontmatter-standard) | `SCHEMA.md` and a validator for the frontmatter in the template |
| [llm-wiki-youtube-transcript](https://github.com/OferBlum/llm-wiki-youtube-transcript) | the wiki skill that fills `7 - Wikipedia/` |
| [vault-semantic-search](https://github.com/OferBlum/vault-semantic-search) | search by meaning, in Hebrew and English |
| [hermes-agent-layer](https://github.com/OferBlum/hermes-agent-layer) | the same vault, run by the Hermes agent |

## License

MIT, see [LICENSE](LICENSE).
