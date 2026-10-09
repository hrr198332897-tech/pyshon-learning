"""Progress checks for the model service adapter exercise."""

import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from llm_adapter import generate, load_config, make_generator


class TestHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        if self.path == "/error":
            self.send_response(500)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", "0"))
        self.rfile.read(length)
        response = b"{broken" if self.path == "/broken" else json.dumps({"text": "mock answer"}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, format: str, *args: object) -> None:
        return


def call_or_skip(test: unittest.TestCase, function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


class LlmAdapterTests(unittest.TestCase):
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
        env = {
            "LLM_ENDPOINT": f"{self.base_url}/generate/",
            "LLM_API_KEY": "secret",
            "LLM_MODEL": "model",
        }
        config = call_or_skip(self, load_config, env)
        self.assertEqual(config["endpoint"], f"{self.base_url}/generate")

    def test_generate(self) -> None:
        answer = call_or_skip(self, generate, "hello", self.config())
        self.assertEqual(answer, "mock answer")

    def test_generate_rejects_http_error(self) -> None:
        try:
            generate("hello", self.config("/error"))
        except NotImplementedError as exc:
            self.skipTest(str(exc))
        except RuntimeError:
            return
        self.fail("HTTP 错误应转换为 RuntimeError")

    def test_make_generator(self) -> None:
        generator = call_or_skip(self, make_generator, self.config())
        self.assertEqual(generator("hello"), "mock answer")


if __name__ == "__main__":
    unittest.main()
