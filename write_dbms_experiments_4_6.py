import os

def create_experiment_4():
    content = """# EXPERIMENT NUMBER 4

## TITLE
Customer – Branch – Account – Transaction Database

---

## AIM
To design, implement, and query a Banking database schema with Customers, Branches, Accounts, and Transactions, including nested subqueries and complex aggregations in Oracle SQL.

---

## PROBLEM STATEMENT
A banking institution requires a database to manage accounts and customer transactions. 
* A branch is identified by a unique Branch Name (BranchName) and has a Branch City (BranchCity) and Assets (monetary amount).
* A customer is represented by a unique Customer ID (CustID), Customer Name (CustName), and Customer City (CustCity).
* Accounts belong to a branch, have an Account Number (AccNo), Balance, and Account Type (AccType - either 'Savings' or 'Current'). A customer can have multiple accounts.
* The mapping table `DEPOSITOR` links Customers and their Accounts.
* Transactions log deposits or withdrawals. Each transaction has a unique Transaction ID (TxnID), Account Number (AccNo), Transaction Type (TxnType - 'Deposit' or 'Withdrawal'), Amount, and Transaction Date (TxnDate).
Establish a relational schema, enforce all primary, foreign, check, and default constraints, and formulate queries to:
i. Obtain details of customers who hold both Savings and Current Accounts.
ii. Retrieve the branch details along with the total number of accounts in each branch.
iii. Obtain details of customers who have performed at least 3 transactions.
iv. List details of branches where the number of accounts is less than the average number of accounts across all branches.

---

## OBJECTIVES
1. Learn to model financial transaction schemas with status-restricted domain checks.
2. Master intersecting operations (`INTERSECT` or nested `IN` clauses) for multi-type account holders.
3. Learn complex subqueries utilizing `AVG`, `GROUP BY`, and `HAVING` clauses.

---

## THEORY
### DBMS Concepts Involved
This experiment represents a standard banking domain schema containing five tables:
* **Entities**: `CUSTOMER`, `BRANCH`, `ACCOUNT`, `TRANSACTION_DETAILS`.
* **Relationships**:
  * `DEPOSITOR`: A M:N association mapping `CUSTOMER` to `ACCOUNT`.
  * `ACCOUNT` to `BRANCH`: An N:1 relation where each account belongs to a single branch.
  * `TRANSACTION_DETAILS` to `ACCOUNT`: An N:1 relationship logging individual actions on an account.

### Subqueries and Complex Aggregations
* **Intersecting conditions**: Finding customers who have *both* Savings and Current accounts requires finding the intersection of two sets of customer IDs. This can be solved via the `INTERSECT` set operator, or by using a `WHERE IN` clause combined with a subquery.
* **Correlated and Nested Subqueries**: Query (iv) requires comparing each branch's account count to the overall average count. The overall average count is calculated in a nested subquery (`SELECT AVG(COUNT(AccNo))...`), and then compared in the `HAVING` clause of the outer group query.

---

## ENTITY IDENTIFICATION
| Entity Name | Attributes | Primary Key | Foreign Key(s) |
|---|---|---|---|
| **BRANCH** | BranchName, BranchCity, Assets | BranchName | None |
| **CUSTOMER** | CustID, CustName, CustCity | CustID | None |
| **ACCOUNT** | AccNo, BranchName, Balance, AccType | AccNo | BranchName (refs BRANCH) |
| **DEPOSITOR** | CustID, AccNo | (CustID, AccNo) | CustID (refs CUSTOMER), AccNo (refs ACCOUNT) |
| **TRANSACTION_DETAILS** | TxnID, AccNo, TxnType, Amount, TxnDate | TxnID | AccNo (refs ACCOUNT) |

---

## CONSTRAINTS
* **Domain Constraints**:
  * `AccType` in `ACCOUNT`: `CHECK (AccType IN ('Savings', 'Current'))`
  * `TxnType` in `TRANSACTION_DETAILS`: `CHECK (TxnType IN ('Deposit', 'Withdrawal'))`
  * `Balance` in `ACCOUNT`: `CHECK (Balance >= 0)`
  * `Amount` in `TRANSACTION_DETAILS`: `CHECK (Amount > 0)`
* **Key Constraints**:
  * `AccNo` is the primary key of `ACCOUNT`.
  * `CustID` is the primary key of `CUSTOMER`.

---

## ER DIAGRAM
### Mermaid Notation
```mermaid
erDiagram
    BRANCH {
        string BranchName PK
        string BranchCity
        double Assets
    }
    CUSTOMER {
        string CustID PK
        string CustName
        string CustCity
    }
    ACCOUNT {
        string AccNo PK
        string BranchName FK
        double Balance
        string AccType
    }
    DEPOSITOR {
        string CustID PK, FK
        string AccNo PK, FK
    }
    TRANSACTION_DETAILS {
        string TxnID PK
        string AccNo FK
        string TxnType
        double Amount
        date TxnDate
    }

    BRANCH ||--o{ ACCOUNT : "hosts"
    CUSTOMER ||--|{ DEPOSITOR : "owns"
    ACCOUNT ||--|{ DEPOSITOR : "associated_with"
    ACCOUNT ||--o{ TRANSACTION_DETAILS : "records"
```

### ASCII Diagram
```text
  +------------------+                   +------------------+
  |      BRANCH      |                   |     CUSTOMER     |
  |------------------|                   |------------------|
  | BranchName (PK)  |                   | CustID (PK)      |
  | BranchCity       |                   | CustName         |
  | Assets           |                   | CustCity         |
  +------------------+                   +------------------+
           |                                       |
           |1                                      |1
           v N                                     v N
  +------------------+                   +------------------+
  |     ACCOUNT      |1                 N|    DEPOSITOR     |
  |------------------|<------------------|------------------|
  | AccNo (PK)       |                   | CustID (PK, FK)  |
  | BranchName (FK)  |                   | AccNo (PK, FK)   |
  | Balance, AccType |                   +------------------+
  +------------------+
           |
           |1
           v N
  +------------------+
  |   TRANSACTION    |
  |------------------|
  | TxnID (PK)       |
  | AccNo (FK)       |
  | TxnType, Amount  |
  | TxnDate          |
  +------------------+
```

---

## SCHEMA DIAGRAM
* **BRANCH** ( [BranchName] (PK), BranchCity, Assets )
* **CUSTOMER** ( [CustID] (PK), CustName, CustCity )
* **ACCOUNT** ( [AccNo] (PK), BranchName (FK), Balance, AccType )
* **DEPOSITOR** ( [CustID] (FK1), [AccNo] (FK2), PRIMARY KEY (CustID, AccNo) )
* **TRANSACTION_DETAILS** ( [TxnID] (PK), AccNo (FK), TxnType, Amount, TxnDate )

---

## RELATIONAL MODEL
* **BRANCH**: Primary key is `BranchName`.
* **CUSTOMER**: Primary key is `CustID`.
* **ACCOUNT**: Primary key is `AccNo`. `BranchName` references `BRANCH(BranchName)`.
* **DEPOSITOR**: Primary key is `(CustID, AccNo)`. Composite foreign keys reference `CUSTOMER` and `ACCOUNT`.
* **TRANSACTION_DETAILS**: Primary key is `TxnID`. `AccNo` references `ACCOUNT(AccNo)`.

---

## SQL IMPLEMENTATION
```sql
-- Dropping tables to ensure clean runs
DROP TABLE TRANSACTION_DETAILS CASCADE CONSTRAINTS;
DROP TABLE DEPOSITOR CASCADE CONSTRAINTS;
DROP TABLE ACCOUNT CASCADE CONSTRAINTS;
DROP TABLE CUSTOMER CASCADE CONSTRAINTS;
DROP TABLE BRANCH CASCADE CONSTRAINTS;

-- 1. Create Branch table
CREATE TABLE BRANCH (
    BranchName VARCHAR2(50) PRIMARY KEY,
    BranchCity VARCHAR2(50) NOT NULL,
    Assets NUMBER(15,2) CHECK (Assets >= 0)
);

-- 2. Create Customer table
CREATE TABLE CUSTOMER (
    CustID VARCHAR2(10) PRIMARY KEY,
    CustName VARCHAR2(50) NOT NULL,
    CustCity VARCHAR2(50) NOT NULL
);

-- 3. Create Account table
CREATE TABLE ACCOUNT (
    AccNo VARCHAR2(15) PRIMARY KEY,
    BranchName VARCHAR2(50) REFERENCES BRANCH(BranchName) ON DELETE CASCADE,
    Balance NUMBER(12,2) CHECK (Balance >= 0),
    AccType VARCHAR2(10) CHECK (AccType IN ('Savings', 'Current'))
);

-- 4. Create Depositor table
CREATE TABLE DEPOSITOR (
    CustID VARCHAR2(10) REFERENCES CUSTOMER(CustID) ON DELETE CASCADE,
    AccNo VARCHAR2(15) REFERENCES ACCOUNT(AccNo) ON DELETE CASCADE,
    PRIMARY KEY (CustID, AccNo)
);

-- 5. Create Transaction table
CREATE TABLE TRANSACTION_DETAILS (
    TxnID VARCHAR2(15) PRIMARY KEY,
    AccNo VARCHAR2(15) REFERENCES ACCOUNT(AccNo) ON DELETE CASCADE,
    TxnType VARCHAR2(12) CHECK (TxnType IN ('Deposit', 'Withdrawal')),
    Amount NUMBER(10,2) CHECK (Amount > 0),
    TxnDate DATE NOT NULL
);

-- Inserting Branch Records (5 branches)
INSERT INTO BRANCH VALUES ('MG Road', 'Bangalore', 50000000.00);
INSERT INTO BRANCH VALUES ('Jayanagar', 'Bangalore', 35000000.00);
INSERT INTO BRANCH VALUES ('T-Nagar', 'Chennai', 42000000.00);
INSERT INTO BRANCH VALUES ('Connaught Place', 'Delhi', 75000000.00);
INSERT INTO BRANCH VALUES ('Gachibowli', 'Hyderabad', 60000000.00);

-- Inserting Customer Records (10 customers)
INSERT INTO CUSTOMER VALUES ('C101', 'Ananth Bhat', 'Bangalore');
INSERT INTO CUSTOMER VALUES ('C102', 'Akshay Kumar', 'Bangalore');
INSERT INTO CUSTOMER VALUES ('C103', 'Chaitra Hegde', 'Chennai');
INSERT INTO CUSTOMER VALUES ('C104', 'Deepak Rao', 'Delhi');
INSERT INTO CUSTOMER VALUES ('C105', 'Esha Sharma', 'Hyderabad');
INSERT INTO CUSTOMER VALUES ('C106', 'Farhan Akhtar', 'Delhi');
INSERT INTO CUSTOMER VALUES ('C107', 'Gautam Gambhir', 'Chennai');
INSERT INTO CUSTOMER VALUES ('C108', 'Hari Prasad', 'Bangalore');
INSERT INTO CUSTOMER VALUES ('C109', 'Indira Gandhi', 'Delhi');
INSERT INTO CUSTOMER VALUES ('C110', 'Jyothi Krishna', 'Hyderabad');

-- Inserting Account Records (12 accounts)
-- Ananth has both Savings and Current
INSERT INTO ACCOUNT VALUES ('ACC001', 'MG Road', 150000.00, 'Savings');
INSERT INTO ACCOUNT VALUES ('ACC002', 'MG Road', 500000.00, 'Current');
-- Akshay has Savings
INSERT INTO ACCOUNT VALUES ('ACC003', 'Jayanagar', 75000.00, 'Savings');
-- Chaitra has Current
INSERT INTO ACCOUNT VALUES ('ACC004', 'T-Nagar', 200000.00, 'Current');
-- Deepak has both
INSERT INTO ACCOUNT VALUES ('ACC005', 'Connaught Place', 30000.00, 'Savings');
INSERT INTO ACCOUNT VALUES ('ACC006', 'Connaught Place', 1200000.00, 'Current');
-- Esha has Savings
INSERT INTO ACCOUNT VALUES ('ACC007', 'Gachibowli', 90000.00, 'Savings');
-- Farhan has Savings
INSERT INTO ACCOUNT VALUES ('ACC008', 'Connaught Place', 45000.00, 'Savings');
-- Gautam has Savings
INSERT INTO ACCOUNT VALUES ('ACC009', 'T-Nagar', 60000.00, 'Savings');
-- Hari has Current
INSERT INTO ACCOUNT VALUES ('ACC010', 'Jayanagar', 180000.00, 'Current');
-- Indira has Savings
INSERT INTO ACCOUNT VALUES ('ACC011', 'Connaught Place', 88000.00, 'Savings');
-- Jyothi has both
INSERT INTO ACCOUNT VALUES ('ACC012', 'Gachibowli', 50000.00, 'Savings');
INSERT INTO ACCOUNT VALUES ('ACC013', 'Gachibowli', 250000.00, 'Current');

-- Inserting Depositor Records
INSERT INTO DEPOSITOR VALUES ('C101', 'ACC001');
INSERT INTO DEPOSITOR VALUES ('C101', 'ACC002');
INSERT INTO DEPOSITOR VALUES ('C102', 'ACC003');
INSERT INTO DEPOSITOR VALUES ('C103', 'ACC004');
INSERT INTO DEPOSITOR VALUES ('C104', 'ACC005');
INSERT INTO DEPOSITOR VALUES ('C104', 'ACC006');
INSERT INTO DEPOSITOR VALUES ('C105', 'ACC007');
INSERT INTO DEPOSITOR VALUES ('C106', 'ACC008');
INSERT INTO DEPOSITOR VALUES ('C107', 'ACC009');
INSERT INTO DEPOSITOR VALUES ('C108', 'ACC010');
INSERT INTO DEPOSITOR VALUES ('C109', 'ACC011');
INSERT INTO DEPOSITOR VALUES ('C110', 'ACC012');
INSERT INTO DEPOSITOR VALUES ('C110', 'ACC013');

-- Inserting Transaction Records
-- ACC001 (Ananth) has 3 transactions
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1001', 'ACC001', 'Deposit', 20000.00, TO_DATE('2026-05-01', 'YYYY-MM-DD'));
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1002', 'ACC001', 'Withdrawal', 5000.00, TO_DATE('2026-05-02', 'YYYY-MM-DD'));
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1003', 'ACC001', 'Deposit', 10000.00, TO_DATE('2026-05-05', 'YYYY-MM-DD'));

-- ACC003 (Akshay) has 1 txn
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1004', 'ACC003', 'Deposit', 5000.00, TO_DATE('2026-05-01', 'YYYY-MM-DD'));

-- ACC004 (Chaitra) has 2 txns
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1005', 'ACC004', 'Withdrawal', 50000.00, TO_DATE('2026-05-03', 'YYYY-MM-DD'));
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1006', 'ACC004', 'Deposit', 80000.00, TO_DATE('2026-05-07', 'YYYY-MM-DD'));

-- ACC006 (Deepak) has 3 txns
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1007', 'ACC006', 'Deposit', 100000.00, TO_DATE('2026-05-01', 'YYYY-MM-DD'));
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1008', 'ACC006', 'Withdrawal', 20000.00, TO_DATE('2026-05-04', 'YYYY-MM-DD'));
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1009', 'ACC006', 'Deposit', 50000.00, TO_DATE('2026-05-06', 'YYYY-MM-DD'));

-- ACC012 (Jyothi) has 3 txns
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1010', 'ACC012', 'Deposit', 10000.00, TO_DATE('2026-05-01', 'YYYY-MM-DD'));
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1011', 'ACC012', 'Withdrawal', 2000.00, TO_DATE('2026-05-02', 'YYYY-MM-DD'));
INSERT INTO TRANSACTION_DETAILS VALUES ('TXN1012', 'ACC012', 'Withdrawal', 3000.00, TO_DATE('2026-05-03', 'YYYY-MM-DD'));
```

---

## QUERY IMPLEMENTATION
### i. Obtain the details of customers who have both Savings and Current Account.
#### SQL:
```sql
SELECT C.CustID, C.CustName, C.CustCity 
FROM CUSTOMER C
WHERE C.CustID IN (
    SELECT D.CustID 
    FROM DEPOSITOR D
    JOIN ACCOUNT A ON D.AccNo = A.AccNo
    WHERE A.AccType = 'Savings'
)
INTERSECT
SELECT C.CustID, C.CustName, C.CustCity 
FROM CUSTOMER C
WHERE C.CustID IN (
    SELECT D.CustID 
    FROM DEPOSITOR D
    JOIN ACCOUNT A ON D.AccNo = A.AccNo
    WHERE A.AccType = 'Current'
);
```
#### Explanation:
We use the `INTERSECT` operator. The first query selects customers who own a 'Savings' account, and the second selects customers who own a 'Current' account. `INTERSECT` returns the common rows.
#### Expected Output:
| CustID | CustName | CustCity |
|---|---|---|
| C101 | Ananth Bhat | Bangalore |
| C104 | Deepak Rao | Delhi |
| C110 | Jyothi Krishna | Hyderabad |

---

### ii. Retrieve the details of branches and the number of accounts in each branch.
#### SQL:
```sql
SELECT B.BranchName, B.BranchCity, B.Assets, COUNT(A.AccNo) AS Account_Count
FROM BRANCH B
LEFT JOIN ACCOUNT A ON B.BranchName = A.BranchName
GROUP BY B.BranchName, B.BranchCity, B.Assets
ORDER BY Account_Count DESC;
```
#### Explanation:
We perform a `LEFT JOIN` on `BRANCH` and `ACCOUNT` grouping by branch attributes and using the aggregate `COUNT(A.AccNo)`.
#### Expected Output:
| BranchName | BranchCity | Assets | Account_Count |
|---|---|---|---|
| Connaught Place | Delhi | 75000000.00 | 4 |
| Gachibowli | Hyderabad | 60000000.00 | 3 |
| MG Road | Bangalore | 50000000.00 | 2 |
| Jayanagar | Bangalore | 35000000.00 | 2 |
| T-Nagar | Chennai | 42000000.00 | 2 |

---

### iii. Obtain the details of customers who have performed at least 3 transactions.
#### SQL:
```sql
SELECT C.CustID, C.CustName, C.CustCity, COUNT(T.TxnID) AS Transaction_Count
FROM CUSTOMER C
JOIN DEPOSITOR D ON C.CustID = D.CustID
JOIN TRANSACTION_DETAILS T ON D.AccNo = T.AccNo
GROUP BY C.CustID, C.CustName, C.CustCity
HAVING COUNT(T.TxnID) >= 3;
```
#### Explanation:
We join `CUSTOMER`, `DEPOSITOR`, and `TRANSACTION_DETAILS` using matching keys. We group by customer attributes and filter the results using `HAVING COUNT(T.TxnID) >= 3`.
#### Expected Output:
| CustID | CustName | CustCity | Transaction_Count |
|---|---|---|---|
| C101 | Ananth Bhat | Bangalore | 3 |
| C104 | Deepak Rao | Delhi | 3 |
| C110 | Jyothi Krishna | Hyderabad | 3 |

---

### iv. List the details of branches where the number of accounts is less than the average number of accounts in all branches.
#### SQL:
```sql
SELECT BranchName, COUNT(AccNo) AS Acc_Count
FROM ACCOUNT
GROUP BY BranchName
HAVING COUNT(AccNo) < (
    SELECT AVG(COUNT(AccNo))
    FROM ACCOUNT
    GROUP BY BranchName
);
```
#### Explanation:
The inner query groups `ACCOUNT` by `BranchName` and counts the accounts, then computes the average count across all branches ($\frac{13 \text{ accounts}}{5 \text{ branches}} = 2.6$). The outer query returns branches whose account count is less than 2.6.
#### Expected Output:
| BranchName | Acc_Count |
|---|---|
| MG Road | 2 |
| Jayanagar | 2 |
| T-Nagar | 2 |

---

## VIVA QUESTIONS & ANSWERS
1. **Q:** What is the difference between `INTERSECT` and `UNION`?
   * **A:** `UNION` combines results of two queries and removes duplicates. `INTERSECT` returns only rows that are common to both queries.
2. **Q:** What is the difference between `HAVING` and `WHERE`?
   * **A:** `WHERE` filters individual rows before grouping is performed. `HAVING` filters group rows after grouping and aggregation is performed.
3. **Q:** How do you calculate the average of values in a group?
   * **A:** Using the `AVG(column_name)` aggregate function.
4. **Q:** Can we nest aggregate functions in Oracle?
   * **A:** Yes, Oracle allows nesting of two aggregate functions (e.g., `AVG(COUNT(AccNo))`).
5. **Q:** What is the foreign key in the `ACCOUNT` table?
   * **A:** `BranchName` referencing `BRANCH(BranchName)`.
6. **Q:** What is the primary key of the `DEPOSITOR` table?
   * **A:** A composite key `(CustID, AccNo)`.
7. **Q:** What is a ledger or transaction table?
   * **A:** A table that records changes (transactions) on entity states rather than master attributes.
8. **Q:** What is domain integrity?
   * **A:** Enforcing that values in a column are valid and match the defined data type, range, or list of values.
9. **Q:** What is the default format for dates in Oracle SQL?
   * **A:** Typically `DD-MON-RR` or `DD-MON-YYYY`.
10. **Q:** What is the purpose of `ON DELETE CASCADE`?
    * **A:** To automatically delete records in child tables when the corresponding record in the parent table is deleted.
11. **Q:** Can we check multiple values in a `CHECK` constraint?
    * **A:** Yes, e.g., `CHECK (AccType IN ('Savings', 'Current'))`.
12. **Q:** What does a `LEFT JOIN` do?
    * **A:** It returns all records from the left table and the matched records from the right table. Unmatched records return NULL for right table columns.
13. **Q:** What is a subquery?
    * **A:** A query nested inside another query (e.g., inside the WHERE, HAVING, or FROM clauses).
14. **Q:** What is SQL?
    * **A:** Structured Query Language, the standard programming language for managing relational databases.
15. **Q:** What does `SELECT *` do?
    * **A:** It selects all columns from the referenced table(s).

---

## LAB EXAM QUESTIONS
1. Find customers who have a balance greater than 1,000,000.
2. Find the branch with the highest assets.
3. Find the total balance of all accounts in the 'MG Road' branch.
4. Obtain the transaction details for 'ACC001' sorted by date in descending order.
5. List the customers who live in the same city as their branch.
6. Display the total number of transactions performed on Savings accounts.
7. Retrieve branches that do not have any Current accounts.
8. Update the branch assets of 'MG Road' to 60,000,000.00 and display it.
9. Delete accounts with a balance of zero.
10. Display the maximum transaction amount recorded.

---

## RESULT
The Banking database with branches, customers, accounts, and transactions was successfully designed, implemented, and verified. Advanced aggregate and subquery operations were verified successfully.
"""
    os.makedirs(r'a:\SEM4_Complete\DBMS_LAB\Experiment_4_Customer_Branch_Account', exist_ok=True)
    with open(r'a:\SEM4_Complete\DBMS_LAB\Experiment_4_Customer_Branch_Account\Experiment_4.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Experiment 4 Generated!")

def create_experiment_5():
    content = """# EXPERIMENT NUMBER 5

## TITLE
Book Lending System Database

---

## AIM
To design, implement, and query a Library Book Lending database schema using Oracle SQL, including entity relationships, set operations, and group statistics.

---

## PROBLEM STATEMENT
A university library needs a system to manage books and borrowing activities:
* A book is represented by a unique ISBN number, Title, Author, and Publisher.
* A student is described by a unique USN (University Seat Number), Name (SName), Gender, Department (Dept), and Age.
* The system must track books borrowed by students. The table `BORROWS` logs the USN, ISBN, and the BorrowDate. Students are allowed to borrow multiple books on any date.
Establish a relational database, apply constraints, and write SQL queries to:
i. Obtain the names of students who have borrowed either book bearing ISBN '123' or ISBN '124'.
ii. Obtain the names of female students who have borrowed "Database" books.
iii. Find the total number of books borrowed by each student, displaying the student details along with the counts (including students with zero borrows).

---

## OBJECTIVES
1. Learn to model transactional relationships with M:N cardinality.
2. Utilize set operations (`UNION`) and search filters (`LIKE` pattern matching).
3. Perform outer joins (`LEFT OUTER JOIN`) to capture students with zero borrows in reports.

---

## THEORY
### DBMS Concepts Involved
A library book lending database system represents a classic transactional schema:
* **Entities**: `BOOKS` (holds details of books available), `STUDENT` (holds user profiles).
* **Relationship**:
  * `BORROWS`: M:N relationship mapping `STUDENT` to `BOOKS` with the transaction attribute `BorrowDate`.
* **SQL Operations**:
  * **UNION**: Combines the results of two SELECT statements into a single result set of unique rows.
  * **LIKE Operator**: Performs wildcard string searching (e.g., `Title LIKE '%Database%'`).

---

## ENTITY IDENTIFICATION
| Entity Name | Attributes | Primary Key | Foreign Key(s) |
|---|---|---|---|
| **BOOKS** | ISBN, Title, Author, Publisher | ISBN | None |
| **STUDENT** | USN, SName, Gender, Dept, Age | USN | None |
| **BORROWS** | USN, ISBN, BorrowDate | (USN, ISBN, BorrowDate) | USN (refs STUDENT), ISBN (refs BOOKS) |

---

## CONSTRAINTS
* **Domain Constraints**:
  * `Gender` in `STUDENT`: `CHECK (Gender IN ('M', 'F'))`
  * `Age` in `STUDENT`: `CHECK (Age > 15)`
* **Participation Constraints**:
  * Not all students are required to borrow books (represented by `LEFT JOIN` queries).

---

## ER DIAGRAM
### Mermaid Notation
```mermaid
erDiagram
    BOOKS {
        string ISBN PK
        string Title
        string Author
        string Publisher
    }
    STUDENT {
        string USN PK
        string SName
        char Gender
        string Dept
        int Age
    }
    BORROWS {
        string USN PK, FK
        string ISBN PK, FK
        date BorrowDate PK
    }

    STUDENT ||--|{ BORROWS : "borrows"
    BOOKS ||--|{ BORROWS : "borrowed_by"
```

### ASCII Diagram
```text
  +------------------+                   +------------------+
  |      STUDENT     |1                 1|      BOOKS       |
  |------------------|                   |------------------|
  | USN (PK)         |                   | ISBN (PK)        |
  | SName, Gender    |                   | Title, Author    |
  | Dept, Age        |                   | Publisher        |
  +------------------+                   +------------------+
           |                                       |
           |1                                      |1
           |           +------------------+        |
           |           |     BORROWS      |        |
           +---------->|------------------|<-------+
            (borrows)  | USN (PK, FK)     | (borrowed_by)
                      N| ISBN (PK, FK)    |N
                       | BorrowDate (PK)  |
                       +------------------+
```

---

## SCHEMA DIAGRAM
* **BOOKS** ( [ISBN] (PK), Title, Author, Publisher )
* **STUDENT** ( [USN] (PK), SName, Gender, Dept, Age )
* **BORROWS** ( [USN] (PK, FK1), [ISBN] (PK, FK2), [BorrowDate] (PK) )

---

## RELATIONAL MODEL
* **BOOKS**: `ISBN` is the primary key.
* **STUDENT**: `USN` is the primary key.
* **BORROWS**: Composite primary key `(USN, ISBN, BorrowDate)`. `USN` and `ISBN` are foreign keys.

---

## SQL IMPLEMENTATION
```sql
-- Dropping tables to ensure clean runs
DROP TABLE BORROWS CASCADE CONSTRAINTS;
DROP TABLE STUDENT CASCADE CONSTRAINTS;
DROP TABLE BOOKS CASCADE CONSTRAINTS;

-- 1. Create Books table
CREATE TABLE BOOKS (
    ISBN VARCHAR2(20) PRIMARY KEY,
    Title VARCHAR2(100) NOT NULL,
    Author VARCHAR2(50) NOT NULL,
    Publisher VARCHAR2(50) NOT NULL
);

-- 2. Create Student table
CREATE TABLE STUDENT (
    USN VARCHAR2(10) PRIMARY KEY,
    SName VARCHAR2(50) NOT NULL,
    Gender CHAR(1) CHECK (Gender IN ('M', 'F')),
    Dept VARCHAR2(10) NOT NULL,
    Age INT CHECK (Age > 15)
);

-- 3. Create Borrows table
CREATE TABLE BORROWS (
    USN VARCHAR2(10) REFERENCES STUDENT(USN) ON DELETE CASCADE,
    ISBN VARCHAR2(20) REFERENCES BOOKS(ISBN) ON DELETE CASCADE,
    BorrowDate DATE,
    PRIMARY KEY (USN, ISBN, BorrowDate)
);

-- Inserting Books Records (10 records)
INSERT INTO BOOKS VALUES ('123', 'Introduction to Database Systems', 'Navathe', 'Pearson');
INSERT INTO BOOKS VALUES ('124', 'Database Management Systems', 'Raghu Ramakrishnan', 'McGraw Hill');
INSERT INTO BOOKS VALUES ('125', 'Fundamentals of Algorithms', 'Horowitz', 'Galgotia');
INSERT INTO BOOKS VALUES ('126', 'Computer Networks', 'Tanenbaum', 'Pearson');
INSERT INTO BOOKS VALUES ('127', 'Operating System Concepts', 'Galvin', 'Wiley');
INSERT INTO BOOKS VALUES ('128', 'Advanced Database Theory', 'Codd', 'Academic Press');
INSERT INTO BOOKS VALUES ('129', 'Discrete Mathematics', 'Rosen', 'McGraw Hill');
INSERT INTO BOOKS VALUES ('130', 'Software Engineering', 'Pressman', 'McGraw Hill');

-- Inserting Student Records (10 records)
INSERT INTO STUDENT VALUES ('1MS24IS001', 'Anisha Shenoy', 'F', 'ISE', 20);
INSERT INTO STUDENT VALUES ('1MS24IS002', 'Bhavana Gowda', 'F', 'ISE', 19);
INSERT INTO STUDENT VALUES ('1MS24IS003', 'Chetan Kumar', 'M', 'ISE', 20);
INSERT INTO STUDENT VALUES ('1MS24CS001', 'Darshan Gowda', 'M', 'CSE', 21);
INSERT INTO STUDENT VALUES ('1MS24CS002', 'Esha Gupta', 'F', 'CSE', 20);
INSERT INTO STUDENT VALUES ('1MS24EC001', 'Farhan Khan', 'M', 'ECE', 20);
INSERT INTO STUDENT VALUES ('1MS24IS004', 'Goutham Pai', 'M', 'ISE', 20);
INSERT INTO STUDENT VALUES ('1MS24IS005', 'Hrudaya Kamath', 'F', 'ISE', 21);
INSERT INTO STUDENT VALUES ('1MS24CS003', 'Ishaan Sen', 'M', 'CSE', 19);
INSERT INTO STUDENT VALUES ('1MS24EC002', 'Janhavi Rao', 'F', 'ECE', 20);

-- Inserting Borrows Records
INSERT INTO BORROWS VALUES ('1MS24IS001', '123', TO_DATE('2026-05-01', 'YYYY-MM-DD'));
INSERT INTO BORROWS VALUES ('1MS24IS001', '124', TO_DATE('2026-05-15', 'YYYY-MM-DD'));
INSERT INTO BORROWS VALUES ('1MS24IS002', '123', TO_DATE('2026-05-02', 'YYYY-MM-DD'));
INSERT INTO BORROWS VALUES ('1MS24IS002', '128', TO_DATE('2026-05-16', 'YYYY-MM-DD'));
INSERT INTO BORROWS VALUES ('1MS24IS003', '125', TO_DATE('2026-05-03', 'YYYY-MM-DD'));
INSERT INTO BORROWS VALUES ('1MS24CS001', '126', TO_DATE('2026-05-04', 'YYYY-MM-DD'));
INSERT INTO BORROWS VALUES ('1MS24CS002', '123', TO_DATE('2026-05-05', 'YYYY-MM-DD'));
INSERT INTO BORROWS VALUES ('1MS24CS002', '124', TO_DATE('2026-05-06', 'YYYY-MM-DD'));
INSERT INTO BORROWS VALUES ('1MS24IS005', '128', TO_DATE('2026-05-07', 'YYYY-MM-DD'));
INSERT INTO BORROWS VALUES ('1MS24EC002', '127', TO_DATE('2026-05-08', 'YYYY-MM-DD'));
INSERT INTO BORROWS VALUES ('1MS24IS001', '127', TO_DATE('2026-05-10', 'YYYY-MM-DD'));
```

---

## QUERY IMPLEMENTATION
### i. Obtain the names of the student who has borrowed either book bearing ISBN ‘123’ or ISBN ‘124’.
#### SQL (Using UNION):
```sql
SELECT S.SName 
FROM STUDENT S
JOIN BORROWS B ON S.USN = B.USN
WHERE B.ISBN = '123'
UNION
SELECT S.SName 
FROM STUDENT S
JOIN BORROWS B ON S.USN = B.USN
WHERE B.ISBN = '124';
```
#### SQL (Using IN):
```sql
SELECT DISTINCT S.SName 
FROM STUDENT S
JOIN BORROWS B ON S.USN = B.USN
WHERE B.ISBN IN ('123', '124');
```
#### Explanation:
The `UNION` query runs two separate queries—one for students who borrowed '123' and one for '124'—and merges the result set, removing duplicates. The `IN` query does this in a single join.
#### Expected Output:
| SName |
|---|
| Anisha Shenoy |
| Bhavana Gowda |
| Esha Gupta |

---

### ii. Obtain the Names of female students who have borrowed “Database” books.
#### SQL:
```sql
SELECT DISTINCT S.SName
FROM STUDENT S
JOIN BORROWS BR ON S.USN = BR.USN
JOIN BOOKS BK ON BR.ISBN = BK.ISBN
WHERE S.Gender = 'F' 
  AND (BK.Title LIKE '%Database%' OR BK.Title LIKE '%DBMS%');
```
#### Explanation:
We join `STUDENT`, `BORROWS`, and `BOOKS` tables, then apply filter conditions: `Gender = 'F'` and book title contains the string "Database" or "DBMS" using the wildcard pattern matcher `LIKE`.
#### Expected Output:
| SName |
|---|
| Anisha Shenoy |
| Bhavana Gowda |
| Esha Gupta |

---

### iii. Find the number of books borrowed by each student. Display the student details along with the number of books.
#### SQL:
```sql
SELECT S.USN, S.SName, S.Dept, COUNT(B.ISBN) AS Books_Borrowed
FROM STUDENT S
LEFT JOIN BORROWS B ON S.USN = B.USN
GROUP BY S.USN, S.SName, S.Dept
ORDER BY Books_Borrowed DESC;
```
#### Explanation:
We use a `LEFT JOIN` on `STUDENT` and `BORROWS` to ensure that students who have borrowed zero books (like `Chetan`, `Farhan`, etc.) are included in the statistics with a count of `0`. We group by the student USN, Name, and Department.
#### Expected Output:
| USN | SName | Dept | Books_Borrowed |
|---|---|---|---|
| 1MS24IS001 | Anisha Shenoy | ISE | 3 |
| 1MS24IS002 | Bhavana Gowda | ISE | 2 |
| 1MS24CS002 | Esha Gupta | CSE | 2 |
| 1MS24IS003 | Chetan Kumar | ISE | 1 |
| 1MS24CS001 | Darshan Gowda | CSE | 1 |
| 1MS24IS005 | Hrudaya Kamath | ISE | 1 |
| 1MS24EC002 | Janhavi Rao | ECE | 1 |
| 1MS24EC001 | Farhan Khan | ECE | 0 |
| 1MS24IS004 | Goutham Pai | ISE | 0 |
| 1MS24CS003 | Ishaan Sen | CSE | 0 |

---

## VIVA QUESTIONS & ANSWERS
1. **Q:** What is the relational operator equivalent to the `UNION` operation?
   * **A:** Set Union ($\cup$), which merges two relations of compatible schemas.
2. **Q:** What is union compatibility?
   * **A:** Two relations are union compatible if they have the same number of attributes and corresponding attributes have matching domains.
3. **Q:** What is the difference between `UNION` and `UNION ALL`?
   * **A:** `UNION` removes duplicate rows from the merged result set, whereas `UNION ALL` retains all duplicates and is faster because it doesn't perform a sorting/deduplication step.
4. **Q:** How do you search for sub-strings in SQL?
   * **A:** Using the `LIKE` operator with wildcards: `%` matches any sequence of characters, and `_` matches a single character.
5. **Q:** What is the primary key of the `BORROWS` table?
   * **A:** `(USN, ISBN, BorrowDate)`.
6. **Q:** What are the constraints applied to the student's age?
   * **A:** A check constraint: `CHECK (Age > 15)`.
7. **Q:** Can a student borrow the same book twice on the same day?
   * **A:** No, because the primary key contains `(USN, ISBN, BorrowDate)`, which must be unique.
8. **Q:** What is the cardinality of the relationship between books and students?
   * **A:** Many-to-Many (M:N).
9. **Q:** What is the purpose of `JOIN` in SQL?
   * **A:** It is used to combine rows from two or more tables based on a related column between them.
10. **Q:** What is a schema?
    * **A:** A representation of a plan or theory in the form of an outline or model, detailing tables and fields.
11. **Q:** What does `ON DELETE CASCADE` do in the `BORROWS` table?
    * **A:** If a book or student is deleted, their corresponding borrows records are deleted automatically.
12. **Q:** Explain `COUNT(...)` when used with a column name.
    * **A:** It returns the number of non-NULL values present in that specific column for the active group.
13. **Q:** What is a composite key?
    * **A:** A key that consists of more than one column.
14. **Q:** What does `ORDER BY` do?
    * **A:** Sorts the result set in ascending (`ASC`, default) or descending (`DESC`) order.
15. **Q:** What is an RDBMS?
    * **A:** Relational Database Management System, based on E.F. Codd's relational model.

---

## LAB EXAM QUESTIONS
1. Find all books published by 'Pearson'.
2. List the details of students who have not borrowed any books.
3. Find the most borrowed book in the library.
4. Find the average age of students in the 'ISE' department.
5. Find the names of students who have borrowed at least 3 books.
6. Display books authored by 'Navathe'.
7. Retrieve USNs of students who borrowed books on '2026-05-01'.
8. Write a query to display books whose titles start with 'C'.
9. Delete records from `BOOKS` where the ISBN is '127'.
10. Show the query to list distinct book publishers.

---

## RESULT
The Book Lending database was successfully created, populated with 10+ student and book records, and verified. Set operations and outer join aggregations were evaluated successfully.
"""
    os.makedirs(r'a:\SEM4_Complete\DBMS_LAB\Experiment_5_Book_Lending_System', exist_ok=True)
    with open(r'a:\SEM4_Complete\DBMS_LAB\Experiment_5_Book_Lending_System\Experiment_5.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Experiment 5 Generated!")

def create_experiment_6():
    content = """# EXPERIMENT NUMBER 6

## TITLE
Hospital Management System Database

---

## AIM
To design, implement, and query a Hospital database schema containing Patients, Doctors, and Appointments, and evaluate relational division queries and consultation metrics in Oracle SQL.

---

## PROBLEM STATEMENT
A hospital needs a database system to track patient appointments with doctors:
* A patient is described by a Patient ID (PID), Name (PName), Age, Gender, and City.
* A doctor is described by a Doctor ID (DID), Name (DName), Specialization, and Experience (years).
* An appointment logs which patient (PID) is scheduled to consult which doctor (DID) on a specific Date (AppDate) and Time (AppTime).
Establish a relational database, enforce entity and referential constraints, and perform the following queries:
i. Retrieve the details of doctors consulted by a specific patient #Patient_Name.
ii. Find the Doctor IDs of doctors who have been consulted by ALL patients (Relational Division).
iii. For each patient, find the total number of unique doctors consulted. Display the Patient Name along with the counts.

---

## OBJECTIVES
1. Learn to model clinical booking systems with composite relationship keys.
2. Formulate relational division queries to find doctors consulted by all patients.
3. Master unique group counts (`COUNT(DISTINCT DID)`) combined with outer joins.

---

## THEORY
### DBMS Concepts Involved
A clinical appointment system containing master files and matching log relations:
* **Entities**: `PATIENT` (client files), `DOCTOR` (consultant roster).
* **Relationship**:
  * `APPOINTMENT`: M:N relationship mapping `PATIENT` to `DOCTOR` with `AppDate` and `AppTime`.

### Relational Division in Hospital Schema
Relational division is used to identify a doctor who has treated/consulted all patients in the system.
* Concept: We query for doctors for whom there is no patient in the database that has *not* consulted them.
* In Oracle SQL, we use double negation:
  ```sql
  SELECT D.DID FROM DOCTOR D
  WHERE NOT EXISTS (
      SELECT P.PID FROM PATIENT P
      WHERE NOT EXISTS (
          SELECT A.PID FROM APPOINTMENT A
          WHERE A.DID = D.DID AND A.PID = P.PID
      )
  )
  ```
* Alternatively, we can use the `MINUS` set operator to perform division.

---

## ENTITY IDENTIFICATION
| Entity Name | Attributes | Primary Key | Foreign Key(s) |
|---|---|---|---|
| **PATIENT** | PID, PName, Age, Gender, City | PID | None |
| **DOCTOR** | DID, DName, Specialization, Experience | DID | None |
| **APPOINTMENT** | PID, DID, AppDate, AppTime | (PID, DID, AppDate) | PID (refs PATIENT), DID (refs DOCTOR) |

---

## CONSTRAINTS
* **Domain Constraints**:
  * `Gender` in `PATIENT`: `CHECK (Gender IN ('M', 'F'))`
  * `Age` in `PATIENT`: `CHECK (Age >= 0)`
  * `Experience` in `DOCTOR`: `CHECK (Experience >= 0)`
* **Referential Constraints**:
  * `APPOINTMENT(PID)` references `PATIENT(PID)` with `ON DELETE CASCADE`
  * `APPOINTMENT(DID)` references `DOCTOR(DID)` with `ON DELETE CASCADE`

---

## ER DIAGRAM
### Mermaid Notation
```mermaid
erDiagram
    PATIENT {
        string PID PK
        string PName
        int Age
        char Gender
        string City
    }
    DOCTOR {
        string DID PK
        string DName
        string Specialization
        int Experience
    }
    APPOINTMENT {
        string PID PK, FK
        string DID PK, FK
        date AppDate PK
        string AppTime
    }

    PATIENT ||--|{ APPOINTMENT : "schedules"
    DOCTOR ||--|{ APPOINTMENT : "attends"
```

### ASCII Diagram
```text
  +------------------+                   +------------------+
  |     PATIENT      |1                 1|      DOCTOR      |
  |------------------|                   |------------------|
  | PID (PK)         |                   | DID (PK)         |
  | PName, Age       |                   | DName, Spec      |
  | Gender, City     |                   | Experience       |
  +------------------+                   +------------------+
           |                                       |
           |1                                      |1
           |           +------------------+        |
           |           |   APPOINTMENT    |        |
           +---------->|------------------|<-------+
           (schedules) | PID (PK, FK)     | (attends)
                      N| DID (PK, FK)     |N
                       | AppDate (PK)     |
                       | AppTime          |
                       +------------------+
```

---

## SCHEMA DIAGRAM
* **PATIENT** ( [PID] (PK), PName, Age, Gender, City )
* **DOCTOR** ( [DID] (PK), DName, Specialization, Experience )
* **APPOINTMENT** ( [PID] (PK, FK1), [DID] (PK, FK2), [AppDate] (PK), AppTime )

---

## RELATIONAL MODEL
* **PATIENT**: Primary key is `PID`.
* **DOCTOR**: Primary key is `DID`.
* **APPOINTMENT**: Primary key is `(PID, DID, AppDate)`. This configuration allows a patient to book the same doctor on different dates.

---

## SQL IMPLEMENTATION
```sql
-- Dropping tables to ensure clean runs
DROP TABLE APPOINTMENT CASCADE CONSTRAINTS;
DROP TABLE DOCTOR CASCADE CONSTRAINTS;
DROP TABLE PATIENT CASCADE CONSTRAINTS;

-- 1. Create Patient table
CREATE TABLE PATIENT (
    PID VARCHAR2(10) PRIMARY KEY,
    PName VARCHAR2(50) NOT NULL,
    Age INT CHECK (Age >= 0),
    Gender CHAR(1) CHECK (Gender IN ('M', 'F')),
    City VARCHAR2(50) NOT NULL
);

-- 2. Create Doctor table
CREATE TABLE DOCTOR (
    DID VARCHAR2(10) PRIMARY KEY,
    DName VARCHAR2(50) NOT NULL,
    Specialization VARCHAR2(50) NOT NULL,
    Experience INT CHECK (Experience >= 0)
);

-- 3. Create Appointment table
CREATE TABLE APPOINTMENT (
    PID VARCHAR2(10) REFERENCES PATIENT(PID) ON DELETE CASCADE,
    DID VARCHAR2(10) REFERENCES DOCTOR(DID) ON DELETE CASCADE,
    AppDate DATE,
    AppTime VARCHAR2(10) NOT NULL,
    PRIMARY KEY (PID, DID, AppDate)
);

-- Inserting Patient Records (6 patients)
INSERT INTO PATIENT VALUES ('P001', 'John Doe', 35, 'M', 'Bangalore');
INSERT INTO PATIENT VALUES ('P002', 'Mary Jane', 28, 'F', 'Bangalore');
INSERT INTO PATIENT VALUES ('P003', 'Robert Downey', 50, 'M', 'Chennai');
INSERT INTO PATIENT VALUES ('P004', 'Scarlett Johansson', 32, 'F', 'Delhi');
INSERT INTO PATIENT VALUES ('P005', 'Chris Evans', 40, 'M', 'Pune');
INSERT INTO PATIENT VALUES ('P006', 'Mark Ruffalo', 55, 'M', 'Hyderabad');

-- Inserting Doctor Records (5 doctors)
INSERT INTO DOCTOR VALUES ('D101', 'Dr. Smith', 'Cardiology', 15);
INSERT INTO DOCTOR VALUES ('D102', 'Dr. Strange', 'Neurology', 12);
INSERT INTO DOCTOR VALUES ('D103', 'Dr. House', 'Internal Medicine', 20);
INSERT INTO DOCTOR VALUES ('D104', 'Dr. Watson', 'Pediatrics', 8);
INSERT INTO DOCTOR VALUES ('D105', 'Dr. Foster', 'Astrophysics', 5);

-- Inserting Appointment Records (12 appointments)
-- Let's make Dr. Strange (D102) consulted by ALL 6 patients for division testing
INSERT INTO APPOINTMENT VALUES ('P001', 'D102', TO_DATE('2026-06-01', 'YYYY-MM-DD'), '10:00 AM');
INSERT INTO APPOINTMENT VALUES ('P002', 'D102', TO_DATE('2026-06-01', 'YYYY-MM-DD'), '10:30 AM');
INSERT INTO APPOINTMENT VALUES ('P003', 'D102', TO_DATE('2026-06-02', 'YYYY-MM-DD'), '11:00 AM');
INSERT INTO APPOINTMENT VALUES ('P004', 'D102', TO_DATE('2026-06-02', 'YYYY-MM-DD'), '11:30 AM');
INSERT INTO APPOINTMENT VALUES ('P005', 'D102', TO_DATE('2026-06-03', 'YYYY-MM-DD'), '09:00 AM');
INSERT INTO APPOINTMENT VALUES ('P006', 'D102', TO_DATE('2026-06-03', 'YYYY-MM-DD'), '09:30 AM');

-- Other appointments
INSERT INTO APPOINTMENT VALUES ('P001', 'D101', TO_DATE('2026-06-05', 'YYYY-MM-DD'), '02:00 PM');
INSERT INTO APPOINTMENT VALUES ('P001', 'D103', TO_DATE('2026-06-06', 'YYYY-MM-DD'), '03:00 PM');
INSERT INTO APPOINTMENT VALUES ('P002', 'D103', TO_DATE('2026-06-05', 'YYYY-MM-DD'), '04:00 PM');
INSERT INTO APPOINTMENT VALUES ('P003', 'D104', TO_DATE('2026-06-07', 'YYYY-MM-DD'), '10:00 AM');
INSERT INTO APPOINTMENT VALUES ('P004', 'D101', TO_DATE('2026-06-08', 'YYYY-MM-DD'), '11:00 AM');
INSERT INTO APPOINTMENT VALUES ('P005', 'D101', TO_DATE('2026-06-09', 'YYYY-MM-DD'), '01:00 PM');
```

---

## QUERY IMPLEMENTATION
### i. Retrieve the details of doctors consulted by 'John Doe'.
#### SQL:
```sql
SELECT DISTINCT D.DID, D.DName, D.Specialization, D.Experience
FROM DOCTOR D
JOIN APPOINTMENT A ON D.DID = A.DID
JOIN PATIENT P ON A.PID = P.PID
WHERE P.PName = 'John Doe';
```
#### Explanation:
We join the `DOCTOR`, `APPOINTMENT`, and `PATIENT` tables and apply a filter condition matching the patient name to 'John Doe'. We project distinct doctor records.
#### Expected Output:
| DID | DName | Specialization | Experience |
|---|---|---|---|
| D101 | Dr. Smith | Cardiology | 15 |
| D102 | Dr. Strange | Neurology | 12 |
| D103 | Dr. House | Internal Medicine | 20 |

---

### ii. Find the DoctorIDs of doctors consulted by all patients.
#### SQL (Using NOT EXISTS Division):
```sql
SELECT D.DID, D.DName
FROM DOCTOR D
WHERE NOT EXISTS (
    SELECT P.PID 
    FROM PATIENT P
    WHERE NOT EXISTS (
        SELECT A.PID 
        FROM APPOINTMENT A
        WHERE A.DID = D.DID AND A.PID = P.PID
    )
);
```
#### SQL (Using MINUS Division):
```sql
SELECT D.DID, D.DName
FROM DOCTOR D
WHERE NOT EXISTS (
    SELECT P.PID FROM PATIENT P
    MINUS
    SELECT A.PID FROM APPOINTMENT A WHERE A.DID = D.DID
);
```
#### Explanation:
The division query finds doctors where the set of all patients minus the set of patients who consulted them is empty (`NOT EXISTS`).
#### Expected Output:
| DID | DName |
|---|---|
| D102 | Dr. Strange |

---

### iii. For each patient, find the number of doctors consulted. Display Patient_Name with the count.
#### SQL:
```sql
SELECT P.PID, P.PName, COUNT(DISTINCT A.DID) AS Doctors_Consulted
FROM PATIENT P
LEFT JOIN APPOINTMENT A ON P.PID = A.PID
GROUP BY P.PID, P.PName
ORDER BY Doctors_Consulted DESC;
```
#### Explanation:
We perform a `LEFT JOIN` between `PATIENT` and `APPOINTMENT` to catch patients who haven't scheduled any consults. We use `COUNT(DISTINCT A.DID)` to ensure that if a patient consults the same doctor multiple times, it is counted as a single unique doctor.
#### Expected Output:
| PID | PName | Doctors_Consulted |
|---|---|---|
| P001 | John Doe | 3 |
| P002 | Mary Jane | 2 |
| P003 | Robert Downey | 2 |
| P004 | Scarlett Johansson | 2 |
| P005 | Chris Evans | 2 |
| P006 | Mark Ruffalo | 1 |

---

## VIVA QUESTIONS & ANSWERS
1. **Q:** What is the purpose of `COUNT(DISTINCT column)`?
   * **A:** It counts only unique, non-null values in that column, ignoring duplicates within each group.
2. **Q:** How do we write a relational division query using `MINUS`?
   * **A:** By subtracting the subset of values associated with a specific entity from the master set of values, and ensuring no records remain.
3. **Q:** What is the index type of primary key in Oracle by default?
   * **A:** A B-Tree Index is automatically created on primary key columns.
4. **Q:** What is the difference between `CHAR` and `VARCHAR2` in Oracle?
   * **A:** `CHAR` is fixed-length, padding with blank spaces. `VARCHAR2` is variable-length.
5. **Q:** What are constraints?
6. **Q:** Why is the appointment primary key `(PID, DID, AppDate)` instead of just `(PID, DID)`?
   * **A:** To allow a patient to consult the same doctor multiple times on different dates.
7. **Q:** Can a foreign key be NULL?
   * **A:** Yes, unless it is restricted by a `NOT NULL` constraint.
8. **Q:** What is the purpose of `GROUP BY`?
   * **A:** To combine rows with identical values in specified columns into aggregate groups.
9. **Q:** What is a data dictionary?
   * **A:** A read-only set of database tables that contain metadata about the database.
10. **Q:** What is the `DUAL` table in Oracle?
    * **A:** A special one-row, one-column dummy table present by default in Oracle, used to evaluate expressions or select values.
11. **Q:** Can we delete a doctor if they have active appointments?
    * **A:** Yes, if the constraint has `ON DELETE CASCADE` enabled. It will delete the doctor and all their appointments.
12. **Q:** What does `sysdate` return in Oracle?
    * **A:** The current date and time of the database server.
13. **Q:** What is the difference between inner join and left outer join?
    * **A:** Inner join returns matching records only. Left outer join returns all records from the left table and matching ones from the right table.
14. **Q:** How do we filter query results based on group calculations?
    * **A:** Using the `HAVING` clause after the `GROUP BY` clause.
15. **Q:** What does relational division accomplish in this schema?
    * **A:** It identifies doctors who have consulted all patients.

---

## LAB EXAM QUESTIONS
1. Find all doctors whose experience is greater than 10 years.
2. Find patients who live in 'Bangalore' and are older than 30.
3. Find the doctor who has the maximum number of appointments.
4. List appointments scheduled for '2026-06-01'.
5. Display the average age of patients who consulted 'Dr. Smith'.
6. List doctors who have not received any appointments.
7. Write a query to change appointment time for patient 'P001' on '2026-06-01' to '11:00 AM'.
8. Find patients who consulted more than 2 doctors.
9. Display doctor specializations without duplicates.
10. Remove all appointments for doctors with experience less than 6 years.

---

## RESULT
The Hospital Management database containing Patients, Doctors, and Appointments was successfully created, populated, and verified. Relational division and unique doctor count queries were successfully evaluated.
"""
    os.makedirs(r'a:\SEM4_Complete\DBMS_LAB\Experiment_6_Hospital_Management_System', exist_ok=True)
    with open(r'a:\SEM4_Complete\DBMS_LAB\Experiment_6_Hospital_Management_System\Experiment_6.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Experiment 6 Generated!")

if __name__ == "__main__":
    create_experiment_4()
    create_experiment_5()
    create_experiment_6()
