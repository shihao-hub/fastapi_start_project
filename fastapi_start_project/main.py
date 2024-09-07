import configparser
import os

import uvicorn

from fastapi import FastAPI

import settings
from apps import authentication
from apps import index
from settings import BASE_DIR

# Windows 平台下，使用 /，暂时先不用 os.path.join 了！
config = configparser.ConfigParser()
config.read(BASE_DIR + "/config/config.ini", encoding="utf-8")

app = FastAPI(**dict(
    title="学习 FastAPI 框架文档",
    description=open(BASE_DIR + "/config/fastapi_doc/fastapi_description.md", encoding="utf-8").read(),
    version="0.0.1",
    debug=True,
))

# 挂在静态资源文件目录
app.mount("/static", settings.staticfiles, name="static")

# 注册 urls （简单模仿一下 Django 的文件目录的，这种简单的方式可以让项目结构清晰明了，很舒服）
authentication.urls.register(app)
index.urls.register(app)

if __name__ == '__main__':
    app_model_name = os.path.basename(__file__)[:-3]
    uvicorn.run(f"{app_model_name}:app", host="127.0.0.1", port=8888, reload=True)
