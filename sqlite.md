
# sqlite3

### What it is good for?

Create and use a *SQLite* database.

SQLite databases are stored in files. For using the `sqlite3` module you don't need to install or set up anything. SQLite is sufficient only for small SQL databases, but Python modules for bigger databases look very similar.

### Installed with Python by default

yes

### Example

Create a new database:

    >>> import sqlite3

    >>> DB_SETUP = '''
    ... CREATE TABLE IF NOT EXISTS person (
    ...     id INTEGER,
    ...     name VARCHAR(32),
    ...     description TEXT
    ... );'''
    >>> db = sqlite3.connect('hamlet.db')
    >>> db.executescript(DB_SETUP)

Insert data:

    >>> query = 'INSERT INTO person VALUES (?,?,?)'
    >>> db.execute(query, (1, "Hamlet", "the prince of Denkmark"))
    >>> db.execute(query, (2, "Polonius", "Ophelias father"))

Submit a query:

    >>> query = '''SELECT name, description FROM person'''
    >>> result = db.execute(query)
    >>> print(list(result))
    [('Hamlet', 'the prince of Denkmark'), ('Polonius', 'Ophelias father')]
    
    >>> db.close()

### Where to learn more?

[]()