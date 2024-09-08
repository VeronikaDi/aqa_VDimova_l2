from lesson_16.Task_1_HW_16.class_employee import Employee


class Manager(Employee):

    __department: str

    def __init__(self, name: str, salary: int, department: str):
        super().__init__(name, salary)
        self.__department = department

    @property
    def department(self) -> str:
        return self.__department
    