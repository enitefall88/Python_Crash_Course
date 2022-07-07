file = input('Enter file name to open')

try:
    with open(file, encoding='utf-8') as file_object:
        lines = file_object.readlines()
        result = ''
        for line in lines:
            result += line
        print(result)

except FileNotFoundError:
    print(f"There is no such file as {file}")
