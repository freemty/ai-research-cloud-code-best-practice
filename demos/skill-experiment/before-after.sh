#!/bin/bash
# Demonstrates the manual pain of setting up an experiment
# Run this to contrast with the skill's one-command approach

set -e

echo "================================================"
echo "  MANUAL EXPERIMENT SETUP (the old way)"
echo "================================================"
echo ""

sleep 1

STEPS=(
  "Step 1:  mkdir -p experiments/my-experiment"
  "Step 2:  mkdir -p experiments/my-experiment/{data,checkpoints,logs,results}"
  "Step 3:  touch experiments/my-experiment/config.yaml"
  "Step 4:  vim config.yaml  # write 30+ lines of hyperparameters..."
  "Step 5:  touch experiments/my-experiment/train.py"
  "Step 6:  vim train.py     # write argparse, config loading..."
  "Step 7:  # ...add seeding (torch.manual_seed, np.random.seed)..."
  "Step 8:  # ...add data loading with proper splits..."
  "Step 9:  # ...add training loop with gradient clipping..."
  "Step 10: # ...add validation loop..."
  "Step 11: # ...add checkpoint saving/loading..."
  "Step 12: # ...add CSV logger..."
  "Step 13: touch experiments/my-experiment/evaluate.py"
  "Step 14: vim evaluate.py  # write evaluation pipeline..."
  "Step 15: touch experiments/my-experiment/README.md"
  "Step 16: vim README.md    # document how to reproduce..."
  "Step 17: # ...add .gitignore for checkpoints..."
  "Step 18: # ...verify config.yaml is valid..."
  "Step 19: # ...realize you forgot warmup steps..."
  "Step 20: # ...fix config, fix train.py, re-verify..."
)

for step in "${STEPS[@]}"; do
  echo "  $step"
  sleep 0.3
done

echo ""
echo "  Total: ~20 steps, 15-30 minutes, error-prone"
echo ""
echo "================================================"
echo "  WITH SKILL: /experiment-setup"
echo "================================================"
echo ""
echo '  > /experiment-setup'
echo '  > Paper: arxiv 1706.03762'
echo '  > Dataset: WMT14 EN-DE'
echo ""
echo "  ...done in ~10 seconds. Every time. Perfectly."
echo ""
echo "================================================"
