from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse

import settings

templates = settings.templates


def register(app: FastAPI):
    tags = ["首页"]
    router = APIRouter(prefix="/index", tags=tags)

    @app.get("/", response_class=HTMLResponse, tags=tags)
    @router.get("/", response_class=HTMLResponse)
    async def get_response(request: Request):
        return templates.TemplateResponse("index.html", dict(request=request))

    @router.get("/hello")
    def app_hello():
        return dict(Hello="app api")

    app.include_router(router)
