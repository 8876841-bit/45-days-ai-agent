# Windows 11 + 中国大陆网络 AI 学习环境配置建议

你的设备信息：

- 系统：Windows 11 专业版
- CPU：Intel Core i5-13400F
- 内存：16GB
- GPU：NVIDIA GeForce RTX 3060 8GB
- 存储：空间充足
- 网络：中国大陆网络

结论：这台机器非常适合完成 45 天 AI Agent 学习计划。重点不是硬件瓶颈，而是网络、API Key、Python 环境和依赖安装稳定性。

---

## 一、适合你的学习路线调整

### 可以放心做的内容

- OpenAI / Claude / 国产模型 API 调用
- Agent、Tool Use、RAG、ReAct、多 Agent 项目
- LangGraph、AutoGen、CrewAI 等框架实验
- Cursor / Codex / Claude Code 类 AI 编程工作流
- Remotion / HyperFrames / 视频自动化项目
- 小型本地 embedding、向量检索、RAG demo

### 不建议一开始死磕的内容

- 在本机训练大模型
- 本地跑 14B、32B 以上大模型
- 复杂 CUDA 环境源码编译
- 一上来搭很重的私有化 Agent 平台

你的 RTX 3060 8GB 更适合：

- 跑 1.5B、3B、7B 量化模型
- 做本地 embedding
- 做轻量推理体验
- 做图像/视频工具的基础加速

---

## 二、推荐软件清单

### 必装

- Windows Terminal
- PowerShell 7
- Git for Windows
- Python 3.10 或 3.11
- VS Code 或 Cursor
- Node.js LTS
- NVIDIA 驱动

### Python 推荐

优先用 `uv` 管理 Python 项目，比传统 `pip + venv` 更快、更干净。

```powershell
pip install uv
uv --version
```

如果 `pip` 下载慢，可以使用国内镜像：

```powershell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### Node 推荐

安装 Node.js LTS 后，配置 npm 国内镜像：

```powershell
npm config set registry https://registry.npmmirror.com
```

---

## 三、API 与网络策略

中国大陆网络下，最容易卡的是：

- OpenAI API 访问
- Anthropic Claude API 访问
- GitHub 下载速度
- npm / pip / Hugging Face 下载
- Claude Code / Cursor 登录和模型访问

### 推荐模型接入策略

优先级建议：

1. 有稳定国际网络：OpenAI / Claude 官方 API
2. 没有稳定国际网络：使用兼容 OpenAI API 格式的国内或中转服务
3. 做本地实验：Ollama / LM Studio + 小模型

### 国内可替代 API

可用于学习 Agent 架构，不影响核心概念：

- 通义千问
- 智谱 GLM
- DeepSeek
- Moonshot / Kimi
- 火山方舟
- 百度千帆

只要服务支持：

- chat completions
- function calling / tool calling
- embedding
- streaming

就足够完成 80% 以上训练内容。

---

## 四、你的本机模型建议

如果你想体验本地模型，建议用 Ollama 或 LM Studio。

适合 RTX 3060 8GB 的模型类型：

- 1.5B：非常轻松
- 3B：轻松
- 7B 量化：可以尝试
- 14B 量化：不建议作为主力，可能卡

本地模型适合做：

- prompt 对比
- 简单聊天
- RAG demo
- 工具调用流程模拟

本地模型不适合作为前期主力：

- 复杂 Agent 推理
- 高稳定 function calling
- 高质量代码生成
- 多 Agent 长链路任务

---

## 五、Day 0：今晚环境准备清单

建议在正式 Day 1 前做一次 Day 0 环境准备。

### 1. 检查系统工具

```powershell
git --version
python --version
node --version
npm --version
nvidia-smi
```

验收标准：

- Python 是 3.10 或 3.11
- Node 是 LTS 版本
- `nvidia-smi` 能看到 RTX 3060

### 2. 创建训练仓库

```powershell
mkdir 45-days-ai-agent
cd 45-days-ai-agent
git init
mkdir notes, experiments, projects, blog, capstone, templates
```

### 3. 创建 Python 环境

```powershell
uv venv
.venv\Scripts\activate
uv pip install openai anthropic tiktoken python-dotenv numpy pandas rich
```

如果暂时不用 Claude，可以先不装 `anthropic`。

### 4. 创建 `.env`

```text
OPENAI_API_KEY=你的key
ANTHROPIC_API_KEY=你的key
```

如果你使用兼容 OpenAI 格式的国内服务，可以增加：

```text
OPENAI_BASE_URL=你的服务地址
OPENAI_API_KEY=你的key
```

### 5. 跑通最小 API 测试

新建 `experiments/day0_api_test.py`：

```python
from openai import OpenAI

client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "用一句话解释什么是AI Agent"}
    ],
)

print(resp.choices[0].message.content)
```

运行：

```powershell
python experiments/day0_api_test.py
```

验收标准：能正常打印模型回复。

---

## 六、45天计划中的关键调整

### Day 1-10

照常执行。底层概念不依赖网络太多，主要用 Python 小实验。

### Day 11-22

如果 OpenAI / Claude API 不稳定：

- 先使用兼容 OpenAI 格式的国内模型服务
- Tool Use 可以先用 prompt JSON 模拟
- Function Calling 后续再替换成官方 tool calling

### Day 27-30

LangGraph 可能涉及依赖安装。若下载慢：

- 优先配置 pip 国内镜像
- 仍失败就先用手写 graph 结构替代，别卡住主线

### Day 31-32

Claude Code 在大陆网络下可能不稳定。替代方案：

- Cursor
- Codex
- 通义灵码
- Trae

核心不是具体工具，而是掌握 Vibe Coding 工作流。

### Day 33-45

毕业项目建议优先选择：

1. 个人助理 Agent
2. AI 编程工作流助手
3. AI 视频自动化工作室

如果网络不稳定，最稳的是个人助理 Agent，因为它可以用国内模型 API 完成。

---

## 七、最稳技术栈建议

### Agent 开发

- Python 3.11
- OpenAI-compatible API
- LangGraph
- FAISS 或 Chroma
- SQLite
- Rich / Typer 做 CLI

### Web 展示

- Next.js 或 Vite React
- Tailwind CSS
- shadcn/ui 可选

### 视频方向

- Node.js LTS
- Remotion
- FFmpeg

### 本地模型

- Ollama 或 LM Studio
- 轻量模型做辅助实验

---

## 八、你的最佳执行策略

1. 先把 API 链路跑通，不要一开始折腾本地大模型。
2. Python 项目统一用 `uv`，减少环境污染。
3. 遇到网络下载问题，优先换镜像，不要反复重试浪费整晚。
4. RTX 3060 用来体验本地模型和加速，不作为主线依赖。
5. 45天主线用云端模型 API，保证 Agent 能力和学习效率。

