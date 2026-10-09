"""Integration tests for the knowledge search CLI."""

import os
import subprocess
import sys
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

try:
    import sklearn
except ImportError:
    sklearn = None


PROJECT_DIR = Path(__file__).resolve().parent


class TestHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        self.rfile.read(length)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"text": "Mock model answer [1]"}')

    def log_message(self, format: str, *args: object) -> None:
        return


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class CliTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), TestHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

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
        self.assertIn("Sources:", result.stdout)

    def test_cli_uses_llm_generator(self) -> None:
        env = {
            **os.environ,
            "PYTHONUTF8": "1",
            "LLM_ENDPOINT": f"{self.base_url}/generate",
            "LLM_API_KEY": "test-key",
            "LLM_MODEL": "test-model",
        }
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "knowledge_search",
                "--query",
                "RAG 是什么",
                "--use-llm",
            ],
            cwd=PROJECT_DIR,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Mock model answer [1]", result.stdout)
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
