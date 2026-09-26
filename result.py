def calculate_result(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            if "python" not in student:
                print("\nMarks not entered yet!")
                return

            total = (
                student["python"]
                + student["mathematics"]
                + student["english"]
            )

            percentage = total / 3

            print("\n----- RESULT -----")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("Total Marks:", total)
            print("Percentage:", percentage)

            if percentage >= 40:
                print("Result: PASS")
            else:
                print("Result: FAIL")

            return

    print("\nStudent not found!")