import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.test
collection = db.students

result = collection.delete_one({'name': 'JR'})
print(result)
print(result.deleted_count)