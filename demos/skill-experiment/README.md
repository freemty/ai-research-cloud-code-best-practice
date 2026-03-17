# Skill Demo: Experiment Setup

A reusable Skill that creates standardized ML experiment workspaces
with one command.

## Structure

```
demos/skill-experiment/
├── SKILL.md             # The skill itself (install to ~/.claude/skills/)
├── before-after.sh      # Show contrast: manual vs skill
└── README.md
```

## Install (for live demo)

```bash
# Copy skill to Claude Code skills directory
mkdir -p ~/.claude/skills/experiment-setup
cp demos/skill-experiment/SKILL.md ~/.claude/skills/experiment-setup/SKILL.md
```

## Demo Script (3 acts)

### Act 1: "The Pain" — Show Manual Setup

```bash
# Run this to show what manual experiment setup looks like
bash demos/skill-experiment/before-after.sh
```

Shows 15+ manual steps: mkdir, touch, write config, write train.py...
Audience feels the pain.

### Act 2: "The Skill" — One Command

Prompt Claude:
```
/experiment-setup

Paper: "Attention Is All You Need" (arxiv 1706.03762)
Dataset: WMT14 EN-DE
Architecture: Transformer base config
```

What happens:
- Claude loads the skill (on-demand, not in context until invoked)
- Creates full directory tree in ~10 seconds
- Generates config.yaml with paper-specific hyperparameters
- Writes train.py skeleton with proper seeding + logging
- Writes evaluate.py + README.md
- Verifies config.yaml is valid YAML

### Act 3: "The Reuse" — Different Experiment, Same Workflow

Prompt Claude:
```
/experiment-setup

Idea: LoRA fine-tuning of LLaMA-3 on custom QA dataset
Dataset: ~/data/my-qa-pairs.json
Base model: meta-llama/Llama-3-8B
```

Same skill, completely different experiment. Same structure, same quality.

**Teaching point**: Write once, reuse forever. The skill encodes your
lab's best practices — every experiment follows the same standard.

## Key Teaching Points

| Aspect | Without Skill | With Skill |
|--------|--------------|------------|
| Setup time | 15-30 min | ~10 sec |
| Consistency | Varies per person | Always standardized |
| Config | Scattered in code | Single config.yaml |
| Logging format | Ad-hoc | Standardized CSV |
| Reproducibility | "It works on my machine" | Deterministic seeding + config |
| Onboarding | "Ask the senior" | Skill IS the documentation |

Core message: **Skills = reusable institutional knowledge.**
Not prompts you retype. Not README you forget to read.
Executable workflow that Claude follows every time.
