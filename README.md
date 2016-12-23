Academic Tracker
================

This tracker is based on a giant ugly spreadsheet made by Leo Bowen-Biggs to keep track of when he did coursework at WPI.
It has been generalized and formalized for use by many people and to aggregate data in easier ways.

The current implemenation uses python and sqlite3. 

# Data Format
Version 1.0

## Tables
The following tables exist:

* Students {student_id, name}
* ProgramRegistrations {student_id, program, department}
* Departments {department, full_name, field}
* Classes {class_id, department, course_number, full_name, short_name, term, year, professor, is_project, units}
* Registrations {student_id, class_id}
* Activites {Student_id, class_id, start_time, end_time, activity, notes}
* CourseSurveys {student_id, class_id, final_grade, difficulty, enjoyment, interest}

## Definitions
Some definitions:

* A *department* is the short code for subjects. Some values it can take are "CS", "ECE", and "RBE". The department also has a full name, such as "Computer Science", "Electrical and Computer Engineering", and "Robotics Engineering". 
* A *Field* is the general subject a department may be in. At this time, it must take one of the following values:
  * "Engineering" including Computer Science
  * "Science" including Mathematics
  * "Humanities and Arts"
  * "Social Science"
* *isProject* is 1 if the course is an ISP, IQP, or MQP, and 0 otherwise.
* *units* is the number of units at WPI the class is worth. This is a real number, as most classes are worth 1/3 of a Unit
* In the course survey, *difficulty*, *enjoyment*, and *interest* are all integer values between 0 and 10, where 10 indicates the maximum positive, eg "maximum difficulty" or "maximum enjoyment". These values are relative only to the student's personal beliefs. 
* A *term* is the name of the term it was taken. It accepts the following values:
  * A
  * B
  * C
  * D
  * E1
  * E2
  * Fall
  * Spring
  * Summer
* *final_grade* is the letter grade recieved for the class. This can be one of the following: "A", "B", "C", "NR", "F", "D", "I", or "SP"
* *start_time* and *end_time* are represented using sqlite3 datetime. 
* An *activity* is one of the following: "reading", "lecture", "exam", "homework", "lab", or  "final project". reading, homework, and final project are considered to be outside of class.

## Representing unusual cases
To represent an MQP or other multi-credit class that spans multiple terms, use a seperate entry into Classes and Registrations. 

For example, to represent an MQP (1 Unit = 9 Credits) divided evenly in 1 semester, do:

```
Classes: 
1939, CS, 4000, A, 2017, Lane Harrison, True, 0.5
1940, CS, 4000, B, 2017, Lane Harrison, True, 0.5

Registrations:
1, 1939
1, 1940
```

This representation is similar to what is seen on the WPI transcript.
