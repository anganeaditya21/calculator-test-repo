# utils.py
# helper functions for the calculator

def is_number(value):
    # check if the value is a number
    try:
        float(value)
        return True
    except:
        return False


def validate_input(a, b):
    # make sure both inputs are numbers
    if is_number(a) == False:
        print("error")
        return False
    if is_number(b) == False:
        print("error")
        return False
    return True


def format_result(result):
    return "Result = " + str(result)
