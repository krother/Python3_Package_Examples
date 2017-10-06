
# Create a database:

import sqlite3

DB_SETUP = '''
  CREATE TABLE IF NOT EXISTS person (
    id INTEGER,
    name VARCHAR(32),
    description TEXT
  );'''
db = sqlite3.connect('hamlet.db')
db.executescript(DB_SETUP)


# Insert data:

query = 'INSERT INTO person VALUES (?,?,?)'
db.execute(query, (1, "Hamlet", "the prince of Denkmark"))
db.execute(query, (2, "Polonius", "Ophelias father"))
db.commit()


# Submit a query:

query = '''SELECT name, description FROM person'''
result = db.execute(query)
print(list(result))
    
db.close()
