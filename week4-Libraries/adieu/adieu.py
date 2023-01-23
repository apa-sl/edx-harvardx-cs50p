# CS50p Problem Set 4: Adieu, Adieu
# https://cs50.harvard.edu/python/2022/psets/4/adieu/
#
# Goal: user inputs n names and program repeats with Adieu, adieu name1, name2, (..) name n-1 and name n
# Author: Adam Labedzki 2023-01-11

import sys
import inflect


def main():
    # initialize list to store names inputed by the user and list for properly joined names (, + and separators)
    names_list = []
    names_joined_list = inflect.engine()

    while True:
        # ask user for names input and store them in the ist
        try:
            name = input("Name: ").strip()
            names_list.append(name)
        # when user will input ctrl+D properly join the names and print them
        except EOFError:
            print(f"Adieu, adieu, to {names_joined_list.join(names_list)}")
            sys.exit()


if __name__ == "__main__":
    main()