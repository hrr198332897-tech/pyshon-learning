"""Progress checks for the JSON API client exercise."""

import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from api_client import extract_records, fetch_json, summarize_records


class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/ok":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps(
                    {
                        "records": [
                            {"label": " python ", "minutes": 60},
                            {"label": "ai", "minutes": 30},
                        ]
                    }
                ).encode("utf-8")
            )
            return

        if self.path == "/broken":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"{broken")
            return

        self.send_response(500)
        self.end_headers()

    def log_message(self, format: str, *args: object) -> None:
        return


def call_or_skip(test: unittest.TestCase, function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except NotImplementedError as exc:
        test.skipTest(str(exc))


class ApiClientTests(unittest.TestCase):
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

    def test_fetch_and_extract(self) -> None:
        payload = call_or_skip(self, fetch_json, f"{self.base_url}/ok")
        records = call_or_skip(self, extract_records, payload)
        self.assertEqual(records[0], {"label": "python", "minutes": 60})

    def test_fetch_rejects_broken_json(self) -> None:
        try:
            fetch_json(f"{self.base_url}/broken")
        except NotImplementedError as exc:
            self.skipTest(str(exc))
        except ValueError:
            return
        self.fail("非 JSON 响应应触发 ValueError")

    def test_fetch_rejects_http_error(self) -> None:
        try:
            fetch_json(f"{self.base_url}/error")
        except NotImplementedError as exc:
            self.skipTest(str(exc))
        except RuntimeError:
            return
        self.fail("HTTP 错误应触发 RuntimeError")

    def test_extract_rejects_bad_payload(self) -> None:
        try:
            extract_records({"records": "not a list"})
        except NotImplementedError as exc:
            self.skipTest(str(exc))
        except ValueError:
            return
        self.fail("错误 payload 应触发 ValueError")

    def test_summarize_records(self) -> None:
        records = [
            {"label": "python", "minutes": 60},
            {"label": "ai", "minutes": 30},
        ]
        result = call_or_skip(self, summarize_records, records)
        self.assertEqual(result, {"count": 2, "total_minutes": 90, "average_minutes": 45.0})


if __name__ == "__main__":
    unittest.main()
