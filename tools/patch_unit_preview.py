#!/usr/bin/env python3
"""Inject unit preview dashboard into all six subject books."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BOOKS = {
    "Engineering_Mathematics_4th_Sem_Notes_Book.html": {
        "subject_id": "maths",
        "home_keys": "['cover']",
        "maths_mode": True,
    },
    "Microcontrollers_4th_Sem_Notes_Book.html": {
        "subject_id": "microcontroller",
        "home_keys": "['home']",
    },
    "DAA_4th_Sem_Notes_Book.html": {
        "subject_id": "daa",
        "home_keys": "['home']",
    },
    "DBMS_4th_Sem_Notes_Book.html": {
        "subject_id": "dbms",
        "home_keys": "['home']",
    },
    "Java_4th_Sem_Notes_Book.html": {
        "subject_id": "java",
        "home_keys": "['home']",
    },
    "R_Programming_4th_Sem_Notes_Book.html": {
        "subject_id": "r_programming",
        "home_keys": "['home']",
    },
}

UNIT_CARD_RE = re.compile(
    r'\s*<div class="syllabus-item unit-nav-card"(?! portal-hub-card)[^>]*onclick="showSection\(\'unit\d\'\)"[^>]*>.*?</div>\s*',
    re.DOTALL | re.IGNORECASE,
)

UNIT_ROW_RE = re.compile(
    r'\s*<tr class="unit-row"[^>]*onclick="showUnit\(\'unit\d\'\)"[^>]*>.*?</tr>\s*',
    re.DOTALL | re.IGNORECASE,
)

DASHBOARD = """
                <div id="unit-preview-dashboard" class="unit-preview-dashboard" aria-live="polite"></div>
"""

PREVIEW_CSS = '  <link rel="stylesheet" href="assets/css/unit-preview.css">\n'
PREVIEW_JS = '  <script src="assets/js/unit-preview.js" defer></script>\n'

SCRIPTS_BLOCK = """  <script src="assets/js/portal-core.js" defer></script>
  <script src="assets/js/notes-enhancements.js" defer></script>
  <script src="assets/js/book-navigation.js" defer></script>
  <script src="assets/js/unit-preview.js" defer></script>
"""


def ensure_css(html: str) -> str:
    if "unit-preview.css" in html:
        return html
    if 'href="assets/css/portal.css"' in html:
        return html.replace(
            'href="assets/css/portal.css">',
            'href="assets/css/portal.css">\n' + PREVIEW_CSS.strip() + "\n",
            1,
        )
    if "</head>" in html:
        return html.replace("</head>", PREVIEW_CSS + "</head>", 1)
    return html


def ensure_subject_id(html: str, sid: str) -> str:
    if "data-subject-id=" in html:
        html = re.sub(
            r'data-subject-id="[^"]*"',
            f'data-subject-id="{sid}"',
            html,
            count=1,
        )
        return html
    html = html.replace(
        "<body",
        f'<body class="portal-enhanced portal-book" data-subject-id="{sid}" data-portal-base=""',
        1,
    )
    if 'class="portal-enhanced portal-book"' not in html and "portal-book" not in html:
        pass
    return html


def ensure_portal_body_class(html: str) -> str:
    if "portal-book" in html:
        return html
    html = re.sub(
        r"<body([^>]*)>",
        lambda m: (
            "<body"
            + m.group(1)
            + (' class="portal-enhanced portal-book"' if "class=" not in m.group(1) else "")
            + ">"
        ),
        html,
        count=1,
    )
    return html


def patch_nav_grid(html: str) -> str:
    if 'id="unit-preview-dashboard"' in html:
        html = UNIT_CARD_RE.sub("", html)
        return html

    def replacer(match: re.Match) -> str:
        block = match.group(0)
        if 'id="unit-preview-dashboard"' in block:
            return block
        return DASHBOARD + block

    # Insert dashboard at start of first portal-nav-grid
    html = re.sub(
        r'(<div class="portal-nav-grid"[^>]*>)',
        DASHBOARD + r"\1",
        html,
        count=1,
    )
    html = UNIT_CARD_RE.sub("", html)
    return html


def patch_maths(html: str) -> str:
    if 'id="unit-preview-dashboard"' not in html:
        html = re.sub(
            r"(<div class=\"card\">\s*<div class=\"card-header\">\s*<h3 class=\"card-title\">)",
            DASHBOARD + r"\1",
            html,
            count=1,
        )
    html = UNIT_ROW_RE.sub("", html)
    # Keep exams hub row — re-add if removed all rows; check pyq row
    if 'showUnit(\'pyq\')' not in html:
        pyq_row = """
                            <tr class="unit-row" role="button" tabindex="0" onclick="showUnit('pyq')" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();showUnit('pyq');}">
                                <td><strong>Exams Hub</strong> · Tap to open</td>
                                <td data-label="Topics">Scanned Question Bank and CIE/SEE Past Papers (2024–2025)</td>
                                <td data-label="PDFs"><code>Sem 4 Question Bank.pdf</code> + 5 papers</td>
                                <td data-label="Priority"><span class="tag-status critical">Essential</span></td>
                            </tr>
"""
        html = html.replace("</tbody>", pyq_row + "\n                        </tbody>", 1)

    for n in range(1, 6):
        anchor = f'<span id="unit-{n}" class="portal-unit-anchor" aria-hidden="true"></span>\n        '
        section_pat = f'<section id="unit{n}" class="unit-section">'
        if section_pat in html and f'id="unit-{n}"' not in html:
            html = html.replace(section_pat, anchor + section_pat, 1)

    html = ensure_subject_id(html, "maths")
    if "portalHomeKeys" not in html:
        html = html.replace(
            "</body>",
            "  <script>window.portalHomeKeys = ['cover'];</script>\n</body>",
            1,
        )
    return html


def ensure_scripts(html: str) -> str:
    if "unit-preview.js" in html:
        return html
    if "</body>" in html:
        return html.replace("</body>", SCRIPTS_BLOCK + "\n</body>", 1)
    return html


def update_card_helper_text(html: str) -> str:
    html = html.replace(
        "Tap any card to open notes or exam papers.",
        "Review unit summaries below, then tap Open Unit on any card.",
    )
    html = html.replace(
        "Tap any card to open.",
        "Review unit summaries below, then tap Open Unit.",
    )
    html = html.replace(
        "Tap a unit row to open lecture notes, solutions, and PDFs.",
        "Use the unit preview cards above, then tap Open Unit to load notes and PDFs.",
    )
    html = html.replace(
        "Tap any unit in the table below to open notes and PDFs.",
        "Use the unit preview cards below—tap Open Unit to load notes and PDFs.",
    )
    return html


def patch_file(name: str, cfg: dict) -> None:
    path = ROOT / name
    if not path.exists():
        print(f"SKIP missing {name}")
        return
    html = path.read_text(encoding="utf-8")
    original = html

    html = ensure_css(html)
    html = ensure_portal_body_class(html)
    html = ensure_subject_id(html, cfg["subject_id"])

    if cfg.get("maths_mode"):
        html = patch_maths(html)
    else:
        html = patch_nav_grid(html)

    html = update_card_helper_text(html)
    html = ensure_scripts(html)

    if "portalHomeKeys" not in html and not cfg.get("maths_mode"):
        html = html.replace(
            "</body>",
            f"  <script>window.portalHomeKeys = {cfg['home_keys']};</script>\n</body>",
            1,
        )

    if html != original:
        path.write_text(html, encoding="utf-8")
        print(f"Patched {name}")
    else:
        print(f"No changes {name}")


def main() -> None:
    for name, cfg in BOOKS.items():
        patch_file(name, cfg)


if __name__ == "__main__":
    main()
