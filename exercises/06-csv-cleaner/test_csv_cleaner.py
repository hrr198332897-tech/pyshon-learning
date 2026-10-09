"""Progress checks for the CSV cleaner exercise."""

import csv
import tempfile
import unittest
from pathlib import Path

from csv_cleaner import clean_rows, load_rows, summarize, write_cleaned


def call_or_skip(test: unittest.TestCase, function, *args):
    try:
        return function(*args)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


class CsvCleanerTests(unittest.TestCase):
    def test_load_rows(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sessions.csv"
            path.write_text(
                "date,minutes,note\n2026-10-09,60,lesson 5\n",
                encoding="utf-8",
            )
            result = call_or_skip(self, load_rows, path)
            self.assertEqual(result, [{"date": "2026-10-09", "minutes": "60", "note": "lesson 5"}])

    def test_clean_rows(self) -> None:
        rows = [{"date": "2026-10-09", "minutes": "60", "note": " lesson 5 "}]
        result = call_or_skip(self, clean_rows, rows)
        self.assertEqual(result, [{"date": "2026-10-09", "minutes": 60, "note": "lesson 5"}])

    def test_clean_rejects_invalid_minutes(self) -> None:
        try:
            clean_rows([{"date": "2026-10-09", "minutes": "abc", "note": ""}])
        except NotImplementedError as exc:
            self.skipTest(str(exc))
        except ValueError:
            return
        self.fail("非数字 minutes 应触发 ValueError")

    def test_summarize(self) -> None:
        rows = [
            {"date": "2026-10-08", "minutes": 45, "note": ""},
            {"date": "2026-10-09", "minutes": 60, "note": ""},
        ]
        result = call_or_skip(self, summarize, rows)
        self.assertEqual(result, {"sessions": 2, "total_minutes": 105, "average_minutes": 52.5})

    def test_write_cleaned(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cleaned.csv"
            rows = [{"date": "2026-10-09", "minutes": 60, "note": "lesson 5"}]
            call_or_skip(self, write_cleaned, path, rows)

            with path.open("r", encoding="utf-8", newline="") as file:
                loaded = list(csv.DictReader(file))
            self.assertEqual(loaded, [{"date": "2026-10-09", "minutes": "60", "note": "lesson 5"}])


if __name__ == "__main__":
    unittest.main()
