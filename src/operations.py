def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Error: Division by 0!")
    return a / b

def exponentiation(a, b):
    if a == 0 and b < 0:
        raise ValueError("Error: 0 cannot be raised to a negative exponent.")
    return a ** b

