# calculator.py
# core calculator logic

from utils import validate_input


def add(a, b):
    if is_number_check(a) == False:
        print("error")
        return None
    if is_number_check(b) == False:
        print("error")
        return None
    return a + b


def subtract(a, b):
    if is_number_check(a) == False:
        print("error")
        return None
    if is_number_check(b) == False:
        print("error")
        return None
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # TODO: handle division by zero
    return a / b


def percentage(a, b):
    # calculate what percent a is of b
    result = (a / b) * 100
    return result


def power(base, exp):
    # raise base to the power of exp
    if is_number_check(exp) == False:
        print("error")
        return None
    return base ** exp


def is_number_check(value):
    try:
        float(value)
        return True
    except:
        return False
