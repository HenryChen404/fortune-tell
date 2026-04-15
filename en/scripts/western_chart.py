#!/usr/bin/env python3.11
"""西洋占星排盘脚本 — 基于 kerykeion"""

import argparse
import sys
from kerykeion import AstrologicalSubjectFactory
from kerykeion.chart_data_factory import ChartDataFactory


SIGN_CN = {
    'Ari': '白羊座', 'Tau': '金牛座', 'Gem': '双子座', 'Can': '巨蟹座',
    'Leo': '狮子座', 'Vir': '处女座', 'Lib': '天秤座', 'Sco': '天蝎座',
    'Sag': '射手座', 'Cap': '摩羯座', 'Aqu': '水瓶座', 'Pis': '双鱼座',
}

PLANET_CN = {
    'Sun': '太阳', 'Moon': '月亮', 'Mercury': '水星', 'Venus': '金星',
    'Mars': '火星', 'Jupiter': '木星', 'Saturn': '土星',
    'Uranus': '天王星', 'Neptune': '海王星', 'Pluto': '冥王星',
    'Chiron': '凯龙星',
    'Mean_North_Lunar_Node': '北交点', 'True_North_Lunar_Node': '真北交点',
    'Mean_Lilith': '莉莉丝',
}

ASPECT_CN = {
    'conjunction': '合相 (0°)',
    'opposition': '对分相 (180°)',
    'trine': '三分相 (120°)',
    'square': '四分相 (90°)',
    'sextile': '六分相 (60°)',
    'quintile': '五分相 (72°)',
    'semi-sextile': '半六合 (30°)',
    'quincunx': '梅花相 (150°)',
    'semi-square': '半刑 (45°)',
    'sesquiquadrate': '补半刑 (135°)',
}

HOUSE_CN = {
    'First_House': '第1宫', 'Second_House': '第2宫', 'Third_House': '第3宫',
    'Fourth_House': '第4宫', 'Fifth_House': '第5宫', 'Sixth_House': '第6宫',
    'Seventh_House': '第7宫', 'Eighth_House': '第8宫', 'Ninth_House': '第9宫',
    'Tenth_House': '第10宫', 'Eleventh_House': '第11宫', 'Twelfth_House': '第12宫',
}

ELEMENT_CN = {'Fire': '火', 'Earth': '土', 'Air': '风', 'Water': '水'}
QUALITY_CN = {'Cardinal': '基本', 'Fixed': '固定', 'Mutable': '变动'}

HOUSE_SYSTEMS = {
    'P': 'Placidus',
    'K': 'Koch',
    'O': 'Porphyrius',
    'R': 'Regiomontanus',
    'C': 'Campanus',
    'A': 'Equal (Asc)',
    'W': 'Whole Sign',
    'B': 'Alcabitius',
}


def sign_cn(sign_abbr):
    return SIGN_CN.get(sign_abbr, sign_abbr)


def format_position(pos):
    deg = int(pos)
    minutes = int((pos - deg) * 60)
    return f"{deg}°{minutes:02d}'"


def generate_western_md(year, month, day, hour, minute, lat, lng, tz_str, house_system='P'):
    subject = AstrologicalSubjectFactory.from_birth_data(
        'Subject', year, month, day, hour, minute,
        lng=lng, lat=lat, tz_str=tz_str, online=False,
        houses_system_identifier=house_system,
    )
    chart = ChartDataFactory.create_natal_chart_data(subject)

    lines = []
    lines.append('# 西洋占星星盘')
    lines.append('')
    lines.append('## 基本信息')
    lines.append('')
    lines.append(f'- 太阳星座: {sign_cn(subject.sun.sign)} {format_position(subject.sun.position)}')
    lines.append(f'- 月亮星座: {sign_cn(subject.moon.sign)} {format_position(subject.moon.position)}')
    lines.append(f'- 上升星座: {sign_cn(subject.ascendant.sign)} {format_position(subject.ascendant.position)}')
    lines.append(f'- 天顶(MC): {sign_cn(subject.medium_coeli.sign)} {format_position(subject.medium_coeli.position)}')
    lines.append(f'- 宫位制: {HOUSE_SYSTEMS.get(house_system, house_system)}')
    if hasattr(chart, 'lunar_phase') and chart.lunar_phase:
        lp = chart.lunar_phase
        lines.append(f'- 月相: {lp.phase_name} ({lp.illumination:.1f}%)')
    lines.append('')

    # 行星位置
    lines.append('## 行星位置')
    lines.append('')
    lines.append('| 行星 | 星座 | 度数 | 宫位 | 逆行 |')
    lines.append('|------|------|------|------|------|')

    planets = [
        subject.sun, subject.moon, subject.mercury, subject.venus, subject.mars,
        subject.jupiter, subject.saturn, subject.uranus, subject.neptune, subject.pluto,
    ]
    for attr in ('chiron', 'mean_north_lunar_node', 'mean_lilith'):
        val = getattr(subject, attr, None)
        if val is not None:
            planets.append(val)
    planets = [p for p in planets if p is not None]

    for p in planets:
        name_cn = PLANET_CN.get(p.name, p.name)
        retro = '℞' if p.retrograde else ''
        house = HOUSE_CN.get(p.house, p.house)
        lines.append(f'| {name_cn} | {sign_cn(p.sign)} | {format_position(p.position)} | {house} | {retro} |')

    lines.append('')

    # 宫头
    lines.append('## 宫头位置')
    lines.append('')
    lines.append('| 宫位 | 星座 | 度数 |')
    lines.append('|------|------|------|')

    houses = [
        subject.first_house, subject.second_house, subject.third_house,
        subject.fourth_house, subject.fifth_house, subject.sixth_house,
        subject.seventh_house, subject.eighth_house, subject.ninth_house,
        subject.tenth_house, subject.eleventh_house, subject.twelfth_house,
    ]
    for i, h in enumerate(houses, 1):
        lines.append(f'| 第{i}宫 | {sign_cn(h.sign)} | {format_position(h.position)} |')

    lines.append('')

    # 相位
    lines.append('## 主要相位')
    lines.append('')
    lines.append('| 行星1 | 相位 | 行星2 | 容许度 |')
    lines.append('|-------|------|-------|--------|')

    for a in chart.aspects:
        p1 = PLANET_CN.get(a.p1_name, a.p1_name)
        p2 = PLANET_CN.get(a.p2_name, a.p2_name)
        aspect = ASPECT_CN.get(a.aspect, a.aspect)
        lines.append(f'| {p1} | {aspect} | {p2} | {a.orbit:.1f}° |')

    lines.append('')

    # 元素与模式分布
    lines.append('## 元素与模式分布')
    lines.append('')
    ed = chart.element_distribution
    lines.append(f'| 元素 | 火 | 土 | 风 | 水 |')
    lines.append(f'|------|----|----|----|----|')
    lines.append(f'| 权重 | {ed.fire:.1f} | {ed.earth:.1f} | {ed.air:.1f} | {ed.water:.1f} |')
    lines.append('')

    qd = chart.quality_distribution
    lines.append(f'| 模式 | 基本 | 固定 | 变动 |')
    lines.append(f'|------|------|------|------|')
    lines.append(f'| 权重 | {qd.cardinal:.1f} | {qd.fixed:.1f} | {qd.mutable:.1f} |')
    lines.append('')

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='西洋占星排盘')
    parser.add_argument('--year', type=int, required=True)
    parser.add_argument('--month', type=int, required=True)
    parser.add_argument('--day', type=int, required=True)
    parser.add_argument('--hour', type=int, required=True)
    parser.add_argument('--minute', type=int, default=0)
    parser.add_argument('--lat', type=float, required=True)
    parser.add_argument('--lng', type=float, required=True)
    parser.add_argument('--tz', type=str, required=True, help='Timezone string, e.g. Asia/Shanghai')
    parser.add_argument('--house-system', type=str, default='P',
                        help='宫位制: P=Placidus, K=Koch, W=Whole Sign, A=Equal 等（默认P）')
    args = parser.parse_args()

    result = generate_western_md(args.year, args.month, args.day, args.hour, args.minute,
                                  args.lat, args.lng, args.tz, args.house_system)
    print(result)


if __name__ == '__main__':
    main()
