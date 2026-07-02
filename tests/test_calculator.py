# test_calculator.py
# a few basic tests

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from calculator import add, subtract, divide, percentage


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) is None


def test_percentage():
    assert percentage(10, 20) == 50.0
    assert percentage(10, 0) is None


def test_divide_error():
    assert divide("a", 2) is None
    assert divide(10, "b") is None

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_divide()
    test_percentage()
    test_divide_error()
    print("tests passed")
