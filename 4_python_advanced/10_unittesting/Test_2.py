import pytest

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(2.5, 3) == 7.5
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(6, 2) == 3
    assert divide(6.0, 2) == 3.0
    #assert divide(6, 0) == pytest.raises(ValueError)
    with pytest.raises(ValueError):
        divide(6, 0)
