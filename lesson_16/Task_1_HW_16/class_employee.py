from abc import ABC


class Employee(ABC):

    __name: str
    __salary: int

    def __init__(self, name: str, salary: int):
        self.__name = name
        self.__salary = salary

    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> int:
        return self.__salary
    