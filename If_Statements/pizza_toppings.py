# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
#
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for requested_topping in requested_toppings:
#  if requested_topping in available_toppings:
#     print(f"adding {requested_topping}")
#  else: print(f"sorry we don`t have {requested_topping}")

new_users = ['john', 'mark', 'mike', 'luke', 'elaya']
current_users = ['Zack', 'Mike', 'Elaya', 'Luke', 'Bill']
current_users_lowercased = []
for current_user in current_users:
    current_users_lowercased.append(current_user.lower())

for new_user in new_users:
    if new_user in current_users_lowercased:
        print(f"Username {new_user} is already used, pick a new one")
    else:
        print(f"Username {new_user} is available")
