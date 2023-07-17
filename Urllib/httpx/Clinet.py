import httpx

headers = {
    'User-Agent' : 'Mozilla 5.0, Windows NT'
}

with httpx.Client(headers=headers) as client:
    r = client.get('https://www.httpbin.org/get')
    print(r)
    print(r.json()['headers']['User-Agent'])

# 以上方法等价与以下方法

# client = httpx.Client(headers=headers)
# try:
#     r = client.get('https://www.httpbin.org/get')
# finally:
#     client.close();