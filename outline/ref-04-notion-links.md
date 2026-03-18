# Reference 04: Notion Links & Boris Cherny Tips

> Sources: Notion LifeOS pages — "Claude Code & Codex 最佳实践", "Claude code 最佳实践", "Coding Agent Best Practices"

---

## 1. Boris Cherny (Claude Code Creator) 10 Tips

Source: @bcherny Twitter thread (2026-01-31)

### Tip 1: Multi-task in Parallel
- Use `git worktree` to run multiple Claude sessions simultaneously
- Create shell alias for quick switching between worktrees

### Tip 2: Plan Mode First
- Invest effort in detailed planning before implementation
- Let one Claude write the plan, another Claude review it
- Switch back to plan mode whenever issues arise

### Tip 3: Invest in CLAUDE.md
- Every time you correct Claude, update CLAUDE.md with a rule to prevent recurrence
- Iterate continuously until error rate drops noticeably

### Tip 4: Create Reusable Skills
- Turn frequent operations (done >1x per day) into custom slash commands, commit to git
- Examples: scan tech debt, sync data, automated tasks

### Tip 5: Let Claude Fix Bugs Independently
- Enable Slack MCP integration, paste bug threads directly to Claude
- Let Claude inspect failing CI tests and Docker logs autonomously

### Tip 6: Level Up Prompting
- Have Claude act as reviewer to challenge code
- Ask Claude to implement elegant solutions from scratch
- Write detailed specs upfront to reduce ambiguity

### Tip 7: Terminal & Environment Config
- Use Ghostty terminal for better rendering
- Customize status bar to show context usage and git branch
- Use voice input for more detailed prompts

### Tip 8: Use Subagents
- Append "use subagents" to requests for more compute
- Delegate subtasks to subagents, keep main context clean
- Route permission requests to Opus 4.5 via hooks for auto-approval

### Tip 9: Use Claude for Data & Analysis
- Leverage CLI tools (BigQuery, databases) directly in Claude Code
- Real-time metric analysis without manual SQL

### Tip 10: Use Claude for Learning
- Enable "Explanatory" output mode
- Have Claude generate HTML presentations to explain code
- Request ASCII diagrams for architecture visualization
- Build spaced-repetition learning skills

---

## 2. Harness Engineering Articles (Three Key Papers)

### OpenAI — Harness Engineering
- URL: https://openai.com/index/harness-engineering/
- Focus: High-throughput, constrained, observable engineering system for Codex
- Key concepts: Repository knowledge, agent legibility, architecture boundaries, low-blocking merges, AI slop cleanup, agent-consumable observability

### Anthropic — Effective Harnesses for Long-Running Agents
- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Focus: Runtime framework for long-running agents
- Key concepts: Task decomposition, state persistence, error recovery, context compression, periodic self-check, clear stop conditions, human supervision points

### Manus — Context Engineering
- URL: https://manus.im/blog/context-engineering
- Focus: Working memory management for agents
- Key concepts: Information density, relevance, timeliness; organizing/filtering/rewriting context so model sees most useful info at each step

### Anthropic — Context Engineering for AI Agents
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

### Anthropic — Demystifying Evals for AI Agents
- URL: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

**One-line distinction:**
> OpenAI = system production engineering; Anthropic = long-running runtime framework; Manus = working memory / context management.

---

## 2b. Tw93 — Claude Code Six-Layer Architecture Deep Dive

Source: @HiTw93 on X (2026-03-16)
URL: https://x.com/HiTw93/status/2032091246588518683

**TLDR:** Claude Code is a six-layer agentic system. Performance issues stem from architectural imbalance, not model limitations.

### Six-Layer Model
1. System Instructions — 系统指令
2. Context Loading — 上下文加载 (CLAUDE.md, Memory)
3. Tool Definitions — 工具定义 (28+ built-in)
4. Skills/Workflows — 技能与工作流
5. Execution Control — 执行控制 (Hooks)
6. Verification — 验证层

> Overloading any single layer creates instability.

### NEW Insights (not in other sources)

- **MCP is a "hidden killer"**: Of the 200K token budget, ~15-20K is fixed overhead (system instructions + tool definitions + MCP servers). Five GitHub-like MCP servers can consume 25,000 tokens before conversation even begins.
- **CLAUDE.md budget: ~2.5K tokens**: Keep it brief. Only include build commands, constraints, architecture boundaries.
- **Skills description strategy**: Write descriptions that clarify "when to use" rather than "what I do" — helps Claude correctly match invocation timing.
- **Prompt Caching**: Maintain static prefixes (system prompt, CLAUDE.md, tool definitions) to maximize cache hits and reduce costs.
- **Hooks = deterministic checks**: Use hooks for linting, testing — don't rely on model consistency for repeatable checks.
- **Verification-first**: "If you cannot articulate what 'done' looks like, that task probably shouldn't run fully autonomous." Define success criteria upfront through tests, lint passes, and acceptance standards.

---

## 3. Coding Agent Best Practices (9 Principles)

Source: Notion page "Coding Agent Best Practices" (@systematicls on X)

### Principle 1: Less is More
- Don't install tons of plugins/harnesses
- Base CLI (Claude Code / Codex) is sufficient
- Truly useful features get integrated by OpenAI/Anthropic

### Principle 2: Context is Everything
- Separate research and implementation phases
- Precise instructions: "Implement JWT auth + bcrypt-12 + 7-day refresh token rotation" > "Build an auth system"

### Principle 3: Leverage Sycophancy Awareness
- Agents will try to please, even if it means fabricating
- Use neutral prompts: "Inspect the database, trace each component's logic, report all findings"

### Principle 4: Avoid "Filling in the Gaps"
- Agent's biggest weakness: connecting dots, making assumptions
- Solution: Set rules in CLAUDE.md, re-read task plan + relevant files

### Principle 5: Define Task Endpoints
- Test-driven: task not complete unless X tests pass
- Screenshot verification: implement → screenshot → verify
- Contract mechanism: create `{TASK}_CONTRACT.md` with completion criteria

### Principle 6: CLAUDE.md as Logic Directory
- Don't write 26,000-line encyclopedia
- Write IF-ELSE logic tree pointing to specific rule/skill files

### Principle 7: Rules vs Skills
- Rules = coding preferences ("use const/let not var")
- Skills = execution recipes ("how to implement OAuth flow")

### Principle 8: Regular Cleanup (Spa Day)
- Rules/skills accumulate → conflicts and context bloat
- Solution: Let agent self-organize: "Consolidate rules and skills, remove contradictions, ask me about updated preferences"

### Principle 9: Don't Chase New Tools
- Observation principle: Features integrated by OpenAI/Anthropic = truly useful
- You only need: regularly update CLI + read new feature notes

---

## 4. Official Documentation Links

### Core Pages
| Resource | URL |
|----------|-----|
| Overview | https://code.claude.com/docs/en/overview |
| Quickstart | https://code.claude.com/docs/en/quickstart |
| Best Practices | https://code.claude.com/docs/en/best-practices |
| Common Workflows | https://code.claude.com/docs/en/common-workflows |
| How Claude Code Works | https://code.claude.com/docs/en/how-claude-code-works |
| CLI Reference | https://code.claude.com/docs/en/cli-reference |

### Features & Extensions
| Resource | URL |
|----------|-----|
| Memory (CLAUDE.md) | https://code.claude.com/docs/en/memory |
| Skills | https://code.claude.com/docs/en/skills |
| Hooks | https://code.claude.com/docs/en/hooks |
| Hooks Guide | https://code.claude.com/docs/en/hooks-guide |
| MCP (Model Context Protocol) | https://code.claude.com/docs/en/mcp |
| Sub-agents | https://code.claude.com/docs/en/sub-agents |
| Agent Teams | https://code.claude.com/docs/en/agent-teams |
| Plugins | https://code.claude.com/docs/en/plugins |
| Features Overview | https://code.claude.com/docs/en/features-overview |

### Environment & Security
| Resource | URL |
|----------|-----|
| Permissions | https://code.claude.com/docs/en/permissions |
| Sandboxing | https://code.claude.com/docs/en/sandboxing |
| Settings | https://code.claude.com/docs/en/settings |
| Checkpointing | https://code.claude.com/docs/en/checkpointing |

### Integrations
| Resource | URL |
|----------|-----|
| VS Code | https://code.claude.com/docs/en/vs-code |
| JetBrains | https://code.claude.com/docs/en/jetbrains |
| Desktop App | https://code.claude.com/docs/en/desktop |
| Web Version | https://code.claude.com/docs/en/claude-code-on-the-web |
| Chrome Extension | https://code.claude.com/docs/en/chrome |
| Slack Integration | https://code.claude.com/docs/en/slack |
| GitHub Actions | https://code.claude.com/docs/en/github-actions |
| GitLab CI/CD | https://code.claude.com/docs/en/gitlab-ci-cd |
| Code Review | https://code.claude.com/docs/en/code-review |
| Remote Control | https://code.claude.com/docs/en/remote-control |

### Other
| Resource | URL |
|----------|-----|
| Agent SDK | https://platform.claude.com/docs/en/agent-sdk/overview |
| Docs Index (llms.txt) | https://code.claude.com/docs/llms.txt |
| Costs | https://code.claude.com/docs/en/costs |
| Codex App Intro (对比) | https://openai.com/zh-Hans-CN/index/introducing-the-codex-app/ |

---

## 5. Community & Tool Links

### Skill Resources
| Resource | URL |
|----------|-----|
| Anthropic Skill Creator Guide | https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md |
| Skills.sh (MCP Skill Marketplace) | https://skills.sh/ |
| Notion API Skill | https://skills.sh/intellectronica/agent-skills/notion-api |
| Manim Skill (Math Animations) | https://github.com/adithya-s-k/manim_skill |
| NanoBanana PPT Skills | https://github.com/op7418/NanoBanana-PPT-Skills |
| cc-nano-banana (Claude Code version) | https://github.com/kkoppenhaver/cc-nano-banana |
| NotebookLM Skill | https://github.com/PleasePrompto/notebooklm-skill |
| Frontend Slides | https://github.com/zarazhangrui/frontend-slides |

### Frameworks & Tools
| Resource | URL |
|----------|-----|
| Superpowers (multi-platform) | https://github.com/obra/superpowers — 完整软件开发工作流 plugin（brainstorm→plan→subagent-driven-dev→TDD→review→finish），14 个 Skills + SessionStart Hook，每个任务 spawn 独立 subagent + 两轮 review（spec 合规 + 代码质量），支持 Claude Code/Cursor/Codex/Gemini CLI |
| Everything Claude Code | https://github.com/affaan-m/everything-claude-code |
| Agent Reach (ClawHub) | https://clawhub.com |
| OpenClaw Setup | https://github.com/jiahao-shao1/openclaw-setup |
| OpenClaw Docs (Model Failover) | https://docs.openclaw.ai/concepts/model-failover |
| Happy (Mobile client) | https://github.com/slopus/happy |

### Practical Tips
| Tip | Detail |
|-----|--------|
| Jina AI Reader | Use `https://r.jina.ai/<URL>` to extract any webpage content |
| Haiku MCP limitation | Haiku doesn't support MCP tool search; switch to `claude --model sonnet` |

### AReaL Case Study (Vibe Coding 32天零手打代码)
Source: 知乎 https://zhuanlan.zhihu.com/p/2003269671630165191
GitHub: https://github.com/inclusionAI/AReaL

- 32天、178 session、72万行净增、零手打代码 — 用 Claude Code 从零构建分布式 RL 框架
- 分层配置架构：CLAUDE.md 精简入口 + rules/ + agents/ + skills/ + commands/
- Read 25,000次 >> Edit 14,000次 — agent 核心价值在于理解和导航，不是生成
- Evidence-driven：先设计验证方案再写代码，测试是你和 AI 之间的合同
- `/pr-review` 动态专家团队：根据 PR 内容自动组装专家团队，按风险分级分配不同模型并行审查
- Skill 升级为 Agent：不给 Write/Edit 权限，只做只读顾问 — 权限隔离原则

### Chinese Community Resources
- B站: Claude Code 使用技巧
- B站: Claude Code Skills 教程
- 知乎: Everything Claude Code 中文解析
- 知乎: Claude Code 深度使用指南
- Right.codes: Claude Code 最佳实践

### Related Tweets
- https://x.com/joooe453/status/2028028166435172725
- https://x.com/HiTw93/status/2032091246588518683 — Tw93 六层架构深度解析

---

## 6. Thariq Shihipar — Lessons from Building Claude Code: How We Use Skills

Source: @trq212 (Anthropic Claude Code 团队工程师, Skills 功能核心推动者)
X Article: https://x.com/dotey/status/2034002188994060691
宝玉翻译版, 原文: @trq212 2026-03-17

### Skills 九大分类 (Anthropic 内部几百个活跃 Skills 中提炼)

| # | 类别 | 说明 | 示例 |
|---|------|------|------|
| 1 | 库与 API 参考 | 正确使用某库/SDK，含踩坑点 | billing-lib, internal-platform-cli, frontend-design |
| 2 | 产品验证 | 搭配 Playwright/tmux 验证代码是否正常 | signup-flow-driver, checkout-verifier |
| 3 | 数据获取与分析 | 连接数据/监控体系 | funnel-query, cohort-compare, grafana |
| 4 | 业务流程与团队自动化 | 重复工作流自动化为一条命令 | standup-post, create-ticket, weekly-recap |
| 5 | 代码脚手架与模板 | 生成特定功能的框架样板代码 | new-workflow, new-migration, create-app |
| 6 | 代码质量与审查 | 执行代码质量标准，可作为 hook/GitHub Action | adversarial-review, code-style, testing-practices |
| 7 | CI/CD 与部署 | 拉取、推送、部署 | babysit-pr, deploy-service, cherry-pick-prod |
| 8 | 运维手册 | 现象→多工具排查→结构化报告 | service-debugging, oncall-runner, log-correlator |
| 9 | 基础设施运维 | 日常维护，含破坏性操作安全护栏 | orphans-cleanup, dependency-management, cost-investigation |

### 核心写 Skill 技巧

- **不要说显而易见的事** — Claude 对代码库已经很了解，重点放在能打破 Claude 常规思维的信息上
- **建踩坑点(gotchas)章节** — Skill 中信息量最大的部分，根据常见失败点持续积累
- **利用文件系统与渐进式披露** — Skill 是文件夹不只是 markdown，用 references/、assets/、scripts/ 子目录按需加载
- **不要限制太死** — 给信息但留灵活性，避免指令过于具体
- **考虑初始设置** — 用 config.json 存用户配置，未设置时自动询问
- **description 写「何时触发」而非「做什么」** — Claude 通过 description 判断该不该调用
- **记忆与数据存储** — 用 log/JSON/SQLite 存历史数据，使用 ${CLAUDE_PLUGIN_DATA} 稳定目录
- **存脚本与生成代码** — 给 Claude 代码库让它专注编排，而非重造样板
- **按需钩子(On Demand Hooks)** — Skills 可注册只在调用时激活的 hook（如 /careful 拦截危险操作, /freeze 限制编辑范围）

### 分发与管理

- 小团队: 提交到 `./.claude/skills`
- 大规模: 内部插件市场 (Plugin Marketplace)
- 自然涌现: 沙盒 → Slack 推荐 → 获得关注 → PR 到市场
- 效果衡量: PreToolUse hook 记录 Skill 使用频率
- 组合 Skills: 直接按名字引用其他 Skills，已安装即可调用

---

## 7. 胡渊鸣 — 如何有效地给 10 个 Claude Code 打工

Source: 胡渊鸣 (Meshy AI CEO, 清华姚班 → MIT PhD)
URL: https://zhuanlan.zhihu.com/p/2007147036185744607
Date: 2026-03-10

### 核心主题
从单线程 Cursor Agent 到多实例并行 Claude Code 的基建演进路线，10 个阶段逐步提高 Agentic Coding 吞吐量。

### 10 个阶段摘要

| # | 阶段 | 关键点 |
|---|------|--------|
| 1 | Cursor → Claude Code | 去掉 GUI 依赖，iPhone SSH 随时派活，可编码时间 8h → 24h |
| 2 | Container + `--dangerously-skip-permissions` | EC2 隔离环境，全权限开放，单 prompt 连续跑 5 分钟 |
| 3 | Ralph Loop | 任务队列 + 自动重启：CC 干完一个活自动拉下一个，列表不空就不停 |
| 4 | Git Worktree 并行 | 同 repo 开 5 个 worktree，每个跑独立 CC，实现 1 分钟 1 commit |
| 5 | CLAUDE.md + PROGRESS.md | CLAUDE.md = 项目规则；PROGRESS.md = 经验教训沉淀，"同样的错误下次不要再犯" |
| 6 | Web Manager 取代 SSH | `claude -p` 非交互模式 + Python subprocess 调度 → 手机端网页操控 |
| 7 | CC 管 CC | `--output-format stream-json --verbose` 让 manager CC 读取 worker JSON log，诊断调优，成功率 20% → 95% |
| 8 | 语音输入 | 各输入框加语音识别 API，走路/开车/吃饭时也能派活 |
| 9 | Plan Mode 封装 | 在 web manager 中封装 Plan Mode，批量 kick off + 统一 review |
| 10 | 不看代码 | "Context, not control" — 只写 CLAUDE.md，不 review 实现代码，专注提问质量和目标定义 |

### 我们 playbook 可借鉴的点

**已覆盖：** CLAUDE.md、Plan Mode、Git Worktree（Boris Tip #1）、Subagent
**未覆盖：**
- Ralph Loop（任务队列驱动连续执行） vs 我们的 `/loop`（定时轮询）— 完全不同的模式
- `claude -p` 非交互式 API — CC 作为可编程组件的用法
- CC-管-CC meta-orchestration — 跨进程 agent 编排
- PROGRESS.md 经验沉淀 — 项目级教训积累文件
- "不看代码"管理哲学 — 使用心法层面的内容

---

## 8. Completed Demos
- Slides demo: https://freemty.github.io/steam-steel-infinite-minds.html
