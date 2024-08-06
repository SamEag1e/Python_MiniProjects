import read_functions
import write_functions


def what_to_do():
    while True:
        check = input(
            (
                "\nCourses:c\tStudents in courses:s\tAdd students:a\nMainMenu:menu\tExit:exit\n"
            )
        ).upper()
        if check == "C":
            print(*read_functions.courses(), sep=" ,")
        if check == "S":
            result = read_functions.student_each_course()
            for course, students in result.items():
                print(course, "Students:", *students)
        if check == "A":
            courses = read_functions.courses()
            print("Availabe courses:")
            print(*courses, sep=" ,")
            which_course = input(
                "Enter exact name of the course you want to add students:\t"
            )
            if which_course in courses:
                adding = get_students()
                old = read_functions.all_students()
                print(
                    f"""CHANGES:...
                \nusers table(Students) From: \n{old}\nTo: {old+adding}\nalso,
                {which_course} course students will be updated.
                \nAre you sure to continue?"""
                )
                final_check = input(
                    "Enter yes to proceed or anything else to cancel:\t"
                ).upper()
                if final_check == "YES":
                    print(write_functions.add_student(which_course, adding))
            else:
                print("The course name you've entered does not exist.")
        if check == "EXIT":
            exit()
        if check == "MENU":
            break


def get_students():
    students = []
    print("\nEnter finish to finish adding")
    while True:
        student = input("\nNew student name:\t")
        if student == "finish":
            break
        students.append(student)
    return students
