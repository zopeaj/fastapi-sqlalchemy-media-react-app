from pydantic import BaseModel

class CustomerInDB(BaseModel):
    pass

class CustomerCreateResponse(CustomerInDB):
    pass

class CustomerUpdateResponse(CustomerInDB):
    pass

class CustomerDeleteResponse(CustomerInDB):
    pass

class CustomerQueryResponse(CustomerInDB):
    pass

