import threading
import time


# 2024-09-07：这里的代码非常重要，这里的代码对理解异步编程怎么实现的有点帮助


# 模拟异步 I/O 操作的生成器
def async_io_operation(duration):
    print(f"开始 I/O 操作，预计持续 {duration} 秒...")

    yield "start_io", 1, 2, 3

    print("I/O 操作完成")


# 2024-09-09：注意，此处可以变成个线程池！在编程语言的层面应该就可以模拟异步了
#               虽然我不知道实现异步是不是需要更底层来实现，比如 CPython ...
def thread_io_fn(task, *args):
    # 开个线程模拟 await asyncio.sleep(2) 这种操作
    print(task, *args)
    print("睡眠 2 秒")
    time.sleep(2)
    # 唤醒协程
    try:
        next(task)
    except StopIteration:
        pass


# 协程管理器
def coroutine_manager():
    # 创建一个协程
    io_task = async_io_operation(3)

    # 唤醒协程，执行到第一个 yield 处
    event, *args = next(io_task)
    # 如果第一个 yield 是 start_io 操作，则创建对应的线程
    io_thread = None
    if event == "start_io":
        io_thread = threading.Thread(target=thread_io_fn, args=(io_task, *args))
    if io_thread:
        io_thread.start()

    print("主线程在执行其他操作中...")
    time.sleep(20)

    if io_thread:
        io_thread.join()


if __name__ == "__main__":
    coroutine_manager()
