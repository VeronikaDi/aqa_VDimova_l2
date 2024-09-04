class Rhombus:

    side_a: int
    angle_a: int

    def __init__(self, side_a: int, angle_a: int):
        self.side_a = side_a
        self.angle_a = angle_a

    def rhombus_side_a(self):
        return f"Side a = {self.side_a}"

    def rhombus_angle_a(self):
        return f"Angle a = {self.angle_a}"

    def __setattr__(self, name, value):
        if name == 'side_a':
            if value < 0:
                raise ValueError("The value of the side must be greater than 0.")
            super().__setattr__(name, value)
            return

        if name == 'angle_a':
            if not (0 < value < 180):
                raise ValueError("The angle must be within (0, 180) degrees.")
            super().__setattr__(name, value)
            super().__setattr__('angle_b', 180 - value)
            return

        if name == 'angle_b':
            raise AttributeError
        super().__setattr__(name, value)

    def rhombus_numbers(self):
        return f"Rhombus(side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b})"
