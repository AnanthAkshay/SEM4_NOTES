# -*- coding: utf-8 -*-
"""Merge DBMS_LAB/1.html .. 12.html into DBMS_Lab_Book.html."""
import os
import re
from pathlib import Path

ROOT = Path(r"a:\SEM4_Complete")
LAB = ROOT / "DBMS_LAB"
OUT = ROOT / "DBMS_Lab_Book.html"
CSS_FILE = ROOT / "css_block.txt"

EXP_TITLES = {
    1: "Employee – Department – Project",
    2: "Part – Supplier – Supply",
    3: "Boat – Sailor – Reserves",
    4: "Customer – Branch – Account – Transaction",
    5: "Books – Student – Borrows",
    6: "Patient – Doctor – Appointment",
    7: "MongoDB Employee & Department",
    8: "MongoDB Patient & Doctor",
    9: "MongoDB Part–Supplier + PL/SQL Backup",
    10: "MongoDB Boat–Sailor + Weekend Trigger",
    11: "MongoDB Customer–Branch + Cursor",
    12: "MongoDB Books–Student + Exception",
}


def extract_container(html: str) -> str:
    m = re.search(
        r'<div\s+class=["\']container["\']\s*>(.*?)</div>\s*</body>',
        html,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if m:
        return m.group(1).strip()
    m = re.search(r"<body[^>]*>(.*?)</body>", html, flags=re.DOTALL | re.IGNORECASE)
    if m:
        body = m.group(1).strip()
        body = re.sub(r"^<div\s+class=[^>]+>\s*", "", body, flags=re.I)
        body = re.sub(r"\s*</div>\s*$", "", body)
        return body.strip()
    return html.strip()


def fix_asset_paths(content: str) -> str:
    content = re.sub(
        r'src=(["\'])image(\d+)\.png\1',
        r'src=\1./DBMS_LAB/image\2.png\1',
        content,
        flags=re.IGNORECASE,
    )
    content = re.sub(
        r'src=(["\'])exp(\d+)\.png\1',
        r'src=\1./DBMS_LAB/exp\2.png\1',
        content,
        flags=re.IGNORECASE,
    )
    content = re.sub(
        r'src=(["\'])er_exp(\d+)\.png\1',
        r'src=\1./DBMS_LAB/er_exp\2.png\1',
        content,
        flags=re.IGNORECASE,
    )
    return content


def load_experiment(num: int) -> str:
    path = LAB / f"{num}.html"
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}")
    html = path.read_text(encoding="utf-8")
    content = extract_container(html)
    return fix_asset_paths(content)


def build():
    base_css = CSS_FILE.read_text(encoding="utf-8") if CSS_FILE.exists() else ""

    exp_content_css = """
        /* User experiment pages (from 1.html–12.html) */
        .exp-panel {
            background: #ffffff;
            color: #1e293b;
            padding: 32px 36px;
            border-radius: 12px;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.35);
            line-height: 1.65;
            font-family: Arial, Helvetica, sans-serif;
        }
        .exp-panel h1, .exp-panel h2, .exp-panel h3 { color: #003366; }
        .exp-panel h1 { font-size: 1.5rem; margin-bottom: 0.25rem; }
        .exp-panel h2 { font-size: 1.2rem; margin-top: 1.5rem; margin-bottom: 0.5rem; }
        .exp-panel h3 { font-size: 1.05rem; margin-top: 1rem; }
        .exp-panel p { margin: 0.6rem 0; }
        .exp-panel ul, .exp-panel ol { margin: 0.6rem 0 0.6rem 1.5rem; }
        .exp-panel table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 0.9rem;
        }
        .exp-panel table, .exp-panel th, .exp-panel td {
            border: 1px solid #334155;
        }
        .exp-panel th {
            background: #003366;
            color: #fff;
            padding: 10px;
            text-align: left;
        }
        .exp-panel td { padding: 8px 10px; }
        .exp-panel pre {
            background: #f4f4f4;
            color: #0f172a;
            padding: 15px;
            border-left: 5px solid #003366;
            overflow: auto;
            border-radius: 0 6px 6px 0;
            font-size: 0.85rem;
            line-height: 1.5;
        }
        .exp-panel img {
            max-width: 100%;
            height: auto;
        }
        .lab-section { display: none; }
        .lab-section.active { display: block; }
        .main-content {
            margin-left: var(--sidebar-width);
            flex: 1;
            padding: 28px 40px 60px;
            max-width: 1100px;
        }
        @media print {
            .sidebar { display: none !important; }
            .main-content { margin-left: 0 !important; max-width: 100%; padding: 0; }
            .lab-section { display: block !important; page-break-after: always; }
            .exp-panel { box-shadow: none; }
        }
    """

    nav_items = []
    sections = []

    for n in range(1, 13):
        content = load_experiment(n)
        exp_id = f"experiment-{n}"
        label = f"Experiment {n}: {EXP_TITLES[n]}"
        nav_items.append(
            f'            <li class="nav-item" data-exp="{n}" onclick="showExp(\'{exp_id}\', this)">{label}</li>\n'
        )
        sections.append(
            f"""        <div id="{exp_id}" class="lab-section">
            <div class="exp-panel">
{content}
            </div>
        </div>
"""
        )

    nav_html = "".join(nav_items)
    sections_html = "".join(sections)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DBMS Laboratory Manual | ISL47 — All 12 Experiments</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    {base_css}
    <style>{exp_content_css}</style>
</head>
<body>
    <div class="sidebar">
        <div class="sidebar-brand">
            <div class="sidebar-logo">DB</div>
            <div class="brand-meta">
                <h1>DBMS Lab</h1>
                <p>ISL47 · Experiments 1–12</p>
            </div>
        </div>
        <ul class="nav-menu">
            <li class="nav-item active" data-exp="0" onclick="showExp('cover', this)">Cover / Home</li>
{nav_html}        </ul>
    </div>

    <div class="main-content">
        <div id="cover" class="lab-section active">
            <div class="exp-panel">
                <h1 align="center">DATABASE MANAGEMENT SYSTEMS LABORATORY</h1>
                <h2 align="center">Course Code: ISL47</h2>
                <p style="text-align:center;margin-top:24px;">
                    Complete manual — <strong>Experiments 1 to 12</strong><br>
                    Select an experiment from the sidebar.
                </p>
                <table style="margin-top:32px;">
                    <tr><th>#</th><th>Title</th></tr>
"""
    for n in range(1, 13):
        html += f"                    <tr><td>{n}</td><td>{EXP_TITLES[n]}</td></tr>\n"

    html += f"""                </table>
                <p style="margin-top:24px;font-size:0.9rem;color:#64748b;">
                    Source: merged from <code>DBMS_LAB/1.html</code> … <code>12.html</code>
                </p>
            </div>
        </div>
{sections_html}    </div>

    <script>
        function showExp(id, el) {{
            document.querySelectorAll('.lab-section').forEach(s => s.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
            const section = document.getElementById(id);
            if (section) section.classList.add('active');
            if (el) el.classList.add('active');
            window.scrollTo(0, 0);
        }}
        // Open experiment from URL hash e.g. #experiment-3
        (function() {{
            const hash = location.hash.replace('#', '');
            if (hash && document.getElementById(hash)) {{
                const item = document.querySelector('.nav-item[data-exp="' + hash.replace('experiment-','') + '"]');
                showExp(hash, item);
            }}
        }})();
    </script>
</body>
</html>
"""

    OUT.write_text(html, encoding="utf-8")
    print(f"Merged 12 experiments -> {OUT}")
    print(f"Size: {OUT.stat().st_size // 1024} KB")


if __name__ == "__main__":
    build()
