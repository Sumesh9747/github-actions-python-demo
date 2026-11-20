
from calculator import add, subtract


def test_addition():
    assert add(10, 20) == 50


def test_subtraction():
    assert subtract(20, 10) == 10
