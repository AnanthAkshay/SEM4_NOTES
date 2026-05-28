import os
import zipfile
import xml.etree.ElementTree as ET
import pypdf

# Namespaces for XML parsing of office documents
NAMESPACES = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
}

def extract_text_from_pptx(pptx_path):
    """Extract text from all slides in a .pptx file."""
    text_runs = []
    try:
        with zipfile.ZipFile(pptx_path, 'r') as zip_ref:
            # Slides are named ppt/slides/slide1.xml, slide2.xml, etc.
            # Let's find all slide files and sort them numerically
            slide_files = [f for f in zip_ref.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            slide_files.sort(key=lambda x: int(os.path.basename(x).replace('slide', '').replace('.xml', '')))
            
            for slide_file in slide_files:
                slide_num = os.path.basename(slide_file).replace('slide', '').replace('.xml', '')
                text_runs.append(f"\n--- SLIDE {slide_num} ---")
                
                slide_xml = zip_ref.read(slide_file)
                root = ET.fromstring(slide_xml)
                
                # In pptx, text is located in <a:t> (text runs) inside <p:txBody> or general drawing elements
                for t_elem in root.findall('.//a:t', NAMESPACES):
                    if t_elem.text:
                        text_runs.append(t_elem.text.strip())
    except Exception as e:
        return f"Error extracting {pptx_path}: {e}"
    
    return "\n".join(text_runs)

def extract_text_from_docx(docx_path):
    """Extract text from a .docx file."""
    text_runs = []
    try:
        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            document_xml = zip_ref.read('word/document.xml')
            root = ET.fromstring(document_xml)
            
            # In docx, text is inside <w:t> elements
            for t_elem in root.findall('.//w:t', NAMESPACES):
                if t_elem.text:
                    text_runs.append(t_elem.text.strip())
    except Exception as e:
        return f"Error extracting {docx_path}: {e}"
    
    return " ".join(text_runs)

def extract_text_from_pdf(pdf_path):
    """Extract text from a .pdf file."""
    text_runs = []
    try:
        reader = pypdf.PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages):
            text_runs.append(f"\n--- PAGE {page_num + 1} ---")
            text = page.extract_text()
            if text:
                text_runs.append(text)
    except Exception as e:
        return f"Error extracting {pdf_path}: {e}"
    
    return "\n".join(text_runs)

def main():
    mc_dir = r"a:\SEM4_Complete\MICROCONTROLLER"
    output_dir = os.path.join(mc_dir, "extracted_txt")
    os.makedirs(output_dir, exist_ok=True)
    
    print("Starting text extraction from Microcontrollers directory...")
    
    # Process files
    for filename in os.listdir(mc_dir):
        file_path = os.path.join(mc_dir, filename)
        if not os.path.isfile(file_path):
            continue
            
        ext = os.path.splitext(filename)[1].lower()
        output_txt_name = filename + ".txt"
        output_txt_path = os.path.join(output_dir, output_txt_name)
        
        print(f"Processing: {filename}...")
        
        if ext == '.pptx':
            text = extract_text_from_pptx(file_path)
            with open(output_txt_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"  Extracted PPTX to {output_txt_name}")
            
        elif ext == '.docx':
            text = extract_text_from_docx(file_path)
            with open(output_txt_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"  Extracted DOCX to {output_txt_name}")
            
        elif ext == '.pdf' and filename != 'Microcontroller Lab.pdf': 
            # We skip extracting lab PDF if it's too large, but actually let's extract it as well!
            text = extract_text_from_pdf(file_path)
            with open(output_txt_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"  Extracted PDF to {output_txt_name}")
            
        elif filename == 'Microcontroller Lab.pdf':
            text = extract_text_from_pdf(file_path)
            with open(output_txt_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"  Extracted Lab PDF to {output_txt_name}")

    # Also search for Microcontroller in the parent directory's syllabus PDF
    syllabus_pdf_path = r"a:\SEM4_Complete\ISE_UG_3 & 4th sem-aug25-V7_9thSep25 (1) (1).pdf"
    if os.path.exists(syllabus_pdf_path):
        print(f"Processing syllabus PDF: {os.path.basename(syllabus_pdf_path)}...")
        try:
            reader = pypdf.PdfReader(syllabus_pdf_path)
            mc_pages = []
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text and ("Microcontroller" in text or "MICROCONTROLLER" in text):
                    mc_pages.append(f"\n--- PAGE {i + 1} ---")
                    mc_pages.append(text)
            
            if mc_pages:
                syllabus_txt_path = os.path.join(output_dir, "Syllabus_MC_Extracted.txt")
                with open(syllabus_txt_path, 'w', encoding='utf-8') as f:
                    f.write("\n".join(mc_pages))
                print(f"  Extracted potential Microcontroller syllabus pages to Syllabus_MC_Extracted.txt")
        except Exception as e:
            print(f"  Error extracting from syllabus PDF: {e}")

    print("\nExtraction complete! All text files saved in a:\\SEM4_Complete\\MICROCONTROLLER\\extracted_txt\\")

if __name__ == '__main__':
    main()
