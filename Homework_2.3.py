# Chris homework_2.3
import math
x_origin = input("Enter x coordinate of origin: ")
x_origin = eval(x_origin)
y_origin = input("Enter y coordinate of origin: ")
y_origin = eval(y_origin)
radius = input("Enter radius: ")
radius = eval(radius)
x_point = input("Enter x coordinate of the point: ")
x_point = eval(x_point)
y_point = input("Enter y coordinate of the point: ")
y_point = eval(y_point)
distance = math.sqrt((x_point - x_origin)**2 + (y_point - y_origin)**2)
if distance > radius:
    print("The point is outside the circle.")
elif distance == radius:
    print("The point is on the circle.")
else:
    print("The point is inside the circle.")