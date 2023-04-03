from fastapi import APIRouter, status, Path, Field, Depends, Form
from fastapi.responses import Response, JSONResponse
from app.schema.customerSchema import (
    CustomerCreateResponse,
    CustomerUpdateResponse,
    CustomerDeleteResponse,
    CustomerQueryResponse,
    CustomerCreate
)
from app.core.business.abstracts.customerService import customerService

customerroutes = APIRouter()

@customerroutes.post("/", response_model=CustomerCreateResponse)
def create_customer(customer: CustomerCreate) -> Any:
    create_customer = customerService.createCustomer(customer)
    return JSONResponse(content=create_customer, status=status.HTTP_201_CREATED, media_type='application/json')

@customerroutes.update("/{customer_id}", response_model=CustomerUpdateResponse)
def update_customer(customer_id: int = Path(..., title="The ID of the customer to get"), firstname: str = Form(...), lastname: str = Form(...), files: Form(...)) -> Any:
    data = CustomerUpdate(firstname, lastname, files)
    update_customer = customerService.updateCustomer(customer_id, data, files)
    return JSONResponse(content=update_customer, status=status.HTTP_200_OK, media_type='application/json')

@customerroutes.delete("/{customer_id}", response_model=CustomerDeleteResponse)
def delete_customer(customer_id: int = Path(...)):
    delete_customer = customerService.deleteCustomer(customer_id)
    return JSONResponse(content=delete_customer, status=status.HTTP_204_NO_CONTENT, media_type='application/json')

@customerroutes.get("/{customer_id}", response_model=CustomerDeleteResponse)
def get_customer(customer_id: int = Path(...)):
    query_customer = customerService.getCustomerById(customer_id)
    if query_customer is not None:
        return JSONResponse(content=query_customer, status=status.HTTP_200_OK, media_type='application/json')
    return JSONResponse(content=query_customer, status=status.HTTP_404_NOT_FOUND, media_type='application/json')

