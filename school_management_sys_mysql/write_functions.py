import mysql.connector


def db_write_query(query):
    connection = mysql.connector.connect(
        user="root", password="admin", host="localhost", database="school"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    last_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return last_id


def add_course(new_courses_list):
    for course in new_courses_list:
        add_to_courses_table = f"""INSERT INTO `courses`(course_name)
        VALUES ('{str(course)}');"""
        db_write_query(add_to_courses_table)
        new_table = f"""CREATE TABLE `{str(course)}`(
        user_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(255),
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        FOREIGN KEY(username) REFERENCES users(username)
        );"""
        db_write_query(new_table)
    return "Success"


def add_student(course_name, students_list):
    for student in students_list:
        add_to_users = f"""INSERT INTO `users` (username,role_id)
        VALUES('{str(student)}',1);"""
        last_id = db_write_query(add_to_users)
        add_to_course = f"""INSERT INTO `{str(course_name)}`(user_id,username)
        VALUES ({last_id},'{str(student)}');"""
        db_write_query(add_to_course)
    return "Success"
