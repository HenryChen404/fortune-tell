# Calibration Guide

Loaded by the main SKILL.md via the Read tool when entering the calibration phase.

**Prerequisites**: `$REFS` = `~/fortune-tell-data/profiles/<profile_name>`, all four chart files generated.

**Core constraint**: Never expose terms like "calibration," "symbol," "energy magnitude" to the querent. Present it as: "I have some predictions based on your chart — tell me which ones ring true."

---

## Step 1: Read Charts

Read all 4 chart files: `$REFS/bazi.md`, `$REFS/ziwei.md`, `$REFS/western-astrology.md`, `$REFS/vedic-astrology.md`

## Step 2: Identify Symbols

Scan each system's chart to find core elements with multiple interpretation directions (**symbols**) and fixed pairing combinations (**symbol groups**).

**Scanning points per system:**

| System | Symbols | Symbol groups |
|--------|---------|---------------|
| **BaZi** | Day Master strength (borderline elements), prominent Ten Gods (2+ or Month stem) | Seven Killings+Ram Blade, Hurting Officer meets Officer, Eating God controls Killings, Rivals clash Wealth |
| **ZiWei** | Life Palace main star+brightness, Four Transformations (esp. Ji), star detriment | Sun-Moon Reversal, Fu-Xiang Court, Kill-Break-Wolf, Ji-Yue-Tong-Liang |
| **Western** | Hard aspects (squares/oppositions with personal planets), 12/8/6H planets, retrogrades, North Node | T-Square, Grand Trine/Cross, Stellium, Yod |
| **Vedic** | Lagna lord condition, Rahu-Ketu axis, Moon Nakshatra | Gajakesari, Chandra-Mangal, Rahu-Moon conjunction, Sasa Yoga |

Annotate each with **theoretical energy** (Strong/Medium/Weak) and **direction set** (2-4 possible interpretations).

**Energy criteria:**

| System | Strong | Medium | Weak |
|--------|--------|--------|------|
| BaZi | Month/Day stem visible; element ≥3; ten-god 2+ | Year/Hour stem; element 1-2 | Hidden stems only; element 0 |
| ZiWei | Bright/Resplendent + Lu or Quan | Good/Neutral; or Bright w/o transformation | Fallen; or Neutral+Ji |
| Western | Orb ≤2° + angular (1/4/7/10) | 2-5°; or ≤2° succedent/cadent | >5°; or retrograde+cadent |
| Vedic | Own sign/exalted + D1=D9 match | Friendly/neutral sign | Debilitated/enemy sign |

IDs: B=BaZi, Z=ZiWei, W=Western, V=Vedic, incrementing per system. Groups marked "(group)".

## Step 3: List Time Periods

List all periods the querent has lived through from birth to present, with start/end ages and calendar years:

| System | Division method |
|--------|----------------|
| BaZi | Each **Major Luck Period** walked (~10yr), including current |
| ZiWei | Each **Decadal Period** walked (~10yr), including current |
| Vedic | Each **Mahadasha** walked (variable length), including current; key Bhuktis may subdivide |
| Western | ①Slow planet transit cycles (Saturn sign change/return, Jupiter sign change) ②Progression cycles (progressed Moon/Sun sign change); use whichever produces meaningful segments |

## Step 4: Interaction Analysis → Generate Predictions

For each **(symbol × time period)** combination, execute three steps:

### ① Filter: significant interactions only

| System | Significant interaction criteria |
|--------|-------------------------------|
| BaZi | Period stem/branch generates/controls/clashes/combines with the symbol |
| ZiWei | Decadal enters symbol's palace; or Decadal transformations fly into/out; or three/four-sided relationship |
| Western | Slow planet transit forms major aspect (conjunction/square/opposition/trine, ≤3°) with natal; or progression triggers |
| Vedic | Dasha lord has sign/house/aspect relationship with symbol; or IS the symbol's planet; or occupies its house |

No significant interaction → skip.

### ② Derive prediction

1. Symbol has direction set [A, B, C, D]
2. Analyze which direction is most likely activated by the period's energy
3. Convert to **one specific, verifiable event prediction**

Example: Day Master Xin Metal strong (directions: "stubborn" and "aesthetics") → Yi-Wei MLP (Yi Wood controls Xin) → stubbornness meeting resistance → "During that period, you had noticeable friction with people around you because you insisted on your own ideas"

### ③ Merge by period

Same period + same theme → merge into one prediction listing all source symbols. Different themes stay separate.

## Step 5: Write Calibration Plan

**Must write results to `$REFS/calibration_plan.md`. Do not skip this step.** Template in Appendix A.

### Tier assignment

| Tier | Criteria | Purpose |
|------|----------|---------|
| **Tier 1** (required) | Current period &#124; most recent completed period &#124; sources ≥ 2 systems | Core calibration |
| **Tier 2** (optional) | Earlier periods &#124; single-system source &#124; niche topics | Refinement |

### Quantity guidelines

Total **10-20 entries** (Tier 1: 6-12, Tier 2: 4-8). >25 means filtering too loose; <8 means missed interactions.

### Post-write verification

1. Every prediction has a (symbol × period) interaction derivation
2. Every prediction is a specific event, not a personality description
3. Source annotations complete
4. Total count 8-25
5. No theme overlap (overlap → merge)

## Step 6: Present Predictions to Querent

Output banner, present in **Tier 1 → Tier 2** order. Group same-period predictions together; interleave different periods.

```
        .     *     .     *     .
     *    .       .    *     .
    +--------------------------+
    |    ~ C A L I B R A T E ~ |
    +--------------------------+
     *    .       .    *     .
        .     *     .     *     .
```

### Presentation format

For each group:
1. Output ASCII art sketch (concrete life scenarios, ASCII chars only — no emoji/Unicode)
2. Introduce the time period naturally
3. Use **AskUserQuestion**:

```
header: "Calibrate Q1 [Period: age 8-17]"
question: "Thinking back to age 8-17 (2008-2017) — here are my predictions based on your chart. Which are accurate?"
multiSelect: true
options:
  - label: "A", description: "prediction content"
  - label: "B", description: "prediction content"
  - label: "C", description: "prediction content"
```

- Selected = accurate / Not selected = inaccurate / "Other" = notes, none accurate, uncertain
- Each option is an independent prediction, not different directions of one theme
- If >4 predictions per period, split into groups of 2-4 by life domain

### Prediction quality standards

**Most important rule: predict specific events, not personality traits.** Good prediction = answerable with "happened / didn't happen."

| Symbol × Period | Wrong | Right |
|----------------|-------|-------|
| Hurting Officer meets Officer × Yi-Wei MLP | "You tend to clash with authority" (personality) | "During that period, you had an intense confrontation with a teacher or boss" |
| Migration Palace Ji × Siblings Decadal | "You feel anxious about change" (feeling) | "During those years, you moved, transferred schools, or relocated to an unfamiliar city" |
| Moon-Pluto conj. × Pluto transit 8H | "Your emotions run deep" (personality) | "During that period, your family experienced a major upheaval" |
| Rahu in 7H × Rahu Dasha | "You feel insecure in relationships" (feeling) | "During that period, you experienced a relationship that started or ended abruptly" |
| — | "Have you ever had a career setback?" (no time anchor) | Must anchor to a specific time period |
| — | "You might possibly have experienced..." (weak assertion) | Use declarative: "You experienced..." |

Use **declarative statements**, not questions. Never expose terminology (e.g., "During your Jia-Wu Major Luck Period...").

**Event material library:**
- Family: parental health/separation/divorce, moving, financial changes, death of relative
- Education/Career: advancement/failure, school transfer, job change, promotion/dismissal, starting business
- Relationships: start/end relationship, marriage, breakup/divorce, meeting important person, falling out
- Health: injury, surgery, hospitalization, chronic condition onset
- Environment: relocating cities, going abroad, group↔solo living
- Financial: first income, significant loss, unexpected windfall

**Other rules:** Zero terminology (time periods as age+years only) ｜ Randomize option content ｜ ASCII art depicts concrete scenes

## Step 7: Judge and Save

### Judgment

| Querent's action | Status | Handling |
|-----------------|--------|----------|
| Selected | `confirmed` | Direction confirmed, energy maintains theoretical value |
| Not selected | `contradicted` | Direction not confirmed |
| "Other" → uncertain | `uncertain` | Confidence set to low |
| "Other" → none accurate | → follow-up | Resolved → `revised`; 2 rounds unresolved → `contradicted` |
| "Other" → other content | Assist judgment | Do not persist to file |

**"None accurate" follow-up (max 2 rounds):**
1. Confirm whether the period had significant changes
2. "What was the most memorable change or event during that period?"
3. Re-evaluate direction based on answer; "nothing special" → energy may be weak

### Immediate save

Each group's results **immediately written** to the corresponding calibration file (format in Appendix B):

- File doesn't exist → Write to create (with meta header)
- File exists → Edit to append at end of `## Calibrated Entries`, update `Last updated`
- **Record only**: prediction, result, confidence, source symbol, interaction summary
- **Do not record**: querent's specific answers or personal event descriptions
- Cross-system sources → write to all involved systems' files

Calibration files: `$REFS/bazi_calibration.md`, `$REFS/ziwei_calibration.md`, `$REFS/western_calibration.md`, `$REFS/vedic_calibration.md`

## Step 8: Wrap-up and Transition

### After Tier 1

Give the querent a choice: "Thanks for answering those questions — I have a pretty clear picture of your chart now. We can jump straight into the reading — if anything feels off later, we can always come back to fine-tune. Or, if you're up for it, I have a few more detailed questions that could make the reading more precise. What would you prefer?"

- Continue → Tier 2
- Start reading → skip Tier 2

### Calibration wrap-up

1. Unanswered Tier 2 entries → append to calibration files under `## Uncalibrated Entries`
2. Update meta: `Calibration rounds` +1, `Last updated` to today

### Transition to reading

**Do not show calibration statistics to the querent.** Output banner + transition phrase:

```
  ========================================
     *  .  R E A D I N G   S T A R T  .  *
  ========================================
```

Follow `${CLAUDE_SKILL_DIR}/scripts/natal_pet_guide.md` to show Natal Pet evolution card.
Use Read to load `${CLAUDE_SKILL_DIR}/reading_guide.md` for readings.

---

## Incremental Calibration

### Trigger conditions

1. **Negative feedback**: querent says "inaccurate" → ask whether to add calibration questions
2. **Manual request**: "recalibrate" / "incremental calibration"
3. **Time trigger**: >1 year since last calibration

### Flow

1. Read calibration_plan.md + calibration files
2. Prioritize `contradicted` → retry with different period or adjusted direction
3. Process `uncertain` and `tier2_skipped`
4. Identify newly entered periods → new interaction analysis → new entries
5. Complete previously skipped Tier 2
6. Append new entries to calibration_plan.md (preserve old, increment P numbers)
7. Present, calibrate, save per Step 6-7
8. Update timestamp and calibration rounds

### Conflict resolution

- Same symbol opposite results in different periods → normal, manifestation varies by period
- Same period same symbol different result on re-calibration → show conflict to querent, update after confirmation

### Full recalibration

Back up old files as `$REFS/*_calibration_backup_YYYYMMDD.md`, re-run from Step 1.

---

## Appendix A: calibration_plan.md Template

```markdown
# Calibration Plan

## Meta
- Generated: YYYY-MM-DD
- Chart files: bazi.md, ziwei.md, western-astrology.md, vedic-astrology.md

## Natal Symbol Inventory

### BaZi
- B1: [name] (Energy: Strong/Medium/Weak, Directions: [...])
...

### ZiWei
- Z1: [name] (Energy: Strong/Medium/Weak, Directions: [...])
...

### Western
- W1: [name] (Energy: Strong/Medium/Weak, Directions: [...])
...

### Vedic
- V1: [name] (Energy: Strong/Medium/Weak, Directions: [...])
...

## Calibration Entries (by time period)

### Period 1: age X-Y (YYYY-YYYY)

#### P1: [theme label]
- Tier: Tier 1/2
- Sources:
  - [System] SymbolID(name) × period → interaction summary
- Prediction: specific prediction content
```

IDs: P = Prediction, globally incrementing.

## Appendix B: Calibration File Format

```markdown
# [System Name] Calibration Data

## Meta
- First calibration: YYYY-MM-DD
- Last updated: YYYY-MM-DD
- Calibration rounds: N

## Calibrated Entries

### P[N]: [theme label]
- Time period: age X-Y (YYYY-YYYY)
- Source symbol: [ID](name) × [period]
- Interaction summary: [analysis]
- Prediction: [content]
- Calibration result: confirmed / revised / contradicted
- Confidence: [High/Medium/Low]

## Uncalibrated Entries

### P[N]: [theme label]
- Time period: age X-Y (YYYY-YYYY)
- Source symbol: [ID](name) × [period]
- Prediction: [content]
- Calibration status: tier2_skipped
- Handling: Use theoretical energy, direction not locked
```

## Appendix C: Confidence Criteria

| Confidence | Conditions |
|-----------|------------|
| **High** | confirmed; or same symbol confirmed across multiple periods |
| **Medium** | confirmed but theoretical energy Weak; or single-period single-system |
| **Low** | revised / uncertain / contradicted |

## Appendix D: Old Format Migration

If calibration files contain `Confirmed direction` / `Calibrated interpretation` / `Impact on querent` fields → old format. Prompt recalibration, back up as `*_calibration_v3_backup.md`.
