import asyncio
import threading
import time

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse

import settings

templates = settings.templates


def register(app: FastAPI):
    tags = ["测试"]
    router = APIRouter(prefix="/test", tags=tags)

    @router.get("/sync")
    def sync_function():
        # time.sleep(10)
        print(f"当前同步函数运行的线程 ID：{threading.current_thread().ident}")
        return {"index": "sync"}

    @router.get("/async")
    async def async_function():
        # await asyncio.sleep(10)
        # 这里测试可以发现，主程序只要没有重启，这里的 ID 永远不会变
        print(f"当前异步函数运行的线程 ID：{threading.current_thread().ident}")
        return {"index": "sync"}

    app.include_router(router)
