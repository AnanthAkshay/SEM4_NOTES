import os
import re

def extract_questions():
    extracted_dir = r"a:\SEM4_Complete\MICROCONTROLLER\extracted_txt"
    files = [
        "CIE-12024.pdf.txt", "CIE-22024.pdf.txt", "CIE-22025.pdf.txt",
        "MAKEUP2023.pdf.txt", "SEE2023.pdf.txt", "SEE2023(O).pdf.txt",
        "SEE2024.pdf.txt", "SEE2025.pdf.txt"
    ]
    
    unit_questions = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    
    current_unit = None
    
    for filename in files:
        file_path = os.path.join(extracted_dir, filename)
        if not os.path.exists(file_path):
            print(f"Skipping {filename}: does not exist")
            continue
            
        print(f"Parsing: {filename}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        current_unit = None
        for i, line in enumerate(lines):
            clean_line = line.strip()
            # Detect unit headings
            unit_match = re.search(r'UNIT\s*[-–_:\s]*([I|V|1|2|3|4|5]+)', clean_line, re.IGNORECASE)
            if unit_match:
                unit_str = unit_match.group(1).upper()
                if 'V' in unit_str and 'I' not in unit_str:
                    current_unit = 5
                elif 'IV' in unit_str:
                    current_unit = 4
                elif 'III' in unit_str:
                    current_unit = 3
                elif 'II' in unit_str:
                    current_unit = 2
                elif 'I' in unit_str:
                    current_unit = 1
                elif '1' in unit_str:
                    current_unit = 1
                elif '2' in unit_str:
                    current_unit = 2
                elif '3' in unit_str:
                    current_unit = 3
                elif '4' in unit_str:
                    current_unit = 4
                elif '5' in unit_str:
                    current_unit = 5
                print(f"  Detected Unit {current_unit} at line {i+1}")
                continue
                
            # If we are inside a unit, try to capture questions
            if current_unit:
                # Question start like "1. a)" or "2." or "Q1" or "a)"
                if re.match(r'^\d+\s*[\.\)]', clean_line) or re.match(r'^[a-g]\s*[\.\)]', clean_line):
                    # We have a question, let's assemble it with some context
                    q_text = clean_line
                    # Look ahead a few lines to combine multi-line questions
                    j = i + 1
                    while j < len(lines):
                        next_line = lines[j].strip()
                        if not next_line:
                            j += 1
                            continue
                        # If next line starts another question or unit, stop
                        if (re.match(r'^\d+\s*[\.\)]', next_line) or 
                            re.match(r'^[a-g]\s*[\.\)]', next_line) or 
                            re.search(r'UNIT\s*[-–_:\s]*[I|V|1|2|3|4|5]+', next_line, re.IGNORECASE) or
                            "Page" in next_line or "21IS" in next_line or "Course" in next_line):
                            break
                        q_text += " " + next_line
                        j += 1
                    
                    # Clean up double spaces
                    q_text = re.sub(r'\s+', ' ', q_text)
                    unit_questions[current_unit].append((filename, q_text))
                    
    # Write categorized questions to a text file
    output_path = os.path.join(extracted_dir, "All_PYQs_By_Unit.txt")
    with open(output_path, 'w', encoding='utf-8') as out:
        for u in range(1, 6):
            out.write(f"\n==================================================\n")
            out.write(f"UNIT {u} Previous Year Questions\n")
            out.write(f"==================================================\n")
            seen = set()
            for file, q in unit_questions[u]:
                # Simple deduplication by basic text matching
                norm_q = re.sub(r'^\d+\s*[\.\)]\s*', '', q).lower()
                norm_q = re.sub(r'\s+', '', norm_q)
                if norm_q not in seen:
                    out.write(f"[{file}] {q}\n")
                    seen.add(norm_q)
                else:
                    out.write(f"[{file}] (Duplicate) {q}\n")
                    
    print(f"\nCompleted! Written unit-wise categorized questions to {output_path}")

if __name__ == '__main__':
    extract_questions()
