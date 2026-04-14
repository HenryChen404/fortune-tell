# fortune-tell-experts

**Claude Code Skill** — 命理解读专家团

## 为什么做这个

单一命理体系的解读本质上是一个人的判断。不同体系源自不同文明、不同数学模型、不同哲学假设——如果它们独立得出了相同的结论，这个信号的可信度就远高于任何单一体系。

这和机器学习中的 ensemble method 是同一个思路：**多个弱判断器投票，比一个强判断器更稳健。**

## 三条规则

**规则一：先判断能不能答。** 不是所有问题都适合所有体系。命主问了一个问题，先判断哪些体系的理论框架能覆盖这个问题，只调用这些体系。不硬答。

**规则二：多数一致才输出。** 设适用体系数为 N，只有 ≥ N-1 个体系结论一致的点才会输出。2 个体系适用，必须 2 个都同意；3 个适用，至少 2 个同意。不满足阈值的解读直接丢弃，不会出现"A 体系认为…但 B 体系不支持"这种噪音。

**规则三：古话翻译成人话。** 这些体系发明于农业社会。"官星被克"不等于你要被贬官，而是你的权威感、管理能力、职场地位在这段时间承压。所有解读自动映射到现代语境。

## 四套引擎

| 体系 | 文明源头 | 排盘库 |
|------|----------|--------|
| 八字五行 | 中国 · 阴阳五行 | `lunar_python` |
| 紫微斗数 | 中国 · 星曜宫位 | `iztro` |
| 西洋占星 | 希腊 · 黄道行星 | `kerykeion` |
| 吠陀占星 | 印度 · 恒星体系 | `PyJHora` |

## 安装

```bash
git clone https://github.com/HenryChen404/fortune-tell.git .claude/skills/fortune-tell-experts
```

首次使用时自动安装 Python / Node 依赖。

## 使用

在 Claude Code 中直接说就行：

> 帮我看看今年事业运

> 我最近感情不太顺，能看看什么情况吗

触发词：算命、运势、命理、八字、紫微、星盘、吠陀、流年、大运、事业运、财运、感情运、健康运、命格、命盘

## 项目结构

```
.claude/skills/fortune-tell-experts/
├── SKILL.md              # Skill 定义与 prompt
├── scripts/
│   ├── bazi_chart.py      # 八字排盘
│   ├── ziwei_chart.js     # 紫微斗数排盘
│   ├── western_chart.py   # 西洋占星排盘
│   ├── vedic_chart.py     # 吠陀占星排盘
│   ├── requirements.txt   # Python 依赖
│   └── package.json       # Node 依赖
└── references/            # (git-ignored) 生成的个人命盘数据
```
