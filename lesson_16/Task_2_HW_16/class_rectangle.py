from typing import override

from lesson_16.Task_2_HW_16.class_figure import Figure


class Rectangle(Figure):

    __rectangle_a: int
    __rectangle_b: int

    def __init__(self, rectangle_a: int, rectangle_b: int):
        self.__rectangle_a = rectangle_a
        self.__rectangle_b = rectangle_b

    @override
    def calculate_perimetr(self) -> int:
        return (self.__rectangle_a * 2) + (self.__rectangle_b * 2)

    @override
    def calculate_square(self) -> int:
        return self.__rectangle_a * self.__rectangle_b
