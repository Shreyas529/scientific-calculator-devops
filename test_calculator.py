import calculator
import math

def test_square_root():
    assert calculator.square_root(16) == 4

def test_factorial():
    assert calculator.factorial(5) == 120

def test_natural_log():
    assert round(calculator.natural_log(math.e), 2) == 1.0

def test_power():
    assert calculator.power(2, 3) == 8

