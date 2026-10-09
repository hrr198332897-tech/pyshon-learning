"""Worked examples for lesson 11."""

from __future__ import annotations

import json
from collections.abc import Callable, Mapping
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


REQUIRED_CONFIG_KEYS = ("LLM_ENDPOINT", "LLM_API_KEY", "LLM_MODEL")


def load_config(env: Mapping[str, str]) -> dict[str, str]:
    """Load and validate model service configuration."""
    missing = [key for key in REQUIRED_CONFIG_KEYS if not env.get(key, "").strip()]
    if missing:
        raise ValueError(f"missing configuration: {', '.join(missing)}")

    return {
        "endpoint": env["LLM_ENDPOINT"].strip().rstrip("/"),
        "api_key": env["LLM_API_KEY"].strip(),
        "model": env["LLM_MODEL"].strip(),
    }


def build_request(prompt: str, config: Mapping[str, str]) -> Request:
    """Build a JSON POST request for the configured model service."""
    if not prompt.strip():
        raise ValueError("prompt cannot be empty")

    body = json.dumps(
        {
            "model": config["model"],
            "prompt": prompt,
        }
    ).encode("utf-8")
    return Request(
        config["endpoint"],
        data=body,
        headers={
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json",
            "User-Agent": "pyshon-learning/1.0",
        },
        method="POST",
    )


def generate(
    prompt: str,
    config: Mapping[str, str],
    timeout: float = 5.0,
) -> str:
    """Call the model service and return its text field."""
    request = build_request(prompt, config)
    try:
        with urlopen(request, timeout=timeout) as response:
            content = response.read().decode("utf-8")
    except HTTPError as exc:
        raise RuntimeError(f"model service returned HTTP {exc.code}") from exc
    except (URLError, TimeoutError) as exc:
        raise RuntimeError("model service request failed") from exc

    try:
        payload: Any = json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError("model service response is not valid JSON") from exc

    if not isinstance(payload, dict) or not isinstance(payload.get("text"), str):
        raise ValueError("model service response must contain a text field")
    return payload["text"]


def make_generator(config: Mapping[str, str]) -> Callable[[str], str]:
    """Create a prompt-to-answer function for knowledge search."""
    def generator(prompt: str) -> str:
        return generate(prompt, config)

    return generator


def main() -> None:
    print("从环境变量加载配置后，用 make_generator() 接入知识搜索。")


if __name__ == "__main__":
    main()
