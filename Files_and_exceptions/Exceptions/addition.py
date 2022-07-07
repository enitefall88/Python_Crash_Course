import sys


def addition():

    while True:
        try:
            x = input("Give me a number: or 'q' to quit ")
            if x == 'q':
               break
            x = int(x)

            y = input("Give me a number: or 'q' to quit ")
            if y == 'q':
                break
            y = int(y)
        except ValueError:
            print("Sorry, I really needed a number.")
        else:
            sum = x + y
            print(f"The sum of {x} and {y} is {sum}.")

addition()

