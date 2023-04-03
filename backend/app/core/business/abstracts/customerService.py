from app.crud.repository.customerRepository import customerRepository
from app.core.utils.imageUtils import imageUtils

class CustomerService:
    def __init__(self, customerRepository):
        self.customerRepository = customerRepository

    def saveCustomer(self):
        pass

    def updateCustomer(self, customer_id, data, files):
        pass

    def getCustomerById(self, customer_id: int):
        pass

    def deleteCustomer(self, customer_id: int):
        pass

customerService = CustomerService(customerRepository)
