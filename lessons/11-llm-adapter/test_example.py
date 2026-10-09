"""Tests for lesson 11 worked examples."""

import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from example import generate, load_config, make_generator


class TestHandler(BaseHTTPRequestHandler):
    received_auth = ""
    received_payload: dict[str, object] = {}

    def do_POST(self) -> None:
        if self.path == "/error":
            self.send_response(500)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8")
        TestHandler.received_auth = self.headers.get("Authorization", "")
        TestHandler.received_payload = json.loads(body)

        if self.path == "/broken":
            response = b"{broken"
        else:
            response = json.dumps({"text": "mock answer"}).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, format: str, *args: object) -> None:
        return


class ExampleTests(unittest.TestCase):
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

    def config(self, suffix: str = "/generate") -> dict[str, str]:
        return {
            "endpoint": f"{self.base_url}{suffix}",
            "api_key": "test-key",
            "model": "test-model",
        }

    def test_load_config(self) -> None:
        config = load_config(
            {
                "LLM_ENDPOINT": f"{self.base_url}/generate/",
                "LLM_API_KEY": "secret",
                "LLM_MODEL": "model",
            }
        )
        self.assertEqual(config["endpoint"], f"{self.base_url}/generate")
        self.assertEqual(config["model"], "model")

    def test_load_config_rejects_missing_key(self) -> None:
        with self.assertRaises(ValueError):
            load_config({"LLM_ENDPOINT": self.base_url, "LLM_MODEL": "model"})

    def test_generate(self) -> None:
        answer = generate("hello", self.config())
        self.assertEqual(answer, "mock answer")
        self.assertEqual(TestHandler.received_auth, "Bearer test-key")
        self.assertEqual(TestHandler.received_payload["model"], "test-model")
        self.assertEqual(TestHandler.received_payload["prompt"], "hello")

    def test_generate_rejects_broken_json(self) -> None:
        with self.assertRaises(ValueError):
            generate("hello", self.config("/broken"))

    def test_generate_rejects_http_error(self) -> None:
        with self.assertRaises(RuntimeError):
            generate("hello", self.config("/error"))

    def test_make_generator(self) -> None:
        generator = make_generator(self.config())
        self.assertEqual(generator("hello"), "mock answer")


if __name__ == "__main__":
    unittest.main()
