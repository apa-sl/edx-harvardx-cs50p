# CS50p Problem Set 1: Meal Time
# https://cs50.harvard.edu/python/2022/psets/1/meal/
#
# Goal: prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all.
# Author: Adam Labedzki 2023-01-06

def main():
    # get time from the user
    time = input("What time is it? ")
    # convert it to float
    time = convert(time)

    # check if the time is falling into any meals time
    if time >= 7 and time <= 8:
        return print("breakfast time")
    elif time >= 12 and time <= 13:
        return print("lunch time")
    elif time >= 18 and time <= 19:
        return print("dinner time")


def convert(time):
    # split hours & minutes from the string to separate variables
    hours, minutes = time.split(":")
    # calculate & return decimal hour value
    return int(hours) + int(minutes)/60


if __name__ == "__main__":
    main()