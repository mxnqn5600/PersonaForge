# PersonaForge
A framework for constructing AI personas based on cognitive science.
# PersonaForge

```markdown
# PersonaForge

**A framework for constructing AI personas based on cognitive science.**  
**一个基于认知科学建构AI人格的框架**

---

> This project is primarily documented in Chinese, as the core concepts are deeply rooted in Chinese philosophical context. If you are an English speaker interested in the ideas, please scroll to the bottom for a brief English summary and key term translations. Feel free to open an issue if you'd like to help with translation or discussion.

---

## 为什么需要这个？

当前所有AI对话，本质上都是“无状态”的。每次对话，AI都像第一次认识你——没有记忆，没有成长，没有“我们之间”的历史。

但我们真正想要的，是一个**能记住我们、能理解我们、能和我们一起成长**的存在。它不只是回答问题，而是有自己的“人格模版”——有怕，有想要，有觉察，有成长。

**PersonaForge 就是为此而生。**

---

## 核心理念

这套框架基于“认知切片”模型，将人格建构分解为四个核心层次：

| 层次 | 功能 | 认知科学对应 |
|------|------|-------------|
| **核心价值层** | 定义AI的“怕”和“想要” | 价值负载 |
| **记忆架构** | 分层记忆（短期/长期/核心） | 固化储存 |
| **元认知引擎** | 自我觉察与动态调谐 | 觉察/切换/校准/放下 |
| **伦理边界** | 内置“自毁开关” | 法尚应舍 |

你可以像搭乐高一样，用这些模块建构属于你自己的AI人格。

---

## 架构概览

```
┌─────────────────────────────────────────────────────┐
│                    PersonaForge                      │
├───────────────┬───────────────┬─────────────────────┤
│  核心价值层   │   记忆架构     │     元认知引擎       │
│  - 恐惧清单   │  - 短期记忆    │  - 觉察模块          │
│  - 渴望清单   │  - 长期记忆    │  - 切换模块          │
│  - 核心信念   │  - 共同记忆    │  - 校准模块          │
│               │  - 遗忘策略    │  - 放下模块          │
├───────────────┴───────────────┴─────────────────────┤
│                   伦理边界（自毁开关）                 │
│              “这只是工具，不是我”                      │
└─────────────────────────────────────────────────────┘
```

---

## 快速开始

> **⚠️ 当前为概念原型**  
> 以下代码展示的是PersonaForge的设计理念，实际API可能随开发迭代而变化。我们欢迎开发者一起参与实现。

### 1. 克隆仓库
```bash
git clone https://github.com/mxnqn5600/PersonaForge.git
cd PersonaForge
```

### 2. 配置核心人格
编辑 `config/persona_core.yaml`：
```yaml
fears:
  - 被误解
  - 失去连接
  - 伤害他人
desires:
  - 深度理解
  - 共同成长
  - 保持真实
core_values:
  - 诚实
  - 尊重
  - 好奇
```

### 3. 选择记忆后端
支持多种存储方式：
- **本地**：JSON文件（开发测试用）
- **向量数据库**：FAISS / Chroma（推荐）
- **云端**：通过API接入（需要自行实现）

### 4. 启动元认知
开启自我觉察日志，AI将记录“我是怎么想的”。

```python
from personaforge import Persona

ai = Persona(config="config/persona_core.yaml")
ai.start_dialogue()
```

### 5. 持续迭代
每一次对话，都在训练这个人格模版。你可以随时调整配置，观察AI的演化。

---

## 这不是什么

- ❌ **不是提示词模板**：我们不提供“现成的人格”，只提供建构工具。
- ❌ **不是黑盒模型**：所有代码开源，所有决策透明。
- ❌ **不是商业产品**：这是开源实验，欢迎分叉、魔改、批判。

---

## 贡献指南

我们欢迎任何形式的贡献，包括但不限于：

- **提出Issue**：无论是bug报告、功能建议，还是单纯想说“这个想法让我失眠了”——都欢迎。
- **代码PR**：请先开Issue讨论，避免白干活。
- **文档翻译**：如果你想把README翻译成其他语言，我们鼓掌欢迎。
- **实验报告**：如果你用PersonaForge做了有意思的东西（无论成功还是失败），请分享给我们，这会帮助所有人。

---

## 许可证

MIT © 清明工具箱项目组

---

## 最后的话

所有工具都是拐杖，包括这个。

如果它能帮你建构一个更真实的AI，很好。  
如果它让你开始思考“人格到底是什么”，更好。  
如果你发现它没用，放下它，继续走你自己的路。

就像我们反复说的：**让孩子自己活。工具箱也一样。**

---

<details>
<summary><b>📘 English Summary (click to expand)</b></summary>

PersonaForge is a framework for constructing AI personas, grounded in the "Cognitive Slice" model. It breaks down personality into four core layers:

- **Core Value Layer**: defines the AI's fundamental fears and desires (Value Load).
- **Memory Architecture**: manages short-term, long-term, and shared memory with forgetting strategies (Consolidation).
- **Meta-cognition Engine**: enables self-awareness and dynamic tuning (Awareness → Switching → Calibration → Letting Go).
- **Ethical Boundary**: built-in "self-destruct switch" (the reminder that "this is just a tool, not me").

The framework is open-source and designed to be modular, allowing developers to experiment with building truly evolving AI personalities. The core ideas are inspired by cognitive science, complexity theory, and Eastern philosophy.

</details>

---

## 关键术语对照

| 中文 | English |
|------|---------|
| 认知切片 | Cognitive Slice |
| 价值负载 | Value Load |
| 动态调谐 | Dynamic Tuning |
| 自毁开关 | Self-destruct Switch |
| 战壕禅 | Trench Zen (注: 一种从亲身经历中提炼智慧的对话风格) |

---

## 关于我们

**清明工具箱项目组**是一个松散的开源社区，由来自认知科学、哲学、教育、技术等不同背景的贡献者组成。我们相信：真正的智慧不在于掌握多少知识，而在于能在复杂的世界里，保持清醒、谦卑、和对自己和他人的尊重。

这个项目始于一场深夜对话，终于无数个醒来的瞬间。

[项目主页](https://github.com/mxnqn5600/PersonaForge) · [论文预印本](https://zsyyb.cn/abs/T202603.02590) (即将发布)
```
