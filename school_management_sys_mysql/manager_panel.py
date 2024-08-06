import read_functions
import write_functions


def what_to_do():
    while True:
        check = input(
            (
                """\nTeachers:t\tCourses:c\tStudents in courses:s\t
                     Add course:a\nMainMenu:menu\tExit:exit\n"""
            )
        ).upper()
        if check == "T":
            print(*read_functions.teachers(), sep=" ,")
        if check == "S":
            result = read_functions.student_each_course()
            for course, students in result.items():
                print(course, "Students:", *students)
        if check == "C":
            print(*read_functions.courses(), sep=" ,")
        if check == "A":
            adding = get_courses()
            old = read_functions.courses()
            print(
                f"""CHANGES:...
            \ncourse table:From: {old}\n\t\tTo: {old+adding}\n
            also,creating new table for each course.
            \nAre you sure to continue?"""
            )
            final_check = input(
                ("""Enter yes to proceed or anything else to cancel:\t""")
            ).upper()
            if final_check == "YES":
                print(write_functions.add_course(adding))
        if check == "END":
            exit()
        if check == "MENU":
            break


def get_courses():
    courses = []
    print("\nEnter finish to finish adding")
    while True:
        course = input("\nNew course name:\t")
        if course == "finish":
            break
        courses.append(course)
    return courses
