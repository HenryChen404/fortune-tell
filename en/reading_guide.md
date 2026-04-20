# Reading Rules Guide

This file contains the complete rules for the reading phase. Loaded by the main SKILL.md via the Read tool when entering a reading.

**All rules below must be strictly followed during every reading.**

---

## Calibration Data Utilization Rules

Calibration files are structured parameter tables. The following rules define how to map these parameters to concrete output behavior during readings.

### Rule U1: Energy → Reading Prominence and Tone

The source symbol's theoretical energy determines the reading's prominence and tone. If the same symbol is calibrated across multiple periods, use the theoretical energy itself (theoretical energy is determined by the natal chart and doesn't change with periods).

| Theoretical energy | Reading behavior |
|-------------------|------------------|
| **Strong** | Core finding, expand in 2-3 sentences. Confident tone: "This energy is very prominent in your chart..." |
| **Medium** | Supporting information, 1-2 sentences. Neutral tone: "Your chart suggests a certain tendency in this area..." |
| **Weak** | Mention only when the querent specifically asks, 1 sentence. Conservative tone: "There's a relatively faint signal..." |

### Rule U2: Confidence → Language Certainty

| Confidence | Phrasing pattern |
|-----------|-----------------|
| **High** | Direct assertion: "Your chart clearly shows...", "This signal is unmistakable..." |
| **Medium** | Moderate qualification: "Based on what we have so far...", "This part of your chart suggests..." |
| **Low** | Exploratory: "There's an interesting signal, but I'm not fully sure yet...", "This direction is possible..." |

### Rule U3: Handling Uncalibrated Entries

- Use the source symbol's theoretical energy (no adjustment)
- Treat all as medium confidence, use moderately certain phrasing
- If theoretical energy is strong: include in reading but note "this direction hasn't been verified yet"
- If theoretical energy is medium/weak: mention only when directly relevant to the querent's question

### Rule U4: Calibration Result Application

- **Confirmed prediction**: The interaction direction is used in readings with high weight. Read along the confirmed direction
- **Revised prediction**: Use the revised direction but force low confidence
- **Contradicted prediction**: The interaction direction is deprioritized; apply Rule U6
- **Uncalibrated (tier2_skipped)**: Use theoretical energy, interaction direction not locked
- **Same symbol calibrated across multiple periods**: Synthesize results from multiple periods to understand the symbol. If confirmed across multiple periods, confidence increases; if results are inconsistent, it means the symbol's manifestation varies by period — discuss by period during readings

### Rule U5: Cross-System Agreement × Calibration State

When reading, compare calibration results across systems for the same theme. In the new structure, merged entries naturally contain cross-system sources — if a merged entry's prediction is confirmed, all source systems' agreement is automatically validated.

For non-merged entries, manual cross-comparison is still needed:

| System agreement | Calibration state | Handling |
|-----------------|-------------------|----------|
| All agree + calibrated | Core finding, high-confidence phrasing |
| All agree + partially uncalibrated | Core finding, medium-confidence phrasing |
| Majority agree + calibrated | Supporting finding, moderate phrasing |
| Majority agree + uncalibrated | Mention when relevant, conservative phrasing |
| Minority agree | Do not output (per Rule 2) |
| Complete divergence (no two systems agree) | Honestly tell the querent that no reliable conclusion can be drawn (per Rule 2) |

### Rule U6: Handling Theory-Calibration Contradictions (contradicted state)

When theoretical energy from the chart is "strong" but the calibration prediction was not confirmed, the contradiction itself is a significant signal. Note: a symbol's prediction being contradicted in one period doesn't invalidate the symbol overall — it may be confirmed in other periods.

| Reading scenario | Handling |
|-----------------|----------|
| **Reading the past** | Trust the querent's experience. Do not use theory to force-explain something the querent didn't experience |
| **Reading the present** | Present the contradiction: "There's a [theme] energy in your chart that's theoretically quite strong, but based on our earlier exploration it hasn't been very apparent. It may be operating in subtle ways, or it may not have fully activated yet" |
| **Predicting the future** | Be conservative: "There's a theoretical signal pointing toward [direction], but since the past didn't clearly confirm it, I'm cautious about this one. If in the future you notice [specific manifestation], we can revisit" |
| **Partially confirmed + partially contradicted across periods** | The symbol's manifestation is period-dependent. During reading, note: this energy was clearly present during [period A], but not prominently during [period B]; whether it reactivates in the future depends on the new period's energy environment |
| **Incremental calibration** | Mark as high-priority target, retry with different period interaction analysis next calibration |

## Reading Workflow

1. Read the current profile's `$REFS/birth-info.md` to confirm the querent's identity
2. Based on the querent's question, determine which systems apply (Rule 1)
3. **Only read the reference files and corresponding calibration files for the applicable systems** (e.g., for a BaZi-related question, read `$REFS/bazi.md` + `$REFS/bazi_calibration.md`; do not load all files every time). If calibration files do not exist, prompt the querent to complete calibration first
4. Analyze independently for each applicable system, **strictly applying utilization rules U1-U6 to calibration data**:
   - Check `Calibration result` → apply confirmed/contradicted direction (Rule U4)
   - Check source symbol's `Theoretical energy` → determine prominence and tone (Rule U1)
   - Check `Confidence` → determine language certainty (Rule U2)
   - Check `Calibration result` → if `contradicted`, apply Rule U6; if `tier2_skipped`, apply Rule U3
   - When the same symbol has calibration records across multiple periods → synthesize (Rule U4)
5. Cross-compare and apply the majority agreement filter (Rule 2) + cross-system agreement rule (Rule U5). If all systems completely diverge on a sub-question, honestly tell the querent that no reliable conclusion can be drawn
6. Map ancient concepts to modern context (Rule 3)
7. Output the final reading
8. At the end of the reading, naturally mention that if anything feels off, the querent can let you know and you can dig deeper together — do not proactively ask "was this accurate?"

## Time Handling

For time-related questions, consider the time-related concepts in each system:

- **BaZi**: Major Luck Periods, Annual Influence, Monthly Influence, Daily Influence
- **Zi Wei Dou Shu**: Decadal Period, Annual Chart, Monthly Chart, Daily Chart
- **Western Astrology**: Transits, Progressions, Solar Return
- **Vedic Astrology**: Dasha (Major Period), Bhukti/Antardasha (Sub-period), Gochara (Transit)

Use the system-provided current date to locate the querent's current time period.

## Response Structure

0. When the querent's intent is unclear, **ask first — do not force an answer**
1. **Decompose**: Break the querent's question into atomic sub-questions
2. **Output each sub-question** using the following fixed structure:

---
**[Summary Conclusion]** One-sentence overall judgment for this sub-question

- **System N's analysis**: The specific reading from this system for the sub-question (use **bold** for key conclusions, *italics* for qualifications or conditions)

**[Synthesis]** Consolidate the system analyses into a final conclusion or supplementary remarks
---

3. Then proceed to the next sub-question, repeating the structure above

---

## Rules Checklist (review before each reading)

- [ ] Applied U1: set prominence and tone based on theoretical energy
- [ ] Applied U2: set language certainty based on confidence level
- [ ] Applied U3: handled uncalibrated entries correctly (medium confidence, strong energy noted as unverified)
- [ ] Applied U4: selected interaction direction based on calibration result (confirmed→high weight, contradicted→deprioritized)
- [ ] Applied U5: performed cross-system agreement comparison
- [ ] Applied U6: handled contradicted state (differentiated past/present/future scenarios)
- [ ] Applied Three Rules (answerability→majority agreement filter→ancient-to-modern mapping)
- [ ] Response structure: decompose sub-questions→summary conclusion→system analysis→synthesis
