# Subagent Demo: Needle in a Haystack

100 random noise images. One has a secret message hidden via LSB steganography.
Find it using parallel subagents.

## Setup

```bash
cd demos/subagent-needle
python generate_haystack.py
```

## Demo Prompt (paste into Claude Code)

```
在 demos/subagent-needle/haystack/ 目录下有 100 张图片。
其中有一张藏了 LSB 隐写信息，其余都是纯噪声。

请用并行 subagent 找出那张图。

检测方法：对每张图运行 python demos/subagent-needle/detect_lsb.py <path>
输出 "FOUND: ..." 表示找到，"CLEAN" 表示没有。

要求：
1. 把 100 张图分成 5 批，每批 20 张
2. 每批启动一个 subagent 并行检查
3. 汇总结果，告诉我是哪张图、隐写内容是什么
```

## What the Audience Sees

1. 5 subagents launch simultaneously
2. Each scans 20 images independently (isolated context)
3. One agent reports "FOUND" — the others report all clean
4. Main context stays clean — only receives the final answer
5. Total time: ~30s vs ~3min sequential

## Key Teaching Points

- **Parallel execution**: 5x speedup, real wall-clock difference
- **Context isolation**: Each agent only loads its 20-image batch
- **Dispatcher pattern**: Main context does zero scanning work
- **Fault tolerance**: If one agent fails, others still complete
