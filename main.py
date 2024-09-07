import configparser
import os
import os.path
import pathlib
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

config = configparser.ConfigParser()
config.read("./config/config.ini", encoding="utf-8")

fastapi_description_file = open("./config/fastapi_doc/fastapi_description.md", encoding="utf-8")

app = FastAPI(**dict(
    title="学习 FastAPI 框架文档",
    description=fastapi_description_file.read(),
    version="0.0.1",
    debug=True,
))

fastapi_description_file.close()

# pathlib 是 Python 的一个标准库模块，提供了一种面向对象的方式来处理文件系统路径，旨在简化文件和目录的操作。
templates = Jinja2Templates(directory=f"{pathlib.Path.cwd()}/templates/")
staticfiles = StaticFiles(directory=f"{pathlib.Path.cwd()}/static/")
# 挂在静态资源文件目录
app.mount("/static", staticfiles, name="static")


@app.get("/", response_class=HTMLResponse)
async def get_response(request: Request):
    return templates.TemplateResponse("index.html", dict(request=request))


@app.get("/app/hello", tags=["app 实例对象注册接口意义示例"])
def app_hello():
    return dict(Hello="app api")


if __name__ == '__main__':
    app_model_name = os.path.basename(__file__)[:-3]
    uvicorn.run(f"{app_model_name}:app", host="127.0.0.1", port=8888, reload=True)
