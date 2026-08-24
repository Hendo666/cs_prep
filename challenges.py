import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Find the highest score
cursor.execute("""
SELECT AVG(grades.score)
FROM grades
JOIN students ON grades.student_id = students.id 
""")

# Get the result out of the box
average_score = cursor.fetchone()[0]

print(f"The school's average score is {average_score}")

conn.close()