import pymysql

"""待添加的信息"""
id = '20210101'
name = '修能'
age = 20

db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor = db.cursor()

sql = 'INSERT INTO students(id,name,age) value(%s,%s,%s)'
try:
    cursor.execute(sql,(id,name,age))
    db.commit()
except:
    db.rollback()
db.close()