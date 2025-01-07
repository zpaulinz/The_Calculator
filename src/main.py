from user_input import get_user_choice, get_numbers_for_operation, get_user_choice_for_continue
from calculator import Calculator

def exit_program():
    print("Exiting program. Thank you for using The_Calculator!")
    exit(0)
    
def main():
    calculator = Calculator()
    
    while True:
        operation = get_user_choice(calculator.operations)

        if operation == '0':
            exit_program()

        num1, num2 = get_numbers_for_operation()
        
        try:
            result = calculator.perform_operation(operation, num1, num2)
            print(f"The result is: {result if isinstance(result, str) else round(result, 2)}")               
            
            if not get_user_choice_for_continue():
                exit_program()
        
        except ValueError as e:
            print(e)   

if __name__ == "__main__":
    main()
    