from operations import add

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = add(num1, num2)
    
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()