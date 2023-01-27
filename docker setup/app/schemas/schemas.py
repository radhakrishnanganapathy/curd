from pydantic import BaseModel
from datetime import date,time

class EmployeeCreate(BaseModel):
     emp_name: str
     # lname: str
     date: date
     salary: int

     class Config:
          orm_mode = True

class EmployeeRead(EmployeeCreate):
     id: int