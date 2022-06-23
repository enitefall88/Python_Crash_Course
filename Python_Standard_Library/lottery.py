from random import choice

numbers_n_letters = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

def lottery(sequence):
    winner_sequence = []
    while len(winner_sequence) < 4 in sequence:
        pulled_item = choice(sequence)
        if pulled_item not in winner_sequence:
            winner_sequence.append(pulled_item)
    print(winner_sequence)


lottery(numbers_n_letters)
