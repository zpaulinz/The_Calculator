from operations import add, subtract, multiply, divide, exponentiation

class Calculator:
    def __init__(self):
        self.operations = {
            '1': ('Add', add),
            '2': ('Subtract', subtract),
            '3': ('Multiply', multiply),
            '4': ('Divide', divide),
            '5': ('Exponentiation', exponentiation)
        }
        
    def perform_operation(self, operation, num1, num2=None):
            result = self.operations[operation][1](num1, num2)
            return result
        