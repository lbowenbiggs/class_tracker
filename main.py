import sqlite3

conn = sqlite3.connect("academics.db")
c = conn.cursor()

c.execute("SELECT COUNT(*) FROM Students")

print "Welcome to the Python front-end for academic tracking! There are " + str(c.fetchone()[0]) + " students in the database"
