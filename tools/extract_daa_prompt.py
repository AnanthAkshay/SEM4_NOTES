import json

log_path = r"C:\Users\Akshay A\.gemini\antigravity-ide\brain\4dd565e2-ab17-40d0-bb9f-4f9e144a39aa\.system_generated\logs\transcript.jsonl"
out_path = r"a:\SEM4_Complete\tools\daa_prompt.txt"

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            step = json.loads(line)
            # Find the step containing "DAA Lab — All 12 Programs"
            content = step.get("content", "")
            if "# 🧠 DAA Lab" in content:
                with open(out_path, 'w', encoding='utf-8') as out_f:
                    out_f.write(content)
                print("Found and extracted DAA Lab programs content successfully!")
                break
        except Exception as e:
            continue
