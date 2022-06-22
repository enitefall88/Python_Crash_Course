class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}"
              f" and {self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

class Ice_cream_stand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavour = ['gold', 'strawberry', 'chocolate']

    def display_flavour(self):
        print(self.flavour)

    def set_and_print_flavour(self, new_flavour):
        appended = self.flavour[:]
        appended.append(new_flavour)
        self.flavour = appended
        print(self.flavour)
        self.display_flavour()

magnum = Ice_cream_stand('ibizza', 'confectionary')
magnum.set_and_print_flavour('nuts')
