import asyncio
import concurrent.futures
import functools
import time

import aiohttp
import requests

URL = "https://www.baidu.com"
MAX_NUMBER = 50


def take_up_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("开始执行 ---> ")
        start_s = time.time()
        res = func(*args, **kwargs)
        using = (time.time() - start_s) * 1000
        print(f"结束执行，消耗时间为：{using} ms")

    return wrapper


def request_sync():
    return requests.get(URL)


async def request_async():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            pass


@take_up_time
def run_sync():
    for _ in range(MAX_NUMBER):
        request_sync()


@take_up_time
def run_sync_but_thread(max_workers=3):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = [pool.submit(request_sync) for _ in range(MAX_NUMBER)]
        for _ in concurrent.futures.as_completed(futures):
            pass


@take_up_time
def run_async():
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(request_async()) for _ in range(MAX_NUMBER)]
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)


if __name__ == '__main__':
    # run_sync() # 7037.7442836761475 ms
    # run_sync_but_thread(8)  # 1121.5815544128418 ms
    # run_async()  # 389.65868949890137 ms
    pass
