from operations import add, subtract, multiply, divide
from user_input import get_float_input, display_operations

def main():
    display_operations()
    choice = input("Enter your choice (1, 2, 3 or 4): ")
    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select 1, 2, 3 or 4.")
        return
    
    num1 = get_float_input(input("Enter the first number: "))
    num2 = get_float_input(input("Enter the second number: "))
    
    if choice == '1':
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of subtracting {num2} from {num1} is: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"The result of multiplying {num2} and {num1} is: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"The result of dividing {num1} by {num2} is: {result}")

if __name__ == "__main__":
    main()