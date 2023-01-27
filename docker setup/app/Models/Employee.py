from sqlalchemy import Column,Date,Integer,String
from sqlalchemy.orm import  Session
from app.db.database import Base
from app.schemas import schemas


class Employee(Base):
     __tablename__ = "employee"

     id = Column(Integer, primary_key = True, index=True)
     emp_name = Column(String , nullable = False, index = True)
     date = Column(Date , nullable = False, index = True)
     # date = Column(Date, nullable = False, index = True)
     salary = Column(Integer, nullable = False, index = True)

     def create_employee(db:Session, EmployeeCreate: schemas.EmployeeCreate):
          db_return = Employee(
               emp_name = EmployeeCreate.emp_name,
               date = EmployeeCreate.date,
               salary = EmployeeCreate.salary
          ) 
          db.add(db_return)
          db.commit()
          db.refresh(db_return)
          return db_return

     def det_data(db:Session, skip: int=0, limit: int=100):
          return  db.query(Employee).offset(skip).limit(limit).all()

     def delete_data(db:Session, emp_name:str):
          db_return = db.query(Employee).filter(Employee.emp_name == emp_name).delete()
          db.commit()
          return db_return

     def update_data(db:Session,EmployeeCreate: schemas.EmployeeCreate):
          db_return = db.query(Employee).filter(Employee.emp_name==EmployeeCreate.emp_name).update({
               "emp_name" : EmployeeCreate.emp_name,
               "date" : EmployeeCreate.date,
               "salary" : EmployeeCreate.salary})
          db.commit()
          db.refresh(db_return)
          return db_return
