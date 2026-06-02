#!/usr/bin/env python3
"""Extract unit summaries, topics, and exam signals from actual note HTML files."""

from __future__ import annotations

import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SUBJECTS = {
    "maths": {
        "title": "Engineering Mathematics IV",
        "folder": "MATHS",
        "units": {i: f"unit{i}_solved.html" for i in range(1, 6)},
    },
    "microcontroller": {
        "title": "Microcontrollers & Embedded Systems",
        "folder": "MICROCONTROLLER",
        "units": {i: f"unit{i}_solved.html" for i in range(1, 6)},
    },
    "daa": {
        "title": "Design and Analysis of Algorithms",
        "folder": "DAA",
        "units": {i: f"unit{i}.html" for i in range(1, 6)},
    },
    "dbms": {
        "title": "Database Management Systems",
        "folder": "DBMS",
        "units": {i: f"unit{i}.html" for i in range(1, 6)},
    },
    "java": {
        "title": "Advanced Java Programming",
        "folder": "JAVA",
        "units": {
            1: "unit1.html",
            2: "unit2.html",
            3: "Unit3.html",
            4: "unit4_exam_notes.html",
            5: "unit5_exam_notes.html",
        },
    },
    "r_programming": {
        "title": "R Programming for Analytics",
        "folder": "R_PROGRAMMING",
        "units": {i: f"unit{i}.html" for i in range(1, 6)},
    },
}

PYQ_RE = re.compile(
    r"\b(PYQ|previous\s+year|every\s+paper|SEE|CIE|exam\s+pattern|question\s+bank|"
    r"most\s+repeated|high[- ]value)\b",
    re.I,
)
SQL_RE = re.compile(
    r"\b(SELECT|INSERT|UPDATE|DELETE|CREATE\s+TABLE|JOIN|GROUP\s+BY|WHERE|"
    r"NORMALIZATION|BCNF|ACID|TRANSACTION|ER\s+MODEL|RELATIONAL\s+ALGEBRA)\b",
    re.I,
)
FORMULA_RE = re.compile(r"(\$\$|\\\[|\\\(|\bO\s*\(|Master\s+Method|recurrence|theorem)", re.I)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._skip = 0
        self.headings: list[tuple[int, str]] = []
        self.toc_items: list[str] = []
        self.paragraphs: list[str] = []
        self._buf: list[str] = []
        self._in_toc = False
        self._tag_stack: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        self._tag_stack.append(tag)
        if tag in ("script", "style"):
            self._skip += 1
        if tag == "a":
            cls = dict(attrs).get("class", "")
            if "toc-item" in cls:
                self._in_toc = True
                self._buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style") and self._skip:
            self._skip -= 1
        if tag in ("h1", "h2", "h3") and self._buf and not self._skip:
            text = clean("".join(self._buf))
            if text and len(text) > 2:
                level = int(tag[1])
                self.headings.append((level, text))
            self._buf = []
        if tag == "p" and self._buf and not self._skip:
            text = clean("".join(self._buf))
            if len(text) > 40:
                self.paragraphs.append(text)
            self._buf = []
        if tag == "a":
            if self._in_toc:
                text = clean("".join(self._buf))
                if text and len(text) > 2:
                    self.toc_items.append(text)
            self._in_toc = False
            self._buf = []
        if self._tag_stack and self._tag_stack[-1] == tag:
            self._tag_stack.pop()

    def     handle_data(self, data: str) -> None:
        if self._skip:
            return
        top = self._tag_stack[-1] if self._tag_stack else ""
        if top in ("h1", "h2", "h3", "p"):
            self._buf.append(data)
        elif top == "a" and self._in_toc:
            self._buf.append(data)


EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002700-\U000027BF"
    "\U00002600-\U000026FF"
    "]+",
    flags=re.UNICODE,
)


def clean(text: str) -> str:
    text = html.unescape(text)
    text = EMOJI_RE.sub("", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^[📐📋🔷\d\.\s·]+", "", text)
    return text


def is_noise_topic(text: str) -> bool:
    low = text.lower()
    if re.match(r"^unit\s*\d+\s*notes?$", low):
        return True
    if re.search(r"^q\d+\s*[–-]\s*q\d+$", low):
        return True
    if "tutorial" in low and re.search(r"tutorial\s*[–-]?\s*\d", low):
        return True
    if len(text) > 90:
        return True
    return False


def unique_keep(items: list[str], limit: int = 12) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        key = item.lower()[:60]
        if key in seen or len(item) < 3:
            continue
        seen.add(key)
        out.append(item)
        if len(out) >= limit:
            break
    return out


def exam_importance(raw: str, pyq_hits: int, headings: list[str]) -> str:
    text = raw.lower() + " " + " ".join(h.lower() for h in headings)
    if pyq_hits >= 12 or "every paper" in text or "every single paper" in text:
        return "very-high"
    if pyq_hits >= 6 or "high-value" in text or "most repeated" in text:
        return "high"
    if pyq_hits >= 2 or "see" in text or "cie" in text:
        return "medium"
    return "low"


def study_hours(word_count: int, topic_count: int) -> str:
    hours = 1.5 + (word_count / 3500) + (topic_count * 0.12)
    hours = max(1.5, min(hours, 4.5))
    h = int(hours)
    m = int(round((hours - h) * 60))
    if m >= 45:
        h += 1
        m = 0
    elif m < 15:
        m = 0
    elif m < 45:
        m = 30
    if m:
        return f"{h}.5 Hours" if h else "0.5 Hours"
    return f"{h} Hour{'s' if h != 1 else ''}"


def build_summary(
    unit_num: int,
    title: str,
    topics: list[str],
    paragraphs: list[str],
    meta_desc: str,
    subject: str,
    raw: str,
) -> str:
    parts: list[str] = []
    if meta_desc and len(meta_desc) > 30:
        parts.append(meta_desc.rstrip("."))
    elif paragraphs:
        parts.append(paragraphs[0].rstrip("."))

    core = ", ".join(topics[:7])
    if core:
        parts.append(f"Unit {unit_num} develops competence in {core}.")

    if subject == "dbms" and SQL_RE.search(raw):
        sql_hits = unique_keep(SQL_RE.findall(raw), 8)
        if sql_hits:
            parts.append("SQL and relational design constructs emphasized include " + ", ".join(sql_hits[:6]) + ".")
    if subject == "daa" and FORMULA_RE.search(raw):
        parts.append("Includes asymptotic notation, recurrence solving, and complexity proofs aligned to SEE marking schemes.")
    elif subject == "maths":
        parts.append("Includes distribution formulas, numerical substitutions, and hypothesis-testing procedures with solved university questions.")
    elif subject == "daa":
        parts.append("Focuses on algorithm design paradigms, asymptotic analysis, and step-by-step tracing for exam proofs.")
    elif subject == "java":
        parts.append("Covers core Java APIs, OOP constructs, and servlet/JSP patterns commonly tested in MSRIT papers.")
    elif subject == "r_programming":
        parts.append("Builds practical R fluency with vectors, data frames, tidy manipulation, and visualization pipelines.")
    elif subject == "microcontroller":
        parts.append("Maps ARM Cortex-M0 peripherals, bus protocols, and embedded C patterns to MSRIT viva and SEE questions.")
    text = " ".join(parts)
    words = text.split()
    if len(words) > 120:
        text = " ".join(words[:120]).rstrip(",;.") + "."
    elif len(words) < 50 and len(paragraphs) > 1:
        extra = paragraphs[1]
        text = (text + " " + extra) if extra not in text else text
        words = text.split()
        if len(words) > 120:
            text = " ".join(words[:120]).rstrip(",;.") + "."

    if not text.endswith("."):
        text += "."
    return text


def learning_outcomes(topics: list[str], subject: str) -> list[str]:
    verbs = {
        "dbms": ("Design", "Write", "Evaluate"),
        "daa": ("Analyze", "Derive", "Implement"),
        "java": ("Explain", "Build", "Debug"),
        "r_programming": ("Load", "Transform", "Visualize"),
        "microcontroller": ("Configure", "Interface", "Troubleshoot"),
        "maths": ("Compute", "Prove", "Apply"),
    }
    v = verbs.get(subject, ("Understand", "Apply", "Solve"))
    outs: list[str] = []
    for i, topic in enumerate(topics[:3]):
        short = topic if len(topic) <= 42 else topic[:39] + "…"
        outs.append(f"{v[i]} {short.lower() if i else short}")
    if len(outs) < 3:
        outs.append("Answer previous-year and CIE-style questions confidently")
    return outs[:3]


def extract_topics_regex(raw: str) -> list[str]:
    found: list[str] = []
    patterns = [
        r'<a[^>]*class="[^"]*nav-link[^"]*"[^>]*>([^<]+)</a>',
        r'<a[^>]*class="[^"]*toc-item[^"]*"[^>]*>.*?<span[^>]*>[^<]*</span>\s*([^<]+)</a>',
        r'<h2[^>]*>([^<]+)</h2>',
        r'class="[^"]*section-title[^"]*"[^>]*>.*?<span[^>]*>[^<]*</span>\s*([^<]+)</div>',
        r'class="[^"]*topic-header[^"]*"[^>]*>.*?<h2>([^<]+)</h2>',
    ]
    for pat in patterns:
        for m in re.finditer(pat, raw, re.I | re.S):
            t = clean(m.group(1))
            if t and not is_noise_topic(t):
                found.append(t)
    return found


def parse_unit_file(path: Path, unit_num: int, subject: str) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    meta_m = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', raw, re.I)
    meta_desc = clean(html.unescape(meta_m.group(1))) if meta_m else ""

    parser = TextExtractor()
    parser.feed(raw)

    hero_h1 = re.search(
        r'<header[^>]*class="[^"]*hero[^"]*"[^>]*>.*?<h1[^>]*>([^<]+)</h1>',
        raw,
        re.I | re.S,
    )
    main_h1 = re.search(r'<h1[^>]*>([^<]+)</h1>', raw, re.I)
    h2s = [clean(t) for _, t in parser.headings if _ == 2]
    h3s = [clean(t) for _, t in parser.headings if _ == 3]

    topics = unique_keep(
        [t for t in extract_topics_regex(raw) + parser.toc_items + h2s + h3s if not is_noise_topic(t)],
        10,
    )
    if not topics:
        topics = unique_keep([t for t in h2s + h3s if not is_noise_topic(t)], 8)

    if hero_h1:
        title = clean(hero_h1.group(1))
    elif main_h1:
        title = clean(main_h1.group(1))
    else:
        tm = re.search(r"<title>([^<]+)</title>", raw, re.I)
        title = clean(tm.group(1)) if tm else f"Unit {unit_num}"
    title = re.sub(r"^Unit\s*\d+\s*[—:\-]\s*", "", title, flags=re.I).strip()

    pyq_hits = len(PYQ_RE.findall(raw))
    importance = exam_importance(raw, pyq_hits, topics)
    word_count = len(re.sub(r"<[^>]+>", " ", raw).split())

    summary = build_summary(
        unit_num, title, topics, parser.paragraphs[:4], meta_desc, subject, raw
    )

    return {
        "number": unit_num,
        "title": title,
        "topics": topics[:8],
        "keyTopics": topics[:6],
        "summary": summary,
        "outcomes": learning_outcomes(topics, subject),
        "studyTime": study_hours(word_count, len(topics)),
        "examImportance": importance,
    }


def main() -> None:
    catalog: dict = {"subjects": {}}
    for sid, cfg in SUBJECTS.items():
        folder = ROOT / cfg["folder"]
        units = []
        for num, fname in sorted(cfg["units"].items()):
            path = folder / fname
            if not path.exists():
                print(f"WARN missing {path}")
                continue
            units.append(parse_unit_file(path, num, sid))
        catalog["subjects"][sid] = {
            "id": sid,
            "title": cfg["title"],
            "units": units,
        }

    out = ROOT / "assets" / "data" / "unit-metadata.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out} ({len(catalog['subjects'])} subjects)")


if __name__ == "__main__":
    main()
