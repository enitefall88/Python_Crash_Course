

list_of_squares = []
for value in range(1,6):
    list_of_squares.append(value**2)
print(list_of_squares)

squares_even = [value**2 for value in range(2,13,2)]
print(squares_even)
