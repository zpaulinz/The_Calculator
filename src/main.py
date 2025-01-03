from operations import add, subtract, multiply, divide, exponentiation
from user_input import get_float_input, display_operations

def main():
    """
    Main function to run the calculator program.
    It handles user input, displays operations, and performs calculations.
    """

    operations = {
        '1': {'name': 'Add', 'func': add},
        '2': {'name': 'Subtract', 'func': subtract},
        '3': {'name': 'Multiply', 'func': multiply},
        '4': {'name': 'Divide', 'func': divide},
        '5': {'name': 'Exponentiation', 'func': exponentiation}
    }
    
    while True:
        display_operations(operations)

        operation = input("\nEnter your choice (1, 2, 3, 4, 5 or 0 to exit): ")

        if operation == '0':
            print("Exiting program...")
            break

        if operation in operations:
            num1 = get_float_input("Enter the first number: ")
            num2 = get_float_input("Enter the second number: ")

            try:
                result = operations[operation]['func'](num1, num2)
                print(f"The result is: {result if isinstance(result, str) else round(result, 2)}")
            except ValueError as e:
                print(e)

        else:    
            print("Error: Invalid choice. Please select a valid operation (0-5).")
            

if __name__ == "__main__":
    main()
    