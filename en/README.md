[**中文版 Chinese Version**](../cn/README.md)

# fortune-tell-experts

**Agent Skill** — Multi-system Fortune Telling Expert Panel

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
curl -sL https://raw.githubusercontent.com/HenryChen404/fortune-tell/main/install.sh | bash
```

Auto-detects system language (Chinese → cn, otherwise → en). Dependencies are auto-installed on first use.

Update: `cd ~/.fortune-tell && git pull`

## Calibration System

After the first chart generation, the system automatically enters a calibration phase. Many symbols in natal charts (e.g., Seven Killings, Sun in the 12th House, Rahu-Ketu axis) are polysemous — the same symbol can manifest in completely different ways for different people. Calibration solves this through retrospective verification:

1. **Read all charts** and identify cross-system resonance symbols and single-system polysemous symbols
2. **Dynamically generate questions**, each anchored to a specific Major Luck Period/Annual Influence/Dasha time period, with 2-4 verifiable options
3. **Collect answers** — supports "Uncertain" (marked as uncalibrated) and "None of the above" (triggers follow-up questions exploring new directions); every question allows free-text supplements
4. **Save calibration data** to each system's independent calibration file (`bazi_calibration.md`, etc.); a cross-system question's results are written to all relevant system files simultaneously

Calibration is not one-time — if a reading feels off, you can always request incremental calibration.

## Natal Pet

After chart generation, the system assigns a Yu-Gi-Oh! style ASCII Art card based on your Zi Wei Dou Shu Life Palace main star — your Natal Pet. Each of the 14 main stars corresponds to a unique mythical creature.

The card is revealed in two steps:
1. **After charting**: An R-level preview card (art masked with `?`, ATK/DEF hidden)
2. **After calibration**: Cross-system resonance scan — how many of BaZi, Western, and Vedic charts resonate with your Life Palace star determines the evolution level (R → SR → SSR → SSSR)

ATK/DEF are dynamically calculated from chart data. Cards render in ANSI terminal colors with different visual effects per rarity.

## Usage

Just talk to Claude Code:

> What does my career look like this year?

> I've been having relationship troubles lately — can you take a look?

If you don't know your exact birth time, you can set it to **12:00 (noon)**.

Trigger words: fortune, horoscope, astrology, vedic, jyotish, birth chart, natal chart, career luck, love life

## Structure

```
en/                        # Symlinked to .claude/skills/fortune-tell-experts/
├── SKILL.md              # Skill definition & prompt
├── scripts/
│   ├── bazi_chart.py      # BaZi chart generator
│   ├── ziwei_chart.js     # Zi Wei Dou Shu chart generator
│   ├── western_chart.py   # Western astrology chart generator
│   ├── vedic_chart.py     # Vedic astrology chart generator
│   ├── natal_pet_card.py  # Natal Pet card generator
│   ├── requirements.txt   # Python deps
│   └── package.json       # Node deps
└── references/            # (git-ignored) Generated personal chart data
    └── <profile_name>/    # One subdirectory per person
        ├── birth-info.md      # Birth information
        ├── bazi.md            # BaZi chart
        ├── ziwei.md           # ZiWei chart
        ├── western-astrology.md  # Western chart
        ├── vedic-astrology.md    # Vedic chart
        ├── bazi_calibration.md   # BaZi calibration data
        ├── ziwei_calibration.md  # ZiWei calibration data
        ├── western_calibration.md # Western calibration data
        └── vedic_calibration.md   # Vedic calibration data
```

## License

MIT

