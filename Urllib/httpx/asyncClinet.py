import httpx
import asyncio

async def fetch(url):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        print(r.text)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(fetch('https://www.httpbin.org/get'))