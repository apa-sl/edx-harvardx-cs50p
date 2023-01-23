# CS50p Problem Set 6: Lines of Code
# https://cs50.harvard.edu/python/2022/psets/6/lines/
#
# Goal: program that counts lines of code in py file pointed out in a cmd-line parameter
# Author: Adam Labedzki 2023-01-15

import sys


def main():
    # check if user has provided cmd-line arg
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # check if user has provided more than 1 cmd-line arg
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # check if there is a .py file type extension in the argument
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a python file")

    # check if file exists
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            print(count_lines(lines))
    except FileNotFoundError:
        sys.exit("File does not exits")


def count_lines(list):
    """ count non-empty lines and lines starting with # """
    total_lines = 0
    for line in list:
        # ignore empty lines
        if len(line.strip()) == 0:
            continue
        # ignore comment lines
        if not line.strip().startswith("#"):
            total_lines += 1

    return total_lines


if __name__ == "__main__":
    main()