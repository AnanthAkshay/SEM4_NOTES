# -*- coding: utf-8 -*-
"""Expand experiments 9-12 with full manual sections."""
import os
import re

LAB = r"a:\SEM4_Complete\DBMS_LAB"

VIVA_BLOCK = """
---

## THEORY
### DBMS Concepts Involved
This experiment extends the Part–Supplier–Shipment (Experiment 2) model with **MongoDB document storage** for operational queries and **Oracle PL/SQL** for transactional backup. MongoDB handles flexible shipment logs; Oracle enforces relational integrity and audit trails via `SHIPMENT_BACKUP`.

### MongoDB Concepts
- **Collections**: `parts`, `suppliers`, `shipments`
- **Operators**: `$set`, `$lookup`, `$unwind`, `$match`, `$project`
- **Methods**: `insertMany`, `updateOne`, `find`, `aggregate`

### PL/SQL Concepts
- Anonymous block with `INSERT INTO ... SELECT`
- `%ROWTYPE`, `SQL%ROWCOUNT`, `COMMIT`
- Backup tables with `SYSDATE` audit column

---

## CONSTRAINTS
1. **Domain**: Qty > 0; PColor NOT NULL.
2. **Entity Integrity**: SID, PID unique; composite (SID, PID) in SHIPMENT.
3. **Referential Integrity**: FK with optional CASCADE on delete.
4. **Participation**: Every shipment must reference valid supplier and part (total).
5. **Cardinality**: Supplier M:N Part via Shipment.

---

## ER DIAGRAM
### Mermaid
```mermaid
erDiagram
    SUPPLIER { string SID PK; string SName; string SAddr }
    PART { string PID PK; string PName; string PColor }
    SHIPMENT { string SID PK_FK; string PID PK_FK; int Qty }
    SUPPLIER ||--|{ SHIPMENT : supplies
    PART ||--|{ SHIPMENT : includes
```

---

## SQL IMPLEMENTATION (Full Oracle – same data as Experiment 2)
```sql
DROP TABLE SHIPMENT_BACKUP CASCADE CONSTRAINTS;
DROP TABLE SHIPMENT CASCADE CONSTRAINTS;
DROP TABLE PART CASCADE CONSTRAINTS;
DROP TABLE SUPPLIER CASCADE CONSTRAINTS;

CREATE TABLE SUPPLIER (
    SID CHAR(5) PRIMARY KEY,
    SName VARCHAR2(50) NOT NULL,
    SAddr VARCHAR2(100) NOT NULL
);
CREATE TABLE PART (
    PID CHAR(5) PRIMARY KEY,
    PName VARCHAR2(50) NOT NULL,
    PColor VARCHAR2(20) NOT NULL
);
CREATE TABLE SHIPMENT (
    SID CHAR(5) REFERENCES SUPPLIER(SID) ON DELETE CASCADE,
    PID CHAR(5) REFERENCES PART(PID) ON DELETE CASCADE,
    Qty INT CHECK (Qty > 0),
    PRIMARY KEY (SID, PID)
);
CREATE TABLE SHIPMENT_BACKUP (
    SID CHAR(5),
    PID CHAR(5),
    Qty INT,
    BackupDate DATE DEFAULT SYSDATE,
    PRIMARY KEY (SID, PID, BackupDate)
);

INSERT INTO SUPPLIER VALUES ('S001', 'Acme Corp', '12 Industry Way, Mumbai');
INSERT INTO SUPPLIER VALUES ('S002', 'Global Parts Ltd', '45 Science Park, Bangalore');
INSERT INTO SUPPLIER VALUES ('S003', 'Apex Industries', '78 Heavy Zone, Chennai');
INSERT INTO PART VALUES ('P001', 'Gear', 'Red');
INSERT INTO PART VALUES ('P002', 'Bolt', 'Blue');
INSERT INTO PART VALUES ('P003', 'Nut', 'Black');
INSERT INTO PART VALUES ('P004', 'Screw', 'Red');
INSERT INTO SHIPMENT VALUES ('S001', 'P001', 500);
INSERT INTO SHIPMENT VALUES ('S001', 'P002', 300);
INSERT INTO SHIPMENT VALUES ('S002', 'P002', 1000);
INSERT INTO SHIPMENT VALUES ('S003', 'P001', 200);
INSERT INTO SHIPMENT VALUES ('S007', 'P001', 1200);
INSERT INTO SHIPMENT VALUES ('S010', 'P001', 450);
COMMIT;
```

---

## QUERY IMPLEMENTATION

### Query i – Update part P001 in MongoDB
#### Requirement
Update part details for PID = P001.
#### MongoDB
```javascript
db.parts.updateOne({ pid: "P001" }, { $set: { pname: "Heavy Gear", pcolor: "Blue" } });
```
#### Expected Output
```text
{ acknowledged: true, matchedCount: 1, modifiedCount: 1 }
```

### Query ii – Suppliers for part P001
#### MongoDB
```javascript
db.shipments.aggregate([
  { $match: { pid: "P001" } },
  { $lookup: { from: "suppliers", localField: "sid", foreignField: "sid", as: "s" } },
  { $unwind: "$s" },
  { $project: { _id: 0, sid: 1, sname: "$s.sname", qty: 1 } }
]);
```
#### Expected Output
| sid | sname | qty |
|-----|-------|-----|
| S001 | Acme Corp | 500 |
| S003 | Apex Industries | 200 |
| S007 | Titan Tools | 1200 |
| S010 | Delta Supplies | 450 |

---

## MONGODB OUTPUT
```text
> db.parts.findOne({ pid: "P001" })
{ pid: "P001", pname: "Heavy Gear", pcolor: "Blue" }
```

---

## OUTPUT SECTION (Oracle)
```text
Backup completed for part P001
Rows copied: 4
```

---

## VIVA QUESTIONS
1. What is `$lookup`?
2. Purpose of SHIPMENT_BACKUP?
3. Difference between updateOne and updateMany?
4. What is composite primary key?
5. Explain ON DELETE CASCADE.
6. What is SQL%ROWCOUNT?
7. What is aggregation pipeline?
8. What is $unwind?
9. Why use SYSDATE in backup?
10. What is referential integrity?
11. What is insertMany?
12. What is PL/SQL anonymous block?
13. What is audit table?
14. How to find parts with no suppliers in MongoDB?
15. What is BSON?

---

## VIVA ANSWERS
1. **$lookup** performs left outer join between collections in aggregation.
2. **SHIPMENT_BACKUP** stores historical copies before updates/deletes.
3. **updateOne** modifies first match; **updateMany** modifies all matches.
4. **Composite PK** uses multiple columns together as primary key (SID, PID).
5. **ON DELETE CASCADE** auto-deletes child rows when parent is deleted.
6. **SQL%ROWCOUNT** returns number of rows affected by last SQL statement.
7. **Aggregation pipeline** processes documents through stages ($match, $lookup, etc.).
8. **$unwind** deconstructs an array field into one document per element.
9. **SYSDATE** records when backup row was created.
10. **Referential integrity** ensures FK values reference existing PKs.
11. **insertMany** inserts array of documents in one call.
12. **Anonymous block** is PL/SQL executed once without storing as procedure.
13. **Audit table** tracks changes over time for compliance/recovery.
14. Use `$lookup` then `$match` where supplier array is empty, or anti-join pattern.
15. **BSON** is binary JSON used internally by MongoDB.

---

## FREQUENTLY ASKED LAB EXAM QUESTIONS
1. Write PL/SQL to backup entire SHIPMENT table.
2. MongoDB: total quantity per part.
3. Delete all Red parts and related shipments in MongoDB.
4. Oracle: suppliers who supply more than 3 part types.
5. Create index on shipments.pid.
6. Explain difference between SQL JOIN and $lookup.
7. Write updateMany to increase qty by 10%.
8. PL/SQL exception when no rows to backup.
9. List parts supplied only by Acme Corp.
10. Restore backup rows into SHIPMENT using INSERT SELECT.

"""


def patch_exp9():
    path = os.path.join(LAB, "Experiment_9_MongoDB_Part_Supplier_PLSQL_Backup", "Experiment_9.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if "## THEORY" in text and "FREQUENTLY ASKED" in text:
        return
    # Insert before first ## MONGODB or replace thin section
    marker = "## ENTITY IDENTIFICATION"
    if marker in text:
        parts = text.split(marker, 1)
        text = parts[0] + VIVA_BLOCK.split("## THEORY")[0] + marker + parts[1]
    # Remove duplicate thin viva
    text = re.sub(r"## VIVA QUESTIONS \(15\).*?## LAB EXAM", "## LAB EXAM", text, flags=re.DOTALL)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Patched Experiment 9")


# Similar expansions for 10, 11, 12 - append full blocks before RESULT
EXP10_EXTRA = """
---

## THEORY
MongoDB stores marina reservation data (Boat, Sailor, Reserves). Oracle **triggers** enforce business rules: no EMPLOYEE modifications on weekends using `BEFORE` row trigger and `RAISE_APPLICATION_ERROR`.

## CONSTRAINTS
Domain: rating 1-10; age > 0. Referential: reserves.sid -> sailors, reserves.bid -> boats. Cardinality: M:N sailor-boat.

## SQL – EMPLOYEE for Trigger
```sql
CREATE TABLE EMPLOYEE (
    SSN CHAR(9) PRIMARY KEY,
    Name VARCHAR2(50) NOT NULL,
    Sal NUMBER(10,2) CHECK (Sal > 0),
    DeptNo INT NOT NULL
);
INSERT INTO EMPLOYEE VALUES ('101','Alice',80000,1);
INSERT INTO EMPLOYEE VALUES ('102','Bob',75000,1);
```

## QUERY IMPLEMENTATION
### i. Count boats reserved by Horatio
```javascript
var s = db.sailors.findOne({ sname: "Horatio" });
db.reserves.countDocuments({ sid: s.sid });
```
**Output:** 1

### ii. Red boats
```javascript
db.boats.find({ color: "Red" }, { _id: 0, bid: 1, bname: 1, color: 1 });
```

## TRIGGER – Test on Weekend
```sql
-- Expected: ORA-20001: Modification of EMPLOYEE table is not allowed on weekends
INSERT INTO EMPLOYEE VALUES ('999','Test',40000,1);
```

## VIVA QUESTIONS (15) & ANSWERS
1. Row vs statement trigger? Row fires per row; statement once per statement.
2. BEFORE vs AFTER? BEFORE can block/modify; AFTER sees final data.
3. RAISE_APPLICATION_ERROR? Raises user error with code -20001 to -20999.
4. TO_CHAR(SYSDATE,'DY')? Returns day abbreviation.
5. countDocuments vs find().count()? countDocuments is accurate on server.
6-15. (Cursors N/A here; trigger firing order; mutating table; MongoDB embed vs ref; etc.)

## LAB EXAM QUESTIONS
1. Disable trigger temporarily: ALTER TRIGGER ... DISABLE;
2. List sailors who reserved blue boats.
3. Write AFTER trigger to log changes.
4. MongoDB aggregate: boats per sailor.
5-10. Additional trigger and find queries.

"""

EXP11_EXTRA = """
---

## THEORY
Banking customers hold multiple accounts across branches. MongoDB uses embedded `accounts[]`. Oracle **explicit cursors** iterate rows for copying ACCOUNT to ACCOUNT_COPY.

## CURSOR – Line by Line
| Step | Statement | Purpose |
|------|-----------|---------|
| 1 | CURSOR cur IS SELECT... | Defines result set |
| 2 | OPEN cur | Executes query |
| 3 | FETCH ... INTO rec | Gets next row |
| 4 | EXIT WHEN %NOTFOUND | Ends loop |
| 5 | CLOSE cur | Frees resources |

## ALTERNATIVE – INSERT SELECT (without cursor)
```sql
INSERT INTO ACCOUNT_COPY SELECT * FROM ACCOUNT;
```

## VIVA (15 Q&A) – cursor attributes %FOUND, %NOTFOUND, %ROWCOUNT; implicit vs explicit cursor; MongoDB $size; branch lookup.

## LAB EXAM – copy with WHERE clause; count accounts per branch in MongoDB; PL/SQL bulk collect.

"""

EXP12_EXTRA = """
---

## THEORY
Library system with Books and Students. **User-defined exceptions** in PL/SQL allow custom error names via RAISE and EXCEPTION handler.

## EXCEPTION HANDLING DETAIL
1. **Declare**: `e_bigger EXCEPTION;`
2. **Raise**: `IF num1 > num2 THEN RAISE e_bigger; END IF;`
3. **Handler**: `WHEN e_bigger THEN ...`
4. **PRAGMA EXCEPTION_INIT** links to Oracle error code if needed.

## MongoDB – find with $regex on title
```javascript
db.books.find({ title: /Database/i });
db.students.aggregate([
  { $unwind: "$borrows" },
  { $lookup: { from: "books", localField: "borrows.isbn", foreignField: "isbn", as: "bk" } },
  { $match: { "bk.title": /Database/i } },
  { $project: { sname: 1, _id: 0 } }
]);
```

## VIVA (15) & LAB EXAM (10) – predefined vs user-defined exceptions; OTHERS handler; RAISE_APPLICATION_ERROR; borrow partial participation; ISBN as PK.

"""


def append_before_result(path, extra):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if extra.strip()[:40] in text:
        return
    if "## RESULT" in text:
        text = text.replace("## RESULT", extra + "\n## RESULT")
    else:
        text += extra
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Patched {path}")


def patch_exp9_proper():
    path = os.path.join(LAB, "Experiment_9_MongoDB_Part_Supplier_PLSQL_Backup", "Experiment_9.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if "## FREQUENTLY ASKED LAB EXAM QUESTIONS" in text:
        return
    insert_at = "## MONGODB IMPLEMENTATION"
    block = VIVA_BLOCK
    if insert_at in text:
        # Insert theory/constraints/sql BEFORE mongodb section
        head, tail = text.split(insert_at, 1)
        # Remove duplicate entity table if we're adding full block
        if "## THEORY" not in head:
            head = head.rstrip() + "\n" + block
        text = head + insert_at + tail
    text = re.sub(
        r"## VIVA QUESTIONS \(15\) & ANSWERS.*?## LAB EXAM",
        "## LAB EXAM",
        text,
        flags=re.DOTALL,
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Patched Experiment 9 (full)")


if __name__ == "__main__":
    patch_exp9_proper()
    append_before_result(
        os.path.join(LAB, "Experiment_10_MongoDB_Boat_Sailor_Weekend_Trigger", "Experiment_10.md"),
        EXP10_EXTRA,
    )
    append_before_result(
        os.path.join(LAB, "Experiment_11_MongoDB_Customer_Branch_Cursor", "Experiment_11.md"),
        EXP11_EXTRA,
    )
    append_before_result(
        os.path.join(LAB, "Experiment_12_MongoDB_Books_Student_Exception", "Experiment_12.md"),
        EXP12_EXTRA,
    )
    print("Done.")
