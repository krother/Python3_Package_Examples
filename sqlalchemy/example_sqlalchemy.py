
from sqlalchemy import create_engine, text

# connection string - specifies
engine = create_engine("sqlite:///example.db", echo=False)

with engine.connect() as conn:
    
    # write data
    conn.execute(text('''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER,
        name VARCHAR(32),
        description TEXT
    );'''))

    conn.execute(text('INSERT INTO person VALUES (:id,:name,:role)'),
                      [
                          {"id": 1, "name": "Hamlet", "role": "the prince of Denkmark"},
                          {"id": 2, "name": "Kunigunde", "role": "the queen of Denkmark"},
                       ])
    conn.commit()  # writes to DB

    # read data
    result = conn.execute(text('SELECT name, description FROM person'))
    for name, description in result:
        print(name, description)
    