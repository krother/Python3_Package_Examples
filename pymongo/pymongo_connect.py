
# full pymongo documentation
# http://api.mongodb.org/python/current/

import pymongo

client = pymongo.MongoClient("localhost", 27017)  # parameters not necessary
db = client.test
print(db.name)

print(db.my_collection)
db.my_collection.insert_one({"x": 10})
db.my_collection.insert_one({"x": 8})
db.my_collection.insert_one({"x": 11})


# get one entry
print(db.my_collection.find_one())

# iterate over entries
for item in db.my_collection.find():
    print(item["x"])

# accelerate query with an index	
db.my_collection.create_index("x")

# sort results
for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
    print(item["x"])

# chain multiple functions
print([item["x"] for item in db.my_collection.find().limit(2).skip(1)])
