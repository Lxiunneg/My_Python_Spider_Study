import asyncio
import requests

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


async def request():
    url = 'https://www.helloxiunneg.com.cn'
    status = requests.get(url).status_code
    return status


def callback(task):
    print('Status:', task.result())


coroutine = request()
task = asyncio.ensure_future(coroutine, loop=loop)
task.add_done_callback(callback)
print('Task:', task)
loop.run_until_complete(task)
print('Task:', task)
