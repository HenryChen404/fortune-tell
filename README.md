# fortune-tell-experts

**Claude Code Skill** — 命理解读专家团 / Multi-system Fortune Telling Expert Panel

四套独立体系分别排盘、独立解读，交叉验证后只输出多数一致的结论。像专家委员会投票，而不是一个人拍脑袋。

Four independent systems generate charts and interpret separately. Only conclusions where the majority converge get surfaced — like a panel of experts voting, not one person guessing.

**[中文文档](cn/README.md)** | **[English](en/README.md)**

## Install

```bash
# English
git clone https://github.com/HenryChen404/fortune-tell.git ~/.fortune-tell
ln -s ~/.fortune-tell/en .claude/skills/fortune-tell-experts

# 中文
git clone https://github.com/HenryChen404/fortune-tell.git ~/.fortune-tell
ln -s ~/.fortune-tell/cn .claude/skills/fortune-tell-experts
```

## Update

```bash
cd ~/.fortune-tell && git pull
```

## License

MIT
