while True:
    answer = input("Why do you like coding? or press 'q' to quit")
    if answer != 'q':
        with open('poll.txt', 'a') as file_object:
            file_object.write(f"{answer}\n")
    else:
        break
