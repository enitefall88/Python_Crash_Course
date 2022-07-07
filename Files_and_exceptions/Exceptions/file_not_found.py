file = input('Enter file name to open')

try:
    with open(file, encoding='utf-8') as file_object:
        content = file_object.read()
        print(content)

except FileNotFoundError:
    print(f"There is no such file as {file}")
