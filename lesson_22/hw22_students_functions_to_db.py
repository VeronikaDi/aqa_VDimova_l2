from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hw22_students_models_for_db import Base, Student, Course, Enrollment
import random

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def create_courses():
    courses = [
        Course(title='Math'),
        Course(title='Science'),
        Course(title='Literature'),
        Course(title='History'),
        Course(title='Art')
    ]
    session.add_all(courses)
    session.commit()


def create_students():
    student_names = [
        'Veronika', 'Laura', 'Gregory', 'Viktor', 'Alfred',
        'Sofia', 'Alex', 'Mia', 'Daniel', 'Julia',
        'Ethan', 'Emily', 'Oliver', 'Chloe', 'Liam',
        'Stefania', 'Serhii', 'Isabella', 'Lucas', 'Aida'
    ]
    students = [Student(name=name) for name in student_names]
    session.add_all(students)
    session.commit()

    for student in students:
        for _ in range(random.randint(1, 3)):
            course = random.choice(session.query(Course).all())
            enrollment = Enrollment(student=student, course=course)
            session.add(enrollment)

    session.commit()


def add_student(name):
    new_student = Student(name=name)
    session.add(new_student)
    session.commit()
    return new_student


def enroll_student(student_id, course_id):
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    session.add(enrollment)
    session.commit()


def get_students_in_course(course_id):
    course = session.query(Course).filter(Course.id == course_id).first()
    return [enrollment.student.name for enrollment in course.enrollments]


def get_courses_for_student(student_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    return [enrollment.course.title for enrollment in student.enrollments]


def update_student(student_id, new_name):
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        student.name = new_name
        session.commit()


def delete_student(student_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        session.delete(student)
        session.commit()
