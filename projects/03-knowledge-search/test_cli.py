"""Integration tests for the knowledge search CLI."""

import os
import subprocess
import sys
import unittest
from pathlib import Path

try:
    import sklearn
except ImportError:
    sklearn = None


PROJECT_DIR = Path(__file__).resolve().parent


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class CliTests(unittest.TestCase):
    def test_cli_answers_rag_question(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "knowledge_search",
                "--query",
                "RAG 是什么",
                "--show-context",
            ],
            cwd=PROJECT_DIR,
            env={**os.environ, "PYTHONUTF8": "1"},
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("RAG 是检索增强生成", result.stdout)
        self.assertIn("rag.md", result.stdout)

    def test_cli_reports_missing_documents(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "knowledge_search",
                "--documents",
                "missing",
                "--query",
                "test",
            ],
            cwd=PROJECT_DIR,
            env={**os.environ, "PYTHONUTF8": "1"},
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("Error:", result.stdout)


if __name__ == "__main__":
    unittest.main()
