from typing import override

from lesson_16.Task_2_HW_16.class_figure import Figure


class Triangle(Figure):

    __triangle_a: int
    __triangle_b: int
    __triangle_c: int
    __height: int

    def __init__(self, triangle_a: int, triangle_b: int, triangle_c: int, height: int):
        self.__triangle_a = triangle_a
        self.__triangle_b = triangle_b
        self.__triangle_c = triangle_c
        self.__height = height

    @override
    def calculate_perimetr(self) -> int:
        return self.__triangle_a + self.__triangle_b + self.__triangle_c

    @override
    def calculate_square(self) -> float:
        return 0.5 * self.__triangle_a * self.__height
    