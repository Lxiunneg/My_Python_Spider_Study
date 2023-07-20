import asyncio
import aiohttp


async def main():
    params = {'name': 'xiunneg', 'age': 20}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.httpbin.org/get',params=params) as response:
            print(await response.text())

if __name__ == '__main__':
    asyncio.run(main())