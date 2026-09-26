from student import add_student
from marks import enter_marks
from result import calculate_result
from search import search_student
from statistics import show_statistics


students = []


while True:

    print("\n========================================")
    print("   STUDENT ACADEMIC RECORD SYSTEM")
    print("========================================")

    print("1. Add Student")
    print("2. Enter Marks")
    print("3. Calculate Result")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Show Class Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        enter_marks(students)

    elif choice == "3":
        calculate_result(students)

    elif choice == "4":
        search_student(students)

    elif choice == "5":
        print("\n----- ALL STUDENTS -----")

        if len(students) == 0:
            print("No students found!")
        else:
            for student in students:
                print("Student ID:", student["id"])
                print("Name:", student["name"])
                print("Branch:", student["branch"])
                print("----------------------")

    elif choice == "6":
        show_statistics(students)

    elif choice == "7":
        print("\nThank you for using the system!")
        break

    else:
        print("\nInvalid choice! Please try again.")