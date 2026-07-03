import pytest
from calculator import add, subtract, multiply, divide, percentage, power
from utils import is_number


def test_add():
    assert add(5, 7) == 12
    assert add('a', 7) is None
    assert add(5, 'b') is None


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract('a', 4) is None
    assert subtract(10, 'b') is None


def test_multiply():
    assert multiply(5, 7) == 35


def test_divide():
    assert divide(10, 2) == 5


def test_percentage():
    assert percentage(5, 10) == 50.0


def test_power():
    assert power(2, 3) == 8
