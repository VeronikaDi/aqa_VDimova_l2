from lesson_16.Task_2_HW_16.class_figure import Figure
from lesson_16.Task_2_HW_16.class_square import Square
from lesson_16.Task_2_HW_16.class_rectangle import Rectangle
from lesson_16.Task_2_HW_16.class_triangle import Triangle

square_f: Square = Square(10)

rectangle: Rectangle = Rectangle(10, 5)

triangle: Triangle = Triangle(3, 5, 8, 4)

figures_list: list[Figure] = [square_f, rectangle, triangle]

list_tuple_perimeter_and_square: list[tuple[int, object]] = [(figure.calculate_perimetr(), figure.calculate_square())
                                                             for figure in figures_list]


for item in list_tuple_perimeter_and_square:
    print(item[0], item[1])
