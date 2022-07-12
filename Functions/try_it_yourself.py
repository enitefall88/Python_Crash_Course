# def make_sandwich(*args):
#     print("The next ingridients for sandwich were ordered.")
#     for arg in args:
#         print(arg)
#
# make_sandwich('roast beef', 'cheddar cheese')

# def make_profile(first_name, last_name, **user_info):
#     user_info['first_name'] = first_name.title()
#     user_info['last_name'] = last_name.title()
#
#     for key, val in user_info.items():
#         print(key, val)
#
# make_profile('anton', 'durandin', location='vancouver', age=33, weight=88)

def make_car(manufacturer, model, **options):
    car_dict = {
    'manufacturer': manufacturer,
    'model': model,
    }
    for option, value in options.items():
        car_dict[option] = value

    for key, val in car_dict.items():
        print(f"{key} : {val}")

car = make_car('subaru', 'outback', color='blue', tow_package=True)
