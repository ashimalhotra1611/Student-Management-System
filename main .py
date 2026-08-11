import json

# Load students data
try:
    with open("students.json", "r") as file:
        students = json.load(file)

except FileNotFoundError:
    students = []

except json.JSONDecodeError:
    print("Error: students.json file is corrupted.")
    students = []


while True:
    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        print("\nAdd Student")

        name = input("Enter Student Name: ").strip()
        roll = input("Enter Roll Number: ").strip()

        # Age error handling
        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

        except ValueError:
            print("Invalid age! Please enter a number.")
            continue

        course = input("Enter Course: ").strip()

        # Empty input checking
        if name == "" or roll == "" or course == "":
            print("Name, Roll Number and Course cannot be empty.")
            continue

        # Duplicate roll number checking
        duplicate = False

        for student in students:
            if student["roll"] == roll:
                duplicate = True
                break

        if duplicate:
            print("Roll Number already exists!")
            continue

        student = {
            "name": name,
            "roll": roll,
            "age": age,
            "course": course
        }

        students.append(student)

        try:
            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

            print("\nStudent Added Successfully!")

        except OSError:
            print("Error: Unable to save student data.")

    # View Student
    elif choice == "2":
        print("\n----- Student List -----")

        if len(students) == 0:
            print("No student found.")

        else:
            for student in students:
                print("Name:", student["name"])
                print("Roll Number:", student["roll"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("----------------")

    # Search Student
    elif choice == "3":
        roll = input("Enter Roll Number to search: ").strip()

        if roll == "":
            print("Roll Number cannot be empty.")
            continue

        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Roll Number:", student["roll"])
                print("Age:", student["age"])
                print("Course:", student["course"])

                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "4":
        roll = input("Enter Roll Number to delete: ").strip()

        if roll == "":
            print("Roll Number cannot be empty.")
            continue

        found = False

        for student in students:
            if student["roll"] == roll:
                students.remove(student)

                try:
                    with open("students.json", "w") as file:
                        json.dump(students, file, indent=4)

                    print("Student deleted successfully!")

                except OSError:
                    print("Error: Unable to save changes.")

                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")