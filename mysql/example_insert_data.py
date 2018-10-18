# Example: inserting data into a table in MySQL

import _mysql

db = _mysql.connect(host = "localhost", db="pycourse",
                    user="python", passwd="python")


db.query("""INSERT INTO pet VALUES (
   "Rex","Peter","dog","M","2009-08-11",0
   )
""")
db.query("""INSERT INTO pet VALUES (
   "Felix","Maria","cat","M","2007-01-03",3
   )
""")

db.query("""INSERT INTO pet VALUES (
   "Maximus","Dr.Kowalska","rat","F",NULL,NULL
   )
""")



