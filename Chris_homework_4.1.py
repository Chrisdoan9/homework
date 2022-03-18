# Chris Doan home work 4.1
numbers_average = input("How many numbers do you want to average (2 or more): ")
numbers_average = eval(numbers_average)
sum = 0
for a in range(1, numbers_average + 1):  # We start from 1 not 0 so we need to adjust default value in range().
    print("Enter value #", a, end="")
    a = input(": ")
    a = eval(a)
    sum = sum + a
print("The average is", sum/numbers_average)