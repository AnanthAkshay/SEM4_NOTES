import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def inspect_docx(path):
    ns = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    }
    
    with zipfile.ZipFile(path) as docx:
        tree = ET.parse(docx.open('word/document.xml'))
        root = tree.getroot()
        body = root.find('w:body', ns)
        if body is None:
            print("No body found")
            return
        
        for element in body:
            # Paragraph
            if element.tag == f"{{{ns['w']}}}p":
                text = "".join(t.text for t in element.iter(f"{{{ns['w']}}}t") if t.text)
                if text.strip():
                    print(f"[P] {text}")
            # Table
            elif element.tag == f"{{{ns['w']}}}tbl":
                print("[TABLE START]")
                rows = element.findall('w:tr', ns)
                for r_idx, row in enumerate(rows):
                    cells = row.findall('w:tc', ns)
                    row_data = []
                    for cell in cells:
                        cell_text = []
                        # Walk through paragraphs inside cell
                        for p in cell.findall('w:p', ns):
                            p_text = "".join(t.text for t in p.iter(f"{{{ns['w']}}}t") if t.text)
                            cell_text.append(p_text)
                        row_data.append(" ".join(cell_text).strip())
                    print(f"  Row {r_idx}: {row_data}")
                print("[TABLE END]")

if __name__ == "__main__":
    import sys
    # Re-route stdout to a UTF-8 file
    with open('a:/SEM4_Complete/tools/docx_full_content.txt', 'w', encoding='utf-8') as f:
        sys.stdout = f
        inspect_docx('a:/SEM4_Complete/DBMS_LAB/DBMSPartAandBPrograms.docx')

