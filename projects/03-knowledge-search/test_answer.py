"""Tests for grounded prompts and answer assembly."""

import unittest
from pathlib import Path

try:
    import sklearn
except ImportError:
    sklearn = None

from knowledge_search.answer import answer_question, build_prompt, extractive_answer
from knowledge_search.documents import load_documents
from knowledge_search.index import build_index


PROJECT_DIR = Path(__file__).resolve().parent
NOTES_DIR = PROJECT_DIR / "examples" / "notes"


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class AnswerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.chunks = load_documents(NOTES_DIR)
        self.index = build_index(self.chunks)

    def test_extractive_answer_without_results(self) -> None:
        self.assertEqual(extractive_answer([]), "不知道：没有找到相关内容。")

    def test_build_prompt_contains_source(self) -> None:
        result = answer_question("RAG 是什么", self.chunks, self.index, top_k=1)
        prompt = build_prompt(
            "RAG 是什么",
            [
                {
                    "source": "rag.md",
                    "position": 1,
                    "text": "RAG 是检索增强生成。",
                    "score": 0.8,
                }
            ],
        )
        self.assertIn("[1] (rag.md #1)", prompt)
        self.assertIn("如果上下文不足", prompt)
        self.assertIn("rag.md", result["sources"][0]["source"])

    def test_answer_uses_generator_boundary(self) -> None:
        captured: list[str] = []

        def fake_generator(prompt: str) -> str:
            captured.append(prompt)
            return "模型回答 [1]"

        result = answer_question(
            "RAG 是什么",
            self.chunks,
            self.index,
            top_k=1,
            generator=fake_generator,
        )
        self.assertEqual(result["answer"], "模型回答 [1]")
        self.assertIn("上下文:", captured[0])

    def test_no_match_does_not_call_generator(self) -> None:
        called = False

        def fake_generator(prompt: str) -> str:
            nonlocal called
            called = True
            return "should not run"

        result = answer_question("量子纠缠实验", self.chunks, self.index, generator=fake_generator)
        self.assertEqual(result["answer"], "不知道：没有找到相关内容。")
        self.assertFalse(called)


if __name__ == "__main__":
    unittest.main()
