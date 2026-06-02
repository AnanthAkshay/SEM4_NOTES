#!/usr/bin/env python3
"""Inject DBMS mobile CSS/JS across notes book, units, lab book, and lab pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CSS_LINK = '  <link rel="stylesheet" href="../assets/css/dbms-mobile.css">\n'
CSS_LINK_BOOK = '  <link rel="stylesheet" href="assets/css/dbms-mobile.css">\n'
JS_LINK = '  <script src="../assets/js/dbms-unit-mobile.js" defer></script>\n'
VIEWPORT = '  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n'
LAB_CSS = '  <link rel="stylesheet" href="../assets/css/dbms-mobile.css">\n'


def inject_after_maths_mobile(text: str, extra: str) -> str:
    needle = "maths-mobile.css"
    if extra.strip() in text:
        return text
    idx = text.find(needle)
    if idx == -1:
        return text
    line_end = text.find("\n", idx)
    return text[: line_end + 1] + extra + text[line_end + 1 :]


def patch_units():
    for p in sorted((ROOT / "DBMS").glob("unit*.html")):
        text = p.read_text(encoding="utf-8")
        text = inject_after_maths_mobile(text, CSS_LINK)
        if "dbms-unit-mobile.js" not in text:
            text = text.replace(
                '  <script src="../assets/js/notes-enhancements.js" defer></script>\n',
                JS_LINK + '  <script src="../assets/js/notes-enhancements.js" defer></script>\n',
            )
        p.write_text(text, encoding="utf-8")
        print("unit", p.name)


def patch_lab_pages():
    for p in sorted((ROOT / "DBMS_LAB").glob("*.html")):
        text = p.read_text(encoding="utf-8")
        if "viewport" not in text:
            text = text.replace("<head>\n", "<head>\n" + VIEWPORT, 1)
            text = text.replace("<head>\r\n", "<head>\r\n" + VIEWPORT, 1)
        if "dbms-mobile.css" not in text:
            if "portal.css" in text:
                text = text.replace(
                    '  <link rel="stylesheet" href="../assets/css/portal.css">\n',
                    '  <link rel="stylesheet" href="../assets/css/portal.css">\n' + LAB_CSS,
                )
            else:
                text = text.replace("</head>", LAB_CSS + "</head>", 1)
        p.write_text(text, encoding="utf-8")
        print("lab", p.name)


def patch_book(path: Path, home_keys: str):
    text = path.read_text(encoding="utf-8")
    rel = "assets/css/dbms-mobile.css"
    if rel not in text:
        text = inject_after_maths_mobile(text, CSS_LINK_BOOK)
    if 'data-subject-id="dbms"' not in text and "portal-book" in text:
        text = text.replace(
            '<body class="portal-enhanced portal-book"',
            '<body class="portal-enhanced portal-book" data-subject-id="dbms"',
            1,
        )
    if "portalHomeKeys" not in text:
        text = text.replace(
            "  <script src=\"assets/js/portal-back-nav.js\"></script>\n",
            f"  <script>window.portalHomeKeys = {home_keys};</script>\n"
            "  <script src=\"assets/js/portal-back-nav.js\"></script>\n",
        )
    text = text.replace(
        'class="pdf-iframe" id="unit',
        'class="pdf-iframe dbms-notes-iframe" id="unit',
    )
    # Unit tab short labels
    replacements = [
        (
            "Exam Study Notes\n                        </button>",
            '<span class="tab-full">Exam Study Notes</span><span class="tab-short">Notes</span>\n                        </button>',
        ),
        (
            "Class PPT Slides\n                        </button>",
            '<span class="tab-full">Class PPT Slides</span><span class="tab-short">PPT</span>\n                        </button>',
        ),
        (
            "Relational Algebra Slides\n                        </button>",
            '<span class="tab-full">Relational Algebra Slides</span><span class="tab-short">RA PPT</span>\n                        </button>',
        ),
    ]
    for old, new in replacements:
        if "tab-full" not in text or old in text:
            text = text.replace(old, new)
    # PYQ tabs
    pyq_map = [
        ("SEE 2025", "SEE 25"),
        ("SEE 2024", "SEE 24"),
        ("SEE 2023", "SEE 23"),
        ("Makeup 2023", "Mk 23"),
        ("CIE-1 2024", "C1 24"),
        ("CIE-2 2024", "C2 24"),
        ("CIE-2 2025", "C2 25"),
    ]
    for full, short in pyq_map:
        old = f'onclick="switchPYQ(\'">{full}</button>'
        # fix pattern - actual buttons use ids
        pass
    for full, short in pyq_map:
        old = f">{full}</button>"
        new = f'><span class="tab-full">{full}</span><span class="tab-short">{short}</span></button>'
        if f'tab-short">{short}' not in text:
            text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")
    print("book", path.name)


def main():
    patch_units()
    patch_lab_pages()
    patch_book(ROOT / "DBMS_4th_Sem_Notes_Book.html", "['home']")
    lab = ROOT / "DBMS_Lab_Book.html"
    text = lab.read_text(encoding="utf-8")
    if "dbms-mobile.css" not in text:
        text = inject_after_maths_mobile(text, CSS_LINK_BOOK)
    if 'data-subject-id="dbms-lab"' not in text:
        text = text.replace(
            '<body class="portal-enhanced portal-book"',
            '<body class="portal-enhanced portal-book" data-subject-id="dbms-lab"',
            1,
        )
    lab.write_text(text, encoding="utf-8")
    print("book", lab.name)


if __name__ == "__main__":
    main()
