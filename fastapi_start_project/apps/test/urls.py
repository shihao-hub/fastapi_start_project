import asyncio
import datetime
import threading
import time
from typing import List, Optional

import aiofiles
from fastapi import FastAPI, Request, APIRouter, File, Form, Response, Cookie
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

    @router.get("/user/{user_id}/article/{article_id}")
    async def user_article_callback(user_id: int, article_id: str):
        return {
            "user_id": user_id,
            "article_id": article_id,
        }

    @router.get("/uls/{file_path:path}")
    async def uls_file_path_callback(response: Response, file_path: str):
        # 2024-09-17：注意这个参数 response: Response，fastapi 会根据类型映射所有参数，顺序和形参名变化都没问题！
        response.set_cookie(f"uls_uls", str(datetime.datetime.now()))
        return {"file_path": file_path}  # 此处返回的类型不需要是 Response

    @router.get("/get_Cookie")
    async def get_cookie(uid: Optional[str] = Cookie(None)):
        print(uid)
        return "set_Cookie ok"

    @router.post("/async_file", summary="File 形式的-单文件上传")
    async def async_file(file: bytes = File(...)):
        # 前端会将文件数据的字节形式发过来，后端会将其异步写入到文件中
        async with aiofiles.open("./async_file.bat", "wb") as f:
            await f.write(file)
        return {"file_size": len(file)}

    @router.post("/async_file2", summary="File 列表形式的-多文件上传")
    async def async_file2(files: List[bytes] = File(...)):
        return {"file_sizes": [len(file) for file in files]}

    app.include_router(router)
