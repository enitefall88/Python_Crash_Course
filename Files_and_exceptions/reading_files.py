# with open('./work/text_files/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
   lines = file_object.readlines()

result = ''
for line in lines:
    result += line.strip()

birthday = '121033'


def find_birthday_occurrences(number):
    counter = 0
    flag = True
    if flag:
        if number in result:
            flag = True
            print('yey')
            print(number)
            counter += 1
        else:
            flag = False

    return counter

print(find_birthday_occurrences(birthday))

