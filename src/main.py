from operations import add, subtract

def main():
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if choice == '1':
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of subtracting {num2} from {num1} is: {result}")


if __name__ == "__main__":
    main()