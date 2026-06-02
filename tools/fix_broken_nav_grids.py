#!/usr/bin/env python3
"""Repair portal-nav-grid HTML broken by partial unit-card removal."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BOOKS = [
    "DBMS_4th_Sem_Notes_Book.html",
    "DAA_4th_Sem_Notes_Book.html",
    "Java_4th_Sem_Notes_Book.html",
    "Microcontrollers_4th_Sem_Notes_Book.html",
    "R_Programming_4th_Sem_Notes_Book.html",
]

ORPHAN_DESC = re.compile(
    r"</div>\s*<div class=\"syllabus-desc\">[^<]*</div>\s*",
    re.IGNORECASE,
)

BROKEN_GRID_CHUNK = re.compile(
    r"(<div class=\"portal-nav-grid\"[^>]*>)\s*"
    r"(?:<div class=\"syllabus-desc\">[^<]*</div>\s*</div>\s*)+",
    re.IGNORECASE | re.DOTALL,
)

EXTRA_CLOSING = re.compile(
    r"(portal-hub-card\"[^>]*>.*?</div>\s*)</div>\s*(</div>\s*</div>)",
    re.DOTALL,
)

DUP_SCRIPTS = re.compile(
    r"(<script src=\"assets/js/portal-core\.js\" defer></script>\s*"
    r"<script src=\"assets/js/notes-enhancements\.js\" defer></script>\s*"
    r"<script src=\"assets/js/book-navigation\.js\" defer></script>\s*)+",
    re.IGNORECASE,
)


def fix_html(html: str) -> str:
    while ORPHAN_DESC.search(html):
        html = ORPHAN_DESC.sub("", html)

    html = BROKEN_GRID_CHUNK.sub(r"\1\n", html)

    # Remove stray closing div after last hub card inside grid
    html = re.sub(
        r"(portal-hub-card\"[^>]*>[\s\S]*?</div>\s*)\n\s*</div>\s*\n(\s*</div>\s*\n\s*</div>)",
        r"\1\n                \2",
        html,
        count=0,
    )

    # Deduplicate script includes (keep one block + unit-preview once)
    if html.count("portal-core.js") > 1:
        seen = False

        def dedupe_scripts(m: re.Match) -> str:
            nonlocal seen
            if seen:
                return ""
            seen = True
            block = m.group(0)
            if "unit-preview.js" not in block:
                block += '  <script src="assets/js/unit-preview.js" defer></script>\n'
            return block

        html = DUP_SCRIPTS.sub(dedupe_scripts, html)
        # Remove any extra unit-preview lines beyond first
        parts = html.split('<script src="assets/js/unit-preview.js" defer></script>')
        if len(parts) > 2:
            html = parts[0] + '<script src="assets/js/unit-preview.js" defer></script>'.join(
                [parts[0], "".join(parts[1:])]
            )
        if len(parts) > 2:
            html = (
                parts[0]
                + '<script src="assets/js/unit-preview.js" defer></script>'
                + "".join(parts[2:])
            )

    # Simpler dedupe: remove duplicate consecutive script lines
    lines = html.splitlines()
    out: list[str] = []
    script_counts: dict[str, int] = {}
    for line in lines:
        if 'src="assets/js/' in line and line.strip().startswith("<script"):
            key = line.strip()
            script_counts[key] = script_counts.get(key, 0) + 1
            if script_counts[key] > 1:
                continue
        out.append(line)
    html = "\n".join(out)

    return html


def main() -> None:
    for name in BOOKS:
        path = ROOT / name
        if not path.exists():
            continue
        original = path.read_text(encoding="utf-8")
        fixed = fix_html(original)
        if fixed != original:
            path.write_text(fixed, encoding="utf-8")
            print(f"Fixed {name}")
        else:
            print(f"OK {name}")


if __name__ == "__main__":
    main()
