from fastapi import APIRouter
from fastapi import Body, Depends
from Schemas import Schemas
from db.database import get_db
from Models.Employee import Employee
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/create-all")
def create_employees(EmployeeCreate: Schemas.EmployeeCreate=Body(...) ,db:Session=Depends(get_db)):
     db_return = Employee.create_employee(db, EmployeeCreate=EmployeeCreate)
     return db_return

@router.get("/get-all")
def get_all(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
     db_return = Employee.det_data(db,skip=skip,limit=limit)
     return db_return