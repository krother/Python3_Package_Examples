
import json

# Convert a dictionary to a JSON-formatted string:
data = {'first': 1, 'second': 'two', 'third': [3,4,5]}
jj = json.dumps(data)
print(jj)

# Convert JSON string back to a Python dictionary:
d = json.loads(jj)
print(d)
