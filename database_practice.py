import sqlite3

# 1. Connect to a database (it creates the file if the file doesn't exist)
conn = sqlite3.connect("my_uni_practice.db")

# 2. Create a cursor (this is how you execute SQL)
cursor = conn.cursor()

# 3. Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL,
    course TEXT NOT NULL
)
""")

# 4. Insert some data
cursor.execute("INSERT INTO students (name, course) VALUES ('Euan', 'Computer Science')")
cursor.execute("INSERT INTO students (name, course) VALUES ('Anna', 'Web Dev')")
cursor.execute("INSERT INTO students (name, course) VALUES ('Ben', 'AI')")

# 5. Save the cahnges
conn.commit()

# 6. Query the data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()