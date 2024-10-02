from hw22_students_functions_to_db import create_courses, create_students, add_student, enroll_student, get_students_in_course, \
    get_courses_for_student, update_student, delete_student


def main():
    create_courses()
    create_students()
    print("Courses and students are successfully created and assigned.")

    new_student = add_student('Mark')
    print(f"Student added: {new_student.name}")

    enroll_student(new_student.id, 1)
    print(f"{new_student.name} has been successfully added to the course 'Math'.")

    students_in_math = get_students_in_course(1)
    print("Students added to 'Math' course:", students_in_math)

    courses_for_student = get_courses_for_student(new_student.id)
    print(f"Courses for student {new_student.name}:", courses_for_student)

    update_student(new_student.id, 'Mark Abramow')
    print(f"The student's name has been updated to: 'Mark Abramow'")

    delete_student(new_student.id)
    print(f"Student {new_student.name} has been deleted successfully.")


if __name__ == "__main__":
    main()
