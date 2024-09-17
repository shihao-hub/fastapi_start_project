import pathlib
from typing import Optional

from pydantic import BaseSettings

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

# pathlib 是 Python 的一个标准库模块，提供了一种面向对象的方式来处理文件系统路径，旨在简化文件和目录的操作。
templates = Jinja2Templates(directory=f"{pathlib.Path.cwd()}/templates/")
staticfiles = StaticFiles(directory=f"{pathlib.Path.cwd()}/static/")


class Settings(BaseSettings):
    debug: bool = False
    title: Optional[str]
    description: Optional[str]
    version: Optional[str]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


if __name__ == '__main__':
    a_settings = Settings()
    print(a_settings)
