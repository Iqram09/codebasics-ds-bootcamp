import mysql.connector
from logging_setup import setup_logger

from contextlib import contextmanager

logger  = setup_logger('db_helper')


#print("***file is****",__file__)
@contextmanager
def get_db_cursor(commit=False):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="expense_manager")

    cursor = mydb.cursor(dictionary=True)
    yield cursor
    if commit:
        mydb.commit()
    print("Closing cursor")
    cursor.close()
    mydb.close()


# def fetch_all_record():
#     with get_db_cursor() as cursor:
#         cursor.execute("SELECT * FROM expenses")
#         expenses = cursor.fetchall()
#         for expense in expenses:
#             print(expense)


def fetch_expense_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)", (expense_date, amount, category, notes))

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start: {start_date} end: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total FROM expenses WHERE expense_date BETWEEN %s and %s GROUP BY category;''', (start_date, end_date))
        data = cursor.fetchall()
        return data


#if __name__ == "__main__":
    #fetch_all_record()
    #fetch_expense_for_date("2024-08-01")
    #insert_expense("2024-08-01", 300, "Food", "Panipuri")
    # fetest_db_helpertch_expense_for_date("2024-08-20")
    # fetch_expense_for_date("2024-08-20")
     # delete_expenses_for_date("2024-08-20")
    # fetch_expense_for_date("2024-08-20")
