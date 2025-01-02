def get_float_input(prompt="Enter a number: "):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def display_operations():
    """
    Displays available mathematical operations to the user.
    """
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
