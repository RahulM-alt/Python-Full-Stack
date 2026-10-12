
Q: Insert a student with StudentID 13, RegID 1012, name Arun, course Python, place Kochi, and phone number +919876543210.

INSERT INTO Students
VALUES (13, 1012, 'Arun', 'Python', 'Kochi', '+919876543210');


---


Q: Display the student name and StudentID increased by 100 for students studying Python.

SELECT StudentName, StudentID + 100 AS NewID
FROM Students
WHERE Course = 'Python';


---

Q: Display the different places of students who are studying C++.

SELECT DISTINCT Place
FROM Students
WHERE Course = 'C++';


---


Q: Display students whose course is Python and whose place is Kottayam.

SELECT *
FROM Students
WHERE Course = 'Python'
AND Place = 'Kottayam';


---

Q: Display students who are studying either Python, Java, or C++.

SELECT *
FROM Students
WHERE Course = 'Python'
OR Course = 'JAVA'
OR Course = 'C++';


---

Q: Display students who are not from Trivandrum and are not studying Python.

SELECT *
FROM Students
WHERE NOT Place = 'Trivandrum'
AND NOT Course = 'Python';


---

Q: Display students who are studying Python or Java and are from Kottayam or Trivandrum.

SELECT *
FROM Students
WHERE (Course = 'Python' OR Course = 'JAVA')
AND (Place = 'Kottayam' OR Place = 'Trivandrum');

Important: Parentheses help group the conditions correctly.


---

Q: Display StudentName and StudentID multiplied by 5, and arrange the result from highest to lowest.

SELECT StudentName, StudentID * 5 AS Result
FROM Students
ORDER BY Result DESC;


---

Q: Display all different courses in alphabetical order.

SELECT DISTINCT Course
FROM Students
ORDER BY Course ASC;


---

Q: Display the names, courses and places of students who are not from Mumbai or Goa, who are studying either Python or Java, and arrange them by name.

SELECT StudentName, Course, Place
FROM Students
WHERE NOT (Place = 'Mumbai' OR Place = 'Goa')
AND (Course = 'Python' OR Course = 'JAVA')
ORDER BY StudentName ASC;

