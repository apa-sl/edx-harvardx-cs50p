# CS50p Problem Set 7: Numb4rs
# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
#
# Goal: validate if use has inputed IPv4 address using regex expressions
# Author: Adam Labedzki 2023-01-17

import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    """ checks with regex if the inputted adress is an IPv4 """
    if matches := re.search(r"^(?:(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]){1}$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()