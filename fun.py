import asyncio
import sys


print(sys.version)

async def doit(i: str, s: int):
    print("Start %d" % i)
    await asyncio.sleep(s)
    print("End %d" % i)
    return i


def app_loop():
    task_number = 0
    while True:
        task_number = task_number + 1
        s = int(sys.stdin.readline())
        asyncio.ensure_future(doit(task_number, s))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print("Ok")
    print('before')
    loop.run_until_complete(loop.run_in_executor(None, app_loop))
    print('oops')
