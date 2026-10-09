"""Tests for lesson 9 worked examples."""

import unittest

try:
    import sklearn
except ImportError:
    sklearn = None

from example import build_context, build_index, search_documents


DOCUMENTS = [
    "Python variables store values for later use.",
    "Python functions organize reusable logic.",
    "TF-IDF ranks documents by word importance.",
    "A database stores structured records.",
]


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class ExampleTests(unittest.TestCase):
    def test_build_index(self) -> None:
        vectorizer, matrix = build_index(DOCUMENTS)
        self.assertEqual(matrix.shape[0], 4)
        self.assertIn("python", vectorizer.vocabulary_)

    def test_search_documents(self) -> None:
        results = search_documents("Python functions", DOCUMENTS, top_k=2)
        self.assertEqual(results[0]["index"], 1)
        self.assertGreater(results[0]["score"], 0)
        self.assertEqual(len(results), 2)

    def test_search_rejects_empty_query(self) -> None:
        with self.assertRaises(ValueError):
            search_documents("", DOCUMENTS)

    def test_build_context(self) -> None:
        context = build_context("Python functions", DOCUMENTS, top_k=1)
        self.assertTrue(context.startswith("[1] Python functions"))

    def test_no_match_context(self) -> None:
        context = build_context("quantum zebra", DOCUMENTS)
        self.assertEqual(context, "没有找到相关内容。")


if __name__ == "__main__":
    unittest.main()
