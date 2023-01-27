from sqlalchemy import Column,Date,Integer,String
from sqlalchemy.orm import  Session
from db.database import Base
from Schemas import Schemas


class Employee(Base):
     __tablename__ = "employee"

     id = Column(Integer, primary_key = True, index=True)
     fname = Column(String , nullable = False, index = True)
     lname = Column(String , nullable = False, index = True)
     # date = Column(Date, nullable = False, index = True)
     # salary = Column(Integer, nullable = False, index = True)

     def create_employee(db:Session, EmployeeCreate: Schemas.EmployeeCreate):
          db_return = Employee(
               fname = EmployeeCreate.fname,
               lname = EmployeeCreate.lname
          ) 
          db.add(db_return)
          db.commit()
          db.refresh(db_return)
          return db_return

     def det_data(db:Session, skip: int=0, limit: int=100):
          return  db.query(Employee).offset(skip).limit(limit).all()
