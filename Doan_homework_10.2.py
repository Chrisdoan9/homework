# Doan_homework_10.2
import math
import random
import turtle


def randomStep(x, y, num_step):
    for i in range(num_step):
        r = random.randint(1, 4)
        if r == 1:
            x = x + 20
        elif r == 2:
            x = x - 20
        elif r == 3:
            y = y + 20
        else:
            y = y - 20
        turtle.goto(x, y)
    turtle.color("green")
    turtle.goto(0, 0)
    distance = math.sqrt(x ** 2 + y ** 2)
    print("The distance between starting point and end point is: ", distance)
    return x, y


num_step = input("Enter number of step: ")
num_step = int(num_step)
randomStep(0, 0, num_step)
