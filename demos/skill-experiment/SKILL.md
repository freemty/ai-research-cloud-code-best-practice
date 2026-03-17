---
name: experiment-setup
description: "Use when setting up a new ML experiment from a paper or idea. Creates standardized directory structure, config, training script skeleton, and evaluation template. Trigger on: 'set up experiment', 'new experiment', 'reproduce paper', '/experiment-setup'."
---

# Experiment Setup Skill

Automate the creation of a reproducible ML experiment workspace.

## Input

The user provides:
- **Paper/idea**: A paper URL, arxiv ID, or brief description
- **Dataset**: Dataset name or path
- **Optional**: Model architecture, hyperparameters, baseline to compare

## Steps

You MUST complete these in order:

### 1. Create Directory Structure

```
experiments/<experiment-name>/
├── config.yaml          # All hyperparameters (single source of truth)
├── train.py             # Training loop skeleton
├── evaluate.py          # Evaluation script
├── data/                # Symlink or download instructions
│   └── README.md        # Dataset description + download command
├── checkpoints/         # Model checkpoints (gitignored)
├── logs/                # Training logs (monitored by Loop)
│   └── .gitkeep
├── results/             # Final metrics, tables, figures
│   └── .gitkeep
└── README.md            # Experiment description + reproduction steps
```

### 2. Generate config.yaml

```yaml
experiment:
  name: "<experiment-name>"
  description: "<one-line from paper/idea>"
  paper_url: "<url if provided>"
  seed: 42
  created: "<YYYY-MM-DD>"

data:
  dataset: "<dataset-name>"
  train_split: "train"
  val_split: "val"
  test_split: "test"

model:
  architecture: "<from paper or user input>"
  # ... model-specific params

training:
  epochs: 100
  batch_size: 32
  learning_rate: 0.001
  optimizer: "adamw"
  scheduler: "cosine"
  warmup_steps: 500
  grad_clip: 1.0

evaluation:
  metrics: ["accuracy", "loss"]
  eval_every: 1  # epochs
  save_best: true
  early_stopping_patience: 10

logging:
  log_file: "logs/training.log"
  log_every: 100  # steps
  format: "epoch,step,train_loss,val_loss,metric,lr,timestamp"
```

### 3. Generate train.py Skeleton

Include:
- Config loading from config.yaml
- Deterministic seeding (torch, numpy, random)
- CSV log writer (append mode, matching logging.format)
- Checkpoint saving/loading
- Basic training loop with validation
- Placeholder for model/dataset (marked with TODO)

### 4. Generate evaluate.py Skeleton

Include:
- Load best checkpoint
- Run on test set
- Print metrics table
- Save results to results/metrics.json

### 5. Generate README.md

Include:
- Experiment description
- Paper reference (if applicable)
- Setup commands (pip install, data download)
- Run commands (train, evaluate)
- Expected results (if known from paper)

## Verification

After creating all files, run:
```bash
python -c "import yaml; yaml.safe_load(open('config.yaml'))"
```
to verify config.yaml is valid.

## Key Principle

**One config.yaml rules everything.** No hardcoded values in scripts.
Every hyperparameter lives in config.yaml and is loaded at runtime.
This makes experiments reproducible and comparable.
