from app.db.base import Base
from sqlalchemy_imageattach.entity import Image
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from typing import Any

class CustomerPicture(Base, Image):
    """User picture model."""
    customer_id = Column(Integer, ForeignKey('customer.id'), primary_key=True)
    customer = relationship('Customer')

    def getCustomer(self) -> Any:
        return self.customer
