from app.crud.repository.customerRepository import customerRepository
from typing import Optional
from app.models.customer import Customer

class CustomerService:
    def __init__(self, customerRepository):
        self.customerRepository = customerRepository

    def saveCustomer(self, customer_create: CustomerCreate) -> Customer:
        return self.customerRepository.saveCustomer(customer_create)

    def updateCustomer(self, customer_id, data, files) -> Optional[Customer]:
        return self.customerRepository.update(customer_id, data, files)

    def getCustomerById(self, customer_id: int):
        return self.customerRepository.getById(customer_id)

    def getCustomerByEmail(self, customer_email: str):
        return self.customerRepository.getByEmail(customer_email)

    def deleteCustomer(self, customer_id: int):
        return self.customerRepository.delete(customer_id)

customerService = CustomerService(customerRepository)
