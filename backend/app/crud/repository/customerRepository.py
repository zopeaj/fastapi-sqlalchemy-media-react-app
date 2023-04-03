from sqlalchemy.orm import Session
from app.db.getDb import get_db
from app.models.customer import Customer
from fastapi.encoders import jsonable_encoders
from typing import Union, Dict, Any, Optional


class CustomerRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self, customer: CustomerCreate) -> Customer:
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

    def delete(self, *, customer_id: int) -> Customer:
        customer_obj = self.db.query(Customer).get(customer_id)
        self.db.delete(customer_obj)
        self.db.commit()
        return customer_db

    def updateCustomerCustom(self, customer_id: int, customer_update: Union[UpdateCustomer, Dict[str, Any]], files: Any) -> Customer:
        customer_to_update = self.getCustomerById(customer_id)
        if customer_to_update is None:
            return None
        customer_obj_data = jsonable_encoders(customer_to_update)
        if isinstance(customer_update, dict):
            update_data = customer_update
        else:
            update_data = customer_update.dict(exclude_unset=True)

        for field in customer_obj_data:
            if field in update_data:
                setattr(customer_obj_data, field, update_data[field])
        for field in customer_obj_data:
            if field in update_data:
                setattr(customer_obj_data, field, update_data[field])
        self.db.add(customer_obj_data)
        self.db.commit()
        self.db.refresh(customer_obj_data)



    def update(self, customer_id: int, customer_update: Union[UpdateCustomer, Dict[str, Any]], files: Any) -> Customer:
        customer_to_update = self.getCustomerById(customer_id)
        customer_obj_data = jsonable_encoders(customer_to_update)
        if isinstance(customer_update, dict):
            update_data = customer_update
        else:
            update_data = customer_update.dict(exclude_unset=True)
        if customer_to_update is None:
            return None
        customer_to_update.setFirstName(customer_update.getFirstName())
        customer_to_update.setLastName(customer_update.getLastName())
        try:
            with store_context(store):
                customer_to_update.picture.from_file(files)
        except Exception:
            self.db.rollback()
            raise
        self.db.add(customer_to_update)
        self.db.commit()
        self.db.refresh(customer_to_update)
        return customer_to_update


    def getById(self, customer_id: int) -> Optional[Customer]:
        return self.db.query(Customer).filter(Customer.getId() == customer_id).first()

    def getByEmail(self, customer_email: str) -> Optional[Customer]
        return self.db.query(Customer).filter(Customer.getEmail() == customer_id).first()

customerRepository = CustomerRepository()
