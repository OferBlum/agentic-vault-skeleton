#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trim_cache.py — keeps only the N most recent sessions in _cache.md,
and moves the older ones into _cache-archive.md. Default: N=2.

Sessions are "## Session …" blocks, newest first. Both files are backed up
to 0 - System/.backup/ before anything is written.

Usage: python3 trim_cache.py [N]
"""
import os, re, shutil, sys
from datetime import datetime
from pathlib import Path

SYSTEM_DIR = "0 - System"
CACHE_NAME = "_cache.md"
ARCHIVE_NAME = "_cache-archive.md"
BACKUP_DIR = ".backup"
DEFAULT_KEEP = 2

# The vault is two levels above this script (<vault>/0 - System/scripts/trim_cache.py).
# VAULT_ROOT overrides it, which is what the tests use.
VAULT = Path(os.environ.get("VAULT_ROOT") or Path(__file__).resolve().parents[2])

ARCHIVE_HEADER = "---\ntags:\n  - cache\n  - archive\n---\n\n# Cache Archive\n\n"


def backup(paths):
    dest = VAULT / SYSTEM_DIR / BACKUP_DIR / datetime.now().strftime("cache-%Y%m%d-%H%M%S")
    dest.mkdir(parents=True, exist_ok=True)
    for p in paths:
        if p.exists():
            shutil.copy2(p, dest / p.name)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    keep = int(argv[0]) if argv else DEFAULT_KEEP
    cache = VAULT / SYSTEM_DIR / CACHE_NAME
    archive = VAULT / SYSTEM_DIR / ARCHIVE_NAME

    if not cache.exists():
        print(f"No {CACHE_NAME}.")
        return 0
    text = cache.read_text(encoding="utf-8")
    header, *blocks = re.split(r"(?m)^(?=## Session)", text)
    if len(blocks) <= keep:
        print(f"Only {len(blocks)} sessions — nothing to archive.")
        return 0

    backup([cache, archive])
    cache.write_text(header + "".join(blocks[:keep]), encoding="utf-8")
    prev = archive.read_text(encoding="utf-8") if archive.exists() else ARCHIVE_HEADER
    archive.write_text(prev + "".join(blocks[keep:]), encoding="utf-8")

    print(f"Kept {keep} sessions in {CACHE_NAME}, archived {len(blocks) - keep}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
