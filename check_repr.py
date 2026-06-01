with open('a:/SEM4_Complete/Java_Advanced_Lab_Book.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'String sql = "INSERT INTO Representative VALUES' in line:
        for j in range(i-1, i+5):
            print(repr(lines[j]))
