import sqlite3

from redis import StrictRedis

redis = StrictRedis(encoding="utf-8")

REDIS_INCR_KEY = "sqlite3_connect:user_id"


def get_counter_from_redis():
    res: bytes = redis.get(REDIS_INCR_KEY)
    print(type(res))  # <class 'bytes'>
    print(res)
    return int(res)


def get_and_incr_counter_from_redis():
    redis.incrby(REDIS_INCR_KEY)
    return int(redis.get(REDIS_INCR_KEY))


conn = sqlite3.connect("./test.db")

cursor = conn.cursor()

cursor.execute("""
create table if not exists user
(
id INT PRIMARY KEY NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL
);
""")

cursor.execute(f"insert into user (id,username,password) "
               f"values ({get_and_incr_counter_from_redis()},'xiaozhong','123456')")
cursor.execute(f"insert into user (id,username,password) "
               f"values ({get_and_incr_counter_from_redis()},'muyu','123456')")

cursor.execute(f"delete from user where id<={max(0, get_counter_from_redis() - 5)}")

cursor = cursor.execute(f"select id, username, password from user")
for row in cursor:
    print(row)

conn.commit()

conn.close()
