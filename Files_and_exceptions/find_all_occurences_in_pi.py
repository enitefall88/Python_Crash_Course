filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

result = ''

for line in lines:
    result += line

birthday = '10128'


def find_all_occurences(number):
    position = 0
    counter = 0

    while True:
        last_found_position = result.find(number, position)  # start with the first

        if last_found_position == -1:
            print("End")
            break

        counter += 1
        print(f'{counter} -- find at: [{last_found_position}...{last_found_position + len(number)}]')
        position = last_found_position + len(number)


find_all_occurences(birthday)
