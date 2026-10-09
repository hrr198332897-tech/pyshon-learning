"""Tests for lesson 4 worked examples."""

import json
import tempfile
import unittest
from pathlib import Path

from example import add_entry, load_entries, save_entries, total_minutes


class ExampleTests(unittest.TestCase):
    def test_save_and_load_entries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "study-log.json"
            entries = [{"day": 1, "minutes": 60}]

            save_entries(path, entries)
            loaded = load_entries(path)

            self.assertEqual(loaded, entries)
            self.assertTrue(path.read_text(encoding="utf-8").endswith("\n"))

    def test_missing_file_returns_empty_list(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.json"
            self.assertEqual(load_entries(path), [])

    def test_invalid_json_raises_value_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.json"
            path.write_text("{broken", encoding="utf-8")

            with self.assertRaises(ValueError):
                load_entries(path)

    def test_add_entry_returns_new_list(self) -> None:
        original = [{"day": 1, "minutes": 30}]
        updated = add_entry(original, day=2, minutes=60)

        self.assertEqual(original, [{"day": 1, "minutes": 30}])
        self.assertEqual(updated[-1], {"day": 2, "minutes": 60})

    def test_add_entry_validates_minutes(self) -> None:
        with self.assertRaises(ValueError):
            add_entry([], day=1, minutes=-1)

    def test_total_minutes(self) -> None:
        entries = [{"day": 1, "minutes": 30}, {"day": 2, "minutes": 60}]
        self.assertEqual(total_minutes(entries), 90)


if __name__ == "__main__":
    unittest.main()
