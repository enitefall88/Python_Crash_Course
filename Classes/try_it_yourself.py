class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}"
              f" and {self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

indian_fusion = Restaurant('Indian Fusion', 'Indian')

mac_donalds = Restaurant("McDonals's", 'fast-food')
osaka_sushi = Restaurant('Osaka sushi', 'Japanese')
casablanca = Restaurant('Casablanca', 'Marrocan')



class User:
    def __init__(self, first_name, last_name, email, username, *password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
    
    def describe_user(self):
        print(f"The real full name of the user {self.username} is {self.first_name}"
              f" {self.last_name}. The email is {self.email}. The password is "
              f" {self.password}")

    def greet_user(self):
        print(f"Hi {self.first_name.title()} {self.last_name.title()}")

oleg = User(
        'Oleg', 'Smirnov',
        'oleg_smirnov@gmail.com',
        'olegsmirn'
        )

jack = User(
        'Jack', 'Brown',
        'jack@gmail.com',
        'jackbrown'
        )

oleg.describe_user()
oleg.greet_user()

jack.describe_user()
jack.greet_user()
