# main.py
# entry point that demonstrates the calculator

from calculator import add, subtract, multiply, divide, percentage, power
from constants import APP_NAME, VERSION


def main():
    print(APP_NAME + " v" + VERSION)
    print("--------------------")

    x = 10
    y = 5

    print("Addition: " + str(add(x, y)))
    print("Subtraction: " + str(subtract(x, y)))
    print("Multiplication: " + str(multiply(x, y)))
    print("Division: " + str(divide(x, y)))
    print("Percentage: " + str(percentage(x, y)))
    print("Power: " + str(power(2, 8)))

    # demo with some hardcoded values
    print("Extra: " + str(add(100, 200)))
    print("Extra: " + str(multiply(3, 3)))


main()
