"""Tests for train.py — used by PostToolUse hook to auto-verify."""

from train import compute_summary, get_best_epoch


MOCK_RESULTS = [
    {"epoch": "1", "train_loss": "2.3", "val_loss": "2.3", "accuracy": "0.11", "lr": "0.001"},
    {"epoch": "2", "train_loss": "1.2", "val_loss": "1.3", "accuracy": "0.58", "lr": "0.001"},
    {"epoch": "3", "train_loss": "0.6", "val_loss": "0.7", "accuracy": "0.78", "lr": "0.0005"},
]


def test_get_best_epoch():
    best = get_best_epoch(MOCK_RESULTS)
    assert best["epoch"] == "3"
    assert float(best["val_loss"]) == 0.7


def test_compute_summary():
    summary = compute_summary(MOCK_RESULTS)
    assert summary["best_epoch"] == 3
    assert summary["best_val_loss"] == 0.7
    assert summary["final_accuracy"] == 0.78
    assert summary["total_epochs"] == 3


def test_summary_keys():
    summary = compute_summary(MOCK_RESULTS)
    expected_keys = {"best_epoch", "best_val_loss", "final_accuracy", "total_epochs"}
    assert set(summary.keys()) == expected_keys
