import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from backend import db_helper




def test_fetch_expense_for_date():
    expenses = db_helper.fetch_expense_for_date("2024-08-20")

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 300.0
    assert expenses[0]['category'] == "Food"
    assert expenses[0]["notes"] == "Panipuri"

def test_fetch_expense_for_date_invalid_date():
    expenses = db_helper.fetch_expense_for_date("9999-08-15")
    assert len(expenses) == 0

def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("2099-01-01", "2099-12-31")
    assert len(summary) == 0

