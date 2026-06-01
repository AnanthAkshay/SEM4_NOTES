# -*- coding: utf-8 -*-
"""Generate DBMS Lab Manual Experiments 7-12 (MongoDB + PL/SQL)."""
import os

BASE = r"a:\SEM4_Complete\DBMS_LAB"


def write_exp(folder, filename, content):
    path = os.path.join(BASE, folder)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, filename), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filename}")


def exp7():
    write_exp(
        "Experiment_7_MongoDB_Employee_Department",
        "Experiment_7.md",
        r"""# EXPERIMENT NUMBER 7

## TITLE
MongoDB Employee and Department + Salary Increment Program

---

## AIM
To design Employee and Department collections in MongoDB, perform document-based queries, and implement a PL/SQL program that awards a 15% salary increment to all employees in a specified department.

---

## PROBLEM STATEMENT
An organization stores workforce data in MongoDB instead of a purely relational store. Each **Department** document contains department number, name, and location. Each **Employee** document contains SSN, name, salary, department reference, and optional project assignments. The system must support listing employees by department name and by project number, and must execute a server-side PL/SQL batch update to increase salaries for a given department.

---

## OBJECTIVES
1. Create and populate MongoDB collections with embedded and referenced data.
2. Execute `find()`, projection, and filtering on nested fields.
3. Write PL/SQL with `UPDATE`, `SQL%ROWCOUNT`, and user feedback messages.

---

## THEORY

### DBMS Concepts Involved
MongoDB is a **document-oriented NoSQL** database. Data is stored as BSON documents inside **collections** (analogous to tables). Unlike rigid relational schemas, documents in the same collection may vary slightly, though lab designs use a consistent structure.

### Entities
| Entity | Storage | Key Fields |
|--------|---------|------------|
| Department | `departments` collection | `dno`, `dname`, `location` |
| Employee | `employees` collection | `ssn`, `name`, `salary`, `dno`, `projects[]` |

### Relationships
- **Employee → Department**: Reference by `dno` (logical foreign key).
- **Employee → Project**: Array of sub-documents `{ pno, hours }` (embedded M:N).

### MongoDB Concepts Used
- `insertOne` / `insertMany` for data loading
- `find` with query filters and projections
- Dot notation for array fields: `projects.pno`

### PL/SQL Concepts Used
- Anonymous PL/SQL block
- `UPDATE` with `WHERE` on department number
- `SQL%ROWCOUNT` to count affected rows
- `DBMS_OUTPUT.PUT_LINE` for messages

---

## ENTITY IDENTIFICATION
| Entity Name | Attributes | Primary Key |
|-------------|------------|-------------|
| Department | dno, dname, location | dno |
| Employee | ssn, name, salary, dno, projects | ssn |

---

## CONSTRAINTS
1. **Domain**: `salary > 0`; `dno` is positive integer.
2. **Entity Integrity**: `ssn` and `dno` must be unique within their collections.
3. **Referential Integrity (Logical)**: Every `employees.dno` must exist in `departments`.
4. **Participation**: Each employee belongs to exactly one department.
5. **Cardinality**: Department 1:N Employee.

---

## ER DIAGRAM

### Mermaid
```mermaid
erDiagram
    DEPARTMENT {
        int dno PK
        string dname
        string location
    }
    EMPLOYEE {
        string ssn PK
        string name
        double salary
        int dno FK
    }
    PROJECT_ASSIGN {
        int pno
        double hours
    }
    DEPARTMENT ||--o{ EMPLOYEE : employs
    EMPLOYEE ||--|{ PROJECT_ASSIGN : works_on
```

### ASCII
```text
  +-------------+ 1     N +------------------+
  | DEPARTMENT  |-------->|    EMPLOYEE      |
  | dno (PK)    |         | ssn (PK)         |
  | dname       |         | name, salary     |
  +-------------+         | dno (FK)         |
                          | projects[]       |
                          +------------------+
```

---

## SCHEMA DIAGRAM
```text
departments( dno PK, dname, location )
employees( ssn PK, name, salary, dno FK, projects[{ pno, hours }] )
```

---

## RELATIONAL MODEL (Oracle mirror for PL/SQL)
```text
DEPARTMENT(DNo, DName, Location)
EMPLOYEE(SSN, Name, Salary, DNo)  -- DNo REFERENCES DEPARTMENT(DNo)
```

---

## SQL IMPLEMENTATION (Oracle tables for PL/SQL)

### CREATE TABLE Statements
```sql
DROP TABLE EMPLOYEE CASCADE CONSTRAINTS;
DROP TABLE DEPARTMENT CASCADE CONSTRAINTS;

CREATE TABLE DEPARTMENT (
    DNo   NUMBER(2) PRIMARY KEY,
    DName VARCHAR2(50) NOT NULL UNIQUE,
    Location VARCHAR2(50) NOT NULL
);

CREATE TABLE EMPLOYEE (
    SSN    CHAR(9) PRIMARY KEY,
    Name   VARCHAR2(50) NOT NULL,
    Salary NUMBER(10,2) CHECK (Salary > 0),
    DNo    NUMBER(2) NOT NULL REFERENCES DEPARTMENT(DNo)
);
```

### INSERT STATEMENTS (10+ records)
```sql
INSERT INTO DEPARTMENT VALUES (1, 'Research', 'Bangalore');
INSERT INTO DEPARTMENT VALUES (2, 'Administration', 'Chennai');
INSERT INTO DEPARTMENT VALUES (3, 'Development', 'Pune');

INSERT INTO EMPLOYEE VALUES ('101', 'Alice Johnson', 80000, 1);
INSERT INTO EMPLOYEE VALUES ('102', 'Bob Smith', 75000, 1);
INSERT INTO EMPLOYEE VALUES ('103', 'Charlie Brown', 60000, 1);
INSERT INTO EMPLOYEE VALUES ('201', 'Diana Prince', 95000, 2);
INSERT INTO EMPLOYEE VALUES ('202', 'Evan Wright', 55000, 2);
INSERT INTO EMPLOYEE VALUES ('301', 'Fiona Gallagher', 110000, 3);
INSERT INTO EMPLOYEE VALUES ('302', 'George Miller', 90000, 3);
INSERT INTO EMPLOYEE VALUES ('303', 'Hannah Abbott', 85000, 3);
INSERT INTO EMPLOYEE VALUES ('304', 'Ian Malcolm', 45000, 3);
INSERT INTO EMPLOYEE VALUES ('305', 'Julia Roberts', 98000, 3);
COMMIT;
```

### DISPLAY TABLE CONTENTS
```sql
SELECT * FROM DEPARTMENT;
SELECT * FROM EMPLOYEE;
```

---

# MONGODB IMPLEMENTATION

## Collection Design
```javascript
// Database: company_db
// Collection: departments
{ "dno": 1, "dname": "Research", "location": "Bangalore" }

// Collection: employees
{
  "ssn": "101",
  "name": "Alice Johnson",
  "salary": 80000,
  "dno": 1,
  "projects": [ { "pno": 12, "hours": 20 } ]
}
```

## Sample Documents – insertMany()
```javascript
use company_db;

db.departments.insertMany([
  { dno: 1, dname: "Research", location: "Bangalore" },
  { dno: 2, dname: "Administration", location: "Chennai" },
  { dno: 3, dname: "Development", location: "Pune" }
]);

db.employees.insertMany([
  { ssn: "101", name: "Alice Johnson", salary: 80000, dno: 1, projects: [{ pno: 12, hours: 20 }] },
  { ssn: "102", name: "Bob Smith", salary: 75000, dno: 1, projects: [{ pno: 12, hours: 40 }] },
  { ssn: "103", name: "Charlie Brown", salary: 60000, dno: 1, projects: [{ pno: 12, hours: 35 }] },
  { ssn: "201", name: "Diana Prince", salary: 95000, dno: 2, projects: [{ pno: 13, hours: 10 }] },
  { ssn: "202", name: "Evan Wright", salary: 55000, dno: 2, projects: [{ pno: 13, hours: 40 }] },
  { ssn: "301", name: "Fiona Gallagher", salary: 110000, dno: 3, projects: [{ pno: 10, hours: 15 }, { pno: 11, hours: 20 }] },
  { ssn: "302", name: "George Miller", salary: 90000, dno: 3, projects: [{ pno: 10, hours: 30 }] },
  { ssn: "303", name: "Hannah Abbott", salary: 85000, dno: 3, projects: [{ pno: 11, hours: 25 }] },
  { ssn: "304", name: "Ian Malcolm", salary: 45000, dno: 3, projects: [{ pno: 14, hours: 45 }] },
  { ssn: "305", name: "Julia Roberts", salary: 98000, dno: 3, projects: [{ pno: 10, hours: 10 }] }
]);
```

## Query 1 – List employees of Department named 'Development'
### Requirement
List all employees belonging to the department whose name is **Development**.

### MongoDB Query
```javascript
var dept = db.departments.findOne({ dname: "Development" });
db.employees.find(
  { dno: dept.dno },
  { _id: 0, ssn: 1, name: 1, salary: 1, dno: 1 }
);
```

### Alternative (aggregation)
```javascript
db.employees.aggregate([
  { $lookup: { from: "departments", localField: "dno", foreignField: "dno", as: "dept" } },
  { $match: { "dept.dname": "Development" } },
  { $project: { _id: 0, ssn: 1, name: 1, salary: 1, dname: { $arrayElemAt: ["$dept.dname", 0] } } }
]);
```

### Expected Output
| ssn | name | salary | dno |
|-----|------|--------|-----|
| 301 | Fiona Gallagher | 110000 | 3 |
| 302 | George Miller | 90000 | 3 |
| 303 | Hannah Abbott | 85000 | 3 |
| 304 | Ian Malcolm | 45000 | 3 |
| 305 | Julia Roberts | 98000 | 3 |

## Query 2 – Employees on Project Number 10
### Requirement
Display names of employees working on project number **10**.

### MongoDB Query
```javascript
db.employees.find(
  { "projects.pno": 10 },
  { _id: 0, name: 1, ssn: 1, projects: 1 }
);
```

### Expected Output
| name | ssn | projects |
|------|-----|----------|
| Fiona Gallagher | 301 | [{pno:10,hours:15},{pno:11,hours:20}] |
| George Miller | 302 | [{pno:10,hours:30}] |
| Julia Roberts | 305 | [{pno:10,hours:10}] |

---

# PL/SQL IMPLEMENTATION

## Complete Program – 15% Pay Increase for Department #3
```sql
SET SERVEROUTPUT ON;

DECLARE
    v_dept_no NUMBER := 3;          -- Department number (Development)
    v_rows    NUMBER;
BEGIN
    UPDATE EMPLOYEE
    SET Salary = Salary * 1.15
    WHERE DNo = v_dept_no;

    v_rows := SQL%ROWCOUNT;

    DBMS_OUTPUT.PUT_LINE('Pay increase of 15% applied to department ' || v_dept_no);
    DBMS_OUTPUT.PUT_LINE('Number of employees updated: ' || v_rows);

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/
```

## Line-by-Line Explanation
| Line | Explanation |
|------|-------------|
| `SET SERVEROUTPUT ON` | Enables message display in SQL Developer |
| `v_dept_no := 3` | Target department for increment |
| `UPDATE ... Salary * 1.15` | Applies 15% increase |
| `SQL%ROWCOUNT` | Returns number of rows updated |
| `COMMIT` | Makes changes permanent |
| `EXCEPTION` block | Rolls back on failure |

## Sample Output
```text
Pay increase of 15% applied to department 3
Number of employees updated: 5
```

---

# MONGODB OUTPUT
```text
> db.employees.find({ "projects.pno": 10 }, { name: 1, _id: 0 })
{ "name": "Fiona Gallagher" }
{ "name": "George Miller" }
{ "name": "Julia Roberts" }
```

---

# OUTPUT SECTION (Oracle SQL Developer style)
```text
SQL> SELECT * FROM EMPLOYEE WHERE DNo = 3;

SSN  NAME              SALARY    DNO
---  ----------------  --------  ---
301  Fiona Gallagher   126500.00  3
302  George Miller     103500.00  3
...
5 rows selected.
```

---

# STEP-BY-STEP EXECUTION
1. Open **MongoDB Compass** or `mongosh` and run `use company_db`.
2. Create `departments` and `employees` collections using `insertMany`.
3. Execute Query 1 and Query 2; verify document counts.
4. Open **Oracle SQL Developer**; run DDL and DML for `DEPARTMENT` and `EMPLOYEE`.
5. Enable `DBMS_OUTPUT`; execute the PL/SQL block for department 3.
6. Run `SELECT * FROM EMPLOYEE WHERE DNo = 3` to verify increased salaries.

---

# VIVA QUESTIONS
1. What is BSON?
2. Difference between SQL and NoSQL databases?
3. What is a collection in MongoDB?
4. What does `insertMany` do?
5. How do you query nested array fields?
6. What is `$lookup` in aggregation?
7. What is `SQL%ROWCOUNT`?
8. Why use PL/SQL instead of a single SQL UPDATE?
9. What is the purpose of `COMMIT`?
10. What is document embedding vs referencing?
11. What is `findOne`?
12. What is projection in MongoDB?
13. What is an anonymous PL/SQL block?
14. How is referential integrity enforced in MongoDB?
15. What is `DBMS_OUTPUT`?

---

# VIVA ANSWERS
1. **BSON** is Binary JSON, MongoDB's internal storage format extending JSON with additional data types.
2. **SQL** uses fixed schemas and tables; **NoSQL** (MongoDB) uses flexible document schemas and horizontal scaling.
3. A **collection** is a grouping of MongoDB documents, similar to a table.
4. **`insertMany`** inserts multiple documents in one operation.
5. Use **dot notation** e.g. `"projects.pno": 10` to match array elements.
6. **`$lookup`** performs a left outer join between collections in an aggregation pipeline.
7. **`SQL%ROWCOUNT`** holds the number of rows affected by the last SQL statement.
8. PL/SQL allows **conditional logic**, error handling, and formatted messages in one block.
9. **`COMMIT`** permanently saves transaction changes.
10. **Embedding** stores related data inside a document; **referencing** stores foreign keys (`dno`) separately.
11. **`findOne`** returns the first matching document or null.
12. **Projection** selects which fields to return: `{ name: 1, _id: 0 }`.
13. An **anonymous block** is PL/SQL code executed once without creating a stored procedure.
14. MongoDB does not enforce FKs by default; applications or schema validation enforce it.
15. **`DBMS_OUTPUT`** is an Oracle package for printing messages from PL/SQL.

---

# FREQUENTLY ASKED LAB EXAM QUESTIONS
1. Write MongoDB query to find employees with salary > 80000.
2. Write PL/SQL to decrease salary by 10% for department 1.
3. How to delete all employees in a department in MongoDB?
4. Write aggregation to count employees per department.
5. What is the difference between `updateOne` and `updateMany`?
6. How to create an index on `employees.dno`?
7. Write SQL join equivalent of `$lookup`.
8. Explain transaction in Oracle PL/SQL.
9. List advantages of MongoDB for unstructured data.
10. Write `find()` with sort and limit.

---

# RESULT
The Employee and Department data was successfully stored in MongoDB and queried by department name and project number. The PL/SQL salary increment program executed correctly and updated five employees in department 3, with the row count displayed through `DBMS_OUTPUT`.
""",
    )


def exp8():
    write_exp(
        "Experiment_8_MongoDB_Patient_Doctor",
        "Experiment_8.md",
        r"""# EXPERIMENT NUMBER 8

## TITLE
MongoDB Patient and Doctor + Consultation Fee Update Program

---

## AIM
To model Patient and Doctor data in MongoDB, execute appointment-based queries, and implement a PL/SQL program that increases consultation fees by 20% for doctors in a given specialization.

---

## PROBLEM STATEMENT
A hospital stores **patients** and **doctors** as MongoDB documents. Appointments link patients to doctors with date and time. The system must list patients treated by a named doctor and patients with appointments on a given date. A PL/SQL program must update consultation fees for all doctors in a specified specialization.

---

## OBJECTIVES
1. Design MongoDB collections with appointment sub-documents or references.
2. Perform filtering on doctor names and appointment dates.
3. Implement PL/SQL bulk update with row count feedback.

---

## THEORY
### DBMS Concepts
- **Entities**: Patient (PID, PName, Age, Gender), Doctor (DID, DName, Specialization, ConsultFee).
- **Relationship**: Appointment (M:N between Patient and Doctor) with Date and Time attributes.
- **MongoDB**: Store appointments as array inside patient document OR separate `appointments` collection.
- **PL/SQL**: `UPDATE` with `WHERE Specialization = ...` and `SQL%ROWCOUNT`.

---

## ENTITY IDENTIFICATION
| Entity | Attributes | Primary Key |
|--------|------------|-------------|
| Patient | pid, pname, age, gender, appointments[] | pid |
| Doctor | did, dname, specialization, consult_fee | did |

---

## CONSTRAINTS
1. Domain: Age > 0; Gender IN ('M','F'); ConsultFee > 0.
2. Entity Integrity: pid, did unique.
3. Referential: appointment.did exists in doctors.
4. Participation: Partial – not all patients need appointments.
5. Cardinality: M:N Patient–Doctor via Appointment.

---

## ER DIAGRAM (Mermaid)
```mermaid
erDiagram
    PATIENT { string pid PK; string pname; int age; char gender }
    DOCTOR { string did PK; string dname; string specialization; double consult_fee }
    APPOINTMENT { date app_date; string app_time; string did FK; string pid FK }
    PATIENT ||--o{ APPOINTMENT : schedules
    DOCTOR ||--o{ APPOINTMENT : conducts
```

---

## MONGODB IMPLEMENTATION

### insertMany – doctors
```javascript
use hospital_db;
db.doctors.insertMany([
  { did: "D101", dname: "Dr. Smith", specialization: "Cardiology", consult_fee: 1500 },
  { did: "D102", dname: "Dr. Strange", specialization: "Neurology", consult_fee: 2000 },
  { did: "D103", dname: "Dr. House", specialization: "Internal Medicine", consult_fee: 1200 },
  { did: "D104", dname: "Dr. Grey", specialization: "Cardiology", consult_fee: 1800 },
  { did: "D105", dname: "Dr. Banner", specialization: "Neurology", consult_fee: 1600 }
]);
```

### insertMany – patients
```javascript
db.patients.insertMany([
  { pid: "P001", pname: "John Doe", age: 45, gender: "M",
    appointments: [
      { did: "D101", dname: "Dr. Smith", app_date: ISODate("2026-06-01"), app_time: "10:00" },
      { did: "D102", dname: "Dr. Strange", app_date: ISODate("2026-06-05"), app_time: "11:30" }
    ]},
  { pid: "P002", pname: "Mary Jane", age: 32, gender: "F",
    appointments: [{ did: "D103", dname: "Dr. House", app_date: ISODate("2026-06-01"), app_time: "09:00" }]},
  { pid: "P003", pname: "Robert Downey", age: 50, gender: "M",
    appointments: [{ did: "D104", dname: "Dr. Grey", app_date: ISODate("2026-06-10"), app_time: "14:00" }]},
  { pid: "P004", pname: "Scarlett Johansson", age: 28, gender: "F", appointments: [] },
  { pid: "P005", pname: "Chris Evans", age: 38, gender: "M",
    appointments: [{ did: "D101", dname: "Dr. Smith", app_date: ISODate("2026-06-01"), app_time: "15:00" }]}
]);
```

### Query i – Patients treated by Dr. Smith
```javascript
db.patients.find(
  { "appointments.dname": "Dr. Smith" },
  { _id: 0, pid: 1, pname: 1, age: 1, gender: 1 }
);
```

### Query ii – Patients with appointment on 2026-06-01
```javascript
db.patients.find(
  { "appointments.app_date": ISODate("2026-06-01") },
  { _id: 0, pname: 1, appointments: 1 }
);
```

---

## SQL IMPLEMENTATION (Oracle for PL/SQL)
```sql
DROP TABLE APPOINTMENT CASCADE CONSTRAINTS;
DROP TABLE PATIENT CASCADE CONSTRAINTS;
DROP TABLE DOCTOR CASCADE CONSTRAINTS;

CREATE TABLE DOCTOR (
    DID VARCHAR2(10) PRIMARY KEY,
    DName VARCHAR2(50) NOT NULL,
    Specialization VARCHAR2(50) NOT NULL,
    ConsultFee NUMBER(8,2) CHECK (ConsultFee > 0)
);

CREATE TABLE PATIENT (
    PID VARCHAR2(10) PRIMARY KEY,
    PName VARCHAR2(50) NOT NULL,
    Age NUMBER(3) CHECK (Age > 0),
    Gender CHAR(1) CHECK (Gender IN ('M','F'))
);

CREATE TABLE APPOINTMENT (
    PID VARCHAR2(10) REFERENCES PATIENT(PID) ON DELETE CASCADE,
    DID VARCHAR2(10) REFERENCES DOCTOR(DID) ON DELETE CASCADE,
    AppDate DATE NOT NULL,
    AppTime VARCHAR2(10),
    PRIMARY KEY (PID, DID, AppDate)
);

INSERT INTO DOCTOR VALUES ('D101','Dr. Smith','Cardiology',1500);
INSERT INTO DOCTOR VALUES ('D102','Dr. Strange','Neurology',2000);
INSERT INTO DOCTOR VALUES ('D103','Dr. House','Internal Medicine',1200);
INSERT INTO DOCTOR VALUES ('D104','Dr. Grey','Cardiology',1800);
INSERT INTO DOCTOR VALUES ('D105','Dr. Banner','Neurology',1600);
-- ... additional inserts for patients and appointments
COMMIT;
```

---

## PL/SQL – 20% Fee Increase for Cardiology
```sql
SET SERVEROUTPUT ON;
DECLARE
    v_spec VARCHAR2(50) := 'Cardiology';
    v_count NUMBER;
BEGIN
    UPDATE DOCTOR
    SET ConsultFee = ConsultFee * 1.20
    WHERE Specialization = v_spec;

    v_count := SQL%ROWCOUNT;
    DBMS_OUTPUT.PUT_LINE('Specialization: ' || v_spec);
    DBMS_OUTPUT.PUT_LINE('Doctors updated: ' || v_count);
    COMMIT;
END;
/
```

### Sample Output
```text
Specialization: Cardiology
Doctors updated: 2
```

---

## MONGODB OUTPUT
```text
{ "pname": "John Doe", "pid": "P001", ... }
{ "pname": "Chris Evans", "pid": "P005", ... }
```

---

## STEP-BY-STEP EXECUTION
1. Create `hospital_db` and insert doctor/patient documents.
2. Run find queries for Dr. Smith and date 2026-06-01.
3. Create Oracle tables; insert matching relational data.
4. Execute PL/SQL fee update; verify with `SELECT * FROM DOCTOR WHERE Specialization='Cardiology'`.

---

## VIVA QUESTIONS
1. How is ISODate used in MongoDB?
2. What is partial participation?
3. Explain M:N mapping in documents.
4. What is SQL%ROWCOUNT?
5. Difference between embedded appointments vs separate collection?
6. How to index appointment dates?
7. What is COMMIT?
8. Write MongoDB updateOne example.
9. What is specialization as domain constraint?
10. How does ON DELETE CASCADE work?
11. What is find() cursor?
12. What is PL/SQL block structure?
13. How to format dates in Oracle?
14. What is aggregation $unwind?
15. Why hospital data may use MongoDB?

---

## VIVA ANSWERS
1. **ISODate** stores UTC dates for reliable date comparisons in queries.
2. **Partial participation**: some patients have zero appointments (optional relationship).
3. **M:N in documents**: duplicate doctor info in patient appointment array or use junction collection.
4. **SQL%ROWCOUNT** returns rows affected by last SQL statement.
5. **Embedded** = faster reads; **separate collection** = normalized, easier updates.
6. `db.patients.createIndex({ "appointments.app_date": 1 })`
7. **COMMIT** saves changes permanently.
8. `db.doctors.updateOne({ did: "D101" }, { $set: { consult_fee: 1600 } })`
9. **Specialization** restricts valid doctor categories (domain/business rule).
10. **ON DELETE CASCADE** removes child rows when parent is deleted.
11. **find()** returns a cursor iterable in mongosh.
12. **DECLARE-BEGIN-EXCEPTION-END** structure.
13. `TO_DATE('2026-06-01','YYYY-MM-DD')` in Oracle.
14. **$unwind** deconstructs array fields into separate documents per element.
15. Flexible schema for varying patient records and nested appointments.

---

## LAB EXAM QUESTIONS
1. List all neurologists in MongoDB.
2. PL/SQL to add flat 500 to all consultation fees.
3. Find patients older than 40 with appointments.
4. Delete appointments on a specific date.
5. Count appointments per doctor using aggregation.
6. Oracle query: patients who consulted Dr. House.
7. Create unique index on pid.
8. updateMany to set gender default.
9. Explain referential integrity in Oracle vs MongoDB.
10. Write exception handler for zero rows updated.

---

## RESULT
Patient and Doctor collections were created in MongoDB and queried successfully. The PL/SQL program increased consultation fees by 20% for Cardiology doctors and reported that 2 doctors were updated.
""",
    )


def exp9():
    write_exp(
        "Experiment_9_MongoDB_Part_Supplier_PLSQL_Backup",
        "Experiment_9.md",
        r"""# EXPERIMENT NUMBER 9

## TITLE
MongoDB Part–Supplier–Shipment + PL/SQL Backup Program

---

## AIM
To manage Part, Supplier, and Shipment data in MongoDB, update part details by PID, list suppliers for a part, and copy Shipment records to a backup table for a specific part using PL/SQL.

---

## PROBLEM STATEMENT
Using the Part–Supplier–Shipment schema, MongoDB stores parts and suppliers with shipment quantities. Operations include updating a part by PID and finding all suppliers for that part. Oracle PL/SQL copies rows from `SHIPMENT` to `SHIPMENT_BACKUP` for a given part number.

---

## OBJECTIVES
1. Implement MongoDB `updateOne` and join-style queries.
2. Use PL/SQL `INSERT INTO ... SELECT` for backup.
3. Understand audit/backup table design.

---

## ENTITY IDENTIFICATION
| Entity | Attributes | PK |
|--------|------------|-----|
| Part | pid, pname, pcolor | pid |
| Supplier | sid, sname, saddr | sid |
| Shipment | sid, pid, qty | (sid, pid) |

---

## MONGODB IMPLEMENTATION
```javascript
use supply_db;
db.parts.insertMany([
  { pid: "P1", pname: "Bolt", pcolor: "Red" },
  { pid: "P2", pname: "Nut", pcolor: "Green" },
  { pid: "P3", pname: "Washer", pcolor: "Red" }
]);
db.suppliers.insertMany([
  { sid: "S1", sname: "Acme Corp", saddr: "Bangalore" },
  { sid: "S2", sname: "Global Parts", saddr: "Mumbai" }
]);
db.shipments.insertMany([
  { sid: "S1", pid: "P1", qty: 100 },
  { sid: "S2", pid: "P1", qty: 50 },
  { sid: "S1", pid: "P2", qty: 200 }
]);
```

### Query i – Update part P1
```javascript
db.parts.updateOne(
  { pid: "P1" },
  { $set: { pname: "Heavy Bolt", pcolor: "Blue" } }
);
```

### Query ii – Suppliers for part P1
```javascript
db.shipments.aggregate([
  { $match: { pid: "P1" } },
  { $lookup: { from: "suppliers", localField: "sid", foreignField: "sid", as: "sup" } },
  { $unwind: "$sup" },
  { $project: { _id: 0, sid: 1, sname: "$sup.sname", qty: 1 } }
]);
```

---

## PL/SQL BACKUP PROGRAM
```sql
DROP TABLE SHIPMENT_BACKUP CASCADE CONSTRAINTS;
DROP TABLE SHIPMENT CASCADE CONSTRAINTS;
DROP TABLE PART CASCADE CONSTRAINTS;
DROP TABLE SUPPLIER CASCADE CONSTRAINTS;

CREATE TABLE SUPPLIER (
    SID CHAR(3) PRIMARY KEY,
    SName VARCHAR2(50) NOT NULL,
    SAddr VARCHAR2(100)
);
CREATE TABLE PART (
    PID CHAR(3) PRIMARY KEY,
    PName VARCHAR2(50) NOT NULL,
    PColor VARCHAR2(20)
);
CREATE TABLE SHIPMENT (
    SID CHAR(3) REFERENCES SUPPLIER(SID),
    PID CHAR(3) REFERENCES PART(PID),
    Qty NUMBER(6) CHECK (Qty > 0),
    PRIMARY KEY (SID, PID)
);
CREATE TABLE SHIPMENT_BACKUP (
    SID CHAR(3),
    PID CHAR(3),
    Qty NUMBER(6),
    BackupDate DATE DEFAULT SYSDATE,
    PRIMARY KEY (SID, PID, BackupDate)
);

-- Insert sample data (10+ rows across tables) ...

SET SERVEROUTPUT ON;
DECLARE
    v_pid PART.PID%TYPE := 'P1';
    v_rows NUMBER;
BEGIN
    INSERT INTO SHIPMENT_BACKUP (SID, PID, Qty, BackupDate)
    SELECT SID, PID, Qty, SYSDATE
    FROM SHIPMENT
    WHERE PID = v_pid;

    v_rows := SQL%ROWCOUNT;
    DBMS_OUTPUT.PUT_LINE('Backup completed for part ' || v_pid);
    DBMS_OUTPUT.PUT_LINE('Rows copied: ' || v_rows);
    COMMIT;
END;
/
```

---

## STEP-BY-STEP EXECUTION
1. Load MongoDB collections; run updateOne and aggregation.
2. Create Oracle tables and insert shipments.
3. Run PL/SQL backup block; verify `SELECT * FROM SHIPMENT_BACKUP`.

---

## VIVA QUESTIONS (15) & ANSWERS
1. **Q:** What is `$lookup`? **A:** Joins another collection in aggregation.
2. **Q:** Purpose of backup table? **A:** Preserves historical shipment data before changes/deletes.
3. **Q:** `INSERT SELECT`? **A:** Copies rows from one table to another in one statement.
4. **Q:** Composite key in SHIPMENT? **A:** (SID, PID) uniquely identifies supplier-part pair.
5. **Q:** updateOne vs updateMany? **A:** updateOne changes first match; updateMany changes all matches.
6–15. (Referential integrity, CASCADE, Qty domain, audit columns, SYSDATE, etc.)

---

## LAB EXAM QUESTIONS
1. Backup all shipments using PL/SQL.
2. MongoDB delete shipments for Red parts.
3. Find total qty per part.
4. List parts not supplied by any supplier.
5–10. Additional join and backup variants.

---

## RESULT
Part details were updated in MongoDB; suppliers for part P1 were retrieved. PL/SQL successfully copied shipment rows to SHIPMENT_BACKUP for the specified part number.
""",
    )


def exp10():
    write_exp(
        "Experiment_10_MongoDB_Boat_Sailor_Weekend_Trigger",
        "Experiment_10.md",
        r"""# EXPERIMENT NUMBER 10

## TITLE
MongoDB Boat–Sailor + Weekend Modification Trigger

---

## AIM
To query boat reservations in MongoDB and create an Oracle trigger on EMPLOYEE that blocks INSERT/UPDATE/DELETE on weekends.

---

## PROBLEM STATEMENT
Sailors reserve boats (RESERVES). MongoDB answers: count of boats reserved by a sailor, and boats of a given color. Oracle trigger on EMPLOYEE(SSN, Name, Sal, DeptNo) must raise an error when the table is modified on Saturday or Sunday.

---

## MONGODB IMPLEMENTATION
```javascript
use marina_db;
db.boats.insertMany([
  { bid: 101, bname: "Interlake", color: "Blue" },
  { bid: 102, bname: "Clipper", color: "Red" },
  { bid: 103, bname: "Marlin", color: "Green" }
]);
db.sailors.insertMany([
  { sid: 22, sname: "Dustin", rating: 7, age: 45 },
  { sid: 31, sname: "Lubber", rating: 8, age: 55 },
  { sid: 44, sname: "Horatio", rating: 7, age: 35 }
]);
db.reserves.insertMany([
  { sid: 22, bid: 101, day: ISODate("2026-06-02") },
  { sid: 22, bid: 102, day: ISODate("2026-06-03") },
  { sid: 31, bid: 103, day: ISODate("2026-06-04") },
  { sid: 44, bid: 101, day: ISODate("2026-06-05") }
]);
```

### i – Boats reserved by Dustin
```javascript
var s = db.sailors.findOne({ sname: "Dustin" });
db.reserves.countDocuments({ sid: s.sid });
// Alternative: aggregate with lookup
```

### ii – Boats of color Red
```javascript
db.boats.find({ color: "Red" }, { _id: 0 });
```

---

## TRIGGER PROGRAMS

### Trigger Definition
A **BEFORE** row trigger on `EMPLOYEE` for `INSERT OR UPDATE OR DELETE` checks `TO_CHAR(SYSDATE,'DY')` and raises application error on weekend.

### Complete Trigger Code
```sql
CREATE OR REPLACE TRIGGER trg_emp_weekend_block
BEFORE INSERT OR UPDATE OR DELETE ON EMPLOYEE
FOR EACH ROW
DECLARE
    v_day VARCHAR2(3);
BEGIN
    v_day := UPPER(TO_CHAR(SYSDATE, 'DY', 'NLS_DATE_LANGUAGE=AMERICAN'));
    IF v_day IN ('SAT', 'SUN') THEN
        RAISE_APPLICATION_ERROR(-20001,
            'Modification of EMPLOYEE table is not allowed on weekends (Saturday/Sunday).');
    END IF;
END;
/
```

### Test Queries
```sql
-- Run on weekday: should succeed
INSERT INTO EMPLOYEE VALUES ('999','Test User',50000,1);

-- Simulate weekend (exam discussion): trigger uses SYSDATE
-- On Saturday/Sunday: ORA-20001 error
```

### Expected Output (Weekend)
```text
ORA-20001: Modification of EMPLOYEE table is not allowed on weekends (Saturday/Sunday).
```

---

## STEP-BY-STEP EXECUTION
1. Insert boats, sailors, reserves in MongoDB.
2. Run count and color queries.
3. Create EMPLOYEE table and weekend trigger in Oracle.
4. Test INSERT on weekday vs weekend.

---

## VIVA QUESTIONS & ANSWERS (15 each – key topics)
Row vs statement triggers; BEFORE vs AFTER; RAISE_APPLICATION_ERROR; TO_CHAR day codes; MongoDB countDocuments; aggregate pipeline for sailor-boat join.

---

## RESULT
MongoDB queries returned reservation counts and boat colors correctly. The weekend trigger prevented EMPLOYEE modifications on Saturday and Sunday.
""",
    )


def exp11():
    write_exp(
        "Experiment_11_MongoDB_Customer_Branch_Cursor",
        "Experiment_11.md",
        r"""# EXPERIMENT NUMBER 11

## TITLE
MongoDB Customer–Branch + Cursor Table Copy Program

---

## AIM
To query banking data in MongoDB and demonstrate copying table contents from one Oracle table to another using explicit cursors.

---

## MONGODB IMPLEMENTATION
```javascript
use bank_db;
db.branches.insertMany([
  { branch_id: "B001", branch_name: "MG Road", city: "Bangalore", assets: 5000000 },
  { branch_id: "B002", branch_name: "Park Street", city: "Kolkata", assets: 3200000 }
]);
db.customers.insertMany([
  { cust_id: "C001", cust_name: "Ravi Kumar", city: "Bangalore",
    accounts: [{ acc_no: "A1001", branch_id: "B001", type: "Savings" },
               { acc_no: "A1002", branch_id: "B001", type: "Current" }] },
  { cust_id: "C002", cust_name: "Priya Shah", city: "Pune",
    accounts: [{ acc_no: "A2001", branch_id: "B002", type: "Savings" }] }
]);
```

### i – Branch name for B001
```javascript
db.branches.findOne({ branch_id: "B001" }, { _id: 0, branch_name: 1 });
```

### ii – Total accounts per customer
```javascript
db.customers.aggregate([
  { $project: { cust_name: 1, total_accounts: { $size: "$accounts" } } }
]);
```

---

## CURSOR PROGRAMS
```sql
DROP TABLE ACCOUNT_COPY CASCADE CONSTRAINTS;
DROP TABLE ACCOUNT CASCADE CONSTRAINTS;
-- Assume ACCOUNT(AccNo, BranchName, Balance, AccType) exists with data

CREATE TABLE ACCOUNT_COPY AS SELECT * FROM ACCOUNT WHERE 1=0;

SET SERVEROUTPUT ON;
DECLARE
    CURSOR cur_account IS
        SELECT AccNo, BranchName, Balance, AccType FROM ACCOUNT;
    v_rec cur_account%ROWTYPE;
    v_count NUMBER := 0;
BEGIN
    OPEN cur_account;
    LOOP
        FETCH cur_account INTO v_rec;
        EXIT WHEN cur_account%NOTFOUND;
        INSERT INTO ACCOUNT_COPY VALUES (v_rec.AccNo, v_rec.BranchName, v_rec.Balance, v_rec.AccType);
        v_count := v_count + 1;
    END LOOP;
    CLOSE cur_account;
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Rows copied: ' || v_count);
END;
/
```

### Cursor Steps Explained
1. **DECLARE CURSOR** – defines SELECT for iteration
2. **OPEN** – executes query, prepares result set
3. **FETCH** – retrieves next row into %ROWTYPE record
4. **CLOSE** – releases cursor resources

---

## RESULT
Branch lookup and account counts worked in MongoDB. Cursor program copied all rows from ACCOUNT to ACCOUNT_COPY with row count displayed.
""",
    )


def exp12():
    write_exp(
        "Experiment_12_MongoDB_Books_Student_Exception",
        "Experiment_12.md",
        r"""# EXPERIMENT NUMBER 12

## TITLE
MongoDB Books–Student + User Defined Exception Program

---

## AIM
To query library data in MongoDB and write a PL/SQL program that accepts two numbers and raises user-defined exception `e_bigger` when the first is larger than the second.

---

## MONGODB IMPLEMENTATION
```javascript
use library_db;
db.books.insertMany([
  { isbn: "123", title: "Database Systems", author: "Korth", publisher: "McGraw" },
  { isbn: "124", title: "Advanced DBMS", author: "Elmasri", publisher: "Pearson" },
  { isbn: "125", title: "Operating Systems", author: "Silberschatz", publisher: "Wiley" }
]);
db.students.insertMany([
  { sid: "S01", sname: "Anita", gender: "F",
    borrows: [{ isbn: "123", bdate: ISODate("2026-05-01") }] },
  { sid: "S02", sname: "Rahul", gender: "M",
    borrows: [{ isbn: "124", bdate: ISODate("2026-05-02") }] },
  { sid: "S03", sname: "Meera", gender: "F",
    borrows: [{ isbn: "123", bdate: ISODate("2026-05-03") }, { isbn: "125", bdate: ISODate("2026-05-04") }] }
]);
```

### i – Books by author Korth
```javascript
db.books.find({ author: "Korth" }, { _id: 0 });
```

### ii – Students who borrowed Database books
```javascript
db.students.find(
  { "borrows.isbn": { $in: ["123", "124"] } },
  { _id: 0, sname: 1, gender: 1 }
);
// Or match title via lookup
```

---

## EXCEPTION HANDLING

### Complete Program
```sql
SET SERVEROUTPUT ON;
DECLARE
    e_bigger EXCEPTION;
    PRAGMA EXCEPTION_INIT(e_bigger, -20010);
    num1 NUMBER := &num1;
    num2 NUMBER := &num2;
BEGIN
    IF num1 > num2 THEN
        RAISE e_bigger;
    END IF;
    DBMS_OUTPUT.PUT_LINE('First number is not larger. Sum = ' || (num1 + num2));
EXCEPTION
    WHEN e_bigger THEN
        DBMS_OUTPUT.PUT_LINE('Error: First number is larger than second number.');
END;
/
```

### Alternative (explicit code)
```sql
DECLARE
    e_bigger EXCEPTION;
BEGIN
    IF num1 > num2 THEN
        RAISE_APPLICATION_ERROR(-20010, 'First number is larger than second number.');
    END IF;
END;
/
```

### Sample Output
```text
Enter num1: 50
Enter num2: 20
Error: First number is larger than second number.
```

---

## RESULT
MongoDB returned books by author and students who borrowed database-related ISBNs. The user-defined exception program correctly raised `e_bigger` when the first number exceeded the second.
""",
    )


if __name__ == "__main__":
    exp7()
    exp8()
    exp9()
    exp10()
    exp11()
    exp12()
    print("All experiments 7-12 generated.")
