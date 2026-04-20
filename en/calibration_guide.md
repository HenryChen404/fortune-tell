# Calibration Guide

This file contains the complete calibration workflow. Loaded by the main SKILL.md via the Read tool when entering the calibration phase.

**Prerequisites**: Before executing calibration, ensure the following variables are set:
- `$SCRIPTS` = `${CLAUDE_SKILL_DIR}/scripts`
- `$REFS` = `~/fortune-tell-data/profiles/<profile_name>`
- All four chart files have been generated

---

After charts are generated and before the first reading, calibration must be completed. The internal purpose of calibration is: present multiple prediction directions to the querent based on each symbol group, have the querent confirm which predictions are accurate, and thereby lock in the interpretation direction. Energy magnitude is determined by the chart itself; calibration only confirms direction and makes minor adjustments when necessary.

**Calibration is fundamentally "prediction validation," aligned with professional practitioners' "chart verification" practice.** Professional fortune tellers predict past facts from the chart; the querent only confirms whether they're correct. Our adaptation: convert assertions into multiple-choice predictions — each symbol group presents 2-4 possible interpretation directions (described as observable behavioral/emotional patterns), and the querent selects which ones are accurate.

**Important: Do not expose calibration purpose to the querent.** The entire calibration process should be presented as "I have some predictions based on your chart — tell me which ones ring true." Do not use terms like "calibration," "symbol," "energy magnitude," or "polysemy" with the querent.

## Step 1: Read All Charts

Read all 4 chart files for the current profile:
- `$REFS/bazi.md`
- `$REFS/ziwei.md`
- `$REFS/western-astrology.md`
- `$REFS/vedic-astrology.md`

## Step 2: Identify Symbols, Time Periods, and Interaction Analysis

This step has three sub-steps: first identify natal symbols, then list time periods, then analyze interactions, filter, and merge to produce the calibration plan.

### 2a. Identify Natal Symbols

Scan each system's chart and identify core metaphysical elements with multiple possible interpretation directions.

**Symbol**: A single core element with multiple interpretation directions.
**Symbol group**: A combination of symbols within the same system that has a special pairing relationship, producing meanings beyond the individual symbols.

**Scanning points per system:**

**BaZi**: Day Master strength (borderline Five Elements statistics), prominent Ten Gods (appearing 2+ times or in the Month Pillar stem)
Symbol groups: Seven Killings + Ram Blade, Hurting Officer + Direct Officer, Eating God + Direct Seal, etc.

**ZiWei**: Life Palace main star + brightness, Four Transformations (especially Ji polysemy), star brightness in detriment
Symbol groups: Sun-Moon Reversal, Fu-Xiang Court Assembly, Kill-Break-Wolf combination, etc.

**Western**: Hard aspects (squares/oppositions involving personal planets), planets in 12th/8th/6th houses, retrograde planets, North Node
Symbol groups: T-Square, Grand Trine, Grand Cross, Stellium, Yod, etc.

**Vedic**: Lagna lord condition, Rahu-Ketu axis, Moon Nakshatra
Symbol groups: Gajakesari Yoga, Chandra-Mangal Yoga, Rahu-Moon conjunction, Sasa Yoga, etc.

Each symbol/group is annotated with:
- **Theoretical energy** (Strong/Medium/Weak), per the criteria below
- **Direction set** (2-4 possible interpretation directions)

| System | Strong | Medium | Weak |
|--------|--------|--------|------|
| **BaZi** | Month/Day stem visible; element count ≥3; ten-god appears 2+ times | Year/Hour stem visible; element count 1-2 | Only in hidden stems; element count 0 (missing) |
| **ZiWei** | Bright/Resplendent + Lu or Quan transformation | Good/Neutral; or Bright but no transformation | Fallen; or Neutral + Ji transformation |
| **Western** | Orb ≤2° + angular house (1/4/7/10) | Orb 2-5°; or ≤2° but succedent/cadent | Orb >5°; or retrograde + cadent |
| **Vedic** | Own sign/exalted + D1=D9 concordance | Friendly/neutral sign | Debilitated/enemy sign |

ID convention: B=BaZi, Z=ZiWei, W=Western, V=Vedic, incrementing within each system. Symbol groups are marked with "(group)" after the name.

### 2b. Identify Time Periods

List all time periods the querent has lived through from birth to present:

| System | Period division method |
|--------|----------------------|
| **BaZi** | Each **Major Luck Period** walked through (~10 years each), including current |
| **ZiWei** | Each **Decadal Period** walked through (~10 years each), including current |
| **Vedic** | Each **Mahadasha** walked through (variable length), including current; key Bhuktis may be subdivided |
| **Western** | Two overlapping systems: ①**Slow planet transit cycles** — divided by landmark transits (Saturn sign change, Saturn return, Jupiter sign change, etc.); ②**Progression cycles** — divided by progressed Moon sign change, progressed Sun sign change, etc. Use whichever produces meaningful segments |

Output: each system's time period list, with start/end ages and calendar years.

### 2c. Interaction Analysis, Filtering, and Merging

For each **(natal symbol × time period)** combination, execute three steps:

**Step 1: Filter — only significant interactions**

Determine whether the period's energy has a significant interaction with the natal symbol. Skip combinations without significant interaction.

| System | Significant interaction criteria |
|--------|-------------------------------|
| **BaZi** | Major Luck Period stem/branch has a generating/controlling/clashing/combining relationship with the symbol (e.g., period stem controls Day Master, period branch combines/clashes with a natal pillar, period triggers Ten God changes) |
| **ZiWei** | Decadal Period enters the palace where the symbol resides; or Decadal Four Transformations fly into/out of that palace; or Decadal palace forms a three-sided/four-sided relationship with the symbol's palace |
| **Western** | Slow planet transit forms a major aspect (conjunction/square/opposition/trine, orb ≤3°) with the natal planet/aspect; or progressed personal planet triggers the natal aspect |
| **Vedic** | Dasha lord has a sign/house/aspect relationship with the symbol's planet; or Dasha lord IS the symbol's planet; or Dasha lord occupies the house of the symbol |

No significant interaction → skip, no entry generated.

**Step 2: Derive specific prediction**

For each (symbol × period) that passes filtering, analyze how the period energy constrains the symbol's direction set, and derive **one specific event prediction**:

1. The natal symbol has direction set [A, B, C, D]
2. Analyze how the period's energy characteristics interact with the natal symbol — which direction is most likely activated in this period
3. Select the most likely direction, combined with the period context, and convert to **one specific, verifiable event prediction** (not a personality description)

Example:
- Natal symbol "Day Master Xin Metal strong" has directions including "stubborn/inflexible" and "refined aesthetics"
- In Yi-Wei Major Luck Period (Yi Wood Indirect Wealth controls Xin Metal) → the "stubbornness meeting resistance" direction is more likely activated
- Prediction: "During that period, you had noticeable friction or conflicts with people around you because you insisted on your own ideas"

**Step 3: Group by period and merge**

Within the same time period, if multiple symbols' predictions point to similar themes, merge into one comprehensive prediction:
- **Merge condition**: same period + same life theme (e.g., both point to "family upheaval" or "conflict with authority")
- Merged entries list all source symbols
- Predictions with different themes remain separate

### Output Calibration Plan File

After interaction analysis, **you must write the complete results to `$REFS/calibration_plan.md`**.

**If you find yourself wanting to skip this step and jump straight to asking questions, stop.** You cannot proceed to Step 3 without calibration_plan.md.

```markdown
# Calibration Plan

## Meta
- Generated: YYYY-MM-DD
- Chart files: bazi.md, ziwei.md, western-astrology.md, vedic-astrology.md

## Natal Symbol Inventory

### BaZi
- B1: [symbol name] (Theoretical energy: Strong/Medium/Weak, Direction set: [brief list])
- B2: [symbol group name] (group) (Theoretical energy: Strong/Medium/Weak, Direction set: [brief list])
...

### ZiWei
- Z1: [symbol name] (Theoretical energy: Strong/Medium/Weak, Direction set: [brief list])
...

### Western
- W1: [symbol name] (Theoretical energy: Strong/Medium/Weak, Direction set: [brief list])
...

### Vedic
- V1: [symbol name] (Theoretical energy: Strong/Medium/Weak, Direction set: [brief list])
...

## Calibration Entries (by time period)

### Period 1: age X-Y (YYYY-YYYY)

#### P1: [prediction theme label, e.g., "conflict with authority"]
- Tier: Tier 1
- Sources:
  - [BaZi] B2(Hurting Officer meets Officer) × Yi-Wei MLP → Yi Wood activates Hurting Officer, Officer clash intensifies
  - [Western] W2(Moon opposite Saturn) × Saturn transit through 2nd house → pressure axis activated
- Prediction: During that period, you had an intense confrontation with a teacher or authority figure

#### P2: [prediction theme label, e.g., "family environment change"]
- Tier: Tier 2
- Sources:
  - [ZiWei] Z3(Migration Palace Ju Men + Lu) × Siblings Decadal → Decadal migration palace activated
- Prediction: During those years, your family moved or you transferred to a new school

### Period 2: age X-Y (YYYY-YYYY)

#### P3: [prediction theme label]
...

### Period 3: age X-Y (YYYY-YYYY, current)

#### P4: [prediction theme label]
...
```

ID convention: P = Prediction, incrementing globally. Source format: `[System] SymbolID(name) × period name → interaction summary`.

### Tier Assignment

**Tier 1 (core round, always asked)**:
- Predictions for the current period (current Major Luck Period/Decadal/Dasha)
- Predictions for the most recently completed period
- Merged predictions with sources from ≥ 2 systems (high cross-validation value)

**Tier 2 (refinement round, querent can opt in or skip)**:
- Predictions for earlier periods
- Single-system source predictions
- Niche/specialized predictions

Record each entry's tier in calibration_plan.md.

### Quantity Guidelines

After filtering and merging, total calibration entries typically fall within **10-20**. Tier 1 typically contains **6-12**, Tier 2 contains **4-8**.

If over 25, check whether filtering was too loose or merging insufficient. If fewer than 8, check for missed significant interactions.

### Verify Plan

After writing calibration_plan.md, quick-check:
1. Every prediction has a clear (symbol × period) interaction derivation
2. Every prediction is a specific verifiable event, not a personality description
3. Source annotations are complete (system, symbol ID, period, interaction summary)
4. Total count is between 8 and 25
5. No two predictions have highly overlapping themes (overlap → should merge)

## Step 3: Present Predictions by Time Period, Calibrate, and Save

Based on the calibration entries in calibration_plan.md, present predictions to the querent by time period, collect confirmations, and save results immediately. After each time period's questions are answered, write results to the corresponding system's calibration file.

Before presenting the first question, output the following banner:

```
        .     *     .     *     .
     *    .       .    *     .
    +--------------------------+
    |    ~ C A L I B R A T E ~ |
    +--------------------------+
     *    .       .    *     .
        .     *     .     *     .
```

Then follow the **Tier 1 → Tier 2** order. Predictions from the same time period are grouped together. Different time periods are interleaved to avoid asking about the same era repeatedly.

### 3a. Presentation: Definitive Predictions

Calibration aligns with professional practitioners' **chart verification** practice: the practitioner makes **definitive predictions** about the querent's past based on the chart, and the querent simply confirms whether each prediction is accurate.

Each time period's predictions are presented as follows:

1. First output an ASCII art sketch (related to the time period or theme, ASCII characters only — no emoji or Unicode)
2. Introduce the time period with natural language
3. Use **AskUserQuestion** to present all predictions for that period:

```
header: "Calibrate Q1 [Period: age 8-17]"
question: "Thinking back to when you were 8-17 (2008-2017) — here are my predictions based on your chart. Which ones are accurate?"
multiSelect: true
options:
  - label: "A", description: "P1's prediction content"
  - label: "B", description: "P2's prediction content"
  - label: "C", description: "P3's prediction content"
```

- Selected = "this prediction is accurate"
- Not selected = "not accurate or not applicable"
- "Other" = additional notes / none are accurate / uncertain

**Each option is an independent prediction** — derived from different symbols' interactions within that time period, not different directions of the same theme. The practitioner makes definitive calls; the querent validates.

### Prediction Content Rules

**Predict specific events, not personality traits (the most important rule)**

- Each prediction describes an **objectively verifiable event or behavior**
- Good predictions: can be answered with "happened / didn't happen"
- Bad predictions: can only be answered with "do you feel like you're this kind of person"

**Right vs. wrong examples:**

| Symbol × Period | Wrong (personality/feeling) | Right (event prediction) |
|----------------|---------------------------|--------------------------|
| Hurting Officer meets Officer × Yi-Wei MLP | "You tend to clash with authority" | "During that period, you had an intense confrontation with a teacher or boss" |
| Migration Palace Ji × Siblings Decadal | "You feel anxious about changing environments" | "During those years, you moved homes, transferred schools, or relocated to an unfamiliar city" |
| Moon-Pluto conjunction × Pluto transit 8H | "Your emotions run deep" | "During that period, your family experienced a major upheaval (death of a relative, parents separating, etc.)" |
| Rahu in 7H × Rahu Dasha | "You feel insecure in relationships" | "During that period, you experienced a relationship that started or ended abruptly" |

Note: correct predictions use **declarative statements** ("You experienced..."), not questions ("Did you experience...?"). The practitioner is making predictions, not asking.

**Common chart verification event types** (material for generating predictions):
- **Family**: parental health changes, separation/divorce, moving, financial changes, death of a relative
- **Education/Career**: advancement/failure, school transfer, job change, promotion, dismissal, starting a business, certification
- **Relationships**: starting/ending a relationship, marriage, breakup/divorce, meeting an important person, falling out with someone
- **Health**: injury, surgery, hospitalization, onset of a chronic condition
- **Environment**: relocating to another city, going abroad, shifting from group to solo living (or vice versa)
- **Financial**: earning income independently for the first time, significant financial loss, unexpected windfall

**Zero terminology**
- Predictions must **contain no metaphysical terminology**: no "Major Luck Period," "Dasha," "Annual Influence," "transit," "Seven Killings," "Saturn," etc.
- Time periods expressed only in **age + calendar years**

**Randomized option content**
- Labels in A, B, C, D order, but **content randomly assigned** — don't put the most likely one at A

**ASCII art**
- Each question group includes a pure ASCII art sketch depicting **concrete life scenarios** (people, buildings, mountains, airplanes, hearts, trees, etc.) — not abstract borders or frames
- **Use only ASCII characters** (`-` `|` `/` `\` `_` `^` `*` `.` `~` `o` `=` `+` `(` `)` `<` `>` letters, digits, etc.), **no emoji or Unicode special symbols**

**Prediction types to avoid:**
- Exposing terminology: "During your Jia-Wu Major Luck Period..."
- Personality description: "You are an introverted person"
- Feeling description: "You felt a lot of pressure"
- No time anchor: "Have you ever had a career setback?"
- Insufficient assertion: "You might possibly have experienced..." → should be "You experienced..."

### Handling Too Many Predictions for One Period

If a time period has more than 4 predictions, split into multiple groups:
- 2-4 predictions per group
- Group by different life domains (e.g., "let's look at family first," "now about academics")
- Each group uses its own AskUserQuestion call

### 3b. Calibration Judgment

Based on the querent's selections, determine each prediction's calibration status:

| Querent's action | Calibration status | Handling |
|-----------------|-------------------|----------|
| Selected the prediction | `confirmed` | The interaction direction is confirmed; source symbol's calibration energy maintains theoretical value |
| Did not select | `contradicted` | The interaction direction was not confirmed |
| "Other" with "uncertain" | `uncertain` | Don't adjust theoretical energy, set confidence to low |
| "Other" with "none are accurate" | Enter follow-up | After resolution → `revised`; unresolvable → `contradicted` |
| "Other" with other content | Use in conversation to assist judgment | **Do not persist to calibration file** |

**Handling "none are accurate":**
1. Confirm whether the querent actually experienced significant changes during that period
2. Open-ended follow-up: "What was the most memorable change or event during that period?"
3. Re-evaluate the interaction analysis direction based on the querent's answer
4. If the querent says "nothing particularly happened": the energy may be weak or the interaction analysis may be off
5. Follow up for a maximum of 2 rounds. If still undetermined, mark as `contradicted`

### 3c. Immediate Save

Each question group's calibration results are **immediately written** to the corresponding system's calibration file:

- File doesn't exist → use Write to create, with meta header + first entry
- File exists → use Edit to append new entries at the end of `## Calibrated Entries`, and update `Last updated` date
- **Only record**: prediction content, calibration result, confidence, source symbol and interaction summary
- **Do not record**: the querent's specific answers, personal event descriptions

Calibration file list:
- `$REFS/bazi_calibration.md`
- `$REFS/ziwei_calibration.md`
- `$REFS/western_calibration.md`
- `$REFS/vedic_calibration.md`

Each entry format:

```markdown
### P[N]: [prediction theme label]
- Time period: age X-Y (YYYY-YYYY)
- Source symbol: [SymbolID](symbol name) × [period name]
- Interaction summary: [brief interaction analysis]
- Prediction: [specific prediction content]
- Calibration result: confirmed / revised / contradicted
- Confidence: [High/Medium/Low]
```

**Merged entry saving**: If a prediction's sources involve symbols from multiple systems (from Step 2 merging), write the result to all involved systems' calibration files. The `Source symbol` field lists all sources.

### Tier 1 Completion Transition

After all Tier 1 questions have been answered, give the querent a natural choice:

"Thanks for answering all those questions — I have a pretty clear picture of your chart now. We can jump straight into the reading — if anything feels off later, we can always come back to fine-tune. Or, if you're up for it, I have a few more detailed questions that could make the reading even more precise. What would you prefer?"

- Querent chooses to continue → proceed to Tier 2 questions
- Querent chooses to start reading → skip Tier 2, proceed to Step 4

Entries not covered due to skipped Tier 2 are marked as "uncalibrated" and use default weights.

## Step 4: Calibration Wrap-up

Since calibration results are saved immediately in Step 3, this step only handles wrap-up:

1. Scan calibration_plan.md and append all Tier 2 entries that were not asked to each system's calibration file under `## Uncalibrated Entries`
2. Update each calibration file's meta (`Calibration rounds` +1, `Last updated` to today)

Full calibration file format:

```markdown
# [System Name] Calibration Data

## Meta
- First calibration: YYYY-MM-DD
- Last updated: YYYY-MM-DD
- Calibration rounds: N

## Calibrated Entries

### P[N]: [prediction theme label]
- Time period: age X-Y (YYYY-YYYY)
- Source symbol: [SymbolID](symbol name) × [period name]
- Interaction summary: [brief interaction analysis]
- Prediction: [specific prediction content]
- Calibration result: confirmed / revised / contradicted
- Confidence: [High/Medium/Low]

## Uncalibrated Entries

### P[N]: [prediction theme label]
- Time period: age X-Y (YYYY-YYYY)
- Source symbol: [SymbolID](symbol name) × [period name]
- Prediction: [specific prediction content]
- Calibration status: tier2_skipped
- Handling: Use theoretical energy, interaction direction not locked
```

### Old Format Detection and Migration

If calibration files contain `Confirmed direction`, `Calibrated interpretation`, or `Impact on querent` fields (old format markers), prompt the querent that recalibration is needed for the new version. Back up old files as `*_calibration_v3_backup.md`.

### Confidence Determination Criteria

| Confidence | Conditions |
|-----------|------------|
| **High** | Prediction directly confirmed (confirmed); or same source symbol confirmed across multiple time periods |
| **Medium** | Prediction confirmed but source symbol's theoretical energy is Weak; or single-period single-system source |
| **Low** | `revised` (corrected after follow-up), `uncertain` (unsure), `contradicted` (prediction inaccurate) |

## Step 5: Natural Transition to Reading

After all questions have been asked, transition to the reading phase with natural language. **Do not present calibration statistics to the querent** (such as "calibrated X predictions," "Y accurate, Z inaccurate" — these are internal details).

First output the following banner, then use a natural transition phrase:

```
  ========================================
     *  .  R E A D I N G   S T A R T  .  *
  ========================================
```

Example transition phrases:
- "Thanks for sharing — I have a much clearer picture of your life story now. Let's move on to your question."
- "Great, those experiences really help me understand your chart better. What would you like to look at first?"

After calibration is complete, follow `${CLAUDE_SKILL_DIR}/scripts/natal_pet_guide.md`, Evolution Display to show the Natal Pet evolution card.

**After calibration, use the Read tool to load `${CLAUDE_SKILL_DIR}/reading_guide.md` and strictly follow the rules in that file for all readings.**

## Incremental Calibration

Calibration is not a one-time event. The querent can continue refining calibration data in subsequent sessions.

### Trigger Conditions

1. **Negative feedback trigger**: After a reading, if the querent says it was "off" or "inaccurate," ask whether to add calibration questions
2. **Manual trigger**: The querent explicitly requests "recalibrate" or "incremental calibration" — can focus on a specific area or automatically identify gaps
3. **Time-based trigger**: If more than 1 year has passed since the last calibration (compare `Last updated` timestamp in calibration files with the current date), suggest a refresh

### Incremental Flow

1. Read `$REFS/calibration_plan.md` and the relevant system's calibration files
2. Prioritize `contradicted` entries — retry with a different time period's interaction analysis or adjust the prediction direction
3. Identify `uncertain` and `tier2_skipped` entries
4. Identify Major Luck Periods/Decadal Periods/Dasha periods the querent has newly entered (not yet experienced at last calibration) — perform new interaction analysis with natal symbols to generate new calibration entries
5. If Tier 2 was skipped last time, prioritize completing Tier 2 questions
6. Append new entries to calibration_plan.md under the appropriate time period (preserve old entries, use incrementing P numbers)
7. Present predictions, calibrate, and save per Step 3 flow
8. Update `Last updated` timestamp and `Calibration rounds`

### Conflict Resolution

If incremental calibration results contradict original calibration (same source symbol gets opposite results in different periods):
- This is normal — the same symbol can manifest differently across periods
- If re-calibrating the same symbol in the same period produces different results: present the conflict to the querent, update after confirmation (preserve history)

### Full Recalibration

If the querent requests a complete redo:
- Back up old calibration files as `$REFS/*_calibration_backup_YYYYMMDD.md` (including calibration_plan.md)
- Re-run the full calibration workflow (from Step 1, regenerating calibration_plan.md)
