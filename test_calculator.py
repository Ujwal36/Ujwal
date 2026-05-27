from calculator import add, sub

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3
