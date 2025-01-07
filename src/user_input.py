from utils import display_error_message

def display_operations(operations):
    """
    Displays the available operations to the user.
    """
    print("\nAvailable operations:".upper())
    for key, value in operations.items():
        print(f"{key}. {value[0]}".upper())
    print("0. Exit")
    

def get_user_choice(operations):
    """
    Prompts the user to choose an operation.
    Validates the user's choice and returns it if valid, or shows an error if invalid.
    """
    display_operations(operations)
    
    while True:
        choice = input("\nChoose an operation (0 to exit): ".upper()).strip()
        print()

        if choice in operations or choice == '0':
            return choice
        else:
            display_error_message("Error: Invalid choice! Please select a valid operation.")
            display_operations(operations)

def get_float_input(prompt="Enter a number: "):
    """
    Prompts the user for a valid float input.
    Continues to prompt until a valid float is provided.
    """
    while True:
        input_value = input(prompt)
        try:
            return float(input_value)
        except ValueError:
            display_error_message("Error: Invalid input! Please enter a valid number.")


def get_numbers_for_operation():
    """
    Gets two numbers from the user to perform a mathematical operation.
    Calls `get_float_input` to gather both numbers.
    """
    num1 = get_float_input("Enter the first number: ")
    num2 = get_float_input("Enter the second number: ")
    print()
    return num1, num2


def get_user_choice_for_continue():
    """
    Asks whether to continue performing operations.
    Returns `True` if the user chooses to continue, or `False` if they choose to exit.
    """
    continue_choice = input("Do you want to perform another operation? (0 to exit, any other key to continue): ").strip()
    return continue_choice != '0'