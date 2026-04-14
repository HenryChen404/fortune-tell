#!/usr/bin/env python3.11
"""吠陀占星排盘脚本 — 基于 PyJHora"""

import argparse
import sys
import collections
from jhora import utils
from jhora.panchanga import drik
from jhora.horoscope.dhasa.graha import vimsottari

Place = collections.namedtuple('Place', ['Place', 'latitude', 'longitude', 'timezone'])

PLANET_NAMES = {
    0: 'Sun / 太阳', 1: 'Moon / 月亮', 2: 'Mars / 火星',
    3: 'Mercury / 水星', 4: 'Jupiter / 木星', 5: 'Venus / 金星',
    6: 'Saturn / 土星', 7: 'Rahu / 罗睺', 8: 'Ketu / 计都',
    9: 'Uranus', 10: 'Neptune', 11: 'Pluto',
}

PLANET_NAMES_SHORT = {
    0: 'Sun', 1: 'Moon', 2: 'Mars', 3: 'Mercury',
    4: 'Jupiter', 5: 'Venus', 6: 'Saturn', 7: 'Rahu', 8: 'Ketu',
}

SIGN_NAMES = [
    'Aries / 白羊', 'Taurus / 金牛', 'Gemini / 双子', 'Cancer / 巨蟹',
    'Leo / 狮子', 'Virgo / 处女', 'Libra / 天秤', 'Scorpio / 天蝎',
    'Sagittarius / 射手', 'Capricorn / 摩羯', 'Aquarius / 水瓶', 'Pisces / 双鱼',
]

NAKSHATRA_NAMES = [
    'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira',
    'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha', 'Magha',
    'Purva Phalguni', 'Uttara Phalguni', 'Hasta', 'Chitra', 'Swati',
    'Vishakha', 'Anuradha', 'Jyeshtha', 'Mula', 'Purva Ashadha',
    'Uttara Ashadha', 'Shravana', 'Dhanishta', 'Shatabhisha',
    'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati',
]

DASHA_LORDS = {
    0: 'Sun', 1: 'Moon', 2: 'Mars', 3: 'Mercury',
    4: 'Jupiter', 5: 'Venus', 6: 'Saturn', 7: 'Rahu', 8: 'Ketu',
}

DASHA_YEARS = {
    0: 6, 1: 10, 2: 7, 3: 17, 4: 16, 5: 20, 6: 19, 7: 18, 8: 7,
}


def format_deg(deg):
    d = int(deg)
    m = int((deg - d) * 60)
    return f"{d}°{m:02d}'"


def generate_vedic_md(year, month, day, hour, minute, lat, lng, tz_offset, gender):
    jd = utils.julian_day_number((year, month, day), (hour, minute, 0))
    place = Place('BirthPlace', lat, lng, tz_offset)
    is_male = gender.lower() in ('male', '男', 'm')

    lines = []
    lines.append('# 吠陀占星命盘 (Vedic / Jyotish)')
    lines.append('')
    lines.append('## 基本信息')
    lines.append('')
    lines.append(f'- 性别: {"男" if is_male else "女"}')
    lines.append(f'- 出生时间: {year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}')
    lines.append(f'- 坐标: {lat}°N, {lng}°E')
    lines.append(f'- 时区: UTC+{tz_offset}')
    lines.append('')

    # Rasi chart (D-1)
    lines.append('## Rasi Chart (本命盘 D-1)')
    lines.append('')

    # Get ascendant
    try:
        asc = drik.ascendant(jd, place)
        lines.append(f'- Lagna (上升点): {SIGN_NAMES[asc[0]]} {format_deg(asc[1])}')
        lines.append('')
    except Exception:
        lines.append('- Lagna: (计算失败)')
        lines.append('')

    # Planet positions
    lines.append('| 行星 | 星座 (Rashi) | 度数 |')
    lines.append('|------|-------------|------|')

    try:
        planet_positions = drik.dhasavarga(jd, place, divisional_chart_factor=1)
        for entry in planet_positions:
            pid = entry[0]
            sign, deg = entry[1]
            name = PLANET_NAMES.get(pid, str(pid))
            if sign < len(SIGN_NAMES):
                lines.append(f'| {name} | {SIGN_NAMES[sign]} | {format_deg(deg)} |')
    except Exception as e:
        lines.append(f'| (计算出错: {e}) | | |')

    lines.append('')

    # Nakshatra
    lines.append('## Nakshatra (月亮星宿)')
    lines.append('')
    try:
        nak = drik.nakshatra(jd, place)
        nak_index = int(nak[0]) - 1
        nak_pada = int(nak[1])
        nak_name = NAKSHATRA_NAMES[nak_index] if 0 <= nak_index < 27 else str(nak[0])
        lines.append(f'- Nakshatra: {nak_name}')
        lines.append(f'- Pada: {nak_pada}')
    except Exception as e:
        lines.append(f'- (计算出错: {e})')

    lines.append('')

    # Vimsottari Dasha
    lines.append('## Vimsottari Dasha (大运体系)')
    lines.append('')

    try:
        balance, dashas = vimsottari.get_vimsottari_dhasa_bhukthi(jd, place)

        # Group by mahadasha (first element of the tuple is the lord chain)
        lines.append('### Mahadasha (主运)')
        lines.append('')
        lines.append('| 主运行星 | 周期 | 起始日期 | 持续(年) |')
        lines.append('|----------|------|----------|----------|')

        seen_maha = set()
        for d in dashas:
            lords = d[0]
            date_tuple = d[1]
            duration = d[2]
            if len(lords) == 1:
                lord_id = lords[0]
                lord_name = DASHA_LORDS.get(lord_id, str(lord_id))
                total_years = DASHA_YEARS.get(lord_id, duration)
                y, m, dy = int(date_tuple[0]), int(date_tuple[1]), int(date_tuple[2])
                if lord_id not in seen_maha:
                    lines.append(f'| {lord_name} | {total_years}年 | {y}-{m:02d}-{dy:02d} | {duration:.1f} |')
                    seen_maha.add(lord_id)
            elif len(lords) == 2:
                # Antardasha — collect for current period display
                pass

        lines.append('')

        # Show current period's antardashas
        lines.append('### Antardasha 明细（前20条）')
        lines.append('')
        lines.append('| 主运 | 子运 | 起始日期 | 持续(年) |')
        lines.append('|------|------|----------|----------|')

        count = 0
        for d in dashas:
            lords = d[0]
            date_tuple = d[1]
            duration = d[2]
            if len(lords) == 2:
                maha = DASHA_LORDS.get(lords[0], str(lords[0]))
                antar = DASHA_LORDS.get(lords[1], str(lords[1]))
                y, m, dy = int(date_tuple[0]), int(date_tuple[1]), int(date_tuple[2])
                lines.append(f'| {maha} | {antar} | {y}-{m:02d}-{dy:02d} | {duration:.2f} |')
                count += 1
                if count >= 20:
                    break

    except Exception as e:
        lines.append(f'(Dasha 计算出错: {e})')

    lines.append('')

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='吠陀占星排盘')
    parser.add_argument('--year', type=int, required=True)
    parser.add_argument('--month', type=int, required=True)
    parser.add_argument('--day', type=int, required=True)
    parser.add_argument('--hour', type=int, required=True)
    parser.add_argument('--minute', type=int, default=0)
    parser.add_argument('--lat', type=float, required=True)
    parser.add_argument('--lng', type=float, required=True)
    parser.add_argument('--tz', type=float, required=True, help='Timezone offset, e.g. 8 for UTC+8')
    parser.add_argument('--gender', type=str, required=True, help='male/female/男/女')
    args = parser.parse_args()

    result = generate_vedic_md(args.year, args.month, args.day, args.hour, args.minute,
                                args.lat, args.lng, args.tz, args.gender)
    print(result)


if __name__ == '__main__':
    main()
