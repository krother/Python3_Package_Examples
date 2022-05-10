
import sqlite3

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

# write data
query = 'INSERT INTO person VALUES (?,?,?)'
# The ?,?,? are a SQLite-specific way of formating strings.
# There are special precautions against SQL injection
db.execute(query, (1, "Hamlet", "the prince of Denkmark"))
db.execute(query, (2, "Polonius", "Ophelias father"))

# read data
query = '''SELECT name, description FROM person'''
result = db.execute(query)  # returns an iterator
print(list(result))


db.close()
