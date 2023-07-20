import asyncio
import aiohttp

async def main():
    data = {'name': 'xiunneg','age': 20}
    url = 'https://www.httpbin.org/post'
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url,data=data) as response:
            print('status:', response.status)
            print('headers:', response.headers)
            print('body:', await response.text())
            print('bytes:', await response.read())
            print('json:', await response.json())

if __name__ == '__main__':
    asyncio.run(main())