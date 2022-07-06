filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

result = ''
for line in lines:
    result += line.strip()

birthday = '10128'


def find_birthday_occurrences(number):
    position = 0
    counter = 0

    while True:
        last_find_pos = result.find(number, position)

        if last_find_pos == -1:
            print(f'End --')
            break

        counter += 1
        print(f'{counter} -- find at: [{last_find_pos}...{last_find_pos+len(number)}]')
        position = last_find_pos + len(number)

    return counter


print(find_birthday_occurrences(birthday))
