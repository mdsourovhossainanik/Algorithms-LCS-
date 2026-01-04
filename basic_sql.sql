 
create database college;
use college;
CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT,
    semester INT,
    batch VARCHAR(20)
);

INSERT INTO student (id, name, marks, semester, batch) VALUES
(1, 'Anik',   85, 1, '2023'),
(2, 'Atik',   78, 1, '2023'),
(3, 'Suvo',   92, 2, '2022'),
(4, 'Nusrat', 88, 2, '2022'),
(5, 'Rahim',  74, 3, '2021'),
(6, 'Karim',  81, 3, '2021'),
(7, 'Sadia',  95, 4, '2020'),
(8, 'Mehedi', 69, 4, '2020'),
(9, 'Tania',  77, 5, '2019'),
(10,'Rafiq',  90, 5, '2019');

select distinct * from student; #distinct  duplicate value bad dey
#where clause:
select* from student where marks>80;   #where condition
select* from student where name= "Anik" and marks>80; 
select* from student where  marks+10>100; 
select* from student where  marks=85; 
select* from student where  marks between 90 and 100; 
select* from student where  batch in(2021,2023);
select* from student where  batch not in(2021); 

#Limit clause: row k select korbe
select* from student limit 3;
select* from student where marks>80 limit 3; #3 ta student k select korbe jader marks >80.alter
select* from student order by marks asc; #assendending order 
select* from student order by marks desc limit 1; #top marks

#Aggregate function:count(),max(),min(),sum(),avg(): populer use
select max(marks) from student;
select avg(marks) from student;
select count( name) from student;

#Group by clause:
select batch,count(name) from student group by batch; #batch colum er same value niye alada alada group korbe
select semester,count(name) from student group by semester;#create group based on semester
select semester,batch ,count(name) from student group by semester,batch; #multiple group
select batch,semester,avg(marks)  from student group by batch,semester;
select batch,semester,sum(marks)  from student group by batch,semester;
select batch,semester,avg(marks)  from student group by batch,semester order by avg(marks);#assending order based on semester
select batch,semester,avg(marks)  from student group by batch,semester order by avg(marks) desc;
select batch,semester,avg(marks)  from student group by batch,semester order by avg(marks) desc limit 1;
CREATE TABLE payment (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    method VARCHAR(30),
    city VARCHAR(50)
);
INSERT INTO payment (customer_id, name, method, city) VALUES
(1, 'Anik', 'Credit Card', 'Dhaka'),
(2, 'Atik', 'Cash', 'Chittagong'),
(3, 'Suvo', 'Bkash', 'Khulna'),
(4, 'Mehedi', 'Nagad', 'Rajshahi'),
(5, 'Rakib', 'Bank Transfer', 'Sylhet'),
(6, 'Sajid', 'Credit Card', 'Dhaka'),
(7, 'Rafi', 'Cash', 'Barishal'),
(8, 'Shanto', 'Bkash', 'Dhaka'),
(9, 'Tonmoy', 'Debit Card', 'Comilla'),
(10, 'Hasan', 'Nagad', 'Rangpur');
select * from payment;
select method,count(customer_id) as Total_payment from payment group by method;
select city,method,count(customer_id) as Total_payment from payment group by city,method order by method;

#Having clause: use for condition based on group
select city,method,count(customer_id) as Total_payment from payment group by city,method   order by method ;
SELECT city, method, COUNT(customer_id) AS Total_payment
FROM payment
GROUP BY city, method
HAVING COUNT(customer_id) >= 2
ORDER BY method;

# flow to General Order :
#select colums_name;
#from table_name;
#where condition;(condition based on row that table)
#group by colums_name;
#having condition;(condition based on group)
#order by colums_name asc/dsc;

#Table related queries(update)
update student 
set marks=0
where marks=85 and id=1; #UPDATE বা DELETE করতে হলে তোমার WHERE condition-এ Primary Key / Indexed Column থাকতে হবে।
update student 
set marks=1
where marks<80;
update student 
set name="Md Sourov Hossain anik"
where id=1;
set sql_safe_updates=0; #off safe mode
set sql_safe_updates=1; #on safe mode
update student 
set marks=98,marks=80
where id=1 or marks<80;

update student 
set marks=90

where marks between 60 and 70;

alter table student  #creating a new static colum with table
add column Grade varchar(5);
update student 
set Grade="A+"
where marks between 90 and 100; 
update student 
set Grade="A"
where marks between 80 and 89; 
update student 
set Grade="A-"
where marks between 70 and 79; 
update student 
set Grade="B"
where marks between 60 and 69; 
update student 
set marks=22
where id=1;
#sort form:
UPDATE student
SET Grade = CASE
    WHEN marks BETWEEN 90 AND 100 THEN 'A+'
    WHEN marks BETWEEN 80 AND 89  THEN 'A'
    WHEN marks BETWEEN 70 AND 79  THEN 'A-'
    WHEN marks BETWEEN 60 AND 69  THEN 'B'
    ELSE 'F'
END;
update student #for all student 3 marks added
set marks=marks+3;

update student 
set marks=marks-10
where id =1;

#generated a dynamic column (virtual/stored)
ALTER TABLE student  #creating a ne colum part
ADD COLUMN grade_dynamic VARCHAR(2) 

AS (   #ASuse  for dynamic colum
    CASE   #case is a logical statement
        WHEN marks BETWEEN 90 AND 100 THEN 'A+'
        WHEN marks BETWEEN 80 AND 89  THEN 'A'
        WHEN marks BETWEEN 70 AND 79  THEN 'A-'
        WHEN marks BETWEEN 60 AND 69  THEN 'B'
        ELSE 'F'
    END  #end means case statement ses kora bujacca
) STORED; # -- অথবা VIRTUAL STORED means database physically save hbe/VIRTUAL means calculate হবে query execution সময়, storage লাগবে না।
update student
set marks =25 #akhun update korlam grade auto change hoye jabe
where id=1 or id=2;
select* from student;

