import requests

# r = requests.get('https://ww.httpbin.com/get')
# print(r.text)

data = {
    'name' : 'germey',
    'age' : '25'
}

r = requests.get('https://www.httpbin.org/get')
# print(type(r.text))
# print(r.text)
print(r.json())
