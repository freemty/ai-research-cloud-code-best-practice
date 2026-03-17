# AI Research Cloud Code Best Practice — Talk Outline

## Core Thesis

> This is NOT about which IDE has a better model.
> This is a **paradigm shift** — from Assistant to ReAct-paradigm Agent harness.

Target audience: AI researchers still anchored in Cursor-style IDE thinking,
who believe "same model = same outcome regardless of harness."

---

## Part 1: Core Design & Paradigm

### 1a. Claude Code High-Level Architecture
- Source: `learn-claude-code` repo
- System design walkthrough
- How Claude Code differs architecturally from IDE-embedded assistants
- The agentic loop: tool use, context management, autonomous decision-making

### 1b. What the ReAct Paradigm Really Means
- Assistant paradigm: single-turn Q&A, user drives every step
- ReAct paradigm: Reasoning + Acting in a loop
  - Observe → Think → Act → Observe → ...
  - Agent autonomously decides next tool call
  - Agent can self-correct, backtrack, and chain complex operations
- Why this distinction matters for research workflows
  - Multi-step experiments
  - Autonomous exploration of codebases
  - Self-directed debugging and iteration

---

## Part 2: Scenarios & Feature Practice

### 2a. AI Research Critical Scenarios
- Sources: personal Memory files, installed Skills
- Potential scenarios:
  - Paper implementation & reproduction
  - Experiment orchestration & monitoring
  - Data pipeline debugging
  - Literature review & knowledge base construction
  - Multi-agent parallel evaluation

### 2b. Special Cases — Showcasing Unique Features
- **Hook**: automated guardrails and workflow triggers
  - e.g., pre-commit security checks, auto-formatting, build verification
  - Custom hooks for research-specific validation
- **Skills**: domain-specific reusable capabilities
  - e.g., experiment orchestration, slide generation, paper writing
  - How Skills encode institutional knowledge
- **Sub-agent**: parallel task decomposition
  - e.g., multi-perspective code review, parallel experiment analysis
  - Orchestrator + worker pattern for complex research tasks
- **Loop**: recurring autonomous monitoring
  - e.g., polling experiment status, watching training jobs

---

## Part 3: Documentation & Management Techniques

### 3a. Harness Engineering & Context Management
- CLAUDE.md as project-level instruction layer
- Context window awareness and management strategies
- Memory system: persistent knowledge across sessions
- Prompt engineering at the harness level (not just the model level)

### 3b. Curated Resources
- Source: Notion LifeOS — Claude Code Best Practice collection
- Links and references to be pulled from Notion
- Boris Cherny's Twitter tips on practical usage patterns

### 3c. Supplementary Materials
- Community best practices
- Real-world research workflow examples
- Before/after comparisons: IDE-assistant vs. agent-harness approach

---

## Guiding Principle

Create **concrete, compelling scenarios** that demonstrate how Claude Code features
(Loop, Hook, Sub-agent, Skills) deliver unique value for AI Research —
things that are structurally impossible in an Assistant-paradigm tool.

---

## Reference Documents

| File | Contents | Status |
|------|----------|--------|
| `ref-01-architecture.md` | Claude Code architecture, ReAct paradigm, tool system, context mgmt, official best practices | Done |
| `ref-02-features-for-research.md` | Hooks, Skills, Subagent, Loop, Pipeline — all with real examples from personal config | Done |
| `ref-03-docs-and-resources.md` | Harness engineering concepts, context techniques, Notion links, demo scenario ideas | Partial (awaiting Notion links) |
| `ref-04-notion-links.md` | All extracted URLs, Boris Cherny 10 tips, Harness Engineering articles, 9 coding agent principles, community links | Done |
| `ref-05-skills-inventory.md` | Full 23-skill inventory with descriptions, categories, and research relevance ranking | Done |
