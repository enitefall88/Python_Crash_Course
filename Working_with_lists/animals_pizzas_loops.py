pizza_list = ['pepperoni', 'meat lovers', 'hawaian']
#
# for pizza in pizza_list:
#     print(f"I like {pizza} pizza")
# print("I also like parmesani and other pizzaz")

# animal_list = ['kangaroo', 'rabbit', 'heir']
#
# for animal in animal_list:
#     print(f"A {animal} would make a great pet")
# print("Any of those animals would make a great pet!")

friend_pizza = pizza_list[:]
# pizza_list.insert(2,'naopoletano')

friend_pizza.append('all cheese')
# print(pizza_list, friend_pizza)
joined_list = []

for pizza in friend_pizza:
    print(f"\n\tMy friends favourite pizzas are: {pizza}")
    joined_list.append(pizza)

for pizza in pizza_list:
    print(f"My favorite pizzas are: {pizza}")
    joined_list.append(pizza)

print(joined_list)

my_fav_food = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

list_of_restaurants = ['velco', 'del art','cicci', 'squirrel']

for food in my_fav_food:
    print(food)

for restaurant in list_of_restaurants:
    print(restaurant)
