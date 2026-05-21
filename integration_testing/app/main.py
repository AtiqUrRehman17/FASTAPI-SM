from fastapi import FastAPI
from pydantic import BaseModel
from app.logic import is_eligible_for_loan

app = FastAPI()

class Applicant(BaseModel):
    income : float
    age : int
    employment_status : str


# endpoints
@app.post('/loan_ligibility')
def check_eligibility(applicant:Applicant):
    eligibility = is_eligible_for_loan(
        income=applicant.income,
        age=applicant.age,
        emplyement_status=applicant.employment_status)
    return {'eligibale':eligibility}