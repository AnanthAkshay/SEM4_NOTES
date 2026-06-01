import re
import os

with open('a:/SEM4_Complete/Java_Advanced_Lab_Book.html', 'r', encoding='utf-8') as f:
    content = f.read()

def extract_and_save(ex_id, file_path):
    pattern = rf'<div class=\"code-content[^\"]*\" id=\"{ex_id}\">\s*<pre>(.*?)</pre>\s*</div>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        code = match.group(1).replace('&lt;', '<').replace('&gt;', '>')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(code.strip())
        print(f'Saved {file_path}')
    else:
        print(f'Failed to find {ex_id}')

extract_and_save('ex9-swing', 'a:/SEM4_Complete/JAVA_LAB/Ex9_StudentUI/studentui/StudentSwingApp.java')
extract_and_save('ex10-cust', 'a:/SEM4_Complete/JAVA_LAB/Ex10_CustomerUI/customerui/CustomerPurchaseApp.java')
extract_and_save('ex11-jdbc', 'a:/SEM4_Complete/JAVA_LAB/Ex11_JDBC/jdbcui/JDBCRepCustApp.java')
extract_and_save('ex12-jsp', 'a:/SEM4_Complete/JAVA_LAB/Ex12_JSP/shirt_purchase.jsp')
