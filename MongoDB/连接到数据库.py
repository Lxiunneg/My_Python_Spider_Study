import pymongo
client = pymongo.MongoClient(host='localhost',port=27017)

db = client.test # 写法1
# db = client['test'] # 写法2

collection = db.students # 写法1
# collection = db['students'] # 写法2

student1 = {
    'id': '10001',
    'name': 'Xiunneg',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '10002',
    'name': 'JR',
    'age': 22,
    'gender': 'male'
}

student3 = {
    'id': '10003',
    'name': 'Dzk',
    'age': 25,
    'gender': 'male'
}
result = collection.insert_one(student1)
result1 = collection.insert_many([student2,student3])
print(result)
print(result.inserted_id)
print(result1)
print(result1.inserted_ids)