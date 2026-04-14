# fortune-tell-experts

**Claude Code Skill** — 命理解读专家团 / Multi-system Fortune Telling Expert Panel

---

## 中文

### 简介

一个 [Claude Code](https://claude.ai/code) 技能（Skill），集成四大命理体系进行综合解读：

- **八字五行** — 基于 `lunar_python` 排盘
- **紫微斗数** — 基于 `iztro` 排盘
- **西洋占星** — 基于 `kerykeion` 排盘
- **吠陀占星 (Jyotish)** — 基于 `PyJHora` 排盘

### 核心机制

- **高共识过滤**：只输出多数体系结论一致的解读，不输出单一体系的孤证
- **古今映射**：将古代语境自动映射为现代表达
- **真实解读**：不谄媚、不引导，只给参考和依据

### 安装

```bash
cd your-project
git clone https://github.com/HenryChen404/fortune-tell.git .claude/skills/fortune-tell-experts
```

首次使用时，Skill 会自动检查并安装 Python / Node 依赖。

### 使用

在 Claude Code 中直接对话即可触发，例如：

> 帮我算算今年的事业运

> 我想看看我的命盘

触发词：算命、运势、命理、八字、紫微、星盘、吠陀、运程、流年、大运、事业运、财运、感情运、健康运、命格、命盘

---

## English

### Introduction

A [Claude Code](https://claude.ai/code) Skill that integrates four major fortune-telling systems for comprehensive readings:

- **BaZi (Four Pillars of Destiny)** — powered by `lunar_python`
- **Zi Wei Dou Shu (Purple Star Astrology)** — powered by `iztro`
- **Western Astrology** — powered by `kerykeion`
- **Vedic Astrology (Jyotish)** — powered by `PyJHora`

### Core Mechanisms

- **High-consensus filtering**: Only outputs interpretations where the majority of applicable systems agree
- **Ancient-to-modern mapping**: Automatically translates classical concepts into modern context
- **Honest readings**: No flattery, no leading — only references and evidence

### Installation

```bash
cd your-project
git clone https://github.com/HenryChen404/fortune-tell.git .claude/skills/fortune-tell-experts
```

On first use, the Skill will automatically check and install Python / Node dependencies.

### Usage

Just talk to Claude Code naturally. Trigger words include: fortune, horoscope, astrology, vedic, jyotish, birth chart, natal chart.

> What does my career look like this year?

> Can you read my birth chart?

---

## Project Structure

```
.claude/skills/fortune-tell-experts/
├── SKILL.md                 # Skill definition & prompt
├── scripts/
│   ├── bazi_chart.py        # BaZi chart generator
│   ├── ziwei_chart.js       # Zi Wei Dou Shu chart generator
│   ├── western_chart.py     # Western astrology chart generator
│   ├── vedic_chart.py       # Vedic astrology chart generator
│   ├── requirements.txt     # Python dependencies
│   └── package.json         # Node dependencies
└── references/              # (git-ignored) Generated chart data
```

## License

MIT
