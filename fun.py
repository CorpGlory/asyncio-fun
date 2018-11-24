import asyncio
import sys


print(sys.version)

async def doit(i: str, s: int):
    print("Start %d" % i)
    await asyncio.sleep(s)
    print("End %d" % i)
    return i


def input_reader_loop(callback_loop: asyncio.AbstractEventLoop):
    task_number = 0
    while True:
        task_number = task_number + 1
        s = int(sys.stdin.readline())
        asyncio.run_coroutine_threadsafe(doit(task_number, s), loop=callback_loop)
        asyncio.sleep(1)
        print('Sent task', task_number)


if __name__ == "__main__":
    print("Start")
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(loop.run_in_executor(None, input_reader_loop, loop))
    print('oops')
