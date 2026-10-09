"""Tests for lesson 2 worked examples."""

import unittest

from example import classify_study_time, count_active_days, first_goal_day


class ExampleTests(unittest.TestCase):
    def test_classify_study_time(self) -> None:
        self.assertEqual(classify_study_time(20), "需要继续积累")
        self.assertEqual(classify_study_time(30), "达到基础目标")
        self.assertEqual(classify_study_time(60), "投入充足")
        self.assertEqual(classify_study_time(120), "高强度学习")

    def test_classify_rejects_negative_minutes(self) -> None:
        with self.assertRaises(ValueError):
            classify_study_time(-1)

    def test_count_active_days(self) -> None:
        self.assertEqual(count_active_days([0, 20, 30, 0, 60]), 3)

    def test_first_goal_day(self) -> None:
        self.assertEqual(first_goal_day([20, 65, 90]), 2)
        self.assertIsNone(first_goal_day([20, 30]))


if __name__ == "__main__":
    unittest.main()
