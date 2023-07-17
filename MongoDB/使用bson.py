import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.test
collection = db.students

result = collection.find_one({'_id': ObjectId('64b52fc4da436e2ccbdf4f2d')})
print(type(result))
print(result)