from user_input import get_user_choice, get_numbers_for_operation, get_user_choice_for_continue
from calculator import Calculator
from utils import display_error_message, display_success_message, display_warning_message

def exit_program():
    display_warning_message("Exiting program. Thank you for using The_Calculator!")
    exit(0)
    
def main():
    calculator = Calculator()
    
    try:
        while True:
            operation = get_user_choice(calculator.operations)

            if operation == '0':
                exit_program()

            num1, num2 = get_numbers_for_operation()
            
            try:
                result = calculator.perform_operation(operation, num1, num2)
                display_success_message(f"The result is: {result if isinstance(result, str) else round(result, 2)}".upper()) 
                print()              
                
                if not get_user_choice_for_continue():
                    exit_program()
            
            except ValueError as e:
                display_error_message(f"{e}")   
                
    except KeyboardInterrupt:
        print()
        exit_program()

if __name__ == "__main__":
    main()
    