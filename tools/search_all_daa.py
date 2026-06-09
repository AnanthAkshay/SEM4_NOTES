import json

log_path = r"C:\Users\Akshay A\.gemini\antigravity-ide\brain\4dd565e2-ab17-40d0-bb9f-4f9e144a39aa\.system_generated\logs\transcript.jsonl"

with open(log_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        try:
            step = json.loads(line)
            content = step.get("content", "")
            if "# 🧠 DAA Lab" in content:
                print(f"Line {idx}: Length: {len(content)}, Has truncation marker? {'truncated' in content or 'TRUNCATED' in content}")
        except Exception as e:
            continue
