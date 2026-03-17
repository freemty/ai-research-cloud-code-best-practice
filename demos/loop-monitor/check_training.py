"""
Training monitor — reads training.log and reports status.

Designed to be called by Claude Code's /loop command.
Detects: plateau (loss stagnant 3+ epochs), spike (loss jumps >50%),
and reports current best metrics.

Usage:
    python check_training.py                  # full report
    python check_training.py --last 5         # only last 5 epochs
    python check_training.py --alert-only     # only print if anomaly detected

Exit codes:
    0 = normal
    1 = anomaly detected (plateau or spike)
"""

import argparse
import csv
import sys
from pathlib import Path

LOG_FILE = Path(__file__).parent / "training.log"

PLATEAU_THRESHOLD = 0.02    # loss change < 2% over 3 epochs = plateau
SPIKE_THRESHOLD = 0.5       # loss increase > 50% = spike


def read_log() -> list[dict]:
    if not LOG_FILE.exists():
        return []
    with open(LOG_FILE) as f:
        return list(csv.DictReader(f))


def get_epoch_summary(rows: list[dict]) -> list[dict]:
    """Aggregate per-epoch: mean train_loss, mean val_loss."""
    epochs = {}
    for r in rows:
        ep = int(r["epoch"])
        if ep not in epochs:
            epochs[ep] = {"train": [], "val": []}
        epochs[ep]["train"].append(float(r["train_loss"]))
        epochs[ep]["val"].append(float(r["val_loss"]))

    return [
        {
            "epoch": ep,
            "train_loss": round(sum(d["train"]) / len(d["train"]), 4),
            "val_loss": round(sum(d["val"]) / len(d["val"]), 4),
        }
        for ep, d in sorted(epochs.items())
    ]


def detect_plateau(summaries: list[dict], window: int = 3) -> bool:
    if len(summaries) < window:
        return False
    recent = summaries[-window:]
    val_losses = [s["val_loss"] for s in recent]
    change = abs(val_losses[-1] - val_losses[0]) / max(val_losses[0], 1e-6)
    return change < PLATEAU_THRESHOLD


def detect_spike(summaries: list[dict]) -> bool:
    if len(summaries) < 2:
        return False
    prev = summaries[-2]["val_loss"]
    curr = summaries[-1]["val_loss"]
    increase = (curr - prev) / max(prev, 1e-6)
    return increase > SPIKE_THRESHOLD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--last", type=int, default=0)
    parser.add_argument("--alert-only", action="store_true")
    args = parser.parse_args()

    rows = read_log()
    if not rows:
        print("NO DATA — training.log is empty or missing")
        sys.exit(0)

    summaries = get_epoch_summary(rows)
    if args.last > 0:
        summaries = summaries[-args.last:]

    # Detect anomalies
    has_plateau = detect_plateau(summaries)
    has_spike = detect_spike(summaries)
    anomaly = has_plateau or has_spike

    if args.alert_only and not anomaly:
        sys.exit(0)

    # Header
    latest = summaries[-1]
    best = min(summaries, key=lambda s: s["val_loss"])
    total_rows = len(rows)

    print("=" * 50)
    print(f"  TRAINING MONITOR  |  {total_rows} entries logged")
    print("=" * 50)
    print(f"  Current:  epoch {latest['epoch']}  train={latest['train_loss']:.4f}  val={latest['val_loss']:.4f}")
    print(f"  Best:     epoch {best['epoch']}  val={best['val_loss']:.4f}")
    print()

    # Anomaly alerts
    if has_spike:
        print("  *** ALERT: LOSS SPIKE DETECTED ***")
        print(f"  val_loss jumped from {summaries[-2]['val_loss']:.4f} to {summaries[-1]['val_loss']:.4f}")
        print("  Possible causes: learning rate too high, data corruption, gradient explosion")
        print()

    if has_plateau:
        print("  *** ALERT: PLATEAU DETECTED ***")
        window = summaries[-3:]
        print(f"  val_loss stagnant over epochs {window[0]['epoch']}-{window[-1]['epoch']}: ", end="")
        print(" → ".join(f"{s['val_loss']:.4f}" for s in window))
        print("  Possible causes: learning rate too low, model capacity, local minimum")
        print()

    if not anomaly:
        print("  Status: NORMAL — training converging as expected")
        print()

    # Recent trend
    print("  Recent epochs:")
    for s in summaries[-5:]:
        bar_len = int(s["val_loss"] * 20)
        bar = "#" * min(bar_len, 40)
        flag = " !!!" if s == summaries[-1] and anomaly else ""
        print(f"    epoch {s['epoch']:2d}  val={s['val_loss']:.4f}  |{bar}{flag}")

    print("=" * 50)
    sys.exit(1 if anomaly else 0)


if __name__ == "__main__":
    main()
