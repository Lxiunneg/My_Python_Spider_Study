import asyncio
import requests

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


async def request():
    url = 'https://www.helloxiunneg.com.cn'
    status = requests.get(url).status_code
    return status


tasks = [asyncio.ensure_future(request(), loop=loop) for _ in range(5)]
print('Task:', tasks)
loop.run_until_complete(asyncio.wait(tasks))
print('Task', tasks)

for task in tasks:
    print('Rusult:',task.result())