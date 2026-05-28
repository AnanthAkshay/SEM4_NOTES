import os
import re

def clean_slide_text(text):
    # Split text into lines, clean whitespace
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if not lines:
        return ""
    
    # Identify title (usually the first line if it's short and uppercase/bold)
    title = lines[0]
    body_lines = lines[1:]
    
    # If first line has slide numbers or is just empty/redundant, clean it
    if re.match(r'^slide\s*\d+$', title.lower()) or len(title) < 2:
        if body_lines:
            title = body_lines[0]
            body_lines = body_lines[1:]
        else:
            title = "Slide Details"

    # Format body into bullet points or clean paragraphs
    formatted_body = ""
    for line in body_lines:
        if line.startswith('•') or line.startswith('-') or line.startswith('*'):
            clean_line = re.sub(r'^[•\-\*]\s*', '', line)
            formatted_body += f"<li>{clean_line}</li>"
        else:
            # If line is longer or looks like a point, make it a bullet
            if len(line) < 120:
                formatted_body += f"<li>{line}</li>"
            else:
                formatted_body += f"<p style='margin-bottom: 8px;'>{line}</p>"
                
    if formatted_body.startswith('<li>'):
        formatted_body = f"<ul style='margin-left: 20px; list-style-type: square;'>{formatted_body}</ul>"
        
    html = f"<div class='slide-title-card'>{title}</div>"
    if formatted_body:
        html += f"<div class='slide-body-card'>{formatted_body}</div>"
        
    return html

def parse_pptx_file(filepath):
    if not os.path.exists(filepath):
        return []
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Split by slide marker: --- SLIDE 1 ---
    raw_slides = re.split(r'---\s*SLIDE\s*\d+\s*---', content)
    slides = []
    
    slide_num = 1
    for raw in raw_slides:
        raw_clean = raw.strip()
        if not raw_clean:
            continue
        
        slide_html = clean_slide_text(raw_clean)
        if slide_html:
            slides.append((slide_num, slide_html))
            slide_num += 1
            
    return slides

def main():
    mc_dir = r"a:\SEM4_Complete\MICROCONTROLLER"
    txt_dir = os.path.join(mc_dir, "extracted_txt")
    
    # Map units to their corresponding text files
    unit_files = {
        1: [
            ("MC_UNIT1_PPT1.pptx.txt", "PPT 1: Introduction to Embedded Systems"),
            ("MC_UNIT1_PPT2_19_02_2026.pptx.txt", "PPT 2: RISC vs CISC"),
            ("MC_UNIT1_PPT3_03-03-2026.pptx.txt", "PPT 3: SoC Infrastructure & Reset")
        ],
        2: [
            ("MC_UNIT2_PPT1_17_3_26.pptx.txt", "PPT 1: Peripherals, Memory & Endianness")
        ],
        3: [
            ("MC_UNIT3_PPT1_21_04_26.pptx.txt", "PPT 1: ARM7 Registers & Core"),
            ("MC_Unit3_PPT2_06_05_2026.pptx.txt", "PPT 2: ARM7 Instruction Set")
        ],
        4: [
            ("MC_Unit4_PPT1_Chapter5_05_05_2026.pptx.txt", "PPT 1: LPC2148 Peripherals (Timers & UART)"),
            ("MC_UNIT4_PPT2_Chapter 6.pptx.txt", "PPT 2: Embedded C and Interfacing")
        ],
        5: [
            ("MC_Unit-5_Chapter7.pptx.txt", "PPT 1: ARM Cortex-M0/M0+ & NVIC")
        ]
    }
    
    # Generate HTML blocks for each unit
    unit_html_blocks = {}
    for unit_num, files in unit_files.items():
        html = ""
        # Selector Dropdown
        html += f"<div class='ppt-selector-container' style='margin-bottom: 20px; display: flex; align-items: center; gap: 12px;'>\n"
        html += f"  <label style='font-family: var(--font-display); font-weight: 700; color: var(--text-primary); font-size: 0.95rem;'>Active Presentation:</label>\n"
        html += f"  <select id='ppt-select-unit{unit_num}' onchange='changePPT({unit_num}, this.value)' style='background-color: var(--bg-card); color: var(--text-primary); border: 1px solid var(--border-color); padding: 8px 12px; border-radius: 8px; font-family: var(--font-sans); outline: none; cursor: pointer;'>\n"
        for idx, (filename, label) in enumerate(files):
            html += f"    <option value='ppt{idx+1}'>{label}</option>\n"
        html += f"  </select>\n"
        
        # Download Link container
        html += f"  <div class='ppt-download-links-container' style='margin-left: auto;'>\n"
        for idx, (filename, label) in enumerate(files):
            real_pptx_name = filename.replace('.txt', '')
            html += f"    <a class='btn-action btn-accent ppt-dl-link-{unit_num} ppt-dl-{unit_num}-ppt{idx+1}' href='MICROCONTROLLER/{real_pptx_name}' download style='display: { 'inline-flex' if idx == 0 else 'none' };'>Download {real_pptx_name}</a>\n"
        html += f"  </div>\n"
        html += f"</div>\n\n"
        
        # Decks containers
        for idx, (filename, label) in enumerate(files):
            filepath = os.path.join(txt_dir, filename)
            slides = parse_pptx_file(filepath)
            
            html += f"<div class='slide-deck unit{unit_num}-deck' id='slide-deck-unit{unit_num}-ppt{idx+1}' style='display: { 'block' if idx == 0 else 'none' }; max-height: 650px; overflow-y: auto; background-color: #0b111e; border: 1px solid var(--border-color); border-radius: 10px; padding: 25px;'>\n"
            
            for s_num, s_html in slides:
                html += f"  <div class='slide-frame' style='background-color: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 24px; margin-bottom: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);'>\n"
                html += f"    <div class='slide-header' style='display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px; margin-bottom: 15px;'>\n"
                html += f"      <span style='font-family: var(--font-display); font-size: 0.8rem; text-transform: uppercase; color: var(--accent-cyan); font-weight: 700; letter-spacing: 0.05em;'>Slide {s_num}</span>\n"
                html += f"      <span style='font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-muted);'>{label}</span>\n"
                html += f"    </div>\n"
                html += f"    <div class='slide-content-wrapper' style='color: var(--text-secondary); font-size: 0.92rem; font-family: var(--font-sans); line-height: 1.6;'>\n"
                html += f"      {s_html}\n"
                html += f"    </div>\n"
                html += f"  </div>\n"
                
            html += f"</div>\n\n"
            
        unit_html_blocks[unit_num] = html
        
    # Read the main dashboard file
    dash_path = r"a:\SEM4_Complete\Microcontrollers_4th_Sem_Notes_Book.html"
    with open(dash_path, 'r', encoding='utf-8') as f:
        dash_content = f.read()
        
    # We will replace the <div class="slide-outline-container" id="unitX-slides" ...> ... </div> block with the new rich slides content
    for unit_num, block in unit_html_blocks.items():
        pattern = rf'<div class="slide-outline-container" id="unit{unit_num}-slides"[^>]*>.*?</div>'
        replacement = f'<div class="slide-outline-container" id="unit{unit_num}-slides" style="display:none;">\n{block}\n</div>'
        dash_content = re.sub(pattern, replacement, dash_content, flags=re.DOTALL)
        
    # Add JavaScript functions to change PPT in the script section
    js_addition = """
        function changePPT(unitNum, pptId) {
            // Hide all decks for this unit
            document.querySelectorAll('.unit' + unitNum + '-deck').forEach(deck => {
                deck.style.display = 'none';
            });
            // Show target deck
            const activeDeck = document.getElementById('slide-deck-unit' + unitNum + '-' + pptId);
            if (activeDeck) {
                activeDeck.style.display = 'block';
            }
            
            // Hide all download links for this unit
            document.querySelectorAll('.ppt-dl-link-' + unitNum).forEach(link => {
                link.style.display = 'none';
            });
            // Show active download link
            const activeLink = document.querySelector('.ppt-dl-' + unitNum + '-' + pptId);
            if (activeLink) {
                activeLink.style.display = 'inline-flex';
            }
        }
    """
    
    # We insert the changePPT function into the script tag in the dashboard
    dash_content = dash_content.replace("function switchUnitTab", js_addition + "\n        function switchUnitTab")
    
    # Add extra style for slide-title-card and slide-body-card in the css section
    css_addition = """
        .slide-title-card {
            font-family: var(--font-display);
            font-size: 1.2rem;
            font-weight: 800;
            color: var(--text-primary);
            margin-bottom: 12px;
            color: var(--accent-amber);
        }
        .slide-body-card {
            font-size: 0.95rem;
            color: var(--text-secondary);
        }
        .slide-body-card li {
            margin-bottom: 8px;
        }
    """
    dash_content = dash_content.replace(".slide-card:last-child {", css_addition + "\n        .slide-card:last-child {")
    
    with open(dash_path, 'w', encoding='utf-8') as f:
        f.write(dash_content)
        
    print("Successfully built slide outline presentation viewer blocks for all 5 units inside Microcontrollers_4th_Sem_Notes_Book.html!")

if __name__ == '__main__':
    main()
