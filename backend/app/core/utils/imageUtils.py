import shutil
from sqlalchemy_imageattach import store
from app.db.getDb import get_db
from fastapi import Depends
from sqlalchemy_imageattach.context import store_context
from urllib2 import urlopen
from sqlalchemy.orm import Session

class ImageUtils:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def set_picture_url_data(self, customer, files):
        try:
            with store_context(store):
                customer.picture.from_file(files)
        except Exception:
            self.db.rollback()
            raise
        self.db.commit()
        return customer

    def get_image_urls(self, customer):
        picture_url = None
        with store_context(store):
            picture_url = customer.picture.locate()
        return picture_url

