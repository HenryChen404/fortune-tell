#!/usr/bin/env python3.11
"""八字五行排盘脚本 — 基于 lunar_python"""

import argparse
import math
import sys
from datetime import datetime
from lunar_python import Solar


def true_solar_time(year, month, day, hour, minute, lng):
    """将钟表时间（北京时间等标准时区时间）转换为真太阳时。

    真太阳时 = 钟表时间 + 经度时差修正 + 均时差修正
    - 经度时差: 4分钟 × (出生地经度 - 标准经度120°)
    - 均时差(Equation of Time): 由一年中的日序数计算
    """
    # 经度时差修正（中国标准时间基准经度为120°E）
    lng_correction = 4.0 * (lng - 120.0)  # 分钟

    # 均时差修正
    dt = datetime(year, month, day)
    day_of_year = dt.timetuple().tm_yday
    b = 2 * math.pi * (day_of_year - 81) / 365.0
    eot = 9.87 * math.sin(2 * b) - 7.53 * math.cos(b) - 1.5 * math.sin(b)  # 分钟

    # 总修正量（分钟）
    total_correction = lng_correction + eot

    # 换算
    total_minutes = hour * 60 + minute + total_correction
    # 处理跨日
    if total_minutes < 0:
        total_minutes += 1440
        # 需要回退一天
        from datetime import timedelta
        dt2 = datetime(year, month, day) - timedelta(days=1)
        return dt2.year, dt2.month, dt2.day, int(total_minutes // 60), int(total_minutes % 60)
    elif total_minutes >= 1440:
        total_minutes -= 1440
        from datetime import timedelta
        dt2 = datetime(year, month, day) + timedelta(days=1)
        return dt2.year, dt2.month, dt2.day, int(total_minutes // 60), int(total_minutes % 60)

    return year, month, day, int(total_minutes // 60), int(total_minutes % 60)


WUXING_MAP = {
    '甲': '木', '乙': '木', '丙': '火', '丁': '火', '戊': '土',
    '己': '土', '庚': '金', '辛': '金', '壬': '水', '癸': '水',
    '子': '水', '丑': '土', '寅': '木', '卯': '木', '辰': '土',
    '巳': '火', '午': '火', '未': '土', '申': '金', '酉': '金',
    '戌': '土', '亥': '水',
}


def count_wuxing(ba):
    """统计八字中五行个数"""
    counts = {'金': 0, '木': 0, '水': 0, '火': 0, '土': 0}
    # 天干
    for gan in [ba.getYear()[0], ba.getMonth()[0], ba.getDay()[0], ba.getTime()[0]]:
        counts[WUXING_MAP.get(gan, '')] += 1
    # 地支
    for zhi in [ba.getYear()[1], ba.getMonth()[1], ba.getDay()[1], ba.getTime()[1]]:
        counts[WUXING_MAP.get(zhi, '')] += 1
    return counts


def get_hidden_gan_str(hide_gan_list):
    """格式化藏干列表"""
    return '、'.join(f'{g}({WUXING_MAP.get(g, "")})' for g in hide_gan_list)


def generate_bazi_md(year, month, day, hour, minute, gender, lng=120.0):
    # 真太阳时校正
    t_year, t_month, t_day, t_hour, t_minute = true_solar_time(
        year, month, day, hour, minute, lng
    )
    solar = Solar(t_year, t_month, t_day, t_hour, t_minute, 0)
    lunar = solar.getLunar()
    ba = lunar.getEightChar()
    is_male = gender.lower() in ('male', '男', 'm')
    yun = ba.getYun(1 if is_male else 0)

    day_gan = ba.getDay()[0]
    day_gan_wuxing = WUXING_MAP.get(day_gan, '')

    lines = []
    lines.append('# 八字五行命盘')
    lines.append('')
    lines.append('## 基本信息')
    lines.append('')
    lines.append(f'- 性别: {"男" if is_male else "女"}')
    lines.append(f'- 钟表时间: {year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}')
    lines.append(f'- 真太阳时: {t_year}-{t_month:02d}-{t_day:02d} {t_hour:02d}:{t_minute:02d}')
    lines.append(f'- 出生经度: {lng}°E')
    lines.append(f'- 日主: {day_gan}（{day_gan_wuxing}）')
    lines.append(f'- 命宫: {ba.getDay()}日')
    lines.append('')

    # 四柱表
    lines.append('## 四柱')
    lines.append('')
    lines.append('| 柱 | 天干 | 地支 | 藏干 | 纳音 |')
    lines.append('|----|------|------|------|------|')

    pillar_names = ['年柱', '月柱', '日柱', '时柱']
    ganzhi = [ba.getYear(), ba.getMonth(), ba.getDay(), ba.getTime()]
    nayin = [ba.getYearNaYin(), ba.getMonthNaYin(), ba.getDayNaYin(), ba.getTimeNaYin()]
    hide_gans = [ba.getYearHideGan(), ba.getMonthHideGan(), ba.getDayHideGan(), ba.getTimeHideGan()]

    for i in range(4):
        gz = ganzhi[i]
        gan, zhi = gz[0], gz[1]
        hg = get_hidden_gan_str(hide_gans[i])
        lines.append(f'| {pillar_names[i]} | {gan}({WUXING_MAP.get(gan, "")}) | {zhi}({WUXING_MAP.get(zhi, "")}) | {hg} | {nayin[i]} |')

    lines.append('')

    # 十神
    lines.append('## 十神')
    lines.append('')
    lines.append('| 位置 | 天干 | 十神 |')
    lines.append('|------|------|------|')
    lines.append(f'| 年干 | {ba.getYear()[0]} | {ba.getYearShiShenGan()} |')
    lines.append(f'| 月干 | {ba.getMonth()[0]} | {ba.getMonthShiShenGan()} |')
    lines.append(f'| 日干 | {ba.getDay()[0]} | 日主 |')
    lines.append(f'| 时干 | {ba.getTime()[0]} | {ba.getTimeShiShenGan()} |')
    lines.append('')

    # 地支十神（含所有藏干）
    lines.append('| 位置 | 地支 | 十神（藏干） |')
    lines.append('|------|------|------------|')
    zhi_shishen = [
        ('年支', ba.getYear()[1], ba.getYearShiShenZhi()),
        ('月支', ba.getMonth()[1], ba.getMonthShiShenZhi()),
        ('日支', ba.getDay()[1], ba.getDayShiShenZhi()),
        ('时支', ba.getTime()[1], ba.getTimeShiShenZhi()),
    ]
    for label, zhi, ss_list in zhi_shishen:
        ss_str = '、'.join(ss_list) if ss_list else ''
        lines.append(f'| {label} | {zhi} | {ss_str} |')
    lines.append('')

    # 五行统计
    wuxing = count_wuxing(ba)
    lines.append('## 五行统计')
    lines.append('')
    lines.append('| 五行 | 金 | 木 | 水 | 火 | 土 |')
    lines.append('|------|----|----|----|----|-----|')
    lines.append(f'| 数量 | {wuxing["金"]} | {wuxing["木"]} | {wuxing["水"]} | {wuxing["火"]} | {wuxing["土"]} |')
    lines.append('')

    # 大运
    lines.append('## 大运')
    lines.append('')
    lines.append(f'- 起运: {yun.getStartYear()}年{yun.getStartMonth()}月{yun.getStartDay()}日')
    lines.append('')
    lines.append('| 起始年龄 | 大运 | 起始年份 |')
    lines.append('|----------|------|----------|')

    dayuns = yun.getDaYun()
    for d in dayuns:
        gz = d.getGanZhi()
        if gz:
            lines.append(f'| {d.getStartAge()}岁 | {gz} | {d.getStartYear()}年 |')

    lines.append('')

    # 流年（当前大运的流年）
    lines.append('## 当前大运流年')
    lines.append('')
    for d in dayuns:
        if d.getStartAge() > 0 and d.getGanZhi():
            liu_nians = d.getLiuNian()
            if liu_nians:
                lines.append(f'### {d.getGanZhi()}运（{d.getStartAge()}岁起）')
                lines.append('')
                lines.append('| 年份 | 流年 | 年龄 |')
                lines.append('|------|------|------|')
                for ln in liu_nians:
                    lines.append(f'| {ln.getYear()}年 | {ln.getGanZhi()} | {ln.getAge()}岁 |')
                lines.append('')

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='八字五行排盘')
    parser.add_argument('--year', type=int, required=True)
    parser.add_argument('--month', type=int, required=True)
    parser.add_argument('--day', type=int, required=True)
    parser.add_argument('--hour', type=int, required=True)
    parser.add_argument('--minute', type=int, default=0)
    parser.add_argument('--lng', type=float, default=120.0, help='出生地经度，用于真太阳时校正（默认120°E）')
    parser.add_argument('--gender', type=str, required=True, help='male/female/男/女')
    args = parser.parse_args()

    result = generate_bazi_md(args.year, args.month, args.day, args.hour, args.minute, args.gender, args.lng)
    print(result)


if __name__ == '__main__':
    main()
