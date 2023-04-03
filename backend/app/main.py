from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.middleware.wsgi import WSGIMiddleware
from sqlalchemy_imageattach.stores.fs import HttpExposedFileSystemStore, FileSystemStore
from app.core.config.settings import settings


app = FastAPI()
fs_store = FileSystemStore(path=settings.LOCAL_VAR_APP_IMAGES, base_url=settings.SERVER_NAME + '/')
fs_store.wsgi_middleware(app)
