import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.test
collection = db.students

results = collection.find({'name': {'$regex': '^X.*'}})
print(results)
for result in results:
    print(result)