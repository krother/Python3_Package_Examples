
# full pymongo documentation
# http://api.mongodb.org/python/current/

import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.test
print db.name

print db.my_collection
db.my_collection.save({"x": 10})
db.my_collection.save({"x": 8})
db.my_collection.save({"x": 11})
db.my_collection.find_one()

for item in db.my_collection.find():
    print item["x"]

	
db.my_collection.create_index("x")

for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
    print item["x"]

print [item["x"] for item in db.my_collection.find().limit(2).skip(1)]
