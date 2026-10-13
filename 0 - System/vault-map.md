---
background: Vault navigation map — what's in each folder, what's off limits, and where to write what
---

# vault-map.md — The Vault Map

> Lets any agent navigate the vault without scanning it. Update it when the folder structure changes.

Identity: [[me]]. Working rules: [[AGENTS]]. Skill catalog: [[skills-index]].

## Folder map

| Folder | Contents | Permission |
|--------|----------|------------|
| `0 - System/` | core files (me, vault-map, skills-index), session cache, hooks, scripts | Read. **Never modify** without an explicit request |
| `1 - Topics/` | one hub page per life domain | Read; add links on request |
| `2 - Notes/` | the user's own notes and ideas, plus summaries they asked for | Their ideas — never rewrite them |
| `3 - …/` | **the private folder**: the journal and every private file | ⛔ Off limits — no read, write, list, index, or memory |
| `4 - Templates/` | templates for new notes | Don't modify; use as the base for new notes |
| `5 - Tables/` | Obsidian Bases / Dataview table files | Don't modify |
| `6 - Images/` | attachments | Don't modify |
| `7 - Wikipedia/` | the AI-maintained wiki of source summaries | Write and maintain through the wiki skill |

## Privacy (above everything)

1. Never open, mention, or remember a file inside the private folder.
2. Never **map** it either: no listing, globbing, or recursing into it. Start every scan at a
   content folder, never at the vault root.

The folder is the whole rule; there is no `private:` frontmatter flag.

A filename starting with `_` is a **generated file, not a secret**: skip it when indexing, but
read it when needed. `_cache.md` is read at every session start.

## Where to write what

- **A summary of an external source** → `7 - Wikipedia/`.
- **A summary the user explicitly asked for** → `2 - Notes/`.
- **A quick capture** → a new note in `2 - Notes/`, never the private folder.
- **Every new file** → start from `4 - Templates/Standard_Note.md` and fill in its frontmatter.
