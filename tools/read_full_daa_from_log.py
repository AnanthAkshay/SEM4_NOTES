import json

log_path = r"C:\Users\Akshay A\.gemini\antigravity-ide\brain\4dd565e2-ab17-40d0-bb9f-4f9e144a39aa\.system_generated\logs\transcript.jsonl"

with open(log_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        try:
            step = json.loads(line)
            content = step.get("content", "")
            if "# 🧠 DAA Lab" in content:
                print(f"Line {idx}: Length of content: {len(content)}")
                # Check if it contains some keywords from the middle
                print("Contains 'Counting Sort'?", "Counting Sort" in content)
                print("Contains 'Hospital Median'?", "Hospital Median" in content)
                print("Contains 'Friend Groups'?", "Friend Groups" in content)
                print("Contains 'City Navigation'?", "City Navigation" in content)
                print("Contains 'Video Matrices'?", "Video Matrices" in content)
                print("Contains 'Plagiarism Check'?", "Plagiarism Check" in content)
                print("Contains 'Huffman Coding'?", "Huffman Coding" in content)
                print("Contains 'File Traversal'?", "File Traversal" in content)
                print("Contains 'Ford-Fulkerson'?", "Ford-Fulkerson" in content)
                break
        except Exception as e:
            continue
