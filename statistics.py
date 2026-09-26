def show_statistics(students):
    if len(students) == 0:
        print("\nNo students found!")
        return

    total_students = len(students)
    total_marks = 0
    count = 0

    for student in students:
        if "python" in student:

            marks = (
                student["python"]
                + student["mathematics"]
                + student["english"]
            )

            total_marks = total_marks + marks
            count = count + 1

    print("\n----- CLASS STATISTICS -----")
    print("Total Students:", total_students)

    if count > 0:
        average = total_marks / count
        print("Class Average:", average)
    else:
        print("Marks are not entered for any student.")