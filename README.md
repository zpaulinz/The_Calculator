# The_Calculator [![Python version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)  

A simple Python application that provides basic mathematical operations.  
It allows users to perform addition, subtraction, multiplication, division and exponentiation with real-time input validation.

## Project Structure

The project is organized as follows:
```
The_Calculator/
├── src/
│   ├── calculator.py 
│   ├── operations.py        
│   ├── user_input.py    
│   ├── utils.py     
│   └── main.py              
├── tests/
│   ├── test_calculator.py 
│   ├── test_operations.py   
│   ├── test_user_input.py   
│   └── test_utils.py  
│   └── test_main.py       
├── LICENSE
└── README.md                
```
In this structure:
- `src/calculator.py` contains the `Calculator` class. This class is responsible for managing the available operations and performing the selected operations on user input. It integrates the mathematical functions from `operations.py` with the user choices.
- `src/operations.py` contains the mathematical functions for various operations such as `add`, `subtract`, `multiply`, `divide`, and `exponentiation`. These functions are used by the `Calculator` class to perform calculations based on the user's selection.
- `src/user_input.py` handles user input validation. This module ensures the user provides valid input for operations and numbers. It includes functions for selecting operations, entering numeric values, and asking if the user wants to continue performing operations.
- `src/utils.py` includes utility functions for displaying formatted messages. These functions are used to display success, error, and warning messages in colored text to enhance the UX.
- `src/main.py` contains the core logic that integrates all the components, runs the calculator, and interacts with the user to perform operations. This is where the main loop runs, asking the user for input and executing operations until the user decides to exit.
- `tests/` includes unit tests for all major components of the project

## Requirements  
- Python 3.13.0 is required.  
- The project may work on other versions of Python, but it has only been tested on Python 3.13.0.  

## How to Run the Project
1. Clone the repository:  
```bash
git clone https://github.com/zpaulinz/The_Calculator.git  
cd The_Calculator/src
```

2. Run the program:
```bash 
python3 main.py
```  

## How to Run the Tests  
```bash  
python3 -m unittest tests/test_calculator.py
```  
```bash  
python3 -m unittest tests/test_operations.py
```
```bash  
python3 -m unittest tests/test_user_input.py
```
```bash  
python3 -m unittest tests/test_utils.py
```  
```bash  
python3 -m unittest tests/test_main.py
```  



