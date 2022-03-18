# Doan home work 1.4.
import math
time = input("Enter a number of seconds: ")
min_total = eval(time)/60  # Convert seconds to total minutes.
hour = math.floor(min_total/60)  # Get the hour.
min_real = math.floor(min_total - hour*60)  # Get the remain minutes than the minutes.
second = eval(time) - hour*60*60 - min_real*60  # Get the second.
print("That is equal to", hour, "hours", min_real, "minutes, and", second, "seconds.")