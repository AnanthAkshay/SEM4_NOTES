# -*- coding: utf-8 -*-
"""Build polished DBMS Lab Manual HTML with diagram images."""
import os
import re

BASE_DIR = r"a:\SEM4_Complete\DBMS_LAB"
OUT_FILE = r"a:\SEM4_Complete\DBMS_Lab_Book.html"
CSS_FILE = r"a:\SEM4_Complete\css_block.txt"


def parse_markdown(md: str, folder: str) -> str:
    html = md
    img_base = f"./DBMS_LAB/{folder}"

    # Horizontal rules
    html = re.sub(r"^---\s*$", '<hr class="section-divider">', html, flags=re.MULTILINE)

    # Images ![alt](file)
    def replace_img(m):
        alt, src = m.group(1), m.group(2)
        if not src.startswith("http"):
            src = f"{img_base}/{src}"
        return (
            f'<figure class="diagram-figure">'
            f'<img src="{src}" alt="{alt}" class="diagram-img" loading="lazy">'
            f'<figcaption>{alt}</figcaption></figure>'
        )

    html = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_img, html)

    # Tables
    def replace_table(match):
        lines = match.group(0).strip().split("\n")
        if len(lines) < 2:
            return match.group(0)
        headers = [c.strip() for c in lines[0].split("|")[1:-1]]
        out = '<div class="table-wrap"><table class="data-table"><thead><tr>'
        for h in headers:
            out += f"<th>{h}</th>"
        out += "</tr></thead><tbody>"
        for line in lines[2:]:
            cells = [c.strip() for c in line.split("|")[1:-1]]
            out += "<tr>"
            for c in cells:
                out += f"<td>{c}</td>"
            out += "</tr>"
        out += "</tbody></table></div>"
        return out

    html = re.sub(
        r"(\|[^\n]+\|\n)(\|[-:| ]+\|\n)((\|[^\n]+\|\n)+)",
        replace_table,
        html,
    )

    # Code blocks
    def replace_code(match):
        lang = (match.group(1) or "code").lower()
        code = match.group(2).replace("<", "&lt;").replace(">", "&gt;")
        label = {"sql": "Oracle SQL", "javascript": "MongoDB", "text": "Output"}.get(lang, lang.upper())
        return (
            f'<div class="code-block"><div class="code-lang">{label}</div>'
            f'<pre><code>{code}</code></pre></div>'
        )

    html = re.sub(r"```(\w*)\n(.*?)```", replace_code, html, flags=re.DOTALL)

    # Mermaid – keep as pre for reference (figure PNG is primary)
    html = re.sub(
        r'<div class="code-block"><div class="code-lang">MERMAID</div><pre><code>(.*?)</code></pre></div>',
        r'<details class="mermaid-src"><summary>Mermaid source (reference)</summary><pre><code>\1</code></pre></details>',
        html,
        flags=re.DOTALL,
    )

    html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"`([^`]+)`", r'<code class="inline-code">\1</code>', html)

    # Headers
    html = re.sub(
        r"^#### (.*?)$",
        r'<h4 class="sub-subsection">\1</h4>',
        html,
        flags=re.MULTILINE,
    )
    html = re.sub(
        r"^### (.*?)$",
        r'<h3 class="subsection">\1</h3>',
        html,
        flags=re.MULTILINE,
    )
    html = re.sub(
        r"^## (.*?)$",
        r'<h2 class="section-title">\1</h2>',
        html,
        flags=re.MULTILINE,
    )
    html = re.sub(
        r"^# (.*?)$",
        lambda m: f'<header class="exp-header"><span class="exp-badge">ISL47</span><h1>{m.group(1)}</h1></header>',
        html,
        count=1,
        flags=re.MULTILINE,
    )

    # Lists
    html = re.sub(r"^(\d+)\. (.*?)$", r'<li class="ol-item">\2</li>', html, flags=re.MULTILINE)
    html = re.sub(r"^\* (.*?)$", r'<li class="ul-item">\1</li>', html, flags=re.MULTILINE)

    # Italic captions
    html = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", html)

    # Paragraphs: lines not tagged
    lines = html.split("\n")
    out = []
    buf = []
    block_tags = ("<h", "<div", "<table", "<hr", "<header", "<figure", "<details", "<li", "<pre")

    def flush_buf():
        if buf:
            text = " ".join(buf).strip()
            if text:
                out.append(f'<p class="body-text">{text}</p>')
            buf.clear()

    for line in lines:
        s = line.strip()
        if not s:
            flush_buf()
            out.append("")
            continue
        if s.startswith(block_tags):
            flush_buf()
            out.append(line)
        else:
            buf.append(s)
    flush_buf()
    html = "\n".join(out)

    return html


def build():
    with open(CSS_FILE, "r", encoding="utf-8") as f:
        base_css = f.read()

    extra_css = """
        :root {
            --dbms-primary: #2563eb;
            --dbms-accent: #0d9488;
        }
        .sidebar-logo { background: linear-gradient(135deg, #2563eb, #0d9488) !important; }
        .exp-header {
            margin-bottom: 28px;
            padding-bottom: 20px;
            border-bottom: 2px solid var(--border-color);
        }
        .exp-header h1 { font-family: var(--font-display); color: #f8fafc; font-size: 1.75rem; margin-top: 8px; }
        .exp-badge {
            display: inline-block;
            background: linear-gradient(135deg, #2563eb, #0d9488);
            color: white;
            font-size: 0.7rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            letter-spacing: 0.05em;
        }
        .section-title {
            font-family: var(--font-display);
            color: #f8fafc;
            font-size: 1.35rem;
            margin: 36px 0 16px;
            padding-left: 12px;
            border-left: 4px solid var(--dbms-primary);
        }
        .subsection { color: #e2e8f0; font-size: 1.05rem; margin: 24px 0 12px; }
        .sub-subsection { color: #94a3b8; font-size: 0.95rem; margin: 16px 0 8px; }
        .body-text { margin: 10px 0; line-height: 1.75; color: var(--text-secondary); }
        .section-divider { border: 0; height: 1px; background: linear-gradient(90deg, transparent, var(--border-color), transparent); margin: 32px 0; }
        .diagram-figure {
            margin: 24px 0;
            text-align: center;
            background: #fff;
            border-radius: 12px;
            padding: 16px;
            border: 1px solid var(--border-color);
            box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        }
        .diagram-img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }
        .diagram-figure figcaption {
            margin-top: 12px;
            font-size: 0.85rem;
            color: var(--text-muted);
            font-style: italic;
        }
        .table-wrap { overflow-x: auto; margin: 16px 0; border-radius: 10px; border: 1px solid var(--border-color); }
        .data-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
        .data-table th { background: rgba(37,99,235,0.2); color: #f8fafc; padding: 12px; text-align: left; border-bottom: 2px solid var(--border-color); }
        .data-table td { padding: 10px 12px; border-bottom: 1px solid var(--border-color); }
        .data-table tr:hover td { background: rgba(255,255,255,0.03); }
        .code-block {
            margin: 16px 0;
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background: #0a0f1a;
        }
        .code-lang {
            background: #1e293b;
            padding: 8px 14px;
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--dbms-accent);
            letter-spacing: 0.04em;
        }
        .code-block pre {
            margin: 0;
            padding: 16px;
            overflow-x: auto;
            font-family: var(--font-mono);
            font-size: 0.82rem;
            line-height: 1.5;
            color: #e2e8f0;
        }
        .inline-code {
            background: rgba(37,99,235,0.15);
            color: #93c5fd;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: var(--font-mono);
            font-size: 0.88em;
        }
        .mermaid-src { margin: 12px 0; padding: 12px; background: rgba(0,0,0,0.2); border-radius: 8px; }
        .mermaid-src summary { cursor: pointer; color: var(--text-muted); font-size: 0.85rem; }
        .card { padding: 28px 32px; }
        @media print {
            .sidebar { display: none; }
            .main-content { margin-left: 0 !important; max-width: 100%; }
            .diagram-figure { break-inside: avoid; box-shadow: none; }
            body { background: white; color: black; }
            .section-title { color: #111; border-left-color: #2563eb; }
            .body-text { color: #333; }
        }
    """

    experiments = []

    def get_exp_num(name):
        m = re.search(r"Experiment_(\d+)", name)
        return int(m.group(1)) if m else 999

    for folder in sorted(os.listdir(BASE_DIR), key=get_exp_num):
        if not folder.startswith("Experiment_"):
            continue
        exp_path = os.path.join(BASE_DIR, folder)
        mds = [f for f in os.listdir(exp_path) if f.endswith(".md")]
        if not mds:
            continue
        with open(os.path.join(exp_path, mds[0]), "r", encoding="utf-8") as f:
            md = f.read()
        num = get_exp_num(folder)
        title_match = re.search(r"## TITLE\s*\n+(.+?)\n", md)
        title = title_match.group(1).strip() if title_match else f"Experiment {num}"
        experiments.append(
            {
                "id": folder,
                "num": num,
                "title": f"Exp {num}: {title[:40]}",
                "html": parse_markdown(md, folder),
            }
        )

    nav = "".join(
        f'            <li class="nav-item" onclick="showExp(\'{e["id"]}\')">{e["title"]}</li>\n'
        for e in experiments
    )
    sections = "".join(
        f'        <div id="{e["id"]}" class="lab-section">\n            <article class="card exp-card">{e["html"]}</article>\n        </div>\n'
        for e in experiments
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DBMS Laboratory Manual | ISL47</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=Inter:wght@400;500;600&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    {base_css}
    <style>{extra_css}</style>
</head>
<body>
    <div class="sidebar">
        <div class="sidebar-brand">
            <div class="sidebar-logo">DB</div>
            <div class="brand-meta">
                <h1>DBMS Lab</h1>
                <p>ISL47 · 12 Experiments</p>
            </div>
        </div>
        <ul class="nav-menu">
{nav}        </ul>
        <p style="margin-top:auto;font-size:0.75rem;color:var(--text-muted);padding:12px;">
            ER &amp; Schema diagrams included as figures. Use Print (Ctrl+P) for record book.
        </p>
    </div>
    <div class="main-content">
        <div id="cover" class="lab-section active">
            <article class="card exp-card">
                <header class="exp-header">
                    <span class="exp-badge">ISL47</span>
                    <h1>Database Management Systems Laboratory Manual</h1>
                </header>
                <p class="body-text"><strong>Course:</strong> DBMS Lab · Credits 0:0:1 · Coordinator: Dr. Savita K. Shetty</p>
                <p class="body-text">Select an experiment from the sidebar. Each includes <strong>ER Diagram</strong> and <strong>Schema Diagram</strong> figures (PNG) for record submission.</p>
                <figure class="diagram-figure">
                    <img src="./DBMS_LAB/Experiment_1_Employee_Department_Project/er_diagram.png" alt="Sample ER" class="diagram-img">
                    <figcaption>Sample: Experiment 1 ER Diagram</figcaption>
                </figure>
            </article>
        </div>
{sections}    </div>
    <script>
        function showExp(id) {{
            document.querySelectorAll('.lab-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            const el = document.getElementById(id);
            if (el) el.classList.add('active');
            if (event && event.target) event.target.classList.add('active');
            window.scrollTo(0, 0);
        }}
    </script>
</body>
</html>
"""
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built {OUT_FILE} with {len(experiments)} experiments")


if __name__ == "__main__":
    build()
