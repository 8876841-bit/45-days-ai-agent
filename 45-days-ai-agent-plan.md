# 45天AI技能体系化掌握打卡计划

目标：45天后交付一个可展示的 Agent 产品、Demo 视频、技术博客和 GitHub 作品集。

建议主线项目：个人助理 Agent。它会逐步集成 Tool Use、RAG、记忆、多 Agent、评估、成本追踪和可观测性。若你更想做 AI 视频方向，可在 Day 29 后把主线切到“AI视频自动化工作室”。

每日节奏：

- 理论：60分钟
- 编码：90分钟
- 笔记/复盘：30分钟
- GitHub：每天至少1次 commit

验收原则：

- 每天必须有一个可见输出物：代码、笔记、图、表、测试、Demo 之一
- 每个阶段必须有一篇总结文章
- 每个项目必须有 README、运行方式、截图或录屏

---

## 阶段一：底层地基 Day 1-10

目标：理解 LLM 的核心机制，知道应用开发中每个参数和概念背后的含义。

### Day 1：Transformer 全景

今日目标：知道 Transformer 为什么适合语言建模。

必学概念：Token、Embedding、Self-Attention、FFN、残差连接、LayerNorm。

编码任务：用 Python 写一个极简 token 统计脚本，统计中文、英文、代码文本的字符和词频。

验收标准：能画出 Transformer 数据流：文本 -> token -> embedding -> attention -> logits -> next token。

输出物：`notes/day01-transformer-overview.md`

Commit 建议：`docs: add transformer overview notes`

### Day 2：Self-Attention

今日目标：理解 Q、K、V 和注意力分数。

必学概念：QKV、点积相似度、softmax、缩放因子。

编码任务：用 NumPy 手写一个单头 attention 前向计算。

验收标准：输入 3 个 token 向量，输出 attention 权重矩阵和加权结果。

输出物：`experiments/day02_attention_numpy.py`

Commit 建议：`feat: implement numpy self attention`

### Day 3：PyTorch Mini Transformer 上半部分

今日目标：用 PyTorch 实现 Embedding、位置编码、多头注意力。

必学概念：nn.Embedding、Position Encoding、Multi-Head Attention。

编码任务：实现 `MiniMultiHeadAttention`。

验收标准：随机输入 batch 能跑通，输出 shape 正确。

输出物：`projects/mini_transformer/model.py`

Commit 建议：`feat: add mini transformer attention block`

### Day 4：PyTorch Mini Transformer 下半部分

今日目标：跑通一个字符级语言模型。

必学概念：causal mask、cross entropy、next token prediction。

编码任务：训练一个极小字符模型，使用任意短文本数据。

验收标准：loss 能下降，模型能生成一小段文本。

输出物：`projects/mini_transformer/train.py`

Commit 建议：`feat: train character mini transformer`

### Day 5：残差网络与跳连接

今日目标：理解残差连接为什么能改善深层网络训练。

必学概念：梯度消失、identity mapping、ResNet block。

编码任务：实现一个简化 ResNet block，并和普通 MLP block 对比 loss。

验收标准：能解释 residual connection 在 Transformer 中的作用。

输出物：`notes/day05-residual-connection.md`

Commit 建议：`docs: explain residual connections`

### Day 6：Tokenizer

今日目标：理解模型为什么不是直接读文字。

必学概念：BPE、SentencePiece、token id、vocab。

编码任务：用 tokenizer 对中文、英文、代码、emoji 做切分对比。

验收标准：整理一张表，说明不同文本的 token 数差异。

输出物：`experiments/day06_tokenizer_compare.py`

Commit 建议：`feat: compare tokenizer behavior`

### Day 7：Embedding 与语义空间

今日目标：理解向量表示和相似度检索。

必学概念：Embedding、cosine similarity、nearest neighbor。

编码任务：构造一组句子 embedding，做相似句检索。

验收标准：输入一个 query，能返回最相近的 3 句话。

输出物：`experiments/day07_embedding_search.py`

Commit 建议：`feat: add embedding similarity demo`

### Day 8：KV Cache 与上下文窗口

今日目标：理解长上下文和推理速度的关系。

必学概念：prefill、decode、KV cache、context window。

编码任务：写一篇图文笔记，解释为什么长对话会越来越贵。

验收标准：能说清楚 KV cache 解决了什么，没有解决什么。

输出物：`notes/day08-kv-cache.md`

Commit 建议：`docs: explain kv cache and context window`

### Day 9：采样策略

今日目标：理解 temperature、top-p、top-k 如何影响输出。

必学概念：logits、概率分布、temperature、top-p、top-k、beam search。

编码任务：写一个模拟采样器，对同一 logits 用不同参数采样。

验收标准：输出对比表，说明稳定性和创造性的变化。

输出物：`experiments/day09_sampling.py`

Commit 建议：`feat: add sampling strategy demo`

### Day 10：阶段复盘

今日目标：把底层概念串成一篇完整文章。

编码任务：整理前 9 天代码和笔记，补 README。

验收标准：写出《Transformer 是如何读懂我说的话的》。

输出物：`blog/01-how-transformer-understands-text.md`

Commit 建议：`docs: add stage one review`

---

## 阶段二：Agent 核心机制 Day 11-22

目标：不用框架也能写一个可运行 Agent，掌握 messages、tool use、RAG、ReAct、memory。

### Day 11：Messages 与 API Payload

今日目标：理解 system、user、assistant、tool 的职责。

编码任务：写一个最小 API 调用脚本，打印 raw request 和 raw response。

验收标准：能解释一次完整对话请求的结构。

输出物：`projects/assistant_agent/day11_basic_chat.py`

Commit 建议：`feat: add basic chat api script`

### Day 12：上下文管理

今日目标：学会控制上下文长度。

编码任务：实现一个 context manager，支持 token 估算、截断、摘要占位。

验收标准：超过阈值时能保留 system、最近消息和摘要。

输出物：`projects/assistant_agent/context_manager.py`

Commit 建议：`feat: implement context manager`

### Day 13：System Prompt 工程

今日目标：掌握角色、边界、格式、失败策略。

编码任务：设计 3 个 system prompt，对同一任务做输出对比。

验收标准：写出对比结论：哪个更稳定，为什么。

输出物：`notes/day13-system-prompt-ablation.md`

Commit 建议：`docs: compare system prompts`

### Day 14：Few-Shot 与推理提示

今日目标：理解例子比抽象要求更能约束模型。

编码任务：在分类、抽取、数学题各做一组 zero-shot vs few-shot 对比。

验收标准：输出简单评测表。

输出物：`experiments/day14_fewshot_eval.py`

Commit 建议：`feat: add few shot evaluation`

### Day 15：Function Calling 入门

今日目标：理解 JSON Schema 和工具调用协议。

编码任务：定义 `get_weather` 和 `calculate` 两个工具 schema。

验收标准：模型能根据用户请求选择正确工具。

输出物：`projects/assistant_agent/tools.py`

Commit 建议：`feat: define first tool schemas`

### Day 16：Tool Use 执行器

今日目标：把模型工具调用和本地函数执行连起来。

编码任务：实现 tool dispatcher，支持多工具注册和调用结果回传。

验收标准：一次对话中能完成“计算 + 查询模拟天气”。

输出物：`projects/assistant_agent/tool_runtime.py`

Commit 建议：`feat: implement tool runtime`

### Day 17：RAG 基础

今日目标：理解 chunking、embedding、retrieval。

编码任务：把自己的 5 篇笔记切块并建立向量索引。

验收标准：输入问题能返回相关 chunk。

输出物：`projects/assistant_agent/rag_index.py`

Commit 建议：`feat: build local rag index`

### Day 18：RAG 问答链路

今日目标：把检索结果塞回模型上下文。

编码任务：实现 retrieve -> prompt assemble -> answer。

验收标准：回答必须引用检索到的笔记片段。

输出物：`projects/assistant_agent/rag_qa.py`

Commit 建议：`feat: implement rag qa flow`

### Day 19：ReAct Loop

今日目标：理解 Thought -> Action -> Observation 循环。

编码任务：不用框架，手写一个 150 行以内 ReAct loop。

验收标准：Agent 能连续调用 2 次工具后给最终答案。

输出物：`projects/assistant_agent/react_loop.py`

Commit 建议：`feat: add handwritten react loop`

### Day 20：记忆机制

今日目标：区分短期记忆、长期记忆和反思。

编码任务：给 Agent 加入 conversation buffer 和 preference memory。

验收标准：用户说“记住我喜欢简洁回答”后，后续回答风格变化。

输出物：`projects/assistant_agent/memory.py`

Commit 建议：`feat: add assistant memory`

### Day 21：Agent 评估初版

今日目标：不要只靠感觉判断 Agent 好不好。

编码任务：写 10 条测试用例，记录成功率、token、延迟。

验收标准：运行一次 eval 生成 JSON 或 CSV 结果。

输出物：`projects/assistant_agent/evals.py`

Commit 建议：`feat: add basic agent evals`

### Day 22：阶段二整合

今日目标：交付个人助理 Agent v1。

编码任务：整合 chat、context、tools、RAG、memory、eval。

验收标准：README 能指导别人本地运行。

输出物：`projects/assistant_agent/README.md`

Commit 建议：`docs: document assistant agent v1`

---

## 阶段三：多 Agent 架构 Day 23-30

目标：理解复杂 Agent 系统如何拆分、调度、通信和评估。

### Day 23：Orchestrator-Worker

今日目标：理解主控 Agent 和执行 Agent 的边界。

编码任务：把个人助理拆成 planner、researcher、executor 三个角色。

验收标准：画出架构图并说明每个角色的输入输出。

输出物：`docs/architecture/orchestrator-worker.md`

Commit 建议：`docs: add orchestrator worker architecture`

### Day 24：Subagent 拆分原则

今日目标：知道什么时候该拆 Agent，什么时候不该拆。

编码任务：为 5 个任务设计单 Agent 和多 Agent 两种方案。

验收标准：总结拆分带来的成本、延迟和稳定性变化。

输出物：`notes/day24-subagent-design.md`

Commit 建议：`docs: summarize subagent design principles`

### Day 25：Skill Registry

今日目标：理解 Skill 如何注册、发现和调用。

编码任务：设计一个 10 个技能的 registry，包括名称、描述、输入、输出。

验收标准：planner 能根据任务选择合适 skill。

输出物：`projects/assistant_agent/skill_registry.py`

Commit 建议：`feat: add skill registry`

### Day 26：感知-推理-执行三层架构

今日目标：把 Agent 系统拆成信息输入、决策、动作执行。

编码任务：重构项目目录，标出 perception、reasoning、action 层。

验收标准：架构图中每层职责清楚，没有互相乱调用。

输出物：`docs/architecture/perception-reasoning-action.md`

Commit 建议：`docs: add three layer agent architecture`

### Day 27：LangGraph 入门

今日目标：理解 graph、node、edge、state。

编码任务：用 LangGraph 实现一个最小 planner -> tool -> answer 流程。

验收标准：能可视化或打印 graph 执行路径。

输出物：`projects/langgraph_agent/minimal_graph.py`

Commit 建议：`feat: add minimal langgraph agent`

### Day 28：LangGraph 重写个人助理

今日目标：把阶段二 Agent 改造成 graph 结构。

编码任务：实现 RAG node、tool node、memory node、answer node。

验收标准：同一 eval 集能跑通。

输出物：`projects/langgraph_agent/agent_graph.py`

Commit 建议：`feat: port assistant agent to langgraph`

### Day 29：框架横向对比

今日目标：理解 LangGraph、AutoGen、CrewAI 的差异。

编码任务：做一张对比表：状态管理、可控性、多 Agent、调试、适用场景。

验收标准：能说明你为什么主线项目选择 LangGraph 或不用框架。

输出物：`blog/02-agent-framework-comparison.md`

Commit 建议：`docs: compare agent frameworks`

### Day 30：多 Agent 阶段复盘

今日目标：交付个人助理 Agent v2。

编码任务：补全 README、架构图、eval 结果。

验收标准：有 v1/v2 对比：能力、成本、延迟、复杂度。

输出物：`projects/langgraph_agent/README.md`

Commit 建议：`docs: document assistant agent v2`

---

## 阶段四：垂直应用实战 Day 31-40

目标：选择一个方向深入，不做工具观光。

推荐选择 A 或 B：

- A：AI个人助理产品化
- B：AI视频自动化工作室

### Day 31：AI 编程工具对比

今日目标：理解 Claude Code、Cursor、Windsurf、Codex 的工作流差异。

编码任务：用同一个小需求分别设计 4 种 AI 编程流程。

验收标准：总结每种工具适合的场景。

输出物：`notes/day31-ai-coding-tools.md`

Commit 建议：`docs: compare ai coding workflows`

### Day 32：Vibe Coding 方法论

今日目标：建立“人定方向、AI做实现、人做校准”的节奏。

编码任务：把一个需求拆成 prompt、验收标准、测试用例、迭代记录。

验收标准：形成自己的 AI 编程模板。

输出物：`templates/vibe-coding-task-template.md`

Commit 建议：`docs: add vibe coding task template`

### Day 33：产品方向选择

今日目标：确定毕业项目。

编码任务：写项目 PRD，包括用户、场景、核心功能、非目标、验收标准。

验收标准：PRD 不超过 2 页，范围清晰可完成。

输出物：`capstone/PRD.md`

Commit 建议：`docs: add capstone prd`

### Day 34：MVP 架构设计

今日目标：把毕业项目拆成可实现模块。

编码任务：画系统架构图，列 API、数据结构、工具列表。

验收标准：每个模块都有输入、输出和失败处理。

输出物：`capstone/architecture.md`

Commit 建议：`docs: add capstone architecture`

### Day 35：MVP 核心链路

今日目标：跑通最小可用流程。

编码任务：实现用户输入 -> Agent 决策 -> 工具/RAG -> 最终输出。

验收标准：至少 3 个真实案例跑通。

输出物：`capstone/src/`

Commit 建议：`feat: implement capstone core flow`

### Day 36：界面或 CLI

今日目标：让项目能被别人使用。

编码任务：做一个 CLI、Web UI 或简单本地页面。

验收标准：README 中一条命令能启动。

输出物：`capstone/README.md`

Commit 建议：`feat: add capstone user interface`

### Day 37：工程化：日志与 Trace

今日目标：让 Agent 的行为可观察。

编码任务：记录每轮输入、模型输出、工具调用、耗时、token。

验收标准：一次运行能生成 trace 文件。

输出物：`capstone/traces/`

Commit 建议：`feat: add tracing and logs`

### Day 38：工程化：成本控制

今日目标：知道一次任务花了多少钱。

编码任务：统计 prompt tokens、completion tokens、总成本。

验收标准：输出每次运行的成本报告。

输出物：`capstone/src/cost_tracker.py`

Commit 建议：`feat: add cost tracking`

### Day 39：工程化：Prompt 版本管理

今日目标：让 prompt 可迭代、可回滚、可对比。

编码任务：把 prompt 从代码中抽离为版本化文件。

验收标准：eval 能对比 v1/v2 prompt 的效果。

输出物：`capstone/prompts/`

Commit 建议：`feat: version capstone prompts`

### Day 40：垂直应用复盘

今日目标：毕业项目进入可展示状态。

编码任务：修 bug、补 README、补案例、补截图。

验收标准：陌生人能按 README 运行 Demo。

输出物：`blog/03-capstone-build-log.md`

Commit 建议：`docs: add capstone build log`

---

## 阶段五：综合交付 Day 41-45

目标：把项目从“能跑”变成“能展示、能解释、能复盘”。

### Day 41：Eval 完善

今日目标：让项目有可信的质量指标。

编码任务：扩展到至少 30 条 eval case。

验收标准：输出成功率、失败分类、改进建议。

输出物：`capstone/evals/`

Commit 建议：`test: expand capstone eval cases`

### Day 42：失败处理与边界条件

今日目标：提升稳定性。

编码任务：处理工具失败、检索为空、模型格式错误、超时。

验收标准：异常不会直接中断用户流程。

输出物：代码改动 + `capstone/docs/failure-handling.md`

Commit 建议：`fix: improve capstone failure handling`

### Day 43：Demo 脚本

今日目标：准备展示叙事。

编码任务：写 3 分钟 Demo 脚本：问题、方案、演示、技术亮点、结果。

验收标准：照脚本能顺畅录屏。

输出物：`capstone/demo-script.md`

Commit 建议：`docs: add capstone demo script`

### Day 44：技术博客

今日目标：写一篇能展示能力的长文。

编码任务：完成毕业项目技术博客。

验收标准：包含架构图、关键代码、踩坑、eval 结果、下一步。

输出物：`blog/04-capstone-technical-review.md`

Commit 建议：`docs: add capstone technical review`

### Day 45：最终交付

今日目标：完成作品集。

编码任务：整理仓库首页 README、项目列表、Demo 链接、学习路线复盘。

验收标准：仓库像一个可展示的作品集，而不是学习草稿。

输出物：`README.md`

Commit 建议：`docs: finalize 45 days ai portfolio`

---

## 每周复盘问题

每 7 天回答一次：

1. 这一周我真正理解了什么？
2. 哪个概念我只是“听过”，还没能讲清楚？
3. 哪段代码最值得保留进作品集？
4. 哪个任务消耗时间最多，为什么？
5. 下周要减少什么，强化什么？

---

## 推荐仓库结构

```text
45-days-ai-agent/
  README.md
  notes/
  blog/
  experiments/
  projects/
    mini_transformer/
    assistant_agent/
    langgraph_agent/
  capstone/
    README.md
    PRD.md
    architecture.md
    src/
    prompts/
    evals/
    traces/
    docs/
  templates/
```

---

## 最小成功标准

如果时间紧，至少完成这些：

- Day 1-10：理解 token、attention、context、sampling
- Day 15-22：完成个人助理 Agent v1
- Day 27-30：用 LangGraph 重构一次
- Day 33-40：完成一个毕业项目 MVP
- Day 41-45：补 eval、Demo、博客、README

最高优先级不是“学完所有工具”，而是交付一个能讲清楚技术取舍、能演示、能运行、能复盘的作品。
