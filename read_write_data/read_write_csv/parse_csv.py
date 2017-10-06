
import csv

data =[]
for row in csv.reader(open('example.csv')):
    data.append(row)

writer = csv.writer(open('output.txt', 'w'), delimiter='|')
writer.writerows(data)
