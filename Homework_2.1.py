# Chris Doan home work 2.1
size_pizza_1 = input(" Enter size pizza 1: ")
size_pizza_1 = eval(size_pizza_1)
price_pizza_1 = input("Enter price pizza 1: ")
price_pizza_1 = eval(price_pizza_1)
size_pizza_2 = input(" Enter size pizza 2: ")
size_pizza_2 = eval(size_pizza_2)
price_pizza_2 = input("Enter price pizza 2: ")
price_pizza_2 = eval(price_pizza_2)
import math
pizza_1_per_dollar = ((size_pizza_1/2)**2*math.pi)/price_pizza_1
print("Pizza 1 has", round(pizza_1_per_dollar,2), "inches of pizza per dollar.")
pizza_2_per_dollar = ((size_pizza_2/2)**2*math.pi)/price_pizza_2
print("Pizza 2 has", round(pizza_2_per_dollar,2), "inches of pizza per dollar.")