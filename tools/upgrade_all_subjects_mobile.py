#!/usr/bin/env python3
"""Apply mobile-friendly portal navigation (no sidebar) to all subject books and unit pages."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MOBILE_LINK = '  <link rel="stylesheet" href="assets/css/maths-mobile.css">\n'
MOBILE_LINK_REL = '  <link rel="stylesheet" href="../assets/css/maths-mobile.css">\n'
BACK_NAV_SCRIPT = '  <script src="assets/js/portal-back-nav.js"></script>\n'
BACK_NAV_SCRIPT_REL = '  <script src="../assets/js/portal-back-nav.js"></script>\n'
VIEWPORT = '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n'

MOBILE_HEADER = """    <header class="mobile-header portal-mobile-header">
        <div style="display:flex;align-items:center;gap:10px;">
            <div class="sidebar-logo" style="width:32px;height:32px;font-size:1rem;border-radius:8px;">{logo}</div>
            <h1 style="font-family:var(--font-display,Inter,sans-serif);font-size:1rem;font-weight:800;color:var(--text-primary,#f8fafc);line-height:1.1;">{title}</h1>
        </div>
        <button type="button" class="btn-back-cover" id="mobile-back-btn" hidden onclick="portalGoHome()">
            <svg viewBox="0 0 24 24" width="18" height="18"><path d="M19 12H5M12 19l-7-7 7-7" fill="none" stroke="currentColor" stroke-width="2"/></svg>
            Overview
        </button>
    </header>
"""

BACK_BAR = """
        <div class="unit-nav-bar" id="unit-nav-bar" hidden>
            <button type="button" class="btn-back-cover" onclick="portalGoHome()">
                <svg viewBox="0 0 24 24" width="18" height="18"><path d="M19 12H5M12 19l-7-7 7-7" fill="none" stroke="currentColor" stroke-width="2"/></svg>
                Back to Course Overview
            </button>
        </div>
"""

UNIT_CARD_ATTRS = (
    ' class="syllabus-item unit-nav-card" role="button" tabindex="0" '
    'onclick="showSection(\'unit{n}\')" '
    'onkeydown="portalCardKey(event,\'unit{n}\')"'
)

HUB_PYQ = """                    <div class="syllabus-item unit-nav-card portal-hub-card" role="button" tabindex="0" onclick="showSection('pyqs')" onkeydown="portalCardKey(event,'pyqs')">
                        <div class="syllabus-title">CIE / SEE Papers Hub</div>
                        <div class="syllabus-desc">Previous year exam papers — tap to open and switch between papers.</div>
                    </div>
"""

HUB_LAB = """                    <div class="syllabus-item unit-nav-card portal-hub-card" role="button" tabindex="0" onclick="showSection('lab')" onkeydown="portalCardKey(event,'lab')">
                        <div class="syllabus-title">Interactive Lab Hub</div>
                        <div class="syllabus-desc">Lab manual PDF and experiment walkthroughs.</div>
                    </div>
"""

HUB_NUMERICAL = """                    <div class="syllabus-item unit-nav-card portal-hub-card" role="button" tabindex="0" onclick="showSection('numerical')" onkeydown="portalCardKey(event,'numerical')">
                        <div class="syllabus-title">Weekly Numerical Tests</div>
                        <div class="syllabus-desc">Solved numerical practice problems.</div>
                    </div>
"""

R_HOME_SECTION = """
        <div class="unit-section active" id="sec-home">
            <div class="cover-intro">
                <h1>R Programming for Analytics</h1>
                <p>Tap a unit below to open solved notes, or open the exam preparation hub.</p>
                <div class="stats-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:16px;margin-top:24px;">
                    <div class="stat-card" style="padding:16px;border:1px solid var(--border-color);border-radius:12px;text-align:center;"><div style="font-weight:800;color:var(--primary);">5 Units</div><div style="font-size:0.8rem;color:var(--text-muted);">Study Notes</div></div>
                    <div class="stat-card" style="padding:16px;border:1px solid var(--border-color);border-radius:12px;text-align:center;"><div style="font-weight:800;color:var(--accent-rose);">Prep Hub</div><div style="font-size:0.8rem;color:var(--text-muted);">MCQs & Viva</div></div>
                </div>
            </div>
            <div class="card">
                <div class="card-header"><h3 class="card-title">Course Units</h3>
                    <p style="font-size:0.85rem;color:var(--text-muted);margin-top:6px;">Tap any card to open.</p>
                </div>
                <div class="portal-nav-grid">
                    <div class="syllabus-item unit-nav-card" role="button" tabindex="0" onclick="showSection('unit1')" onkeydown="portalCardKey(event,'unit1')"><div class="syllabus-title">Unit 1: Basics &amp; Setup</div><div class="syllabus-desc">R ecosystem, types, and exploration commands.</div></div>
                    <div class="syllabus-item unit-nav-card" role="button" tabindex="0" onclick="showSection('unit2')" onkeydown="portalCardKey(event,'unit2')"><div class="syllabus-title">Unit 2: Loading Data</div><div class="syllabus-desc">Vectors, factors, matrices, and data structures.</div></div>
                    <div class="syllabus-item unit-nav-card" role="button" tabindex="0" onclick="showSection('unit3')" onkeydown="portalCardKey(event,'unit3')"><div class="syllabus-title">Unit 3: I/O &amp; Aggregations</div><div class="syllabus-desc">apply, tapply, and data handling.</div></div>
                    <div class="syllabus-item unit-nav-card" role="button" tabindex="0" onclick="showSection('unit4')" onkeydown="portalCardKey(event,'unit4')"><div class="syllabus-title">Unit 4: Data Frames &amp; EDA</div><div class="syllabus-desc">dplyr-style workflows and exploration.</div></div>
                    <div class="syllabus-item unit-nav-card" role="button" tabindex="0" onclick="showSection('unit5')" onkeydown="portalCardKey(event,'unit5')"><div class="syllabus-title">Unit 5: ggplot2 &amp; Visuals</div><div class="syllabus-desc">Grammar of graphics and plotting.</div></div>
                    <div class="syllabus-item unit-nav-card portal-hub-card" role="button" tabindex="0" onclick="showSection('prep')" onkeydown="portalCardKey(event,'prep')"><div class="syllabus-title">Exam Preparation Hub</div><div class="syllabus-desc">MCQs, viva questions, and revision sheet.</div></div>
                </div>
            </div>
        </div>
"""


def ensure_viewport(html: str) -> str:
    if "viewport-fit=cover" in html:
        return html
    if 'name="viewport"' in html:
        return re.sub(
            r'<meta name="viewport" content="[^"]*">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">',
            html,
            count=1,
        )
    return html.replace("<head>", "<head>\n" + VIEWPORT, 1)


def ensure_book_assets(html: str) -> str:
    if "maths-mobile.css" not in html:
        html = html.replace(
            '<link rel="stylesheet" href="assets/css/portal.css">',
            '<link rel="stylesheet" href="assets/css/portal.css">\n' + MOBILE_LINK,
        )
    if "portal-back-nav.js" not in html:
        html = html.replace("</body>", BACK_NAV_SCRIPT + "</body>")
    return html


def ensure_unit_assets(html: str) -> str:
    html = ensure_viewport(html)
    if "portal-enhanced" not in html and "portal-book" not in html:
        return html
    if "maths-mobile.css" not in html:
        marker = '<link rel="stylesheet" href="../assets/css/portal.css">'
        if marker in html:
            html = html.replace(marker, marker + "\n" + MOBILE_LINK_REL)
        else:
            html = html.replace("</head>", MOBILE_LINK_REL + "</head>", 1)
    return html


def inject_mobile_chrome(html: str, logo: str, title: str) -> str:
    if "portal-mobile-header" not in html:
        html = re.sub(
            r"<body([^>]*)>",
            lambda m: f"<body{m.group(1)}>\n" + MOBILE_HEADER.format(logo=logo, title=title),
            html,
            count=1,
        )
    if 'id="unit-nav-bar"' not in html:
        html = re.sub(
            r'(<(?:div|main) class="main-content"[^>]*>\s*)',
            r"\1" + BACK_BAR,
            html,
            count=1,
        )
    return html


def make_unit_cards(html: str, max_unit: int = 5) -> str:
    for n in range(1, max_unit + 1):
        attrs = UNIT_CARD_ATTRS.format(n=n)
        html = re.sub(
            rf'<div class="syllabus-item">\s*\n\s*<div class="syllabus-title">Unit {n}:',
            f"<div{attrs}>\n                        <div class=\"syllabus-title\">Unit {n}:",
            html,
            count=1,
            flags=re.IGNORECASE,
        )
    return html


def add_hub_cards(html: str, hubs: list[str]) -> str:
    grid_marker = 'class="portal-nav-grid"'
    if grid_marker in html:
        return html
    insert = ""
    if "pyqs" in hubs and "onclick=\"showSection('pyqs')\"" not in html:
        insert += HUB_PYQ
    if "lab" in hubs and "onclick=\"showSection('lab')\"" not in html:
        insert += HUB_LAB
    if "numerical" in hubs and "onclick=\"showSection('numerical')\"" not in html:
        insert += HUB_NUMERICAL
    if not insert:
        return html
    html = re.sub(
        r'(<div style="display:grid; grid-template-columns: repeat\(auto-fit, minmax\(300px, 1fr\)\); gap: 20px;">)',
        r'<div class="portal-nav-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">\n' + insert,
        html,
        count=1,
    )
    return html


def patch_show_section(html: str) -> str:
    if "updatePortalBackBar" in html:
        return html

    # showSection variant
    html = re.sub(
        r"(function showSection\(sectionId\)\s*\{[\s\S]*?)"
        r"(document\.getElementById\('sidebar'\)\.classList\.remove\('open'\);|"
        r"document\.querySelector\('\.sidebar'\)\.classList\.remove\('open'\);|"
        r"if \(window\.innerWidth <= 992\) document\.querySelector\('\.sidebar'\)\.classList\.remove\('open'\);)\s*",
        r"\1",
        html,
        count=1,
    )
    html = re.sub(
        r"(function showSection\(sectionId\)\s*\{[\s\S]*?)(window\.scrollTo\(\{top: 0, behavior: 'smooth'\}\);|window\.scrollTo\(0, 0\);)",
        r"\1if (typeof updatePortalBackBar === 'function') updatePortalBackBar(sectionId); else \2",
        html,
        count=1,
    )
    if "updatePortalBackBar(sectionId)" not in html:
        html = re.sub(
            r"(function showSection\(sectionId\)\s*\{[\s\S]*?document\.getElementById\('btn-' \+ sectionId\)\.classList\.add\('active'\);)\s*",
            r"\1\n            if (typeof updatePortalBackBar === 'function') updatePortalBackBar(sectionId);\n            ",
            html,
            count=1,
        )
    return html


def patch_show_exp(html: str) -> str:
    if "updatePortalBackBar" in html:
        return html
    html = re.sub(
        r"(function showExp\(id, el\)\s*\{[\s\S]*?)(window\.scrollTo\(0, 0\);)",
        r"\1if (typeof updatePortalBackBar === 'function') updatePortalBackBar(id); else \2",
        html,
        count=1,
    )
    return html


def patch_dbms_lab_cover(html: str) -> str:
    if "lab-exp-table" in html:
        return html
    old = 'Select an experiment from the sidebar.'
    new = 'Tap an experiment row below to open.'
    html = html.replace(old, new)
    cover_marker = '<div id="cover" class="lab-section active">'
    idx = html.find(cover_marker)
    if idx == -1:
        return html
    end = html.find("</table>", idx)
    if end == -1:
        return html
    chunk = html[idx : end + len("</table>")]
    new_chunk = chunk.replace(
        '<table style="margin-top:32px;">',
        '<table class="lab-exp-table course-table" style="margin-top:32px;">',
    )

    def row_repl(m):
        n = m.group(1)
        if int(n) > 12:
            return m.group(0)
        exp_id = f"experiment-{n}"
        title = m.group(2)
        return (
            f'<tr class="unit-row" role="button" tabindex="0" '
            f"onclick=\"showExp('{exp_id}', null)\" "
            f"onkeydown=\"portalCardKey(event,'{exp_id}','showExp')\"><td><strong>Exp {n}</strong></td>"
            f"<td data-label=\"Title\">{title}</td></tr>"
        )

    new_chunk = re.sub(r"<tr><td>(\d+)</td><td>([^<]+)</td></tr>", row_repl, new_chunk)
    return html[:idx] + new_chunk + html[end + len("</table>") :]


def upgrade_notes_book(path: Path, logo: str, title: str, hubs: list[str]) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    text = ensure_viewport(text)
    text = ensure_book_assets(text)
    text = inject_mobile_chrome(text, logo, title)
    if "sec-home" in text or "id=\"cover\"" in text:
        text = make_unit_cards(text)
        text = add_hub_cards(text, hubs)
    text = patch_show_section(text)
    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def upgrade_r_book(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = ensure_viewport(text)
    text = ensure_book_assets(text)
    text = inject_mobile_chrome(text, "R", "R Analytics Portal")
    if "sec-home" not in text:
        text = text.replace(
            '    <main class="main-content">\n\n        <!-- UNIT 1 -->',
            '    <main class="main-content">\n' + R_HOME_SECTION + "\n        <!-- UNIT 1 -->",
        )
        text = text.replace(
            '<div class="unit-section active" id="sec-unit1">',
            '<div class="unit-section" id="sec-unit1">',
        )
    if 'id="unit-nav-bar"' not in text:
        text = re.sub(r"(<main class=\"main-content\">\s*)", r"\1" + BACK_BAR, text, count=1)
    text = patch_show_section(text)
    if "portalHomeKeys" not in text:
        text = text.replace(
            "function showSection(sectionId)",
            "window.portalHomeKeys = ['home'];\n        function showSection(sectionId)",
            1,
        )
    path.write_text(text, encoding="utf-8")


def upgrade_lab_book(path: Path, logo: str, title: str, is_dbms: bool) -> None:
    text = path.read_text(encoding="utf-8")
    text = ensure_viewport(text)
    text = ensure_book_assets(text)
    text = inject_mobile_chrome(text, logo, title)
    if 'id="unit-nav-bar"' not in text:
        text = re.sub(
            r'(<div class="main-content"[^>]*>\s*)',
            BACK_BAR,
            text,
            count=1,
        )
    if is_dbms:
        text = patch_dbms_lab_cover(text)
    text = patch_show_exp(text)
    if "portalHomeKeys" not in text:
        text = text.replace(
            "<script>",
            "<script>\n        window.portalHomeKeys = ['cover'];\n",
            1,
        )
    path.write_text(text, encoding="utf-8")


def upgrade_java_lab(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = ensure_viewport(text)
    text = ensure_book_assets(text)
    text = inject_mobile_chrome(text, "☕", "Java Advanced Lab")
    if 'id="unit-nav-bar"' not in text:
        text = re.sub(r"(<main class=\"main-content\">\s*)", r"\1" + BACK_BAR, text, count=1)
    if "onclick=\"showSection('ex1')\"" not in text:
        ex_cards = ""
        items = [
            ("eclipse", "Eclipse Run Guide", "IDE setup and run workflow"),
            ("ex1", "Ex 1: Complex Arithmetic", "Real and Imaginary multiplication"),
            ("ex2", "Ex 2: Bank Constraints", "Minimum balance validations"),
            ("ex3", "Ex 3: Payroll System", "OOP package layout"),
            ("ex4", "Ex 4: Queue & Exceptions", "Custom exception queue"),
            ("ex5", "Ex 5: Strings Package", "String operations"),
            ("ex6", "Ex 6: Palindrome StringBuffer", "Case-insensitive check"),
            ("ex7", "Ex 7: Password Security", "Password rules"),
            ("ex8", "Ex 8: Telephone Recorder", "Missed calls simulator"),
            ("ex9", "Ex 9: Books Collection DB", "Sorted book list"),
            ("ex10", "Ex 10: Generic Stack Class", "Type-safe stack"),
            ("ex11", "Ex 11: Student Info Swing", "Swing dialog UI"),
            ("ex12", "Ex 12: Customer Purchases", "Billing terminal"),
        ]
        for sid, title, desc in items:
            ex_cards += (
                f'                    <div class="syllabus-item unit-nav-card" role="button" tabindex="0" '
                f"onclick=\"showSection('{sid}')\" onkeydown=\"portalCardKey(event,'{sid}')\"><div class=\"syllabus-title\">{title}</div>"
                f'<div class="syllabus-desc">{desc}</div></div>\n'
            )
        text = text.replace(
            '<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">',
            '<div class="portal-nav-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">\n' + ex_cards,
            1,
        )
        text = re.sub(
            r'<div style="background-color:rgba\(255,255,255,0\.02\);[\s\S]*?</div>\s*</div>\s*</div>\s*</div>\s*\n\s*<!-- ======================= ECLIPSE',
            "\n            </div>\n        </div>\n\n        <!-- ======================= ECLIPSE",
            text,
            count=1,
        )
    text = patch_show_section(text)
    if "portalHomeKeys" not in text:
        text = text.replace(
            "function showSection(sectionId)",
            "window.portalHomeKeys = ['home'];\n        function showSection(sectionId)",
            1,
        )
    path.write_text(text, encoding="utf-8")


def upgrade_daa_lab(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = ensure_viewport(text)
    text = ensure_book_assets(text)
    text = inject_mobile_chrome(text, "D", "DAA Lab")
    if 'id="daa-lab-cover"' not in text:
        cards = ""
        exps = [
            ("Experiment_1_MergeSort", "Experiment 1: Merge Sort"),
            ("Experiment_2_RandomizedQuickSort", "Experiment 2: Randomized Quick Sort"),
            ("Experiment_3_PriorityQueue", "Experiment 3: Priority Queue"),
            ("Experiment_4_CountingSort", "Experiment 4: Counting Sort"),
            ("Experiment_5_MedianOfMedians", "Experiment 5: Median of Medians"),
            ("Experiment_6_DisjointSetUnion", "Experiment 6: Disjoint Set Union"),
            ("Experiment_7_Dijkstra", "Experiment 7: Dijkstra"),
            ("Experiment_8_MatrixChainMultiplication", "Experiment 8: Matrix Chain"),
            ("Experiment_9_LongestCommonSubsequence", "Experiment 9: LCS"),
            ("Experiment_10_HuffmanCoding", "Experiment 10: Huffman Coding"),
            ("Experiment_11_DepthFirstSearch", "Experiment 11: DFS"),
            ("Experiment_12_FordFulkersonMaxFlow", "Experiment 12: Max Flow"),
        ]
        for eid, label in exps:
            cards += (
                f'                    <div class="syllabus-item unit-nav-card" role="button" tabindex="0" '
                f"onclick=\"showExp('{eid}')\" onkeydown=\"portalCardKey(event,'{eid}','showExp')\"><div class=\"syllabus-title\">{label}</div></div>\n"
            )
        cover = f"""
        <div id="daa-lab-cover" class="lab-section active">
            <div class="card" style="padding:24px;">
                <h1 style="margin-bottom:12px;">DAA Laboratory Manual</h1>
                <p style="margin-bottom:20px;color:#94a3b8;">Tap an experiment to open solutions.</p>
                <div class="portal-nav-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;">
{cards}                </div>
            </div>
        </div>
"""
        text = text.replace(
            '<div class="main-content">\n        <div id="Experiment_1_MergeSort"',
            '<div class="main-content">\n' + BACK_BAR + cover + '        <div id="Experiment_1_MergeSort"',
            1,
        )
    text = re.sub(
        r"function showExp\(id\)\s*\{[\s\S]*?window\.scrollTo\(0, 0\);\s*\}",
        """function showExp(id, el) {
            document.querySelectorAll('.lab-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            const section = document.getElementById(id);
            if (section) section.classList.add('active');
            if (el) el.classList.add('active');
            if (typeof updatePortalBackBar === 'function') updatePortalBackBar(id);
            else window.scrollTo(0, 0);
        }""",
        text,
        count=1,
    )
    text = re.sub(
        r"\s*if \(document\.querySelector\('\.nav-item'\)\) \{\s*document\.querySelector\('\.nav-item'\)\.click\(\);\s*\}",
        "",
        text,
    )
    if "portalHomeKeys" not in text:
        text = text.replace("<script>", "<script>\n        window.portalHomeKeys = ['daa-lab-cover'];\n", 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    books = [
        (ROOT / "DBMS_4th_Sem_Notes_Book.html", "DB", "Database Systems", ["pyqs"]),
        (ROOT / "Java_4th_Sem_Notes_Book.html", "JV", "Advanced Java", ["pyqs"]),
        (ROOT / "DAA_4th_Sem_Notes_Book.html", "DA", "DAA Premium", ["pyqs", "numerical"]),
        (ROOT / "Microcontrollers_4th_Sem_Notes_Book.html", "MC", "Microcontrollers", ["pyqs", "lab"]),
    ]
    for path, logo, title, hubs in books:
        if path.exists():
            upgrade_notes_book(path, logo, title, hubs)
            print(f"Updated {path.name}")

    r_path = ROOT / "R_Programming_4th_Sem_Notes_Book.html"
    if r_path.exists():
        upgrade_r_book(r_path)
        print(f"Updated {r_path.name}")

    upgrade_lab_book(ROOT / "DBMS_Lab_Book.html", "DB", "DBMS Lab", True)
    print("Updated DBMS_Lab_Book.html")

    upgrade_daa_lab(ROOT / "DAA_Lab_Book.html")
    print("Updated DAA_Lab_Book.html")

    upgrade_java_lab(ROOT / "Java_Advanced_Lab_Book.html")
    print("Updated Java_Advanced_Lab_Book.html")

    unit_dirs = ["DBMS", "JAVA", "DAA", "R_PROGRAMMING", "MICROCONTROLLER"]
    count = 0
    for d in unit_dirs:
        folder = ROOT / d
        if not folder.is_dir():
            continue
        for html in folder.glob("*.html"):
            text = html.read_text(encoding="utf-8")
            new = ensure_unit_assets(text)
            if new != text:
                html.write_text(new, encoding="utf-8")
                count += 1
    print(f"Updated {count} unit HTML files")


if __name__ == "__main__":
    main()
