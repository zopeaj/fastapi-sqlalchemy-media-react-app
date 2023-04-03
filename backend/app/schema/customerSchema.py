from pydantic import BaseModel, EmailStr
from typing import Optional


class CustomerInDB(BaseModel):
    id: Optional[int] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    picture: Optional[Any] = None

class CustomerCreateResponse(CustomerInDB):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] =  None
    picture: Optional[Any] = None

class CustomerUpdateResponse(CustomerInDB):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] =  None
    picture: Optional[Any] = None


class CustomerDeleteResponse(CustomerInDB):
    success_data: Optional[str] = None


class CustomerQueryResponse(CustomerInDB):
    id: Optional[int] = None
    lastname: Optional[str] = None
    email: Optional[str] = None


