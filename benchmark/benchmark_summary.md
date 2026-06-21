# Fortune-Tell Skill Benchmark 汇总报告

**Date**: 2026-06-20
**Author**: QA-man
**Version**: 1.0

---

## 概览

| 维度 | 通过率 | 评分 | 状态 |
|------|--------|------|------|
| **A. 计算正确性** | 98.5% | 128+2P/130 | ✅ PASS |
| **B. 运行轨迹** | 100% | 72/72 | ✅ PASS |
| **C. 解读质量** | 98.3% | 59/60 | ✅ PASS |

**综合评定: PASS**

---

## Phase 1: 计算正确性 (维度 A)

- **方法**: 5个标准测试人物 × 4体系 × 多项验证 = 130个验证点
- **Ground Truth**: BeyondBazi, astro.com, Jagannatha Hora, 紫微斗数排盘网
- **结果**: 128+2P/130 (98.5%)
  - BaZi: 40/40 (100%)
  - ZiWei: 28+2P/30 (93.3%) — 2个P1标签问题(命宫主星/身宫主星 header)
  - Western: 30/30 (100%)
  - Vedic: 30/30 (100%)
- **已修复 Bug**:
  - P0-B1: Vedic DST (vedic_chart.py --tz 改为 IANA 字符串)
  - P0-B2: BaZi/ZiWei 120°E 硬编码 (改为动态基准经线)
- **详细报告**: benchmark_computation.md + benchmark_retest.md

## Phase 2: 运行轨迹 (维度 B)

- **方法**: 3个模拟场景 × 步骤级 trace 评估 + 实际脚本执行验证
- **范围**: SKILL.md + calibration_guide.md + reading_guide.md + natal_pet_guide.md
- **结果**: 72/72 (100%)
  - S1 新用户全流程: 55/55 (Phase 0-3 + 参数一致性)
  - S2 验盘校正: 8/8
  - S3 回访用户: 9/9
- **实际执行验证**: 4个排盘脚本 + natal_pet_card.py (2种模式) 全部通过
- **CN/EN 脚本同步**: diff 确认 4 个脚本完全一致
- **发现**: 4个 P3 信息性问题 (无功能影响)
- **详细报告**: benchmark_trace.md

## Phase 3: 解读质量 (维度 C)

- **方法**: 规范审计 — 评估 reading_guide.md 的完整性、一致性、质量保障能力
- **范围**: 6项质量量表 + 三大法则 + 验盘数据利用 + 数据流 + 核查清单
- **结果**: 59/60 (98.3%)
  - 质量量表规范覆盖: 12/12
  - 三大法则实现: 14/15 (第三法则缺映射示例)
  - 验盘数据利用: 7/7
  - 数据流完整性: 8/8
  - 核查清单覆盖: 18/18
- **发现**: 3个 P3 建议 (缺术语映射示例/拒绝措辞模板/清单条目补充)
- **Phase 3b (真人专家对比)**: 待条件具备后执行
- **详细报告**: benchmark_reading_quality.md

---

## 遗留问题

| # | 优先级 | 描述 | 状态 |
|---|--------|------|------|
| L1 | P1 | ZiWei 命宫主星/身宫主星 header 标签显示命主/身主而非实际主星 | 待修复 |
| F1 | P2 | bazi_chart.py shebang python3.11 vs 系统 python3 | 已知, 规范正确 |
| F2 | P3 | DST 检测仅覆盖中国1986-1991 | 信息性 |
| F3 | P3 | calibration_plan.md 写入无错误恢复 | 极低风险 |
| F4 | P3 | natal_pet 进化展示编号引用不统一 | 无影响 |
| F5 | P3 | reading_guide 缺术语→现代语言映射示例 | 建议 |
| F6 | P3 | 单体系拒绝缺措辞模板 | 建议 |
| F7 | P3 | 核查清单缺5项显式条目 | 建议 |

---

## 输出物索引

| 文件 | 内容 |
|------|------|
| `benchmark_plan.md` | v1.1 评估计划 |
| `benchmark_computation.md` | Phase 1 计算正确性报告 (130点) |
| `benchmark_retest.md` | Phase 1 B1+B2 修复验证 |
| `benchmark_trace.md` | Phase 2 运行轨迹报告 (72点) |
| `benchmark_reading_quality.md` | Phase 3 解读质量报告 (60点) |
| `benchmark_summary.md` | 本汇总报告 |
| `benchmark_phase2/` | S1 场景脚本输出 (4个md) |

---

## 结论

Fortune-tell skill v4.0.0 通过三维度 benchmark 评估：

1. **计算引擎可靠**: DST 和经度基准修复后，四体系排盘精度达到行业标准 (Western/Vedic 行星经度 ±0.03°)
2. **执行规范完整**: SKILL.md + 三个指南文件构成无遗漏、无歧义、可执行的指令集
3. **解读质量规范充分**: 双层修正机制 + 5种验盘状态处理 + 三大法则 + 自检清单，为 LLM 提供了产出高质量解读的充分规范支撑

唯一待修复项为 P1 级 ZiWei 标签问题 (L1)，不影响计算正确性。
