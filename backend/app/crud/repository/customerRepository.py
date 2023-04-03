from sqlalchemy.orm import Session
from app.db.getDb import get_db
from app.models.customer import Customer
from fastapi.encoders import jsonable_encoders
from typing import Union, Dict, Any, Optional


class CustomerRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def saveCustomer(self, customer: CustomerCreate) -> Customer:
        customer_db = Customer(
            customer.getFirstName(),
            customer.getLastName(),
            customer.getEmail(),
            customer.getAge()
        )
        self.db.add(customer_db)
        self.db.commit()
        self.db.refresh(customer_db)
        return customer_db

    def deleteCustomer(self, *, customer_id: int) -> Customer:
        customer_obj = self.db.query(Customer).get(customer_id)
        self.db.delete(customer_obj)
        self.db.commit()
        return customer_db

    def updateCustomer(self, customer_id: int, customer_update: Union[UpdateCustomer, Dict[str, Any]]) -> Customer:
        custom_obj_data = jsonable_encoders(Customer)
        if isinstance(customer_update, dict):
            update_data = customer_update
        else:
            update_data = customer_update.dict(exclude_unset=True)
        for field in custom_obj_data:
            if filed in update_data:
                setattr(custom_obj_data, field, update_data[field])
        self.db.add(custom_obj_data)
        self.db.commit()
        self.db.refresh(custom_obj_data)
        return custom_obj_data

    def getCustomerById(self, customer_id: int) -> Optional[Customer]:
        return self.db.query(Customer).filter(Customer.getId() == customer_id).first()

    def getCustomerByEmail(self, customer_email: str) -> Optional[Customer]
        return self.db.query(Customer).filter(Customer.getEmail() == customer_id).first()

customerRepository = CustomerRepository()
