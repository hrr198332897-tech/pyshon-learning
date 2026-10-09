"""Tests for the optional remote model provider."""

import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from knowledge_search.provider import (
    generate_with_llm,
    load_llm_config,
    make_llm_generator,
)


class TestHandler(BaseHTTPRequestHandler):
    received_auth = ""
    received_payload: dict[str, object] = {}

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8")
        TestHandler.received_auth = self.headers.get("Authorization", "")
        TestHandler.received_payload = json.loads(body)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"text": "Remote answer [1]"}).encode("utf-8"))

    def log_message(self, format: str, *args: object) -> None:
        return


class ProviderTests(unittest.TestCase):
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

    def config(self) -> dict[str, str]:
        return {
            "endpoint": f"{self.base_url}/generate",
            "api_key": "test-key",
            "model": "test-model",
        }

    def test_load_config(self) -> None:
        config = load_llm_config(
            {
                "LLM_ENDPOINT": f"{self.base_url}/generate/",
                "LLM_API_KEY": "secret",
                "LLM_MODEL": "model",
            }
        )
        self.assertEqual(config["endpoint"], f"{self.base_url}/generate")

    def test_generate_with_llm(self) -> None:
        answer = generate_with_llm("prompt", self.config())
        self.assertEqual(answer, "Remote answer [1]")
        self.assertEqual(TestHandler.received_auth, "Bearer test-key")
        self.assertEqual(TestHandler.received_payload["model"], "test-model")

    def test_make_llm_generator(self) -> None:
        generator = make_llm_generator(self.config())
        self.assertEqual(generator("prompt"), "Remote answer [1]")


if __name__ == "__main__":
    unittest.main()
