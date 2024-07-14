
from sqlalchemy import create_engine

# connection string - specifies
db = create_engine("sqlite:///example.db")

db.execute('''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER,
    name VARCHAR(32),
    description TEXT
);''')

db.execute('INSERT INTO person VALUES (?,?,?)', 1, "Hamlet", "the prince of Denkmark")
db.execute('INSERT INTO person VALUES (?,?,?)', 2, "Kunigunde", "the queen of Denkmark")

# read data
result = db.execute('SELECT name, description FROM person')
for name, description in result:
    print(name, description)
