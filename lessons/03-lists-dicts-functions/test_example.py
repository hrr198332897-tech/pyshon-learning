"""Tests for lesson 3 worked examples."""

import unittest

from example import add_word, build_summary, count_words, top_words


class ExampleTests(unittest.TestCase):
    def test_count_words(self) -> None:
        result = count_words("Python python AI.")
        self.assertEqual(result, {"python": 2, "ai": 1})

    def test_add_word(self) -> None:
        vocabulary = {"python": 1}
        add_word(vocabulary, "python")
        self.assertEqual(vocabulary, {"python": 2})

    def test_top_words_breaks_ties_by_word(self) -> None:
        vocabulary = {"python": 2, "ai": 2, "github": 1}
        self.assertEqual(
            top_words(vocabulary),
            [("ai", 2), ("python", 2), ("github", 1)],
        )

    def test_build_summary(self) -> None:
        result = build_summary("Python AI Python")
        self.assertEqual(result, "共 2 个词，最常出现的是 python（2 次）。")

    def test_empty_summary(self) -> None:
        self.assertEqual(build_summary(""), "文本中没有可统计的词。")


if __name__ == "__main__":
    unittest.main()
