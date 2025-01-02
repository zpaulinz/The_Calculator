def get_float_input(prompt="Enter a number: "):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Error: invalid input! Please enter a valid number.")


def display_operations(operations):
    """
    Displays available mathematical operations to the user.
    """
    print("Available operations:")
    for key, value in operations.items():
        print(f"{key}. {value['name']}")
  
