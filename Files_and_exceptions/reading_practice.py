with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

result = ''

for line in lines:
    result += line.rstrip()

result = result.replace('Python', 'C')

print(result)

