# Chris Doan homework 3.1.
import math
a = input("Enter a positive integer: ")
a = eval(a)
print(2)
# 2 is a special prime number that I can't apply with the algorithm below.
# I use loop in loop.
for i in range(a+1):  # range(a+1) not range(a) in case the number that user enter is a prime number.
    for b in range(2, i):
        if i/b == math.trunc(i/b):  # This code will eliminate a number that is not a prime number.
            break
        elif b == i-1:  # I use this code to print the prime number in a loop only one time.
            print(i)

