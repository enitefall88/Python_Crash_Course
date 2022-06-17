# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
#
# for alien in aliens[0:5]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#
# print(aliens[:5])

# pizza = {
# 'crust': 'thick',
# 'toppings': ['mushrooms', 'extra cheese'],
# }
#
# for topping in pizza['toppings']:
#     print(topping)
# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }

# for person in favorite_languages:
#     print(f"\n {person.title()}`s favourite languages are")
#     for language in favorite_languages[person]:
#         print(f"\t{language.title()}")
#
# for person, languages in favorite_languages.items():
#     print(f" {person.title()}`s favourite languages are")
#     for language in languages:
#         print(f"{language}")

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }
#
# for username, userinfo in users.items():
#     print(f"Username is {username}")
#     full_name = userinfo['first'].title() + " " + userinfo['last'].title()
#     location = userinfo['location']
#     print(f"Full name is {full_name} and lives at {location.title()}")
