import re
import sys

def main():
    with open('a:/SEM4_Complete/Java_Advanced_Lab_Book.html', 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'id="ex10-cust">.*?<pre>(.*?)</pre>', re.DOTALL)
    m = pattern.search(content)
    if m:
        pre_content = m.group(1)
        lines = pre_content.split('\n')
        print(f"Total lines in HTML: {len(lines)}")
        for idx in range(min(len(lines), 35)):
            print(f"{idx+1}: {repr(lines[idx])}")
    else:
        print("Not found")

if __name__ == '__main__':
    main()
