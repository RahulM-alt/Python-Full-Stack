create database mashup
use mashup
CREATE TABLE student (
  ID INT PRIMARY KEY,
  name VARCHAR(20),
  place VARCHAR(20),
  course VARCHAR(20),
  phone VARCHAR(10),
  mark INT
);
  
  SELECT ID AS 'Students ID'
From students;
ALTER TABLE student
RENAME TO students;
ALTER TABLE students
MODIFY COLUMN course varchar(20);

ALTER TABLE students
DROP COLUMN mark;

create table teachers(
    id int PRIMARY KEY,
    name varchar (20)
    );
    DROP TABLE teachers