from random import choice

numbers_n_letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

def lottery(sequence):
    winner_sequence = []
    while len(winner_sequence) < 4 in sequence:
        pulled_item = choice(sequence)
        if pulled_item not in winner_sequence:
            winner_sequence.append(pulled_item)
    return winner_sequence

def checking(ticket):
    counter = 0
    while lottery(sequence=numbers_n_letters) != ticket:
        counter += 1
        # print(counter)
    return counter


my_ticket = ['a', 'd', 8, 1]

print(checking(my_ticket))
