# Example: querying data in MySQL

import _mysql

db = _mysql.connect(host = "localhost", db="pycourse",
                    user="python", passwd="python")


db.query("""SELECT name, species FROM pet
       WHERE age>=1;
""")
result = db.store_result()

print "Rows",result.num_rows()
print "Fields",result.num_fields()

for i in range(result.num_rows()):
    print result.fetch_row()[0]

