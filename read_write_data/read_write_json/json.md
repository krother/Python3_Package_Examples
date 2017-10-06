
# json

### What it is good for?

Convert Python dictionaries to JSON and back.

The *JavaScript Object Notation (JSON)* is frequently used to send structured data around the web or store it painlessly in files. The `json` modules utilizes the similarity of the JSON format to Python dictionaries.

### Installed with Python by default

yes

### Example

Convert a dictionary to a JSON-formatted string:

    import json

    data = {'first': 1, 'second': 'two', 'third': [3,4,5]}
    jj = json.dumps(data)
    print(jj)
    '{"second": "two", "first": 1, "third": [3, 4, 5]}'

Convert JSON string back to a Python dictionary:

    d = json.loads(jj)
    print(d)

    {'second': 'two', 'first': 1, 'third': [3, 4, 5]}

### Where to learn more?

[https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)
