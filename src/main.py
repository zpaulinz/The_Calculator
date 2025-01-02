from operations import add, subtract, multiply, divide
from user_input import get_float_input, display_operations

def main():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    
    while True:
        display_operations()

        operation = input("\nEnter your choice (1, 2, 3, 4 or 5): ")

        if operation == '5':
            print("Exit")
            break

        if operation in operations:
            num1 = get_float_input("Enter the first number: ")
            num2 = get_float_input("Enter the second number: ")

            result = operations[operation](num1, num2)
            print(f"The result is: {result if isinstance(result, str) else round(result, 2)}")

        else:    
            print("Invalid choice. Please select a valid operation.")
            

if __name__ == "__main__":
    main()