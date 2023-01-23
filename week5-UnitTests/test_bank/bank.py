# CS50p Problem Set 1: Home Federal Savings Bank
# https://cs50.harvard.edu/python/2022/psets/1/bank/
#
# Goal: Prompt the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
# Author: Adam Labedzki 2023-01-06

def main():
    greeting = input("How you want to greet? ").lstrip()
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello") == True:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()