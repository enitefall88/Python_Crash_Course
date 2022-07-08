import json

name = input("Enter your name")

filename = 'names.json'

with open(filename, 'w') as f:
    json.dump(name, f)
