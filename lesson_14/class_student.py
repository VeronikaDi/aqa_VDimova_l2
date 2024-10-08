class Student:

    name: str
    last_name: str
    age: int
    average_grade: int

    def __init__(self, name: str, last_name: str, age: int, average_grade: int):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def student_info(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Average grade: {self.average_grade}")

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade
