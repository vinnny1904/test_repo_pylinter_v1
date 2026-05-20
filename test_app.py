from app import add, multiply

def test_add():
    assert add(2, 3) == 5

def test_multi():
    assert multiply(2, 2) == 4