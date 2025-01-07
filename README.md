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
├── LICENSE
└── README.md                
```
In this structure:
- `src/calculator.py` contains the 'Calculator' class, which manages operations and performs calculations based on user input
- `src/operations.py` contains mathematical functions (add, subtract, multiply, divide, exponentiate) used by the 'Calculator' class
- `src/user_input.py` handles user input validation, including operation selection, number entry, and asking about continuation
- `src/utils.py` contains helper functions for displaying success, error, and warning messages in color enhancing UX
- `src/main.py` contains the core program logic that integrates all components and interacts with the user
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



