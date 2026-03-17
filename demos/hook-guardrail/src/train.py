"""Mock training script for hook demo."""

import csv
from pathlib import Path


def load_results(path: str = "data/experiment_results.csv") -> list[dict]:
    with open(path) as f:
        return list(csv.DictReader(f))


def get_best_epoch(results: list[dict]) -> dict:
    return min(results, key=lambda r: float(r["val_loss"]))


def compute_summary(results: list[dict]) -> dict:
    best = get_best_epoch(results)
    return {
        "best_epoch": int(best["epoch"]),
        "best_val_loss": float(best["val_loss"]),
        "final_accuracy": float(results[-1]["accuracy"]),
        "total_epochs": len(results),
    }


if __name__ == "__main__":
    results = load_results()
    summary = compute_summary(results)
    print(f"Best epoch: {summary['best_epoch']}")
    print(f"Best val_loss: {summary['best_val_loss']}")
    print(f"Final accuracy: {summary['final_accuracy']}")
