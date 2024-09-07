import asyncio
import time
import collections
from types import GeneratorType
from typing import Union, Sequence, Coroutine


class EventLoop:
    def __init__(self):
        self.tasks = collections.deque()  # 用于存储待执行的任务

    def create_task(self, coroutine: Union[Coroutine, Sequence]):
        if isinstance(coroutine, Sequence):
            self.tasks.extend(coroutine)
            return
        self.tasks.append(coroutine)  # 将协程添加到任务队列

    def run(self):
        while self.tasks:
            task = self.tasks.popleft()
            try:
                result = next(task)
                print(f"result: {result} - {type(result)}")
                if isinstance(task, GeneratorType):
                    self.tasks.append(task)  # 将生成器添加回任务队列
            except StopIteration as e:
                # 协程正常结束
                print(f"协程({id(task)})结束，返回值为: {e.value}")


def async_func(func):
    """ 装饰器，用于将普通函数转换为协程 """

    def wrapper(*args, **kwargs):
        yield func(*args, **kwargs)

    return wrapper


@async_func
def coroutine_1():
    print("开始执行协程 1 ...")

    # 模拟 I/O 操作
    time.sleep(2)

    print("协程 1 执行完成。")
    return "协程 1 的结果"


@async_func
def coroutine_2():
    print("开始执行协程 2 ...")

    # 模拟 I/O 操作
    time.sleep(2)

    print("协程 2 执行完成。")
    return "协程 2 的结果"


if __name__ == '__main__':
    loop = EventLoop()
    loop.create_task(coroutine_1())
    loop.create_task(coroutine_2())
    loop.run()
