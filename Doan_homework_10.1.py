# Doan_homework_10.1
import math
import random


def randomStep(x, y, num_step, replicate):
    total_distance = 0
    data = []
    for i in range(replicate):
        for j in range(num_step):
            r = random.randint(1, 4)
            if r == 1:
                x = x + 1
            elif r == 2:
                x = x - 1
            elif r == 3:
                y = y + 1
            else:
                y = y - 1
        distance = math.sqrt(x ** 2 + y ** 2)
        data.append(distance)
        total_distance = total_distance + distance
    average = total_distance / replicate
    variation = sum((x - average) ** 2 for x in data) / replicate
    # The line above (24th) got the idea from https://www.geeksforgeeks.org/python-standard-deviation-of-list/
    stand_dev = math.sqrt(variation)
    return print("The average displacement is:", round(average, 2), ".", "The standard deviation is:", round(stand_dev))

num_step = input("Enter number of step: ")
num_step = int(num_step)
x = 0
y = 0
replicate = input("Enter number of replicate: ")
replicate = int(replicate)
randomStep(0, 0, num_step, replicate)
