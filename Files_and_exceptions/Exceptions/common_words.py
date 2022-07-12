books = ['mobi.txt', 'siddharta.txt', 'alice.txt']

def occurrences_calculator(sources, word):
    occurrences_counter = 0
    for source in sources:
        try:
            with open(source) as file_object:
                content = file_object.read()
        except FileNotFoundError:
            pass
        else:
            occurrences_counter += content.lower().count(word)
    print(occurrences_counter)

occurrences_calculator(books, 'magnificent')
