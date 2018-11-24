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
    res = pow(7, n)
    print("End exec", i, ':', res)

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
            coro = do_async_sleep(task_number, n)

        if splits[0] == 'x':
            coro = loop.run_in_executor(executor, execution_job, task_number, n)

        if coro is None:
            print('Bad task...')
            continue

        print('Send task...', splits[0], task_number)
        asyncio.run_coroutine_threadsafe(coro, loop=callback_loop)


if __name__ == "__main__":
    print("Start")
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(max_workers=None)
    loop.run_until_complete(loop.run_in_executor(None, input_reader_loop, loop, executor))
