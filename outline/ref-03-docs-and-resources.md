# Reference 03: Documentation, Resources & Context Management Techniques

> Sources: Notion LifeOS, official docs, community resources
> Status: Partial — awaiting Notion content extraction for full link list

---

## 1. Harness Engineering Concepts

### What is Harness Engineering?

The shift from "prompt engineering" (optimizing what you say to the model) to
"harness engineering" (optimizing the **system around** the model):

- CLAUDE.md as project-level instruction layer
- Hook scripts as behavioral guardrails
- Skills as reusable domain knowledge packages
- Subagent architecture for context management
- Pipeline state machines for workflow automation

### Key Insight for the Talk
> In Cursor, you engineer prompts.
> In Claude Code, you engineer the harness.
> The model is the same — the difference is what **surrounds** it.

---

## 2. Context Management Techniques

### The Problem
Context window is finite. AI researchers work with:
- Large codebases (experiment frameworks, model implementations)
- Long-running sessions (debug cycles, paper writing)
- Multiple concerns in parallel (code + data + results + writing)

### Techniques Hierarchy

**Level 1: Basic (most users know)**
- `/clear` between unrelated tasks
- `/compact` when context feels "foggy"

**Level 2: Intermediate**
- `/compact focus on X` — directed compression
- CLAUDE.md < 200 lines — only what Claude can't infer
- Auto Memory for cross-session persistence
- `/btw` for tangential questions (doesn't pollute history)

**Level 3: Advanced (harness engineering)**
- Subagent delegation for heavy generation (slides, HTML, analysis)
- Skills lazy-loading — full prompt only loaded on use
- Workflow pipeline state — externalize stage tracking to JSON
- PreCompact hook — detect approaching limit, set flags before compression
- Multi-session parallelism — Writer session + Reviewer session

### Memory Architecture

```
Per-Session                    Cross-Session
─────────────                  ──────────────
Conversation history           CLAUDE.md (user-written rules)
Tool call results              MEMORY.md (auto-saved, first 200 lines)
Loaded skill prompts           memory/*.md (topic-specific notes)
Compacted summaries            state.json (pipeline state)
```

---

## 3. Notion LifeOS References

### Known Pages (from search)

| Page | Type | Status | Key Content |
|------|------|--------|-------------|
| Claude Code & Codex 最佳实践 | Notes | 进行中 | Main collection, last edited today |
| Claude code 最佳实践 | Notes | 进行中 | Earlier version |
| Coding Agent Best Practices | Knowledge | — | URL: code.claude.com/docs/en/overview, folder: AI/Agentic Engineering |
| Claude Code官方文档 | Resource/Doc | — | URL: code.claude.com/docs/zh-CN/hooks-guide |
| vibe coding tutorial | Blog | 进行中 | Related blog post |
| Everything-Claude-Code | Task | — | Learning task |
| OpenClaw最佳实践 → Claude Code & Codex 最佳实践 | Notes | 已完成 | Merged into main page |

### Links to Extract (pending agent results)
- [ ] All bookmarked URLs from "Claude Code & Codex 最佳实践"
- [ ] All bookmarked URLs from "Claude code 最佳实践"
- [ ] All bookmarked URLs from "Coding Agent Best Practices"
- [ ] Boris Cherny Twitter/X references
- [ ] Community blog posts and tutorials

---

## 4. Known External Resources

### Official Documentation
- `code.claude.com/docs/en/overview` — Main docs
- `code.claude.com/docs/en/how-claude-code-works` — Architecture
- `code.claude.com/docs/en/tools-reference` — Tool system
- `code.claude.com/docs/en/best-practices` — Official best practices
- `code.claude.com/docs/en/sub-agents` — Subagent docs
- `code.claude.com/docs/en/memory` — Memory system
- `code.claude.com/docs/zh-CN/hooks-guide` — Hooks guide (Chinese)

### GitHub
- `github.com/anthropics/claude-code` (78.1k stars) — Official repo

### Community (to be populated from Notion)
- Boris Cherny Twitter tips — [links pending]
- Other community best practices — [links pending]

---

## 5. Talk-Ready Comparisons

### Before/After: IDE Assistant vs Agent Harness

**Scenario: Reproduce a paper's experiment**

IDE Assistant approach:
1. Open paper PDF, manually read methodology
2. Ask AI: "Write me the model architecture from this paper"
3. Copy-paste code into editor
4. Manually debug import errors
5. Ask AI: "Fix this error: ..."
6. Repeat steps 4-5 for 30 minutes
7. Manually set up training script
8. Manually monitor training

Agent Harness approach:
1. Tell Claude: "Reproduce the experiment from this paper. The PDF is at ./paper.pdf. Use PyTorch, write tests, and run a small-scale validation."
2. Claude autonomously:
   - Reads the paper
   - Searches for existing implementations
   - Implements the architecture with tests
   - Runs tests to verify
   - Sets up training script
   - Uses `/loop` to monitor training
   - Generates results slides via `/slides-dispatch`

### Before/After: Managing Experiment Lifecycle

IDE Assistant:
- Manual tracking: "What stage am I at?"
- Context lost between sessions
- No automated reminders
- Results scattered across files

Agent Harness:
- Pipeline hooks auto-track stages
- Memory persists across sessions
- Stop hook reminds next step
- Automated slide generation and changelog

---

## 6. Supplementary Material Ideas

### Demo Scenarios to Build
1. **Hook Demo**: Show PreToolUse blocking a dangerous operation + suggesting safer alternative
2. **Skill Demo**: Show `/agent-exp-orchestration` managing parallel experiments
3. **Subagent Demo**: Show context size before/after using `/slides-dispatch`
4. **Loop Demo**: Show `/loop 1m` monitoring a simulated training job
5. **Pipeline Demo**: Show full dev → experiment → analysis → commit cycle
6. **MCP Demo**: Show Notion integration for research note-taking during coding
