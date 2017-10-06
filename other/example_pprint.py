
# Pretty-print data using a wide and a narrow width:

from pprint import pprint

data = {'second': 'two', 'first': 1, 'third': [3, 4, 5]}
pprint(data)

pprint(data, width=20)
