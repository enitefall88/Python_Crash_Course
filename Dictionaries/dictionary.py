
# for key, values in radik.items():
#     print(f"{key}: {values}")

# for x in radik.keys():
#     print(f"{x}: {radik[x]}")
#
# favorite_numbers = {
#     'Kolly': 11,
#     'John': 21,
#     'Maggy': 33,
#     'Arup': 24,
#     'Zelda': 34
#     }
#
# for key, value in favorite_numbers.items():
#     print(f"{key} his/her favourite number is: {value}")

# glossary = {
#     'dictionary': 'object',
#     'slice': 'array_slicing',
#     'list': 'list making',
#     'pop': 'remove the last element',
#     'for_loop': 'making loops',
#     'set': 'set of unique values',
#     'values': 'returns only values'
#     }
#
# for entry in glossary:
#     print(f"I have learnt about {entry} and it is {glossary[entry]}")
people = [
    {
    'first_name': 'Radik',
    'last_name': 'Tatar',
    'city': 'Burnaby',
    'age': 33,
    },
{
    'first_name': 'vova',
    'last_name': 'shtimat',
    'city': 'Vancouver',
    'age': 28,
    },
{
    'first_name': 'yan',
    'last_name': 'zavelion',
    'city': 'Richmond',
    'age': 50,
    }
]

for person in people:
    full_name = person['first_name'].title() + ' ' +  person['last_name'].title()
    print(f"The person`s name is {full_name}")
    print(f"\t and he lives in {person['city']}and is {person['age']} years old \n")
