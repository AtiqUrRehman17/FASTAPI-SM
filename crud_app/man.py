from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from typing import List
import models, crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency with db
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# create employee
@app.post('/employees', response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)


# get all employees
@app.get('/employees', response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employee(db)


# get single employee
@app.get('/employee/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):

    employee = crud.get_single(db, emp_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


# update employee
@app.put('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def update_employee(
    emp_id: int,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_db)
):

    db_employee = crud.update_employee(db, emp_id, employee)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return db_employee


# delete employee
@app.delete('/delete/{emp_id}', response_model=schemas.EmployeeOut)
def delete_emp(emp_id: int, db: Session = Depends(get_db)):

    db_employee = crud.delete_employee(db, emp_id)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return db_employee