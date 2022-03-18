# Chris Doan home work 4.2
a = 0
b = 0
sum = 0
while a != "stop":
    a = input("Enter a number to be averaged (enter \"stop\" when done): ")
    if a != "stop":
        a = eval(a)
        b = b + 1
        sum = sum + a
print("The average of", b, "numbers is", sum/b)
