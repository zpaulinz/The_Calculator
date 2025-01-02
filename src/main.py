from operations import add, subtract, multiply, divide
from user_input import get_float_input, display_operations

def main():
    operations = {
        '1': {'name': 'Add', 'func': add},
        '2': {'name': 'Subtract', 'func': subtract},
        '3': {'name': 'Multiply', 'func': multiply},
        '4': {'name': 'Divide', 'func': divide}
    }
    
    while True:
        display_operations(operations)

        operation = input("\nEnter your choice (1, 2, 3, 4 or 5 to exit): ")

        if operation == '5':
            print("Exit")
            break

        if operation in operations:
            num1 = get_float_input("Enter the first number: ")
            num2 = get_float_input("Enter the second number: ")

            result = operations[operation]['func'](num1, num2)
            print(f"The result is: {result if isinstance(result, str) else round(result, 2)}")

        else:    
            print("Error: invalid choice. Please select a valid operation.")
            

if __name__ == "__main__":
    main()