#!/usr/bin/env python3
"""Tests for trim_cache.py against a throwaway vault."""
import importlib, io, os, sys, tempfile, unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

HEADER = "---\ntags:\n  - cache\n---\n\n# Session Cache\n\n"


def session(n):
    return f"## Session {n}\n- did thing {n}\n\n"


class TrimCacheTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name)
        (self.vault / "0 - System").mkdir()
        os.environ["VAULT_ROOT"] = str(self.vault)
        import trim_cache
        self.tc = importlib.reload(trim_cache)
        self.cache = self.vault / "0 - System" / "_cache.md"
        self.archive = self.vault / "0 - System" / "_cache-archive.md"

    def tearDown(self):
        os.environ.pop("VAULT_ROOT", None)
        self.tmp.cleanup()

    def run_trim(self, *args):
        with redirect_stdout(io.StringIO()):
            return self.tc.main(list(args))

    def test_keeps_newest_and_archives_the_rest(self):
        self.cache.write_text(HEADER + session(4) + session(3) + session(2) + session(1), encoding="utf-8")
        self.run_trim()
        self.assertEqual(self.cache.read_text(encoding="utf-8"), HEADER + session(4) + session(3))
        archived = self.archive.read_text(encoding="utf-8")
        self.assertIn(session(2) + session(1), archived)
        self.assertTrue(archived.startswith("---\n"))

    def test_appends_to_an_existing_archive(self):
        self.archive.write_text("# Cache Archive\n\n" + session(1), encoding="utf-8")
        self.cache.write_text(HEADER + session(3) + session(2), encoding="utf-8")
        self.run_trim("1")
        self.assertEqual(self.cache.read_text(encoding="utf-8"), HEADER + session(3))
        self.assertEqual(self.archive.read_text(encoding="utf-8"), "# Cache Archive\n\n" + session(1) + session(2))

    def test_nothing_to_do_writes_nothing(self):
        self.cache.write_text(HEADER + session(1), encoding="utf-8")
        self.run_trim()
        self.assertFalse(self.archive.exists())
        self.assertFalse((self.vault / "0 - System" / ".backup").exists())

    def test_backs_up_before_writing(self):
        original = HEADER + session(3) + session(2) + session(1)
        self.cache.write_text(original, encoding="utf-8")
        self.run_trim()
        backups = list((self.vault / "0 - System" / ".backup").glob("cache-*/_cache.md"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(encoding="utf-8"), original)

    def test_missing_cache_is_not_an_error(self):
        self.assertEqual(self.run_trim(), 0)


if __name__ == "__main__":
    unittest.main()
