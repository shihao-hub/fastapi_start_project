from typing import Optional

from pydantic import BaseModel
from starlette import status

from fastapi import Depends, HTTPException, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


def register(app: FastAPI):
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    # 模拟用户数据库
    fake_users_db = {
        "user@example.com": {
            "username": "user@example.com",
            "full_name": "John Doe",
            "email": "user@example.com",
            "hashed_password": "fakehashedsecret",
            "disabled": False,
        }
    }

    # 用户模型
    class User(BaseModel):
        username: str
        full_name: Optional[str] = None
        email: str
        disabled: Optional[bool] = None

        @staticmethod
        def fake_hash_password(password: str):
            """ 认证函数 """
            return "fakehashed" + password

    async def get_current_user(token: str = Depends(oauth2_scheme)):
        user = fake_users_db.get(token)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user

    @app.post("/token")  # 登录路由
    async def login(form_data: OAuth2PasswordRequestForm = Depends()):
        user = fake_users_db.get(form_data.username)
        if not user or not user.get("hashed_password") == User.fake_hash_password(form_data.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return {"access_token": user.get("username"), "token_type": "bearer"}

    @app.get("/users/me", response_model=User)  # 受保护的路由，不太懂，没有这个参数不行...
    async def read_users_me(current_user: User = Depends(get_current_user)):
        return current_user
