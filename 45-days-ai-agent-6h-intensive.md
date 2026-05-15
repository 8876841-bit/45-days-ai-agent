# 45天AI Agent高强度训练计划：每天6小时版

目标：45天后形成一个可展示的 AI Agent 作品集，包括可运行项目、技术博客、Demo 视频、评估结果和完整 GitHub 仓库。

每日固定节奏：

| 时间 | 模块 | 目的 |
|---|---|---|
| 09:00-10:20 | 理论输入 | 建立当天核心概念 |
| 10:20-10:35 | 休息 | 离屏、喝水、走动 |
| 10:35-12:00 | 拆解与小实验 | 用小代码验证概念 |
| 12:00-13:30 | 午餐休息 | 不看教程，给大脑整理时间 |
| 13:30-15:00 | 主项目编码 | 把知识接进主线项目 |
| 15:00-15:15 | 休息 | 离屏 |
| 15:15-16:30 | Debug / 扩展 / 对比 | 修问题、做实验、加功能 |
| 16:30-16:45 | 休息 | 清空注意力 |
| 16:45-17:30 | 笔记与复盘 | 写当天总结、提交代码 |

每天必须产出：

- 一份代码、笔记、图表、评估结果或 Demo
- 一次 GitHub commit
- 一段 5-10 行复盘：今天学会什么、卡在哪里、明天怎么处理

---

## Day 1：AI Agent 全景与 Transformer 直觉

今日目标：知道从 Transformer 到 Agent 的完整链路。

09:00-10:20 理论输入：

- 看 3Blue1Brown Transformer 可视化视频
- 理解 Token、Embedding、Attention、Logits、Sampling
- 记住一句话：LLM 是根据上下文预测下一个 token 的概率机器

10:35-12:00 小实验：

- 安装 Python 依赖：`openai`、`tiktoken`
- 用 tokenizer 对中文、英文、代码做切分
- 记录不同文本的 token 数差异

13:30-15:00 主项目：

- 创建仓库结构
- 新建 `notes/`、`experiments/`、`projects/`、`blog/`
- 写第一份全景笔记

15:15-16:30 扩展：

- 画一张链路图：文本 -> token -> embedding -> attention -> logits -> sampling -> response
- 写出每一步对应用开发的影响

16:45-17:30 复盘：

- 写《Day 1：我如何理解 LLM 的工作流》
- commit：`docs: add llm overview notes`

验收标准：能用 3 分钟讲清楚 LLM 和 Agent 的关系。

---

## Day 2：Attention 与 QKV

今日目标：理解 Attention 是“加权查表”。

09:00-10:20 理论输入：

- 学 Q、K、V 的含义
- 理解 softmax、点积相似度、缩放因子
- 不追求公式细节，先追求能解释

10:35-12:00 小实验：

- 用 NumPy 手写单头 attention
- 输入 3 个 token 向量
- 打印 attention 权重矩阵

13:30-15:00 主项目：

- 写 `experiments/day02_attention_numpy.py`
- 增加注释解释每一步 shape

15:15-16:30 扩展：

- 修改输入向量，观察 attention 权重变化
- 手动构造一个“某个 token 强关注另一个 token”的例子

16:45-17:30 复盘：

- 写《QKV 到底在做什么》
- commit：`feat: implement numpy self attention`

验收标准：能解释“Q 是我在找什么，K 是我有什么标签，V 是实际内容”。

---

## Day 3：PyTorch Mini Transformer 上半部分

今日目标：用 PyTorch 搭出 Transformer block 的骨架。

09:00-10:20 理论输入：

- 学 `nn.Embedding`
- 学 Multi-Head Attention
- 学 causal mask 的作用

10:35-12:00 小实验：

- 写一个 embedding demo
- 输入 token ids，输出 embedding tensor
- 打印 batch、seq_len、hidden_dim 的 shape

13:30-15:00 主项目：

- 创建 `projects/mini_transformer/model.py`
- 实现 `MiniMultiHeadAttention`

15:15-16:30 Debug：

- 用随机 tensor 跑通 forward
- 检查输出 shape 是否正确

16:45-17:30 复盘：

- 写清楚 batch、head、seq、dim 四个维度
- commit：`feat: add mini transformer attention block`

验收标准：模型 forward 不报错，shape 全部能解释。

---

## Day 4：PyTorch Mini Transformer 下半部分

今日目标：训练一个字符级语言模型。

09:00-10:20 理论输入：

- 学 next token prediction
- 学 cross entropy loss
- 学训练循环：forward、loss、backward、step

10:35-12:00 小实验：

- 准备一段短文本作为训练数据
- 写字符到 id 的映射
- 构造 batch

13:30-15:00 主项目：

- 实现 `projects/mini_transformer/train.py`
- 跑通训练循环

15:15-16:30 Debug：

- 观察 loss 是否下降
- 写一个 generate 函数

16:45-17:30 复盘：

- 写《为什么 LLM 是预测下一个 token》
- commit：`feat: train character mini transformer`

验收标准：能生成一小段文本，哪怕质量很差。

---

## Day 5：残差连接、LayerNorm 与训练稳定性

今日目标：理解深层网络为什么需要残差连接。

09:00-10:20 理论输入：

- 学梯度消失
- 学 ResNet block
- 学 Transformer 中 residual + LayerNorm 的位置

10:35-12:00 小实验：

- 写普通 MLP block 和 residual MLP block
- 对比训练 loss

13:30-15:00 主项目：

- 给 mini Transformer 加 FFN、residual、LayerNorm

15:15-16:30 扩展：

- 移除 residual 重新训练，对比变化
- 记录观察

16:45-17:30 复盘：

- 画出 Transformer block 结构图
- commit：`feat: add ffn residual and layernorm`

验收标准：能解释 residual connection 在 Transformer 里的作用。

---

## Day 6：Tokenizer 与上下文成本

今日目标：知道 token 如何影响成本、速度和上下文。

09:00-10:20 理论输入：

- 学 BPE、SentencePiece、vocabulary
- 学 token 数和价格的关系
- 学 context window 的限制

10:35-12:00 小实验：

- 用 tokenizer 比较中文、英文、代码、Markdown
- 统计同一含义不同表达的 token 数

13:30-15:00 主项目：

- 写 `experiments/day06_tokenizer_compare.py`
- 输出 Markdown 表格

15:15-16:30 扩展：

- 设计 5 条更省 token 的 prompt 改写
- 对比改写前后 token 数

16:45-17:30 复盘：

- 写《为什么 prompt 不是越长越好》
- commit：`feat: compare tokenizer behavior`

验收标准：能估算一次对话为什么会变贵。

---

## Day 7：Embedding 与相似度检索

今日目标：理解 RAG 的底层是向量检索。

09:00-10:20 理论输入：

- 学 embedding
- 学 cosine similarity
- 学 top-k retrieval

10:35-12:00 小实验：

- 准备 10 句话
- 生成或模拟 embedding
- 实现相似句检索

13:30-15:00 主项目：

- 写 `experiments/day07_embedding_search.py`
- 输入 query 返回 top 3

15:15-16:30 扩展：

- 尝试不同 chunk 长度
- 观察检索质量变化

16:45-17:30 复盘：

- 写《Embedding 为什么能让文本被搜索》
- commit：`feat: add embedding similarity demo`

验收标准：能讲清楚 RAG 为什么不是“模型记住了文档”。

---

## Day 8：KV Cache、长上下文与推理速度

今日目标：理解为什么长对话越来越慢、越来越贵。

09:00-10:20 理论输入：

- 学 prefill 和 decode
- 学 KV cache
- 学长上下文的成本

10:35-12:00 小实验：

- 写伪代码模拟历史消息增长
- 估算每轮 token 数变化

13:30-15:00 主项目：

- 写一个 token budget calculator
- 输入 messages，输出估算 token 数

15:15-16:30 扩展：

- 设计三种上下文策略：截断、摘要、滑动窗口
- 比较优缺点

16:45-17:30 复盘：

- 写《上下文窗口不是无限记忆》
- commit：`feat: add token budget calculator`

验收标准：能解释 KV cache 解决了什么，没有解决什么。

---

## Day 9：采样策略

今日目标：理解 temperature、top-p、top-k 如何改变输出。

09:00-10:20 理论输入：

- 学 logits 到概率分布
- 学 temperature
- 学 top-p、top-k、beam search

10:35-12:00 小实验：

- 写一个模拟采样器
- 固定 logits，改变参数观察输出

13:30-15:00 主项目：

- 写 `experiments/day09_sampling.py`
- 输出不同参数下的采样结果表

15:15-16:30 扩展：

- 总结不同任务的推荐参数
- 例如：代码、创意写作、分类、抽取

16:45-17:30 复盘：

- 写《为什么 temperature 高会更发散》
- commit：`feat: add sampling strategy demo`

验收标准：能根据任务选择合适采样参数。

---

## Day 10：底层阶段复盘

今日目标：把 Transformer 到 LLM 推理链路讲清楚。

09:00-10:20 整理：

- 回看 Day 1-9 笔记
- 标出仍然不懂的概念

10:35-12:00 补洞：

- 重跑所有小实验
- 修复不能运行的脚本

13:30-15:00 写作：

- 写博客《Transformer 是如何读懂我说的话的》

15:15-16:30 图表：

- 补 1 张架构图
- 补 1 张 token/采样对比表

16:45-17:30 复盘：

- 整理 README
- commit：`docs: add stage one review`

验收标准：能用自己的话解释 token、attention、embedding、sampling、context。

---

## Day 11：Messages 与 API 调用

今日目标：理解 Agent 的输入输出协议。

09:00-10:20 理论输入：

- 学 messages 数组
- 学 system/user/assistant/tool role
- 学 raw request 和 raw response

10:35-12:00 小实验：

- 写最小 OpenAI 或 Claude API 调用
- 打印完整 response

13:30-15:00 主项目：

- 创建 `projects/assistant_agent/`
- 写 `basic_chat.py`

15:15-16:30 扩展：

- 对比不同 system prompt 的输出
- 记录稳定性变化

16:45-17:30 复盘：

- 写《Agent 的对话历史是如何组织的》
- commit：`feat: add basic chat api script`

验收标准：能解释一次 API 请求里每个字段的作用。

---

## Day 12：上下文管理器

今日目标：让 Agent 不被历史消息拖垮。

09:00-10:20 理论输入：

- 学截断策略
- 学摘要策略
- 学 sliding window

10:35-12:00 小实验：

- 写 token 估算函数
- 模拟 20 轮对话增长

13:30-15:00 主项目：

- 实现 `context_manager.py`
- 保留 system、最近消息、摘要占位

15:15-16:30 测试：

- 写 5 个测试 case
- 检查超长消息是否被压缩

16:45-17:30 复盘：

- 写上下文管理策略对比表
- commit：`feat: implement context manager`

验收标准：上下文超过阈值后仍能保持关键设定。

---

## Day 13：System Prompt 工程

今日目标：学会写可控、可测、可迭代的 system prompt。

09:00-10:20 理论输入：

- 学角色定义
- 学约束
- 学输出格式
- 学失败处理

10:35-12:00 小实验：

- 写 3 个 system prompt 版本
- 用同一任务测试输出差异

13:30-15:00 主项目：

- 给 assistant agent 加 prompt 文件
- 不把 prompt 硬编码在脚本里

15:15-16:30 对比：

- 做一个 prompt ablation 表
- 记录准确性、稳定性、冗余程度

16:45-17:30 复盘：

- 写自己的 system prompt 模板
- commit：`docs: compare system prompts`

验收标准：能写出适合工具调用 Agent 的 system prompt。

---

## Day 14：Few-Shot 与 CoT

今日目标：理解例子和推理提示如何改变模型表现。

09:00-10:20 理论输入：

- 学 zero-shot
- 学 few-shot
- 学 chain-of-thought
- 学什么时候不该暴露推理过程

10:35-12:00 小实验：

- 分类任务做 zero-shot vs few-shot
- 抽取任务做 zero-shot vs few-shot

13:30-15:00 主项目：

- 写 `experiments/day14_fewshot_eval.py`
- 输出准确率对比

15:15-16:30 扩展：

- 给 assistant agent 加 examples 配置
- 尝试减少输出格式错误

16:45-17:30 复盘：

- 写《规则不如例子稳定吗》
- commit：`feat: add few shot evaluation`

验收标准：知道 few-shot 在什么任务里最有效。

---

## Day 15：Function Calling 入门

今日目标：理解模型如何“决定调用工具”。

09:00-10:20 理论输入：

- 学 JSON Schema
- 学 tool name、description、parameters
- 学工具选择不是工具执行

10:35-12:00 小实验：

- 定义 `get_weather`
- 定义 `calculate`
- 让模型选择工具

13:30-15:00 主项目：

- 写 `tools.py`
- 建立工具注册表

15:15-16:30 测试：

- 设计 10 条用户请求
- 看模型选错工具的情况

16:45-17:30 复盘：

- 写工具 description 的写法总结
- commit：`feat: define first tool schemas`

验收标准：模型能根据请求选择正确工具。

---

## Day 16：Tool Runtime

今日目标：把工具调用真正执行起来。

09:00-10:20 理论输入：

- 学 tool call lifecycle
- 学参数校验
- 学错误回传

10:35-12:00 小实验：

- 写 dispatcher
- 接收 tool name 和 args
- 执行本地函数

13:30-15:00 主项目：

- 实现 `tool_runtime.py`
- 支持多工具注册

15:15-16:30 Debug：

- 测试正常参数、缺失参数、非法参数
- 工具错误不要让程序崩溃

16:45-17:30 复盘：

- 写《LLM 不是自己调用工具，是程序帮它执行》
- commit：`feat: implement tool runtime`

验收标准：Agent 能完成“计算 + 模拟天气查询”。

---

## Day 17：RAG 索引

今日目标：把自己的笔记变成可检索知识库。

09:00-10:20 理论输入：

- 学 chunking
- 学 embedding index
- 学 top-k retrieval

10:35-12:00 小实验：

- 选 5 篇自己的笔记
- 做 chunk 切分
- 给每个 chunk 编号

13:30-15:00 主项目：

- 实现 `rag_index.py`
- 建立本地向量索引或简化相似度索引

15:15-16:30 测试：

- 输入 10 个问题
- 检查返回 chunk 是否相关

16:45-17:30 复盘：

- 写 chunk 长度、重叠、召回质量观察
- commit：`feat: build local rag index`

验收标准：输入问题能返回相关笔记片段。

---

## Day 18：RAG 问答

今日目标：实现 retrieve -> answer 的完整链路。

09:00-10:20 理论输入：

- 学检索增强生成
- 学引用片段
- 学检索为空时的回答策略

10:35-12:00 小实验：

- 把 top-k chunks 塞进 prompt
- 要求回答引用来源

13:30-15:00 主项目：

- 实现 `rag_qa.py`
- 支持基于笔记问答

15:15-16:30 Debug：

- 测试检索错、检索为空、问题太泛
- 调整 prompt

16:45-17:30 复盘：

- 写《RAG 的答案为什么仍可能幻觉》
- commit：`feat: implement rag qa flow`

验收标准：回答必须基于检索片段，不能胡编来源。

---

## Day 19：手写 ReAct Loop

今日目标：理解 Agent 自主性的核心：循环 + 工具 + 状态。

09:00-10:20 理论输入：

- 学 Thought -> Action -> Observation
- 学 max steps
- 学 finish 条件

10:35-12:00 小实验：

- 写 calculator
- 写 fake search
- 让模型输出 JSON action

13:30-15:00 主项目：

- 实现 `react_loop.py`
- 支持连续两次工具调用

15:15-16:30 Debug：

- 处理 JSON 解析失败
- 处理工具不存在
- 处理超过最大步数

16:45-17:30 复盘：

- 写《Agent 的自主性从哪里来》
- commit：`feat: add handwritten react loop`

验收标准：能完成“先查再算”的多步任务。

---

## Day 20：Memory

今日目标：给 Agent 加入短期和长期记忆。

09:00-10:20 理论输入：

- 学 conversation buffer
- 学 preference memory
- 学 vector memory
- 学 memory 的风险

10:35-12:00 小实验：

- 写一个 JSON 文件保存用户偏好
- 对话中读取偏好

13:30-15:00 主项目：

- 实现 `memory.py`
- 支持“记住我喜欢简洁回答”

15:15-16:30 测试：

- 测试写入、读取、覆盖、删除
- 防止把临时信息当长期记忆

16:45-17:30 复盘：

- 写记忆策略规则
- commit：`feat: add assistant memory`

验收标准：Agent 能在后续对话中使用用户偏好。

---

## Day 21：Agent Eval 初版

今日目标：开始用数据评估 Agent。

09:00-10:20 理论输入：

- 学成功率
- 学延迟
- 学 token 成本
- 学失败分类

10:35-12:00 小实验：

- 写 10 条测试用例
- 标注期望行为

13:30-15:00 主项目：

- 实现 `evals.py`
- 自动运行测试集

15:15-16:30 分析：

- 输出 JSON 或 CSV
- 统计成功/失败

16:45-17:30 复盘：

- 写失败案例分析
- commit：`feat: add basic agent evals`

验收标准：不是凭感觉说 Agent 好不好。

---

## Day 22：个人助理 Agent v1 整合

今日目标：交付第一个完整 Agent。

09:00-10:20 整理：

- 回看 Day 11-21 代码
- 列出必须修的 bug

10:35-12:00 修复：

- 统一入口文件
- 统一配置读取

13:30-15:00 整合：

- 串起 chat、context、tools、RAG、memory、eval

15:15-16:30 README：

- 写安装、配置、运行、示例
- 补 3 个演示 case

16:45-17:30 复盘：

- 写《我的第一个个人助理 Agent》
- commit：`docs: document assistant agent v1`

验收标准：陌生人能按 README 跑起来。

---

## Day 23：Orchestrator-Worker 架构

今日目标：理解主控 Agent 如何拆任务。

09:00-10:20 理论输入：

- 学 orchestrator-worker
- 学 planner 和 executor 的职责边界
- 学为什么多 Agent 会增加成本

10:35-12:00 架构：

- 把个人助理拆成 planner、researcher、executor
- 写每个角色的输入输出

13:30-15:00 主项目：

- 创建多 Agent 版本目录
- 写角色 prompt

15:15-16:30 测试：

- 用 3 个任务观察拆分是否必要
- 对比单 Agent 和多 Agent

16:45-17:30 复盘：

- 画架构图
- commit：`docs: add orchestrator worker architecture`

验收标准：知道什么时候不该拆成多 Agent。

---

## Day 24：Subagent 设计原则

今日目标：建立拆分 Agent 的判断标准。

09:00-10:20 理论输入：

- 学任务复杂度
- 学上下文隔离
- 学权限隔离
- 学并行执行

10:35-12:00 案例分析：

- 选 5 个任务
- 分别设计单 Agent 和多 Agent 方案

13:30-15:00 主项目：

- 给 v1 Agent 标出可拆分模块
- 写拆分计划

15:15-16:30 对比：

- 估算拆分后的 token、延迟、稳定性变化

16:45-17:30 复盘：

- 写《我什么时候会创建 Subagent》
- commit：`docs: summarize subagent design principles`

验收标准：能说清拆分带来的收益和代价。

---

## Day 25：Skill Registry

今日目标：让 Agent 像查工具箱一样选择技能。

09:00-10:20 理论输入：

- 学 skill name
- 学 skill description
- 学 input/output schema
- 学 skill routing

10:35-12:00 设计：

- 设计 10 个技能
- 写名称、描述、输入、输出、失败情况

13:30-15:00 主项目：

- 实现 `skill_registry.py`
- 支持根据任务选择 skill

15:15-16:30 测试：

- 写 10 条用户请求
- 检查路由是否合理

16:45-17:30 复盘：

- 写 skill description 写法总结
- commit：`feat: add skill registry`

验收标准：planner 能选出合适技能。

---

## Day 26：感知-推理-执行三层架构

今日目标：把 Agent 产品化思路结构化。

09:00-10:20 理论输入：

- 感知层：输入、文件、网页、用户状态
- 推理层：规划、选择工具、判断风险
- 执行层：调用 API、写文件、发请求

10:35-12:00 架构：

- 画三层架构图
- 标出每层输入输出

13:30-15:00 主项目：

- 重构项目目录
- 标出 perception、reasoning、action

15:15-16:30 检查：

- 查找跨层乱调用
- 写清楚边界

16:45-17:30 复盘：

- 写《Agent 产品的三层结构》
- commit：`docs: add three layer agent architecture`

验收标准：架构图能指导后续开发。

---

## Day 27：LangGraph 入门

今日目标：理解 graph、node、edge、state。

09:00-10:20 理论输入：

- 学 state graph
- 学 node function
- 学 conditional edge

10:35-12:00 小实验：

- 写 planner -> tool -> answer 的最小图
- 打印执行路径

13:30-15:00 主项目：

- 创建 `projects/langgraph_agent/`
- 实现 `minimal_graph.py`

15:15-16:30 Debug：

- 加一个条件分支
- 观察 state 如何变化

16:45-17:30 复盘：

- 写 LangGraph 和手写 ReAct 的区别
- commit：`feat: add minimal langgraph agent`

验收标准：能解释 node、edge、state 的作用。

---

## Day 28：LangGraph 重写个人助理

今日目标：把 v1 Agent 改造成 graph。

09:00-10:20 设计：

- 定义 state
- 定义 RAG node、tool node、memory node、answer node

10:35-12:00 编码：

- 先实现最短链路
- 确保能跑通

13:30-15:00 主项目：

- 实现 `agent_graph.py`
- 接入已有工具和 RAG

15:15-16:30 测试：

- 跑 Day 21 的 eval
- 记录 v1/v2 差异

16:45-17:30 复盘：

- 写迁移记录
- commit：`feat: port assistant agent to langgraph`

验收标准：同一批任务 v2 能稳定运行。

---

## Day 29：Agent 框架对比

今日目标：理解 LangGraph、AutoGen、CrewAI 的取舍。

09:00-10:20 理论输入：

- 查官方文档或高质量资料
- 只看核心概念，不追教程细节

10:35-12:00 对比：

- 建表：状态管理、调试、多 Agent、可控性、适用场景

13:30-15:00 主项目：

- 给自己的项目写“为什么选/不选某框架”

15:15-16:30 扩展：

- 选一个小任务，用另一个框架做伪代码设计

16:45-17:30 复盘：

- 写《主流 Agent 框架对比》
- commit：`docs: compare agent frameworks`

验收标准：能根据项目需求选择框架。

---

## Day 30：多 Agent 阶段复盘

今日目标：交付个人助理 Agent v2。

09:00-10:20 整理：

- 回看 Day 23-29
- 列出架构变化

10:35-12:00 修复：

- 修 LangGraph 版本 bug
- 补配置和启动脚本

13:30-15:00 README：

- 写 v2 README
- 加架构图

15:15-16:30 评估：

- 对比 v1/v2 成功率、延迟、成本

16:45-17:30 复盘：

- 写《单 Agent 到多 Agent 的取舍》
- commit：`docs: document assistant agent v2`

验收标准：v2 是可运行、可解释、可评估的版本。

---

## Day 31：AI 编程工具与工作流

今日目标：理解 Claude Code、Cursor、Windsurf、Codex 的差异。

09:00-10:20 理论输入：

- 学 AI 编程工具的基本工作流
- 关注上下文、文件编辑、终端、测试、PR 能力

10:35-12:00 对比：

- 用同一个小需求写 4 种工具的使用流程

13:30-15:00 实操：

- 选一个工具完成一个小功能
- 记录人类如何校准 AI

15:15-16:30 总结：

- 建表比较适用场景

16:45-17:30 复盘：

- 写《AI 编程工具怎么选》
- commit：`docs: compare ai coding workflows`

验收标准：知道不同工具适合什么开发场景。

---

## Day 32：Vibe Coding 方法论

今日目标：形成自己的 AI 编程节奏。

09:00-10:20 理论输入：

- 人定方向
- AI 做实现
- 人做验收和校准

10:35-12:00 模板：

- 写需求模板
- 写验收标准模板
- 写测试模板

13:30-15:00 实操：

- 用模板驱动 AI 做一个 Markdown 转 PPT 小工具原型

15:15-16:30 迭代：

- 每次只让 AI 改一个点
- 记录 3 轮修改过程

16:45-17:30 复盘：

- 写自己的 Vibe Coding SOP
- commit：`docs: add vibe coding task template`

验收标准：有一套以后能复用的 AI 编程模板。

---

## Day 33：毕业项目 PRD

今日目标：锁定最终作品方向。

09:00-10:20 选题：

- 在个人助理、AI 视频、AI 编程助手、商业工具中选一个
- 判断展示价值和可完成度

10:35-12:00 用户场景：

- 写目标用户
- 写 3 个真实使用场景
- 写非目标

13:30-15:00 PRD：

- 完成 `capstone/PRD.md`
- 明确 MVP 功能

15:15-16:30 验收：

- 写功能验收标准
- 写失败边界

16:45-17:30 复盘：

- 写选题理由
- commit：`docs: add capstone prd`

验收标准：项目范围足够小，10天内能完成。

---

## Day 34：毕业项目架构

今日目标：把 PRD 拆成系统设计。

09:00-10:20 设计：

- 定义核心模块
- 定义数据流
- 定义工具列表

10:35-12:00 架构图：

- 画用户输入 -> Agent -> 工具/RAG -> 输出

13:30-15:00 技术方案：

- 写 `capstone/architecture.md`
- 列 API、数据结构、状态

15:15-16:30 风险：

- 写失败处理
- 写成本控制点

16:45-17:30 复盘：

- commit：`docs: add capstone architecture`

验收标准：可以直接按架构开工。

---

## Day 35：毕业项目核心链路

今日目标：跑通 MVP 最短路径。

09:00-10:20 任务拆解：

- 只保留最核心流程
- 删掉锦上添花功能

10:35-12:00 编码：

- 创建 `capstone/src/`
- 写入口、配置、核心 Agent

13:30-15:00 主流程：

- 实现用户输入 -> 决策 -> 工具/RAG -> 输出

15:15-16:30 测试：

- 跑 3 个真实案例
- 修最明显 bug

16:45-17:30 复盘：

- 写 MVP 运行记录
- commit：`feat: implement capstone core flow`

验收标准：核心链路能跑通，不追求漂亮。

---

## Day 36：CLI 或 Web UI

今日目标：让别人能用你的项目。

09:00-10:20 方案选择：

- CLI：最快
- Web UI：展示更好
- 根据项目目标选一个

10:35-12:00 实现：

- 做最小交互界面
- 支持输入和输出

13:30-15:00 接入：

- 把 UI 接到核心链路
- 加 loading 和错误提示

15:15-16:30 README：

- 写启动方式
- 写使用示例

16:45-17:30 复盘：

- commit：`feat: add capstone user interface`

验收标准：一条命令能启动 Demo。

---

## Day 37：日志与 Trace

今日目标：让 Agent 行为可观察。

09:00-10:20 理论输入：

- 学 trace
- 学 tool call log
- 学 latency log

10:35-12:00 设计：

- 定义 trace JSON 格式
- 包含输入、输出、工具、耗时、错误

13:30-15:00 编码：

- 给 capstone 加 trace 记录

15:15-16:30 测试：

- 跑 5 次任务
- 检查 trace 是否可读

16:45-17:30 复盘：

- 写《我如何调试 Agent》
- commit：`feat: add tracing and logs`

验收标准：出错时能从 trace 看出发生了什么。

---

## Day 38：成本控制

今日目标：知道每次运行花多少钱。

09:00-10:20 理论输入：

- 学 prompt tokens
- 学 completion tokens
- 学模型价格估算

10:35-12:00 小实验：

- 写 token 统计器
- 估算不同 prompt 版本成本

13:30-15:00 主项目：

- 实现 `cost_tracker.py`
- 每次运行输出成本

15:15-16:30 优化：

- 压缩 prompt
- 控制检索 chunk 数
- 对比成本变化

16:45-17:30 复盘：

- 写成本优化记录
- commit：`feat: add cost tracking`

验收标准：每次 Demo 都能看到 token 和成本。

---

## Day 39：Prompt 版本管理

今日目标：让 prompt 可迭代、可回滚、可评估。

09:00-10:20 理论输入：

- 学 prompt versioning
- 学 ablation
- 学 prompt changelog

10:35-12:00 重构：

- 把 prompt 从代码中抽离
- 建 `capstone/prompts/`

13:30-15:00 编码：

- 支持选择 prompt v1/v2
- 记录当前版本

15:15-16:30 评估：

- 用 eval 对比两个 prompt
- 记录成功率差异

16:45-17:30 复盘：

- 写 prompt changelog
- commit：`feat: version capstone prompts`

验收标准：prompt 改动可追踪，不靠记忆。

---

## Day 40：垂直应用阶段复盘

今日目标：毕业项目进入可展示状态。

09:00-10:20 整理：

- 列出必须修的问题
- 列出可以放弃的功能

10:35-12:00 修复：

- 修启动问题
- 修明显交互问题

13:30-15:00 案例：

- 准备 3 个最佳演示案例
- 保存输入、输出、trace

15:15-16:30 文档：

- 补 README
- 补截图或运行记录

16:45-17:30 复盘：

- 写《毕业项目构建日志》
- commit：`docs: add capstone build log`

验收标准：项目可以拿给别人试用。

---

## Day 41：Eval 扩展

今日目标：让项目有可信质量指标。

09:00-10:20 设计：

- 定义成功标准
- 定义失败类型
- 定义评分规则

10:35-12:00 数据：

- 写 30 条 eval case
- 覆盖正常、边界、异常

13:30-15:00 编码：

- 扩展 eval runner
- 输出统计结果

15:15-16:30 分析：

- 分类失败原因
- 找 top 3 改进点

16:45-17:30 复盘：

- commit：`test: expand capstone eval cases`

验收标准：有成功率、失败分类和改进建议。

---

## Day 42：失败处理与稳定性

今日目标：让项目更像产品，而不是 demo 脚本。

09:00-10:20 风险梳理：

- 工具失败
- 检索为空
- JSON 格式错误
- 超时
- 用户输入不完整

10:35-12:00 编码：

- 加错误捕获
- 加 fallback

13:30-15:00 测试：

- 人为制造异常
- 检查用户体验

15:15-16:30 文档：

- 写 failure handling 文档

16:45-17:30 复盘：

- commit：`fix: improve capstone failure handling`

验收标准：异常不会直接中断流程。

---

## Day 43：Demo 脚本与录屏准备

今日目标：让项目能被 3 分钟讲清楚。

09:00-10:20 叙事：

- 问题是什么
- 你的方案是什么
- 为什么 Agent 适合

10:35-12:00 脚本：

- 写 3 分钟 Demo script
- 标出每个镜头要展示什么

13:30-15:00 演练：

- 按脚本跑 3 次
- 记录卡顿点

15:15-16:30 修整：

- 修演示路径 bug
- 准备演示数据

16:45-17:30 复盘：

- commit：`docs: add capstone demo script`

验收标准：照脚本能流畅演示。

---

## Day 44：技术博客

今日目标：写出一篇能展示能力的长文。

09:00-10:20 大纲：

- 背景
- 架构
- 核心实现
- Eval
- 踩坑
- 下一步

10:35-12:00 初稿：

- 写背景、目标、架构

13:30-15:00 技术部分：

- 写关键代码和设计取舍
- 插入 trace、eval 表格

15:15-16:30 修改：

- 删废话
- 补图表
- 调整标题

16:45-17:30 复盘：

- commit：`docs: add capstone technical review`

验收标准：文章能让别人看懂你做了什么、难点在哪里。

---

## Day 45：最终作品集交付

今日目标：把 45 天成果整理成作品集。

09:00-10:20 清点：

- 列出所有项目
- 列出所有博客
- 列出所有 Demo

10:35-12:00 README：

- 写仓库首页
- 放学习路线、项目列表、运行方式

13:30-15:00 最终检查：

- 检查链接
- 检查启动命令
- 检查截图和示例

15:15-16:30 复盘：

- 写 45 天总复盘
- 写下一阶段计划

16:45-17:30 收尾：

- 最终 commit
- 打 tag 或 release

Commit：`docs: finalize 45 days ai portfolio`

验收标准：仓库像一个作品集，而不是零散学习草稿。

---

## 每天结束时的固定复盘模板

```md
## Day X 复盘

### 今天完成了什么

- 

### 今天真正理解了什么

- 

### 今天卡在哪里

- 

### 明天要优先处理什么

- 

### 今日 commit

- 
```

---

## 高强度执行规则

1. 卡住 15 分钟还没进展，就写下问题，先绕过去。
2. 每天 13:30 后必须写代码，不能继续刷教程。
3. 每天 16:45 必须复盘，不允许用“继续调 bug”挤掉复盘。
4. 每 5 天做一次小整理，每 10 天做一次大复盘。
5. 优先完成能展示的闭环，不追求把每个工具都学全。

