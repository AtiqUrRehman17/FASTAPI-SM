from sqlalchemy.orm import Session
import schemas,models

# geeting full data
def get_employee(db:Session):
    return db.query(models.Employee).all()


def get_single(db:Session,emp_id:int):
    return (
        db
        .query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )

def create_employee(db:Session,employee : schemas.EmployeeCreate):
    db_employee = models.Employee(
        name=employee.name,email=employee.email
    )
    db.add(db_employee) # adding the new record to the db
    db.commit() # commiting the changes to the db
    db.refresh(db_employee)

    return db_employee

def update_employee(db:Session,emp_id:int,employee : schemas.EmployeeUpdate):
    db_employee = models.Employee(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee :
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit()
        db.refresh()
    return db_employee

def delete_employee(db:Session,emp_id):
    db_employee = models.Employee(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee :
        db.delete(db_employee)
        db.commit()
    return db_employee