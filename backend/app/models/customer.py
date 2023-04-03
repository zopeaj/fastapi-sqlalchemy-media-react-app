from app.db.base import Base
from typing import Any
from sqlalchemy import String, Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.core.config.utils.uuidUtils import defaultUUid
from app.models.customerPicture import CustomerPicture
from sqlalchemy_imageattach.entity import image_attachment
import hashlib


class Customer(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=defaultUUid)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    age = Column(Integer)
    picture = image_attachment('CustomerPicture')

    def getFirstName(self) -> str:
        return self.firstname

    def getLastName(self) -> str:
        return self.lastname

    def getEmail(self) -> str:
        return self.email

    def getAge(self) -> int:
        return self.age

    def getPicture(self) -> Any
        return self.picture


    @property
    def object_id(self):
        return int(hashlib.sha1(self.id).hexdigest(), 16)


