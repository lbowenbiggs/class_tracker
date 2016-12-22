import sqlite3

def create_user(cursor, uname):
	cursor.execute("SELECT MAX(student_id) FROM Students")
	max_uid = cursor.fetchone()[0]
	new_id = max_uid + 1;
	tup = (new_id, uname)
	cursor.execute("INSERT INTO Students VALUES (?, ?)", tup)
	return new_id

conn = sqlite3.connect("academics.db")
c = conn.cursor()

c.execute("SELECT COUNT(*) FROM Students")
num_students = c.fetchone()[0]

print "Welcome to the Python front-end for academic tracking!" 
print "There are " + str(num_students) + " students in the database"

uname = raw_input("What is your name? ")
tupname = (uname,)

c.execute("SELECT student_id FROM Students WHERE name=?", tupname)
uid_tuple = c.fetchone()

if uid_tuple == None:
	print "Welcome " + uname + "! Creating a record for you"
	uid = create_user(c, uname)
else:
	print "Welcome back " + uname
	uid = uid_tuple[0]

conn.commit()
conn.close()
