"""Progress checks for the word statistics exercise."""

import unittest

from word_stats import build_summary, count_words, top_words


def call_or_skip(test: unittest.TestCase, function, *args):
    try:
        return function(*args)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


class WordStatsTests(unittest.TestCase):
    def test_count_words(self) -> None:
        result = call_or_skip(self, count_words, "Python python AI.")
        self.assertEqual(result, {"python": 2, "ai": 1})

    def test_top_words_breaks_ties_by_word(self) -> None:
        vocabulary = {"python": 2, "ai": 2, "github": 1}
        result = call_or_skip(self, top_words, vocabulary)
        self.assertEqual(result, [("ai", 2), ("python", 2), ("github", 1)])

    def test_build_summary(self) -> None:
        result = call_or_skip(self, build_summary, "Python AI Python")
        self.assertEqual(result, "共 2 个词，最常出现的是 python（2 次）。")

    def test_empty_summary(self) -> None:
        result = call_or_skip(self, build_summary, "")
        self.assertEqual(result, "文本中没有可统计的词。")


if __name__ == "__main__":
    unittest.main()
