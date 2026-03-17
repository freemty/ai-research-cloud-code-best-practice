# Reference 05: Skills Inventory (23 Skills)

> Source: ~/.claude/skills/, agent scan results

---

## Skills by Category

### A. Research Platform (6 skills)

| Skill | Description | Research Showcase Value |
|-------|-------------|----------------------|
| **fars-system** | FARS (Full Autonomous Research System) architecture overview — 8 lead agents in parallel, KB construction, evaluation pipeline, hook behaviors | Demo: multi-agent autonomous research system architecture |
| **fars-ideagen** | Idea-generation module implementation details — method signatures, tool schemas, hook thresholds, token counting, message persistence | Demo: method-level precision in research agent code |
| **fars-reviewer** | Paper integrity audit agent — covers 8 AI-specific failure modes | Demo: automated paper quality assurance |
| **fars-plan** | Experiment plan generation agent — converts research proposals to structured executable plans | Demo: research proposal → experiment plan automation |
| **rope2sink** | ICML 2026 paper "From a Spiral to a Sink" writing guide — LaTeX, attention sink analysis, DiT architecture | Demo: domain-specific paper writing skill |
| **agent-exp-orchestration** | Parallel LLM experiment orchestration — job conflicts, rate limits, subprocess isolation, cron monitoring, retry, post-run analysis | Demo: managing concurrent experiments at scale |

### B. Presentation & Visualization (4 skills)

| Skill | Description | Research Showcase Value |
|-------|-------------|----------------------|
| **slides-dispatch** | Thin dispatcher for slide generation — delegates to subagent, keeps main context clean | Demo: subagent delegation pattern (core talk material) |
| **agent-slides** | ML experiment analysis slides — cross-comparison tables, recall/FPR tables, heatmaps, case studies | Demo: auto-generated experiment result presentations |
| **frontend-slides** | Animation-rich HTML presentations, PPT-to-web conversion | Demo: zero-dependency single-file presentations |
| **frontend-design** | Production-grade frontend interfaces with distinctive design | Supporting: UI for research dashboards |

### C. Writing & Editing (4 skills)

| Skill | Description | Research Showcase Value |
|-------|-------------|----------------------|
| **humanizer** | Remove AI writing artifacts from English text (based on Wikipedia AI writing signs guide) | Demo: paper polishing, removing detectable AI patterns |
| **Humanizer-zh** | Chinese version — remove AI artifacts, inject authentic personality | Demo: Chinese academic/blog writing |
| **writing-skills** | Meta-skill: create, edit, verify agent skills (TDD approach for skill docs) | Demo: how to create your own skills |
| **commit-changelog** | Standardized commit messages and changelog entries | Supporting: structured research progress tracking |

### D. Tool Integration (4 skills)

| Skill | Description | Research Showcase Value |
|-------|-------------|----------------------|
| **agent-reach** | Install/configure 12+ platform tools (Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, Douyin, LinkedIn, Boss, RSS) | Demo: multi-platform data access for research |
| **nano-banana** | Image generation/editing via Gemini CLI | Supporting: blog images, diagrams, visual assets |
| **notebooklm** | Query Google NotebookLM from Claude Code — source-grounded, citation-backed answers | Demo: document-grounded research Q&A |
| **notion-lifeos** | Notion PARA system — tasks, notes, projects, resources, areas, make-time entries | Demo: research project management integration |

### E. Agent Architecture (4 skills)

| Skill | Description | Research Showcase Value |
|-------|-------------|----------------------|
| **proactive-agent** | Transform agents from task-followers to proactive partners — WAL Protocol, Working Buffer, Compaction Recovery | Demo: advanced agent architecture patterns |
| **find-skills** | Discover and install skills from open ecosystem via `npx skills` CLI | Demo: extensibility of the skill system |
| **munger-observer** | Daily wisdom review applying Charlie Munger's mental models | Supporting: decision-making framework |
| **weekly-progress** | Weekly progress document from real experiment data | Demo: automated research reporting |

### F. Other

| Skill | Description |
|-------|-------------|
| **learned** | Empty directory (no skill.md) |

---

## Top Skills for Talk Demo

Priority selection for showcasing in the talk:

### Must-Show (directly illustrate paradigm difference)
1. **slides-dispatch** — Subagent delegation pattern (context protection)
2. **agent-exp-orchestration** — Parallel experiment management (impossible in IDE assistant)
3. **writing-skills** — Meta: how to create skills (shows extensibility)

### Should-Show (strong AI Research value)
4. **fars-system** — Full autonomous research system (impressive scale)
5. **notebooklm** — Document-grounded research answers
6. **weekly-progress** — Automated research reporting
7. **humanizer** / **Humanizer-zh** — Paper polishing

### Could-Show (if time permits)
8. **agent-reach** — Multi-platform data access
9. **proactive-agent** — Advanced agent architecture
10. **find-skills** — Skill ecosystem discovery

---

## Skill System Architecture Notes

- Skills stored as markdown files in `~/.claude/skills/{name}/skill.md`
- Loaded on-demand into context (lazy loading)
- 22 of 23 use YAML frontmatter format
- Skill prompt sizes range from small (~1KB) to heavy (~57KB for frontend-slides)
- Heavy skills should use subagent delegation pattern (see ref-02)
- Skills are user-invocable via `/skill-name` syntax
- New skills can be installed via `find-skills` or created via `writing-skills`
