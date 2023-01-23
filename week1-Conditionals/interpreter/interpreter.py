# CS50p Problem Set 1: Math Interpreter
# https://cs50.harvard.edu/python/2022/psets/1/interpreter/
#
# Goal: prompt the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place.
# Author: Adam Labedzki 2023-01-06

def main():
    # ask user for the expression and split it to x, y ints & operation
    x, operation, y = input("Expression: ").split(" ")
    x = int(x)
    y = int(y)

    # call interperter function and print the result
    print(interpreter(x, y, operation))


def interpreter(x, y, operation):
    match operation:
        case "+":
            return round(float(x + y), 1)
        case "-":
            return round(float(x - y), 1)
        case "*":
            return round(float(x * y), 1)
        case "/":
            return round(float(x / y), 1)


main()