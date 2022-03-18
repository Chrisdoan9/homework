# Chris Doan homework 6.1
def C_to_F():
    Celcius = input("Enter a temperature in Celsius: ")
    Celcius = float(Celcius)
    Fahrenheit = round(9 / 5 * Celcius + 32, 0)
    return print("That is", Fahrenheit, "degrees Fahrenheit.")
def F_to_C():
    F_to_C = input("Enter a temperature in Fahrenheit: ")
    F_to_C = float(F_to_C)
    Celcius = (F_to_C - 32) * 5 / 9
    return print("That is", Celcius, "degrees Celsius.")
direction = input("Convert C to F type C, convert F to C type F: ")
if direction == "C" or direction == "c":
    C_to_F()
else:
    F_to_C()
