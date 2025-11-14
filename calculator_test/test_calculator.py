import pytest
from calculator import sum, subtract, multiply, divide

def test_sum():
    assert sum(3, 5) == 8
    assert sum(-1, 1) == 0
    assert sum(-2, -3) == -5
    assert sum(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0
    assert subtract(-3, -2) == -1
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-1, 1) == -1
    assert multiply(-2, -3) == 6
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 2) == -3
    assert divide(-9, -3) == 3
    assert divide(5, 0) == "Error: Division by zero"

# python -m pytest .\test_calculator.py -v