import json
# with open('data.json','r',encoding='utf-8') as file:
#     str = file.read()
#     data = json.loads(str)
#     print(data[0]['name'])

data = json.load(open('data.json','r',encoding='utf-8'))
print(data[0]['name'])