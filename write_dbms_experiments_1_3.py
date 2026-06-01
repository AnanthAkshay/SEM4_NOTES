import os

def create_experiment_1():
    content = """# EXPERIMENT NUMBER 1

## TITLE
Employee – Department – Project Database

---

## AIM
To design, implement, and query an Employee-Department-Project database schema using Oracle SQL, including ER mapping, constraint enforcement, and multi-table joins.

---

## PROBLEM STATEMENT
An organization needs a database to manage its workforce, departments, and projects. 
* Each employee is uniquely identified by a Social Security Number (SSN) and has a Name, Address, Gender, and Salary.
* A department has a unique Department Number (DNo), a name (DName), and is managed by an employee (Manager) with a specific manager start date. 
* A project is identified by a unique Project Number (PNo) and has a Name, Location, Domain (e.g., Database, Cloud), and is controlled by a single department.
* Employees can work on multiple projects, with a specific number of hours allocated for each. An employee may also have a supervisor (another employee).
Develop a relational database system to represent this scenario and write Oracle SQL queries to perform operational queries.

---

## OBJECTIVES
1. Learn relational database modeling and schema definition using SQL DDL commands.
2. Implement primary keys, foreign keys, check constraints, and referential integrity.
3. Master multi-table joins, aggregation (`GROUP BY`), and table updates.

---

## THEORY
### DBMS Concepts Involved
A Relational Database Management System (RDBMS) stores data in tables (relations) consisting of rows (tuples) and columns (attributes). In this schema, we represent the standard employee-department-project architecture:
* **Entities**: `EMPLOYEE` (strong entity), `DEPARTMENT` (strong entity), and `PROJECT` (strong entity).
* **Relationships**:
  * **Works_In** (Employee to Department): Many-to-One (N:1) relationship. An employee belongs to one department; a department contains many employees.
  * **Manages** (Employee to Department): One-to-One (1:1) relationship. An employee manages at most one department.
  * **Controls** (Department to Project): One-to-Many (1:N) relationship. A department controls multiple projects.
  * **Works_On** (Employee to Project): Many-to-Many (M:N) relationship. An employee can work on multiple projects, and a project can have multiple employees. The attribute `Hours` belongs to this relationship.
  * **Supervises** (Employee to Employee): Unary/Recursive One-to-Many (1:N) relationship. An employee can supervise multiple employees, but an employee has at most one supervisor.

### Constraints
1. **Entity Integrity**: Primary keys must be unique and non-null (e.g., `SSN` in `EMPLOYEE`, `DNo` in `DEPARTMENT`).
2. **Referential Integrity**: Foreign keys must match a primary key in the referenced table or be null (e.g., `DNo` in `EMPLOYEE` referencing `DNo` in `DEPARTMENT`).
3. **Domain Constraints**: Attribute values must lie within valid ranges (e.g., `Sex` must be 'M' or 'F', `Salary` must be positive).

---

## ENTITY IDENTIFICATION
| Entity Name | Attributes | Primary Key | Foreign Key(s) |
|---|---|---|---|
| **EMPLOYEE** | SSN, Name, Address, Sex, Salary, SuperSSN, DNo | SSN | SuperSSN (refs EMPLOYEE), DNo (refs DEPARTMENT) |
| **DEPARTMENT** | DNo, DName, MgrSSN, MgrStartDate | DNo | MgrSSN (refs EMPLOYEE) |
| **PROJECT** | PNo, PName, PLocation, Domain, DNo | PNo | DNo (refs DEPARTMENT) |
| **WORKS_ON** | SSN, PNo, Hours | (SSN, PNo) | SSN (refs EMPLOYEE), PNo (refs PROJECT) |

---

## CONSTRAINTS
* **Domain Constraints**:
  * `Sex` in `EMPLOYEE`: `CHECK (Sex IN ('M', 'F'))`
  * `Salary` in `EMPLOYEE`: `CHECK (Salary > 0)`
  * `Hours` in `WORKS_ON`: `CHECK (Hours > 0)`
* **Participation Constraints**:
  * Every department must have a manager (total participation).
  * Every employee must belong to a department (total participation, modeled by `DNo NOT NULL`).
* **Cardinality Ratios**:
  * Employee to Department: N:1
  * Employee to Employee (Supervisor): N:1
  * Department to Project: 1:N
  * Employee to Project: M:N

---

## ER DIAGRAM
### Mermaid Notation
```mermaid
erDiagram
    EMPLOYEE {
        string SSN PK
        string Name
        string Address
        char Sex
        double Salary
        string SuperSSN FK
        int DNo FK
    }
    DEPARTMENT {
        int DNo PK
        string DName
        string MgrSSN FK
        date MgrStartDate
    }
    PROJECT {
        int PNo PK
        string PName
        string PLocation
        string Domain
        int DNo FK
    }
    WORKS_ON {
        string SSN PK, FK
        int PNo PK, FK
        double Hours
    }

    EMPLOYEE }o--o| EMPLOYEE : "supervises"
    EMPLOYEE }|--|| DEPARTMENT : "works_in"
    EMPLOYEE |o--o| DEPARTMENT : "manages"
    DEPARTMENT ||--o{ PROJECT : "controls"
    EMPLOYEE ||--|{ WORKS_ON : "works"
    PROJECT ||--|{ WORKS_ON : "includes"
```

### ASCII Diagram
```text
  +------------------+                    +------------------+
  |     EMPLOYEE     |1                  1|    DEPARTMENT    |
  |------------------|------------------->|------------------|
  | SSN (PK)         |   (Works_In)       | DNo (PK)         |
  | Name, Address    |                    | DName            |
  | Sex, Salary      |                    | MgrSSN (FK)      |
  | SuperSSN (FK)    |                    | MgrStartDate     |
  | DNo (FK)         |                    +------------------+
  +------------------+                             |
         | ^                                       |
         | | (Supervises)                          |1
         +-+                                       |
          N                                        v N (Controls)
  +------------------+                    +------------------+
  |     WORKS_ON     |                    |     PROJECT      |
  |------------------|                    |------------------|
  | SSN (PK, FK)     |N                  1| PNo (PK)         |
  | PNo (PK, FK)     |<-------------------| PName, PLocation |
  | Hours            |    (Works_On)      | Domain           |
  +------------------+                    | DNo (FK)         |
                                          +------------------+
```

---

## SCHEMA DIAGRAM
* **EMPLOYEE** ( [SSN] (PK), Name, Address, Sex, Salary, SuperSSN (FK), DNo (FK) )
* **DEPARTMENT** ( [DNo] (PK), DName, MgrSSN (FK), MgrStartDate )
* **PROJECT** ( [PNo] (PK), PName, PLocation, Domain, DNo (FK) )
* **WORKS_ON** ( [SSN] (PK, FK), [PNo] (PK, FK), Hours )

---

## RELATIONAL MODEL
* The **EMPLOYEE** relation has `SSN` as the primary key. `DNo` is a foreign key referencing `DEPARTMENT(DNo)`, and `SuperSSN` is a self-referencing foreign key referencing `EMPLOYEE(SSN)`.
* The **DEPARTMENT** relation has `DNo` as the primary key. `MgrSSN` is a foreign key referencing `EMPLOYEE(SSN)`.
* The **PROJECT** relation has `PNo` as the primary key. `DNo` is a foreign key referencing `DEPARTMENT(DNo)`.
* The **WORKS_ON** relation has a composite primary key `(SSN, PNo)`. `SSN` references `EMPLOYEE(SSN)` and `PNo` references `PROJECT(PNo)`.

---

## SQL IMPLEMENTATION
```sql
-- Dropping existing tables to ensure clean execution
DROP TABLE WORKS_ON CASCADE CONSTRAINTS;
DROP TABLE PROJECT CASCADE CONSTRAINTS;
DROP TABLE EMPLOYEE CASCADE CONSTRAINTS;
DROP TABLE DEPARTMENT CASCADE CONSTRAINTS;

-- 1. Create Department table (without foreign key to Employee first)
CREATE TABLE DEPARTMENT (
    DNo INT PRIMARY KEY,
    DName VARCHAR2(50) NOT NULL,
    MgrSSN CHAR(9),
    MgrStartDate DATE
);

-- 2. Create Employee table
CREATE TABLE EMPLOYEE (
    SSN CHAR(9) PRIMARY KEY,
    Name VARCHAR2(50) NOT NULL,
    Address VARCHAR2(100),
    Sex CHAR(1) CHECK (Sex IN ('M', 'F')),
    Salary NUMBER(10,2) CHECK (Salary > 0),
    SuperSSN CHAR(9) REFERENCES EMPLOYEE(SSN),
    DNo INT REFERENCES DEPARTMENT(DNo)
);

-- 3. Add foreign key from Department to Employee (for MgrSSN)
ALTER TABLE DEPARTMENT ADD CONSTRAINT fk_dept_mgr FOREIGN KEY (MgrSSN) REFERENCES EMPLOYEE(SSN);

-- 4. Create Project table
CREATE TABLE PROJECT (
    PNo INT PRIMARY KEY,
    PName VARCHAR2(50) NOT NULL,
    PLocation VARCHAR2(50),
    Domain VARCHAR2(30),
    DNo INT REFERENCES DEPARTMENT(DNo)
);

-- 5. Create Works_On table
CREATE TABLE WORKS_ON (
    SSN CHAR(9) REFERENCES EMPLOYEE(SSN) ON DELETE CASCADE,
    PNo INT REFERENCES PROJECT(PNo) ON DELETE CASCADE,
    Hours NUMBER(4,1) CHECK (Hours > 0),
    PRIMARY KEY (SSN, PNo)
);

-- Inserting Data
-- Insert Departments first (temporarily leaving MgrSSN as NULL)
INSERT INTO DEPARTMENT VALUES (1, 'Research', NULL, TO_DATE('2025-01-01', 'YYYY-MM-DD'));
INSERT INTO DEPARTMENT VALUES (2, 'Administration', NULL, TO_DATE('2025-02-15', 'YYYY-MM-DD'));
INSERT INTO DEPARTMENT VALUES (3, 'Development', NULL, TO_DATE('2025-03-20', 'YYYY-MM-DD'));

-- Insert Employees
-- Research Dept
INSERT INTO EMPLOYEE VALUES ('101', 'Alice Johnson', '123 Pine St, Bangalore', 'F', 80000, NULL, 1);
INSERT INTO EMPLOYEE VALUES ('102', 'Bob Smith', '456 Oak Rd, Bangalore', 'M', 75000, '101', 1);
INSERT INTO EMPLOYEE VALUES ('103', 'Charlie Brown', '789 Maple Dr, Mumbai', 'M', 60000, '101', 1);

-- Admin Dept
INSERT INTO EMPLOYEE VALUES ('201', 'Diana Prince', '101 Segway Ave, Chennai', 'F', 95000, NULL, 2);
INSERT INTO EMPLOYEE VALUES ('202', 'Evan Wright', '202 Lincoln Rd, Chennai', 'M', 55000, '201', 2);

-- Dev Dept
INSERT INTO EMPLOYEE VALUES ('301', 'Fiona Gallagher', '303 Sunset Blvd, Pune', 'F', 110000, NULL, 3);
INSERT INTO EMPLOYEE VALUES ('302', 'George Miller', '404 Forest Ave, Pune', 'M', 90000, '301', 3);
INSERT INTO EMPLOYEE VALUES ('303', 'Hannah Abbott', '505 Ridge Rd, Bangalore', 'F', 85000, '301', 3);
INSERT INTO EMPLOYEE VALUES ('304', 'Ian Malcolm', '606 Chaos St, Pune', 'M', 45000, '302', 3);
INSERT INTO EMPLOYEE VALUES ('305', 'Julia Roberts', '707 Hollywood Blvd, Bangalore', 'F', 98000, '301', 3);

-- Update Department Manager SSNs
UPDATE DEPARTMENT SET MgrSSN = '101' WHERE DNo = 1;
UPDATE DEPARTMENT SET MgrSSN = '201' WHERE DNo = 2;
UPDATE DEPARTMENT SET MgrSSN = '301' WHERE DNo = 3;

-- Insert Projects
INSERT INTO PROJECT VALUES (10, 'Database Migration', 'Bangalore', 'Database', 3);
INSERT INTO PROJECT VALUES (11, 'Cloud Infrastructure', 'Pune', 'Cloud', 3);
INSERT INTO PROJECT VALUES (12, 'Big Data Analysis', 'Bangalore', 'Database', 1);
INSERT INTO PROJECT VALUES (13, 'HR Portal', 'Chennai', 'Web', 2);
INSERT INTO PROJECT VALUES (14, 'AI Chatbot', 'Bangalore', 'AI', 3);

-- Insert Works_On relationships
INSERT INTO WORKS_ON VALUES ('101', 12, 20.0);
INSERT INTO WORKS_ON VALUES ('102', 12, 40.0);
INSERT INTO WORKS_ON VALUES ('103', 12, 35.0);
INSERT INTO WORKS_ON VALUES ('201', 13, 10.0);
INSERT INTO WORKS_ON VALUES ('202', 13, 40.0);
INSERT INTO WORKS_ON VALUES ('301', 10, 15.0);
INSERT INTO WORKS_ON VALUES ('301', 11, 20.0);
INSERT INTO WORKS_ON VALUES ('301', 14, 10.0);
INSERT INTO WORKS_ON VALUES ('302', 10, 30.0);
INSERT INTO WORKS_ON VALUES ('302', 11, 10.0);
INSERT INTO WORKS_ON VALUES ('303', 10, 40.0);
INSERT INTO WORKS_ON VALUES ('304', 14, 45.0);
INSERT INTO WORKS_ON VALUES ('305', 10, 25.0);
```

---

## QUERY IMPLEMENTATION
### i. Obtain the details of employees assigned to “Database” project.
#### SQL:
```sql
SELECT DISTINCT E.SSN, E.Name, E.Address, E.Sex, E.Salary, E.DNo 
FROM EMPLOYEE E
JOIN WORKS_ON W ON E.SSN = W.SSN
JOIN PROJECT P ON W.PNo = P.PNo
WHERE P.Domain = 'Database' OR P.PName LIKE '%Database%';
```
#### Explanation:
We join the `EMPLOYEE`, `WORKS_ON`, and `PROJECT` tables using the common keys `SSN` and `PNo`. Then, we apply a filter on the `Domain` or `PName` columns of the `PROJECT` table to match the string "Database".
#### Expected Output:
| SSN | Name | Address | Sex | Salary | DNo |
|---|---|---|---|---|---|
| 101 | Alice Johnson | 123 Pine St, Bangalore | F | 80000 | 1 |
| 102 | Bob Smith | 456 Oak Rd, Bangalore | M | 75000 | 1 |
| 103 | Charlie Brown | 789 Maple Dr, Mumbai | M | 60000 | 1 |
| 301 | Fiona Gallagher | 303 Sunset Blvd, Pune | F | 110000 | 3 |
| 302 | George Miller | 404 Forest Ave, Pune | M | 90000 | 3 |
| 303 | Hannah Abbott | 505 Ridge Rd, Bangalore | F | 85000 | 3 |
| 305 | Julia Roberts | 707 Hollywood Blvd, Bangalore | F | 98000 | 3 |

---

### ii. Find the number of employees working in each department with department details.
#### SQL:
```sql
SELECT D.DNo, D.DName, COUNT(E.SSN) AS Number_of_Employees, AVG(E.Salary) AS Average_Salary
FROM DEPARTMENT D
LEFT JOIN EMPLOYEE E ON D.DNo = E.DNo
GROUP BY D.DNo, D.DName
ORDER BY D.DNo;
```
#### Explanation:
We perform a `LEFT JOIN` between `DEPARTMENT` and `EMPLOYEE` on `DNo` so that even departments with no employees are included in the result. We use the `GROUP BY` clause on the department details and use `COUNT(E.SSN)` to calculate the size of the workforce.
#### Expected Output:
| DNo | DName | Number_of_Employees | Average_Salary |
|---|---|---|---|
| 1 | Research | 3 | 71666.67 |
| 2 | Administration | 2 | 75000.00 |
| 3 | Development | 5 | 85600.00 |

---

### iii. Update the Project details of Employee bearing SSN = '304' to ProjectNo = 10 and display the same.
#### SQL:
```sql
-- Step 1: Update the record in WORKS_ON
UPDATE WORKS_ON 
SET PNo = 10 
WHERE SSN = '304' AND PNo = 14;

-- Step 2: Select to display updated record
SELECT E.SSN, E.Name, W.PNo, P.PName, W.Hours
FROM EMPLOYEE E
JOIN WORKS_ON W ON E.SSN = W.SSN
JOIN PROJECT P ON W.PNo = P.PNo
WHERE E.SSN = '304';
```
#### Explanation:
The `UPDATE` statement targets the `WORKS_ON` table, changing the `PNo` value from its previous project (14) to 10 for the employee whose `SSN` is '304'. We join the tables back to display the changed project assignments.
#### Expected Output:
| SSN | Name | PNo | PName | Hours |
|---|---|---|---|---|
| 304 | Ian Malcolm | 10 | Database Migration | 45 |

---

## VIVA QUESTIONS & ANSWERS
1. **Q:** What is the difference between a primary key and a unique key?
   * **A:** A table can have only one Primary Key, which cannot accept NULL values. It can have multiple Unique Keys, which can accept NULL values.
2. **Q:** What is a foreign key?
   * **A:** A foreign key is a column or set of columns in one table that references the primary key of another table to maintain referential integrity.
3. **Q:** What is the recursive relationship in the Employee table?
   * **A:** The supervisor-supervisee relationship, modeled by `SuperSSN` referencing `SSN` in the same table.
4. **Q:** What does `ON DELETE CASCADE` do?
   * **A:** When a referenced row in the parent table is deleted, all matching rows in the child table are automatically deleted.
5. **Q:** Why did we add the MgrSSN constraint using `ALTER TABLE` instead of directly in `CREATE TABLE`?
   * **A:** To avoid a circular dependency deadlock, as `EMPLOYEE` references `DEPARTMENT` and `DEPARTMENT` references `EMPLOYEE`.
6. **Q:** What is a composite primary key?
   * **A:** A primary key consisting of more than one column (e.g., `(SSN, PNo)` in `WORKS_ON`).
7. **Q:** What is the difference between `CHAR` and `VARCHAR2`?
   * **A:** `CHAR` is fixed-length, padding empty spaces, while `VARCHAR2` is variable-length and space-efficient.
8. **Q:** What are aggregate functions?
   * **A:** Functions like `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX` that operate on a set of values to return a single summary value.
9. **Q:** When do we use the `HAVING` clause?
   * **A:** To filter groups created by the `GROUP BY` clause. It cannot be used without `GROUP BY` (conceptually).
10. **Q:** What is the default join type in SQL?
    * **A:** An `INNER JOIN`.
11. **Q:** What is the purpose of the `CHECK` constraint?
    * **A:** To restrict the range of values that can be placed in a column (e.g., checking `Sex` or `Salary`).
12. **Q:** What is a schema?
    * **A:** A logical description of the database structure, tables, columns, data types, and constraints.
13. **Q:** What is a candidate key?
    * **A:** A column or group of columns that can uniquely identify a row in a table. The primary key is chosen from the candidate keys.
14. **Q:** What does `SELECT DISTINCT` do?
    * **A:** It removes duplicate rows from the query result set.
15. **Q:** What is referential integrity?
    * **A:** A rule stating that every foreign key value must either point to a valid primary key value or be NULL.

---

## LAB EXAM QUESTIONS
1. Write a query to find the names of employees who do not manage any department.
2. List the names of all employees who have no supervisor.
3. Write a query to display the manager name and department name for all departments.
4. Retrieve the project names controlled by the 'Development' department.
5. List the employees working more than 30 hours on any project.
6. Display the department details with the maximum average salary.
7. Retrieve employees whose names start with 'A'.
8. Find the total hours spent on all projects controlled by department 3.
9. Write a query to display employee details who work on more than two projects.
10. Delete the project 'AI Chatbot' and verify the changes in the `WORKS_ON` table.

---

## RESULT
The Employee-Department-Project database was successfully designed, implemented with all integrity constraints, populated with data, and verified by running the multi-table join and update queries.
"""
    os.makedirs(r'a:\SEM4_Complete\DBMS_LAB\Experiment_1_Employee_Department_Project', exist_ok=True)
    with open(r'a:\SEM4_Complete\DBMS_LAB\Experiment_1_Employee_Department_Project\Experiment_1.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Experiment 1 Generated!")

def create_experiment_2():
    content = """# EXPERIMENT NUMBER 2

## TITLE
Part – Supplier – Supply Database

---

## AIM
To design, implement, and query a Part-Supplier-Shipment database schema using Oracle SQL, including entity constraints, relationship management, and cascading delete operations.

---

## PROBLEM STATEMENT
A logistics tracking system needs to maintain information about suppliers, parts, and shipments:
* Each supplier is described by a unique Supplier ID (SID), Supplier Name (SName), and Address (SAddr).
* Each part has a unique Part ID (PID), Part Name (PName), and Color (PColor).
* The shipment table (Shipment/Supply) tracks the quantity (Qty) of a specific part supplied by a specific supplier.
Establish a relational database for this schema, enforce all key and reference constraints, and perform the following database operations:
i. Obtain the details of parts supplied by a specific supplier #SNAME.
ii. Obtain the names of suppliers who supply a specific part #PNAME.
iii. Delete parts of a specific color #PCOLOR and observe cascading effects.

---

## OBJECTIVES
1. Master relational modeling of M:N relationships using an intersection table (`SHIPMENT`).
2. Implement primary keys, foreign keys, and cascading delete operations (`ON DELETE CASCADE`).
3. Formulate SQL queries utilizing joins, string comparisons, and deletion tasks.

---

## THEORY
### DBMS Concepts Involved
This database models a supply chain database system containing two primary master tables and one mapping table:
* **Entities**:
  * `SUPPLIER`: Holds master information about suppliers.
  * `PART`: Holds master information about components/parts.
* **Relationship**:
  * `SHIPMENT` (Supply): An M:N relationship linking `SUPPLIER` and `PART` with an attribute `Qty` (Quantity). Each supplier can ship multiple parts, and each part can be shipped by multiple suppliers.

### ON DELETE CASCADE Constraint
When deleting a record from a master table (like `PART`), if there are references to it in a transaction table (like `SHIPMENT`), the database engine will reject the delete command by default to protect referential integrity.
By specifying `ON DELETE CASCADE` on the foreign key:
* If a `PART` (e.g., PID = 'P1') is deleted, the database automatically deletes all rows in `SHIPMENT` where `PID` = 'P1'.
* This prevents orphaned records in the `SHIPMENT` table.

---

## ENTITY IDENTIFICATION
| Entity Name | Attributes | Primary Key | Foreign Key(s) |
|---|---|---|---|
| **SUPPLIER** | SID, SName, SAddr | SID | None |
| **PART** | PID, PName, PColor | PID | None |
| **SHIPMENT** | SID, PID, Qty | (SID, PID) | SID (refs SUPPLIER), PID (refs PART) |

---

## CONSTRAINTS
* **Domain Constraints**:
  * `Qty` in `SHIPMENT`: `CHECK (Qty > 0)`
  * `PColor` in `PART`: `NOT NULL`
* **Referential Constraints**:
  * `SHIPMENT(SID)` references `SUPPLIER(SID)` with `ON DELETE CASCADE`
  * `SHIPMENT(PID)` references `PART(PID)` with `ON DELETE CASCADE`

---

## ER DIAGRAM
### Mermaid Notation
```mermaid
erDiagram
    SUPPLIER {
        string SID PK
        string SName
        string SAddr
    }
    PART {
        string PID PK
        string PName
        string PColor
    }
    SHIPMENT {
        string SID PK, FK
        string PID PK, FK
        int Qty
    }

    SUPPLIER ||--|{ SHIPMENT : "supplies"
    PART ||--|{ SHIPMENT : "shipped_via"
```

### ASCII Diagram
```text
  +------------------+                   +------------------+
  |     SUPPLIER     |1                 1|       PART       |
  |------------------|                   |------------------|
  | SID (PK)         |                   | PID (PK)         |
  | SName, SAddr     |                   | PName, PColor    |
  +------------------+                   +------------------+
          |                                       |
          |1                                      |1
          |           +------------------+        |
          |           |     SHIPMENT     |        |
          +---------->|------------------|<-------+
           (supplies) | SID (PK, FK)     | (shipped_via)
                     N| PID (PK, FK)     |N
                      | Qty              |
                      +------------------+
```

---

## SCHEMA DIAGRAM
* **SUPPLIER** ( [SID] (PK), SName, SAddr )
* **PART** ( [PID] (PK), PName, PColor )
* **SHIPMENT** ( [SID] (PK, FK1), [PID] (PK, FK2), Qty )

---

## RELATIONAL MODEL
* **SUPPLIER**: `SID` uniquely identifies a supplier.
* **PART**: `PID` uniquely identifies a part.
* **SHIPMENT**: The key is `(SID, PID)`. `SID` references `SUPPLIER(SID)` and `PID` references `PART(PID)`. Both have cascade delete rules enabled.

---

## SQL IMPLEMENTATION
```sql
-- Dropping tables to ensure clean runs
DROP TABLE SHIPMENT CASCADE CONSTRAINTS;
DROP TABLE PART CASCADE CONSTRAINTS;
DROP TABLE SUPPLIER CASCADE CONSTRAINTS;

-- 1. Create Supplier table
CREATE TABLE SUPPLIER (
    SID CHAR(5) PRIMARY KEY,
    SName VARCHAR2(50) NOT NULL,
    SAddr VARCHAR2(100) NOT NULL
);

-- 2. Create Part table
CREATE TABLE PART (
    PID CHAR(5) PRIMARY KEY,
    PName VARCHAR2(50) NOT NULL,
    PColor VARCHAR2(20) NOT NULL
);

-- 3. Create Shipment table with cascading deletes
CREATE TABLE SHIPMENT (
    SID CHAR(5) REFERENCES SUPPLIER(SID) ON DELETE CASCADE,
    PID CHAR(5) REFERENCES PART(PID) ON DELETE CASCADE,
    Qty INT CHECK (Qty > 0),
    PRIMARY KEY (SID, PID)
);

-- Inserting Supplier Records (10+ records)
INSERT INTO SUPPLIER VALUES ('S001', 'Acme Corp', '12 Industry Way, Mumbai');
INSERT INTO SUPPLIER VALUES ('S002', 'Global Parts Ltd', '45 Science Park, Bangalore');
INSERT INTO SUPPLIER VALUES ('S003', 'Apex Industries', '78 Heavy Zone, Chennai');
INSERT INTO SUPPLIER VALUES ('S004', 'Zenith Supply', '99 Metro St, Delhi');
INSERT INTO SUPPLIER VALUES ('S005', 'Matrix Logistical', '101 Cyber Link, Hyderabad');
INSERT INTO SUPPLIER VALUES ('S006', 'Vortex Manufacturing', '505 Ring Rd, Pune');
INSERT INTO SUPPLIER VALUES ('S007', 'Titan Tools', '88 Factory Lane, Bangalore');
INSERT INTO SUPPLIER VALUES ('S008', 'Alpha Distributing', '14 Ocean Blvd, Cochin');
INSERT INTO SUPPLIER VALUES ('S009', 'Prime Logistics', '27 Highway Ave, Kolkata');
INSERT INTO SUPPLIER VALUES ('S010', 'Delta Supplies', '40 Park St, Noida');

-- Inserting Part Records (10+ records)
INSERT INTO PART VALUES ('P001', 'Gear', 'Red');
INSERT INTO PART VALUES ('P002', 'Bolt', 'Blue');
INSERT INTO PART VALUES ('P003', 'Nut', 'Black');
INSERT INTO PART VALUES ('P004', 'Screw', 'Red');
INSERT INTO PART VALUES ('P005', 'Washer', 'Silver');
INSERT INTO PART VALUES ('P006', 'Bracket', 'Black');
INSERT INTO PART VALUES ('P007', 'Pin', 'Silver');
INSERT INTO PART VALUES ('P008', 'Shaft', 'Blue');
INSERT INTO PART VALUES ('P009', 'Valve', 'Green');
INSERT INTO PART VALUES ('P010', 'Spring', 'Silver');

-- Inserting Shipment Records (12+ records)
INSERT INTO SHIPMENT VALUES ('S001', 'P001', 500);
INSERT INTO SHIPMENT VALUES ('S001', 'P002', 300);
INSERT INTO SHIPMENT VALUES ('S002', 'P002', 1000);
INSERT INTO SHIPMENT VALUES ('S002', 'P003', 1500);
INSERT INTO SHIPMENT VALUES ('S003', 'P001', 200);
INSERT INTO SHIPMENT VALUES ('S003', 'P004', 800);
INSERT INTO SHIPMENT VALUES ('S004', 'P005', 2500);
INSERT INTO SHIPMENT VALUES ('S005', 'P006', 400);
INSERT INTO SHIPMENT VALUES ('S006', 'P007', 600);
INSERT INTO SHIPMENT VALUES ('S007', 'P001', 1200);
INSERT INTO SHIPMENT VALUES ('S007', 'P008', 350);
INSERT INTO SHIPMENT VALUES ('S008', 'P009', 100);
INSERT INTO SHIPMENT VALUES ('S009', 'P010', 900);
INSERT INTO SHIPMENT VALUES ('S010', 'P001', 450);
INSERT INTO SHIPMENT VALUES ('S010', 'P004', 600);
```

---

## QUERY IMPLEMENTATION
### i. Obtain the details of parts supplied by supplier 'Acme Corp'.
#### SQL:
```sql
SELECT P.PID, P.PName, P.PColor, S.Qty 
FROM PART P
JOIN SHIPMENT S ON P.PID = S.PID
JOIN SUPPLIER SU ON S.SID = SU.SID
WHERE SU.SName = 'Acme Corp';
```
#### Explanation:
We perform an inner join between `PART`, `SHIPMENT`, and `SUPPLIER` using their primary/foreign key connections (`PID` and `SID`). Then we filter the records where the supplier's name is 'Acme Corp' and display the parts.
#### Expected Output:
| PID | PName | PColor | Qty |
|---|---|---|---|
| P001 | Gear | Red | 500 |
| P002 | Bolt | Blue | 300 |

---

### ii. Obtain the Names of suppliers who supply 'Gear'.
#### SQL:
```sql
SELECT DISTINCT SU.SName, SU.SAddr
FROM SUPPLIER SU
JOIN SHIPMENT S ON SU.SID = S.SID
JOIN PART P ON S.PID = P.PID
WHERE P.PName = 'Gear';
```
#### Explanation:
By joining `SUPPLIER`, `SHIPMENT`, and `PART`, we filter the joined tuples for part names matching 'Gear'. We project only the supplier's name and address.
#### Expected Output:
| SName | SAddr |
|---|---|
| Acme Corp | 12 Industry Way, Mumbai |
| Apex Industries | 78 Heavy Zone, Chennai |
| Titan Tools | 88 Factory Lane, Bangalore |
| Delta Supplies | 40 Park St, Noida |

---

### iii. Delete the parts which are in 'Red'.
#### SQL:
```sql
-- Check shipments before deletion
SELECT * FROM SHIPMENT WHERE PID IN (SELECT PID FROM PART WHERE PColor = 'Red');

-- Perform deletion
DELETE FROM PART WHERE PColor = 'Red';

-- Verify shipments after deletion (should be empty due to CASCADE)
SELECT * FROM SHIPMENT WHERE PID IN (SELECT PID FROM PART WHERE PColor = 'Red');

-- Verify Part Table
SELECT * FROM PART;
```
#### Explanation:
First, we observe which shipments exist for Red parts ('P001', 'P004'). When we issue the `DELETE` query against `PART` where the color is 'Red', the database engine automatically fires cascades, deleting those related records in the `SHIPMENT` table.
#### Expected Output (Verification):
`0 rows selected` from shipment verification query, confirming Cascade Delete worked successfully.
Part table listing:
| PID | PName | PColor |
|---|---|---|
| P002 | Bolt | Blue |
| P003 | Nut | Black |
| P005 | Washer | Silver |
| P006 | Bracket | Black |
| P007 | Pin | Silver |
| P008 | Shaft | Blue |
| P009 | Valve | Green |
| P010 | Spring | Silver |

---

## VIVA QUESTIONS & ANSWERS
1. **Q:** What is the relational database term for a row and a column?
   * **A:** A row is called a "tuple" and a column is called an "attribute".
2. **Q:** What is the difference between `DELETE` and `TRUNCATE`?
   * **A:** `DELETE` is a DML command that can be rolled back and deletes rows based on conditions, firing triggers. `TRUNCATE` is a DDL command that deallocates data pages, is faster, cannot have a WHERE clause, and doesn't fire delete triggers.
3. **Q:** What is referential integrity?
   * **A:** It requires that any foreign key column value must match an existing primary key value in the parent table.
4. **Q:** What are the alternatives to `ON DELETE CASCADE`?
   * **A:** `ON DELETE SET NULL` (sets the foreign key columns to NULL) and `RESTRICT`/`NO ACTION` (rejects the delete operation).
5. **Q:** What is a composite key?
   * **A:** A key that consists of two or more attributes to uniquely identify a record.
6. **Q:** How do we write a pattern matching query in SQL?
   * **A:** Using the `LIKE` operator along with wildcards `%` (zero or more characters) and `_` (exactly one character).
7. **Q:** Can a foreign key reference a non-primary key?
   * **A:** Yes, but it must reference a column that has a `UNIQUE` constraint on it.
8. **Q:** What is the difference between `INNER JOIN` and `OUTER JOIN`?
   * **A:** `INNER JOIN` returns rows with matching values in both tables. `OUTER JOIN` returns matching rows plus unmatched rows from one or both tables (Left, Right, or Full).
9. **Q:** What are the properties of a transaction (ACID)?
   * **A:** Atomicity, Consistency, Isolation, and Durability.
10. **Q:** What is a natural join?
    * **A:** A join that joins tables based on columns with the same name and data type in both tables.
11. **Q:** What is the purpose of the `COMMIT` statement?
    * **A:** It permanently saves all database changes made during the current transaction.
12. **Q:** What is the role of a database catalog?
    * **A:** It store metadata containing details about the structures, files, relationships, and constraints of the database.
13. **Q:** Can we have duplicate records in a table with a primary key?
    * **A:** No, primary keys guarantee row uniqueness.
14. **Q:** What is the use of the `IN` operator?
    * **A:** It allows checking if a value matches any value in a specified list or subquery.
15. **Q:** What does `CASCADE` mean?
    * **A:** It means the change (delete or update) propagates dynamically to all dependent tables.

---

## LAB EXAM QUESTIONS
1. Write a query to find the total quantity of all parts shipped by supplier 'S001'.
2. List the names of suppliers who do not supply any parts.
3. Find the part with the maximum quantity shipped in a single order.
4. Display suppliers who reside in 'Bangalore'.
5. Obtain the number of parts supplied of each color.
6. Display part details that have never been shipped.
7. Write a query to increase shipment quantity by 10% for supplier 'S002' and part 'P002'.
8. Find suppliers who supply more than 2 parts.
9. List the details of parts whose colors are either Red or Blue.
10. Show how to drop the foreign key constraint on the `SHIPMENT` table.

---

## RESULT
The Part-Supplier-Shipment database was successfully created, populated with 10+ records, and verified. Deleting red parts successfully triggered cascading deletes in the shipment table as expected.
"""
    os.makedirs(r'a:\SEM4_Complete\DBMS_LAB\Experiment_2_Part_Supplier_Supply', exist_ok=True)
    with open(r'a:\SEM4_Complete\DBMS_LAB\Experiment_2_Part_Supplier_Supply\Experiment_2.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Experiment 2 Generated!")

def create_experiment_3():
    content = """# EXPERIMENT NUMBER 3

## TITLE
Boat – Sailor – Reserves Database

---

## AIM
To design, implement, and query a Boat-Sailor-Reserves schema using Oracle SQL, and perform relational division queries, reserves calculations, and group aggregations.

---

## PROBLEM STATEMENT
A yacht club needs a database to keep track of its operations:
* Each sailor has a unique Sailor ID (SID), Name (SName), Rating (an integer representing skill), and Age.
* Each boat is identified by a unique Boat ID (BID), Boat Name (BName), and Color.
* The reservation system (Reserves) logs reservations by recording which sailor (SID) reserved which boat (BID) on which Day (Date).
Establish a relational database, apply constraints, and write SQL queries to:
i. Obtain the details of boats reserved by a specific sailor #Sailor_Name.
ii. Retrieve the BID of boats that have been reserved by ALL sailors (Relational Division).
iii. Find the total number of boats reserved by each sailor, displaying the sailor's name with their reservation count.

---

## OBJECTIVES
1. Implement M:N relationships containing composite primary keys and date columns.
2. Master the concept of **Relational Division** in SQL using double `NOT EXISTS` or `MINUS` set operations.
3. Use aggregation (`GROUP BY` and `COUNT`) with `LEFT JOIN` to avoid omitting sailors with zero reservations.

---

## THEORY
### DBMS Concepts Involved
This schema manages yacht rental activities.
* **Entities**:
  * `SAILOR`: Strong entity storing member information (rating, age).
  * `BOAT`: Strong entity storing fleet data.
* **Relationships**:
  * `RESERVES`: Many-to-Many mapping table recording date-stamped boat rentals.

### Relational Division
Relational division (R ÷ S) is a relational algebra operation that finds values in one relation that are associated with all values in another relation. In SQL, there is no direct `DIVIDE BY` operator. Instead, we implement it using:
1. **Double Negation (Double NOT EXISTS)**: "Find boats where there does not exist a sailor for whom there does not exist a reservation of this boat."
2. **Set Differences (MINUS)**: "Find boats where the set of all sailors MINUS the set of sailors who reserved this boat is empty."

---

## ENTITY IDENTIFICATION
| Entity Name | Attributes | Primary Key | Foreign Key(s) |
|---|---|---|---|
| **SAILOR** | SID, SName, Rating, Age | SID | None |
| **BOAT** | BID, BName, Color | BID | None |
| **RESERVES** | SID, BID, Day | (SID, BID, Day) | SID (refs SAILOR), BID (refs BOAT) |

---

## CONSTRAINTS
* **Domain Constraints**:
  * `Rating` in `SAILOR`: `CHECK (Rating BETWEEN 1 AND 10)`
  * `Age` in `SAILOR`: `CHECK (Age > 0)`
* **Key Constraints**:
  * The primary key of `RESERVES` is `(SID, BID, Day)` to allow the same sailor to reserve the same boat on different days.

---

## ER DIAGRAM
### Mermaid Notation
```mermaid
erDiagram
    SAILOR {
        int SID PK
        string SName
        int Rating
        int Age
    }
    BOAT {
        int BID PK
        string BName
        string Color
    }
    RESERVES {
        int SID PK, FK
        int BID PK, FK
        date Day PK
    }

    SAILOR ||--|{ RESERVES : "reserves"
    BOAT ||--|{ RESERVES : "reserved_by"
```

### ASCII Diagram
```text
  +------------------+                   +------------------+
  |      SAILOR      |1                 1|       BOAT       |
  |------------------|                   |------------------|
  | SID (PK)         |                   | BID (PK)         |
  | SName, Rating    |                   | BName, Color     |
  | Age              |                   +------------------+
  +------------------+                            |
           |                                      |
           |1                                     |1
           |           +------------------+       |
           |           |     RESERVES     |       |
           +---------->|------------------|<------+
            (reserves) | SID (PK, FK)     | (reserved_by)
                      N| BID (PK, FK)     |N
                       | Day (PK)         |
                       +------------------+
```

---

## SCHEMA DIAGRAM
* **SAILOR** ( [SID] (PK), SName, Rating, Age )
* **BOAT** ( [BID] (PK), BName, Color )
* **RESERVES** ( [SID] (PK, FK1), [BID] (PK, FK2), [Day] (PK) )

---

## RELATIONAL MODEL
* **SAILOR**: Primary key is `SID`.
* **BOAT**: Primary key is `BID`.
* **RESERVES**: Composite primary key `(SID, BID, Day)`. If `Day` is not part of the primary key, a sailor could only reserve a specific boat once in the entire system history.

---

## SQL IMPLEMENTATION
```sql
-- Dropping tables to ensure clean runs
DROP TABLE RESERVES CASCADE CONSTRAINTS;
DROP TABLE BOAT CASCADE CONSTRAINTS;
DROP TABLE SAILOR CASCADE CONSTRAINTS;

-- 1. Create Sailor table
CREATE TABLE SAILOR (
    SID INT PRIMARY KEY,
    SName VARCHAR2(50) NOT NULL,
    Rating INT CHECK (Rating BETWEEN 1 AND 10),
    Age INT CHECK (Age > 0)
);

-- 2. Create Boat table
CREATE TABLE BOAT (
    BID INT PRIMARY KEY,
    BName VARCHAR2(50) NOT NULL,
    Color VARCHAR2(20) NOT NULL
);

-- 3. Create Reserves table
CREATE TABLE RESERVES (
    SID INT REFERENCES SAILOR(SID) ON DELETE CASCADE,
    BID INT REFERENCES BOAT(BID) ON DELETE CASCADE,
    Day DATE,
    PRIMARY KEY (SID, BID, Day)
);

-- Inserting Sailor Records (10+ records)
INSERT INTO SAILOR VALUES (1001, 'Dustin', 7, 45);
INSERT INTO SAILOR VALUES (1002, 'Brutus', 1, 33);
INSERT INTO SAILOR VALUES (1003, 'Lubber', 8, 55);
INSERT INTO SAILOR VALUES (1004, 'Andy', 8, 25);
INSERT INTO SAILOR VALUES (1005, 'Rusty', 10, 35);
INSERT INTO SAILOR VALUES (1006, 'Horatio', 7, 16);
INSERT INTO SAILOR VALUES (1007, 'Zorba', 10, 16);
INSERT INTO SAILOR VALUES (1008, 'Art', 3, 25);
INSERT INTO SAILOR VALUES (1009, 'Bob', 9, 29);
INSERT INTO SAILOR VALUES (1010, 'Alice', 9, 28);

-- Inserting Boat Records (5+ records)
INSERT INTO BOAT VALUES (101, 'Interlake', 'Blue');
INSERT INTO BOAT VALUES (102, 'Interlake', 'Red');
INSERT INTO BOAT VALUES (103, 'Clipper', 'Green');
INSERT INTO BOAT VALUES (104, 'Marine', 'Red');
INSERT INTO BOAT VALUES (105, 'Enterprise', 'Blue');

-- Inserting Reserves Records (15+ records)
-- Let's make Boat 103 reserved by ALL 10 sailors for division testing
INSERT INTO RESERVES VALUES (1001, 103, TO_DATE('2026-05-01', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1002, 103, TO_DATE('2026-05-01', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1003, 103, TO_DATE('2026-05-01', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1004, 103, TO_DATE('2026-05-02', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1005, 103, TO_DATE('2026-05-03', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1006, 103, TO_DATE('2026-05-04', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1007, 103, TO_DATE('2026-05-04', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1008, 103, TO_DATE('2026-05-05', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1009, 103, TO_DATE('2026-05-05', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1010, 103, TO_DATE('2026-05-06', 'YYYY-MM-DD'));

-- Other reservations
INSERT INTO RESERVES VALUES (1001, 101, TO_DATE('2026-05-10', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1001, 102, TO_DATE('2026-05-11', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1002, 102, TO_DATE('2026-05-12', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1004, 101, TO_DATE('2026-05-15', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1005, 105, TO_DATE('2026-05-16', 'YYYY-MM-DD'));
INSERT INTO RESERVES VALUES (1006, 102, TO_DATE('2026-05-17', 'YYYY-MM-DD'));
```

---

## QUERY IMPLEMENTATION
### i. Obtain the details of the boats reserved by 'Dustin'.
#### SQL:
```sql
SELECT B.BID, B.BName, B.Color, R.Day
FROM BOAT B
JOIN RESERVES R ON B.BID = R.BID
JOIN SAILOR S ON R.SID = S.SID
WHERE S.SName = 'Dustin';
```
#### Explanation:
We join the `BOAT`, `RESERVES`, and `SAILOR` tables and filter using the condition `S.SName = 'Dustin'`.
#### Expected Output:
| BID | BName | Color | Day |
|---|---|---|---|
| 103 | Clipper | Green | 01-MAY-26 |
| 101 | Interlake | Blue | 10-MAY-26 |
| 102 | Interlake | Red | 11-MAY-26 |

---

### ii. Retrieve the BID of the boats reserved necessarily by all the sailors.
#### SQL (Using NOT EXISTS Division):
```sql
SELECT B.BID, B.BName
FROM BOAT B
WHERE NOT EXISTS (
    SELECT S.SID 
    FROM SAILOR S
    WHERE NOT EXISTS (
        SELECT R.SID 
        FROM RESERVES R
        WHERE R.BID = B.BID AND R.SID = S.SID
    )
);
```
#### SQL (Using MINUS Division):
```sql
SELECT B.BID, B.BName
FROM BOAT B
WHERE NOT EXISTS (
    SELECT S.SID FROM SAILOR S
    MINUS
    SELECT R.SID FROM RESERVES R WHERE R.BID = B.BID
);
```
#### Explanation:
The division query identifies a boat where there is zero sailors who haven't reserved it. The `MINUS` query takes the set of all sailors and subtracts the set of sailors who have reserved boat `B.BID`. If this difference is empty (`NOT EXISTS`), it means all sailors have reserved that boat.
#### Expected Output:
| BID | BName |
|---|---|
| 103 | Clipper |

---

### iii. Find the number of boats reserved by each sailor. Display the Sailor_Name along with the number of boats reserved.
#### SQL:
```sql
SELECT S.SID, S.SName, COUNT(R.BID) AS Total_Reservations
FROM SAILOR S
LEFT JOIN RESERVES R ON S.SID = R.SID
GROUP BY S.SID, S.SName
ORDER BY Total_Reservations DESC;
```
#### Explanation:
We use a `LEFT JOIN` starting from the `SAILOR` table so that sailors who have never reserved a boat (like `1003` if they didn't reserve 103, but in our case, everyone reserved 103 so count is at least 1) are still listed with a count of 0. We group the results by the sailor's primary identifier and name.
#### Expected Output:
| SID | SName | Total_Reservations |
|---|---|---|
| 1001 | Dustin | 3 |
| 1002 | Brutus | 2 |
| 1004 | Andy | 2 |
| 1005 | Rusty | 2 |
| 1006 | Horatio | 2 |
| 1007 | Zorba | 1 |
| 1003 | Lubber | 1 |
| 1008 | Art | 1 |
| 1009 | Bob | 1 |
| 1010 | Alice | 1 |

---

## VIVA QUESTIONS & ANSWERS
1. **Q:** What is relational division?
   * **A:** It is a binary operator in relational algebra used to express queries involving the phrase "for all" or "every".
2. **Q:** How is relational division represented in relational algebra?
   * **A:** By the division symbol (÷). `R ÷ S` yields all values of attributes in R but not in S that are associated with all tuples in S.
3. **Q:** Why do we use `LEFT JOIN` in aggregation queries?
   * **A:** To ensure that rows from the left table (e.g., `SAILOR`) are not discarded even if they have no matching records in the right table (e.g., `RESERVES`).
4. **Q:** What happens if `Day` is omitted from the primary key of `RESERVES`?
   * **A:** A sailor would be restricted to reserving a specific boat at most once ever.
5. **Q:** How does `MINUS` operator work?
   * **A:** It returns all unique rows from the first query that are not present in the second query.
6. **Q:** Is `DATE` a standard data type in Oracle?
   * **A:** Yes, it stores both date and time information.
7. **Q:** What is the difference between `COUNT(*)` and `COUNT(column_name)`?
   * **A:** `COUNT(*)` counts all rows including NULLs, whereas `COUNT(column_name)` counts only non-NULL values in that column.
8. **Q:** What is the purpose of `GROUP BY`?
   * **A:** To partition the table rows into groups based on matching values in the grouping columns, allowing aggregate operations per group.
9. **Q:** Can we use alias names in the `WHERE` clause?
   * **A:** No, because the `WHERE` clause is evaluated before select list expressions.
10. **Q:** What does double negation represent logically?
    * **A:** $\forall x P(x) \equiv \neg \exists x \neg P(x)$ ("For all x, P(x)" is logically equivalent to "There does not exist x for which P(x) is false").
11. **Q:** How do you insert a date value in Oracle?
    * **A:** Using the `TO_DATE` function or using date literals (e.g., `DATE '2026-05-01'`).
12. **Q:** What is referential integrity in this schema?
    * **A:** Ensuring `SID` in `RESERVES` exists in `SAILOR` and `BID` in `RESERVES` exists in `BOAT`.
13. **Q:** What is the rating check constraint in this schema?
    * **A:** `Rating CHECK (Rating BETWEEN 1 AND 10)`.
14. **Q:** Does Oracle support the `LIMIT` clause?
    * **A:** In older versions, we use `ROWNUM` or `FETCH FIRST n ROWS ONLY` in Oracle 12c+.
15. **Q:** What is a weak entity?
    * **A:** An entity that does not have a primary key of its own and depends on a parent identifying entity for its existence.

---

## LAB EXAM QUESTIONS
1. Find the names of sailors who have reserved a Red or Green boat.
2. Find the names of sailors who have reserved at least two boats.
3. List the BIDs of boats that have never been reserved.
4. Display the average age of all sailors.
5. Find the oldest sailor in the yacht club.
6. Retrieve sailors with rating greater than 7 who reserved a Red boat.
7. Find the number of reservations made on each day.
8. List boats that have been reserved on consecutive days by the same sailor.
9. Delete reservations made before '2026-05-02' and verify changes.
10. Show the query to find sailors who have reserved only Red boats.

---

## RESULT
The Boat-Sailor-Reserves database was successfully designed, implemented, and queried. The relational division queries using set operators and nested exists correctly identified the boat reserved by all sailors.
"""
    os.makedirs(r'a:\SEM4_Complete\DBMS_LAB\Experiment_3_Boat_Sailor_Reserves', exist_ok=True)
    with open(r'a:\SEM4_Complete\DBMS_LAB\Experiment_3_Boat_Sailor_Reserves\Experiment_3.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Experiment 3 Generated!")

if __name__ == "__main__":
    create_experiment_1()
    create_experiment_2()
    create_experiment_3()
