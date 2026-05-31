import os
import sys

def extract_pdf_text(pdf_path, txt_path):
    print(f"Extracting {pdf_path} -> {txt_path}")
    try:
        # Try PyPDF2
        import PyPDF2
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for i, page in enumerate(reader.pages):
                text += f"\n--- Page {i+1} ---\n"
                text += page.extract_text() or ""
            with open(txt_path, 'w', encoding='utf-8') as out:
                out.write(text)
            return True
    except ImportError:
        try:
            # Try pypdf
            import pypdf
            with open(pdf_path, 'rb') as f:
                reader = pypdf.PdfReader(f)
                text = ""
                for i, page in enumerate(reader.pages):
                    text += f"\n--- Page {i+1} ---\n"
                    text += page.extract_text() or ""
                with open(txt_path, 'w', encoding='utf-8') as out:
                    out.write(text)
                return True
        except ImportError:
            try:
                # Try pdfminer
                from pdfminer.high_level import extract_text
                text = extract_text(pdf_path)
                with open(txt_path, 'w', encoding='utf-8') as out:
                    out.write(text)
                return True
            except ImportError:
                print("No PDF libraries installed. Attempting to install pypdf via pip...")
                return False

if __name__ == "__main__":
    pdf_dir = r"a:\SEM4_Complete\DAA"
    out_dir = r"a:\SEM4_Complete\DAA_text"
    os.makedirs(out_dir, exist_ok=True)
    
    # Also extract syllabus PDF in the root
    syllabus_pdf = r"a:\SEM4_Complete\ISE_UG_3 & 4th sem-aug25-V7_9thSep25 (1) (1).pdf"
    if os.path.exists(syllabus_pdf):
        extract_pdf_text(syllabus_pdf, os.path.join(out_dir, "syllabus.txt"))
        
    for file in os.listdir(pdf_dir):
        if file.lower().endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, file)
            txt_path = os.path.join(out_dir, file.replace('.pdf', '.txt'))
            success = extract_pdf_text(pdf_path, txt_path)
            if not success:
                # We need to install pypdf, let's exit with 1 to indicate we need installation
                sys.exit(1)
    print("All PDFs successfully extracted!")
