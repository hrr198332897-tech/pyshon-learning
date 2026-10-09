"""Practice reproducible model training and evaluation."""

from __future__ import annotations

from typing import Any


def make_dataset(random_state: int = 42) -> tuple[Any, Any]:
    """Create a deterministic binary classification dataset."""
    raise NotImplementedError("请完成 make_dataset 函数")


def split_dataset(
    features: Any,
    labels: Any,
    test_size: float = 0.25,
    random_state: int = 42,
) -> tuple[Any, Any, Any, Any]:
    """Split features and labels into train and test sets."""
    raise NotImplementedError("请完成 split_dataset 函数")


def build_model() -> Any:
    """Build a reproducible preprocessing and classification pipeline."""
    raise NotImplementedError("请完成 build_model 函数")


def train_and_evaluate(
    train_features: Any,
    train_labels: Any,
    test_features: Any,
    test_labels: Any,
) -> dict[str, Any]:
    """Train a model and return predictions and accuracy."""
    raise NotImplementedError("请完成 train_and_evaluate 函数")


def main() -> None:
    print("请先安装 scikit-learn，再用测试驱动完成本练习。")


if __name__ == "__main__":
    main()
