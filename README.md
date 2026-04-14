# fortune-tell-experts

**Claude Code Skill** — Multi-system Fortune Telling Expert Panel

## Why This Exists

A single divination system is essentially one opinion. These four systems originate from different civilizations, different mathematical models, different philosophical assumptions — when they independently reach the same conclusion, that signal is far more credible than any single system alone.

Same idea as ensemble methods in ML: **multiple weak classifiers voting is more robust than one strong classifier.**

## Three Rules

**Rule 1: Assess answerability first.** Not every question fits every system. Given a question, the skill first determines which systems' theoretical frameworks actually cover it, and only invokes those. No forced answers.

**Rule 2: Majority agreement or silence.** Let N = number of applicable systems. A conclusion is only surfaced when ≥ N-1 systems agree. If 2 systems apply, both must agree; if 3 apply, at least 2 must agree. Below-threshold interpretations are discarded entirely — no "System A says X but System B disagrees" noise.

**Rule 3: Translate ancient to modern.** These systems were invented in agrarian societies. "Officer star under attack" doesn't mean you'll be demoted — it means your sense of authority, management capacity, and workplace standing are under pressure during this period. All readings are auto-mapped to modern context.

## Four Engines

| System | Origin | Chart Library |
|--------|--------|---------------|
| BaZi (Four Pillars) | China · Yin-Yang & Five Elements | `lunar_python` |
| Zi Wei Dou Shu | China · Star-Palace | `iztro` |
| Western Astrology | Greco-Roman · Tropical Zodiac | `kerykeion` |
| Vedic Astrology (Jyotish) | India · Sidereal System | `PyJHora` |

## Installation

```bash
git clone https://github.com/HenryChen404/fortune-tell.git .claude/skills/fortune-tell-experts
```

Dependencies are auto-installed on first use.

## Usage

Just talk to Claude Code:

> What does my career look like this year?

> I've been having relationship troubles lately — can you take a look?

If you don't know your exact birth time, you can set it to **12:00 (noon)**.

Trigger words: fortune, horoscope, astrology, vedic, jyotish, birth chart, natal chart, career luck, love life

## Structure

```
fortune-tell/                # Clone into .claude/skills/fortune-tell-experts/
├── SKILL.md              # Skill definition & prompt
├── scripts/
│   ├── bazi_chart.py      # BaZi chart generator
│   ├── ziwei_chart.js     # Zi Wei Dou Shu chart generator
│   ├── western_chart.py   # Western astrology chart generator
│   ├── vedic_chart.py     # Vedic astrology chart generator
│   ├── requirements.txt   # Python deps
│   └── package.json       # Node deps
└── references/            # (git-ignored) Generated personal chart data
```

## License

MIT

---

**中文版:** `git clone -b cn https://github.com/HenryChen404/fortune-tell.git .claude/skills/fortune-tell-experts`
