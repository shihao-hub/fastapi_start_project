from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

import settings

templates = settings.templates


def register(app: FastAPI):
    @app.get("/", response_class=HTMLResponse)
    async def get_response(request: Request):
        return templates.TemplateResponse("index.html", dict(request=request))

    @app.get("/app/hello", tags=["app 实例对象注册接口意义示例"])
    def app_hello():
        return dict(Hello="app api")
