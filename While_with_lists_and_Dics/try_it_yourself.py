# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []
#
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(sandwich)
#     print(f"I made you {sandwich} sandwich")
#
# print("The list of sandwiches that have been made")
# for sandwich in finished_sandwiches:
#     print(sandwich)


#
# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#     'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []
#
# print("We ran out of pastrami")
#
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(current_sandwich)
#
# for sandwich in finished_sandwiches:
#     print(sandwich)

dream_places = {}
poll_active = True

while poll_active:
    name = input("Your name?")
    dream_place = input("What is your dream place you would like to go to?")

    dream_places[name] = dream_place

    next_vote = input("Next person?")
    if next_vote == 'no':
        poll_active = False

for key, value in dream_places.items():
    print(key, value)
