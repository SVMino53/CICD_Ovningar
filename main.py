# A simple calculator application

import sys
import os
import logging


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    run = True
    while run:
        print("-" * 30)
        print("Welcome to simple calculator!")
        print("-" * 30)
        print("What operation do you want to perform?")
        print("Addition: <num1> + <num2>")
        print("\tExapmle: 2 + 3")
        print("Subtraction: <num1> - <num2>")
        print("\tExapmle: 5 - 2")
        print("Multiplication: <num1> * <num2>")
        print("\tExapmle: 4 * 3")
        print("Division: <num1> / <num2>")
        print("\tExapmle: 8 / 2")
        print("Type 'exit' to quit the program.")

        user_input = input("> ")
        if user_input.lower() == 'exit':
            run = False
            print("Exiting the calculator. Goodbye!")
            continue
        try:
            num1, operator, num2 = user_input.split()
            try:
                num1, num2 = int(num1), int(num2)
            except ValueError:
                num1, num2 = float(num1), float(num2)
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator! Please use +, -, *, or /.")
                continue
            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input! Please enter in the format: <num1> <operator> <num2>")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            print("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    main()