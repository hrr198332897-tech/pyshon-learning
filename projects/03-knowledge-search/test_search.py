"""Tests for TF-IDF indexing and search."""

import unittest
from pathlib import Path

try:
    import sklearn
except ImportError:
    sklearn = None

from knowledge_search.documents import load_documents
from knowledge_search.index import build_index, search


PROJECT_DIR = Path(__file__).resolve().parent
NOTES_DIR = PROJECT_DIR / "examples" / "notes"


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class SearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.chunks = load_documents(NOTES_DIR)
        self.index = build_index(self.chunks)

    def test_search_rag(self) -> None:
        results = search("RAG 是什么", self.chunks, self.index, top_k=1)
        self.assertEqual(results[0]["source"], "rag.md")
        self.assertGreater(results[0]["score"], 0)

    def test_search_no_match_returns_empty(self) -> None:
        self.assertEqual(search("量子纠缠实验", self.chunks, self.index), [])


if __name__ == "__main__":
    unittest.main()
