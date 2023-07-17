import csv
import pandas as pd

# with open('data.csv','w',encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','Mike',20])
#     writer.writerow(['10002','Bob',22])
#     writer.writerow(['10003','Selina',43])
#     writer.writerows([['10004','刘',33],['10005','蒋',25],['10006','欣彤',19]])

data = [
    {'id': '10001', 'name': '蒋欣彤', 'age': 20},
    {'id': '10002', 'name': '刘杰', 'age': 22},
]
df = pd.DataFrame(data)
df.to_csv('data.csv',index=False)