# Day 1：Transformer 与 LLM 全景直觉

今天的目标不是手搓 Transformer，而是建立一条完整心智链路：

```text
文本 -> Tokenize -> Embedding -> Attention -> Logits -> Sampling -> 输出
```

## 1. 文本不是直接进入模型

LLM 看到的不是“字”或“单词”，而是一串 token id。

例如：

```text
我要在45天内掌握AI Agent
```

会先被 tokenizer 切成若干 token。token 可能是一个中文词、一个英文片段、一个数字、一个空格加单词，甚至是代码里的符号。

这件事直接影响三个东西：

- 成本：token 越多，费用通常越高
- 延迟：上下文越长，处理越慢
- 表达：同样意思，不同写法会产生不同 token 数

## 2. Embedding：把 token 变成向量

token id 本身只是编号，模型不能直接理解它。

Embedding 层会把每个 token id 映射成一个向量。你可以把它想成“语义坐标”：

```text
token id -> [0.12, -0.48, 0.07, ...]
```

后面的 attention、FFN、输出预测，处理的都是这些向量。

## 3. Attention：让每个 token 看上下文

Attention 的核心直觉是：每个 token 都会问“我现在应该关注上下文里的谁？”

常见记忆句：

```text
Q = 我在找什么
K = 我有什么标签
V = 我的实际内容
```

公式是：

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```

但今天先记住直觉就够了：

```text
Attention = 根据相关性，对上下文信息做加权汇总
```

## 4. Logits 与 Sampling：模型不是直接“写答案”

模型每一步输出的是下一个 token 的概率分布。

比如它可能认为下一个 token 是：

```text
"是": 0.35
"可以": 0.18
"不是": 0.08
...
```

Sampling 策略决定最终选哪个 token：

- temperature 低：更稳定、更保守
- temperature 高：更多样、更发散
- top-p：只在累计概率较高的一批 token 中采样
- top-k：只在概率最高的 k 个 token 中采样

## 5. 上下文窗口不是长期记忆

上下文窗口是模型一次请求能看到的 token 范围。它更像短期工作台，不是永久记忆。

当对话越来越长时：

- prompt token 变多
- 请求变慢
- 成本变高
- 旧信息可能需要截断、摘要或检索回来

这就是后面 Agent 要学习 context manager、RAG 和 memory 的原因。

## 6. 今天的小实验

运行：

```powershell
python experiments/day01_tokenizer_demo.py
```

观察重点：

- 中文字符数和 token 数不是一一对应
- 英文经常会出现“空格 + 单词片段”的 token
- 代码里的换行、缩进、标点也会占 token
- Markdown 结构符号也会占 token

## 7. 今日结论

LLM 的底层工作流可以简化理解为：

```text
把文本切成 token，把 token 变成向量，用 attention 汇总上下文，再预测下一个 token。
```

Agent 不是另一个神秘物种。Agent 是在 LLM 这套能力外面加上：

- 工具
- 记忆
- 检索
- 循环
- 评估
- 状态管理

所以第一步先理解 token 和上下文，是后面理解 Agent 成本、稳定性和能力边界的地基。
