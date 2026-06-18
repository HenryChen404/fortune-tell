# Chart Verification Guide

Loaded by the main SKILL.md via the Read tool when entering the chart verification phase.

**Prerequisites**: `$REFS` = `~/fortune-tell-data/profiles/<profile_name>`, all four chart files generated.

**Core constraint**: Never expose internal terms like "natal indicator," "innate strength," "symbol meanings," "baseline" to the querent. The term "chart verification" is acceptable — practitioners openly say "let me verify the chart first." The querent is a visiting guest who does not understand these terms — use natural conversational language throughout.

---

## Four Layers of Chart Verification

Chart verification is not just about "locking in the reading direction." It must resolve four layers of questions:

| Layer | Question | Action |
|-------|----------|--------|
| 1 | Is the chart itself correct (birth hour, calendar system) | Pre-check + time correction |
| 2 | Which specific natal indicator manifested (Travel Star = business trip or job change) | Lock manifestation form |
| 3 | The querent's life baseline ("financial loss" = bankruptcy or a few months' salary) | Adjust baseline |
| 4 | Model confirmation (full match) | Chart confirmed |

### Four Feedback Scenarios

| Scenario | Querent's response | Internal action |
|----------|-------------------|-----------------|
| **Complete mismatch** | "No, that year was smooth" | Suspect wrong birth hour -> try adjacent hours, re-chart |
| **Right indicator, wrong event** | "Didn't move, but was on a long business trip" | Energy direction correct, lock specific manifestation form |
| **Right direction, wrong magnitude** | "Mom's fine, just stressed about buying a house" | Energy domain correct but baseline differs, adjust future prediction intensity |
| **Complete match** | "Spot on" | Chart confirmed, high confidence |

---

## Phase 0: Pre-check

**Purpose**: Rule out obvious time errors before formal verification.

### Step 0.1: Daylight Saving Time Detection

Birth year 1986-1991 and birthplace in China -> naturally ask the querent:

> "About the birth time you gave me — China used daylight saving time for a few years, where clocks were set one hour forward. Is the time you gave me the original time from the hospital records, or has it already been adjusted?"

If the querent is unsure or says it is the original record -> mark as "pending -1 hour re-verification." In Phase 4, if widespread mismatches appear, prioritize re-charting with the time minus 1 hour.

### Step 0.2: Hour Boundary Detection

Check if the birth time falls within +/-15 minutes of a traditional hour boundary (note: use the true solar time corrected value).

If within boundary range -> annotate "boundary hour" in `birth-info.md`. If widespread mismatches appear during verification, prioritize trying the adjacent hour.

### Step 0.3: Solar/Lunar Calendar Confirmation

Already confirmed during birth info collection; retained.

### Write

Append detection results to `$REFS/birth-info.md`:

```markdown
## Pre-check
- Daylight Saving: Not applicable / Pending verification / Already adjusted
- Hour boundary: No risk / Boundary hour (XX hour / XX hour)
- Calendar confirmed: Solar
```

---

## Phase 1: Extract Natal Indicators and Time Periods

### Step 1.1: Read Charts

Read all 4 chart files: `$REFS/bazi.md`, `$REFS/ziwei.md`, `$REFS/western-astrology.md`, `$REFS/vedic-astrology.md`

### Step 1.2: Extract Natal Indicators

Scan each system's chart to find core elements with multiple interpretation directions (**natal indicators**) and fixed pairing combinations (**chart patterns**).

**Scanning points per system:**

| System | Natal indicators | Chart patterns |
|--------|---------|---------------|
| **BaZi** | Day Master strength (borderline elements), prominent Ten Gods (2+ or Month stem) | Seven Killings+Ram Blade, Hurting Officer meets Officer, Eating God controls Killings, Rivals clash Wealth |
| **ZiWei** | Life Palace main star+brightness, Four Transformations (esp. Ji), star detriment | Sun-Moon Reversal, Fu-Xiang Court, Kill-Break-Wolf, Ji-Yue-Tong-Liang |
| **Western** | Hard aspects (squares/oppositions with personal planets), 12/8/6H planets, retrogrades, North Node | T-Square, Grand Trine/Cross, Stellium, Yod |
| **Vedic** | Lagna lord condition, Rahu-Ketu axis, Moon Nakshatra | Gajakesari, Chandra-Mangal, Rahu-Moon conjunction, Sasa Yoga |

Annotate each natal indicator / chart pattern with **innate strength** (Strong/Medium/Weak) and **symbol meanings** (2-4 possible interpretation directions).

**Innate strength criteria:**

| System | Strong | Medium | Weak |
|--------|--------|--------|------|
| BaZi | Month/Day stem visible; element >=3; ten-god 2+ | Year/Hour stem; element 1-2 | Hidden stems only; element 0 |
| ZiWei | Bright/Resplendent + Lu or Quan | Good/Neutral; or Bright w/o transformation | Fallen; or Neutral+Ji |
| Western | Orb <=2 deg + angular (1/4/7/10) | 2-5 deg; or <=2 deg succedent/cadent | >5 deg; or retrograde+cadent |
| Vedic | Own sign/exalted + D1=D9 match | Friendly/neutral sign | Debilitated/enemy sign |

IDs: B=BaZi, Z=ZiWei, W=Western, V=Vedic, incrementing per system. Chart patterns marked "(pattern)".

### Step 1.3: List Time Periods

List all periods the querent has lived through from birth to present, each with start/end ages and calendar years:

| System | Division method |
|--------|----------------|
| BaZi | Each **Major Luck Period** walked (~10yr), including current |
| ZiWei | Each **Decadal Period** walked (~10yr), including current |
| Vedic | Each **Mahadasha** walked (variable length), including current; key Bhuktis may subdivide |
| Western | (1) Slow planet transit cycles (Saturn sign change/return, Jupiter sign change) (2) Progression cycles (progressed Moon/Sun sign change); use whichever produces meaningful segments |

---

## Phase 2: Transit Analysis -> Generate Predictions

### Step 2.1: Filter for Significant Activations

For each **(natal indicator x time period)** combination, keep only those with significant activations:

| System | Significant activation criteria |
|--------|-------------------------------|
| BaZi | Period stem/branch generates/controls/clashes/combines with the natal indicator |
| ZiWei | Decadal enters natal indicator's palace; or Decadal transformations fly into/out; or three/four-sided relationship |
| Western | Slow planet transit forms major aspect (conjunction/square/opposition/trine, <=3 deg) with natal; or progression triggers |
| Vedic | Dasha lord has sign/house/aspect relationship with natal indicator; or IS the natal indicator's planet; or occupies its house |

No significant activation -> skip.

### Step 2.2: Split Symbol Meanings into Independent Options

For each combination with a significant activation:

1. Natal indicator has symbol meanings [A, B, C, D]
2. Analyze which directions the period's influence activates
3. **Split each possible manifestation form into an independent option** for the querent to multi-select

**Core rule**: Do not combine multiple possibilities into one "A or B" statement. Instead, split them into independent options. This captures two layers of information simultaneously — whether the indicator manifested at all + which specific form it took.

Example:

Natal indicator "Travel Star (change/movement)" x Major Luck Period "Yi-Wei" -> symbol meanings include [moving, school transfer, long business trip, change of environment]

Generate 4 independent options:
- "Moved house or changed cities"
- "Transferred schools"
- "Spent an extended period in a completely unfamiliar environment"
- "Frequently traveled for work or was constantly on the move"

### Step 2.3: Tag Probe Type

Tag each option with a **probe type** (internal use only, never exposed to querent):

| Type | Meaning | Purpose |
|------|---------|---------|
| `time_diagnostic` | This option is highly dependent on birth hour — wrong hour flips the direction | Verify whether the birth hour is correct |
| `form_probe` | This option is one of multiple manifestation forms of a natal indicator | Lock the querent's specific manifestation pattern |
| `magnitude_probe` | The severity of this option can measure the baseline | Determine the querent's life baseline |

### Step 2.4: Group by Period

- Options from the same period go into one group
- Different manifestation options from the same natal indicator stay together (but the querent does not see the grouping logic)
- More than 4 options in one period -> split into multiple groups by life domain (2-4 each, AskUserQuestion tool is limited to 2-4 options)

---

## Phase 3: Write Verification Plan

**Must write results to `$REFS/calibration_plan.md`. Do not skip this step and go straight to asking the querent.** Template in Appendix A.

### Tier Assignment

| Tier | Criteria | Purpose |
|------|----------|---------|
| **Tier 1** (required) | Current period &#124; most recent completed period &#124; sources >= 2 systems | Core verification |
| **Tier 2** (optional) | Earlier periods &#124; single-system source &#124; niche topics | Refinement |

### Quantity Guidelines

Total options **15-20** (Tier 1: 10-14, Tier 2: 5-6). Split each natal indicator into 2-3 manifestation options — no need to exhaustively list every possibility. Keep the total manageable to minimize interaction rounds.

### Probe Coverage Requirements

- Tier 1 must include at least 3-4 `time_diagnostic` options
- Each system must have at least 2 `form_probe` options
- For natal indicators with innate strength "Strong," include `magnitude_probe` options

### Post-write Verification

1. Every option has a (natal indicator x period) activation derivation
2. Every option is a specific event, not a personality description
3. Source annotations complete
4. Different manifestation forms of the same natal indicator are within the same group

---

## Phase 4: Present and Collect Feedback

### Round 1: Quick Scan

Output banner, **present ALL Tier 1 first, then Tier 2**. Even if Tier 1 and Tier 2 options belong to the same time period, present them separately — Tier 2 always comes after all Tier 1 is complete.

```
        .     *     .     *     .
     *    .       .    *     .
    +--------------------------+
    | ~ V E R I F I C A T I O N ~ |
    +--------------------------+
     *    .       .    *     .
        .     *     .     *     .
```

For each group:
1. Output ASCII art sketch (concrete life scenarios, ASCII chars only — no emoji/Unicode)
2. Introduce the time period naturally
3. Use **AskUserQuestion**:

```
header: "Verify Q1 [Period: age 13-17]"
question: "Thinking back to age 13-17 (2013-2017) — which of these things happened to you? If something is roughly right but the details are off, skip it for now — we'll discuss those in a moment."
multiSelect: true
options:
  - label: "A", description: "Moved house or changed cities"
  - label: "B", description: "Transferred schools or changed classes"
  - label: "C", description: "Had an intense conflict with a teacher or authority figure"
  - label: "D", description: "Poured a lot of time into a particular hobby or interest"
```

When a time period has more options, split into sub-groups presented sequentially (2-4 options each):

```
header: "Verify Q1b [Period: age 13-17, family]"
question: "Same period, regarding family:"
multiSelect: true
options:
  - label: "E", description: "Your family went through a significant change"
  - label: "F", description: "A noticeable tension appeared in your relationship with family"
```

- Selected = happened
- Not selected = to be followed up
- "Other" = none accurate / additional info

**Internal interpretation of selections** (not visible to querent):

| Selection pattern | Internal judgment |
|-------------------|-------------------|
| 1-2 items selected within same natal indicator group | Indicator verified + specific manifestation form locked |
| All items selected within same natal indicator group | Indicator strongly manifested (amplified) |
| Items selected across groups | Judge each group independently |

**Presentation rules:**
- Zero terminology (time periods as age + years only)
- Randomize option order within each group (do not let options from the same natal indicator always appear adjacent)
- **2-4 options per group** (AskUserQuestion tool is hard-limited to 2-4 options)
- If a time period has >4 options → split into sub-groups by life domain
- Use declarative statements, not questions

### Prediction Quality Standards

**Most important rule: predict specific events, not personality traits.** Good prediction = answerable with "happened / didn't happen."

| Natal indicator x Period | Wrong | Right |
|--------------------------|-------|-------|
| Hurting Officer meets Officer x Yi-Wei MLP | "You tend to clash with authority" (personality) | "During that period, you had an intense confrontation with a teacher or boss" |
| Migration Palace Ji x Siblings Decadal | "You feel anxious about change" (feeling) | "During those years, you moved, transferred schools, or relocated to an unfamiliar city" |
| Moon-Pluto conj. x Pluto transit 8H | "Your emotions run deep" (personality) | "During that period, your family experienced a major upheaval" |
| Rahu in 7H x Rahu Dasha | "You feel insecure in relationships" (feeling) | "During that period, you experienced a relationship that started or ended abruptly" |
| — | "Have you ever had a career setback?" (no time anchor) | Must anchor to a specific time period |
| — | "You might possibly have experienced..." (weak assertion) | Use declarative: "You experienced..." |

**Event material library:**
- Family: parental health/separation/divorce, moving, financial changes, death of relative
- Education/Career: advancement/failure, school transfer, job change, promotion/dismissal, starting business
- Relationships: start/end relationship, marriage, breakup/divorce, meeting important person, falling out
- Health: injury, surgery, hospitalization, chronic condition onset
- Environment: relocating cities, going abroad, group vs. solo living
- Financial: first income, significant loss, unexpected windfall
- Psychological: noticeable emotional low, personality shift, period of confusion

**Other rules:** Zero terminology (time periods as age+years only) | ASCII art depicts concrete scenes | Option descriptions should use concrete scenarios ("entered university / started a new school"), not abstract concepts ("entered a rule-bound environment")

### Round 2: Follow Up on Every Unselected Option

**Every unselected option must be followed up until enough information is gathered for classification. Do not skip or assume defaults.**

Follow-up is done through **natural conversation**, not structured UI. In Veronica's voice:

**Follow-up examples:**

> Veronica: "You didn't select 'moved house or changed cities.' I just want to double-check — even though you didn't move, was there some similar kind of change during those years? Like your work environment changed, or your daily routine suddenly became very different?"
>
> Querent: "Didn't move, but that year I was sent on a long business trip for most of the year"
>
> -> Internal judgment: **Right indicator, wrong event.** "Travel Star" actually manifested as "extended business trip."

> Veronica: "One of the items mentioned 'a family elder had health issues.' You didn't select that — was there truly nothing, or was there something but not as serious?"
>
> Querent: "Mom was fine, just really stressed about buying a house that year"
>
> -> Internal judgment: **Right direction, wrong magnitude.** "Seal Star under attack" manifested as asset pressure rather than family health issues.

> Veronica: "There was also one about 'relationships being tense with people around you.' How about that one?"
>
> Querent: "No, that year was actually pretty smooth"
>
> -> Internal judgment: **Complete mismatch.** Mark as contradicted.

**Follow-up rules:**

1. Warm, natural tone — no terminology whatsoever
2. Start with open-ended probing ("Was there anything similar?"), then follow up on specifics based on the response
3. Do not ask the querent to classify — classification is done internally based on their answers
4. If the querent's answer is vague -> ask one more specific question to help determine the classification
5. Multiple items from the same period can be naturally chained together in follow-up
6. The querent's specific events are **not written to the calibration file** (privacy protection) — only record the classification result and abstract manifestation form
7. **Maximum 2 rounds of follow-up per unselected option**: Round 1 = open-ended probe, Round 2 = specific confirmation. If still unclear after 2 rounds → `uncertain`

**Internal classification logic** (not visible to querent):

| Querent's response pattern | Scenario | Stored status |
|---------------------------|----------|---------------|
| Selected an option | Complete match | `confirmed` |
| Same natal indicator group: partial selection | Specific form locked | `confirmed_form` (selected form is locked) |
| "Something similar happened but not what you described, it was XX" | Right indicator, wrong event (new manifestation form) | `confirmed_form` + manifestation_form |
| "Yes but not that serious" / "Much worse than you described" | Right direction, wrong magnitude | `confirmed_scaled` + magnitude_adjustment |
| "Not at all" / "That year was fine" | Complete mismatch | `contradicted` |
| "Can't remember" / "Maybe but not sure" | Uncertain | `uncertain` |

### Round 3: Time Correction (Conditionally Triggered)

Initiate time correction when any of the following occurs:

- `contradicted` entries exceed 60%
- All `time_diagnostic` options are contradicted
- Querent explicitly says "none of this is right"

**Steps:**

**Step 1: Collect the querent's major life events**

> Veronica: "It looks like quite a few of my predictions were off — the birth time might have a small error. But don't worry, I'll take a different approach to confirm. Can you tell me 3-5 of the most significant turning points in your life? For example, when you changed jobs, went through a major relationship change, moved, or had a health issue? Rough years are fine."

**Step 2: Re-chart with adjacent hours**

| System | Offset | Notes |
|--------|--------|-------|
| BaZi | +/-1 traditional hour (+/-2 clock hours) | Hour Pillar changes directly, may affect structure and useful god |
| ZiWei | +/-1 traditional hour (+/-2 clock hours) | Life Palace shifts, all 12 palaces re-arranged |
| Western | +/-1-2 clock hours | ASC may change signs, all houses shift |
| Vedic | +/-1-2 clock hours | Lagna may change signs, Nakshatra may change, Dasha sequence may re-order |

Generate 2-3 candidate charts (original + shifted earlier + shifted later).

**Step 3: Reverse-engineer from the querent's major events**

Compare the querent's major events against each candidate chart's major periods/transits:
- For each candidate, do the major period / annual influences show significant activation in the years the querent's events occurred?
- The candidate with the highest match rate wins

**Step 4: Verification predictions**

Based on the candidate chart, generate 2-3 new predictions (selecting entries where the old and new charts differ most) and present them to the querent for confirmation.

**Step 5: Judgment**

| Result | Action |
|--------|--------|
| New predictions mostly match | Adopt the new hour. Update birth-info.md (record both original and corrected hours), re-chart all four systems, restart from Phase 1 |
| Still wrong | Investigate solar/lunar calendar mix-up -> ask querent -> convert and re-chart |
| Still indeterminate | Mark "birth hour uncertain," apply "uncertain-default-to-weak" principle |

**Step 6: "Uncertain-default-to-weak" principle**

If the birth hour ultimately cannot be determined:
- Conclusions consistent across both candidate charts -> high confidence
- Inconsistent conclusions -> low confidence, honestly tell the querent these parts are uncertain
- Never force-pick one hour just to "give a clear conclusion"

---

## Phase 5: Save and Baseline

### Immediate Save

Each group's results **immediately written** to the corresponding calibration file (format in Appendix B):

- File doesn't exist -> Write to create (with meta header)
- File exists -> Edit to append at end of `## Verified Entries`, update `Last updated`
- **Record**: prediction option, result status, confidence, source natal indicator, manifestation form, baseline adjustment
- **Do not record**: querent's specific answers or personal event descriptions
- Cross-system sources -> write to all involved systems' files

Calibration files: `$REFS/bazi_calibration.md`, `$REFS/ziwei_calibration.md`, `$REFS/western_calibration.md`, `$REFS/vedic_calibration.md`

### Baseline Synthesis

After all entries are saved, perform a comprehensive analysis of verification results and generate a "Querent Baseline Summary," written to the `## Querent Baseline` section at the top of each calibration file:

Analysis dimensions:

1. **Manifestation tendency**: Among `confirmed_form` entries, which category does the manifestation form lean toward (inner psychological vs. external events vs. family/relationship vs. material/financial)
2. **Magnitude baseline**: Among `confirmed_scaled` entries, distribution of magnitude_adjustment. Amplified count > diminished → "leans strong"; diminished > amplified → "leans weak"; roughly equal → "standard"
3. **Primary manifestation domains**: Domain distribution of all confirmed entries, ranked by confirmed count in descending order
4. **Family buffering**: Confirmed_scaled (diminished) entries involving family members >= 2 → "high"; 1 → "medium"; 0 → "low"

### Wrap-up and Transition

#### After Tier 1

Give the querent a choice:

> "Thanks for answering those questions — I have a pretty clear picture of your chart now. We can jump straight into the reading — if anything feels off later, we can always come back to fine-tune. Or, if you're up for it, I have a few more detailed questions that could make the reading more precise. What would you prefer?"

- Continue -> Tier 2
- Start reading -> skip Tier 2

#### Verification Wrap-up

1. Unasked Tier 2 entries -> append to calibration files under `## Unverified Entries`
2. Update meta: `Verification rounds` +1, `Last updated` to today

#### Transition to Reading

**Do not show verification statistics to the querent.** Output banner + transition phrase:

```
  ========================================
     *  .  D E L I N E A T I O N   S T A R T  .  *
  ========================================
```

Follow `${CLAUDE_SKILL_DIR}/scripts/natal_pet_guide.md` to show Natal Pet evolution card.
Use Read to load `${CLAUDE_SKILL_DIR}/reading_guide.md` for readings.

---

## Incremental Verification

### Trigger Conditions

1. **Negative feedback**: querent says "inaccurate" -> ask whether to add verification questions
2. **Manual request**: "re-verify" / "incremental verification"
3. **Time trigger**: >1 year since last verification

### Flow

1. Read calibration_plan.md + calibration files
2. Re-examine existing verification data:
   - `contradicted` -> is there a new period where the same natal indicator can be re-tested?
   - `confirmed_form` -> has the manifestation form changed due to a new life phase?
   - `confirmed_scaled` -> does the baseline need adjustment due to life changes?
3. Process `uncertain` and `tier2_skipped`
4. Identify newly entered periods -> new activation analysis -> new entries
5. Complete previously skipped Tier 2
6. Append new entries to calibration_plan.md (preserve old entries, increment numbering)
7. Present, verify, save per Phase 4 flow
8. Recalculate baseline summary
9. Update timestamp and verification rounds

### Conflict Resolution

- Same natal indicator with opposite results in different periods -> normal, manifestation varies by period
- Same period, same natal indicator, different result on re-verification -> show conflict to querent, update after confirmation
- New verification contradicts old baseline -> recalculate baseline

### Full Re-verification

Back up old files as `$REFS/*_calibration_backup_YYYYMMDD.md`, restart from Phase 0.

---

## Appendix A: calibration_plan.md Template

```markdown
# Verification Plan

## Meta
- Generated: YYYY-MM-DD
- Chart files: bazi.md, ziwei.md, western-astrology.md, vedic-astrology.md
- Pre-check: Daylight Saving [status] / Hour boundary [status]

## Natal Indicator Inventory

### BaZi
- B1: [name] (Innate strength: Strong/Medium/Weak, Symbol meanings: [...])
...

### ZiWei
- Z1: [name] (Innate strength: Strong/Medium/Weak, Symbol meanings: [...])
...

### Western
- W1: [name] (Innate strength: Strong/Medium/Weak, Symbol meanings: [...])
...

### Vedic
- V1: [name] (Innate strength: Strong/Medium/Weak, Symbol meanings: [...])
...

## Cross-system Natal Indicator Groups
- G1: [B1 + W3 + V2] (Shared theme: ...)
...

## Verification Entries (by time period)

### Period 1: age X-Y (YYYY-YYYY)

#### P1: [theme label]
- Tier: Tier 1/2
- Probe type: time_diagnostic / form_probe / magnitude_probe
- Sources:
  - [System] IndicatorID(name) x period name -> activation summary
- Options:
  - P1a: "Description of manifestation form A"
  - P1b: "Description of manifestation form B"
  - P1c: "Description of manifestation form C"
```

IDs: P = Prediction group, globally incrementing. P1a/P1b/P1c = different options within the same natal indicator group.

## Appendix B: Calibration File Format

```markdown
# [System Name] Calibration Data

## Meta
- First calibration: YYYY-MM-DD
- Last updated: YYYY-MM-DD
- Verification rounds: N
- Birth hour status: confirmed / adjusted (original XX -> XX) / uncertain

## Querent Baseline
- Manifestation tendency: [inner psychological / external events / family-relationship / material-financial]
- Magnitude baseline: [standard / amplified / diminished]
- Primary manifestation domains: [domain ranking]
- Family buffering: [high / medium / low]

## Verified Entries

### P[N]: [theme label]
- Time period: age X-Y (YYYY-YYYY)
- Source natal indicator: [ID](name) x [period name]
- Activation summary: [analysis]
- Prediction option: [option content presented to querent]
- Verification result: confirmed / confirmed_form / confirmed_scaled / contradicted / uncertain
- Confidence: [High/Medium/Low]
- Manifestation form: [confirmed_form only: the specific form actually manifested for the querent]
- Baseline adjustment: [confirmed_scaled only: amplified/standard/diminished + explanation]

## Unverified Entries

### P[N]: [theme label]
- Time period: age X-Y (YYYY-YYYY)
- Source natal indicator: [ID](name) x [period name]
- Prediction option: [content]
- Verification status: tier2_skipped
- Handling: Use innate strength, direction not locked
```

## Appendix C: Confidence Criteria

| Confidence | Conditions |
|-----------|------------|
| **High** | confirmed or confirmed_form; or same natal indicator confirmed across multiple periods |
| **Medium** | confirmed_scaled (direction correct but magnitude adjusted); or single-period single-system confirmed |
| **Low** | uncertain; or confirmed with innate strength Weak; or data from post-time-correction |

## Appendix D: Old Format Migration

Calibration files containing any of the following old fields -> old format:
- `Confirmed direction` / `Calibrated interpretation` / `Impact on querent` (v2 format)
- `Original possible directions` / `Querent's selection` (v3 format)
- `Calibration result: revised` (v4 format, maps to `confirmed_form`)

Handling: Prompt the querent to perform incremental verification or full re-verification. Back up old files as `*_calibration_v5_backup.md`.

Old status mapping:
- Old `confirmed` -> new `confirmed`
- Old `revised` -> new `confirmed_form` (needs manifestation_form supplement)
- Old `contradicted` -> new `contradicted`
- Old `uncertain` -> new `uncertain`

> **Backward compatibility note**: Old user data files may use `## Calibrated Entries`, `Source symbol`, `Interaction summary`, `Theoretical energy` as section headings or field names. When encountered, treat these as equivalent to the new terms `## Verified Entries`, `Source natal indicator`, `Activation summary`, `Innate strength` — no need to require the querent to re-verify.
