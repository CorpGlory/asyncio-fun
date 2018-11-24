import asyncio
import sys
from concurrent.futures import Executor, ThreadPoolExecutor


async def do_async_sleep(i: str, n: int):
    print("Start sleep", i)
    await asyncio.sleep(n)
    print("End sleep", i)
    return i

def execution_job(i: str, n: int):
    print("Start exec", i)
    k = 0
    for q in range(n * 1000000):
        k = k + 1
    print("End exec", i, ':', n)

def input_reader_loop(callback_loop: asyncio.AbstractEventLoop, executor: Executor):
    task_number = 0
    while True:
        task_number = task_number + 1
        line: str = sys.stdin.readline()
        splits = line.split(' ')

        coro = None
        if len(splits) < 2:
            print('...')
            continue

        n = int(splits[1])

        if splits[0] == 's':
            print('Send sleep task...', task_number)
            asyncio.run_coroutine_threadsafe(do_async_sleep(task_number, n), loop=callback_loop)
            print('Ok')

        if splits[0] == 'x':
            print('Send compute task...', task_number)
            callback_loop.run_in_executor(executor, execution_job, task_number, n)
            print('Ok')



if __name__ == "__main__":
    print("Start")
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(max_workers=20)
    loop.run_in_executor(None, input_reader_loop, loop, executor)
    loop.run_forever()
