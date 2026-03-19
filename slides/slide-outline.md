# Slide Outline: cc-research-playbook

Style: Academic Light (Anthropic-inspired) — preview at slides/theme-preview.html
Target: 25 slides (ZH primary, EN parallel)

---

## Opening (1 slide)

### Slide 1: Title
- "CC Research Playbook"
- Subtitle: "AI Researcher 的 CLI Agent 实践指南"
- Author: sum_young / Date: 2026-03-16

---

## Part 1: 范式与核心概念 (2 slides)

### Slide 2: 范式之争 — Same Model, Different Harness
- Cursor、Codex、Claude Code 底层使用相同模型 — 能力差异来自 harness 设计
- 左: IDE 内嵌助手 — 单轮问答、文本生成、作用于当前文件
- 右: CLI Agent (ReAct Loop) — 自主循环 plan→act→verify、工具调用、跨项目感知
- 金句: "The model didn't change. The harness around it did."
- 引用: [1] Anthropic Harness ↗ [2] OpenAI Harness Engineering ↗

### Slide 3: Context is All You Need
- 核心论点: CLI Agent 的一切工程化手段，都围绕 context 展开
- 三列: Input (feed context) / Output (efficient decisions) / Management (keep agent clear-headed)
- 底部: Skills, Hooks, Sub-Agent, MCP — all serve one purpose: engineering the context
- 引用: [3] Anthropic Context Engineering ↗ [4] Manus Context Engineering ↗

---

## Part 2: 实践篇 (18 slides)

### Slide 4: Motivation — 现状
- CLI Agent 生态快速迭代，每周都在变
- 左: Community Voices — @bcherny ↗, @trq212 ↗, @systematicls ↗, @HiTw93 ↗, 胡渊鸣 ↗, AReaL ↗
- 右: THE PROBLEM (不知道从哪里开始) + OUR APPROACH (围绕 Context 理解工具角色)

### Slide 5: Features Serve Context (callback)
- Skills/Hooks/Sub-agent/Loop 不是凭空出现，而是服务于 context 三维度
- 三列 Input/Output/Management 各对应具体工具
- 底部: 介绍顺序 Skills → Hooks → Sub-agents → Loop

### Slide 6: Skills — 可复用工作流的分发单元
- 左: What is a Skill? + Anthropic 内部几百个活跃 Skills
- 右: Popular Skills (全部带 ↗ 链接) — notion-lifeos, frontend-design, proactive-agent, hf-paper-pages, superpowers
- 本质: 工作流的可重复化分发

### Slide 7: Skills 对研究者的价值 + 最佳实践
- 01: Context 满了 → 整理成 Skill
- 02: 重复 Workflow → 一键 Skill，持续迭代
- 03: 告别漫长 Prompt，维护 Skill 即可
- 底部 Tips: description=触发条件 / gotchas=最有价值 / 渐进式披露
- 引用: @trq212 ↗ + code.claude.com/docs/en/skills ↗

### Slide 8: 新的重复劳动 (Hook 引入)
- Claude Code 消灭了写代码的重复劳动，但践行 Best Practice 本身又成了新的重复劳动
- 左: 5 个常见的"忘了做" — worktree/Skill 整理/commit 规范/push review/console.log
- 右: 不一致 + 讽刺 ("管理 AI 又制造了新的重复劳动")

### Slide 9: Hooks — 确定性消灭重复劳动
- 官方文档引用: "user-defined shell commands, HTTP endpoints, or LLM prompts..."
- 左: 4 handler types (command/http/prompt/agent)
- 右: 8+ key events (SessionStart, PreToolUse, PostToolUse, Stop, PreCompact, SubagentStart, UserPromptSubmit, ConfigChange)
- 底部: matcher 正则 / exit code 机制 / 三层配置
- 引用: code.claude.com/docs/en/hooks ↗

### Slide 10: Hook 实践案例
- 左: 4 个日常 Hook (git push 审查 / 自动格式化 / console.log 审计 / Skill 沉淀提醒)
- 右: Case — 实验管理 (exp{NN}{x}/ 目录结构 + SessionStart/PostToolUse/Stop 自动化)

### Slide 11: Hook 如何服务 Context 三维度
- Input: Stop 检测大量编辑 → 沉淀为 Skill
- Output: PostToolUse 自动推进 pipeline → 生成报告
- Manage: PreCompact 保存状态到 state.json
- 底部: 实验 pipeline (new-exp → scaffold → run → analyze → summary → commit)

### Slide 12: Sub-agent — Context Isolation 的功能分区
- 问题: 读论文会污染 coding context
- 左: Without isolation (context 被淹没) → 右: With subagents (功能分区)
- 底部: "专有 agent 获取专有 memory — 主 context 干净，也能获取之前 session 的 context"

### Slide 13: Sub-agent 研究场景
- 三列: Paper Reader (读论文→沉淀 repo) / Background Monitor (loop+tmux) / Experiment Manager (生命周期)
- 底部: Main Context spawn → 三个 agent 的树状关系
- 引用: code.claude.com/docs/en/sub-agents ↗ + AReaL 知乎 ↗

### Slide 14: Loop — 循环自主执行
- /loop 5m <command>
- 用例: 训练监控 / 实验轮询 / CI 观察 / 资源监控
- 引用: code.claude.com/docs/en/cli-reference ↗

### Slide 15: Superpowers — Context is All You Need, in Practice
- 三列 callback: Input (Brainstorming 产生丰富 context) / Output (Sub-agent 驱动输出) / Management (落盘为文档)
- 底部: 完整链路 Brainstorming → Spec → Plan → Worktree → TDD → Review → Verify & Merge
- 引用: github.com/obra/superpowers ↗

### Slide 16: Think — Brainstorming → Spec → Plan
- 左: Brainstorming (逐个提问、2-3 方案、逐节确认) → Output: spec.md
- 右: Writing Plans (映射文件、拆分任务、reviewer 审查) → Output: plan.md
- 底部: "所有思考过程落盘为文档 — 跨 session 永不丢失"

### Slide 17: Build & Verify — Execute → Review → Merge
- 左: Execute (git worktree + subagent 并行 + TDD) + Review (双重审查: spec + 代码质量)
- 右: Verify (无证据不完成) + Finish (4 种路径: Merge/PR/Keep/Discard)

### Slide 18: Labmate — Context is All You Need, Fully Realized
- 三列 recall: Input (专有 Agent 喂 context) / Output (Skill 驱动标准化输出) / Management (知识进 repo)
- 底部: claude plugin install freemty/labmate → 7 agents + 7 skills + 5 hooks
- 引用: github.com/freemty/labmate ↗

### Slide 19: Labmate — 研究工作流 Demo
- 左: 目录架构树 (CLAUDE.md / agents / skills / hooks / exp{NN}{x} / pipeline-state.json)
- 右: 5 步完整循环 (/new-experiment → run → /analyze → /commit → /update-project-skill → repeat)
- 底部三条设计原则: agent 最小权限 / hook 只提醒不拦截 / 所有知识进 repo
- 引用: github.com/freemty/labmate ↗ | PostTrainBench first user

---

## Part 3: 实用技巧 (3 slides)

### Slide 20: CLAUDE.md 最佳实践
- DO: 构建命令 / 代码风格 / 测试指南 / 架构决策 / IF-ELSE 逻辑目录→Skills
- DON'T: Claude 能推断的 / 标准惯例 / 详细 API 文档 / 频繁变化配置 / 百科全书式罗列
- 优先级: Hooks > CLAUDE.md (100%) / Skills > CLAUDE.md (按需) / Token 预算 <200 行
- 引用: code.claude.com/docs/en/best-practices ↗

### Slide 21: Key Tips 精选
- 左 WORKFLOW: git worktree 并行 / Plan Mode 先行 / "use subagents" / 定义终点
- 右 DISCIPLINE: 纠正后更新 CLAUDE.md / 日常操作→Skills / 利用讨好倾向 / 定期清理
- 引用: @bcherny ↗ + @systematicls ↗

### Slide 22: 常见失败模式
- 5 行表格: 厨房水槽 Session / 反复纠正 / CLAUDE.md 过长 / 信任验证差距 / 无限探索
- 底部: "所有失败模式的根因都是同一个：context 管理失控"
- 引用: code.claude.com/docs/en/best-practices ↗

---

## Closing (3 slides)

### Slide 23: Mindset — The Meta Layer
- Ivan Zhao 金句: "Steel. Steam. Infinite minds. The next skyline is there, waiting for us to build it."
- 左: 每当 AI 能做一件事，我们往上跳一层 — Meta 层面思考
- 右: Case — Labmate 正在加速 Language Model Prompting Agent 训练
- 底部: "Scalable 自我觉察：Agent 维护着让自己随时间变聪明的基础设施"
- 引用: Ivan Zhao, "Steam, Steel, and Infinite Minds" ↗

### Slide 24: 参考阅读
- 左上 HARNESS ENGINEERING: Anthropic ×2 ↗, OpenAI ↗, Manus ↗, Ivan Zhao ↗ (全部可点击)
- 左下 OFFICIAL DOCS: overview / hooks / skills / sub-agents / memory (全部可点击)
- 右上 KEY PEOPLE: @trq212 ↗, @bcherny ↗, @systematicls ↗, @HiTw93 ↗, AReaL ↗ (全部可点击)
- 右下 GITHUB: freemty/labmate ↗, obra/superpowers ↗, anthropics/claude-code ↗, inclusionAI/AReaL ↗, huggingface/skills ↗

### Slide 25: End
- "Questions?"
- 金句: "We want humans to supervise the loops from a leveraged point, not be in them." — Ivan Zhao
- @sum_young | 2026-03-16 | github.com/freemty/labmate
