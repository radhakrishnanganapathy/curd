from fastapi import APIRouter
from fastapi import Body, Depends
from app.schemas import schemas
from app.db.database import get_db
from app.Models.Employee import Employee
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/create-all")
def create_employees(EmployeeCreate: schemas.EmployeeCreate=Body(...) ,db:Session=Depends(get_db)):
     db_return = Employee.create_employee(db, EmployeeCreate=EmployeeCreate)
     return db_return

@router.get("/get-all")
def get_all(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
     db_return = Employee.det_data(db,skip=skip,limit=limit)
     return db_return

@router.delete("/delete")
def delete_name(emp_name: str, db:Session=Depends(get_db)):
     db_return = Employee.delete_data(db,emp_name=emp_name)
     return (emp_name, ": Delete Successfully")

@router.put('/update')
def update_data(EmployeeCreate: schemas.EmployeeCreate=Body(...), db:Session=Depends(get_db)):
     print("11111111111111111111111111111111111111111111111111111111111")
     db_return = Employee.update_data(db=db,EmployeeCreate=EmployeeCreate)
     print("################################################x1x")
     return ("update successfully")
