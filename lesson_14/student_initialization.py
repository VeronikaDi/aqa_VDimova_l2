from lesson_14.class_student import Student

student = Student("Jon", "Dominio", 25, 75)

print(student.student_info())

student.change_average_grade(100)

print("\nAverage grade changed:")
student.student_info()
