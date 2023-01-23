# CS50p Problem Set 6: Pizza Py
# https://cs50.harvard.edu/python/2022/psets/6/pizza/
#
# Goal: program is being lanuched with csv file as parameter and renders table as ASCII art using tabulate from PyPI
# Author: Adam Labedzki 2023-01-15

import sys
import csv
from tabulate import tabulate


def main():
    # check if there is 1 argument provided
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # check if there is csv file name as an argument
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    # check if file exists

    try:
        # open csv & save all lines as a menu list
        menu = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)

    except FileNotFoundError:
        sys.exit("File does not exits")
    else:
        # print ASCII table
        print(render_table(menu))


def render_table(data):
    """ prints table using tabulate module. parameters: headers, showindex, tablefmt """
    return tabulate(data, headers="firstrow", tablefmt="grid")


if __name__ == "__main__":
    main()