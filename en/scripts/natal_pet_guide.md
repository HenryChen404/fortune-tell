# Natal Pet Guide / 命盘宠物指南

This file defines when and how to invoke the Natal Pet card system.
本文件定义命盘宠物卡的调用时机和方式。

Variables used below / 以下使用的变量：
- `$SCRIPTS` = `${CLAUDE_SKILL_DIR}/scripts`
- `$REFS` = `~/fortune-tell-data/profiles/<profile_name>`
- `--lang` = `cn` or `en` (match the language used by the querent / 与命主使用的语言一致)

---

## Preview Mode / 预览模式

**When / 触发时机**: After first chart generation (step 8 of "No profiles" flow).
首次排盘完成后（「无档案」流程第 8 步）。

**Command / 命令**:

```bash
python3.11 "$SCRIPTS/natal_pet_card.py" \
  --ziwei "$REFS/ziwei.md" \
  --lang cn --mode preview
```

**Presentation / 展示方式**:

Introduce the Natal Pet in Veronica's voice. / 用维罗妮卡的口吻介绍命盘宠物。

CN example / 中文示例：
> 排盘完成了。顺便给你看看你的命盘宠物——**[卡牌名]**。它目前还是 R 级的雏形。等我们完成校准，如果其他三套命盘的能量与它产生共鸣，它可能会进化哦……

EN example / 英文示例：
> Charts are done! By the way, here's a peek at your Natal Pet — **[card name]**. It's still in R-level form for now. Once we finish calibration, if the energy from your other three chart systems resonates, it might evolve...

---

## Full Mode / 完整模式

**When / 触发时机**: When an existing profile has no `$REFS/natal_pet.md` yet (first time viewing pet for this profile).
已有档案但尚未生成 `$REFS/natal_pet.md` 时（该档案首次查看宠物）。

**Command / 命令**:

```bash
python3.11 "$SCRIPTS/natal_pet_card.py" \
  --ziwei "$REFS/ziwei.md" \
  --bazi "$REFS/bazi.md" \
  --western "$REFS/western-astrology.md" \
  --vedic "$REFS/vedic-astrology.md" \
  --lang cn --mode full
```

**Presentation / 展示方式**:

CN: 「对了，我发现你还没见过你的命盘宠物呢。让我给你看看……」
EN: "Oh, I just realized you haven't met your Natal Pet yet! Let me show you..."

---

## Evolution Display / 进化展示

**When / 触发时机**: After calibration is complete (Step 5 transition to reading).
校准完成后（第五步过渡到解读之前）。

**Command / 命令**: Same as Full Mode above. / 与完整模式相同。

**Presentation / 展示方式**:

Reveal the evolution result in Veronica's voice. / 用维罗妮卡的口吻揭示进化结果。

- If evolved (SR/SSR/SSSR): celebrate. / 如果进化了（SR/SSR/SSSR），庆祝。
- If stayed R: reassure that every card has unique value. / 如果保持 R 级，安慰命主并指出每张卡都有独特价值。

---

## Save & Print Path / 保存并打印路径

After generating the pet card (any mode except preview), save the card info to `$REFS/natal_pet.md`:

```markdown
# 命盘宠物 / Natal Pet

- 主星 / Star: <star name>
- 卡牌 / Card: <card name>
- 稀有度 / Rarity: <R/SR/SSR/SSSR>
- ATK: <value>
- DEF: <value>
- 共振 / Resonance: <resonating systems, comma-separated, or empty>
```

**After saving, print the full file path so the querent can view it. / 保存后，向命主打印完整文件路径以便查看。**

CN example / 中文示例：
> 你的命盘宠物卡已保存到：`~/fortune-tell-data/profiles/<名字>/natal_pet.md`

EN example / 英文示例：
> Your Natal Pet card has been saved to: `~/fortune-tell-data/profiles/<name>/natal_pet.md`
