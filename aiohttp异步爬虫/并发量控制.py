import asyncio
import aiohttp
import time

start = time.time()
count = 1
CONCURRENCY = 100
URL = 'https://www.baidu.com'

semaphere = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_api():
    async with semaphere:
        global count
        print('scraping', count, URL)
        count += 1
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()


async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
    await asyncio.gather(*scrape_index_tasks)


if __name__ == '__main__':
    asyncio.run(main())
    end = time.time()
    print('All Cost:', end - start)
