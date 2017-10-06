
import sqlite3
# SQLite is a very straightforward SQL database. 
# In contrast to MySQL or PostGreSQL, the data is stored in a single file.
# The nice thing is that the Python module for accessing the data works
# in almost the same way.

DB_SETUP = '''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER,
    name VARCHAR(32),
    description TEXT
);

CREATE UNIQUE INDEX IF NOT EXISTS i1 ON person(id);
'''

# watch out for the file 'hamlet.db' being created.
db = sqlite3.connect('hamlet.db')
db.executescript(DB_SETUP)

query = 'INSERT INTO person VALUES (?,?,?)'
# The ?,?,? are a SQLite-specific way of formating strings.
# There are special precautions against malicious attacks
# (e.g. injecting a quote into the SQL statement)
db.execute(query, (1, "Hamlet", "the prince of Denkmark"))
db.execute(query, (2, "Polonius", "Ophelias father"))

query = '''SELECT name, description FROM person'''
result = db.execute(query)
# result is an iterator, hence we need to convert it to a list to print it.
print(list(result))


db.close()

# Other things to look at:
#   SQLAlchemy (acess database without having to write SQL code)
#   pandas     (also has a method to export to SQL)
