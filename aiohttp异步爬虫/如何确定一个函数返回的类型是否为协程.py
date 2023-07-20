import inspect
import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    return True


def my_function():
    return False


print(inspect.iscoroutinefunction(my_coroutine))  # 输出 True
print(inspect.iscoroutinefunction(my_function))  # 输出 False
