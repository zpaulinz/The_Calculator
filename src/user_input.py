def get_float_input(prompt="Enter a number: "):
    while True:
        input_value = input(prompt)
        try:
            return float(input_value)
        except ValueError:
            print("Error: Invalid input! Please enter a valid number.")


def display_operations(operations):
    print("\nAvailable operations:")
    for key, value in operations.items():
        print(f"{key}. {value['name']}")
    print("0. Exit")
