# CS50p Problem Set 4: Frank, Ian and Glen’s Letters
# https://cs50.harvard.edu/python/2022/psets/4/figlet/
#
# Goal: render text in nice ASCII art text based on figlet
# Author: Adam Labedzki 2023-01-11

import sys
from pyfiglet import Figlet
from random import choice


figlet = Figlet()


def main():
    # if there are no params use random font
    if len(sys.argv) == 1:
        font = choice(figlet.getFonts())
        figletize("Input: ", font)
    # if there is font param check if the param flag is OK and font exists
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        figletize("Input: ", font)
    else:
        sys.exit("Invalid usage")


def figletize(prompt, f):
    # get text input from the user
    text = input(prompt).strip()
    # convert inputed string using figlet
    figlet.setFont(font=f)
    # print results
    print("Output:")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()