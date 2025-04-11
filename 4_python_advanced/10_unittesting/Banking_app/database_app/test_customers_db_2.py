import pytest

from customers_db import CustomersDB

@pytest.fixture
def db():
    db_instance = CustomersDB()
    db_instance.connect()
    yield db_instance

    db_instance.clear_customers()
    db_instance.close()



def test_insert_customer(db: CustomersDB):
    db.insert_customer("Iqram","iqp@gmail.com")
    customer = db.get_customer_by_name("Iqram")

    assert customer is not None
    assert customer['name'] == "Iqram"
    assert customer['email'] == "iqp@gmail.com"

def test_get_all_customers(db: CustomersDB):
    db.insert_customer("Iqram","iqp@gmail.com")
    db.insert_customer("Mohammed","mohammed@gmail.com")

    customers = db.get_all_customers()
    assert len(customers) == 2
