from fastapi import APIRouter

from Endpoint import Employee

api_router = APIRouter()

api_router.include_router(Employee.router, prefix="/employee", tags=['Employee'])