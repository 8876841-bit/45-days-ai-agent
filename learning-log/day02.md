# Day 2 Learning Log：Self-Attention 与 QKV

日期：2026-05-20

主题：用 NumPy 手写单头 self-attention，并理解 Q、K、V、scores、weights、output。

## 今日文件

- `experiments/day02_attention_numpy.py`
- `notes/day02-attention-qkv.md`

## 今日核心卡点

### 1. NumPy attention 输出看不懂

我的问题：

> 这个没看懂。

当时看到的输出分成四块：

```text
Input token vectors
Attention scores = QK^T / sqrt(d_k)
Attention weights = softmax(scores)
Output vectors = attention_weights @ V
```

整理后的理解：

```text
input vectors：每个 token 原本的信息
scores：两两相似度
weights：每个 token 应该关注谁、关注多少
output：混合上下文后的新 token 表示
```

保留结论：

```text
Self-Attention 会让每个 token 看一遍上下文，决定关注谁，然后把被关注 token 的信息按比例混进自己的新表示里。
```

## 2. 向量坐标的标准是什么

我的问题：

> 设计情况里设置“向量坐标”的标准是什么？

解释摘要：

真实模型里的 token 向量不是人手工设计的，而是模型训练出来的。

但 Day 2 实验里，我们人为设置了 3 个很小的向量：

```text
我    = [1.0, 0.0, 0.0]
喜欢  = [0.8, 0.2, 0.0]
AI    = [0.0, 0.1, 1.0]
```

目的不是模拟真实语义，而是制造一个容易观察的关系：

```text
如果两个向量方向接近，它们就更像。
如果两个向量方向差很远，它们就不太像。
```

所以在这个实验里：

```text
我 和 喜欢 比较像
AI 和前两个不太像
```

临时理解：

```text
第 1 维：偏“人/动作上下文”
第 2 维：轻微连接维度
第 3 维：偏“AI/技术概念”
```

重要提醒：

```text
这只是教学用。真实模型可能有几千维，而且每一维不一定能被人类直接命名。
```

## 3. Attention scores 是什么意思

我的问题：

> Attention scores 这个是什么意思？

解释摘要：

```text
Attention scores = QK^T / sqrt(d_k)
```

这一步是在算：每个 token 和其他 token 有多像。

在 Day 2 的简化实验里：

```text
q = x
k = x
v = x
```

所以可以先理解成：

```text
scores = 向量点积 / sqrt(维度数)
```

例子：

```text
我    = [1.0, 0.0, 0.0]
喜欢  = [0.8, 0.2, 0.0]
```

点积：

```text
1.0 * 0.8 + 0.0 * 0.2 + 0.0 * 0.0 = 0.8
```

向量维度是 3：

```text
sqrt(3) ≈ 1.732
```

所以：

```text
0.8 / 1.732 ≈ 0.462
```

这就是输出表里的：

```text
我 -> 喜欢 = 0.462
```

保留结论：

```text
scores 是原始相似度分数，不是最终注意力比例。
```

## 4. QK^T / sqrt(d_k) 是干嘛用的

我的问题：

> 这个是干嘛用的？

解释摘要：

`QK^T` 用来算 query 和 key 的相关性，也就是“当前 token 应该关注谁”。

```text
Q = Query，我在找什么
K = Key，我有什么标签
V = Value，我的实际内容
```

先用 Q 和 K 算分数：

```text
QK^T
```

再除以：

```text
sqrt(d_k)
```

这是为了缩放分数，避免分数太大导致 softmax 过于极端。

最后用 softmax 得到 attention weights，再用 weights 去加权汇总 V。

保留结论：

```text
Q 和 K 决定“看谁”，V 决定“拿到什么信息”。
```

## 5. weights 和 output 怎么理解

Attention weights：

```text
softmax(scores)
```

它把原始分数变成比例，每一行加起来约等于 1。

例如：

```text
我 -> 我     0.408
我 -> 喜欢   0.363
我 -> AI     0.229
```

可以读成：

```text
当模型更新“我”这个 token 的表示时：
40.8% 看“我”
36.3% 看“喜欢”
22.9% 看“AI”
```

Output vectors：

```text
attention_weights @ V
```

它表示用注意力比例把上下文信息混合进当前 token。

原始的“我”：

```text
[1.0, 0.0, 0.0]
```

经过 attention 后：

```text
[0.698, 0.096, 0.229]
```

说明它已经混入了“喜欢”和“AI”的信息。

## 今日最终记忆句

```text
scores 是“像不像”，weights 是“看多少”，output 是“混合后的新表示”。
```

## 下次继续

下一步进入 Day 3：

```text
PyTorch Mini Transformer 上半部分
```

重点不是训练模型，而是理解：

```text
[batch, seq, hidden]
```

以及 Q、K、V 在 PyTorch 里如何由 Linear 层投影出来。

