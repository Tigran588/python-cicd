from calculator import add, multiply,divide


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-2, 3) == -6
    assert multiply(0, 10) == 0
