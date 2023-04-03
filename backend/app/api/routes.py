from fastapi import APIRouter
from app.api.controller.customerController import customerroutes

api_router = APIRouter()
api_router.include_router(customerroutes, prefix="customer", tags=["customer"])

