
# Create a table with characters and numbers.:

import pandas as pd

hamlet = [['Hamlet', 1.76], ['Polonius', 1.52], ['Ophelia', 1.83], ['Claudius', 1.95]]
df = pd.DataFrame(data = hamlet, columns = ['name', 'size'])
print(df)


# Sorted lines by name, filter by minimum size,
# print first two values and write  a CSV file:

sorted = df.sort_values(by='name', ascending=False)
tall = sorted[sorted['size'] > 1.70]
print(tall.head(2))

df.to_csv('hamlet.csv', index=False, header=True)
