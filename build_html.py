import os
import re

def parse_markdown(md):
    html = md
    
    # HR
    html = re.sub(r'^---\s*$', '<hr class="section-divider">', html, flags=re.MULTILINE)
    
    # Tables
    def replace_table(match):
        table_text = match.group(0)
        lines = table_text.strip().split('\n')
        if len(lines) < 2: return table_text
        
        headers = lines[0].split('|')[1:-1]
        out = '<div class="card"><div class="table-container" style="overflow-x:auto;"><table><thead><tr>'
        for h in headers:
            out += f'<th style="padding:12px; border:1px solid #1e293b; text-align:left; background:rgba(255,255,255,0.05); color:#f8fafc;">{h.strip()}</th>'
        out += '</tr></thead><tbody>'
        
        for line in lines[2:]:
            cells = line.split('|')[1:-1]
            out += '<tr>'
            for c in cells:
                out += f'<td style="padding:12px; border:1px solid #1e293b; text-align:left;">{c.strip()}</td>'
            out += '</tr>'
            
        out += '</tbody></table></div></div>'
        return out
        
    html = re.sub(r'(\|.*?\|.*?\n)(\|[-| ]+\|\n)((\|.*?\|.*?\n)*)', replace_table, html + '\n')
    
    # Code blocks
    def replace_code(match):
        lang = match.group(1)
        code = match.group(2).replace('<', '&lt;').replace('>', '&gt;')
        return f'<div class="code-container"><div class="code-tabs"><div class="code-tab active">{lang.upper()}</div></div><div class="code-content active"><pre class="language-{lang}">{code}</pre></div></div>'
        
    html = re.sub(r'```(\w*)\n(.*?)```', replace_code, html, flags=re.DOTALL)
    
    # Bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    
    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code class="inline-code">\1</code>', html)
    
    # Headers
    html = re.sub(r'^### (.*?)$', r'<div class="card-title" style="margin-top:30px; margin-bottom:15px;">\1</div>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2 style="font-family:\'Outfit\',sans-serif; color:#f8fafc; font-size:1.8rem; margin-top:40px; margin-bottom:20px;">\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<div class="hero-card"><div class="hero-card-tag">DAA Lab Manual</div><h2>\1</h2><p>Design and Analysis of Algorithms Laboratory Solutions.</p></div>', html, flags=re.MULTILINE)
    
    # Wrap standard paragraphs in basic divs to avoid floating text issues if needed
    
    return html

def build_html():
    base_dir = r'a:\SEM4_Complete\DAA_LAB'
    experiments = []
    
    # Read the premium CSS
    with open('css_block.txt', 'r', encoding='utf-8') as f:
        premium_css = f.read()
    
    if os.path.exists(base_dir):
        def get_exp_num(folder_name):
            match = re.search(r'Experiment_(\d+)', folder_name)
            return int(match.group(1)) if match else 999
            
        for folder in sorted(os.listdir(base_dir), key=get_exp_num):
            if folder.startswith('Experiment_'):
                exp_path = os.path.join(base_dir, folder)
                if os.path.isdir(exp_path):
                    md_files = [f for f in os.listdir(exp_path) if f.endswith('.md')]
                    if md_files:
                        md_path = os.path.join(exp_path, md_files[0])
                        with open(md_path, 'r', encoding='utf-8') as f:
                            md_content = f.read()
                        
                        png_files = [f for f in os.listdir(exp_path) if f.endswith('.png')]
                        img_path = ''
                        if png_files:
                            img_path = f'./DAA_LAB/{folder}/{png_files[0]}'
                            
                        experiments.append({
                            'id': folder,
                            'title': md_files[0].replace('.md', '').replace('_', ' '),
                            'html': parse_markdown(md_content),
                            'img': img_path
                        })
                        
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DAA Lab Manual Solutions</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
    {premium_css}
    <style>
        .inline-code {{
            background: rgba(248, 152, 32, 0.15);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: var(--font-mono);
            color: var(--primary);
        }}
        .section-divider {{
            border: 0;
            height: 1px;
            background: var(--border-color);
            margin: 40px 0;
        }}
        .perf-graph {{ 
            width: 100%; 
            max-width: 800px; 
            border-radius: 12px; 
            margin: 20px 0; 
            border: 1px solid var(--border-color); 
            box-shadow: 0 10px 30px rgba(0,0,0,0.5); 
        }}
    </style>
</head>
<body>
    <div class="sidebar">
        <div class="sidebar-brand">
            <div class="sidebar-logo">D</div>
            <div class="brand-meta">
                <h1>DAA Lab</h1>
                <p>Solutions Manual</p>
            </div>
        </div>
        <ul class="nav-menu">
"""
    
    for exp in experiments:
        html_template += f'            <li class="nav-item" onclick="showExp(\'{exp["id"]}\')">{exp["title"]}</li>\n'
        
    html_template += """        </ul>
    </div>
    
    <div class="main-content">
"""
    
    for exp in experiments:
        img_html = f'<div class="card"><img src="{exp["img"]}" class="perf-graph" alt="Performance Graph"></div>' if exp["img"] else ''
        content_with_img = exp["html"].replace('<h2 style="font-family:\'Outfit\',sans-serif; color:#f8fafc; font-size:1.8rem; margin-top:40px; margin-bottom:20px;">OBSERVATION</h2>', f'{img_html}<h2 style="font-family:\'Outfit\',sans-serif; color:#f8fafc; font-size:1.8rem; margin-top:40px; margin-bottom:20px;">OBSERVATION</h2>')
        
        html_template += f"""        <div id="{exp["id"]}" class="lab-section">
            <div class="card">
                {content_with_img}
            </div>
        </div>
"""

    html_template += """    </div>

    <script>
        function showExp(id) {
            document.querySelectorAll('.lab-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            
            document.getElementById(id).classList.add('active');
            event.target.classList.add('active');
            window.scrollTo(0, 0);
        }
        
        document.querySelectorAll('pre').forEach(pre => {
            let code = pre.innerHTML;
            code = code.replace(/\\/\\*([\\s\\S]*?)\\*\\//g, '<span class="j-comment">/*$1*/</span>');
            code = code.replace(/\\/\\/(.*)/g, '<span class="j-comment">//$1</span>');
            code = code.replace(/"(.*?)"/g, '<span class="j-string">"$1"</span>');
            code = code.replace(/\\b(int|void|if|else|while|for|return|def|import|class|print|from|try|except|break|continue|elif)\\b/g, '<span class="j-keyword">$1</span>');
            pre.innerHTML = code;
        });

        if (document.querySelector('.nav-item')) {
            document.querySelector('.nav-item').click();
        }
    </script>
</body>
</html>
"""
    with open(r'a:\SEM4_Complete\DAA_Lab_Book.html', 'w', encoding='utf-8') as f:
        f.write(html_template)
    print("DAA Lab Book HTML Generated Successfully!")

if __name__ == "__main__":
    build_html()
