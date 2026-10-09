"""Tests for lesson 1 worked examples."""

import unittest

from example import build_summary, greet, minutes_to_hours


class ExampleTests(unittest.TestCase):
    def test_greet(self) -> None:
        self.assertEqual(greet("小明"), "你好，小明！")

    def test_minutes_to_hours(self) -> None:
        self.assertEqual(minutes_to_hours(90), 1.5)

    def test_build_summary(self) -> None:
        result = build_summary("小明", 150)
        self.assertEqual(result, "你好，小明！ 你这周计划学习 150 分钟，也就是 2.5 小时。")


if __name__ == "__main__":
    unittest.main()

