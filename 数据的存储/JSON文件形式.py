import json

str = """
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1992-10-18"
},{
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-10-18"
}]
"""
print(type(str))
data = json.loads(str)
print(type(data))
print(data)

print(data[0]['name'])
print(data[1]['birthday'])