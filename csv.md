
# csv

### What it is good for?

Read and write *comma-separated-value (CSV)* files.

The `csv` module reads and writes nested lists from/to CSV files. You can set a *field delimiter*, *quote character* and *line terminator* character. Note that when reading a line, all columns are in string format.

### Installed with Python by default

yes

### Example

Write a table with two rows to a CSV file:

    import csv

    data = [["first", 1, 234],
            ["second", 5, 678]]

    outfile = open('example.csv', 'w')
    writer = csv.writer(outfile, delimiter=';', quotechar='"')
    writer.writerows(data)
    outfile.close()
    
Read the file again:

    for row in csv.reader(open('example.csv'), delimiter=';'):
       print(row)
    
    ['first', '1', '234']
    ['second', '5', '678']

### Where to learn more?

[https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)
