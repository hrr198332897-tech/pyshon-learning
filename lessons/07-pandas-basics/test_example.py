"""Tests for lesson 7 worked examples."""

import unittest

try:
    import pandas as pd
except ImportError:
    pd = None

from example import build_dataframe, filter_minimum, minutes_by_label, summarize


@unittest.skipIf(pd is None, "pandas is not installed")
class ExampleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = [
            {"label": "python", "minutes": 60},
            {"label": "ai", "minutes": 30},
            {"label": "python", "minutes": 45},
        ]

    def test_build_dataframe(self) -> None:
        frame = build_dataframe(self.rows)
        self.assertEqual(frame["minutes"].dtype, "int64")
        self.assertEqual(len(frame), 3)

    def test_filter_minimum(self) -> None:
        frame = build_dataframe(self.rows)
        filtered = filter_minimum(frame, 45)
        self.assertEqual(filtered["minutes"].tolist(), [60, 45])
        self.assertEqual(len(frame), 3)

    def test_minutes_by_label(self) -> None:
        frame = build_dataframe(self.rows)
        self.assertEqual(
            minutes_by_label(frame),
            [{"label": "ai", "minutes": 30}, {"label": "python", "minutes": 105}],
        )

    def test_summarize(self) -> None:
        frame = build_dataframe(self.rows)
        self.assertEqual(
            summarize(frame),
            {"sessions": 3, "total_minutes": 135, "average_minutes": 45.0},
        )

    def test_empty_summary(self) -> None:
        frame = build_dataframe([])
        self.assertEqual(
            summarize(frame),
            {"sessions": 0, "total_minutes": 0, "average_minutes": 0.0},
        )


if __name__ == "__main__":
    unittest.main()
