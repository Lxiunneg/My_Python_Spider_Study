import httpx

url = 'https://spa16.scrape.center/'

client = httpx.Client(http2=True)  # 打开h2协议请求,client变量接收一个已经支持h2请求的对象
r = client.get(url)

# 可以简化成一下形式，只不过不能重复以HTTP/2.0协议请求
# r = httpx.Client(http2=True).get(url)

print(r.text)