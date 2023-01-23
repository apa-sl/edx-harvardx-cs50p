# CS50p Problem Set 7: Response Validation
# https://cs50.harvard.edu/python/2022/psets/7/response/
#
# validates using PyPI package if provided email is valid
# Author: Adam Labedzki 2023-01-19

from validator_collection import checkers


def main():
    print(validate_email(input("What's your email address? ")))


def validate_email(email):
    """ checks if provided email is a proper one or not """
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()