def search_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            print("\n----- STUDENT DETAILS -----")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("Branch:", student["branch"])

            if "python" in student:
                print("Python Marks:", student["python"])
                print("Mathematics Marks:", student["mathematics"])
                print("English Marks:", student["english"])

            return

    print("\nStudent not found!")