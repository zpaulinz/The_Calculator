# The_Calculator [![Python version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)  

A simple Python application that provides basic mathematical operations.  
It allows users to perform addition, subtraction, multiplication and division with real-time input validation.

## Project Structure

The project is organized as follows:
```
The_Calculator/
├── src/
│   ├── operations.py        
│   ├── user_input.py        
│   └── main.py              
├── tests/
│   ├── test_operations.py   
│   ├── test_user_input.py   
│   └── test_main.py         
└── README.md                
```
In this structure:
- `operations.py` contains the mathematical functions like addition, subtraction, multiplication, and division
- `user_input.py` handles user input, ensuring that the user provides valid data
- `main.py` contains the core logic that integrates all the functions and runs the calculator
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
python main.py
```  

## How to Run the Tests  
```bash  
python3 -m unittest tests/test_operations.py
```
```bash  
python3 -m unittest tests/test_user_input.py
```
```bash  
python3 -m unittest tests/test_main.py
```  

