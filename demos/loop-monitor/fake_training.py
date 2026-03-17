"""
Fake training script that simulates realistic training dynamics.

Writes one log line every 3 seconds to training.log.
Simulates: normal convergence → plateau → sudden spike (epoch 15+).

Usage:
    python fake_training.py              # normal run
    python fake_training.py --spike      # inject a loss spike at epoch 15
    python fake_training.py --plateau    # inject plateau at epoch 8
    python fake_training.py --both       # plateau then spike
"""

import argparse
import csv
import math
import random
import sys
import time
from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).parent / "training.log"
INTERVAL = 3  # seconds between log entries


def normal_loss(epoch: int, step: int) -> tuple[float, float]:
    """Smooth convergence curve with slight noise."""
    t = epoch + step / 100
    base = 2.5 * math.exp(-0.15 * t) + 0.3
    noise = random.gauss(0, 0.02)
    train_loss = max(0.01, base + noise)
    val_loss = max(0.01, base + 0.05 + abs(random.gauss(0, 0.03)))
    return round(train_loss, 4), round(val_loss, 4)


def plateau_loss(epoch: int, step: int) -> tuple[float, float]:
    """Loss stops decreasing — stuck at ~0.8."""
    t = epoch + step / 100
    if t < 7:
        return normal_loss(epoch, step)
    base = 0.78 + random.gauss(0, 0.015)
    val = 0.82 + random.gauss(0, 0.02)
    return round(max(0.01, base), 4), round(max(0.01, val), 4)


def spike_loss(epoch: int, step: int) -> tuple[float, float]:
    """Normal convergence then sudden spike at epoch 15."""
    t = epoch + step / 100
    if t < 14.5:
        return normal_loss(epoch, step)
    # Spike: loss jumps 3x
    train, val = normal_loss(epoch, step)
    spike_factor = 2.5 + random.gauss(0, 0.3)
    return round(train * spike_factor, 4), round(val * spike_factor, 4)


def both_loss(epoch: int, step: int) -> tuple[float, float]:
    """Plateau at epoch 8, then spike at epoch 15."""
    t = epoch + step / 100
    if t < 7:
        return normal_loss(epoch, step)
    if t < 14.5:
        return plateau_loss(epoch, step)
    train, val = plateau_loss(epoch, step)
    spike_factor = 2.0 + random.gauss(0, 0.2)
    return round(train * spike_factor, 4), round(val * spike_factor, 4)


def get_lr(epoch: int, total_epochs: int = 20) -> float:
    """Cosine learning rate schedule."""
    return round(0.001 * 0.5 * (1 + math.cos(math.pi * epoch / total_epochs)), 6)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spike", action="store_true")
    parser.add_argument("--plateau", action="store_true")
    parser.add_argument("--both", action="store_true")
    args = parser.parse_args()

    if args.both:
        loss_fn = both_loss
        mode = "plateau+spike"
    elif args.spike:
        loss_fn = spike_loss
        mode = "spike"
    elif args.plateau:
        loss_fn = plateau_loss
        mode = "plateau"
    else:
        loss_fn = normal_loss
        mode = "normal"

    print(f"Starting fake training (mode: {mode})")
    print(f"Logging to: {LOG_FILE}")
    print(f"Interval: {INTERVAL}s per step")
    print("Press Ctrl+C to stop")
    print()

    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["epoch", "step", "train_loss", "val_loss", "lr", "timestamp"])
        f.flush()

        total_epochs = 20
        steps_per_epoch = 10

        for epoch in range(1, total_epochs + 1):
            lr = get_lr(epoch, total_epochs)
            for step in range(1, steps_per_epoch + 1):
                train_loss, val_loss = loss_fn(epoch, step)

                row = [
                    epoch,
                    step,
                    train_loss,
                    val_loss,
                    lr,
                    datetime.now().strftime("%H:%M:%S"),
                ]
                writer.writerow(row)
                f.flush()

                status = f"  epoch {epoch:2d}/{total_epochs} step {step:2d}/{steps_per_epoch}  train_loss={train_loss:.4f}  val_loss={val_loss:.4f}  lr={lr}"
                sys.stdout.write(f"\r{status}")
                sys.stdout.flush()

                time.sleep(INTERVAL)

            print()  # newline after each epoch

    print("\nTraining complete.")


if __name__ == "__main__":
    main()
