from sqlalchemy.orm import Session
from app.db.getDb import get_db

class CustomerRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def saveCustomer(self, customer):
        pass

    def deleteCustomer(self, customer_id):
        pass

    def updateCustomer(self, customer, customer_data):
        pass

    def getCustomerById(self, customer_id):
        pass
