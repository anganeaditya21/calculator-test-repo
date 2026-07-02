# test_calculator.py
# a few basic tests

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from calculator import add, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


if __name__ == "__main__":
    test_add()
    test_subtract()
    print("tests passed")
