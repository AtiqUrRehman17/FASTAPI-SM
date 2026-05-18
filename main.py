from fastapi import FastAPI,HTTPException
from models import Employee
from typing import List

app = FastAPI()

employee_db: List[Employee] = [] # empty db for the employees


# home 
@app.get('/')
def home():
    return {'message':'Welcome to the Employee Management System'}
# read all the employees
@app.get('/employees',response_model=List[Employee])
def get_employees():
    return employee_db


@app.get('/employees/{emp_id}',response_model=Employee)
def get_employee(emp_id:int):
    for index, employee in enumerate(employee_db):
        if employee.id == emp_id:
            return employee_db[index]
    raise HTTPException(status_code=404,detail='User not fund')

# add an employee
@app.post('/employees',response_model=Employee)
def add_employee(new_id:Employee):
    for employee in employee_db:
        if employee.id == new_id.id:
            raise HTTPException(status_code=400,detail='User Already Exist')
    employee_db.append(new_id)
    return new_id


# upadate an employee
@app.put('/employees/{emp_id}',response_model=Employee)
def update_employee(emp_id:int,updated_employee:Employee):
    for index,employee in enumerate(employee_db):
        if employee.id == emp_id:
            employee_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=400,detail= 'User not fund')

# delete

@app.delete('delete_employee/{emp_id}',response_model=Employee)
def delete(emp_id:int):
    for index,employee in enumerate(employee_db):
        if employee.id == emp_id:
            del employee_db[index]
            return {'message':'Employee deletd successfully'}
    raise HTTPException(status_code=400,detail='User not fund')