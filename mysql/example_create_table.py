
# Example: creating a table in MySQL

import _mysql

db = _mysql.connect(host = "localhost", db="pycourse",
                    user="python", passwd="python")

db.query("""CREATE TABLE pet (
              name VARCHAR(20),
              owner VARCHAR(20),
              species VARCHAR(20),
              sex CHAR(1),
              birth DATE, 
              age INTEGER);
""")


