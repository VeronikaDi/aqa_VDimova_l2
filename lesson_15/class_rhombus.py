class Rhombus:
    __side_a: int
    __angle_a: int
    __angle_b: int

    def __init__(self, side_a: int, angle_a: int):
        self.condition_side_a(side_a)
        self.condition_angle_a(angle_a)
        self.__side_a = side_a
        self.__angle_a = angle_a

    def rhombus_side_a(self):
        return self.__side_a

    def rhombus_angle_a(self):
        return self.__angle_a

    def rhombus_angle_b(self):
        return self.__angle_b

    def condition_side_a(self, value: int):
        if value <= 0:
            raise ValueError("The value of the side must be greater than 0.")

    def condition_angle_a(self, value: int):
        if not (0 < value < 180):
            raise ValueError("The angle must be within (0, 180) degrees.")

    def __setattr__(self, name, value):
        if name == '_Rhombus__side_a':
            self.condition_side_a(value)
        if name == '_Rhombus__angle_a':
            self.condition_angle_a(value)
            super().__setattr__('_Rhombus__angle_b', 180 - value)
        if name == '_Rhombus__angle_b':
            raise AttributeError("Cannot set __angle_b directly. It is calculated from __angle_a.")

        super().__setattr__(name, value)

    def rhombus_numbers(self):
        return f"Rhombus(side_a={self.__side_a}, angle_a={self.__angle_a}, angle_b={self.__angle_b})"
