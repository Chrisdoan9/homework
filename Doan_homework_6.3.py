# Doan_homework_6.3
import math

line_order = 0  # To count the number of circles.

sum_circumference = 0  # To calculate the average of circumference later.


def circumference(c):
    return 2 * c * math.pi


sum_area = 0


def area(c):
    return c * c * math.pi


sum_diameter = 0


def diameter(c):
    return 2 * c


input_file = input("Enter file path: ")
output_file = input("Enter output file path and name: ")
input_file = open(input_file, "r")
output_file = open(output_file, "w")
output_file.write("Order Radius Circumference  Area     Diameter\n")
for line in input_file:
    line_order = line_order + 1
    line = float(line)
    sum_area = sum_area + round(area(line), 2)
    sum_diameter = sum_diameter + round(diameter(line), 2)
    sum_circumference = sum_circumference + round(circumference(line), 2)
    line = str(line_order) + str("      ") + str(line) + str("      ") + str(round(2 * line * math.pi, 2)) + str(
        "       ") + str(round(line * line * math.pi, 2)) + str("       ") + str(2 * line) + str("\n")
    output_file.write(line)
print("The number of circles are:", line_order)
print("The average area are:", round(sum_area / line_order, 2))
print("The average diameter are:", round(sum_diameter / line_order, 2))
print("The average circumference are:", round(sum_circumference / line_order, 2))

input_file.close()
output_file.close()

