import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

#JOIN students and grades together
cursor.execute("""
SELECT students.name, grades.subject, grades.score
FROM students
JOIN grades ON students.id = grades.student_id
ORDER BY students.name
""")

rows = cursor.fetchall()

print("Student Grades: ")
print("---------------")
for row in rows:
    print(f"{row[0]} - {row[1]}: {row[2]}")

    conn.close()