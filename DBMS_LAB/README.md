# DATABASE MANAGEMENT SYSTEMS LABORATORY MANUAL

**Course Code:** ISL47  
**Credits:** 0:0:1  
**Contact Hours:** 30P  
**Course Coordinator:** Dr. Savita K. Shetty  
**Institution:** Engineering College — Semester 4 (ISE)

---

## Purpose

Complete lab record material for:

- Record submission  
- Internal evaluation  
- Lab viva  
- Practical examination  
- End-semester lab examination  

---

## Experiments Index

| # | Title | Technologies |
|---|--------|--------------|
| 1 | Employee – Department – Project | Oracle SQL |
| 2 | Part – Supplier – Supply (Shipment) | Oracle SQL |
| 3 | Boat – Sailor – Reserves | Oracle SQL |
| 4 | Customer – Branch – Account – Transaction | Oracle SQL |
| 5 | Books – Student – Borrows | Oracle SQL |
| 6 | Patient – Doctor – Appointment | Oracle SQL |
| 7 | MongoDB Employee/Department + Salary PL/SQL | MongoDB + PL/SQL |
| 8 | MongoDB Patient/Doctor + Fee Update PL/SQL | MongoDB + PL/SQL |
| 9 | MongoDB Part/Supplier + Shipment Backup PL/SQL | MongoDB + PL/SQL |
| 10 | MongoDB Boat/Sailor + Weekend Trigger | MongoDB + Trigger |
| 11 | MongoDB Customer/Branch + Cursor Copy | MongoDB + Cursor |
| 12 | MongoDB Books/Student + User Exception | MongoDB + PL/SQL |

---

## How to Use

1. **Per experiment:** Open `Experiment_N_.../Experiment_N.md` and copy sections into your record book in order (Aim → Theory → ER → SQL → Queries → Result → Viva).
2. **Interactive manual:** Open `DBMS_Lab_Book.html` in a browser (sidebar navigation for all 12 experiments).
3. **Execution:** Run SQL in Oracle SQL Developer; run MongoDB scripts in `mongosh` or MongoDB Compass.
4. **Regenerate:**  
   `python write_dbms_experiments_1_3.py`  
   `python write_dbms_experiments_4_6.py`  
   `python write_dbms_experiments_7_12.py`  
   `python build_dbms_html.py`

---

## Record Book Section Order (Per Experiment)

1. Aim  
2. Problem Statement  
3. Objectives  
4. Theory  
5. Entity Identification  
6. Constraints  
7. ER Diagram (Mermaid + ASCII)  
8. Schema Diagram  
9. Relational Model  
10. SQL / MongoDB / PL/SQL Implementation  
11. Queries with Expected Output  
12. Output Section  
13. Step-by-Step Execution  
14. Viva Questions & Answers  
15. Lab Exam Questions  
16. Result  

---

## Diagram Images (for Record Book)

Each experiment folder contains **print-ready PNG figures**:

| File | Description |
|------|-------------|
| `er_diagram.png` | Chen-style ER diagram (entities, relationships, PK/FK) |
| `schema_diagram.png` | Relational schema (tables, keys, FK arrows) |

**Paste in record:** Open the PNG from the experiment folder → paste or glue below the ER DIAGRAM / SCHEMA DIAGRAM headings. Markdown and HTML already embed these images.

**Regenerate diagrams:**
```powershell
python generate_dbms_diagrams.py
python build_dbms_html.py
```

---

## Files

- `a:\SEM4_Complete\DBMS_LAB\` — All experiment markdown + diagram PNGs  
- `a:\SEM4_Complete\DBMS_Lab_Book.html` — **Merged manual** (your `1.html`–`12.html` + sidebar navigation)  
- `a:\SEM4_Complete\DBMS_LAB\1.html` … `12.html` — Individual experiment pages (source)  

**Rebuild merged book after editing any `N.html`:**
```powershell
python merge_dbms_html.py
```
