# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     confirmed_users.append(current_user)
#
# confirmed_users.sort()
#
# print("the following users have been confirmed")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond?")
    if repeat == 'no':
       polling_active = False
print(responses)

