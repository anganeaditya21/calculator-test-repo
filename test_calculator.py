import pytest
from calculator import add, subtract, multiply, divide, percentage, power
from utils import is_number, validate_input


def test_add():
    assert add(2, 3) == 5
    assert add('a', 3) is None
    assert add(2, 'b') is None


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract('a', 3) is None
    assert subtract(5, 'b') is None


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(6, 3) == 2
    # TODO: test division by zero


def test_percentage():
    assert percentage(2, 10) == 20.0


def test_power():
    assert power(2, 3) == 8


def test_is_number():
    assert is_number(2)
    assert is_number(2.5)
    assert not is_number('a')


def test_validate_input():
    assert validate_input(2, 3)
    assert not validate_input('a', 3)
    assert not validate_input(2, 'b')
