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
* Class {class_id, department, course_number, full_name, short_name, term, year, professor, is_project, units}
* Registrations {student_id, class_id}
* ActivityLog {Student_id, class_id, start_time, end_time, activity, notes}
* CourseSurvey {student_id, class_id, final_grade, difficulty, enjoyment, interest}

## Definitions
Some definitions:

* A *department* is the short code for subjects. Some values it can take are "CS", "ECE", and "RBE". The department also has a full name, such as "Computer Science", "Electrical and Computer Engineering", and "Robotics Engineering". 
* A *Field* is the general subject a department may be in. At this time, it must take one of the following values:
  * "Engineering" including Computer Science
  * "Science" including Mathematics
  * "Humanities and Arts"
  * "Social Science"
* *isProject* is true if the course is an ISP, IQP, or MQP.
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
* A *date* starts at either sunrise or when the student woke up, wichever is earlier. The date ends when the following date begins. If an activity spans date boundries, then it belongs with the date in which it was started.

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
