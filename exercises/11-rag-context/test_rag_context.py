"""Progress checks for the RAG context exercise."""

import unittest

from rag_context import build_prompt, chunk_text, normalize_chunks


def call_or_skip(test: unittest.TestCase, function, *args):
    try:
        return function(*args)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


class RagContextTests(unittest.TestCase):
    def test_chunk_text_has_overlap(self) -> None:
        result = call_or_skip(self, chunk_text, "abcdefghij", 6, 2)
        self.assertEqual(result, ["abcdef", "efghij"])

    def test_chunk_text_empty_input(self) -> None:
        self.assertEqual(call_or_skip(self, chunk_text, "   "), [])

    def test_normalize_chunks(self) -> None:
        result = call_or_skip(self, normalize_chunks, ["  a  ", "", " b "])
        self.assertEqual(result, ["a", "b"])

    def test_build_prompt(self) -> None:
        prompt = call_or_skip(self, build_prompt, "问题", [" 第一段 ", "第二段"])
        self.assertIn("[1] 第一段", prompt)
        self.assertIn("[2] 第二段", prompt)
        self.assertIn("不知道", prompt)


if __name__ == "__main__":
    unittest.main()
