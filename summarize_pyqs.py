import os
import re

def summarize_papers():
    txt_dir = r"a:\SEM4_Complete\DAA_text"
    output_file = r"a:\SEM4_Complete\DAA_text\aggregated_pyqs.txt"
    
    files = [f for f in os.listdir(txt_dir) if f.endswith('.txt') and f != 'syllabus.txt' and f != 'aggregated_pyqs.txt']
    
    unit_questions = {
        "UNIT 1": [],
        "UNIT 2": [],
        "UNIT 3": [],
        "UNIT 4": [],
        "UNIT 5": []
    }
    
    for filename in files:
        paper_name = filename.replace('.txt', '')
        path = os.path.join(txt_dir, filename)
        if not os.path.exists(path):
            continue
            
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Try to split by UNIT
        # We look for "UNIT - I", "UNIT I", "UNIT - 1", "UNIT 1" etc.
        units_split = re.split(r'UNIT\s*[-–]?\s*(?:[IVX12345]+|\d+)', content, flags=re.IGNORECASE)
        
        # Let's find unit markers to see which parts correspond to which units
        unit_markers = re.findall(r'UNIT\s*[-–]?\s*([IVX12345]+|\d+)', content, flags=re.IGNORECASE)
        
        if len(units_split) > 1:
            for idx, unit_num_str in enumerate(unit_markers):
                unit_part = units_split[idx + 1]
                # Normalize unit number
                u_str = unit_num_str.upper().strip()
                unit_key = None
                if u_str in ['I', '1']: unit_key = "UNIT 1"
                elif u_str in ['II', '2']: unit_key = "UNIT 2"
                elif u_str in ['III', '3']: unit_key = "UNIT 3"
                elif u_str in ['IV', '4']: unit_key = "UNIT 4"
                elif u_str in ['V', '5']: unit_key = "UNIT 5"
                
                if unit_key:
                    # Extract questions
                    # Usually formatted as "1. a) ...", "2. b) ..." etc.
                    lines = unit_part.split('\n')
                    current_q = []
                    for line in lines:
                        line_stripped = line.strip()
                        if not line_stripped:
                            continue
                        if re.match(r'^\d+\.', line_stripped) or re.match(r'^[a-z]\)', line_stripped):
                            if current_q:
                                unit_questions[unit_key].append(f"[{paper_name}] " + " ".join(current_q))
                                current_q = []
                            current_q.append(line_stripped)
                        elif current_q:
                            current_q.append(line_stripped)
                    if current_q:
                        unit_questions[unit_key].append(f"[{paper_name}] " + " ".join(current_q))
        else:
            # If no units found, just append to a general pool or try to parse line by line
            pass
            
    with open(output_file, 'w', encoding='utf-8') as out:
        for unit, qs in unit_questions.items():
            out.write(f"=================================================\n{unit}\n=================================================\n")
            # Deduplicate questions somewhat or just print them all
            for q in qs:
                out.write(f"- {q}\n\n")
            out.write("\n")
            
    print(f"Aggregated questions written to {output_file}")

if __name__ == "__main__":
    summarize_papers()
