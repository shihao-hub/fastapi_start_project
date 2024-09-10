import os.path
import pathlib
import sqlite3
from pathlib import Path

import sqlalchemy

SQLITE3_DB_PATH = "./user.db"


# SLAP
# 创建同步 SQLAlchemy 引擎
# 定义数据库表映射模型
# 通过 SQLAlchemy 创建表
# 创建数据库表并查看表信息
# 创建数据库连接会话
# 对模型类进行 CRUD 操作

def create_sync_sqlalchemy_engine():
    url = "SQLite://" + os.path.abspath(SQLITE3_DB_PATH).replace("\\", "/")
    return sqlalchemy.create_engine(url)


def define_database_mapping_model():
    pass


if __name__ == '__main__':
    create_sync_sqlalchemy_engine()
