/*Write a SQL query that transponses columns and rows of the table A*/

CREATE TABLE A (
ID int not null,
Name varchar(10) not null,
Val int not null
);

INSERT INTO A (ID, Name, Val)
VALUES (1, 'A',10), (1,'B',9),(2, 'B',8), (2,'C',7),(3, 'A',6), (3,'C',5);
Select * from A;

CREATE VIEW A_answer AS 
select ID,
  sum(case when Name = 'A' then Val else 0 end) A,
  sum(case when Name = 'B' then Val else 0 end) B,
  sum(case when Name = 'C' then Val else 0 end) C
from A
group by ID;

Select * from A_answer;
