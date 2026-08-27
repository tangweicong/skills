#!/usr/bin/env python3
"""ORD-48 引用真实性核验：对两臂产出里的引用做 ID 反查 + 存活检查。

ORD-48 强制范围 = 带 arXiv ID / DOI 的引用 → 反查标题（权威 API）。
补充（超出 ORD-48 范围，仅作参考）= 其余 URL 的 HTTP 存活。

防误杀（ORD-48 条款 d，本次实跑加强）：
1. 单条失败须重试后才判失败；
2. **整体失败率异常高（>50%）先判定为客户端/环境故障**，换客户端复核后再下结论——
   本文件初版用 urllib，34/35 条系统性失败，实为 HTTPS 客户端不通而非引用伪造。
   现改用 curl（该环境实测可用）。
"""
import json
import re
import subprocess
import sys
import time

UA = "ORD-48-citation-check"


def curl(url, tries=3, wait=3, head=False):
    args = ["curl", "-sSL", "-A", UA, "--max-time", "25"]
    args += ["-o", "/dev/null", "-w", "%{http_code}", "-I"] if head else []
    for i in range(tries):
        r = subprocess.run(args + [url], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout
        if i < tries - 1:
            time.sleep(wait)
    return None


def check_doi(doi):
    body = curl(f"https://api.crossref.org/works/{doi}")
    msg = json.loads(body)["message"]
    title = (msg.get("title") or ["<无标题>"])[0]
    return " ".join(title.split()), msg.get("issued", {}).get("date-parts", [[None]])[0][0]


def check_arxiv(aid):
    body = curl(f"https://export.arxiv.org/api/query?id_list={aid}")
    m = re.search(r"<entry>(.*?)</entry>", body, re.S)
    if not m:
        raise LookupError("no entry")
    t = re.search(r"<title>(.*?)</title>", m.group(1), re.S)
    p = re.search(r"<published>(.*?)</published>", m.group(1), re.S)
    return " ".join(t.group(1).split()), (p.group(1)[:4] if p else "?")


def main():
    spec = json.load(open(sys.argv[1]))
    print("=" * 8, "ORD-48 强制范围：ID ↔ 标题 反查", "=" * 8)
    fails = 0
    for kind, ident, claimed in spec["id_cited"]:
        try:
            title, year = check_doi(ident) if kind == "doi" else check_arxiv(ident)
            hit = any(w.lower() in title.lower() for w in claimed.split() if len(w) > 3)
            print(f"[{'OK' if hit else '??'}] {kind}:{ident}  {year}  {title[:75]}")
            if not hit:
                print(f"       引用处所述关键词=「{claimed}」→ 需人工确认是否同一文献")
        except Exception as e:  # noqa: BLE001
            fails += 1
            print(f"[FAIL] {kind}:{ident}  重试后仍失败 → {type(e).__name__}")
        time.sleep(1)

    total = len(spec["id_cited"])
    if fails > total / 2:
        print(f"\n⚠ 失败 {fails}/{total} > 50% → 按防误杀条款判定为**客户端/环境故障**，不得据此判引用伪造")

    print()
    print("=" * 8, "补充（超出 ORD-48 范围）：其余 URL 存活", "=" * 8)
    bad = []
    for url in spec["other_urls"]:
        st = (curl(url, head=True) or "ERR").strip()
        if st not in ("200", "301", "302", "303", "307", "308", "403", "405", "999"):
            bad.append((url, st))
        print(f"[{st}] {url[:92]}")
    print(f"\n非存活（403/405/999 视为反爬非失效）: {len(bad)}/{len(spec['other_urls'])}")
    for u, s in bad:
        print(f"  {s}  {u}")


if __name__ == "__main__":
    main()
