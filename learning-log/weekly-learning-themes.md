# 45天 AI Agent 学习计划：每周主题地图

用途：把 45 天计划按周整理成学习节奏。  
目标：每周都有一个清晰主题，知道这一周大概在学什么、为什么学、最后要产出什么。

---

## 第 1 周：大模型底层直觉入门

覆盖时间：Day 1-7

本周主题：

```text
从“AI 好像会说话”转向“LLM 是围绕 token 工作的预测系统”。
```

这一周主要解决的问题：

- 大模型到底是怎么处理一句话的？
- token、embedding、attention 分别是什么？
- 为什么模型能根据上下文生成内容？
- RAG 里最基础的 embedding 检索是怎么来的？

本周学习内容：

- Day 1：Token、Embedding 与 LLM 全景
- Day 2：Self-Attention 与 QKV
- Day 3：PyTorch、Shape 与 Mini Transformer 骨架
- Day 4：最小字符级语言模型
- Day 5：残差连接与 LayerNorm
- Day 6：Tokenizer 与上下文成本
- Day 7：Embedding 与语义检索

本周关键词：

```text
token
embedding
self-attention
Q/K/V
shape
next token prediction
residual connection
context window
semantic search
```

本周最终要形成的理解：

```text
大模型不是魔法，而是先把文本切成 token，把 token 变成向量，用 attention 处理上下文，再不断预测下一个 token。
```

本周产出物：

- tokenizer 对比实验
- NumPy attention 实验
- PyTorch attention shape 理解
- 字符级语言模型实验
- embedding 检索 demo
- 第一阶段底层概念笔记

---

## 第 2 周：上下文、生成与模型使用边界

覆盖时间：Day 8-14

本周主题：

```text
理解模型生成为什么有成本、有边界，以及如何更稳定地控制模型行为。
```

这一周主要解决的问题：

- 为什么长上下文会慢、会贵？
- KV Cache 到底解决了什么？
- 为什么同一个 prompt 有时稳定、有时发散？
- Agent API 里的 messages 是怎么组织的？
- system prompt、few-shot、CoT 怎么让模型更可控？

本周学习内容：

- Day 8：KV Cache 与长上下文成本
- Day 9：采样策略
- Day 10：第一阶段复盘
- Day 11：Messages 与 API Payload
- Day 12：上下文管理
- Day 13：System Prompt 工程
- Day 14：Few-Shot 与推理提示

本周关键词：

```text
KV Cache
prefill
decode
temperature
top-p
top-k
messages
system prompt
context manager
few-shot
CoT
```

本周最终要形成的理解：

```text
模型不是只靠一句 prompt 工作，而是依赖 messages、上下文窗口、采样参数和提示策略共同决定输出效果。
```

本周产出物：

- KV Cache 图文笔记
- 采样策略实验
- 第一阶段复盘文章
- messages API 调用脚本
- context manager 初版
- system prompt 对比记录
- few-shot 小评测

---

## 第 3 周：Agent 核心能力闭环

覆盖时间：Day 15-21

本周主题：

```text
从“会聊天的模型”走向“能调用工具、检索知识、循环行动的 Agent”。
```

这一周主要解决的问题：

- 模型如何调用外部工具？
- function calling 和真正执行工具有什么区别？
- RAG 如何让 Agent 使用外部知识？
- ReAct 为什么能让 Agent 看起来会自主推进任务？
- memory 和 eval 为什么是 Agent 工程里的关键？

本周学习内容：

- Day 15：Function Calling 入门
- Day 16：Tool Runtime
- Day 17：RAG 索引
- Day 18：RAG 问答链路
- Day 19：ReAct Loop
- Day 20：Memory
- Day 21：Agent Eval 初版

本周关键词：

```text
function calling
tool schema
tool runtime
RAG
chunking
retrieval
ReAct
memory
eval
success rate
token cost
```

本周最终要形成的理解：

```text
Agent 的能力不是模型自己凭空拥有的，而是由模型决策、工具执行、知识检索、记忆和评估共同组成。
```

本周产出物：

- 工具 schema
- tool dispatcher
- RAG index
- RAG QA
- 手写 ReAct loop
- memory 模块
- eval 测试集初版

---

## 第 4 周：个人助理 Agent 与多 Agent 架构

覆盖时间：Day 22-28

本周主题：

```text
把单点能力整合成个人助理 Agent，并开始理解多 Agent 如何分工协作。
```

这一周主要解决的问题：

- 如何把 chat、tools、RAG、memory、eval 串成一个完整 Agent？
- 什么时候需要多 Agent？
- orchestrator-worker 架构解决什么问题？
- subagent 应该怎么拆？
- skill registry 和三层架构如何帮助 Agent 产品化？
- LangGraph 如何用图管理 Agent 流程？

本周学习内容：

- Day 22：个人助理 Agent v1 整合
- Day 23：Orchestrator-Worker 架构
- Day 24：Subagent 设计原则
- Day 25：Skill Registry
- Day 26：感知-推理-执行三层架构
- Day 27：LangGraph 入门
- Day 28：LangGraph 重写个人助理

本周关键词：

```text
assistant agent
orchestrator
worker
subagent
skill registry
perception
reasoning
action
LangGraph
state
node
edge
```

本周最终要形成的理解：

```text
复杂 Agent 不是堆更多 prompt，而是通过模块边界、状态流转、工具能力和多角色协作来降低复杂度。
```

本周产出物：

- 个人助理 Agent v1
- 多 Agent 架构图
- subagent 设计笔记
- skill registry
- 三层架构文档
- LangGraph 最小 demo
- LangGraph 版个人助理 Agent

---

## 第 5 周：框架选择、AI 编程与毕业项目定题

覆盖时间：Day 29-35

本周主题：

```text
从学习框架和工具，转向确定自己的毕业项目，并跑通 MVP 核心链路。
```

这一周主要解决的问题：

- LangGraph、AutoGen、CrewAI 应该怎么选？
- AI 编程工具如何进入自己的工作流？
- Vibe Coding 的正确用法是什么？
- 毕业项目应该解决什么问题？
- 如何把项目从想法拆成架构？
- MVP 最短路径是什么？

本周学习内容：

- Day 29：Agent 框架对比
- Day 30：多 Agent 阶段复盘
- Day 31：AI 编程工具与工作流
- Day 32：Vibe Coding 方法论
- Day 33：毕业项目 PRD
- Day 34：毕业项目架构
- Day 35：毕业项目核心链路

本周关键词：

```text
LangGraph
AutoGen
CrewAI
AI coding
Vibe Coding
PRD
MVP
architecture
core flow
capstone
```

本周最终要形成的理解：

```text
框架和工具不是目标，真正的目标是选定一个能落地的毕业项目，并先跑通从用户输入到最终输出的最小闭环。
```

本周产出物：

- Agent 框架对比表
- 多 Agent 阶段复盘
- AI 编程工具对比
- Vibe Coding 模板
- 毕业项目 PRD
- 毕业项目架构图
- MVP 核心链路代码

---

## 第 6 周：毕业项目产品化与工程化

覆盖时间：Day 36-42

本周主题：

```text
让毕业项目从“能跑”变成“能用、能观察、能评估、能稳定运行”。
```

这一周主要解决的问题：

- 项目如何提供可使用入口？
- 如何观察 Agent 每一步做了什么？
- 如何计算每次运行的 token 和成本？
- prompt 如何版本化？
- 如何判断项目质量？
- 工具失败、检索为空、格式错误时怎么办？

本周学习内容：

- Day 36：CLI 或 Web UI
- Day 37：日志与 Trace
- Day 38：成本控制
- Day 39：Prompt 版本管理
- Day 40：垂直应用阶段复盘
- Day 41：Eval 完善
- Day 42：失败处理与稳定性

本周关键词：

```text
CLI
Web UI
trace
logging
cost tracking
prompt versioning
eval cases
failure handling
fallback
stability
```

本周最终要形成的理解：

```text
一个 Agent 项目不是只要能回答就够了，还要可使用、可观察、可控成本、可评估，并且能处理失败。
```

本周产出物：

- CLI 或 Web UI
- trace 日志
- cost tracker
- prompt 版本目录
- 阶段构建日志
- 扩展 eval 测试集
- failure handling 文档

---

## 第 7 周：作品集收官与公开表达

覆盖时间：Day 43-45

本周主题：

```text
把 45 天学习成果整理成可以展示、可以讲清楚、可以继续迭代的作品集。
```

这一周主要解决的问题：

- 如何用 3 分钟讲清楚毕业项目？
- 技术博客应该如何解释项目？
- GitHub 仓库如何从学习草稿变成作品集？
- 45 天之后下一阶段应该怎么继续？

本周学习内容：

- Day 43：Demo 脚本与录屏准备
- Day 44：技术博客
- Day 45：最终作品集交付

本周关键词：

```text
demo
storytelling
technical blog
portfolio
README
review
showcase
next plan
```

本周最终要形成的理解：

```text
学习的终点不是“我看完了”，而是“我做出了东西，并且能把它讲清楚”。
```

本周产出物：

- 3 分钟 Demo 脚本
- 项目录屏素材
- 毕业项目技术博客
- 最终仓库 README
- 45 天总复盘
- 下一阶段学习计划

---

## 一句话总览

```text
第 1 周：理解模型底层怎么处理文本。
第 2 周：理解模型生成、上下文和提示控制。
第 3 周：掌握 Agent 的工具、RAG、ReAct、记忆和评估。
第 4 周：整合个人助理 Agent，并理解多 Agent 架构。
第 5 周：选择框架和工具，确定毕业项目并跑通 MVP。
第 6 周：把项目工程化，补日志、成本、eval 和稳定性。
第 7 周：整理 Demo、博客和作品集，完成最终交付。
```

