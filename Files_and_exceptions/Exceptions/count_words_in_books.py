filenames = ['alice.txt', 'siddharta.txt', 'testa.txt', 'mobi.txt']


def count_words(books):
    errors = ''
    content = ''
    for filename in filenames:
        try:
            with open(filename, encoding='utf-8') as file_object:
                lines = file_object.readlines()
                for line in lines:
                    content += line
        except FileNotFoundError:
            errors += filename
        else:
            result = len(content.split())
            print(f"{filename} contains {result} words")
    with open('errors.txt', 'w') as file_object:
        file_object.write(errors)
    print(f"The following files don't exist: {errors}")


count_words(filenames)
with open('errors.txt') as file_object:
    errors = file_object.read()
    print(errors)
