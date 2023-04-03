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
    create_user = customerService.createCustomer(customer)
    return JSONResponse(content=create_user, status=status.HTTP_201_CREATED, headers=None, media_type='application/json')


@customerroutes.update("/{customer_id}", response_model=CustomerUpdateResponse)
def update_customer(customer_id: int = Path(..., title="The ID of the customer to get"), firstname: str = Form(...), lastname: str = Form(...), files: Form(...)) -> Any:
    pass

@customerroutes.delete("/{customer_id}", response_model=CustomerDeleteResponse)
def delete_customer(customer_id: int = Path(...)):
    pass

@customerroutes.get("/{id}", response_model=CustomerDeleteResponse)
def get_customer(id: int = Path(...)):
    pass

