favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'dylon': 'Julia',
    }

voted_persons = ['sarah', 'luke', 'edward', 'jen']
# friends = ['sarah']
# all_keys = favorite_languages.keys()
# print(all_keys)
# for key in favorite_languages.keys():
#     if key in friends:
#         print(f"Hey {key.title()}, we know you like {favorite_languages[key]}")
#     else:
#         print(key, favorite_languages[key])
# for name in sorted(favorite_languages.keys()):
#     print(name, favorite_languages[name])

# for language in set(favorite_languages.values()):
#     print(language.title())

# rivers = {
#     'egypt': 'the nile',
#     'brazil': 'the amazonka',
#     'usa': 'the mississipi',
# }
#
# for country, river in rivers.items():
#     print(f"{river.title()} runs through {country.title()}")

for person in favorite_languages.keys():
    if person in voted_persons:
        print(f"thanks for voting {person}")
    else:
        print(f"\n Please vote {person}")
