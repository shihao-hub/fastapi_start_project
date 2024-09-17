import configparser
import os

import uvicorn

from fastapi import FastAPI

import apps
import settings
from settings import BASE_DIR

# Windows 平台下，使用 /，暂时先不用 os.path.join 了！
config = configparser.ConfigParser()
config.read(BASE_DIR / "config/config.ini", encoding="utf-8")

app = FastAPI(**dict(
    title=config.get("fastapi_config", "title"),
    description=open(BASE_DIR / "config/fastapi_doc/fastapi_description.md", encoding="utf-8").read(),
    version=config.get("fastapi_config", "version"),
    debug=bool(config.get("fastapi_config", "debug")),
))

# 挂载静态资源文件目录
app.mount("/static", settings.staticfiles, name="static")

# (TD)!: 自定义 docs，为了保证模板所需资源可以从本地获取 p53 页


# 注册 urls （简单模仿一下 Django 的文件目录的，这种简单的方式可以让项目结构清晰明了，很舒服）
# apps.authentication.urls.register(app) # 这个先注释掉，因为是随便写的，作用还不明了
apps.index.urls.register(app)
apps.test.urls.register(app)

if __name__ == '__main__':
    # http://127.0.0.1:8888/docs#
    # http://127.0.0.1:8888/redoc#
    app_model_name = os.path.basename(__file__)[:-3]
    uvicorn.run(f"{app_model_name}:app", host="127.0.0.1", port=8888, reload=True)
