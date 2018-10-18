"""
SQLite is a very straightforward SQL database. 
The data is stored in a single file.
The nice thing about Python SQL modules is
that they have almost the same interface.
"""

import sqlite3

DB_SETUP = '''
CREATE TABLE IF NOT EXISTS babynames (
    id INTEGER,
    name VARCHAR(32),
    gender VARCHAR(1),
    amount INTEGER,
    year INTEGER
);

CREATE UNIQUE INDEX IF NOT EXISTS i1 ON babynames(id);
'''

# watch out for the file 'babynames.db' being created.
db = sqlite3.connect('babynames.db')
db.executescript(DB_SETUP)


# The ?,?,? are a SQLite-specific format string.
# There are special precautions against malicious attacks
# (e.g. injecting a quote into the SQL statement)
query = 'INSERT INTO babynames VALUES (?,?,?,?,?)'


# load the data
year = 1880
for i, line in enumerate(open('yob{}.txt'.format(year))):
    row = line.strip().split(',')
    name = row[0]
    gender = row[1]
    amount = int(row[2])
    db.execute(query, (i, name, gender, amount, year))


# run a query
# the result is an iterator, 
# we need to convert it to a list to print it.
query = '''SELECT name, gender, amount FROM babynames WHERE amount > 5000'''
result = db.execute(query)
print(list(result))


db.close()

# Other things to look at:
#   psycopg2   (access PostGreS database)
#   SQLAlchemy (acess database without having to write SQL code)
#   pandas     (also has a method to export to SQL)
