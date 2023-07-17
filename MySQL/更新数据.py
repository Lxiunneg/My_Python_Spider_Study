import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql, (1009, 'JR'))
    db.commit()
except:
    db.rollback()
db.close()
