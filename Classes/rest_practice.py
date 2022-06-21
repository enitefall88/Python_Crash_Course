class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}"
              f" and {self.restaurant_name} serves {self.cuisine_type}"
              f" and has served {self.number_served} meals")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number_of_customers):
        self.number_served = number_of_customers

    def call_increment(self, increment_number=30):
        self.number_served += increment_number


restaurant = Restaurant('Indian Fusion', 'Indian')


restaurant.call_increment()

restaurant.describe_restaurant()
