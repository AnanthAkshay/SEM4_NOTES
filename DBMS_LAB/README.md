# DATABASE MANAGEMENT SYSTEMS LABORATORY MANUAL

**Course Code:** 24ISL47  
**Credits:** 0:0:1  
**Term:** Feb 2026 to Jun 2026  
**Institution:** Ramaiah Institute of Technology — Semester 4 (ISE)

---

## Purpose

Complete lab record material for:

- Record submission  
- Internal evaluation  
- Lab viva  
- Practical examination  
- End-semester lab examination (SEE)  

---

## Experiments Index

Each experiment below is structured with **PART A** (Oracle SQL design, constraints, and query execution) and **PART B** (MongoDB document queries and Oracle PL/SQL programming).

| # | Title | Technologies |
|---|--------|--------------|
| 1 | Employee – Department – Project | SQL + MongoDB + PL/SQL |
| 2 | Part – Supplier – Supply (Shipment) | SQL + MongoDB + PL/SQL |
| 3 | Boat – Sailor – Reserves | SQL + MongoDB + PL/SQL |
| 4 | Books – Student – Borrows | SQL + MongoDB + PL/SQL |
| 5 | Patient – Doctor – Appointment | SQL + MongoDB + PL/SQL |

---

## How to Use

1. **Per experiment:** Open `Experiment_N_.../Experiment_N.md` and copy sections into your record book in order (Aim → Theory → ER → SQL → MongoDB → PL/SQL → Queries → Result → Viva).
2. **Interactive manual:** Open `DBMS_Lab_Book.html` in a browser (sidebar navigation for all 5 integrated experiments).
3. **Execution:** Run SQL & PL/SQL in Oracle SQL Developer; run MongoDB scripts in `mongosh` or MongoDB Compass.
4. **Formatting Optimization:**  
   ```powershell
   python tools/upgrade_all_subjects_mobile.py
   ```

---

## Record Book Section Order (Per Experiment)

1. Aim  
2. Problem Statement  
3. Objectives  
4. Theory (SQL & NoSQL Concepts)  
5. Entity Identification  
6. Constraints  
7. ER Diagram (Chen Notation + Mermaid + ASCII)  
8. Schema Diagram  
9. Relational Model  
10. PART A: SQL Implementation (DDL, DML, Queries with expected output)  
11. PART B: MongoDB & PL/SQL Implementation (Collections, queries, and PL/SQL block)  
12. Viva Questions & Answers  
13. Lab Exam Questions  
14. Result  

---

## Diagram Images (for Record Book)

Each experiment folder contains **print-ready PNG figures**:

| File | Description |
|------|-------------|
| `er_diagram.png` | Chen-style ER diagram (entities, relationships, PK/FK) |
| `schema_diagram.png` | Relational schema (tables, keys, FK arrows) |

**Paste in record:** Open the PNG from the experiment folder → paste or glue below the ER DIAGRAM / SCHEMA DIAGRAM headings. Markdown and HTML already embed these images.

---

## Files

- `a:\SEM4_Complete\DBMS_LAB\` — All experiment markdown + diagram PNGs  
- `a:\SEM4_Complete\DBMS_Lab_Book.html` — **Merged manual** (interactive browser viewer with sidebar navigation)  
- `a:\SEM4_Complete\DBMS_LAB\1.html` … `5.html` — Individual experiment HTML pages (source)  
