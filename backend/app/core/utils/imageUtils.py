import shutil
from sqlalchemy_imageattach import store
from app.db.getDb import get_db
from fastapi import Depends
from sqlalchemy_imageattach.context import store_context
from urllib2 import urlopen


class ImageUtils:
    def __init__(self, customerService):
        self.db: Session = Depends(get_db)
        self.customerService = customerService

    def copy_image_file(self, image, filename):
        with store.open(image) as src:
            with open(filename, 'wb') as dst:
                shutil.copyfileobj(src, dst)

    def store_image_file(self, imagefile, image):
        with open(imagefile, 'rb') as f:
            store.store(image, f)

    def copy_image_file_from_file(self, file, entity):
        try:

            with open(file) as f:
                entity.picture.from_file(f)
            self.dd.commit()
        except Exception:
            self.db.rollback()

    def attaching_from_file_object(self, customer_id, files):
        try:
            customer = self.customerService.getCustomerById(customer_id)
            if customer == None:
                raise Exception("")
            with store_context(store):
                customer.picture.from_file(files['picture'])
        except Exception:
            self.db.rollback()
            raise
        self.db.commit()

    def set_picture_url_data(self, customer_id, files):
        try:
            customer self.customerService.getCustomerById(customer_id)
            picture_url = files['picture_url']
            with store_context(store):
                customer.picture.from_file(urlopen(picture_url))
        except Exception:
            self.db.rollback()
            raise
        self.db.commit()

    def attaching_from_byte_string(self, request, customer_id):
        try:
            customer = self.customerService.getCustomerById(customer_id):
            picture_url = request.values['picture_url']
            image_binary = self.getPictureUrl(picture_url).content
            with store_context(store):
                customer.picture.from_blob(image_binary)
        except Exception:
            self.db.rollback()
            raise
        self.db.commit()

    def get_image_urls(self, request, customer_id):
        customer = self.customerService.getCustomerById(customer_id)
        with store_context(store):
            picture_url = customer.picture.locate()
        return render_template('customer_profile.html', customer=customer, picture_url=picture_url)


    def getting_image_file(self):
        with store_context(store):
            with customer.picture.open_file() as f:
                shutil.copyfileobj(f, dst)

    def getting_image_binary(self):
        with store_context(store):
            blob = customer.picture.make_blob()

    def getting_image_file(self):
        with store_context(store):
            with customer.picture.open_file() as f:
                blob = f.read()

    def getting_image_file_thumbnails(self):
        with store_context(store):
            width_150 = customer.picture.generate_thumbnail(width=150)
            height_300 = customer.picture.generate_thumbnail(height=300)
            half = customer.picture.generate_thumbnail(ratio=0.5)
            # Get their urls
            width_150_url = width_150.locate()
            height_300_url = width_300.locate()
            half = half.locate()

    def finding_thumbnails(self):
        with store_context(store):
            width_150 = customer.picture.finding_thumbnails(width=150)
            height_300 = customer.picture.finding_thumbnails(height=300)
            # Get their urls
            width_150_url = width_150.locate()
            height_300_url = width_300.locate()

    def find_or_create(imageset, width=None, height=None):
        assert width is not None or height is not None
        try:
            image = imageset.finding_thumbnails(width=width, height=height)
        except NoResultFound:
            image = imageset.generate_thumbnail(width=width, height=height)
        return image
