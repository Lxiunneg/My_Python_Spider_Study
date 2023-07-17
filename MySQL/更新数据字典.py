import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id': '20220202',
    'name': 'JR',
    'age': 33
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = f'INSERT INTO {table} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '
update = ','.join(["{key} = %s".format(key = key) for key in data])
sql += update
print(sql,tuple(data.values()) * 2)
# try:
#     if cursor.execute(sql,tuple(data.values()) * 2):
#         print('Successful!')
#         db.commit()
# except:
#     db.rollback()
db.close()

