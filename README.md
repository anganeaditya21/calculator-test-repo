# Simple Calculator

A very small, beginner-style calculator written in plain Python. It performs
basic arithmetic operations and prints the results to the console.

## Project Overview

This project provides functions for addition, subtraction, multiplication,
division, percentage, and power. `main.py` runs a short demo that calls each
of these functions with example values.

## Folder Structure

```
calculator/
├── main.py                 # entry point / demo
├── calculator.py           # core math functions
├── utils.py                # helper functions
├── constants.py            # app constants
├── README.md               # this file
└── tests/
    └── test_calculator.py  # a few unit tests
```

## How to Run

From inside the `calculator/` folder:

```
python main.py
```

To run the tests:

```
python tests/test_calculator.py
```

## Known Issues

- Division by zero is not handled and will crash the program.
- There is duplicated validation logic across files.
- Most functions have no docstrings or type hints.
- Error messages are not helpful (just prints "error").
- Only two functions are covered by tests.
- Some values are hardcoded.

## Future Improvements

- Handle division by zero properly.
- Add type hints and docstrings.
- Remove duplicate validation code.
- Add proper input validation and better error messages.
- Add more unit tests.
- Add logging.
- Support command line arguments / interactive input.
