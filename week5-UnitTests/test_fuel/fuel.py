# CS50p Problem Set 2: Fuel Gauge
# https://cs50.harvard.edu/python/2022/psets/3/fuel/
#
# Goal: prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
# Author: Adam Labedzki 2023-01-09

def main():
    # get fuel level as a fraction from the user
    fuel_fraction = input("Fraction: ").strip()

    # check if there is value err or division by zero, if yes repeat prompt to the user
    while True:
        try:
            fuel = convert(fuel_fraction)
        except (ValueError, ZeroDivisionError):
            fuel_fraction = input("Fraction: ").strip()
        else:
            break

    # output properly formated info
    print(gauge(fuel))


def convert(fraction):
    # extract X & Y from the user input
    values = fraction.split("/")

    # check: X, Y should be int
    x = int(values[0])
    y = int(values[1])
    # check: X should be <= Y
    if y == 0:
        raise ZeroDivisionError
    elif x > y or x < 0 or y < 0:
        raise ValueError
    # check: Y should != 0


    # calculate the percentage fuel level
    value_percent = int((x/y)*100)
    return value_percent


# check if level is in E or F range:
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (str(percentage)+"%")


if __name__ == "__main__":
    main()