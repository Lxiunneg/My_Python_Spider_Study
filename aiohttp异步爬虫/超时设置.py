import aiohttp
import asyncio

async def main():
    url = 'https://www.httpbin.org/get'
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url) as response:
            print('status:', response.status)

if __name__ == '__main__':
    asyncio.run(main())