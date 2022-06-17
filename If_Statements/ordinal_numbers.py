numbers = list(range(1,11))

for number in numbers:
    if number == 1:
        print(f"\n{number}st")
    elif number == 2:
        print(f"\n{number}nd")
    elif number == 3:
        print(f"\t{number}rd")
    else:
        print(f"\t{number}th")

lonely_tuple = (3,)
print(lonely_tuple)
