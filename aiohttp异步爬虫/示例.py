import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status


async def main():
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'https://helloxiunneg.com.cn')
        print(f'html:{html[:100]}...')
        print(f'status:{status}')

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

"""Python3.6及以上写法"""
if __name__ == '__main__':
    asyncio.run(main())