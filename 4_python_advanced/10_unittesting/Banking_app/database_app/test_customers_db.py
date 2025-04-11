import pytest

from customers_db import CustomersDB

def test_insert_customer():
    db = CustomersDB()
    db.connect()

    db.insert_customer("Iqram","iqp@gmail.com")
    customer = db.get_customer_by_name("Iqram")

    assert customer is not None
    assert customer['name'] == "Iqram"
    assert customer['email'] == "iqp@gmail.com"

    db.clear_customers()
    db.close()
