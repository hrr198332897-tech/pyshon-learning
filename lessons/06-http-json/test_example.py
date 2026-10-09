"""Tests for lesson 6 worked examples."""

import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from example import extract_records, fetch_json, summarize_records


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
                            {"label": "python", "minutes": 60},
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

    def test_fetch_and_extract(self) -> None:
        payload = fetch_json(f"{self.base_url}/ok")
        records = extract_records(payload)
        self.assertEqual(records[0], {"label": "python", "minutes": 60})
        self.assertEqual(
            summarize_records(records),
            {"count": 2, "total_minutes": 90, "average_minutes": 45.0},
        )

    def test_fetch_rejects_broken_json(self) -> None:
        with self.assertRaises(ValueError):
            fetch_json(f"{self.base_url}/broken")

    def test_fetch_rejects_http_error(self) -> None:
        with self.assertRaises(RuntimeError):
            fetch_json(f"{self.base_url}/error")

    def test_extract_rejects_bad_payload(self) -> None:
        with self.assertRaises(ValueError):
            extract_records({"records": "not a list"})

    def test_extract_rejects_bad_record(self) -> None:
        with self.assertRaises(ValueError):
            extract_records({"records": [{"label": "python", "minutes": -1}]})

    def test_empty_summary(self) -> None:
        self.assertEqual(
            summarize_records([]),
            {"count": 0, "total_minutes": 0, "average_minutes": 0.0},
        )


if __name__ == "__main__":
    unittest.main()
