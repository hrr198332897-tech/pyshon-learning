"""Worked examples for lesson 8."""

from __future__ import annotations

from typing import Any

try:
    from sklearn.datasets import make_classification
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
except ImportError:
    make_classification = None
    LogisticRegression = None
    train_test_split = None
    Pipeline = None
    StandardScaler = None


def require_sklearn() -> None:
    """Raise a clear error when scikit-learn is unavailable."""
    if make_classification is None:
        raise RuntimeError("scikit-learn is required for this lesson")


def make_dataset(random_state: int = 42) -> tuple[Any, Any]:
    """Create a deterministic binary classification dataset."""
    require_sklearn()
    return make_classification(
        n_samples=120,
        n_features=4,
        n_informative=3,
        n_redundant=0,
        class_sep=1.6,
        flip_y=0.02,
        random_state=random_state,
    )


def split_dataset(
    features: Any,
    labels: Any,
    test_size: float = 0.25,
    random_state: int = 42,
) -> tuple[Any, Any, Any, Any]:
    """Split features and labels into train and test sets."""
    require_sklearn()
    return train_test_split(
        features,
        labels,
        test_size=test_size,
        random_state=random_state,
        stratify=labels,
    )


def build_model() -> Any:
    """Build a reproducible preprocessing and classification pipeline."""
    require_sklearn()
    return Pipeline(
        [
            ("scale", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )


def train_and_evaluate(
    train_features: Any,
    train_labels: Any,
    test_features: Any,
    test_labels: Any,
) -> dict[str, Any]:
    """Train a model and return predictions and accuracy."""
    model = build_model()
    model.fit(train_features, train_labels)
    predictions = model.predict(test_features)
    return {
        "accuracy": round(float(model.score(test_features, test_labels)), 3),
        "predictions": [int(value) for value in predictions],
    }


def main() -> None:
    features, labels = make_dataset()
    train_x, test_x, train_y, test_y = split_dataset(features, labels)
    result = train_and_evaluate(train_x, train_y, test_x, test_y)
    print(f"Accuracy: {result['accuracy']}")


if __name__ == "__main__":
    main()
