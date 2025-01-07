def display_error_message(message):
    RED = '\033[31m'
    RESET = '\033[0m'
    print(f"{RED}{message}{RESET}")

def display_success_message(message):
    GREEN = '\033[32m'
    RESET = '\033[0m'
    print(f"{GREEN}{message}{RESET}")

def display_warning_message(message):
    YELLOW = '\033[33m'
    RESET = '\033[0m'
    print(f"{YELLOW}{message}{RESET}")
