from  random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, n_of_sides, times):
        for time in range(times):
            roll_number = randint(1,6)
            print(f"The {n_of_sides}-sided die just rolled {roll_number}")




lets_roll_20 = Die()
lets_roll_20.roll_die(10, 10)
