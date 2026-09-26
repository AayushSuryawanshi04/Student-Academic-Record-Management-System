def enter_marks(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            student["python"] = int(input("Enter Python marks: "))
            student["mathematics"] = int(input("Enter Mathematics marks: "))
            student["english"] = int(input("Enter English marks: "))

            print("\nMarks added successfully!")
            return

    print("\nStudent not found!")