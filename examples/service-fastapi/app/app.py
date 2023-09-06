import os

from fastapi import FastAPI

from .service import router

### When managed by Jupyterhub, the actual endpoints
### will be served out prefixed by /services/:name.
### One way to handle this with FastAPI is to use an APIRouter.
### All routes are defined in service.py

app = FastAPI(
    title="Example FastAPI Service",
    version="0.1",
    openapi_url=f"{router.prefix}/openapi.json",
    docs_url=f"{router.prefix}/docs",
    redoc_url=f"{router.prefix}/redoc",
    swagger_ui_init_oauth={"clientId": os.environ["JUPYTERHUB_CLIENT_ID"]},
    swagger_ui_oauth2_redirect_url=os.environ["JUPYTERHUB_OAUTH_CALLBACK_URL"],
)
app.include_router(router)
