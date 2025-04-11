import pytest
from inventory_management import Inventory


def test_add_stock():
    inventory = Inventory()
    inventory.add_stock("Apple", 10)
    assert inventory.stock["Apple"] == 10
    inventory.add_stock("Google", 8)
    assert inventory.stock["Google"] == 8
    #test add_stock function

def test_remove_stock():
    inventory = Inventory()
    inventory.add_stock("Apple", 10)
    inventory.remove_stock("Apple",4)
    assert inventory.stock["Apple"] == 6
    with pytest.raises(ValueError):
        inventory.remove_stock("Apple",7)


# test remove stock function along with exception

def test_check_availability():
    inventory = Inventory()
    inventory.add_stock("Apple", 10)
    assert inventory.check_availability("Apple", 9)
    assert inventory.check_availability("Apple", 2)


# test check_availability function

def test_remove_stock_with_insufficient_inventory():
    inventory = Inventory()
    inventory.add_stock("Apple", 10)
    with pytest.raises(ValueError):
        inventory.remove_stock("Apple",11)




# rest exception situation in remove stock function

def test_full_inventory_cycle():
    inventory = Inventory()
    inventory.add_stock("Apple", 10)
    inventory.remove_stock("Apple", 6)
    assert inventory.check_availability("Apple", 4)
    inventory.remove_stock("Apple", 4)
    assert not inventory.check_availability("Apple", 1)

# test entire cycle which is add_stock -> remove_stock -> check_availibility