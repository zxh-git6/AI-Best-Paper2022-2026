#!/usr/bin/env python3
"""Render conference notes, TRENDS is hand-written. This script renders
conference markdown files and data/papers.csv from data/papers.jsonl.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "papers.jsonl"
OUT_DIR = ROOT / "conferences"
CSV_PATH = ROOT / "data" / "papers.csv"

CONF_ORDER = ["ICLR", "NeurIPS", "ICML", "ACL", "EMNLP", "NAACL", "AAAI"]
CONF_BLURB = {
    "ICLR": "International Conference on Learning Representations。表征学习与深度学习方法。本页收 Outstanding Paper 与 Honorable Mention。",
    "NeurIPS": "Conference on Neural Information Processing Systems。机器学习理论、算法与应用，含 Datasets and Benchmarks 轨道的最佳论文。",
    "ICML": "International Conference on Machine Learning。本页收 Outstanding / Best Paper、Honorable Mention，以及官方 Outstanding Position Paper。",
    "ACL": "Annual Meeting of the Association for Computational Linguistics。收 Best / Outstanding，以及 Social Impact、Resource、Theme、Reproduction 等专项论文奖。不含 Demo、学生研讨会和分轨 SAC 奖。",
    "EMNLP": "Conference on Empirical Methods in Natural Language Processing。收录口径与 ACL 相同。2022 年官方站点已不易访问，只写入能交叉核实的奖项。",
    "NAACL": "Annual Conference of the Nations of the Americas Chapter of the ACL（2024 年前称 North American Chapter）。2023 与 2026 未办会。",
    "AAAI": "AAAI Conference on Artificial Intelligence。收 Outstanding、Distinguished、Outstanding Student，以及 Alignment / Social Impact 等轨道的最佳论文。不含 Poster、Demo 和 Student Abstract。",
}


def load():
    rows = []
    with SRC.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def authors_short(authors: str) -> str:
    if not authors:
        return "待补充"
    parts = [p.strip() for p in authors.replace(";", ",").split(",") if p.strip()]
    if len(parts) <= 4:
        return ", ".join(parts)
    return ", ".join(parts[:3]) + " 等"


def render_paper(p):
    url = p.get("url") or ""
    link = f"[论文]({url})" if url else "链接待补充"
    lines = [
        f"#### {p['title']}",
        "",
        f"- 作者：{authors_short(p.get('authors', ''))}",
        f"- 奖项：{p['award']}",
        f"- 论文：{link}",
        "",
        "| 领域 | 做了什么 | 核心洞见 | 可能为什么获奖 |",
        "| --- | --- | --- | --- |",
        f"| {p['domain']} | {p['did']} | {p['insight']} | {p['why']} |",
        "",
    ]
    return "\n".join(lines)


def render_tot(p):
    url = p.get("url") or ""
    link = f"[论文]({url})" if url else "链接待补充"
    orig = p.get("original_year") or "原发表年待补充"
    return (
        f"- **{p['title']}**（原论文 {orig}，{p['year']} 年颁发）"
        f" — {authors_short(p.get('authors', ''))}。{link}。"
        f"{p.get('why', '')}\n"
    )


def render_conference(conf, rows):
    current = [r for r in rows if not r.get("test_of_time")]
    tots = [r for r in rows if r.get("test_of_time")]
    by_year = defaultdict(list)
    for r in current:
        by_year[r["year"]].append(r)
    lines = [
        f"# {conf}",
        "",
        CONF_BLURB[conf],
        "",
        "阅读时先看每年最上面的 Best / Outstanding，再看 Honorable Mention 和专项奖。四栏笔记按摘要和官方授奖说明改写，不引用未在材料里出现的数字。",
        "",
    ]
    years = sorted(by_year)
    if conf == "NeurIPS" and 2026 not in years:
        pass
    for year in years:
        lines.append(f"## {year}")
        lines.append("")
        groups = defaultdict(list)
        for p in by_year[year]:
            groups[p["award"]].append(p)
        # stable-ish order: awards that contain Best or Outstanding first, then others as encountered
        seen = []
        for p in by_year[year]:
            if p["award"] not in seen:
                seen.append(p["award"])
        for award in seen:
            lines.append(f"### {award}")
            lines.append("")
            for p in groups[award]:
                lines.append(render_paper(p))
    if conf == "NeurIPS":
        lines += [
            "## 2026",
            "",
            "待补充。NeurIPS 2026 定于 2026 年 12 月 6–12 日在悉尼举行，截至 2026 年 11 月 25 日，官方博客只公布了 tutorial、journal track 和 reproducibility track，没有公布 Best Paper。",
            "",
        ]
    if conf == "NAACL":
        lines += [
            "## 2023",
            "",
            "该年未举办。NAACL 在 ACL 于美洲召开的年份停办；2023 年主会是 ACL（多伦多）。",
            "",
            "## 2026",
            "",
            "该年未举办。章节站点列出的下一次会议是 NAACL 2027（旧金山，6 月 1–5 日）。",
            "",
        ]
    if conf == "EMNLP":
        lines += [
            "## 关于 2022 年的 Outstanding 名单",
            "",
            "待补充。康奈尔大学新闻、短文第一作者的公开说明，以及会后综述都指向同一对奖：最佳长文 *Abstract Visual Reasoning with Tangram Shapes*，最佳短文 *Topic-Regularized Authorship Representation Learning*。EMNLP 2022 论文集前言只写获奖名单将在闭幕式公布，会后官网已不稳定。若当年另有 Outstanding Paper 名单，这里不猜测。",
            "",
        ]
    if tots:
        lines += [
            "## 附录：Test of Time / Classic Paper",
            "",
            "这些是当年大会回看大约十年前论文时颁发的时间检验奖，原论文早于 2022，不放进正文的研究地图，也不拿来论证「这一年的新趋势」。",
            "",
        ]
        for p in tots:
            lines.append(render_tot(p))
        lines.append("")
    text = "\n".join(lines).rstrip() + "\n"
    path = OUT_DIR / f"{conf}.md"
    path.write_text(text, encoding="utf-8")
    return path


def main():
    rows = load()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    by_conf = defaultdict(list)
    for r in rows:
        by_conf[r["conference"]].append(r)
    for conf in CONF_ORDER:
        render_conference(conf, by_conf.get(conf, []))
    # csv: contemporary papers first, then test of time
    fields = ["conference", "year", "award", "title", "authors", "url", "领域", "test_of_time"]
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(
                {
                    "conference": r["conference"],
                    "year": r["year"],
                    "award": r["award"],
                    "title": r["title"],
                    "authors": r.get("authors", ""),
                    "url": r.get("url", ""),
                    "领域": r.get("domain", ""),
                    "test_of_time": "yes" if r.get("test_of_time") else "no",
                }
            )
    # counts
    counts = defaultdict(int)
    for r in rows:
        if r.get("test_of_time"):
            continue
        counts[(r["conference"], r["year"])] += 1
    print("contemporary papers", sum(counts.values()))
    for conf in CONF_ORDER:
        years = sorted({y for (c, y) in counts if c == conf})
        bits = [f"{y}:{counts[(conf, y)]}" for y in years]
        print(conf, ", ".join(bits) if bits else "(none)")


if __name__ == "__main__":
    main()
