
# pprint

### What it is good for?

Print complex data structures nicely.

The `pprint` module prints lists, tuples, dictionary and other data structures. It tries to fit everything into one line. If this does not work, each entry gets its own line. You can control the line width.

### Installed with Python by default?

yes

### Example

Pretty-print data using a wide and a narrow width:

    >>> from pprint import pprint

    >>> data = {'second': 'two', 'first': 1, 'third': [3, 4, 5]}
    >>> pprint(data)
    {'first': 1, 'second': 'two', 'third': [3, 4, 5]}

    >>> pprint(data, width=20)
    {'first': 1,
     'second': 'two',
     'third': [3,
               4,
               5]}

### Where to learn more?

[https://docs.python.org/3/library/pprint.html](https://docs.python.org/3/library/pprint.html)
