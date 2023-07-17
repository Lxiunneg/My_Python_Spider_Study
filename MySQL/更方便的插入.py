import pymysql

datas = [
    {
        'id': '20220202',
        'name': 'JR',
        'age': 33
    },
    {
        'id': '20220203',
        'name': 'DZK',
        'age': 23
    },
    {
        'id': '20220204',
        'name': 'GKH',
        'age': 32
    }
]

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

for data in datas:
    table = 'students'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    sql = f'INSERT INTO {table} ({keys}) VALUES ({values})'

    print('keys:' + keys)
    print('values:' + values)
    print('sql:' + sql)
    try:
        if cursor.execute(sql,tuple(data.values())):
            print('Successful!')
            db.commit()
    except:
        print('Failed')
        db.rollback()
db.close()
