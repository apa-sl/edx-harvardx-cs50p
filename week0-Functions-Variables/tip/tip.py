# CS50p Problem Set 0: Tip Calculator
# https://cs50.harvard.edu/python/2022/psets/0/tip/
#
# Goal: program that calculates tip for your server at restaurant
# Some code was provided by CS50 as initial template. My own code is marked with #OWNCODE
# Author: Adam Labedzki 2023-01-04

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # OWNCODE
    d = float(d.replace("$", ""))
    return d


def percent_to_float(p):
    # OWNCODE
    p = float(p.replace("%", ""))/100
    return p


main()