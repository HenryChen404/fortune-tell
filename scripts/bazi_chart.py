#!/usr/bin/env python3.11
"""八字五行排盘脚本 — 基于 lunar_python"""

import argparse
import sys
from lunar_python import Solar


WUXING_MAP = {
    '甲': '木', '乙': '木', '丙': '火', '丁': '火', '戊': '土',
    '己': '土', '庚': '金', '辛': '金', '壬': '水', '癸': '水',
    '子': '水', '丑': '土', '寅': '木', '卯': '木', '辰': '土',
    '巳': '火', '午': '火', '未': '土', '申': '金', '酉': '金',
    '戌': '土', '亥': '水',
}


def hour_minute_to_shichen(hour, minute):
    """将时分转换为时辰描述"""
    total = hour * 60 + minute
    shichen = [
        (0, '早子'), (60, '丑'), (180, '寅'), (300, '卯'),
        (420, '辰'), (540, '巳'), (660, '午'), (780, '未'),
        (900, '申'), (1020, '酉'), (1140, '戌'), (1260, '亥'), (1380, '晚子'),
    ]
    name = '早子'
    for start, n in shichen:
        if total >= start:
            name = n
    return name


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


def generate_bazi_md(year, month, day, hour, minute, gender):
    solar = Solar(year, month, day, hour, minute, 0)
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

    # 地支十神
    lines.append('| 位置 | 地支 | 十神 |')
    lines.append('|------|------|------|')
    lines.append(f'| 年支 | {ba.getYear()[1]} | {ba.getYearShiShenZhi()[0] if ba.getYearShiShenZhi() else ""} |')
    lines.append(f'| 月支 | {ba.getMonth()[1]} | {ba.getMonthShiShenZhi()[0] if ba.getMonthShiShenZhi() else ""} |')
    lines.append(f'| 日支 | {ba.getDay()[1]} | {ba.getDayShiShenZhi()[0] if ba.getDayShiShenZhi() else ""} |')
    lines.append(f'| 时支 | {ba.getTime()[1]} | {ba.getTimeShiShenZhi()[0] if ba.getTimeShiShenZhi() else ""} |')
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
    parser.add_argument('--gender', type=str, required=True, help='male/female/男/女')
    args = parser.parse_args()

    result = generate_bazi_md(args.year, args.month, args.day, args.hour, args.minute, args.gender)
    print(result)


if __name__ == '__main__':
    main()
