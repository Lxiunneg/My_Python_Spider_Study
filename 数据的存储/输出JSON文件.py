import json

data = [{
    "name": "蒋锐",
    "gender": "男",
    "birthday": "1992-10-18"
}]

with open('data.json','w',encoding='utf-8') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))