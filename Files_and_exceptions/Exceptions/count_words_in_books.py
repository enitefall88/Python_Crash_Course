filenames = ['alice.txt', 'siddharta.txt', 'testa.txt', 'mobi.txt']
def count_words(books):
    content = ''
    for filename in filenames:
        try:
            with open(filename, encoding='utf-8') as file_object:
                lines = file_object.readlines()
                for line in lines:
                    content += line
        except FileNotFoundError:
            pass
        else:
            result = len(content.split())
            print(f"{filename} contains {result} words")

count_words(filenames)

