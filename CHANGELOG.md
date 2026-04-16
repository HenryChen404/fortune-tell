# Changelog

## 2.3.0

- 命盘宠物卡 ASCII Art 全面细化：侧视图 + 特征比例夸张 + 内部结构线
  - 5 张卡改为侧视图（狐、凤凰、鹿、玄龟·天梁、虎）
  - 1 张保持正面（猫头鹰，眼部辨识度需要）
  - 8 张侧视微调，增加内部线条（龙鳞、虎纹、龟壳纹、羽纹等）
  - 天府龟 vs 天梁龟通过壳大小 + 内部纹路双重区分
- 稀有度视觉效果增强
  - 色阶重新设计：R 灰色 → SR 绿色 → SSR 洋红 → SSSR 金黄，梯度更清晰
  - ATK/DEF 改为 `█░` stat bar 可视化（bar 长 20 格，按比例填充）
  - preview 卡显示全空 stat bar + `????`
- Natal Pet card ASCII art overhaul: side view + exaggerated features + internal detail lines
  - 5 cards changed to side view (Fox, Phoenix, Deer, Ancient Tortoise, Tiger)
  - 1 card kept front view (Owl, eye recognition requires it)
  - 8 side-view cards refined with internal lines (dragon scales, tiger stripes, shell texture, feather marks, etc.)
  - Jade Tortoise vs Ancient Tortoise differentiated by shell size + internal pattern
- Rarity visual effects enhancement
  - Color scheme redesigned: R gray → SR green → SSR magenta → SSSR gold, clearer gradient
  - ATK/DEF replaced with `█░` stat bar visualization (20-segment bar, proportional fill)
  - Preview card shows empty stat bars + `????`

## 2.2.0

- 新增命盘宠物系统：排盘后自动分配一张游戏王风格的 ASCII Art 卡牌
  - 14 张卡牌对应紫微斗数 14 主星，每颗星化身一只独特神兽
  - 稀有度由跨体系共振决定（R/SR/SSR/SSSR）
  - ATK/DEF 根据四套命盘数据动态计算
  - 两步进化式 UX：排盘后展示 R 级预览卡，校准后触发进化揭示
  - 支持 ANSI 终端色彩渲染，不同稀有度有不同视觉效果
  - 非 TTY 环境自动禁用色彩，支持 `--no-color` 开关
- Natal Pet system: a Yu-Gi-Oh! style ASCII Art card assigned after chart generation
  - 14 cards based on Zi Wei Dou Shu main stars, each a unique mythical creature
  - Rarity determined by cross-system resonance (R/SR/SSR/SSSR)
  - ATK/DEF dynamically calculated from all four chart systems
  - Two-step evolution UX: R-level preview after charting, evolution reveal after calibration
  - ANSI terminal color rendering with per-rarity visual effects
  - Auto-disables color in non-TTY environments, supports `--no-color` flag
- 校准问题精度提升：从"按时间段的生活普查"改为"按意象组的方向鉴别"
  - 新增意象组构建规则：同源分组（4 条规则）+ 内部结构化输出格式
  - 核心规则重写：一问一组、选项即方向、时间段为锚点非组织原则、主题必须具体
  - 新增格式要求"主题聚焦"，修改选项要求为"同一件事的不同表现方式"
  - 新增 4 条反面典型（生活普查式、一问多主题、时间段代替主题、跨主题方向不可区分）
  - 示例问题全部替换为意象导向的新示例
- Calibration question precision overhaul: from "life survey by time period" to "direction discrimination by symbol group"
  - New Symbol Group construction rules: homologous grouping (4 rules) + internal structured output format
  - Core rules rewritten: one question per group, options = directions, time as anchor not organizer, theme must be specific
  - New format requirement "theme focus"; option requirement changed to "different manifestations of the same thing"
  - 4 new anti-patterns (life survey, one-question-many-themes, time-as-subject, cross-theme indistinguishable)
  - Example questions fully replaced with symbol-centric new examples

## 2.1.1

- 更新后自动加载新版本：`git pull` 成功后通过 Read 工具从磁盘重新读取 SKILL.md，当前会话无需重启即可使用新版指令
- Auto-reload after update: after `git pull`, use Read tool to load the freshly updated SKILL.md from disk so the current session uses the new instructions without restart

## 2.0.0

- 新增校准系统：排盘后、首次解读前进行意象校准
  - 动态生成校准问题，绑定大运/流年/Dasha 时间段
  - 支持跨体系校准（一个问题同时校准多个体系的同源意象）
  - 校准结果分4个体系文件独立存储（bazi/ziwei/western/vedic_calibration.md）
  - 支持"不确定"和"都不符合"回答，后者触发追问探索新方向
  - 每题允许命主自由文字补充
- 新增增量校准：命主反馈不准时可追加校准，支持冲突处理和完全重新校准
- 解读工作流集成校准数据：已校准意象按确认方向解读，未校准用默认权重

## 1.1.0

- 添加自动更新检查：每次 skill 唤起时检查 git 远程是否有新版本

## 1.0.0

- 四体系命理解读（八字、紫微、西洋占星、吠陀占星）
- 中英文双版本（cn/ 和 en/）
- ensemble voting 机制：多数一致才输出
- 古今映射：古代概念自动翻译为现代语境
