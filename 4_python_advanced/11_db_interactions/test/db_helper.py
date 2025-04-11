import mysql.connector

from contextlib import contextmanager

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


def fetch_all_record():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expense_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)", (expense_date, amount, category, notes))

def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

if __name__ == "__main__":
    #fetch_all_record()
    #fetch_expense_for_date("2024-08-01")
    #insert_expense("2024-08-20", 300, "Food", "Panipuri")
    #fetch_expense_for_date("2024-08-20")


    print("*+xexpenses for 8/28 skikikikk")
    fetch_expense_for_date("2024-08-20")
    print("#kxdelete for 8/20 xkwrixix")
    delete_expenses_for_date("2024-08-20")
    print("xxxagain fetch expenses for 8/20 skirt")
    fetch_expense_for_date("2024-08-20")
