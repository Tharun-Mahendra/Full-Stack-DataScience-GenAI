# This module contains basic arithmetic operations
# such as addition, subtraction, multiplication, division, and power.

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a,b):
    return a ** b

