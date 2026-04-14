#!/usr/bin/env node
/**
 * 紫微斗数排盘脚本 — 基于 iztro
 */

const { astro } = require('iztro');

function parseArgs() {
  const args = {};
  const argv = process.argv.slice(2);
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i].replace(/^--/, '');
    args[key] = argv[i + 1];
  }
  return args;
}

function hourToTimeIndex(hour, minute) {
  const total = hour * 60 + (minute || 0);
  // 时辰索引: 0=子(23:00-01:00), 1=丑(01:00-03:00), ..., 12=子(23:00-01:00 晚子)
  if (total >= 1380 || total < 60) return 0;   // 子时
  if (total < 180) return 1;   // 丑时
  if (total < 300) return 2;   // 寅时
  if (total < 420) return 3;   // 卯时
  if (total < 540) return 4;   // 辰时
  if (total < 660) return 5;   // 巳时
  if (total < 780) return 6;   // 午时
  if (total < 900) return 7;   // 未时
  if (total < 1020) return 8;  // 申时
  if (total < 1140) return 9;  // 酉时
  if (total < 1260) return 10; // 戌时
  return 11; // 亥时
}

function formatStars(stars) {
  if (!stars || stars.length === 0) return '—';
  return stars.map(s => {
    let str = s.name;
    if (s.brightness) str += `(${s.brightness})`;
    if (s.mutagen) str += `[${s.mutagen}]`;
    return str;
  }).join('、');
}

function generateMarkdown(result) {
  const lines = [];

  lines.push('# 紫微斗数命盘');
  lines.push('');
  lines.push('## 基本信息');
  lines.push('');
  lines.push(`- 性别: ${result.gender === '男' ? '男' : '女'}`);
  lines.push(`- 阳历: ${result.solarDate}`);
  lines.push(`- 阴历: ${result.lunarDate}`);
  lines.push(`- 四柱: ${result.chineseDate}`);
  lines.push(`- 生肖: ${result.zodiac}`);
  lines.push(`- 星座: ${result.sign}`);
  lines.push(`- 五行局: ${result.fiveElementsClass}`);
  lines.push(`- 命宫主星: ${result.soul}`);
  lines.push(`- 身宫主星: ${result.body}`);
  lines.push('');

  // 十二宫排盘
  lines.push('## 十二宫排盘');
  lines.push('');
  lines.push('| 宫位 | 天干地支 | 主星 | 辅星 | 杂曜 |');
  lines.push('|------|----------|------|------|------|');

  for (const p of result.palaces) {
    const ganZhi = `${p.heavenlyStem}${p.earthlyBranch}`;
    const major = formatStars(p.majorStars);
    const minor = formatStars(p.minorStars);
    const adj = formatStars(p.adjectiveStars);
    lines.push(`| ${p.name} | ${ganZhi} | ${major} | ${minor} | ${adj} |`);
  }

  lines.push('');

  // 本命四化
  lines.push('## 本命四化');
  lines.push('');

  const mutagenTypes = ['禄', '权', '科', '忌'];
  for (const p of result.palaces) {
    for (const starList of [p.majorStars, p.minorStars, p.adjectiveStars]) {
      if (!starList) continue;
      for (const s of starList) {
        if (s.mutagen) {
          lines.push(`- ${s.mutagen}: ${s.name} 在 ${p.name}`);
        }
      }
    }
  }

  lines.push('');

  // 大限排列
  lines.push('## 大限排列');
  lines.push('');
  lines.push('| 宫位 | 大限范围 |');
  lines.push('|------|----------|');

  for (const p of result.palaces) {
    if (p.decadal) {
      const range = `${p.decadal.range[0]}-${p.decadal.range[1]}岁`;
      lines.push(`| ${p.name} | ${range} |`);
    }
  }

  lines.push('');

  return lines.join('\n');
}

// Main
const args = parseArgs();

if (!args.date || !args.gender) {
  console.error('Usage: node ziwei_chart.js --date YYYY-M-D --hour H [--minute M] --gender male/female/男/女');
  process.exit(1);
}

const hour = parseInt(args.hour || '0', 10);
const minute = parseInt(args.minute || '0', 10);
const timeIndex = hourToTimeIndex(hour, minute);
const gender = (args.gender === 'male' || args.gender === 'm') ? '男' : (args.gender === 'female' || args.gender === 'f') ? '女' : args.gender;

const result = astro.bySolar(args.date, timeIndex, gender, true, 'zh-CN');
console.log(generateMarkdown(result));
