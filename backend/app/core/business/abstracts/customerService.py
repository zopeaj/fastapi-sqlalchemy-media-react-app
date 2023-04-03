from app.crud.repository.customerRepository import customerRepository


class CustomerService:
    def __init__(self, customerRepository, imageUtil):
        self.customerRepository = customerRepository
        self.imageUtil = imageUtil

    def saveCustomer(self):
        pass

    def updateCustomer(self):
        pass

    def getCustomer(self):
        pass

    def deleteCustomer(self, customer_id: int):
        pass

customerService = CustomerService(customerRepository)
