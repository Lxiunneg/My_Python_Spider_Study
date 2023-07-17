import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

condition = {'age': {'$gt': 10}}
result = collection.find_one(condition, {'$inc': {'age': 1}})

print(result)
print(result.matched_count, result.modified_count)
