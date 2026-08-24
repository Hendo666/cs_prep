import sqlite3


def get_db_connection():
    conn = sqlite3.connect("school.db")
    return conn

def add_student():
    name = input("Enter the student's name: ")
    course = input("Enter the student's course: ")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO students (name, course) VALUES (?, ?)", (name, course))

    conn.commit()
    conn.close()

    print(f"{name} added successfully!")
1
def view_student():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    print("\n--- Student list ---")
    for student in students:
        print(f"ID: {student[0]} | Name: {student[1]} | Course: {student[2]}")

def update_student():
    student_id = input("Enter the ID of the student to update: ")

    new_course = input("Enter the new course: ")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE students SET course = ? WHERE id = ?", (new_course, student_id))

    conn.commit()
    conn.close()

    print(f"Student ID {student_id} updated successfully!")

def delete_student():
    student_id = input("Enter the ID of the student to delete: ")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id))

    conn.commit()
    conn.close()

    print(f"Student ID {student_id} successfully deleted.")
        

def main():
    while True:
        print("\n--- Student Registration System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Course")
        print("4. Delete Student")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

main()