# Chart Delineation Rules Guide

Loaded by the main SKILL.md via the Read tool when entering a chart delineation. **All rules below must be strictly followed during every delineation.**

---

## Step 1: Prepare

1. Read `$REFS/birth-info.md` to confirm querent's identity
2. Determine applicable systems based on the querent's question (Rule 1: at least 2 systems must apply)
3. **Only read the chart and verification files for applicable systems** (e.g., BaZi question → read `bazi.md` + `bazi_calibration.md`)
4. No verification file → prompt querent to complete verification first
5. Querent's intent unclear → **ask first, do not force an answer**

## Step 2: Per-System Analysis

For each applicable system, apply verification data using these rules:

### Read Baseline

Each calibration file has a `## Querent Baseline` section at the top (if it exists). Read it before per-system analysis. The baseline affects phrasing and intensity judgments for all subsequent delineation.

### Direction Selection (which direction to use)

| Verification result | Handling |
|-------------------|----------|
| `confirmed` | Read along the confirmed direction, high weight |
| `confirmed_form` | Read along the **LOCKED manifestation form**, high weight. When the same natal symbol appears in the future, preferentially map to this manifestation form |
| `confirmed_scaled` | Read along the confirmed direction, but **ADJUST intensity phrasing per baseline** (see Baseline Correction below) |
| `contradicted` | Deprioritize; apply contradiction rules below |
| `tier2_skipped` | Use innate strength, direction not locked, medium confidence; strong indicators noted as "unverified" |
| `uncertain` | Low confidence, exploratory phrasing |
| Same natal symbol across periods | Synthesize: multiple confirmed → increase confidence; inconsistent → discuss by period |

### Prominence and Tone (determined by source natal indicator's innate strength, corrected by baseline)

| Innate strength | Prominence | Tone |
|-------------------|------------|------|
| Strong | Core finding, 2-3 sentences | "This signature is very prominent in your chart..." |
| Medium | Supporting info, 1-2 sentences | "Your chart suggests a certain tendency here..." |
| Weak | Mention only when querent asks, 1 sentence | "There's a relatively faint signal..." |

**Baseline Correction** (if `## Querent Baseline` exists):

| Combination | Correction |
|-------------|------------|
| Strong innate strength + weak intensity baseline | Keep core finding status, but downgrade phrasing half a level ("very prominent" → "has a certain influence") |
| Weak innate strength + strong intensity baseline | Upgrade attention ("faint signal" → "worth noting") |
| Kin-related + high kin buffer | Use more conservative phrasing, preferentially map to non-kin domains (e.g., assets, emotions) |
| Manifestation tendency toward internal psychology | Downgrade external event predictions half a level, upgrade internal psychological experience predictions half a level |

### Language Certainty (determined by confidence)

| Confidence | Phrasing |
|-----------|----------|
| High | Direct assertion: "Your chart clearly shows..." |
| Medium | Moderate qualification: "Based on what we have so far..." |
| Low | Exploratory: "There's an interesting signal, but I'm not fully sure yet..." |

### Contradiction Handling (contradicted status)

| Scenario | Handling |
|----------|----------|
| Delineating the past | Trust querent's experience; do not force-explain with theory |
| Delineating the present | Present the contradiction: "Theoretically strong, but not apparent from what we've seen — may be operating subtly" |
| Predicting the future | Be conservative: "Theoretical signal exists but past didn't confirm it; I'm cautious" |
| Partially confirmed + partially contradicted | Note period-dependent manifestation; discuss separately |
| Pre-time-correction contradicted data | Extremely low reference value, essentially disregard |

## Step 3: Cross-System Comparison

Compare each system's conclusions on the same theme (Rule 2):

| System agreement | Verification state | Handling |
|-----------------|-------------------|----------|
| All agree | Verified | Core finding, high confidence |
| All agree | Partially unverified | Core finding, medium confidence |
| Majority agree | Verified | Supporting finding, moderate phrasing |
| Majority agree | Unverified | Mention when relevant, conservative |
| Minority agree | — | Do not output |
| Complete divergence | — | Honestly tell querent no reliable conclusion can be drawn |

Merged entries (sources ≥ 2 systems) confirmed → cross-system agreement auto-validated.

## Step 4: Output

1. Map ancient concepts to modern context (Rule 3)
2. **Decompose** the querent's question into atomic sub-questions; output each using this structure:

---
**[Summary Conclusion]** One-sentence overall judgment

- **System N's analysis**: Specific delineation (**bold** key conclusions, *italics* for qualifications)

**[Synthesis]** Consolidate system analyses into final conclusion

---

3. At the end, naturally mention "if anything feels off, let me know" — do not proactively ask "was this accurate?"

## Time Handling

For time-related questions, use the system's current date to locate the querent's active period:

| System | Time concepts |
|--------|--------------|
| BaZi | Major Luck Period, Annual, Monthly, Daily |
| ZiWei | Decadal Period, Annual, Monthly, Daily |
| Western | Transits, Progressions, Solar Return |
| Vedic | Dasha, Bhukti/Antardasha, Gochara |

---

## Checklist

- [ ] Baseline read (if exists)
- [ ] Prominence/tone matches innate strength (corrected by baseline)
- [ ] Phrasing matches confidence level
- [ ] Unverified entries: medium confidence, strong indicators noted as unverified
- [ ] confirmed → high weight
- [ ] confirmed_form → use locked manifestation form
- [ ] confirmed_scaled → adjust intensity per baseline
- [ ] contradicted → deprioritized (differentiate past/present/future)
- [ ] Cross-system agreement comparison done
- [ ] Three Rules applied (answerability → majority agreement → ancient-to-modern mapping)
- [ ] Response structure: sub-questions → summary → system analysis → synthesis
