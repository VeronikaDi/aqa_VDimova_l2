from class_rhombus import Rhombus

rhombus: Rhombus = Rhombus(15, 100)
rhombus_2: Rhombus = Rhombus(20, 89)

print(rhombus.rhombus_side_a())
print(rhombus.rhombus_angle_a())
print(f"Angle b = {rhombus.angle_b}, the value is set automatically.")

# also could be written as:
print(rhombus_2.rhombus_numbers())
