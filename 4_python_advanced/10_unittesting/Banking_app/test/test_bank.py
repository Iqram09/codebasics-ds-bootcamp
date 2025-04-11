import pytest

from src.bank import BankAccount

def test_bank_account_creation():
    account = BankAccount("Iqram Patel",1000)

    assert account.owner == "Iqram Patel"
    assert account.balance == 1000

def test_bank_account_deposit():
    account = BankAccount("Iqram Patel")
    account.deposit(100)
    account.deposit(200)
    assert account.balance == 300

    with pytest.raises(ValueError):
        account.deposit(-10)

def test_bank_account_withdraw():
    account = BankAccount("Iqram Patel",1000)
    account.withdraw(100)
    account.withdraw(200)
    assert account.balance == 700

    with pytest.raises(ValueError):
        account.withdraw(1000)

@pytest.mark.skip(reason="Skipping due to xyz reason")
def test_get_balance():
    account = BankAccount("Iqram Patel",1000)
    assert account.get_balance() == 1000


