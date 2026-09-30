from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    name: str
    age: int
    income: float
    loan_amount: float
    employeement_years: int

@app.post("/predict")
def predict_loan(application: LoanApplication):
    if (application.age >= 18 and application.income >= 50000 and application.employeement_years > 3):
        decission = 'Approved'
    else:
        decission = 'Reject'
    return {
        "Applicant_Name": application.name,
        "Applicant_age": application.age,
        "Applicant_income": application.income,
        "Loan_amount_of_applicant": application.loan_amount,
        "Is_Approved": decission
    }