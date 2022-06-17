# pizzas
# pizza_topping = []
# prompt = "Please enter your pizza topping "
# pizza_selection = ""
# while pizza_selection != "quit":
#     pizza_selection = input(prompt)
#     pizza_topping.append(pizza_selection)
#     if pizza_selection != "quit":
#         print(f"Your toppings are {pizza_topping}")
#

#   tickets
# prompt = "What is your age? "
# age = 1
#
# while age:
#     age = input(prompt)
#     if age.isdigit():
#
#         if int(age) < 3:
#             print("Your ticket is free")
#         elif 3 < int(age) < 12:
#             print("The ticket price is 10 bucks")
#         else:
#             print("The ticket is 15")
#     else:
#         print("Not a number")

max_number_of_toppings = 0
pizza_topping = []
prompt = "Please enter your pizza topping "
pizza_selection = ""
message_how_many_is_left = "The number of toppings left to choose"
counter = 4
active = True
while max_number_of_toppings < 4 and active:
    pizza_selection = input(prompt)
    max_number_of_toppings += 1
    counter -= 1
    pizza_topping.append(pizza_selection)
    if pizza_selection != "quit":
        active = False
        print(f"Your toppings are {pizza_topping} {message_how_many_is_left} {counter}")
    else:
        break


