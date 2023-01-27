from fastapi import APIRouter

from app.Endpoint import Employee

api_router = APIRouter()

api_router.include_router(Employee.router, prefix="/employee", tags=['Employee'])