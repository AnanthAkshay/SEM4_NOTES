with open('a:/SEM4_Complete/Java_Advanced_Lab_Book.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'String sql = "INSERT INTO Representative VALUES' in line:
        for char in line[-15:]:
            print(f"char: {char} code: {ord(char)}")
