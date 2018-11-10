"""
Parsing JSON

1. Try pd.read_json()
"""
import pandas as pd

pd.read_json('btc.json')

"""
2. Check possible values for the 'orientation' parameter
   ('split', 'records', 'index', 'columns', 'values')
"""

pd.read_json('btc.json', orient='records').head(3)
pd.read_json('btc.json', orient='values').head(3)

"""
3. If that doesn't work, read the JSON file yourself
"""

import json

j = json.loads(open('btc.json').read())
print(j.keys())

df = pd.DataFrame(j['prices'], columns=['date', 'price'])

"""
4. Convert time to a DatetimeIndex
"""
import time

def convert(t):
    # leaving away min/sec
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t/1000))

dt = pd.to_datetime(df['date'].apply(convert))

df.set_index(dt, inplace=True)  # <-- create new index
del df['date']


import matplotlib.pyplot as plt

df.plot()
plt.show()
