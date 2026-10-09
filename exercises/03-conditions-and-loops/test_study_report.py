"""Progress checks for the weekly study report exercise."""

import unittest

from study_report import (
    build_report,
    classify_study_time,
    count_active_days,
    first_goal_day,
)


def call_or_skip(test: unittest.TestCase, function, *args):
    try:
        return function(*args)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


class StudyReportTests(unittest.TestCase):
    def test_classify_study_time(self) -> None:
        result = call_or_skip(self, classify_study_time, 60)
        self.assertEqual(result, "投入充足")

    def test_classify_rejects_negative_minutes(self) -> None:
        try:
            classify_study_time(-1)
        except NotImplementedError as exc:
            self.skipTest(str(exc))
        except ValueError:
            return
        self.fail("负数分钟数应触发 ValueError")

    def test_count_active_days(self) -> None:
        result = call_or_skip(self, count_active_days, [0, 20, 30, 0, 60])
        self.assertEqual(result, 3)

    def test_first_goal_day(self) -> None:
        result = call_or_skip(self, first_goal_day, [20, 65, 90])
        self.assertEqual(result, 2)
        no_result = call_or_skip(self, first_goal_day, [20, 30])
        self.assertIsNone(no_result)

    def test_build_report(self) -> None:
        result = call_or_skip(self, build_report, [20, 65, 0, 90, 30, 130, 45])
        self.assertEqual(result, "本周有 6 天完成学习，首次达标日是第 2 天。")

    def test_build_report_without_goal_day(self) -> None:
        result = call_or_skip(self, build_report, [20, 30, 0])
        self.assertEqual(result, "本周没有达到目标的学习日。")


if __name__ == "__main__":
    unittest.main()
