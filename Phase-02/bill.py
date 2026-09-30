from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class paksitanBillsystem(BaseModel):
    user_name: str
    consumed_units: int

@app.post("/bill")
def your_bill(bill: paksitanBillsystem):
    fuel_adj_price = 50
    fixed_charges = 500

    if(bill.consumed_units <= 200 and bill.consumed_units >= 0):
        unit_rate = 40
        user_total_bill = unit_rate * bill.consumed_units
    elif(bill.consumed_units > 200 and bill.consumed_units <= 300):
        unit_rate = 80
        user_total_bill = unit_rate * bill.consumed_units
    else:
        unit_rate = 110
        user_total_bill = unit_rate * bill.consumed_units


    return{
        "Consumer_name": bill.user_name,
        "Bill_WithOut_Taxes": user_total_bill,
        "Bill_With_Taxes": user_total_bill + fuel_adj_price + fixed_charges,
        "Unit_Rate_For_You": f"Your unit rate is {unit_rate} because your consumed units are {bill.consumed_units}."
    }