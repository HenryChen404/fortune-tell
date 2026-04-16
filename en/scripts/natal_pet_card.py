#!/usr/bin/env python3.11
"""
Natal Chart Pet Card Generator
Generates a Yu-Gi-Oh! style ASCII art card based on ZiWei Dou Shu main star,
with rarity determined by cross-system resonance (BaZi, Western, Vedic).
"""

import argparse
import os
import re
import sys
import time
import unicodedata

# ═══════════════════════════════════════════════════════════════
# DISPLAY WIDTH UTILITIES
# ═══════════════════════════════════════════════════════════════

def display_width(s):
    """Calculate terminal display width of a string."""
    w = 0
    for ch in s:
        eaw = unicodedata.east_asian_width(ch)
        w += 2 if eaw in ('F', 'W') else 1
    return w


def pad_to_width(text, width):
    """Pad text with trailing spaces to reach exact display width."""
    current = display_width(text)
    if current >= width:
        return text
    return text + ' ' * (width - current)


# ═══════════════════════════════════════════════════════════════
# ANSI COLOR UTILITIES
# ═══════════════════════════════════════════════════════════════

class Colors:
    RESET = '\033[0m'
    DIM = '\033[2m'
    BLINK = '\033[5m'
    BOLD = '\033[1m'

    # Rarity colors
    R_BORDER = '\033[90m'       # Gray
    R_NAME = '\033[1;90m'       # Bold gray
    SR_BORDER = '\033[32m'      # Green
    SR_NAME = '\033[1;32m'      # Bold green
    SSR_BORDER = '\033[35m'     # Magenta
    SSR_NAME = '\033[1;35m'     # Bold magenta
    SSSR_BORDER = '\033[33m'    # Gold/Yellow
    SSSR_NAME = '\033[1;33m'    # Bold yellow

    # Element colors
    FIRE = '\033[31m'
    EARTH = '\033[33m'
    METAL = '\033[37m'
    WATER = '\033[34m'
    WOOD = '\033[32m'


RARITY_STYLES = {
    'R':    {'border': Colors.R_BORDER,    'name': Colors.R_NAME,    'blink': False, 'stars': 3},
    'SR':   {'border': Colors.SR_BORDER,   'name': Colors.SR_NAME,   'blink': False, 'stars': 5},
    'SSR':  {'border': Colors.SSR_BORDER,  'name': Colors.SSR_NAME,  'blink': True,  'stars': 7},
    'SSSR': {'border': Colors.SSSR_BORDER, 'name': Colors.SSSR_NAME, 'blink': True,  'stars': 8},
}

ELEMENT_COLORS = {
    '火': Colors.FIRE, '土': Colors.EARTH, '金': Colors.METAL,
    '水': Colors.WATER, '木': Colors.WOOD,
    'Fire': Colors.FIRE, 'Earth': Colors.EARTH, 'Metal': Colors.METAL,
    'Water': Colors.WATER, 'Wood': Colors.WOOD,
}

# ═══════════════════════════════════════════════════════════════
# CARD DATA — ALL 14 CARDS
# ═══════════════════════════════════════════════════════════════

CARD_DATA = {
    "紫微": {
        "name_cn": "帝龙·紫微", "name_en": "Emperor Dragon",
        "element": "土", "element_en": "Earth",
        "base_atk": 2400, "base_def": 2200,
        "desc_cn": [
            "紫微帝星化形为龙，紫气缭绕，冠盖天下。",
            "命宫得此星者，天生王者之气，",
            "一念之间可定乾坤。",
        ],
        "desc_en": [
            "The Emperor Star takes the form of a great",
            "dragon wreathed in purple mist. Those born",
            "under its light carry the bearing of kings.",
        ],
        "art": [
            r"          /|    /| ",
            r"         / |   / | ",
            r"     ___/  |__/  | ",
            r"    /  o        / ",
            r"    | \/\/\/\  / ",
            r"     \_      _/ ",
            r"       \    / ",
            r"        \  / ",
            r"        _\/ ",
            r"       /\/\ ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "天机": {
        "name_cn": "织策·天机", "name_en": "Weaving Fox",
        "element": "木", "element_en": "Wood",
        "base_atk": 1600, "base_def": 2400,
        "desc_cn": [
            "天机星化身银狐，",
            "九尾间编织星图，策算万象。",
            "命得天机者，心思如丝，洞察先机。",
        ],
        "desc_en": [
            "The Strategist Star manifests as a silver",
            "fox weaving star-maps between its tails,",
            "calculating the myriad patterns of fate.",
        ],
        "art": [
            r"        /\ ",
            r"       /  \ ",
            r"      / o  | ",
            r"      |   _/ ",
            r"       \_/ ",
            r"       / \ ",
            r"      /   \___ ",
            r"     |   ////  \ ",
            r"     |  /////   | ",
            r"      \_/////  / ",
            r"        \_____/ ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "太阳": {
        "name_cn": "耀凤·太阳", "name_en": "Solar Phoenix",
        "element": "火", "element_en": "Fire",
        "base_atk": 2800, "base_def": 1600,
        "desc_cn": [
            "太阳星化身金凤，",
            "振翅则光耀四方，万物生辉。",
            "命得太阳者，胸怀磊落，光芒难掩。",
        ],
        "desc_en": [
            "The Sun Star takes the form of a golden",
            "phoenix. When it spreads its wings, light",
            "fills every corner and all things flourish.",
        ],
        "art": [
            r"          _ ",
            r"         /o \__ ",
            r"        / //   \ ",
            r"       / //     \ ",
            r"       |/       | ",
            r"       \       _/ ",
            r"        \_____/________ ",
            r"         \ / / / / / / ",
            r"          \/ / / / / / ",
            r"           \__________/ ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "武曲": {
        "name_cn": "铁骏·武曲", "name_en": "Iron Steed",
        "element": "金", "element_en": "Metal",
        "base_atk": 2600, "base_def": 2400,
        "desc_cn": [
            "武曲星化身铁骏，",
            "钢鬃如刃，铁蹄踏地则金石俱震。",
            "命得武曲者，刚毅果决，财帛丰厚。",
        ],
        "desc_en": [
            "The Warrior Star gallops forth as an Iron",
            "Steed, its steel mane like blades, its",
            "hooves shaking gold and stone alike.",
        ],
        "art": [
            r"            __ ",
            r"           //\ ",
            r"          // | ",
            r"         / o  \____ ",
            r"        |  /  /   _/ ",
            r"         \/  / __/ ",
            r"     /\   \_/ / ",
            r"    /  \   | / ",
            r"    |   |  | | ",
            r"    |   |  | | ",
            r"    |___|  |_| ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "天同": {
        "name_cn": "云鹿·天同", "name_en": "Cloud Deer",
        "element": "水", "element_en": "Water",
        "base_atk": 1400, "base_def": 2800,
        "desc_cn": [
            "天同星化身云鹿，行走于祥云之间，",
            "所过之处万物和谐。",
            "命得天同者，心性纯良，福泽绵长。",
        ],
        "desc_en": [
            "The Harmony Star becomes a Cloud Deer,",
            "walking among auspicious clouds.",
            "Wherever it passes, all things find peace.",
        ],
        "art": [
            r"        _/| ",
            r"       / /| ",
            r"      | / | ",
            r"      |/  | ",
            r"       \  | ",
            r"        \_| ",
            r"        /o \ ",
            r"       /    \___ ",
            r"      | - - -   \ ",
            r"      |   - -    | ",
            r"       \___|  |__/ ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "廉贞": {
        "name_cn": "焰蛇·廉贞", "name_en": "Inferno Serpent",
        "element": "火", "element_en": "Fire",
        "base_atk": 2600, "base_def": 1800,
        "desc_cn": [
            "廉贞星化身焰蛇，",
            "火鳞缠身，于暗处灼灼生辉。",
            "命得廉贞者，外冷内热，情深似渊。",
        ],
        "desc_en": [
            "The Passion Star coils into a Flame",
            "Serpent, its fire-scales smoldering in",
            "darkness. Those it marks burn with intensity.",
        ],
        "art": [
            r"        ______ ",
            r"       / o    \ ",
            r"       |       | ",
            r"        \_    / ",
            r"          \  / ",
            r"          / / ",
            r"         /\/ ",
            r"        / / ",
            r"       /\/ ",
            r"      / / ",
            r"     /__/ ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "天府": {
        "name_cn": "玉龟·天府", "name_en": "Jade Tortoise",
        "element": "土", "element_en": "Earth",
        "base_atk": 1800, "base_def": 3000,
        "desc_cn": [
            "天府星化身玉龟，",
            "背负山河，腹藏万宝。",
            "命得天府者，稳如磐石，富贵绵延。",
        ],
        "desc_en": [
            "The Treasury Star takes the form of a Jade",
            "Tortoise bearing mountains on its shell,",
            "holding ten thousand treasures within.",
        ],
        "art": [
            r"          ______ ",
            r"         /  /\  \ ",
            r"        / _/  \_ \ ",
            r"        | / \/ \ | ",
            r"         \______/ ",
            r"      __|        |__ ",
            r"     /o |        |  \ ",
            r"     \__|        |__/ ",
            r"         |__| |__| ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "太阴": {
        "name_cn": "霜鹤·太阴", "name_en": "Frost Crane",
        "element": "水", "element_en": "Water",
        "base_atk": 1600, "base_def": 2600,
        "desc_cn": [
            "太阴星化身霜鹤，月下独立，清冷如水。",
            "命得太阴者，",
            "心思细腻，洞若观火。",
        ],
        "desc_en": [
            "The Moon Star becomes a Frost Crane,",
            "standing alone beneath the moon, cold and",
            "clear as water. Its gaze perceives all.",
        ],
        "art": [
            r"          _ ",
            r"         /o\ ",
            r"          | ",
            r"         / ",
            r"        / ",
            r"         \ ",
            r"          \___ ",
            r"         / // \ ",
            r"        | ///  | ",
            r"         \____/ ",
            r"           || ",
            r"           || ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "贪狼": {
        "name_cn": "混元狼·贪狼", "name_en": "Chaos Wolf",
        "element": "木", "element_en": "Wood",
        "base_atk": 2400, "base_def": 1800,
        "desc_cn": [
            "贪狼星化身混元之狼，",
            "七变其形，百纳其能。",
            "命得贪狼者，欲壑难填，才华横溢。",
        ],
        "desc_en": [
            "The Desire Star becomes the Chaos Wolf,",
            "shifting between seven forms, absorbing",
            "a hundred talents. Boundless ability.",
        ],
        "art": [
            r"       /\ ",
            r"      /  | ",
            r"     /   / ",
            r"    /   / ",
            r"    |o / ",
            r"    | / ",
            r"     \|_____ ",
            r"     / //   \ ",
            r"    | ///    | ",
            r"    |  //   / ",
            r"     \____/ ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "巨门": {
        "name_cn": "渊枭·巨门", "name_en": "Abyssal Owl",
        "element": "水", "element_en": "Water",
        "base_atk": 2200, "base_def": 2000,
        "desc_cn": [
            "巨门星化身渊枭，",
            "暗夜中双瞳如炬，一鸣可破虚妄。",
            "命得巨门者，明察秋毫，言辞犀利。",
        ],
        "desc_en": [
            "The Communication Star becomes the Abyssal",
            "Owl, its twin eyes blazing in darkness.",
            "One cry shatters all illusion.",
        ],
        "art": [
            r"       ___     ___ ",
            r"      /   \   /   \ ",
            r"     | / \ | | / \ | ",
            r"     | \o/ | | \o/ | ",
            r"      \___/   \___/ ",
            r"          |   | ",
            r"          |   | ",
            r"          |\/\| ",
            r"          |/\/| ",
            r"           \_/ ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "天相": {
        "name_cn": "天鹅·天相", "name_en": "Harmony Swan",
        "element": "水", "element_en": "Water",
        "base_atk": 1800, "base_def": 2400,
        "desc_cn": [
            "天相星化身天鹅，",
            "于碧波之上优雅游弋，不偏不倚。",
            "命得天相者，进退有度，左右逢源。",
        ],
        "desc_en": [
            "The Minister Star takes the form of a",
            "graceful Swan gliding upon still waters,",
            "perfectly balanced and impartial.",
        ],
        "art": [
            r"          _ ",
            r"         /o\ ",
            r"          | \ ",
            r"           \ \ ",
            r"            | | ",
            r"           / | ",
            r"          /  |___ ",
            r"         | ////  \ ",
            r"         |/////   | ",
            r"    ~~~~~~\______/~~~~ ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "天梁": {
        "name_cn": "玄龟·天梁", "name_en": "Ancient Tortoise",
        "element": "土", "element_en": "Earth",
        "base_atk": 1600, "base_def": 3200,
        "desc_cn": [
            "天梁星化身玄龟，",
            "阅尽沧桑，甲如磐石，守护四方。",
            "命得天梁者，化险为夷，长者之风。",
        ],
        "desc_en": [
            "The Wisdom Star manifests as the Ancient",
            "Tortoise, shell like bedrock, guardian",
            "of the four directions across all ages.",
        ],
        "art": [
            r"        ___________ ",
            r"       /  ---  ---  \ ",
            r"      / ---  /---\  \ ",
            r"     | ---  ---  --- | ",
            r"     |  ---   ---    | ",
            r"      \______________/ ",
            r"    __|              |__ ",
            r"   /o |              |  \ ",
            r"   \__|              |__/ ",
            r"       |__|      |__| ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "七杀": {
        "name_cn": "雷虎·七杀", "name_en": "Thunder Tiger",
        "element": "火", "element_en": "Fire",
        "base_atk": 3200, "base_def": 1400,
        "desc_cn": [
            "七杀星化身雷虎，",
            "踏雷而行，势不可挡。",
            "命得七杀者，刚猛无匹，破釜沉舟。",
        ],
        "desc_en": [
            "The Power Star becomes the Thunder Tiger,",
            "riding lightning, unstoppable in its charge.",
            "Those born under its sign fight to the end.",
        ],
        "art": [
            r"        ____ ",
            r"       / o  \________ ",
            r"      /  \/    |  |  \ ",
            r"      \_    |  |  |   | ",
            r"        \   |  |  |  / ",
            r"         \__|__|__|_/ ",
            r"         /  |  |  | \ ",
            r"        |   |  |  |  | ",
            r"        |___|  |  |__| ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
    "破军": {
        "name_cn": "暴岚鹰·破军", "name_en": "Storm Hawk",
        "element": "金", "element_en": "Metal",
        "base_atk": 2800, "base_def": 1200,
        "desc_cn": [
            "破军星化身暴岚之鹰，",
            "所过之处风云变色。",
            "命得破军者，不破不立，革故鼎新。",
        ],
        "desc_en": [
            "The Revolution Star becomes the Storm Hawk.",
            "Where it flies, wind and cloud change color.",
            "Those it marks must destroy to rebuild.",
        ],
        "art": [
            r"        /o\ ",
            r"       / _/ ",
            r"      / /______ ",
            r"      |/       \ ",
            r"       \        | ",
            r"       /\    __/ ",
            r"      /  \__/ ",
            r"     / ///   \ ",
            r"    | ////    | ",
            r"     \________/ ",
            r"    ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        ],
    },
}


# ═══════════════════════════════════════════════════════════════
# CHART PARSERS
# ═══════════════════════════════════════════════════════════════

def parse_ziwei(filepath):
    """Parse ZiWei Dou Shu chart markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        'main_star': None,
        'brightness': None,
        'stars_in_ming': [],         # all stars in 命宫
        'minor_stars_in_ming': [],   # 辅星 in 命宫
        'misc_stars_in_ming': [],    # 杂曜 in 命宫
        'all_palaces': {},           # palace -> {main_stars, minor_stars, misc_stars}
        'sihua': {},                 # 禄/权/科/忌 -> {star, palace}
    }

    # Parse 十二宫排盘 table to find 命宫 main star
    table_pattern = r'\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|'
    for m in re.finditer(table_pattern, content):
        palace = m.group(1).strip()
        ganzi = m.group(2).strip()
        main_stars_raw = m.group(3).strip()
        minor_stars_raw = m.group(4).strip()
        misc_stars_raw = m.group(5).strip()

        # Skip header rows
        if palace in ('宫位', '---', '----'):
            continue

        # Parse main stars: e.g. "天同(平)" or "武曲(平)、破军(平)" or "—"
        main_stars = []
        for star_match in re.finditer(r'([\u4e00-\u9fff]+)\((\S+?)\)', main_stars_raw):
            main_stars.append({
                'name': star_match.group(1),
                'brightness': star_match.group(2),
            })

        # Parse minor stars
        minor_stars = []
        for part in re.split(r'[、，,]', minor_stars_raw):
            part = part.strip().replace('—', '').replace('—', '')
            if part:
                name_m = re.match(r'([\u4e00-\u9fff]+)', part)
                if name_m:
                    minor_stars.append(name_m.group(1))

        palace_data = {
            'main_stars': main_stars,
            'minor_stars': minor_stars,
            'raw_main': main_stars_raw,
        }
        data['all_palaces'][palace] = palace_data

        if palace == '命宫':
            data['stars_in_ming'] = main_stars
            data['minor_stars_in_ming'] = minor_stars
            data['misc_stars_in_ming'] = [s.strip() for s in re.split(r'[、，,]', misc_stars_raw) if s.strip() and s.strip() != '—']

            # Find the first star that is one of the 14 main stars
            fourteen = set(CARD_DATA.keys())
            for s in main_stars:
                if s['name'] in fourteen:
                    data['main_star'] = s['name']
                    data['brightness'] = s['brightness']
                    break

    # Fallback: if 命宫 has no 14-main-star, try 身宫主星 from basic info
    if not data['main_star']:
        m = re.search(r'身宫主星:\s*([\u4e00-\u9fff]+)', content)
        if m and m.group(1) in CARD_DATA:
            data['main_star'] = m.group(1)
            data['brightness'] = '平'  # default

    # Parse 四化
    for m in re.finditer(r'(禄|权|科|忌):\s*([\u4e00-\u9fff]+)\s*在\s*([\u4e00-\u9fff]+)', content):
        data['sihua'][m.group(1)] = {'star': m.group(2), 'palace': m.group(3)}

    return data


def parse_bazi(filepath):
    """Parse BaZi chart markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        'day_master': None,       # e.g. '辛'
        'day_master_element': None,  # e.g. '金'
        'elements': {},           # {'金': 4, '木': 0, ...}
        'ten_gods_tiangan': {},   # {'年干': '比肩', '月干': '正官', ...}
        'ten_gods_dizhi': {},     # {'年支': ['正官', '劫财', '正印'], ...}
        'all_ten_gods': [],       # flat list of all ten gods
    }

    # Parse 日主
    m = re.search(r'日主:\s*([\u4e00-\u9fff])（([\u4e00-\u9fff])）', content)
    if m:
        data['day_master'] = m.group(1)
        data['day_master_element'] = m.group(2)

    # Parse 五行统计
    elem_pattern = r'\|\s*数量\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|'
    m = re.search(elem_pattern, content)
    if m:
        data['elements'] = {
            '金': int(m.group(1)), '木': int(m.group(2)),
            '水': int(m.group(3)), '火': int(m.group(4)),
            '土': int(m.group(5)),
        }

    # Parse 十神 (天干)
    tiangan_pattern = r'\|\s*(年干|月干|日干|时干)\s*\|\s*\S+\s*\|\s*(\S+)\s*\|'
    for m in re.finditer(tiangan_pattern, content):
        pos = m.group(1)
        god = m.group(2)
        data['ten_gods_tiangan'][pos] = god
        if god != '日主':
            data['all_ten_gods'].append(god)

    # Parse 十神 (地支藏干)
    dizhi_pattern = r'\|\s*(年支|月支|日支|时支)\s*\|\s*\S+\s*\|\s*(.+?)\s*\|'
    for m in re.finditer(dizhi_pattern, content):
        pos = m.group(1)
        gods = [g.strip() for g in m.group(2).split('、') if g.strip()]
        data['ten_gods_dizhi'][pos] = gods
        data['all_ten_gods'].extend(gods)

    return data


def parse_western(filepath):
    """Parse Western astrology chart markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        'planets': {},     # planet -> {sign, house, degree, retrograde}
        'aspects': [],     # [{p1, aspect_type, p2, orb}, ...]
        'rising_sign': None,
        'mc_sign': None,
        'elements': {},    # {'火': 6.6, '土': 5.5, ...}
    }

    # Parse basic info
    m = re.search(r'上升星座:\s*(\S+座)', content)
    if m:
        data['rising_sign'] = m.group(1)

    m = re.search(r'天顶\(MC\):\s*(\S+座)', content)
    if m:
        data['mc_sign'] = m.group(1)

    # Parse planet positions
    planet_pattern = r'\|\s*([\u4e00-\u9fff]+(?:星)?)\s*\|\s*(\S+座)\s*\|\s*[\d°\'"]+\s*\|\s*第(\d+)宫\s*\|\s*(.*?)\s*\|'
    for m in re.finditer(planet_pattern, content):
        planet = m.group(1)
        data['planets'][planet] = {
            'sign': m.group(2),
            'house': int(m.group(3)),
            'retrograde': '℞' in m.group(4),
        }

    # Parse aspects
    aspect_pattern = r'\|\s*([\u4e00-\u9fff]+(?:星|点)?)\s*\|\s*(\S+)\s*\(\d+°\)\s*\|\s*([\u4e00-\u9fff]+(?:星|点)?)\s*\|\s*([\d.]+)°\s*\|'
    for m in re.finditer(aspect_pattern, content):
        data['aspects'].append({
            'p1': m.group(1),
            'type': m.group(2),
            'p2': m.group(3),
            'orb': float(m.group(4)),
        })

    # Parse element weights
    elem_w_pattern = r'\|\s*权重\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|'
    m = re.search(elem_w_pattern, content)
    if m:
        data['elements'] = {
            '火': float(m.group(1)), '土': float(m.group(2)),
            '风': float(m.group(3)), '水': float(m.group(4)),
        }

    return data


def parse_vedic(filepath):
    """Parse Vedic astrology chart markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        'lagna_sign': None,       # e.g. 'Pisces'
        'rasi_planets': {},       # planet_en -> sign_en
        'navamsa_planets': {},    # planet_en -> sign_en
        'nakshatra': None,
        'nakshatra_pada': None,
        'dasha': [],              # [{planet, start, duration}, ...]
    }

    # Parse Lagna
    m = re.search(r'Lagna.*?:\s*(\w+)\s*/\s*[\u4e00-\u9fff]+\s*[\d°\'"]+', content)
    if m:
        data['lagna_sign'] = m.group(1)

    # Parse Rasi chart planets
    rasi_pattern = r'\|\s*(\w+)\s*/\s*[\u4e00-\u9fff]+\s*\|\s*(\w+)\s*/\s*[\u4e00-\u9fff]+\s*\|\s*[\d°\'"]+\s*\|'
    in_rasi = False
    in_navamsa = False
    for line in content.split('\n'):
        if 'Rasi Chart' in line:
            in_rasi = True
            in_navamsa = False
            continue
        if 'Navamsa Chart' in line:
            in_rasi = False
            in_navamsa = True
            continue
        if 'Nakshatra' in line and 'Nakshatra:' not in line:
            in_rasi = False
            in_navamsa = False
            continue

        m = re.search(r'\|\s*(\w+)\s*/\s*[\u4e00-\u9fff]+\s*\|\s*(\w+)\s*/\s*[\u4e00-\u9fff]+\s*\|\s*[\d°\'"]+\s*\|', line)
        if not m:
            # Try pattern without Chinese
            m = re.search(r'\|\s*(\w+)\s*\|\s*(\w+)\s*/\s*[\u4e00-\u9fff]+\s*\|\s*[\d°\'"]+\s*\|', line)
        if m:
            planet = m.group(1)
            sign = m.group(2)
            if in_rasi:
                data['rasi_planets'][planet] = sign
            elif in_navamsa:
                data['navamsa_planets'][planet] = sign

    # Parse Nakshatra
    m = re.search(r'Nakshatra:\s*(\w+)', content)
    if m:
        data['nakshatra'] = m.group(1)

    m = re.search(r'Pada:\s*(\d+)', content)
    if m:
        data['nakshatra_pada'] = int(m.group(1))

    return data


# ═══════════════════════════════════════════════════════════════
# VEDIC HELPER — HOUSE CALCULATION
# ═══════════════════════════════════════════════════════════════

SIGN_ORDER = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

def vedic_house_of(planet_sign, lagna_sign):
    """Calculate which house a planet is in based on Lagna (whole sign)."""
    if planet_sign not in SIGN_ORDER or lagna_sign not in SIGN_ORDER:
        return None
    lagna_idx = SIGN_ORDER.index(lagna_sign)
    planet_idx = SIGN_ORDER.index(planet_sign)
    return ((planet_idx - lagna_idx) % 12) + 1


def is_kendra(house):
    """Check if house is a Kendra (angular house: 1, 4, 7, 10)."""
    return house in (1, 4, 7, 10)


def vedic_sign_lord(sign):
    """Return the traditional ruling planet of a sign."""
    lords = {
        'Aries': 'Mars', 'Taurus': 'Venus', 'Gemini': 'Mercury',
        'Cancer': 'Moon', 'Leo': 'Sun', 'Virgo': 'Mercury',
        'Libra': 'Venus', 'Scorpio': 'Mars', 'Sagittarius': 'Jupiter',
        'Capricorn': 'Saturn', 'Aquarius': 'Saturn', 'Pisces': 'Jupiter',
    }
    return lords.get(sign)


# ═══════════════════════════════════════════════════════════════
# CROSS-SYSTEM RESONANCE CHECKING
# ═══════════════════════════════════════════════════════════════

# Western sign groups
EARTH_SIGNS_W = {'金牛座', '处女座', '摩羯座'}
FIRE_SIGNS_W = {'白羊座', '狮子座', '射手座'}
WATER_SIGNS_W = {'巨蟹座', '天蝎座', '双鱼座'}
AIR_SIGNS_W = {'双子座', '天秤座', '水瓶座'}

def _count_ten_god(bazi, god_name):
    """Count occurrences of a ten god in BaZi chart."""
    return sum(1 for g in bazi['all_ten_gods'] if g == god_name)


def _has_ten_god_in_month(bazi, god_name):
    """Check if a ten god appears in the month stem."""
    return bazi['ten_gods_tiangan'].get('月干') == god_name


def _planet_in_houses(western, planet, houses):
    """Check if a Western planet is in any of the given houses."""
    p = western['planets'].get(planet)
    return p is not None and p['house'] in houses


def _planet_in_signs(western, planet, signs):
    """Check if a Western planet is in any of the given signs."""
    p = western['planets'].get(planet)
    return p is not None and p['sign'] in signs


def _has_hard_aspect(western, p1, p2, max_orb=5.0):
    """Check if two planets have a hard aspect (conjunction/square/opposition)."""
    hard_types = {'合相', '四分相', '对分相'}
    for asp in western['aspects']:
        if asp['orb'] > max_orb:
            continue
        if asp['type'] in hard_types:
            names = {asp['p1'], asp['p2']}
            if p1 in names and p2 in names:
                return True
    return False


def _vedic_planet_in_kendra(vedic, planet):
    """Check if a planet is in a Kendra house in Vedic chart."""
    sign = vedic['rasi_planets'].get(planet)
    if not sign or not vedic['lagna_sign']:
        return False
    house = vedic_house_of(sign, vedic['lagna_sign'])
    return house is not None and is_kendra(house)


def _vedic_planet_in_sign(vedic, planet, signs):
    """Check if a Vedic planet is in any of the given signs."""
    sign = vedic['rasi_planets'].get(planet)
    return sign in signs


def _vedic_lagna_lord_in_kendra(vedic):
    """Check if the Lagna lord is in a Kendra house."""
    if not vedic['lagna_sign']:
        return False
    lord = vedic_sign_lord(vedic['lagna_sign'])
    if not lord:
        return False
    return _vedic_planet_in_kendra(vedic, lord)


def check_resonance(star, bazi, western, vedic):
    """Check cross-system resonance for a given ZiWei main star.
    Returns list of resonating systems: ['bazi', 'western', 'vedic']
    """
    resonances = []

    checks = RESONANCE_CHECKS.get(star, {})

    if checks.get('bazi') and checks['bazi'](bazi):
        resonances.append('bazi')
    if checks.get('western') and checks['western'](western):
        resonances.append('western')
    if checks.get('vedic') and checks['vedic'](vedic):
        resonances.append('vedic')

    return resonances


# Resonance check functions for each star
RESONANCE_CHECKS = {
    "紫微": {
        "bazi": lambda b: _has_ten_god_in_month(b, '正官') or _count_ten_god(b, '七杀') >= 2,
        "western": lambda w: _planet_in_houses(w, '太阳', {10}) or _planet_in_houses(w, '火星', {10}) or w.get('mc_sign') == '摩羯座',
        "vedic": lambda v: _vedic_planet_in_sign(v, 'Sun', {'Leo'}) or _vedic_lagna_lord_in_kendra(v),
    },
    "天机": {
        "bazi": lambda b: _count_ten_god(b, '偏印') >= 2 or (_count_ten_god(b, '正印') + _count_ten_god(b, '偏印')) >= 3,
        "western": lambda w: _planet_in_houses(w, '水星', {1, 4, 7, 10}) or _planet_in_signs(w, '水星', {'处女座', '双子座'}),
        "vedic": lambda v: _vedic_planet_in_kendra(v, 'Mercury') or (_vedic_planet_in_kendra(v, 'Jupiter') and _vedic_planet_in_kendra(v, 'Mercury')),
    },
    "太阳": {
        "bazi": lambda b: b['day_master'] in ('丙', '丁') or b['elements'].get('火', 0) >= 3,
        "western": lambda w: _planet_in_houses(w, '太阳', {1, 10}) or w.get('rising_sign') == '狮子座',
        "vedic": lambda v: _vedic_planet_in_sign(v, 'Sun', {'Leo', 'Aries'}) or _vedic_planet_in_kendra(v, 'Sun'),
    },
    "武曲": {
        "bazi": lambda b: (_has_ten_god_in_month(b, '正财') or _has_ten_god_in_month(b, '偏财')) or ((_count_ten_god(b, '正财') + _count_ten_god(b, '偏财')) >= 2 and b['elements'].get(b.get('day_master_element', ''), 0) >= 3),
        "western": lambda w: _planet_in_signs(w, '火星', EARTH_SIGNS_W) or _planet_in_houses(w, '金星', {2, 8}),
        "vedic": lambda v: _vedic_planet_in_sign(v, 'Mars', {'Aries', 'Scorpio', 'Capricorn'}) or (lambda: (lord := vedic_sign_lord(v['rasi_planets'].get('Venus', ''))) is not None and _vedic_planet_in_kendra(v, lord) if v.get('lagna_sign') else False)(),
    },
    "天同": {
        "bazi": lambda b: _has_ten_god_in_month(b, '食神') or (max(b['elements'].values(), default=0) - min(b['elements'].values(), default=0) <= 2 if b['elements'] else False),
        "western": lambda w: _planet_in_signs(w, '金星', {'金牛座', '天秤座', '双鱼座'}) or _planet_in_signs(w, '月亮', {'巨蟹座', '金牛座'}),
        "vedic": lambda v: _vedic_planet_in_kendra(v, 'Venus') or _vedic_planet_in_sign(v, 'Moon', {'Cancer', 'Taurus'}),
    },
    "廉贞": {
        "bazi": lambda b: ('正官' in [b['ten_gods_tiangan'].get(k) for k in ('年干', '月干', '时干')] and '七杀' in [b['ten_gods_tiangan'].get(k) for k in ('年干', '月干', '时干')]) or (_has_ten_god_in_month(b, '伤官') and _count_ten_god(b, '正官') >= 1),
        "western": lambda w: _planet_in_houses(w, '冥王星', {1, 4, 7, 10}) or _has_hard_aspect(w, '太阳', '冥王星') or _has_hard_aspect(w, '月亮', '冥王星'),
        "vedic": lambda v: _vedic_planet_in_kendra(v, 'Rahu') or _vedic_planet_in_kendra(v, 'Ketu') or (v['rasi_planets'].get('Mars') == v['rasi_planets'].get('Saturn') and v['rasi_planets'].get('Mars') is not None),
    },
    "天府": {
        "bazi": lambda b: (_count_ten_god(b, '正财') >= 1 and _count_ten_god(b, '正印') >= 1),
        "western": lambda w: _planet_in_houses(w, '木星', {2, 4}) or (_planet_in_signs(w, '金星', EARTH_SIGNS_W) and _planet_in_houses(w, '金星', {1, 4, 7, 10})),
        "vedic": lambda v: _vedic_planet_in_kendra(v, 'Jupiter'),
    },
    "太阴": {
        "bazi": lambda b: b['day_master'] in ('壬', '癸') or (b['elements'].get('水', 0) >= 2 and _count_ten_god(b, '正印') >= 1),
        "western": lambda w: _planet_in_signs(w, '月亮', {'巨蟹座', '双鱼座', '金牛座'}) or _planet_in_houses(w, '月亮', {4, 8, 12}),
        "vedic": lambda v: _vedic_planet_in_sign(v, 'Moon', {'Cancer', 'Taurus'}) or _vedic_planet_in_kendra(v, 'Moon'),
    },
    "贪狼": {
        "bazi": lambda b: _count_ten_god(b, '偏财') >= 2 or (_count_ten_god(b, '食神') >= 1 and _count_ten_god(b, '偏财') >= 1),
        "western": lambda w: _planet_in_houses(w, '金星', {5}) or any(a for a in w['aspects'] if {a['p1'], a['p2']} == {'火星', '金星'} and a['orb'] <= 5),
        "vedic": lambda v: _vedic_planet_in_sign(v, 'Venus', {'Taurus', 'Libra'}) or _vedic_planet_in_kendra(v, 'Rahu'),
    },
    "巨门": {
        "bazi": lambda b: _has_ten_god_in_month(b, '伤官') or _count_ten_god(b, '伤官') >= 2,
        "western": lambda w: _planet_in_houses(w, '水星', {3, 9}) or sum(1 for p in w['planets'].values() if p['sign'] in {'双子座', '处女座'}) >= 3,
        "vedic": lambda v: (lambda h: h in (2, 3) if h else False)(vedic_house_of(v['rasi_planets'].get('Mercury', ''), v.get('lagna_sign', ''))) or (lambda h: h == 3 if h else False)(vedic_house_of(v['rasi_planets'].get('Rahu', ''), v.get('lagna_sign', ''))),
    },
    "天相": {
        "bazi": lambda b: (_has_ten_god_in_month(b, '正官') and _count_ten_god(b, '七杀') == 0) or (_count_ten_god(b, '正印') >= 1 and _count_ten_god(b, '正官') >= 1),
        "western": lambda w: _planet_in_houses(w, '金星', {7}) or w.get('rising_sign') == '天秤座' or _planet_in_signs(w, '太阳', {'天秤座'}),
        "vedic": lambda v: (lambda h: is_kendra(h) if h else False)(vedic_house_of(v['rasi_planets'].get(vedic_sign_lord(SIGN_ORDER[(SIGN_ORDER.index(v['lagna_sign']) + 6) % 12]) if v.get('lagna_sign') and v['lagna_sign'] in SIGN_ORDER else '', ''), v.get('lagna_sign', ''))) or _vedic_planet_in_kendra(v, 'Venus'),
    },
    "天梁": {
        "bazi": lambda b: _has_ten_god_in_month(b, '正印') or _count_ten_god(b, '正印') >= 2,
        "western": lambda w: _planet_in_houses(w, '木星', {9, 12}) or (_planet_in_signs(w, '土星', {'摩羯座', '水瓶座'})),
        "vedic": lambda v: (lambda h: h == 9 if h else False)(vedic_house_of(v['rasi_planets'].get('Jupiter', ''), v.get('lagna_sign', ''))) or _vedic_planet_in_sign(v, 'Saturn', {'Capricorn', 'Aquarius', 'Libra'}),
    },
    "七杀": {
        "bazi": lambda b: _has_ten_god_in_month(b, '七杀') or _count_ten_god(b, '七杀') >= 2,
        "western": lambda w: _planet_in_signs(w, '火星', {'白羊座', '天蝎座', '摩羯座'}) or _planet_in_houses(w, '火星', {1, 10}),
        "vedic": lambda v: _vedic_planet_in_sign(v, 'Mars', {'Aries', 'Scorpio', 'Capricorn'}) or _vedic_planet_in_kendra(v, 'Mars'),
    },
    "破军": {
        "bazi": lambda b: _has_ten_god_in_month(b, '劫财') or (any(v == 0 for v in b['elements'].values()) and any(v >= 4 for v in b['elements'].values()) if b['elements'] else False),
        "western": lambda w: _planet_in_houses(w, '天王星', {1, 4, 7, 10}) or _has_hard_aspect(w, '太阳', '天王星') or _has_hard_aspect(w, '月亮', '天王星'),
        "vedic": lambda v: (lambda h: h in (1, 10) if h else False)(vedic_house_of(v['rasi_planets'].get('Rahu', ''), v.get('lagna_sign', ''))) or (lambda h: h in (4, 7) if h else False)(vedic_house_of(v['rasi_planets'].get('Ketu', ''), v.get('lagna_sign', ''))),
    },
}


# ═══════════════════════════════════════════════════════════════
# ATK / DEF CALCULATION
# ═══════════════════════════════════════════════════════════════

BRIGHTNESS_ATK = {'旺': 200, '庙': 200, '得': 100, '平': 0, '利': -50, '陷': -100}
RARITY_MULT = {'R': 1.0, 'SR': 1.1, 'SSR': 1.2, 'SSSR': 1.35}

ATTACK_MINOR_STARS = {'擎羊', '火星', '铃星'}
DEFENSE_MINOR_STARS = {'左辅', '右弼', '天魁', '天钺'}


def calculate_atk_def(star, ziwei, bazi, western, vedic, rarity):
    """Calculate ATK and DEF dynamically from natal chart data."""
    card = CARD_DATA[star]
    atk = card['base_atk']
    def_val = card['base_def']

    # --- ATK modifiers ---
    # BaZi: fire element
    atk += bazi['elements'].get('火', 0) * 150
    # BaZi: 七杀 + 伤官
    atk += (_count_ten_god(bazi, '七杀') + _count_ten_god(bazi, '伤官')) * 200

    # Western: Mars position
    mars = western['planets'].get('火星')
    if mars:
        if mars['house'] in (1, 10):
            atk += 300
        elif mars['sign'] in FIRE_SIGNS_W:
            atk += 200

    # Western: hard aspects on personal planets
    personal = {'太阳', '月亮', '水星', '金星', '火星'}
    hard_count = sum(1 for a in western['aspects']
                     if a['type'] in ('合相', '四分相', '对分相')
                     and (a['p1'] in personal or a['p2'] in personal)
                     and a['orb'] <= 5)
    atk += hard_count * 100

    # Vedic: Mars dignity
    if _vedic_planet_in_sign(vedic, 'Mars', {'Aries', 'Scorpio', 'Capricorn'}):
        atk += 250

    # ZiWei: brightness
    if ziwei['brightness']:
        atk += BRIGHTNESS_ATK.get(ziwei['brightness'], 0)

    # ZiWei: 煞星 in 命宫
    for ms in ziwei.get('minor_stars_in_ming', []):
        if ms in ATTACK_MINOR_STARS:
            atk += 150

    # --- DEF modifiers ---
    # BaZi: earth element
    def_val += bazi['elements'].get('土', 0) * 150
    # BaZi: 正印 + 偏印
    def_val += (_count_ten_god(bazi, '正印') + _count_ten_god(bazi, '偏印')) * 200

    # Western: Moon position
    moon = western['planets'].get('月亮')
    if moon:
        if moon['house'] == 4:
            def_val += 300
        elif moon['sign'] in WATER_SIGNS_W:
            def_val += 200

    # Western: harmonious aspects
    harmony_count = sum(1 for a in western['aspects']
                        if a['type'] in ('三分相', '六分相')
                        and (a['p1'] in personal or a['p2'] in personal)
                        and a['orb'] <= 5)
    def_val += harmony_count * 100

    # Vedic: Jupiter dignity
    if _vedic_planet_in_sign(vedic, 'Jupiter', {'Sagittarius', 'Pisces', 'Cancer'}):
        def_val += 250

    # ZiWei: 天府/天梁 in 命宫三方四正 (simplified: check all palaces)
    for palace, pdata in ziwei.get('all_palaces', {}).items():
        for ms in pdata.get('main_stars', []):
            if ms['name'] in ('天府', '天梁') and palace in ('命宫', '官禄', '迁移', '财帛'):
                def_val += 200
                break

    # ZiWei: 吉星 in 命宫
    for ms in ziwei.get('minor_stars_in_ming', []):
        if ms in DEFENSE_MINOR_STARS:
            def_val += 100

    # Apply rarity multiplier
    mult = RARITY_MULT.get(rarity, 1.0)
    atk = round(atk * mult / 50) * 50
    def_val = round(def_val * mult / 50) * 50

    # Clamp
    atk = max(1000, min(4000, atk))
    def_val = max(1000, min(4000, def_val))

    return atk, def_val


# ═══════════════════════════════════════════════════════════════
# CARD RENDERING
# ═══════════════════════════════════════════════════════════════

CARD_WIDTH = 52  # display columns between outer ┃ borders
ART_WIDTH = 48   # display columns between inner │ borders


def _make_stars(filled, total=8):
    """Generate star rating string."""
    return '*' * filled + '.' * (total - filled)


BAR_LEN = 20


def _stat_bar_content(label, value, value_str, bc, use_color):
    """Build stat bar inner content (without card border).

    Returns (plain_text, colored_text) where plain_text is for width
    calculation and colored_text has ANSI codes for display.
    """
    if value is not None:
        filled = max(1, round(value / 4000 * BAR_LEN))
    else:
        filled = 0
    empty = BAR_LEN - filled
    bar_plain = '█' * filled + '░' * empty
    plain = f"  {label} {bar_plain} {value_str}"
    if use_color:
        dim = '\033[90m'
        bar_colored = '█' * filled + f"{dim}{'░' * empty}{Colors.RESET}{bc}"
        colored = f"  {label} {bar_colored} {value_str}"
    else:
        colored = plain
    return plain, colored


def render_card(star, rarity, atk, def_val, resonances, lang='cn', use_color=True):
    """Render a full card as a list of lines."""
    card = CARD_DATA[star]
    style = RARITY_STYLES[rarity]
    W = CARD_WIDTH

    # Color helpers
    bc = style['border'] if use_color else ''   # border color
    nc = style['name'] if use_color else ''      # name color
    rst = Colors.RESET if use_color else ''
    blink = Colors.BLINK if use_color and style['blink'] else ''

    name = card['name_cn'] if lang == 'cn' else card['name_en']
    element = card['element'] if lang == 'cn' else card['element_en']
    desc = card['desc_cn'] if lang == 'cn' else card['desc_en']
    elem_label = f"[ {element} ]"
    rarity_tag = f"[{rarity}]"

    lines = []

    # Top border
    lines.append(f"{bc}{blink}{'':s}┏{'━' * W}┓{rst}")

    # Blank
    lines.append(f"{bc}┃{pad_to_width('', W)}┃{rst}")

    # Stars + rarity
    stars_str = _make_stars(style['stars'])
    star_line = f"  {stars_str}"
    rarity_part = f"{blink}{rarity_tag}{rst}{bc}" if use_color else rarity_tag
    # Build: "  ********                                [SSR]  "
    right_part = f"  {rarity_tag}  "
    left_content = f"  {stars_str}"
    padding = W - display_width(left_content) - display_width(right_part)
    star_content = left_content + ' ' * padding + right_part
    if use_color:
        lines.append(f"{bc}┃{nc}{pad_to_width(f'  {stars_str}', W - display_width(right_part) - 0)}{blink}{rarity_tag}{rst}{bc}  ┃{rst}")
    else:
        lines.append(f"┃{pad_to_width(star_content, W)}┃")

    # Blank
    lines.append(f"{bc}┃{pad_to_width('', W)}┃{rst}")

    # Name
    name_content = f"  {name}"
    if use_color:
        lines.append(f"{bc}┃{nc}{blink}{pad_to_width(name_content, W)}{rst}{bc}┃{rst}")
    else:
        lines.append(f"┃{pad_to_width(name_content, W)}┃")

    # Blank
    lines.append(f"{bc}┃{pad_to_width('', W)}┃{rst}")

    # Art frame top
    art_border = '─' * (W - 6)
    lines.append(f"{bc}┃  ┌{art_border}┐  ┃{rst}")

    # Art content
    for art_line in card['art']:
        padded_art = pad_to_width(art_line, W - 6)
        lines.append(f"{bc}┃  │{padded_art}│  ┃{rst}")

    # Art frame bottom
    lines.append(f"{bc}┃  └{art_border}┘  ┃{rst}")

    # Blank
    lines.append(f"{bc}┃{pad_to_width('', W)}┃{rst}")

    # Element
    elem_content = f"  {elem_label}"
    ec = ELEMENT_COLORS.get(element, '') if use_color else ''
    if use_color:
        lines.append(f"{bc}┃{ec}{pad_to_width(elem_content, W)}{rst}{bc}┃{rst}")
    else:
        lines.append(f"┃{pad_to_width(elem_content, W)}┃")

    # Blank
    lines.append(f"{bc}┃{pad_to_width('', W)}┃{rst}")

    # Description
    for d in desc:
        desc_content = f"  {d}"
        lines.append(f"{bc}┃{pad_to_width(desc_content, W)}┃{rst}")

    # Blank
    lines.append(f"{bc}┃{pad_to_width('', W)}┃{rst}")

    # Separator
    sep = '─' * (W - 4)
    lines.append(f"{bc}┃  {sep}  ┃{rst}")

    # ATK / DEF stat bars
    atk_plain, atk_colored = _stat_bar_content('ATK', atk, str(atk), bc, use_color)
    atk_pad = ' ' * max(0, W - display_width(atk_plain))
    lines.append(f"{bc}┃{atk_colored}{atk_pad}┃{rst}")

    def_plain, def_colored = _stat_bar_content('DEF', def_val, str(def_val), bc, use_color)
    def_pad = ' ' * max(0, W - display_width(def_plain))
    lines.append(f"{bc}┃{def_colored}{def_pad}┃{rst}")

    # Resonance
    res_dots = ''
    for sys_name in ['bazi', 'western', 'vedic']:
        res_dots += ('*' if sys_name in resonances else '-')
    res_str = f"  Cross-System: {res_dots}  Resonance: {rarity}"
    lines.append(f"{bc}┃{pad_to_width(res_str, W)}┃{rst}")

    # Blank
    lines.append(f"{bc}┃{pad_to_width('', W)}┃{rst}")

    # Bottom border
    lines.append(f"{bc}{blink}┗{'━' * W}┛{rst}")

    return lines


def render_preview(star, lang='cn', use_color=True):
    """Render R-level preview card with mystery art."""
    card = CARD_DATA[star]
    W = CARD_WIDTH

    dim = Colors.DIM if use_color else ''
    rst = Colors.RESET if use_color else ''
    bc = Colors.R_BORDER if use_color else ''

    name = card['name_cn'] if lang == 'cn' else card['name_en']
    element = card['element'] if lang == 'cn' else card['element_en']
    desc = card['desc_cn'] if lang == 'cn' else card['desc_en']
    elem_label = f"[ {element} ]"

    lines = []

    # Top border
    lines.append(f"{dim}{bc}┏{'━' * W}┓{rst}")

    # Blank
    lines.append(f"{dim}{bc}┃{pad_to_width('', W)}┃{rst}")

    # Stars (R = 3)
    stars_str = _make_stars(3)
    rarity_tag = "[R]"
    right_part = f"  {rarity_tag}  "
    star_content = f"  {stars_str}"
    lines.append(f"{dim}{bc}┃{pad_to_width(star_content, W - display_width(right_part))}{right_part}┃{rst}")

    # Blank
    lines.append(f"{dim}{bc}┃{pad_to_width('', W)}┃{rst}")

    # Name
    lines.append(f"{dim}{bc}┃{pad_to_width(f'  {name}', W)}┃{rst}")

    # Blank
    lines.append(f"{dim}{bc}┃{pad_to_width('', W)}┃{rst}")

    # Art frame top
    art_border = '─' * (W - 6)
    lines.append(f"{dim}{bc}┃  ┌{art_border}┐  ┃{rst}")

    # Mystery art (? pattern)
    mystery_patterns = [
        "     ? ? ?     ? ? ? ? ?     ? ? ?       ",
        "   ? ? ? ? ?     ? ? ?     ? ? ? ? ?     ",
        "     ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?       ",
        "   ? ? ?     ? ? ? ? ? ? ?     ? ? ?     ",
        "     ? ? ? ?     ? ? ?     ? ? ? ?       ",
        "       ? ? ? ? ? ? ? ? ? ? ? ? ?         ",
    ]
    # Repeat to fill art area
    for i in range(12):
        pattern = mystery_patterns[i % len(mystery_patterns)]
        lines.append(f"{dim}{bc}┃  │{pad_to_width(pattern, W - 6)}│  ┃{rst}")

    # Art frame bottom
    lines.append(f"{dim}{bc}┃  └{art_border}┘  ┃{rst}")

    # Blank
    lines.append(f"{dim}{bc}┃{pad_to_width('', W)}┃{rst}")

    # Element
    lines.append(f"{dim}{bc}┃{pad_to_width(f'  {elem_label}', W)}┃{rst}")

    # Blank
    lines.append(f"{dim}{bc}┃{pad_to_width('', W)}┃{rst}")

    # Description
    for d in desc:
        lines.append(f"{dim}{bc}┃{pad_to_width(f'  {d}', W)}┃{rst}")

    # Blank
    lines.append(f"{dim}{bc}┃{pad_to_width('', W)}┃{rst}")

    # Separator
    sep = '─' * (W - 4)
    lines.append(f"{dim}{bc}┃  {sep}  ┃{rst}")

    # ATK / DEF (hidden stat bars)
    atk_plain, atk_colored = _stat_bar_content('ATK', None, '????', bc, use_color)
    atk_pad = ' ' * max(0, W - display_width(atk_plain))
    lines.append(f"{dim}{bc}┃{atk_colored}{atk_pad}┃{rst}")

    def_plain, def_colored = _stat_bar_content('DEF', None, '????', bc, use_color)
    def_pad = ' ' * max(0, W - display_width(def_plain))
    lines.append(f"{dim}{bc}┃{def_colored}{def_pad}┃{rst}")

    # Resonance
    res_str = "  Cross-System: ---  Resonance: R"
    lines.append(f"{dim}{bc}┃{pad_to_width(res_str, W)}┃{rst}")

    # Evolution hint
    if lang == 'cn':
        hint = "  >> 完成校准后可能触发进化..."
    else:
        hint = "  >> Complete calibration to evolve..."
    lines.append(f"{dim}{bc}┃{pad_to_width(hint, W)}┃{rst}")

    # Blank
    lines.append(f"{dim}{bc}┃{pad_to_width('', W)}┃{rst}")

    # Bottom border
    lines.append(f"{dim}{bc}┗{'━' * W}┛{rst}")

    return lines


# ═══════════════════════════════════════════════════════════════
# EVOLUTION ANIMATION
# ═══════════════════════════════════════════════════════════════

def animate_evolution(star, rarity, resonances, card_lines, lang='cn', use_color=True):
    """Print evolution animation then final card."""
    bc = RARITY_STYLES[rarity]['border'] if use_color else ''
    nc = RARITY_STYLES[rarity]['name'] if use_color else ''
    rst = Colors.RESET if use_color else ''
    bold = Colors.BOLD if use_color else ''

    # Phase 1: Scanning
    if lang == 'cn':
        scan_msg = "共鸣扫描中"
    else:
        scan_msg = "Scanning resonance"

    for i in range(3):
        dots = '.' * (i + 1)
        sys.stdout.write(f"\r  {scan_msg}{dots}   ")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

    # Phase 2: Result
    n = len(resonances)
    if lang == 'cn':
        sys_names = {'bazi': '八字', 'western': '西洋占星', 'vedic': '吠陀占星'}
    else:
        sys_names = {'bazi': 'BaZi', 'western': 'Western', 'vedic': 'Vedic'}

    if n == 0:
        if lang == 'cn':
            print(f"  检测到 0/3 体系共鸣")
            time.sleep(0.3)
            print(f"  保持 R 级形态")
        else:
            print(f"  Detected 0/3 system resonance")
            time.sleep(0.3)
            print(f"  Maintaining R-level form")
    else:
        res_names = ' + '.join(sys_names.get(r, r) for r in resonances)
        if lang == 'cn':
            print(f"  {bold}{bc}检测到 {n}/3 体系共鸣!{rst}")
            time.sleep(0.3)
            print(f"  {bc}{res_names} 的能量与命宫主星产生共振!{rst}")
            time.sleep(0.5)
            print(f"  {nc}{bold}进化! R -> {rarity}!{rst}")
        else:
            print(f"  {bold}{bc}Detected {n}/3 system resonance!{rst}")
            time.sleep(0.3)
            print(f"  {bc}{res_names} energy resonates with Life Palace star!{rst}")
            time.sleep(0.5)
            print(f"  {nc}{bold}Evolution! R -> {rarity}!{rst}")

    time.sleep(0.5)
    print()

    # Phase 3: Print card
    for line in card_lines:
        print(line)


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description='Natal Chart Pet Card Generator')
    parser.add_argument('--ziwei', required=True, help='Path to ziwei.md')
    parser.add_argument('--bazi', help='Path to bazi.md')
    parser.add_argument('--western', help='Path to western-astrology.md')
    parser.add_argument('--vedic', help='Path to vedic-astrology.md')
    parser.add_argument('--lang', default='cn', choices=['cn', 'en'])
    parser.add_argument('--mode', default='full', choices=['preview', 'full'])
    parser.add_argument('--animate', default='auto', choices=['true', 'false', 'auto'])
    parser.add_argument('--no-color', action='store_true')

    args = parser.parse_args()

    use_color = not args.no_color and sys.stdout.isatty()
    do_animate = (args.animate == 'true' or
                  (args.animate == 'auto' and sys.stdout.isatty()))

    # Parse ZiWei (always needed)
    ziwei = parse_ziwei(args.ziwei)

    if not ziwei['main_star']:
        print("Error: Could not determine main star from ZiWei chart.", file=sys.stderr)
        sys.exit(1)

    star = ziwei['main_star']

    if star not in CARD_DATA:
        print(f"Error: Unknown main star '{star}'.", file=sys.stderr)
        sys.exit(1)

    # Preview mode
    if args.mode == 'preview':
        lines = render_preview(star, lang=args.lang, use_color=use_color)
        for line in lines:
            print(line)
        return

    # Full mode — need all 4 charts
    if not all([args.bazi, args.western, args.vedic]):
        print("Error: Full mode requires --bazi, --western, and --vedic.", file=sys.stderr)
        sys.exit(1)

    bazi = parse_bazi(args.bazi)
    western = parse_western(args.western)
    vedic = parse_vedic(args.vedic)

    # Calculate resonance
    resonances = check_resonance(star, bazi, western, vedic)
    rarity_map = {0: 'R', 1: 'SR', 2: 'SSR', 3: 'SSSR'}
    rarity = rarity_map[len(resonances)]

    # Calculate ATK/DEF
    atk, def_val = calculate_atk_def(star, ziwei, bazi, western, vedic, rarity)

    # Render card
    card_lines = render_card(star, rarity, atk, def_val, resonances,
                             lang=args.lang, use_color=use_color)

    # Output
    if do_animate and args.mode == 'full':
        animate_evolution(star, rarity, resonances, card_lines,
                          lang=args.lang, use_color=use_color)
    else:
        for line in card_lines:
            print(line)


if __name__ == '__main__':
    main()
