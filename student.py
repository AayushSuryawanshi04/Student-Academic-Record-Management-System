def add_student(students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")

    student = {
        "id": student_id,
        "name": name,
        "branch": branch
    }

    students.append(student)

    print("\nStudent added successfully!")