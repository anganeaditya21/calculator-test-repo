# test_calculator.py
# a few basic tests

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from calculator import add, subtract, power, multiply, divide, percentage


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_power_positive_integer():
    assert power(2, 3) == 8


def test_power_negative_integer():
    assert power(2, -3) == 1/8


def test_power_float():
    assert power(2, 0.5) == 2**0.5


def test_power_error():
    assert power(2, 'a') == None


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(10, 2) == 5


def test_percentage():
    assert percentage(10, 20) == 50

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_power_positive_integer()
    test_power_negative_integer()
    test_power_float()
    test_power_error()
    test_multiply()
    test_divide()
    test_percentage()
    print("tests passed")
