import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.test
collection = db.students

count = collection.count_documents({'name': 'Xiunneg'})
print(type(count))
print(count)