"""Worked examples for lesson 6."""

from __future__ import annotations

import json
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def fetch_json(url: str, timeout: float = 5.0) -> Any:
    """Fetch and decode a JSON response."""
    request = Request(url, headers={"User-Agent": "pyshon-learning/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            content = response.read().decode("utf-8")
    except HTTPError as exc:
        raise RuntimeError(f"HTTP request failed with status {exc.code}") from exc
    except (URLError, TimeoutError) as exc:
        raise RuntimeError("network request failed") from exc

    try:
        return json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError("response is not valid JSON") from exc


def extract_records(payload: Any) -> list[dict[str, Any]]:
    """Validate and normalize API records."""
    if not isinstance(payload, dict):
        raise ValueError("payload must be a JSON object")

    records = payload.get("records")
    if not isinstance(records, list):
        raise ValueError("payload must contain a records list")

    cleaned: list[dict[str, Any]] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"record {index} must be an object")

        label = record.get("label")
        minutes = record.get("minutes")
        if not isinstance(label, str) or not label.strip():
            raise ValueError(f"record {index} has an invalid label")
        if not isinstance(minutes, int) or minutes < 0:
            raise ValueError(f"record {index} has invalid minutes")

        cleaned.append({"label": label.strip(), "minutes": minutes})
    return cleaned


def summarize_records(records: list[dict[str, Any]]) -> dict[str, int | float]:
    """Return aggregate statistics for normalized records."""
    if not records:
        return {"count": 0, "total_minutes": 0, "average_minutes": 0.0}

    total = sum(record["minutes"] for record in records)
    return {
        "count": len(records),
        "total_minutes": total,
        "average_minutes": round(total / len(records), 1),
    }


def main() -> None:
    payload = {
        "records": [
            {"label": "python", "minutes": 60},
            {"label": "ai", "minutes": 30},
        ]
    }
    records = extract_records(payload)
    print(summarize_records(records))


if __name__ == "__main__":
    main()
