flag = True

while flag:
    name = input('Enter your name or press q to quit ')
    print(f"Hi there  {name}")
    if name != 'q':
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(f"{name}\n")
    else:
        flag = False

with open('guest_book.txt') as file_object:
    content = file_object.readlines()

print(content)
