# Loop Demo: Training Monitor

A fake training script + monitor that demonstrates Claude Code's
`/loop` command for continuous, unattended experiment monitoring.

## Structure

```
demos/loop-monitor/
├── fake_training.py     # Simulates training with configurable anomalies
├── check_training.py    # Monitor script (called by /loop)
├── training.log         # Generated at runtime (gitignored)
└── README.md
```

## Setup

No setup needed — just run.

## Demo Script (3 acts)

### Act 1: Start Training (in a separate terminal/tmux pane)

```bash
# Option A: Normal convergence (boring but works)
python demos/loop-monitor/fake_training.py

# Option B: Loss plateau at epoch 8 (recommended for demo)
python demos/loop-monitor/fake_training.py --plateau

# Option C: Loss spike at epoch 15 (dramatic)
python demos/loop-monitor/fake_training.py --spike

# Option D: Plateau then spike (best for demo — shows both detections)
python demos/loop-monitor/fake_training.py --both
```

Each step takes 3 seconds. One epoch = 30 seconds. Full run = 10 minutes.

### Act 2: Start Loop Monitor (in Claude Code)

```
/loop 30s 检查 demos/loop-monitor/training.log 的训练状态。
运行 python demos/loop-monitor/check_training.py 并报告结果。
如果检测到异常（plateau 或 spike），分析可能的原因并建议修复方案。
```

What happens:
- Every 30 seconds, Claude runs check_training.py
- Shows current epoch, best val_loss, convergence trend
- When plateau detected: Claude suggests lowering LR or increasing capacity
- When spike detected: Claude warns about gradient explosion

### Act 3: "The Moment" — Anomaly Triggers Response

With `--both` mode, around epoch 8 (4 min into demo):

```
*** ALERT: PLATEAU DETECTED ***
val_loss stagnant over epochs 6-8: 0.8012 → 0.7934 → 0.7891
```

Claude automatically:
1. Diagnoses the plateau
2. Suggests: reduce LR, add regularization, or increase model capacity
3. Optionally: edits config.yaml to adjust hyperparameters

Then at epoch 15 (7.5 min):

```
*** ALERT: LOSS SPIKE DETECTED ***
val_loss jumped from 0.7823 to 1.9541
```

Claude automatically:
1. Warns about gradient explosion
2. Suggests: gradient clipping, LR warmup, or checkpoint rollback
3. Optionally: rolls back to best checkpoint

## Standalone Testing

```bash
# Start training in background
python demos/loop-monitor/fake_training.py --both &

# Wait ~30 seconds, then check
sleep 30 && python demos/loop-monitor/check_training.py

# Wait for plateau (~4 min)
sleep 240 && python demos/loop-monitor/check_training.py

# Check with alert-only mode (silent if normal)
python demos/loop-monitor/check_training.py --alert-only
```

## Key Teaching Points

| Aspect | Without Loop | With Loop |
|--------|-------------|-----------|
| Monitoring | Manual `tail -f`, stare at terminal | Automated, periodic, intelligent |
| Detection | Human eyeballs loss curves | Code-based threshold detection |
| Response | "I'll check after lunch" | Immediate alert + diagnosis |
| Context | Need to remember experiment state | Loop maintains awareness |
| Overnight | Hope nothing breaks | Loop watches while you sleep |

Core message: **Loop = autonomous monitoring.**
Your experiments run 24/7. Your attention doesn't. Loop bridges the gap.
