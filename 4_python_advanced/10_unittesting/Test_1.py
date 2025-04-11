def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_bignumber():
    assert add(1000, 1000) == 2000