---
tags:
  - cache
background: Hot context carried between agent sessions
---

# Session Cache

> Read at session start, updated at session end (see `hooks.json`). Newest session first.
> `trim_cache.py` keeps the 2 most recent sessions here and moves older ones to `_cache-archive.md`.
