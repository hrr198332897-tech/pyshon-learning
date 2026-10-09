"""Tests for local document loading and chunking."""

import unittest
from pathlib import Path

from knowledge_search.documents import chunk_text, load_documents


PROJECT_DIR = Path(__file__).resolve().parent
NOTES_DIR = PROJECT_DIR / "examples" / "notes"


class DocumentTests(unittest.TestCase):
    def test_chunk_text_has_overlap(self) -> None:
        self.assertEqual(chunk_text("abcdefghij", max_chars=6, overlap=2), ["abcdef", "efghij"])

    def test_load_documents(self) -> None:
        chunks = load_documents(NOTES_DIR)
        self.assertEqual(len(chunks), 3)
        sources = {chunk["source"] for chunk in chunks}
        self.assertEqual(sources, {"data.md", "python.md", "rag.md"})

    def test_missing_directory(self) -> None:
        with self.assertRaises(FileNotFoundError):
            load_documents(PROJECT_DIR / "missing")


if __name__ == "__main__":
    unittest.main()
