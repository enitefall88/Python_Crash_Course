import json

filename = 'numbers.json'

try:
    with open(filename) as f:
        content = json.load(f)
except FileNotFoundError:
    print('no such file')
else:
    print(content)
