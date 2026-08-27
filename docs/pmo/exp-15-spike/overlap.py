#!/usr/bin/env python3
"""EXP-15 信号 ② 计数器：按 method.md 预注册的归一化规则算证据源重叠率。

用法：overlap.py <urls.json>
  urls.json = {"视角名": ["url", ...], ...}
输出：逐对重叠率 + 最大值（最保守口径）+ 是否达标（≤50%）。
"""
import json
import re
import sys
from itertools import combinations


def normalize(url):
    u = re.sub(r"^https?://", "", url.strip())
    u = re.sub(r"^www\.", "", u)
    u = u.split("?")[0].split("#")[0].rstrip("/")
    # arXiv 同一论文的 abs / html / pdf / ar5iv 视为同一源
    m = re.search(r"arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})", u) or re.search(
        r"ar5iv\.[\w.]*/html/(\d{4}\.\d{4,5})", u
    )
    if m:
        return f"arxiv:{m.group(1)}"
    return u


def main():
    sets = {k: {normalize(u) for u in v} for k, v in json.load(open(sys.argv[1])).items()}
    rates = []
    for (a, sa), (b, sb) in combinations(sets.items(), 2):
        shared = sa & sb
        rate = len(shared) / min(len(sa), len(sb)) if sa and sb else 0.0
        rates.append(rate)
        print(f"{a} × {b}: {len(shared)}/{min(len(sa), len(sb))} = {rate:.0%}"
              + (f"  共享={sorted(shared)}" if shared else ""))
    worst = max(rates) if rates else 0.0
    print(f"\n最大重叠率 = {worst:.0%} → 信号 ② {'达标' if worst <= 0.5 else '未达标'}（阈值 ≤50%）")


if __name__ == "__main__":
    main()
