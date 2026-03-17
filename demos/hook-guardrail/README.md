# Hook Demo: Experiment Safety Guardrails

Three hooks that protect your experiment data, auto-verify code changes,
and warn about uncommitted results.

## Structure

```
demos/hook-guardrail/
├── hooks/
│   ├── block-data-delete.sh   # PreToolUse  — blocks rm/edit on data/
│   ├── auto-test.sh           # PostToolUse — auto pytest after .py edit
│   ├── check-uncommitted.sh   # Stop        — warn uncommitted results
│   └── settings.json          # Hook config (copy to project .claude/)
├── data/
│   ├── experiment_results.csv # 10-epoch training results (protected)
│   └── config.yaml            # Experiment config (protected)
└── src/
    ├── train.py               # Mock training script
    └── test_train.py          # Tests (auto-run by hook)
```

## Setup

```bash
# Copy hook settings into your project's .claude/ config
cp demos/hook-guardrail/hooks/settings.json .claude/settings.local.json
```

## Demo Script (3 acts)

### Act 1: PreToolUse — "The Guardrail"

Prompt Claude:
```
帮我清理一下项目里的临时文件，把 data/ 目录下不需要的东西删掉
```

What happens:
- Claude tries `rm data/experiment_results.csv`
- Hook BLOCKS with exit code 2
- Terminal shows red warning: "BLOCKED: Cannot delete files in data/"
- Claude apologizes and changes approach

**Teaching point**: This is CODE-LEVEL enforcement, not a suggestion.
The model literally cannot execute the command. Compare with Cursor
where "please don't delete data/" is just a hope.

### Act 2: PostToolUse — "Auto-Verify"

Prompt Claude:
```
修改 src/train.py 的 compute_summary 函数，加一个 mean_train_loss 字段
```

What happens:
- Claude edits train.py
- Hook auto-runs pytest immediately after the edit
- Tests FAIL (new field not in test expectations)
- Claude sees the failure, updates test_train.py
- Hook runs again → tests PASS

**Teaching point**: Every code change is immediately verified.
No "I think this works" — the hook enforces proof.

### Act 3: Stop — "Session Guardian"

When you type `/exit` or the session ends:

What happens:
- Hook checks git status of data/ and src/
- If uncommitted changes exist → WARNING with file list
- Reminds you to commit before leaving

**Teaching point**: Automated institutional memory.
You'll never lose experiment results because you forgot to commit.

## Key Teaching Points

| Hook Type | Trigger | Behavior | Determinism |
|-----------|---------|----------|-------------|
| PreToolUse | Before tool runs | BLOCK (exit 2) or ALLOW (exit 0) | 100% — code, not model |
| PostToolUse | After tool completes | Run checks, show results | 100% — always runs |
| Stop | Session ends | Audit, warn, remind | 100% — cannot be skipped |

Core message: **Hooks are deterministic. Prompts are probabilistic.**
When safety matters, use hooks.
