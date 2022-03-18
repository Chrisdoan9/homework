# Doan home work 1.3.
import math
a_x = input("Enter the x-coordinate of the first point: ")
a_x = eval(a_x)
a_y = input("Enter the y-coordinate of the first point: ")
a_y = eval(a_y)
b_x = input("Enter the x-coordinate of the second point: ")
b_x = eval(b_x)
b_y = input("Enter the y-coordinate of the second point: ")
b_y = eval(b_y)
distance = round(math.sqrt((a_x -b_x)**2 + (a_y - b_y)**2), 3)
print("The distance between those point is", distance,".")