from fastapi import APIRouter, status, Path, Field
from fastapi.responses import Response, JSONResponse
from app.schema.customerSchema import CustomerCreateResponse, CustomerUpdateResponse, CustomerDeleteResponse, CustomerQueryResponse

customerroutes = APIRouter()

@customerroutes.post("/", response_model=CustomerCreateResponse)
def create_customer() -> Any:
    pass

@customerroutes.update("/{id}", response_model=CustomerUpdateResponse)
def update_customer() -> Any:
    pass

@customerroutes.delete("/{id}", response_model=CustomerDeleteResponse)
def delete_customer(id: int = Path(...)):
    pass

@customerroutes.get("/{id}", response_model=CustomerDeleteResponse)
def get_customer(id: int = Path(...)):
    pass

