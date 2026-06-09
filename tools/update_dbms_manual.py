import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Define the HTML content blocks for each experiment
EXP_BLOCKS = {}

# EXP 1
EXP_BLOCKS[1] = """<h3>Schema Diagram</h3>
                <pre>
EMPLOYEE ( ssn [PK], name, deptno )
PROJECT ( projectno [PK], projectarea )
WORKS_ON ( ssn [FK], projectno [FK] )
                </pre>
                <h3>Create Table Statements</h3>
                <pre>
create table Employee
(
ssn varchar(6),
name varchar(10),
deptno int,
primary key(ssn)
);

create table Project
(
projectno varchar(10),
projectarea varchar(20),
primary key(projectno)
);

create table Works_On
(
ssn varchar(6),
projectno varchar(10),
foreign key(ssn)references Employee(ssn),
foreign key(projectno)references Project(projectno)
);
                </pre>
                <h3>Insert Sample Data</h3>
                <pre>
INSERT INTO Employee VALUES ('E101','Ravi',10);
INSERT INTO Employee VALUES ('E102','Anu',20);
INSERT INTO Employee VALUES ('E103','Kiran',30);
INSERT INTO Employee VALUES ('E104','Priya',10);

INSERT INTO Project VALUES (101,'Database');
INSERT INTO Project VALUES (102,'Cloud');
INSERT INTO Project VALUES (103,'Data Science');

INSERT INTO Works_On VALUES ('E101',101);
INSERT INTO Works_On VALUES ('E102',102);
INSERT INTO Works_On VALUES ('E103',101);
INSERT INTO Works_On VALUES ('E104',103);
                </pre>
                <h3>Verify Table Insertion</h3>
                <p><b>select * from Employee;</b></p>
                <table>
                    <tr><th>ssn</th><th>name</th><th>deptno</th></tr>
                    <tr><td>E101</td><td>Ravi</td><td>10</td></tr>
                    <tr><td>E102</td><td>Anu</td><td>20</td></tr>
                    <tr><td>E103</td><td>Kiran</td><td>30</td></tr>
                    <tr><td>E104</td><td>Priya</td><td>10</td></tr>
                </table>
                <p><b>select * from Project;</b></p>
                <table>
                    <tr><th>projectno</th><th>projectarea</th></tr>
                    <tr><td>101</td><td>Database</td></tr>
                    <tr><td>102</td><td>Cloud</td></tr>
                    <tr><td>103</td><td>Data Science</td></tr>
                </table>
                <p><b>select * from Works_On;</b></p>
                <table>
                    <tr><th>ssn</th><th>projectno</th></tr>
                    <tr><td>E101</td><td>101</td></tr>
                    <tr><td>E102</td><td>102</td></tr>
                    <tr><td>E103</td><td>101</td></tr>
                    <tr><td>E104</td><td>103</td></tr>
                </table>
                <h3>Query i</h3>
                <p><b>Obtain the details of employees assigned to “Database” project.</b></p>
                <pre>
SELECT E.*
FROM Employee E
JOIN Works_On W ON E.ssn = W.ssn
JOIN Project P ON W.projectno = P.projectno
WHERE P.projectarea = 'Database';
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>ssn</th><th>name</th><th>deptno</th></tr>
                    <tr><td>E101</td><td>Ravi</td><td>10</td></tr>
                    <tr><td>E103</td><td>Kiran</td><td>30</td></tr>
                </table>
                <h3>Query ii</h3>
                <p><b>Find the number of employees working in each department with department details.</b></p>
                <pre>
select deptno,count(ssn) as NumberofEmployees 
from Employee 
group by deptno;
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>deptno</th><th>NumberofEmployees</th></tr>
                    <tr><td>10</td><td>2</td></tr>
                    <tr><td>20</td><td>1</td></tr>
                    <tr><td>30</td><td>1</td></tr>
                </table>
                <h3>Query iii</h3>
                <p><b>Update the Project details of Employee bearing SSN='E102' to ProjectNo=101 and display the same.</b></p>
                <pre>
UPDATE Works_On
SET projectno = 101
WHERE SSN = 'E102';

SELECT * from Works_On;
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>ssn</th><th>projectno</th></tr>
                    <tr><td>E101</td><td>101</td></tr>
                    <tr><td>E102</td><td>101</td></tr>
                    <tr><td>E103</td><td>101</td></tr>
                    <tr><td>E104</td><td>103</td></tr>
                </table>
                <hr>
                <h2>PART B — NoSQL (MongoDB) &amp; Procedural SQL (PL/SQL)</h2>
                <h3>Aim</h3>
                <p>To perform MongoDB operations on Employee and Department collections, and implement salary adjustment logic using a PL/SQL block in Oracle.</p>
                <h3>MongoDB Collections &amp; Document Insertion</h3>
                <pre>
db.Employee.insertMany([
  { Emp_ID:101, Emp_Name:"Ravi", Dept_No:10, Salary:50000, Project_No:"P101"},
  { Emp_ID:102, Emp_Name:"Rani", Dept_No:20, Salary:60000, Project_No:"P102"},
  { Emp_ID:103, Emp_Name:"Kushal", Dept_No:10, Salary:55000, Project_No:"P101"}
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a20078bbc1cfd02008ce5af'),
    '1': ObjectId('6a20078bbc1cfd02008ce5b0'),
    '2': ObjectId('6a20078bbc1cfd02008ce5b1')
  }
}
                </pre>
                <pre>
db.Department.insertMany([
  {Dept_No:10, Dept_Name:"HR"},
  {Dept_No:20, Dept_Name:"IT"}
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a20078cbc1cfd02008ce5b2'),
    '1': ObjectId('6a20078cbc1cfd02008ce5b3')
  }
}
                </pre>
                <h3>MongoDB Query i</h3>
                <p><b>List all the employees of Department named "HR".</b></p>
                <pre>
var dept=db.Department.findOne(
   {Dept_Name:"HR"}
);

db.Employee.find(
   {Dept_No:dept.Dept_No}
);
                </pre>
                <h4>Expected Output</h4>
                <pre>[
  {
    _id: ObjectId('6a20078bbc1cfd02008ce5af'),
    Emp_ID: 101,
    Emp_Name: 'Ravi',
    Dept_No: 10,
    Salary: 50000,
    Project_No: 'P101'
  },
  {
    _id: ObjectId('6a20078bbc1cfd02008ce5b1'),
    Emp_ID: 103,
    Emp_Name: 'Kushal',
    Dept_No: 10,
    Salary: 55000,
    Project_No: 'P101'
  }
]</pre>
                <h3>MongoDB Query ii</h3>
                <p><b>Name the employees working on Project Number: "P101".</b></p>
                <pre>
db.Employee.find(
   {Project_No:"P101"},
   {Emp_Name:1,_id:0}
);
                </pre>
                <h4>Expected Output</h4>
                <pre>[ { Emp_Name: 'Ravi' }, { Emp_Name: 'Kushal' } ]</pre>
                <h3>PL/SQL Program</h3>
                <p><b>Write a PL/SQL program that gives all employees in Department 10 a 15% pay increase. Display a message displaying how many employees were awarded the increase.</b></p>
                <p><b>Table Setup:</b></p>
                <pre>
CREATE TABLE Employee (
    Emp_ID NUMBER(5) PRIMARY KEY,
    Emp_Name VARCHAR2(20),
    Dept_No NUMBER(8),
    Salary NUMBER(10)
);

INSERT INTO Employee VALUES (101, 'Ravi', 10, 50000);
INSERT INTO Employee VALUES (102, 'Anu', 20, 60000);
INSERT INTO Employee VALUES (103, 'Kiran', 10, 55000);
INSERT INTO Employee VALUES (104, 'Priya', 30, 45000);
COMMIT;

SELECT * FROM Employee;
                </pre>
                <h4>Initial Employee Table Output</h4>
                <table>
                    <tr><th>EMP_ID</th><th>EMP_NAME</th><th>DEPT_NO</th><th>SALARY</th></tr>
                    <tr><td>101</td><td>Ravi</td><td>10</td><td>50000</td></tr>
                    <tr><td>102</td><td>Anu</td><td>20</td><td>60000</td></tr>
                    <tr><td>103</td><td>Kiran</td><td>10</td><td>55000</td></tr>
                    <tr><td>104</td><td>Priya</td><td>30</td><td>45000</td></tr>
                </table>
                <p><b>PL/SQL Block:</b></p>
                <pre>
SET SERVEROUTPUT ON;
DECLARE
   v_count NUMBER;
BEGIN
   UPDATE Employee
   SET Salary = Salary * 1.15
   WHERE Dept_No = 10;

   v_count := SQL%ROWCOUNT;
   DBMS_OUTPUT.PUT_LINE(v_count || ' employees awarded 15% increase');
END;
/
SELECT * FROM Employee;
                </pre>
                <h4>Execution Output</h4>
                <pre>
2 employees awarded 15% increase
                </pre>
                <h4>Updated Employee Table Output</h4>
                <table>
                    <tr><th>EMP_ID</th><th>EMP_NAME</th><th>DEPT_NO</th><th>SALARY</th></tr>
                    <tr><td>101</td><td>Ravi</td><td>10</td><td>57500</td></tr>
                    <tr><td>102</td><td>Anu</td><td>20</td><td>60000</td></tr>
                    <tr><td>103</td><td>Kiran</td><td>10</td><td>63250</td></tr>
                    <tr><td>104</td><td>Priya</td><td>30</td><td>45000</td></tr>
                </table>
                <hr>
"""

# EXP 2
EXP_BLOCKS[2] = """<h3>Schema Diagram</h3>
                <pre>
PART ( pno [PK], pname, colour )
SUPPLIER ( sno [PK], sname, address )
SUPPLY ( pno [PK, FK], sno [PK, FK], quantity )
                </pre>
                <h3>Create Table Statements</h3>
                <pre>
create table part
(
pno number(10),
pname varchar(20),
colour varchar(20),
primary key(pno)
);

create table supplier
(
sno number(10),
sname varchar(20),
address varchar(20),
primary key(sno)
);

create table supply
(
pno number(10),
sno number(10),
quantity varchar(20),
primary key(pno,sno),
foreign key(pno) references part(pno)on delete cascade,
foreign key(sno) references supplier(sno)on delete cascade
);
                </pre>
                <h3>Insert Sample Data</h3>
                <pre>
insert into part values(1,'plug','black');
insert into part values(2,'bolt','blue');
insert into part values(3,'nut','green');

insert into supplier values(10,'Anoop','udupi');
insert into supplier values(15,'Bharath','mangalore');
insert into supplier values(20,'Ram','bangalore');

insert into supply values(1,10,50);
insert into supply values(2,10,30);
insert into supply values(1,15,70);
insert into supply values(3,15,40);
insert into supply values(1,20,55);
insert into supply values(2,20,65);
insert into supply values(3,20,75);
                </pre>
                <h3>Verify Table Insertion</h3>
                <p><b>select * from part;</b></p>
                <table>
                    <tr><th>PNO</th><th>PNAME</th><th>COLOUR</th></tr>
                    <tr><td>1</td><td>plug</td><td>black</td></tr>
                    <tr><td>2</td><td>bolt</td><td>blue</td></tr>
                    <tr><td>3</td><td>nut</td><td>green</td></tr>
                </table>
                <p><b>select * from supplier;</b></p>
                <table>
                    <tr><th>SNO</th><th>SNAME</th><th>ADDRESS</th></tr>
                    <tr><td>10</td><td>Anoop</td><td>udupi</td></tr>
                    <tr><td>15</td><td>Bharath</td><td>mangalore</td></tr>
                    <tr><td>20</td><td>Ram</td><td>bangalore</td></tr>
                </table>
                <p><b>select * from supply;</b></p>
                <table>
                    <tr><th>PNO</th><th>SNO</th><th>QUANTITY</th></tr>
                    <tr><td>1</td><td>10</td><td>50</td></tr>
                    <tr><td>2</td><td>10</td><td>30</td></tr>
                    <tr><td>1</td><td>15</td><td>70</td></tr>
                    <tr><td>3</td><td>15</td><td>40</td></tr>
                    <tr><td>1</td><td>20</td><td>55</td></tr>
                    <tr><td>2</td><td>20</td><td>65</td></tr>
                    <tr><td>3</td><td>20</td><td>75</td></tr>
                </table>
                <h3>Query i</h3>
                <p><b>Obtain the part identifiers of parts supplied by supplier 'Ram'.</b></p>
                <pre>
select pno from supply 
where sno IN(select sno from supplier where sname='Ram');
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>PNO</th></tr>
                    <tr><td>1</td></tr>
                    <tr><td>2</td></tr>
                    <tr><td>3</td></tr>
                </table>
                <h3>Query ii</h3>
                <p><b>Obtain the Names of suppliers who supply 'bolt'.</b></p>
                <pre>
select sname,pname 
from supplier,supply,part 
where pname='bolt' AND supply.sno=supplier.sno AND part.pno=supply.pno;
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>SNAME</th><th>PNAME</th></tr>
                    <tr><td>Anoop</td><td>bolt</td></tr>
                    <tr><td>Ram</td><td>bolt</td></tr>
                </table>
                <h3>Query iii</h3>
                <p><b>Delete the parts which are in 'green' color.</b></p>
                <pre>
delete from part where colour='green';
                </pre>
                <h4>Output</h4>
                <pre>1 row deleted.</pre>
                <hr>
                <h2>PART B — NoSQL (MongoDB) &amp; Procedural SQL (PL/SQL)</h2>
                <h3>Aim</h3>
                <p>To perform MongoDB operations on Part and Supplier collections, and implement record copying using a PL/SQL block in Oracle.</p>
                <h3>MongoDB Collections &amp; Document Insertion</h3>
                <pre>
db.Part.insertMany([
  {PID:"P1", PName:"Bolt", Price:20},
  {PID:"P2", PName:"Nut", Price:10}
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a2157e7346482d7de8ce5af'),
    '1': ObjectId('6a2157e7346482d7de8ce5b0')
  }
}
                </pre>
                <pre>
db.Supplier.insertMany([
  {SID:1,SName:"ABC Suppliers",PID:"P1"},
  {SID:2,SName:"XYZ Suppliers",PID:"P1"},
  {SID:3,SName:"Global Parts",PID:"P2"}
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a215845c53bedb60c8ce5b1'),
    '1': ObjectId('6a215845c53bedb60c8ce5b2'),
    '2': ObjectId('6a215845c53bedb60c8ce5b3')
  }
}
                </pre>
                <h3>MongoDB Query i</h3>
                <p><b>Update the details of parts for a given part identifier: "P1".</b></p>
                <pre>
db.Part.updateOne(
  {PID:"P1"},
  {$set:{Price:25}}
);
                </pre>
                <h4>Expected Output</h4>
                <pre>{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}</pre>
                <h3>MongoDB Query ii</h3>
                <p><b>Display all suppliers who supply the part with part identifier: "P1".</b></p>
                <pre>
db.Supplier.find(
  {PID:"P1"},
  {SName:1,_id:0}
);
                </pre>
                <h4>Expected Output</h4>
                <pre>[ { SName: 'ABC Suppliers' }, { SName: 'XYZ Suppliers' } ]</pre>
                <h3>PL/SQL Program</h3>
                <p><b>Write a PL/SQL program to copy the contents of the Shipment table to another table for maintaining records for specific part number.</b></p>
                <p><b>Table Setup:</b></p>
                <pre>
CREATE TABLE Shipment (
    SID NUMBER(5),
    PID VARCHAR2(5),
    Qty NUMBER(5)
);

CREATE TABLE Shipment_Backup (
    SID NUMBER(5),
    PID VARCHAR2(5),
    Qty NUMBER(5)
);

INSERT INTO Shipment VALUES (101,'P1',50);
INSERT INTO Shipment VALUES (102,'P2',40);
INSERT INTO Shipment VALUES (103,'P1',30);
INSERT INTO Shipment VALUES (104,'P3',20);
COMMIT;

SELECT * FROM Shipment;
                </pre>
                <h4>Initial Shipment Table Output</h4>
                <table>
                    <tr><th>SID</th><th>PID</th><th>QTY</th></tr>
                    <tr><td>101</td><td>P1</td><td>50</td></tr>
                    <tr><td>102</td><td>P2</td><td>40</td></tr>
                    <tr><td>103</td><td>P1</td><td>30</td></tr>
                    <tr><td>104</td><td>P3</td><td>20</td></tr>
                </table>
                <p><b>PL/SQL Block:</b></p>
                <pre>
SET SERVEROUTPUT ON;
BEGIN
   INSERT INTO Shipment_Backup
   SELECT *
   FROM Shipment
   WHERE PID='P1';

   DBMS_OUTPUT.PUT_LINE('Records copied successfully');
END;
/
SELECT * FROM Shipment_Backup;
                </pre>
                <h4>Execution Output</h4>
                <pre>
Records copied successfully
                </pre>
                <h4>Shipment Backup Table Output</h4>
                <table>
                    <tr><th>SID</th><th>PID</th><th>QTY</th></tr>
                    <tr><td>101</td><td>P1</td><td>50</td></tr>
                    <tr><td>103</td><td>P1</td><td>30</td></tr>
                </table>
                <hr>
"""

# EXP 3
EXP_BLOCKS[3] = """<h3>Schema Diagram</h3>
                <pre>
SAILOR ( SailorID [PK], Name, Age )
BOAT ( BID [PK], BoatName, Color )
RESERVES ( SailorID [PK, FK], BID [PK, FK], Day [PK] )
                </pre>
                <h3>Create Table Statements</h3>
                <pre>
CREATE TABLE SAILOR (
    SailorID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT CHECK (Age > 0)
);

CREATE TABLE BOAT (
    BID INT PRIMARY KEY,
    BoatName VARCHAR(50),
    Color VARCHAR(20)
);

CREATE TABLE RESERVES (
    SailorID INT,
    BID INT,
    Day DATE,
    PRIMARY KEY (SailorID, BID, Day),
    FOREIGN KEY (SailorID) REFERENCES SAILOR(SailorID),
    FOREIGN KEY (BID) REFERENCES BOAT(BID)
);
                </pre>
                <h3>Insert Sample Data</h3>
                <pre>
INSERT INTO SAILOR VALUES (1, 'Ravi', 25);
INSERT INTO SAILOR VALUES (2, 'Meena', 30);
INSERT INTO SAILOR VALUES (3, 'Arun', 28);

INSERT INTO BOAT VALUES (101, 'Sea Queen', 'Red');
INSERT INTO BOAT VALUES (102, 'Wave Rider', 'Blue');
INSERT INTO BOAT VALUES (103, 'Ocean Star', 'Green');

INSERT INTO RESERVES VALUES (1, 101, '20-APR-2001');
INSERT INTO RESERVES VALUES (1, 102, '20-APR-2002');
INSERT INTO RESERVES VALUES (2, 101, '21-APR-2001');
INSERT INTO RESERVES VALUES (2, 102, '22-APR-2004');
INSERT INTO RESERVES VALUES (3, 101, '26-APR-2003');
                </pre>
                <h3>Query i</h3>
                <p><b>Obtain the details of the boats reserved by 'Ravi'.</b></p>
                <pre>
SELECT B.*
FROM BOAT B
JOIN RESERVES R ON B.BID = R.BID
JOIN SAILOR S ON S.SailorID = R.SailorID
WHERE S.Name = 'Ravi';
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>BID</th><th>BOATNAME</th><th>COLOR</th></tr>
                    <tr><td>101</td><td>Sea Queen</td><td>Red</td></tr>
                    <tr><td>102</td><td>Wave Rider</td><td>Blue</td></tr>
                </table>
                <h3>Query ii</h3>
                <p><b>Retrieve the BID of the boats reserved necessarily by all the sailors.</b></p>
                <pre>
SELECT BID
FROM RESERVES
GROUP BY BID
HAVING COUNT(DISTINCT SailorID) = (SELECT COUNT(*) FROM SAILOR);
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>BID</th></tr>
                    <tr><td>101</td></tr>
                </table>
                <h3>Query iii</h3>
                <p><b>Find the number of boats reserved by each sailor. Display the Sailor_Name along with the number of boats reserved.</b></p>
                <pre>
SELECT S.Name, COUNT(R.BID) AS TotalBoats
FROM SAILOR S
LEFT JOIN RESERVES R ON S.SailorID = R.SailorID
GROUP BY S.Name;
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>NAME</th><th>TOTALBOATS</th></tr>
                    <tr><td>Arun</td><td>1</td></tr>
                    <tr><td>Meena</td><td>2</td></tr>
                    <tr><td>Ravi</td><td>2</td></tr>
                </table>
                <hr>
                <h2>PART B — NoSQL (MongoDB) &amp; Procedural SQL (PL/SQL)</h2>
                <h3>Aim</h3>
                <p>To perform MongoDB operations on Sailor, Boat, and Reserve collections, and implement count logic using a PL/SQL block in Oracle.</p>
                <h3>MongoDB Collections &amp; Document Insertion</h3>
                <pre>
db.Sailor.insertMany([
  {SID:1,SName:"Ramesh"},
  {SID:2,SName:"Suresh"}
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a2159745fdbac8b848ce5af'),
    '1': ObjectId('6a2159745fdbac8b848ce5b0')
  }
}
                </pre>
                <pre>
db.Boat.insertMany([
  {BID:101,BName:"Sea King",Color:"Red"},
  {BID:102,BName:"Ocean Star",Color:"Blue"}
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a2159a5a394a68ce18ce5b1'),
    '1': ObjectId('6a2159a5a394a68ce18ce5b2')
  }
}
                </pre>
                <pre>
db.Reserve.insertMany([
  {SID:1,BID:101},
  {SID:1,BID:102},
  {SID:2,BID:102}
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a2159daa3049e238d8ce5b3'),
    '1': ObjectId('6a2159daa3049e238d8ce5b4'),
    '2': ObjectId('6a2159daa3049e238d8ce5b5')
  }
}
                </pre>
                <h3>MongoDB Query i</h3>
                <p><b>Obtain the number of boats reserved by sailor "Ramesh".</b></p>
                <pre>
var sailor=db.Sailor.findOne(
  {SName:"Ramesh"}
);

db.Reserve.countDocuments(
  {SID:sailor.SID}
);
                </pre>
                <h4>Expected Output</h4>
                <pre>2</pre>
                <h3>MongoDB Query ii</h3>
                <p><b>Retrieve boats of color "Blue".</b></p>
                <pre>
db.Boat.find(
  {Color:"Blue"}
);
                </pre>
                <h4>Expected Output</h4>
                <pre>[
  {
    _id: ObjectId('6a215a462dbc9d54be8ce5b2'),
    BID: 102,
    BName: 'Ocean Star',
    Color: 'Blue'
  }
]</pre>
                <h3>PL/SQL Program</h3>
                <p><b>Write a PL/SQL program to Count the number of boats.</b></p>
                <p><b>Table Setup:</b></p>
                <pre>
CREATE TABLE Boat (
    BID NUMBER(5) PRIMARY KEY,
    BName VARCHAR2(30),
    Color VARCHAR2(20)
);

INSERT INTO Boat VALUES (1,'BoatA','Red');
INSERT INTO Boat VALUES (2,'BoatB','Blue');
INSERT INTO Boat VALUES (3,'BoatC','Green');
COMMIT;

SELECT * FROM Boat;
                </pre>
                <h4>Initial Boat Table Output</h4>
                <table>
                    <tr><th>BID</th><th>BNAME</th><th>COLOR</th></tr>
                    <tr><td>1</td><td>BoatA</td><td>Red</td></tr>
                    <tr><td>2</td><td>BoatB</td><td>Blue</td></tr>
                    <tr><td>3</td><td>BoatC</td><td>Green</td></tr>
                </table>
                <p><b>PL/SQL Block:</b></p>
                <pre>
SET SERVEROUTPUT ON;
DECLARE
    v_count NUMBER;
BEGIN
    SELECT COUNT(*)
    INTO v_count
    FROM Boat;
    DBMS_OUTPUT.PUT_LINE('Total Boats = ' || v_count);
END;
/
                </pre>
                <h4>Execution Output</h4>
                <pre>
Total Boats = 3
                </pre>
                <hr>
"""

# EXP 4
EXP_BLOCKS[4] = """<h3>Schema Diagram</h3>
                <pre>
STUDENT ( StudentID [PK], Name, Gender )
BOOK ( ISBN [PK], Title, Author, Publisher )
BORROWS ( StudentID [PK, FK], ISBN [PK, FK], BorrowDate [PK] )
                </pre>
                <h3>Create Table Statements</h3>
                <pre>
CREATE TABLE STUDENT (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Gender VARCHAR(10)
);

CREATE TABLE BOOK (
    ISBN VARCHAR(10) PRIMARY KEY,
    Title VARCHAR(50),
    Author VARCHAR(50),
    Publisher VARCHAR(50)
);

CREATE TABLE BORROWS (
    StudentID INT,
    ISBN VARCHAR(10),
    BorrowDate DATE,
    PRIMARY KEY (StudentID, ISBN, BorrowDate),
    FOREIGN KEY (StudentID) REFERENCES STUDENT(StudentID),
    FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN)
);
                </pre>
                <h3>Insert Sample Data</h3>
                <pre>
INSERT INTO STUDENT VALUES (1, 'Asha', 'Female');
INSERT INTO STUDENT VALUES (2, 'Ravi', 'Male');
INSERT INTO STUDENT VALUES (3, 'Meena', 'Female');

INSERT INTO BOOK VALUES ('123', 'Database', 'Korth', 'McGraw');
INSERT INTO BOOK VALUES ('124', 'Networks', 'Tanenbaum', 'Pearson');
INSERT INTO BOOK VALUES ('125', 'AI', 'Russell', 'Elsevier');

INSERT INTO BORROWS VALUES (1, '123', '20-JAN-2001');
INSERT INTO BORROWS VALUES (1, '124', '20-JAN-2002');
INSERT INTO BORROWS VALUES (2, '125', '20-JAN-2002');
INSERT INTO BORROWS VALUES (3, '123', '20-JAN-2002');
                </pre>
                <h3>Query i</h3>
                <p><b>Obtain the names of the student who has borrowed either book bearing ISBN '123' or ISBN '124'.</b></p>
                <pre>
SELECT DISTINCT s.Name
FROM STUDENT s
JOIN BORROWS b ON s.StudentID = b.StudentID
WHERE b.ISBN IN ('123', '124');
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>NAME</th></tr>
                    <tr><td>Asha</td></tr>
                    <tr><td>Meena</td></tr>
                </table>
                <h3>Query ii</h3>
                <p><b>Obtain the Names of female students who have borrowed "Database" books.</b></p>
                <pre>
SELECT DISTINCT s.Name
FROM STUDENT s
JOIN BORROWS b ON s.StudentID = b.StudentID
JOIN BOOK bk ON b.ISBN = bk.ISBN
WHERE s.Gender = 'Female' AND bk.Title = 'Database';
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>NAME</th></tr>
                    <tr><td>Asha</td></tr>
                    <tr><td>Meena</td></tr>
                </table>
                <h3>Query iii</h3>
                <p><b>Find the number of books borrowed by each student. Display the student details along with the number of books.</b></p>
                <pre>
SELECT s.StudentID, s.Name, COUNT(b.ISBN) AS TotalBooks
FROM STUDENT s
LEFT JOIN BORROWS b ON s.StudentID = b.StudentID
GROUP BY s.StudentID, s.Name;
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>STUDENTID</th><th>NAME</th><th>TOTALBOOKS</th></tr>
                    <tr><td>1</td><td>Asha</td><td>2</td></tr>
                    <tr><td>2</td><td>Ravi</td><td>1</td></tr>
                    <tr><td>3</td><td>Meena</td><td>1</td></tr>
                </table>
                <hr>
                <h2>PART B — NoSQL (MongoDB) &amp; Procedural SQL (PL/SQL)</h2>
                <h3>Aim</h3>
                <p>To perform MongoDB operations on Book and Student collections, and implement price adjustments using a PL/SQL block in Oracle.</p>
                <h3>MongoDB Collections &amp; Document Insertion</h3>
                <pre>
db.Book.insertMany([
  { Book_ID:1, Title:"Database Systems", Author:"Navathe", Price:500 },
  { Book_ID:2, Title:"Python Programming", Author:"John", Price:400 }
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a2271ee9153378f068ce5af'),
    '1': ObjectId('6a2271ee9153378f068ce5b0')
  }
}
                </pre>
                <pre>
db.Student.insertMany([
  { SID:1, SName:"Kushal", Book_ID:1 },
  { SID:2, SName:"Priya", Book_ID:2 }
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a227252494b62d38a8ce5af'),
    '1': ObjectId('6a227252494b62d38a8ce5b0')
  }
}
                </pre>
                <h3>MongoDB Query i</h3>
                <p><b>Obtain the book details authored by "Navathe".</b></p>
                <pre>
db.Book.find(
  {Author:"Navathe"}
);
                </pre>
                <h4>Expected Output</h4>
                <pre>[
  {
    _id: ObjectId('6a2272c847771f32118ce5af'),
    Book_ID: 1,
    Title: 'Database Systems',
    Author: 'Navathe',
    Price: 500
  }
]</pre>
                <h3>MongoDB Query ii</h3>
                <p><b>Obtain the Names of students who have borrowed "Database" books.</b></p>
                <pre>
var book=db.Book.findOne(
  {Title:"Database Systems"}
);

db.Student.find(
  {Book_ID:book.Book_ID},
  {SName:1,_id:0}
);
                </pre>
                <h4>Expected Output</h4>
                <pre>[ { SName: 'Kushal' } ]</pre>
                <h3>PL/SQL Program</h3>
                <p><b>Write a PL/SQL program to increase the price of all books by 10%.</b></p>
                <p><b>Table Setup:</b></p>
                <pre>
CREATE TABLE Book (
    Book_ID NUMBER(5) PRIMARY KEY,
    Title VARCHAR2(50),
    Author VARCHAR2(50),
    Price NUMBER(8,2)
);

INSERT INTO Book VALUES (101, 'Database Systems', 'Navathe', 500);
INSERT INTO Book VALUES (102, 'Operating Systems', 'Galvin', 600);
INSERT INTO Book VALUES (103, 'Python Programming', 'John', 450);
INSERT INTO Book VALUES (104, 'Computer Networks', 'Tanenbaum', 550);
COMMIT;

SELECT * FROM Book;
                </pre>
                <h4>Initial Book Table Output</h4>
                <table>
                    <tr><th>BOOK_ID</th><th>TITLE</th><th>AUTHOR</th><th>PRICE</th></tr>
                    <tr><td>101</td><td>Database Systems</td><td>Navathe</td><td>500</td></tr>
                    <tr><td>102</td><td>Operating Systems</td><td>Galvin</td><td>600</td></tr>
                    <tr><td>103</td><td>Python Programming</td><td>John</td><td>450</td></tr>
                    <tr><td>104</td><td>Computer Networks</td><td>Tanenbaum</td><td>550</td></tr>
                </table>
                <p><b>PL/SQL Block:</b></p>
                <pre>
BEGIN
    UPDATE Book
    SET Price = Price * 1.10;
    DBMS_OUTPUT.PUT_LINE('Book prices updated');
END;
/
SELECT * FROM Book;
                </pre>
                <h4>Execution Output</h4>
                <pre>
Book prices updated
                </pre>
                <h4>Updated Book Table Output</h4>
                <table>
                    <tr><th>BOOK_ID</th><th>TITLE</th><th>AUTHOR</th><th>PRICE</th></tr>
                    <tr><td>101</td><td>Database Systems</td><td>Navathe</td><td>550</td></tr>
                    <tr><td>102</td><td>Operating Systems</td><td>Galvin</td><td>660</td></tr>
                    <tr><td>103</td><td>Python Programming</td><td>John</td><td>495</td></tr>
                    <tr><td>104</td><td>Computer Networks</td><td>Tanenbaum</td><td>605</td></tr>
                </table>
                <hr>
"""

# EXP 5
EXP_BLOCKS[5] = """<h3>Schema Diagram</h3>
                <pre>
PATIENT ( Patient_ID [PK], Name, Age, Gender )
DOCTOR ( Doctor_ID [PK], Name, Specialization )
APPOINTMENT ( Patient_ID [PK, FK], Doctor_ID [PK, FK], Appointment_Date [PK] )
                </pre>
                <h3>Create Table Statements</h3>
                <pre>
CREATE TABLE PATIENT (
    Patient_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Gender VARCHAR(10)
);

CREATE TABLE DOCTOR (
    Doctor_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Specialization VARCHAR(50)
);

CREATE TABLE APPOINTMENT (
    Patient_ID INT,
    Doctor_ID INT,
    Appointment_Date DATE,
    PRIMARY KEY(Patient_ID, Doctor_ID, Appointment_Date),
    FOREIGN KEY(Patient_ID) REFERENCES PATIENT(Patient_ID),
    FOREIGN KEY(Doctor_ID) REFERENCES DOCTOR(Doctor_ID)
);
                </pre>
                <h3>Insert Sample Data</h3>
                <pre>
INSERT INTO PATIENT VALUES (1, 'Anu', 22, 'Female');
INSERT INTO PATIENT VALUES (2, 'Ravi', 30, 'Male');

INSERT INTO DOCTOR VALUES (101, 'Dr. Kumar', 'Cardiology');
INSERT INTO DOCTOR VALUES (102, 'Dr. Meena', 'Dermatology');

INSERT INTO APPOINTMENT VALUES (1, 101, '01-JAN-2024');
INSERT INTO APPOINTMENT VALUES (1, 102, '02-JAN-2024');
INSERT INTO APPOINTMENT VALUES (2, 101, '03-JAN-2024');
                </pre>
                <h3>Query i</h3>
                <p><b>Retrieve the details of doctors consulted by 'Ravi'.</b></p>
                <pre>
SELECT D.*
FROM DOCTOR D
JOIN APPOINTMENT A ON D.Doctor_ID = A.Doctor_ID
JOIN PATIENT P ON A.Patient_ID = P.Patient_ID
WHERE P.Name = 'Ravi';
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>DOCTOR_ID</th><th>NAME</th><th>SPECIALIZATION</th></tr>
                    <tr><td>101</td><td>Dr. Kumar</td><td>Cardiology</td></tr>
                </table>
                <h3>Query ii</h3>
                <p><b>Find the DoctorIDs of doctors consulted by all patients.</b></p>
                <pre>
SELECT Doctor_ID
FROM APPOINTMENT
GROUP BY Doctor_ID
HAVING COUNT(DISTINCT Patient_ID) = (SELECT COUNT(*) FROM PATIENT);
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>DOCTOR_ID</th></tr>
                    <tr><td>101</td></tr>
                </table>
                <h3>Query iii</h3>
                <p><b>For each patient, find the number of doctors consulted. Display Patient_Name with the count.</b></p>
                <pre>
SELECT P.Name, COUNT(A.Doctor_ID) AS Doctor_Count
FROM PATIENT P
LEFT JOIN APPOINTMENT A ON P.Patient_ID = A.Patient_ID
GROUP BY P.Name;
                </pre>
                <h4>Output</h4>
                <table>
                    <tr><th>NAME</th><th>DOCTOR_COUNT</th></tr>
                    <tr><td>Anu</td><td>2</td></tr>
                    <tr><td>Ravi</td><td>1</td></tr>
                </table>
                <hr>
                <h2>PART B — NoSQL (MongoDB) &amp; Procedural SQL (PL/SQL)</h2>
                <h3>Aim</h3>
                <p>To perform MongoDB operations on Doctor and Patient collections, and implement fee adjustment logic using a PL/SQL block in Oracle.</p>
                <h3>MongoDB Collections &amp; Document Insertion</h3>
                <pre>
db.Doctor.insertMany([
  { Doctor_ID:1, Doctor_Name:"Dr. Kumar", Specialization:"Cardiology", Fee:1000 },
  { Doctor_ID:2, Doctor_Name:"Dr. Ravi", Specialization:"Neurology", Fee:1200 }
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a2275b652a9f4050d8ce5af'),
    '1': ObjectId('6a2275b652a9f4050d8ce5b0')
  }
}
                </pre>
                <pre>
db.Patient.insertMany([
  { Patient_ID:1, Patient_Name:"Anita", Doctor_ID:1, Appointment_Date:"2025-05-10" },
  { Patient_ID:2, Patient_Name:"Shruti", Doctor_ID:1, Appointment_Date:"2025-05-10" },
  { Patient_ID:3, Patient_Name:"Meena", Doctor_ID:2, Appointment_Date:"2025-05-12" }
]);
                </pre>
                <h4>Output</h4>
                <pre>
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a2275f4e935b4340f8ce5b1'),
    '1': ObjectId('6a2275f4e935b4340f8ce5b2'),
    '2': ObjectId('6a2275f4e935b4340f8ce5b3')
  }
}
                </pre>
                <h3>MongoDB Query i</h3>
                <p><b>List all the patients treated by the doctor named "Dr. Kumar".</b></p>
                <pre>
var doc=db.Doctor.findOne(
  {Doctor_Name:"Dr. Kumar"}
);

db.Patient.find(
  {Doctor_ID:doc.Doctor_ID},
  {Patient_Name:1,_id:0}
);
                </pre>
                <h4>Expected Output</h4>
                <pre>[ { Patient_Name: 'Anita' }, { Patient_Name: 'Shruti' } ]</pre>
                <h3>MongoDB Query ii</h3>
                <p><b>Display the names of patients who have an appointment on date "2025-05-10".</b></p>
                <pre>
db.Patient.find(
  {Appointment_Date:"2025-05-10"},
  {Patient_Name:1,_id:0}
);
                </pre>
                <h4>Expected Output</h4>
                <pre>[ { Patient_Name: 'Anita' }, { Patient_Name: 'Shruti' } ]</pre>
                <h3>PL/SQL Program</h3>
                <p><b>Write a PL/SQL program that increases the consultation fee of all doctors in specialization 'Cardiology' by 20%.</b></p>
                <p><b>Table Setup:</b></p>
                <pre>
CREATE TABLE Doctor (
    Doctor_ID NUMBER(5) PRIMARY KEY,
    Doctor_Name VARCHAR2(20),
    Specialization VARCHAR2(20),
    Fee NUMBER(8,2)
);

INSERT INTO Doctor VALUES (101, 'Dr. Kumar', 'Cardiology', 1000);
INSERT INTO Doctor VALUES (102, 'Dr. Ravi', 'Neurology', 1200);
INSERT INTO Doctor VALUES (103, 'Dr. Meena', 'Cardiology', 1500);
INSERT INTO Doctor VALUES (104, 'Dr. Priya', 'Orthopedics', 1300);
COMMIT;

SELECT * FROM Doctor;
                </pre>
                <h4>Initial Doctor Table Output</h4>
                <table>
                    <tr><th>DOCTOR_ID</th><th>DOCTOR_NAME</th><th>SPECIALIZATION</th><th>FEE</th></tr>
                    <tr><td>101</td><td>Dr. Kumar</td><td>Cardiology</td><td>1200</td></tr>
                    <tr><td>102</td><td>Dr. Ravi</td><td>Neurology</td><td>1200</td></tr>
                    <tr><td>103</td><td>Dr. Meena</td><td>Cardiology</td><td>1800</td></tr>
                    <tr><td>104</td><td>Dr. Priya</td><td>Orthopedics</td><td>1300</td></tr>
                </table>
                <p><b>PL/SQL Block:</b></p>
                <pre>
SET SERVEROUTPUT ON;
DECLARE
    v_count NUMBER;
BEGIN
    UPDATE Doctor
    SET Fee = Fee * 1.20
    WHERE Specialization = 'Cardiology';

    v_count := SQL%ROWCOUNT;
    DBMS_OUTPUT.PUT_LINE(v_count || ' doctors updated');
END;
/
SELECT * FROM Doctor;
                </pre>
                <h4>Execution Output</h4>
                <pre>
2 doctors updated
                </pre>
                <h4>Updated Doctor Table Output</h4>
                <table>
                    <tr><th>DOCTOR_ID</th><th>DOCTOR_NAME</th><th>SPECIALIZATION</th><th>FEE</th></tr>
                    <tr><td>101</td><td>Dr. Kumar</td><td>Cardiology</td><td>1440</td></tr>
                    <tr><td>102</td><td>Dr. Ravi</td><td>Neurology</td><td>1200</td></tr>
                    <tr><td>103</td><td>Dr. Meena</td><td>Cardiology</td><td>2160</td></tr>
                    <tr><td>104</td><td>Dr. Priya</td><td>Orthopedics</td><td>1300</td></tr>
                </table>
                <hr>
"""

def replace_in_html(content: str, exp_num: int) -> str:
    # Matches from <h3>Schema Diagram</h3> to <h2>Result</h2> or <hr>\n\n<h2>Result</h2>
    pattern = r'<h3>Schema Diagram</h3>[\s\S]*?(?:<hr>\s*)?<h2>Result</h2>'
    replacement = EXP_BLOCKS[exp_num] + "\\n                <h2>Result</h2>"
    
    # In individual files, Result has slightly different formatting, let's accommodate it:
    if "<h2>Result</h2>" not in content and "<h2>Result</h2>" in content.upper():
         replacement = EXP_BLOCKS[exp_num] + "\\n<h2>Result</h2>"
         pattern = r'<h3>Schema Diagram</h3>[\s\S]*?(?:<hr>\s*)?<h2>Result</h2>'
         
    new_content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
    print(f"Replaced {count} occurrences for Exp {exp_num}")
    return new_content

def update_individual_files():
    for n in range(1, 6):
        path = ROOT / "DBMS_LAB" / f"{n}.html"
        if path.exists():
            print(f"Processing {path.name}...")
            text = path.read_text(encoding="utf-8")
            new_text = replace_in_html(text, n)
            path.write_text(new_text, encoding="utf-8")

def update_combined_file():
    path = ROOT / "DBMS_Lab_Book.html"
    if path.exists():
        print(f"Processing {path.name}...")
        text = path.read_text(encoding="utf-8")
        
        for n in range(1, 6):
            start_tag = f'<div id="experiment-{n}" class="lab-section">'
            if start_tag not in text:
                print(f"Could not find {start_tag}")
                continue
            
            start_idx = text.find(start_tag)
            
            if n < 5:
                end_tag = f'<div id="experiment-{n+1}" class="lab-section">'
                end_idx = text.find(end_tag)
            else:
                end_idx = text.rfind("</div>\\n\\n    <script>")
                if end_idx == -1:
                    end_idx = text.rfind("</div>\\n    <script>")
                if end_idx == -1:
                    end_idx = len(text)
            
            if start_idx != -1 and end_idx != -1:
                section_content = text[start_idx:end_idx]
                updated_section = replace_in_html(section_content, n)
                text = text[:start_idx] + updated_section + text[end_idx:]
                
        path.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    update_individual_files()
    update_combined_file()
    print("All DBMS code blocks updated successfully!")
