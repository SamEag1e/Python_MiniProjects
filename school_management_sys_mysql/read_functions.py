import mysql.connector


def db_read_query(query):
    connection = mysql.connector.connect(
        user="root", password="admin", host="localhost", database="school"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    data_list = []
    for row in cursor:
        row_str = "".join(row)
        list.append(row_str)
    cursor.close()
    connection.close()
    return data_list


def all_students():
    return db_read_query("SELECT username FROM `users` WHERE role_id=1")


def teachers():
    return db_read_query("SELECT username FROM users WHERE role_id=2")


def courses():
    return db_read_query("SELECT course_name FROM courses")


def student_each_course():
    crs = courses()
    result_dict = {}
    for course in crs:
        q = f"""SELECT username FROM `{course}` """
        result_dict.update({course: db_read_query(q)})
    return result_dict
