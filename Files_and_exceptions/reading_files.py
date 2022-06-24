# with open('./work/text_files/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
   lines = file_object.readlines()

result = ''
for line in lines:
    result += line.strip()

birthday = '121101213'
counter = 0

if birthday in result:
    print('yey')
    counter += 1


print(counter)

