# Reference 01: Claude Code Architecture & ReAct Paradigm

> Source: Official docs at code.claude.com, anthropics/claude-code repo (78.1k stars)
> Note: No standalone "learn-claude-code" repo exists. Architecture docs live at code.claude.com/docs/

---

## 1. Core Thesis: Assistant vs Agent Paradigm

| Dimension | Traditional Chat Assistant | Claude Code (Agent) |
|-----------|---------------------------|---------------------|
| Work Mode | Answer question, then wait | Read files, run commands, work autonomously |
| Capability | Text reply only | Execute actions: edit, search, run, deploy |
| Context | Only sees current file | Sees entire project, works cross-file |
| Usage | You write code, AI reviews | You describe goal, AI plans and implements |
| Feedback Loop | Depends on user judgment | Self-verifies (run tests, compare screenshots) |

Core principle: **"Delegate, don't dictate"** — give goals and context, let Claude decide execution steps.

---

## 2. System Architecture

Claude Code = **Agentic Harness** built around Claude LLM.

Two core components:
- **Models** — reasoning and code understanding
- **Tools** — action execution

Three runtime environments:
| Environment | Code Runs On | Use Case |
|-------------|-------------|----------|
| Local | Your machine | Default, full file/tool access |
| Cloud | Anthropic-managed VM | Offload tasks, remote work |
| Remote Control | Your machine, via browser | Web UI + local execution |

---

## 3. The Agentic Loop (ReAct)

Three-phase cycle (NOT linear — iterative and interleaved):

```
┌─────────────────────┐
│  1. Gather Context   │ ← Search files, read code, understand structure
│         ↓            │
│  2. Take Action      │ ← Edit files, run commands, make changes
│         ↓            │
│  3. Verify Results   │ ← Run tests, check output, confirm correctness
│         ↓            │
│     (loop back)      │
└─────────────────────┘
```

Key characteristics:
- Loop adapts to task — simple Q might need only context; complex bug fix requires many cycles
- User is part of the loop — can interrupt and redirect at any time
- Claude works autonomously but stays responsive to user input
- Each tool call result feeds back into the loop, guiding next decision

### Why this matters for AI Research:
- Multi-step experiments: gather data → run experiment → analyze results → iterate
- Autonomous codebase exploration: understand unfamiliar paper implementations
- Self-directed debugging: find bug → hypothesize → test → fix → verify

---

## 4. Tool System (28+ Built-in Tools)

| Category | Capabilities | Tools |
|----------|-------------|-------|
| File Ops | Read, edit, create, rename | `Read`, `Edit`, `Write`, `NotebookEdit` |
| Search | Pattern match files, regex content search | `Glob`, `Grep` |
| Execution | Shell commands, tests, git | `Bash` |
| Web | Search web, fetch docs | `WebFetch`, `WebSearch` |
| Code Intelligence | Type errors, goto def, find refs | `LSP` |

Orchestration tools:
- `Agent` — Spawn subagents
- `AskUserQuestion` — Ask user for input
- `TaskCreate/TaskList/TaskUpdate` — Task management
- `Skill` — Invoke skills (reusable workflows)
- `EnterPlanMode/ExitPlanMode` — Plan mode toggle
- `CronCreate/CronDelete/CronList` — Scheduled tasks

Permission model:
- Some tools need user approval (`Bash`, `Edit`, `Write`, `WebFetch`)
- Read-only tools are permission-free (`Read`, `Glob`, `Grep`)
- Configurable via `allowedTools`

Extension mechanisms:
- **Skills** — On-demand domain knowledge and reusable workflows
- **MCP (Model Context Protocol)** — Connect external services (Notion, Jira, Slack, etc.)
- **Hooks** — Auto-run scripts before/after tool execution
- **Subagents** — Specialized agents in independent context windows

---

## 5. Context Management (The Most Critical Resource)

Context window contains:
- Conversation history
- File contents
- Command outputs
- CLAUDE.md instructions
- Loaded skills
- System prompt

Management strategies:

| Strategy | How | When |
|----------|-----|------|
| Auto Compaction | Clear old tool output, summarize conversation | Near context limit |
| `/compact` | Manual compress, can specify focus | Mid-session cleanup |
| `/clear` | Full context reset | Between unrelated tasks |
| Subagents | Run in independent context, return summary only | Heavy generation tasks |
| Skills lazy-load | Full content loaded only on use | Always |
| `/btw` sidebar | Answer appears in dismissable overlay, not in history | Quick tangential questions |

Persistent memory:
- **CLAUDE.md** — User-written project instructions, loaded every session
- **Auto Memory** — Claude's self-saved notes (`~/.claude/projects/<project>/memory/`)
- MEMORY.md first 200 lines loaded at session start

---

## 6. Subagent Architecture

- Each subagent has **independent context window, system prompt, tool access**
- Built-in types: `Explore` (Haiku, read-only fast search), `Plan` (planning research), `General-purpose` (complex multi-step)
- Custom agents via `.claude/agents/` markdown files
- Support foreground/background, parallel research, chained calls
- Subagents **cannot spawn other subagents** (prevents infinite nesting)

---

## 7. Official Best Practices (Expanded)

### The Explore-Plan-Code Workflow (4 phases)
1. **Explore**: Plan Mode — read files, ask questions, no modifications
2. **Plan**: Create detailed implementation plan, `Ctrl+G` to edit in editor
3. **Implement**: Normal Mode — code + verify per plan
4. **Commit**: Let Claude commit and create PR

> Skip planning for trivial tasks (typos, logging). Use planning for uncertain approaches, multi-file changes, unfamiliar code.

### Top 10 Official Best Practices

1. **Give Claude verification means** — tests, screenshots, expected output (highest leverage)
2. **Explore → Plan → Code** — separate research and execution phases
3. **Provide specific context** — name files, describe symptoms, reference patterns ("follow HotDogWidget.php")
4. **Configure environment** — CLAUDE.md, permissions, CLI tools, MCP, hooks, skills, subagents
5. **Communicate effectively** — ask like talking to senior engineer; let Claude interview you for specs
6. **Course-correct early** — `Esc` to stop, `Esc+Esc` to rewind; if two corrections fail, `/clear` + better prompt
7. **Manage context aggressively** — `/clear` between tasks, `/compact focus on X`, subagents for investigation
8. **Automate and scale** — `claude -p` for CI/scripts, Writer/Reviewer pattern, file fan-out
9. **Avoid common failure patterns** (see table below)
10. **Develop your intuition** — notice what works, apply flexibly not rigidly

### Common Failure Patterns

| Pattern | Problem | Solution |
|---------|---------|----------|
| Kitchen sink session | Mixed tasks, irrelevant context | `/clear` between tasks |
| Repeated corrections | Context filled with failed attempts | 2 corrections → `/clear` + better prompt |
| Over-specified CLAUDE.md | Too long → Claude ignores important rules | Ruthlessly prune; don't write what Claude gets right |
| Trust-verification gap | Looks right but misses edge cases | Always provide verification (tests/scripts/screenshots) |
| Infinite exploration | Unbounded research fills context | Narrow scope or use subagents |

### CLAUDE.md Best Practices
- Generate with `/init`, keep concise
- Include: build commands, code style, test guidelines, repo conventions, architecture decisions
- Exclude: what Claude can infer from code, standard conventions, detailed API docs, frequently changing info
- Use `@path/to/import` syntax to reference other files
- Priority markers: "IMPORTANT" or "YOU MUST" for critical rules
- **Hooks > CLAUDE.md rules** for things that must execute 100%
- **Skills > CLAUDE.md** for domain knowledge not needed every session

---

## Key Doc Sources

- `code.claude.com/docs/en/how-claude-code-works`
- `code.claude.com/docs/en/tools-reference`
- `code.claude.com/docs/en/best-practices`
- `code.claude.com/docs/en/sub-agents`
- `code.claude.com/docs/en/memory`
- GitHub: `github.com/anthropics/claude-code`
