from sqlalchemy import Column, Integer, String 
from database import base

# write a class for the table
class Employee(base):
    # give a name to the table
    __tablename__ = 'employees'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,index=True)
    email =Column(String,unique=True,index=True)