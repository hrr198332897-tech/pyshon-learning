"""Tests for lesson 5 worked examples."""

import csv
import tempfile
import unittest
from pathlib import Path

from example import clean_rows, load_rows, summarize, write_cleaned


class ExampleTests(unittest.TestCase):
    def test_load_clean_and_summarize(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sessions.csv"
            path.write_text(
                "date,minutes,note\n"
                "2026-10-08,45,lesson 1\n"
                "2026-10-09,60,project\n",
                encoding="utf-8",
            )

            rows = load_rows(path)
            cleaned = clean_rows(rows)

            self.assertEqual(cleaned[0]["minutes"], 45)
            self.assertEqual(
                summarize(cleaned),
                {"sessions": 2, "total_minutes": 105, "average_minutes": 52.5},
            )

    def test_clean_rejects_invalid_minutes(self) -> None:
        with self.assertRaises(ValueError):
            clean_rows([{"date": "2026-10-09", "minutes": "abc", "note": ""}])

    def test_clean_rejects_negative_minutes(self) -> None:
        with self.assertRaises(ValueError):
            clean_rows([{"date": "2026-10-09", "minutes": "-1", "note": ""}])

    def test_clean_rejects_empty_date(self) -> None:
        with self.assertRaises(ValueError):
            clean_rows([{"date": "", "minutes": "60", "note": ""}])

    def test_write_cleaned(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cleaned.csv"
            rows = [{"date": "2026-10-09", "minutes": 60, "note": "lesson 5"}]

            write_cleaned(path, rows)

            with path.open("r", encoding="utf-8", newline="") as file:
                loaded = list(csv.DictReader(file))
            self.assertEqual(loaded, [{"date": "2026-10-09", "minutes": "60", "note": "lesson 5"}])

    def test_empty_summary(self) -> None:
        self.assertEqual(
            summarize([]),
            {"sessions": 0, "total_minutes": 0, "average_minutes": 0.0},
        )


if __name__ == "__main__":
    unittest.main()
