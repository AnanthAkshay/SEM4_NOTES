import zipfile
import xml.etree.ElementTree as ET

def get_docx_text(path):
    text = []
    with zipfile.ZipFile(path) as docx:
        tree = ET.parse(docx.open('word/document.xml'))
        root = tree.getroot()
        for paragraph in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            para_text = []
            for run in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                para_text.append(run.text)
            text.append(''.join(para_text))
    return '\n'.join(text)

try:
    text_ab = get_docx_text('a:/SEM4_Complete/DBMS_LAB/DBMSPartAandBPrograms.docx')
    with open('a:/SEM4_Complete/DBMS_LAB/DBMSPartAandBPrograms.txt', 'w', encoding='utf-8') as f:
        f.write(text_ab)
    print("DBMSPartAandBPrograms.docx converted successfully!")
except Exception as e:
    print("Error parsing DBMSPartAandBPrograms.docx:", e)

try:
    text_b = get_docx_text('a:/SEM4_Complete/DBMS_LAB/DBMSPartBPrograms.docx')
    with open('a:/SEM4_Complete/DBMS_LAB/DBMSPartBPrograms.txt', 'w', encoding='utf-8') as f:
        f.write(text_b)
    print("DBMSPartBPrograms.docx converted successfully!")
except Exception as e:
    print("Error parsing DBMSPartBPrograms.docx:", e)
