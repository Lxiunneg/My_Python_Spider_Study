import asyncio
import aiohttp
import time

TOTAL_NUMBER = 10

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response


async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    response = await get(url)
    print('Get responses from', url, 'response', response)


tasks = [asyncio.ensure_future(request()) for _ in range(TOTAL_NUMBER)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost Time:', end - start)
