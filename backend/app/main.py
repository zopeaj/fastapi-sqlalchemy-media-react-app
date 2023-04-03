from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.middleware.wsgi import WSGIMiddleware
from sqlalchemy_imageattach.stores.fs import HttpExposedFileSystemStore, FileSystemStore
from app.core.config.settings import settings
from app.api.routes import api_router

app = FastAPI()
fs_store = FileSystemStore(path=settings.LOCAL_VAR_APP_IMAGES, base_url=settings.SERVER_NAME + '/')
fs_store.wsgi_middleware(app)

app.include_router(api_router, prefix="/api/v1/", tags=['app'])
