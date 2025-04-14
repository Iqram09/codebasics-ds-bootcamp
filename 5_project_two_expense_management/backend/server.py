from fastapi import FastAPI
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel


class Expense(BaseModel):
    #expense_date: date
    amount: float
    category: str
    notes: str

app = FastAPI()

@app.get("/expenses/{expense_date}", response_model= List[Expense])
def get_expense(expense_date: date):
    expenses = db_helper.fetch_expense_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=404, detail="No data found")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date,expense: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expense:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "success"}
