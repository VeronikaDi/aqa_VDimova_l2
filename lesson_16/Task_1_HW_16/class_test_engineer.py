from lesson_16.Task_1_HW_16.class_employee import Employee


class TestEngineer(Employee):

    __programming_language: str

    def __init__(self, name: str, salary: int, programming_language: str):
        super().__init__(name, salary)
        self.__programming_language = programming_language

    @property
    def programming_language(self) -> str:
        return self.__programming_language
    