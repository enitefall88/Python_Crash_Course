import json


def get_stored_username():

    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        check = input(f"Welcome back, {username}! Is it your name")
        if check == 'n':
           get_new_username()
           print(get_stored_username())

    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
