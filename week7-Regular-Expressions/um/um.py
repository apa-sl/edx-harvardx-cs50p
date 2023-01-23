# CS50p Problem Set 7: Regular, um, Expressions
# https://cs50.harvard.edu/python/2022/psets/7/um/
#
# Goal: counts "um" words in a provided string
# Author: Adam Labedzki 2023-01-18

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    """ find all "um" occurences using regex and return lenght of results list """
    return len(re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()