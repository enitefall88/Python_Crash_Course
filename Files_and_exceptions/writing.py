with open('test_writing.txt', 'w') as file_object:
    file_object.write("TesT I like coding!")


with open('test_writing.txt') as file_object:
   print(file_object.read())



