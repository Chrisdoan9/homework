# Doan_homework_6.2
def main():
    a = 0
    while a != "":
        a = input("Enter something (enter a blank line when done): ")
        try:
            a = float(a)
            print("This is a valid number.")
        except ValueError:
            print("This is not a valid number.")
main()



