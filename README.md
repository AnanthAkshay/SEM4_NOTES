# 📚 SEM 4 Notes — ISE | MSRIT × VTU

> Comprehensive study notes, lab programs, and compiled HTML note-books for **4th Semester Information Science & Engineering** at M.S. Ramaiah Institute of Technology (MSRIT), Bengaluru — affiliated with Visvesvaraya Technological University (VTU).

---

## 🗂️ Subjects Covered

| Subject | Theory Notes | Lab Notes | Compiled HTML Book |
|---|---|---|---|
| **Advanced Java** | [`JAVA/`](./JAVA) | [`JAVA_LAB/`](./JAVA_LAB) | [`Java_4th_Sem_Notes_Book.html`](./Java_4th_Sem_Notes_Book.html) · [`Java_Advanced_Lab_Book.html`](./Java_Advanced_Lab_Book.html) |
| **Database Management Systems (DBMS)** | [`DBMS/`](./DBMS) | [`DBMS_LAB/`](./DBMS_LAB) | [`DBMS_4th_Sem_Notes_Book.html`](./DBMS_4th_Sem_Notes_Book.html) · [`DBMS_Lab_Book.html`](./DBMS_Lab_Book.html) |
| **Design & Analysis of Algorithms (DAA)** | [`DAA/`](./DAA) · [`DAA_text/`](./DAA_text) | [`DAA_LAB/`](./DAA_LAB) | [`DAA_4th_Sem_Notes_Book.html`](./DAA_4th_Sem_Notes_Book.html) · [`DAA_Lab_Book.html`](./DAA_Lab_Book.html) |
| **Engineering Mathematics** | [`MATHS/`](./MATHS) | — | [`Engineering_Mathematics_4th_Sem_Notes_Book.html`](./Engineering_Mathematics_4th_Sem_Notes_Book.html) |
| **Microcontrollers** | [`MICROCONTROLLER/`](./MICROCONTROLLER) | — | [`Microcontrollers_4th_Sem_Notes_Book.html`](./Microcontrollers_4th_Sem_Notes_Book.html) |
| **R Programming (Data Analytics)** | [`R_PROGRAMMING/`](./R_PROGRAMMING) | — | [`R_Programming_4th_Sem_Notes_Book.html`](./R_Programming_4th_Sem_Notes_Book.html) |

📄 Official VTU scheme document: [`ISE_UG_3 & 4th sem-aug25-V7_9thSep25.pdf`](./ISE_UG_3%20%26%204th%20sem-aug25-V7_9thSep25%20(1)%20(1).pdf)

---

## 🚀 How to Use

### Option 1 — Open the HTML Note-Books (Recommended)

Each subject has a self-contained `.html` file that bundles all notes into a single, readable, browser-viewable document. Just clone the repo and open any HTML file in your browser — no dependencies needed.

```bash
git clone https://github.com/AnanthAkshay/SEM4_NOTES.git
cd SEM4_NOTES

# Open any subject note-book
open Java_4th_Sem_Notes_Book.html          # macOS
start Java_4th_Sem_Notes_Book.html         # Windows
xdg-open Java_4th_Sem_Notes_Book.html      # Linux
```

### Option 2 — Browse Raw Notes

Navigate into any subject folder (`JAVA/`, `DBMS/`, `DAA/`, etc.) to access the individual raw notes and source files directly.

---

## 🏗️ Build System

The HTML note-books are auto-generated from raw notes using a set of Python scripts. The pipeline is:

```
Raw Notes (PDFs / Markdown / Code)
        │
        ▼
  Python Build Scripts
  (extract_pdfs.py, write_md*.py, build_html.py, etc.)
        │
        ▼
  Compiled HTML Note-Books  ←  Ready to open in any browser
```

### Key Scripts

| Script | Purpose |
|---|---|
| `build_html.py` | Compiles theory notes into HTML note-books |
| `build_dbms_html.py` | DBMS-specific HTML builder |
| `extract_pdfs.py` | Extracts content from source PDFs |
| `extract_code.py` | Pulls out code snippets for lab sections |
| `generate_dbms_diagrams.py` | Generates ER and schema diagrams for DBMS |
| `summarize_pyqs.py` | Processes and summarizes Previous Year Questions |
| `write_dbms_experiments_*.py` | Writes DBMS lab experiments (batched 1–3, 4–6, 7–12) |
| `format_dbms_manual.py` | Formats the DBMS lab manual |
| `merge_dbms_html.py` | Merges partial HTML fragments into one file |
| `write_md*.py` | Iterative markdown generation utilities (v1–v9) |
| `check*.py` | Validation and integrity checks |

To rebuild a note-book after editing raw notes:

```bash
python build_html.py          # Rebuild theory note-books
python build_dbms_html.py     # Rebuild DBMS note-book
```

---

## 📁 Repository Structure

```
SEM4_NOTES/
│
├── 📂 DAA/                          # DAA theory notes
├── 📂 DAA_LAB/                      # DAA lab programs
├── 📂 DAA_text/                     # DAA reference textbook excerpts
├── 📂 DBMS/                         # DBMS theory notes
├── 📂 DBMS_LAB/                     # DBMS lab SQL experiments (12 programs)
├── 📂 JAVA/                         # Advanced Java theory notes
├── 📂 JAVA_LAB/                     # Advanced Java lab programs (12 programs)
├── 📂 MATHS/                        # Engineering Mathematics notes
├── 📂 MICROCONTROLLER/              # Microcontrollers theory notes
├── 📂 R_PROGRAMMING/                # R Programming & Data Analytics notes
│
├── 📄 *.html                        # Compiled subject note-books (open in browser)
├── 📄 ISE_UG_3 & 4th sem-...pdf    # Official VTU scheme & syllabus
│
└── 🐍 *.py                          # Python build and generation scripts
```

---

## 🛠️ Tech Stack

- **Notes Format:** Markdown, HTML, PDF
- **Build Tools:** Python 3 (standard library + BeautifulSoup / custom parsers)
- **Lab Programs:** Java (Advanced Java), SQL (DBMS), C (DAA), R
- **Output:** Self-contained HTML note-books, browser-viewable offline

---

## 🎓 Academic Context

| Field | Details |
|---|---|
| **Institution** | M.S. Ramaiah Institute of Technology (MSRIT), Bengaluru |
| **University** | Visvesvaraya Technological University (VTU) |
| **Department** | Information Science & Engineering (ISE) |
| **Semester** | 4th Semester (Batch: 2024–25) |
| **Scheme** | VTU ISE UG Scheme — Aug 2025 Revision |

---

## 👤 Author

**Ananthakrishna Akshay**
- GitHub: [@AnanthAkshay](https://github.com/AnanthAkshay)
- Repo: [AnanthAkshay/SEM4_NOTES](https://github.com/AnanthAkshay/SEM4_NOTES)

---

## 📌 Notes

- These notes are intended for personal academic use and sharing with fellow MSRIT ISE students.
- Lab programs follow the official VTU syllabus programs and are exam-ready.
- If you find any errors or want to contribute corrections, feel free to open an issue or a pull request.

---

*Last updated: June 2026*
