import subprocess

# Get old file content
old_content = subprocess.run(
    ["git", "show", "84a06d26d184b6150e9d6d909d21d376299ece49~1:DAA_Lab_Book.html"],
    capture_output=True, text=True, encoding='utf-8'
).stdout

# Get new file content (current main HEAD)
new_content = subprocess.run(
    ["git", "show", "HEAD:DAA_Lab_Book.html"],
    capture_output=True, text=True, encoding='utf-8'
).stdout

def get_experiment_1_block(text, search_tag, next_tag):
    start_idx = text.find(search_tag)
    end_idx = text.find(next_tag)
    if start_idx != -1 and end_idx != -1:
        return text[start_idx:end_idx]
    return "Not Found"

print("--- OLD Experiment 1 block structure ---")
old_block = get_experiment_1_block(old_content, 'id="Experiment_1_MergeSort"', 'id="Experiment_2_RandomizedQuickSort"')
for line in old_block.splitlines():
    if "<h" in line or "class=" in line or "<pre" in line or "<img" in line:
        print(line.strip())

print("\n--- NEW Experiment 1 block structure ---")
new_block = get_experiment_1_block(new_content, 'id="exp-1"', 'id="exp-2"')
for line in new_block.splitlines():
    if "<h" in line or "class=" in line or "<pre" in line or "<img" in line:
        print(line.strip())
