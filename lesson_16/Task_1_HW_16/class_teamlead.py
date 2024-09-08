from lesson_16.Task_1_HW_16.class_manager import Manager
from lesson_16.Task_1_HW_16.class_test_engineer import TestEngineer


class TeamLead(Manager, TestEngineer):

    __team_size: int

    def __init__(self, name: str, salary: int, department: str, team_size: int, programming_language: str):
        Manager.__init__(self, name, salary, department)
        TestEngineer.__init__(self, name, salary, programming_language)
        self.__team_size = team_size

    @property
    def team_size(self) -> int:
        return self.__team_size
