"""Practice a generic model service adapter."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from urllib.request import Request


def load_config(env: Mapping[str, str]) -> dict[str, str]:
    """Load and validate model service configuration."""
    raise NotImplementedError("请完成 load_config 函数")


def build_request(prompt: str, config: Mapping[str, str]) -> Request:
    """Build a JSON POST request for the configured model service."""
    raise NotImplementedError("请完成 build_request 函数")


def generate(
    prompt: str,
    config: Mapping[str, str],
    timeout: float = 5.0,
) -> str:
    """Call the model service and return its text field."""
    raise NotImplementedError("请完成 generate 函数")


def make_generator(config: Mapping[str, str]) -> Callable[[str], str]:
    """Create a prompt-to-answer function for knowledge search."""
    raise NotImplementedError("请完成 make_generator 函数")


def main() -> None:
    print("实现适配器后，使用本地模拟服务测试。")


if __name__ == "__main__":
    main()
