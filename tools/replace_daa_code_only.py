import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def main():
    # 1. Read simple version from git commit 84a06d26
    res = subprocess.run(
        ["git", "show", "84a06d26d184b6150e9d6d909d21d376299ece49:DAA_Lab_Book.html"],
        capture_output=True, text=True, encoding='utf-8'
    )
    if res.returncode != 0:
        print("Error reading simple version:", res.stderr)
        return
    simple_html = res.stdout

    # 2. Extract codes from simple version
    # Inside simple version, experiments are in <div id="exp-N" ...>
    # C code is between the first <pre> and </pre> inside C Implementation
    # Python code is between the first <pre> and </pre> inside Python Implementation
    simple_codes = {}
    for n in range(1, 13):
        # find the exp div
        start_tag = f'<!-- ========================= EXPERIMENT {n} ========================= -->'
        if start_tag not in simple_html:
            # Fallback to class search
            start_tag = f'<div id="exp-{n}" class="lab-section">'
        
        start_idx = simple_html.find(start_tag)
        if start_idx == -1:
            print(f"Failed to find simple exp {n}")
            continue
            
        if n < 12:
            end_tag = f'<!-- ========================= EXPERIMENT {n+1} ========================= -->'
            if end_tag not in simple_html:
                end_tag = f'<div id="exp-{n+1}" class="lab-section">'
            end_idx = simple_html.find(end_tag)
        else:
            end_idx = simple_html.find('<!-- ========================= VIVA VOCE')
            if end_idx == -1:
                end_idx = len(simple_html)
                
        exp_block = simple_html[start_idx:end_idx]
        
        # Extract C code
        c_pre_start = exp_block.find('<pre>')
        c_pre_end = exp_block.find('</pre>')
        c_code = exp_block[c_pre_start+5:c_pre_end]
        
        # Extract Python code (it's the second pre block in the exp block)
        py_pre_start = exp_block.find('<pre>', c_pre_end)
        py_pre_end = exp_block.find('</pre>', py_pre_start)
        py_code = exp_block[py_pre_start+5:py_pre_end]
        
        simple_codes[n] = {
            'c': c_code,
            'py': py_code
        }
        print(f"Extracted simple code for Exp {n}")

    # 3. Read current local original DAA_Lab_Book.html
    local_path = ROOT / "DAA_Lab_Book.html"
    local_html = local_path.read_text(encoding="utf-8")
    
    # We will locate each experiment section in local_html and replace the first <pre class="language-c"> and <pre class="language-python">
    # Experiment section IDs are Experiment_1_MergeSort, Experiment_2_RandomizedQuickSort, etc.
    exp_ids = [
        "Experiment_1_MergeSort",
        "Experiment_2_RandomizedQuickSort",
        "Experiment_3_PriorityQueue",
        "Experiment_4_CountingSort",
        "Experiment_5_MedianOfMedians",
        "Experiment_6_DisjointSetUnion",
        "Experiment_7_Dijkstra",
        "Experiment_8_MatrixChainMultiplication",
        "Experiment_9_LongestCommonSubsequence",
        "Experiment_10_HuffmanCoding",
        "Experiment_11_DepthFirstSearch",
        "Experiment_12_FordFulkersonMaxFlow"
    ]
    
    for n in range(1, 13):
        exp_id = exp_ids[n-1]
        start_tag = f'<div id="{exp_id}" class="lab-section">'
        start_idx = local_html.find(start_tag)
        if start_idx == -1:
            print(f"Could not find local exp {exp_id}")
            continue
            
        if n < 12:
            next_exp_id = exp_ids[n]
            end_tag = f'<div id="{next_exp_id}" class="lab-section">'
            end_idx = local_html.find(end_tag)
        else:
            # Exp 12 ends before the scripts or page end
            end_idx = local_html.find('<!-- ======================= ECLIPSE')
            if end_idx == -1:
                end_idx = len(local_html)
                
        exp_block = local_html[start_idx:end_idx]
        
        # Replace C code block (first occurrence of <pre class="language-c">...</pre>)
        c_pattern = r'(<pre class="language-c">)([\s\S]*?)(</pre>)'
        # Replace Python code block (first occurrence of <pre class="language-python">...</pre>)
        py_pattern = r'(<pre class="language-python">)([\s\S]*?)(</pre>)'
        
        # Let's replace only the first occurrence of C pattern
        c_match = re.search(c_pattern, exp_block)
        if c_match:
            new_c_block = c_match.group(1) + simple_codes[n]['c'] + c_match.group(3)
            # Replace the first occurrence of c_match in exp_block
            exp_block = exp_block.replace(c_match.group(0), new_c_block, 1)
        else:
            print(f"Could not find C block in local exp {n}")
            
        # Replace the first occurrence of Python pattern
        py_match = re.search(py_pattern, exp_block)
        if py_match:
            # We want to make sure it's the main algorithm block and not the plotting block.
            # The main algorithm block has def merge() or class MaxHeap etc., whereas plotting script has "import matplotlib"
            # Since the main algorithm python block is always the first <pre class="language-python"> in the exp block,
            # this works perfectly. Let's verify:
            new_py_block = py_match.group(1) + simple_codes[n]['py'] + py_match.group(3)
            exp_block = exp_block.replace(py_match.group(0), new_py_block, 1)
        else:
            print(f"Could not find Python block in local exp {n}")
            
        # Put the updated exp_block back into local_html
        local_html = local_html[:start_idx] + exp_block + local_html[end_idx:]
        print(f"Replaced C and Python programs in local exp {n}")
        
    local_path.write_text(local_html, encoding="utf-8")
    print("DAA_Lab_Book.html updated successfully with simple programs!")

if __name__ == "__main__":
    main()
