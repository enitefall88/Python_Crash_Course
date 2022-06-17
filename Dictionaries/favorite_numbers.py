favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }

for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()} favourite numbers are:")
    for number in numbers:
        print(f'\t{number}')

