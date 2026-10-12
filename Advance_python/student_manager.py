import json
import os

FILE_NAME = "students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("The JSON file is invalid.")
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    student = {
        "id": len(students) + 1,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Marks: {student['marks']}"
        )


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Try again.")
