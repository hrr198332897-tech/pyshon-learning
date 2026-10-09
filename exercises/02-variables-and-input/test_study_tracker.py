"""Progress checks for the study tracker exercise."""

import unittest

from study_tracker import build_summary, greet, minutes_to_hours


def call_or_skip(test: unittest.TestCase, function, *args):
    try:
        return function(*args)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


class StudyTrackerTests(unittest.TestCase):
    def test_greet(self) -> None:
        result = call_or_skip(self, greet, "小明")
        self.assertEqual(result, "你好，小明！")

    def test_minutes_to_hours(self) -> None:
        result = call_or_skip(self, minutes_to_hours, 150)
        self.assertEqual(result, 2.5)

    def test_build_summary(self) -> None:
        result = call_or_skip(self, build_summary, "小明", 150)
        self.assertEqual(result, "你好，小明！ 你这周计划学习 150 分钟，也就是 2.5 小时。")


if __name__ == "__main__":
    unittest.main()
