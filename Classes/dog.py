class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} is now rolling")

my_dog = Dog('Zak', 11)


koshkas_dog = Dog('Pochie', 20)
koshkas_dog.roll_over()
