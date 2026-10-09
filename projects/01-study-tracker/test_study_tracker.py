"""Tests for the study tracker reference project."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from study_tracker import add_entry, build_report, load_entries, save_entries


PROJECT_DIR = Path(__file__).resolve().parent
SCRIPT = PROJECT_DIR / "study_tracker.py"


class StudyTrackerTests(unittest.TestCase):
    def test_missing_file_returns_empty_list(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.json"
            self.assertEqual(load_entries(path), [])

    def test_save_and_load_entries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "study-tracker.json"
            entries = [{"date": "2026-10-09", "minutes": 60, "note": "lesson 1"}]

            save_entries(path, entries)
            loaded = load_entries(path)

            self.assertEqual(loaded, entries)
            self.assertTrue(path.read_text(encoding="utf-8").endswith("\n"))

    def test_add_entry_does_not_mutate_original(self) -> None:
        original = [{"date": "2026-10-08", "minutes": 30, "note": ""}]
        updated = add_entry(original, "2026-10-09", 60, "lesson 1")

        self.assertEqual(len(original), 1)
        self.assertEqual(updated[-1]["minutes"], 60)

    def test_add_entry_rejects_invalid_date(self) -> None:
        with self.assertRaises(ValueError):
            add_entry([], "10-09-2026", 60)

    def test_add_entry_rejects_negative_minutes(self) -> None:
        with self.assertRaises(ValueError):
            add_entry([], "2026-10-09", -1)

    def test_build_report(self) -> None:
        entries = [
            {"date": "2026-10-08", "minutes": 30, "note": ""},
            {"date": "2026-10-09", "minutes": 90, "note": ""},
        ]
        report = build_report(entries)

        self.assertEqual(report["sessions"], 2)
        self.assertEqual(report["total_minutes"], 120)
        self.assertEqual(report["average_minutes"], 60.0)
        self.assertEqual(report["best_minutes"], 90)

    def test_empty_report(self) -> None:
        self.assertEqual(
            build_report([]),
            {
                "sessions": 0,
                "total_minutes": 0,
                "average_minutes": 0.0,
                "best_minutes": 0,
            },
        )

    def test_cli_add_and_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "study-tracker.json"
            env = {**os.environ, "PYTHONUTF8": "1"}

            add_result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--data",
                    str(path),
                    "add",
                    "--date",
                    "2026-10-09",
                    "--minutes",
                    "45",
                    "--note",
                    "integration test",
                ],
                cwd=PROJECT_DIR,
                env=env,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )
            self.assertEqual(add_result.returncode, 0, add_result.stderr)
            self.assertIn("累计 45 分钟", add_result.stdout)

            report_result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--data",
                    str(path),
                    "report",
                ],
                cwd=PROJECT_DIR,
                env=env,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )
            self.assertEqual(report_result.returncode, 0, report_result.stderr)
            self.assertIn("学习次数: 1", report_result.stdout)
            self.assertIn("总学习: 45 分钟", report_result.stdout)

            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved[0]["note"], "integration test")

    def test_cli_rejects_invalid_data_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.json"
            path.write_text("{broken", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--data", str(path), "report"],
                cwd=PROJECT_DIR,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )

            self.assertEqual(result.returncode, 2)
            self.assertIn("数据错误", result.stdout)


if __name__ == "__main__":
    unittest.main()
