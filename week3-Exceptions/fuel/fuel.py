# CS50p Problem Set 2: Fuel Gauge
# https://cs50.harvard.edu/python/2022/psets/3/fuel/
#
# Goal: prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
# Author: Adam Labedzki 2023-01-09

def main():
    # get fuel level as a fraction from the user
    fuel_fraction = input("Fraction: ")

    # check if there is value err or division by zero, if yes repeat prompt to the user
    while True:
        try:
            fuel_level = num_to_percent(fuel_fraction)
        except (ValueError, ZeroDivisionError):
            fuel = input("Fraction: ").strip()
        else:
            break
    # output properly formated info
    if type(fuel_level) == str:
        print(fuel_level)
    else:
        print(f"{fuel_level}%")


def num_to_percent(s):
    # extract X & Y from the user input
    values = s.split("/")

    # check: X, Y should be int
    x = int(values[0])
    y = int(values[1])
    # check: X should be <= Y
    if x > y:
        raise ValueError
    # check: Y should != 0
    if y == 0:
        raise ZeroDivisionError

    # calculate the percentage fuel level
    value_percent = int(round(int(values[0])/int(values[1])*100, 0))

    # check if level is in E or F range:
    if value_percent <= 1:
        return "E"
    elif value_percent >= 99:
        return "F"
    else:
        return value_percent


main()