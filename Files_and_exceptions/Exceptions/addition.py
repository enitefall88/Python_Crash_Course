import sys


def addition():
    number1 = input('enter the first number')
    try:
        number1 = int(number1)
    except: ValueError
    print(f"{number1} is not a number")
    sys.exit(1)

    number2 = input('enter the second number')
    try:
        number2 = int(number2)
    except ValueError:
        print(f"{number2} is not a number")
    else:
        return print(number1 * number2)

addition()

