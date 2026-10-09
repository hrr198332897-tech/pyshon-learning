"""Tests for lesson 10 worked examples."""

import unittest

from example import build_prompt, chunk_text, normalize_chunks


class ExampleTests(unittest.TestCase):
    def test_chunk_text_has_overlap(self) -> None:
        text = "abcdefghij"
        self.assertEqual(chunk_text(text, max_chars=6, overlap=2), ["abcdef", "efghij"])

    def test_chunk_text_empty_input(self) -> None:
        self.assertEqual(chunk_text("   "), [])

    def test_chunk_text_rejects_invalid_overlap(self) -> None:
        with self.assertRaises(ValueError):
            chunk_text("abcdef", max_chars=5, overlap=5)

    def test_normalize_chunks(self) -> None:
        self.assertEqual(normalize_chunks(["  a  ", "", " b "]), ["a", "b"])

    def test_build_prompt(self) -> None:
        prompt = build_prompt("问题", [" 第一段 ", "第二段"])
        self.assertIn("[1] 第一段", prompt)
        self.assertIn("[2] 第二段", prompt)
        self.assertIn("如果上下文不足", prompt)
        self.assertIn("回答后列出使用的来源编号", prompt)

    def test_build_prompt_rejects_missing_context(self) -> None:
        with self.assertRaises(ValueError):
            build_prompt("问题", [])


if __name__ == "__main__":
    unittest.main()
