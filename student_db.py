import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

#Create a students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT NOT NULL
)
""")

#Create the grades table
cursor.execute("""
CREATE TABLE IF NOT EXISTS grades(
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT NOT NULL,
    score INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id)
)
""")

#Insert students 
cursor.execute("INSERT INTO students (name, course) VALUES ('Euan', 'Computer Science')")
cursor.execute("INSERT INTO students (name, course) VALUES ('Anna', 'Web Development')")
cursor.execute("INSERT INTO students (name, course) VALUES ('Ben', 'AI')")

#Get the student IDs (we need them for the grades table)
cursor.execute("SELECT id FROM students WHERE name = 'Euan'")
euan_id = cursor.fetchone()[0]

cursor.execute("SELECT id FROM students WHERE name = 'Anna'")
anna_id = cursor.fetchone()[0]

cursor.execute("SELECT id FROM students WHERE name = 'Ben'")
ben_id = cursor.fetchone()[0]

#Insert grades for each student
cursor.execute("INSERT INTO grades (student_id, subject, score) VALUES (?, ?, ?)", (euan_id, "Maths", 85))
cursor.execute("INSERT INTO grades (student_id, subject, score) VALUES (?, ?, ?)", (euan_id, "Python", 92))
cursor.execute("INSERT INTO grades (student_id, subject, score) VALUES (?, ?, ?)", (anna_id, "HTML", 78))
cursor.execute("INSERT INTO grades (student_id, subject, score) VALUES (?, ?, ?)", (anna_id, "CSS", 88))
cursor.execute("INSERT INTO grades (student_id, subject, score) VALUES (?, ?, ?)", (ben_id, "AI Ethics", 95))

conn.commit()
print("Data inserted successfully!")
conn.close()