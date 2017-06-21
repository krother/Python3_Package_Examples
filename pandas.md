
# pandas

### What it is good for?

Analyze tabular data.

`pandas` is an extremely powerful library to analyze, combine and manipulate data in many thinkable (and some unthinkable) ways. The tables called *DataFrame* have many similarities to R. DataFrames have an index column and functions for plotting and reading from CSV or Excel files are included by default. Pandas uses `numpy` under the hood.

### Installed with Python by default

no

### Installed with Anaconda

yes

### How to install it?

    pip install pandas

### Example

Create a table with characters and numbers.:

    import pandas as pd

    hamlet = [['Hamlet', 1.76], ['Polonius', 1.52], ['Ophelia', 1.83], ['Claudius', 1.95]]
    df = pd.DataFrame(data = hamlet, columns = ['name', 'size'])
    print(df)

           name  size
    0    Hamlet  1.76
    1  Polonius  1.52
    2   Ophelia  1.83
    3  Claudius  1.95

Sorted lines by name, filter by minimum size, print first two values and write  a CSV file:

    sorted = df.sort_values(by='name', ascending=False)
    tall = sorted[sorted['size'] > 1.70]
    print(tall.head(2))

           name  size
    3  Claudius  1.95
    2   Ophelia  1.83
    
    df.to_csv('hamlet.csv', index=False, header=True)

### Where to learn more?

[http://pandas.pydata.org/](http://pandas.pydata.org/)
