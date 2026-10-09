"""Progress checks for the Pandas report exercise."""

import unittest

try:
    import pandas as pd
except ImportError:
    pd = None

from pandas_report import build_dataframe, filter_minimum, minutes_by_label, summarize


def call_or_skip(test: unittest.TestCase, function, *args):
    try:
        return function(*args)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


@unittest.skipIf(pd is None, "pandas is not installed")
class PandasReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = [
            {"label": "python", "minutes": 60},
            {"label": "ai", "minutes": 30},
            {"label": "python", "minutes": 45},
        ]

    def test_build_dataframe(self) -> None:
        frame = call_or_skip(self, build_dataframe, self.rows)
        self.assertEqual(frame["minutes"].dtype, "int64")

    def test_filter_minimum(self) -> None:
        frame = call_or_skip(self, build_dataframe, self.rows)
        filtered = call_or_skip(self, filter_minimum, frame, 45)
        self.assertEqual(filtered["minutes"].tolist(), [60, 45])

    def test_minutes_by_label(self) -> None:
        frame = call_or_skip(self, build_dataframe, self.rows)
        result = call_or_skip(self, minutes_by_label, frame)
        self.assertEqual(
            result,
            [{"label": "ai", "minutes": 30}, {"label": "python", "minutes": 105}],
        )

    def test_summarize(self) -> None:
        frame = call_or_skip(self, build_dataframe, self.rows)
        result = call_or_skip(self, summarize, frame)
        self.assertEqual(
            result,
            {"sessions": 3, "total_minutes": 135, "average_minutes": 45.0},
        )


if __name__ == "__main__":
    unittest.main()
