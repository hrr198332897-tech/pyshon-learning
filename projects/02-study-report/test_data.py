"""Tests for study_report data loading."""

import tempfile
import unittest
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    pd = None

from study_report.data import load_sessions


PROJECT_DIR = Path(__file__).resolve().parent
SAMPLE_PATH = PROJECT_DIR / "examples" / "sessions.csv"


@unittest.skipIf(pd is None, "pandas is not installed")
class DataTests(unittest.TestCase):
    def test_load_sample(self) -> None:
        frame = load_sessions(SAMPLE_PATH)
        self.assertEqual(len(frame), 5)
        self.assertEqual(frame["minutes"].dtype, "int64")
        self.assertEqual(frame["label"].tolist()[0], "python")

    def test_missing_file(self) -> None:
        with self.assertRaises(FileNotFoundError):
            load_sessions(PROJECT_DIR / "missing.csv")

    def test_missing_column(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text("date,minutes\n2026-10-09,60\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_sessions(path)

    def test_invalid_minutes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text(
                "date,minutes,label,note\n2026-10-09,abc,python,test\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                load_sessions(path)

    def test_negative_minutes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text(
                "date,minutes,label,note\n2026-10-09,-1,python,test\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                load_sessions(path)


if __name__ == "__main__":
    unittest.main()
