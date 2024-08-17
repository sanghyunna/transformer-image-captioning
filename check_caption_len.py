import json

input_file = './source/captions.json'

with open(input_file, 'r') as file:
    data = json.load(file)

sorted_data = dict(sorted(data.items()))

print(len(sorted_data.keys()))