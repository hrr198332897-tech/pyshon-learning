"""Tests for study_report summaries and Markdown output."""

import unittest
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    pd = None

from study_report.data import load_sessions
from study_report.report import build_markdown_report, minutes_by_label, summarize_sessions


PROJECT_DIR = Path(__file__).resolve().parent
SAMPLE_PATH = PROJECT_DIR / "examples" / "sessions.csv"


@unittest.skipIf(pd is None, "pandas is not installed")
class ReportTests(unittest.TestCase):
    def test_summarize_sessions(self) -> None:
        frame = load_sessions(SAMPLE_PATH)
        self.assertEqual(
            summarize_sessions(frame),
            {
                "sessions": 5,
                "total_minutes": 225,
                "average_minutes": 45.0,
                "active_days": 4,
                "top_label": "ai",
                "top_minutes": 120,
            },
        )

    def test_minutes_by_label(self) -> None:
        frame = load_sessions(SAMPLE_PATH)
        self.assertEqual(
            minutes_by_label(frame),
            [
                {"label": "ai", "minutes": 120},
                {"label": "python", "minutes": 105},
                {"label": "review", "minutes": 0},
            ],
        )

    def test_markdown_report(self) -> None:
        frame = load_sessions(SAMPLE_PATH)
        report = build_markdown_report(frame)
        self.assertIn("# Study Report", report)
        self.assertIn("- Total minutes: 225", report)
        self.assertIn("| ai | 120 |", report)


if __name__ == "__main__":
    unittest.main()
