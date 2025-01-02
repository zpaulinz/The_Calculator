def get_float_input(prompt="Enter a number: "):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
