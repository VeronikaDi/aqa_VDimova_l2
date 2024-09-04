class Rhombus:

    _side_a: int
    _angle_a: int
    _angle_b: int

    def __init__(self, side_a: int, angle_a: int):
        self.condition_side_a(side_a)
        self.condition_angle_a(angle_a)
        self._side_a = side_a
        self._angle_a = angle_a

    def rhombus_side_a(self):
        return self._side_a

    def rhombus_angle_a(self):
        return self._angle_a

    def rhombus_angle_b(self):
        return 180 - self._angle_a

    def condition_side_a(self, value: int):
        if value <= 0:
            raise ValueError("The value of the side must be greater than 0.")

    def condition_angle_a(self, value: int):
        if not (0 < value < 180):
            raise ValueError("The angle must be within (0, 180) degrees.")

    def __setattr__(self, name, value):
        if name == '_side_a':
            self.condition_side_a(value)
            super().__setattr__(name, value)
            return

        if name == '_angle_a':
            self.condition_angle_a(value)
            super().__setattr__(name, value)
            super().__setattr__('_angle_b', 180 - value)
            return

        if name == 'angle_b':
            raise AttributeError("Cannot set angle_b directly. It is calculated from angle_a.")

        super().__setattr__(name, value)

    def rhombus_numbers(self):
        return f"Rhombus(side_a={self._side_a}, angle_a={self._angle_a}, angle_b={self._angle_b})"
