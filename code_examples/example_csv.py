
# Write a table with two rows to a CSV file:

import csv

data = [["first", 1, 234],
        ["second", 5, 678]]

outfile = open('example.csv', 'w')
writer = csv.writer(outfile, delimiter=';', quotechar='"')
writer.writerows(data)
outfile.close()
    

# Read the file again:

for row in csv.reader(open('example.csv'), delimiter=';'):
   print(row)
