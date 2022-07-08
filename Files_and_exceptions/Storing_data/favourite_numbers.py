import json

filename = 'favourite_num.json'


def take_number_input():
    favourite_number = input("What is your favourite number?")
    return favourite_number

def check_number():
    try:
        with open(filename) as f:
            favourite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favourite_number


def make_number():
    with open(filename, 'w') as f:
        fav_number = take_number_input()
        json.dump(fav_number, f)
        print(fav_number)

def main_number():
    number = check_number()
    if number:
        print(number)
    else:
        make_number()

main_number()
