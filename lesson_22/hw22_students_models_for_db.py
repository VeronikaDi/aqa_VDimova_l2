from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    enrollments = relationship("Enrollment", back_populates="student")


class Course(Base):

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    enrollments = relationship("Enrollment", back_populates="course")


class Enrollment(Base):

    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
