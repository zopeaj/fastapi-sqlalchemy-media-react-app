from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class CustomerImage(BaseModel):
    url: str

class CustomerInDB(BaseModel):
    id: Optional[int] = None
    firstname: Optional[str] = Field(None, title="customer first name data")
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    picture: Optional[Any] = None

class CustomerCreate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

class CustomerUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    image: Optional[CustomerImage] = None

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


