# Slide Outline: AI Research Cloud Code Best Practice

Style: Terminal Green (developer-focused, monospace, dark terminal aesthetic)
Target: 38 slides

---

## Opening (Slides 1-3)

### Slide 1: Title
- Title: "AI Research Cloud Code Best Practice"
- Subtitle: "From Assistant to Agent — a paradigm shift for AI researchers"
- Author + Date

### Slide 2: The Question
- "If the model is the same, why does the harness matter?"
- Visual: Cursor logo vs Claude Code terminal side-by-side

### Slide 3: The Answer
- "This is NOT a tool comparison. This is a paradigm shift."
- Assistant Paradigm → ReAct Agent Paradigm
- Key phrase: "You don't switch tools. You switch how you work."

---

## Part 1: Core Design & Paradigm (Slides 4-12)

### Slide 4: Part 1 Section Title
- "Core Design & Paradigm"
- "Understanding what makes an Agent different"

### Slide 5: Assistant vs Agent — Comparison Table
- 5-row table: Work Mode / Capability / Context / Usage / Feedback Loop
- Left: Traditional Chat (answer & wait, text only, single file)
- Right: Agent (autonomous, executes actions, cross-project)

### Slide 6: The Agentic Loop (ReAct)
- Diagram: Gather Context → Take Action → Verify Results → (loop)
- Key point: NOT linear — iterative and self-correcting

### Slide 7: Why ReAct Matters for Research
- Multi-step experiments: data → run → analyze → iterate
- Autonomous codebase exploration
- Self-directed debugging
- "Delegate, don't dictate"

### Slide 8: System Architecture
- Two pillars: Models + Tools
- Three environments: Local / Cloud / Remote Control

### Slide 9: Tool System Overview
- 28+ built-in tools in 5 categories
- File Ops / Search / Execution / Web / Code Intelligence
- Plus orchestration: Agent, Skill, Cron, Task

### Slide 10: Extension Mechanisms
- 4 pillars: Skills / MCP / Hooks / Subagents
- Each with 1-line description

### Slide 11: Context Window — The Critical Resource
- "Your most important resource is context, not compute"
- Context = conversation + files + outputs + instructions + skills

### Slide 12: Context Management Strategies
- 3-tier: Basic (/clear, /compact) → Intermediate (CLAUDE.md, Memory, /btw) → Advanced (Subagents, Skills lazy-load, Pipeline state)

---

## Part 2: Scenarios & Features (Slides 13-27)

### Slide 13: Part 2 Section Title
- "Scenarios & Feature Practice"
- "What you can do that IDE assistants can't"

### Slide 14: Feature Overview — The Big Four
- Hook / Skills / Sub-agent / Loop
- Each with icon + 1-line value prop

### Slide 15: Hook — What It Is
- Shell scripts triggered on events
- 4 types: PreToolUse / PostToolUse / Stop / PreCompact
- Key: deterministic execution, not suggestions

### Slide 16: Hook — Real Example: Experiment Pipeline
- Pipeline diagram: dev → skill-update → experiment → monitoring → analysis → commit
- Stop hook reminds next step; PostToolUse advances stage

### Slide 17: Hook — Real Example: Safety Guardrails
- slides-guard.sh blocks heavy skills, suggests dispatcher
- console.log audit on session end
- git push review opens editor before push

### Slide 18: Skills — What It Is
- Markdown files loaded on-demand into context
- Encode institutional knowledge that survives across sessions
- "Your research lab's playbook, machine-readable"

### Slide 19: Skills — Research Skills Showcase
- Table: fars-system / fars-reviewer / agent-exp-orchestration / rope2sink / weekly-progress
- Each with 1-line description

### Slide 20: Skills — Extensibility
- writing-skills: TDD for skill docs
- find-skills: discover from open ecosystem (npx skills)
- "You can build your own research workflow skills"

### Slide 21: Sub-agent — What It Is
- Independent context window + system prompt + tools
- Types: Explore (Haiku, fast) / Plan / General-purpose / Custom
- Cannot spawn other subagents (prevents infinite nesting)

### Slide 22: Sub-agent — The Delegation Pattern
- Diagram: Main Context (clean, 10 lines) → Subagent (reads 60KB skill, generates 3000 lines HTML) → Returns 5-line summary
- "Heavy lifting in disposable context, results in clean context"

### Slide 23: Sub-agent — Research Applications
- Parallel: Agent 1 reads paper + Agent 2 searches implementations + Agent 3 checks datasets
- Split-role: factual reviewer + security expert + senior engineer
- Writer/Reviewer: one implements, another audits

### Slide 24: Loop — What It Is
- `/loop 5m <command>` — recurring autonomous execution
- Use cases: training monitoring, experiment polling, CI watching

### Slide 25: The Complete Picture — Workflow Pipeline
- Full architecture diagram: Hooks (trigger) + State (JSON) + Skills (execution)
- Show the complete dev → commit cycle with all features integrated

### Slide 26: Before/After — Paper Reproduction
- Left (IDE): 8 manual steps, copy-paste, repeat debug
- Right (Agent): 1 prompt → Claude autonomously explores, implements, tests, monitors

### Slide 27: Before/After — Experiment Lifecycle
- Left: manual tracking, context lost, no reminders, scattered results
- Right: pipeline hooks auto-track, memory persists, automated slides + changelog

---

## Part 3: Documentation & Management (Slides 28-35)

### Slide 28: Part 3 Section Title
- "Documentation & Management Techniques"
- "Engineer the harness, not just the prompt"

### Slide 29: Harness Engineering — The Concept
- "In Cursor, you engineer prompts. In Claude Code, you engineer the harness."
- Harness = CLAUDE.md + Hooks + Skills + Subagents + Pipeline

### Slide 30: Three Harness Engineering Papers
- OpenAI: system production engineering
- Anthropic: long-running runtime framework
- Manus: working memory / context management
- "One sentence each" comparison

### Slide 31: CLAUDE.md Best Practices
- DO: build commands, code style, test guidelines, architecture decisions
- DON'T: what Claude infers, standard conventions, detailed API docs
- "Hooks > CLAUDE.md for 100% execution; Skills > CLAUDE.md for occasional knowledge"

### Slide 32: 9 Coding Agent Principles
- Compact grid: Less is More / Context is Everything / Leverage Sycophancy / Avoid Gap-Filling / Define Endpoints / CLAUDE.md as Logic Dir / Rules vs Skills / Spa Day / Don't Chase Tools

### Slide 33: Boris Cherny's 10 Tips (Part 1: 1-5)
- 1. git worktree parallel sessions
- 2. Plan Mode first
- 3. Invest in CLAUDE.md
- 4. Create reusable Skills
- 5. Let Claude fix bugs independently (Slack MCP)

### Slide 34: Boris Cherny's 10 Tips (Part 2: 6-10)
- 6. Level up prompting (reviewer pattern)
- 7. Terminal & environment config (Ghostty, voice input)
- 8. Use subagents ("use subagents" keyword)
- 9. Data & analysis (BigQuery, real-time metrics)
- 10. Use Claude for learning (HTML slides, ASCII diagrams)

### Slide 35: Common Failure Patterns
- Table: Kitchen sink / Repeated corrections / Over-specified CLAUDE.md / Trust-verification gap / Infinite exploration
- Each with problem + solution

---

## Closing (Slides 36-38)

### Slide 36: Key Takeaways
- 1. It's a paradigm shift, not a tool swap
- 2. Engineer the harness: Hooks + Skills + Subagents + Loop
- 3. Context is your most critical resource — manage it actively
- 4. Build reusable workflows, not one-off prompts

### Slide 37: Resources
- Official docs: code.claude.com/docs
- GitHub: anthropics/claude-code (78.1k stars)
- Harness Engineering articles (3 links)
- Boris Cherny @bcherny
- Community: Everything Claude Code, Superpowers, ClawHub

### Slide 38: End Slide
- "Questions?"
- Contact / social info
- "The future belongs to those who engineer their agents, not just prompt them."
