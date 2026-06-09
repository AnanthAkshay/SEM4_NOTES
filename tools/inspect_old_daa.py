import subprocess

# Retrieve the old file content using git show
res = subprocess.run(
    ["git", "show", "84a06d26d184b6150e9d6d909d21d376299ece49~1:DAA_Lab_Book.html"],
    capture_output=True,
    text=True,
    encoding='utf-8'
)

if res.returncode == 0:
    content = res.stdout
    lines = content.splitlines()
    print(f"Total lines: {len(lines)}")
    # Print lines that look like section divisions or H2/H3 tags
    for idx, line in enumerate(lines):
        if "<div id=" in line or "class=\"lab-section" in line or "<h2>" in line or "<h3>" in line:
            if idx < 1000: # limit to first 1000 lines for overview
                print(f"Line {idx+1}: {line.strip()}")
else:
    print("Error running git show:", res.stderr)
