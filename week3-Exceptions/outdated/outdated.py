# CS50p Problem Set 2: Outdated
# https://cs50.harvard.edu/python/2022/psets/3/outdated/
#
# Goal: convert inputed date from middle-endian format to ISO 8601.
# Author: Adam Labedzki 2023-01-10

"""
accepted us date input formats:
MM/DD/YYYY and Month DD, YYY
"""

# months names reausable for all functions
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():



    while True:
        date = input("Date: ").strip()
        try:
            validate_date(date)
        except ValueError:
            continue
        else:
            print(convert_date(date))
            break


def validate_date(us_date):
    # check if date is with "/" separator
    if "/" in us_date:
        us_date = us_date.split("/")

        # check if there are only digits
        for i in range(len(us_date)):
            if us_date[i].isdigit() == False:
                raise ValueError

        # check if month&day have values in proper ranges and year is no higher than 9999
        if int(us_date[0]) not in range(1,12) or int(us_date[1]) not in range (1,31) or len(us_date[2]) > 4:
            raise ValueError

    # if not, extract data differently
    elif " " in us_date and "," in us_date:
        # remove "," from date
        us_date = us_date.replace(",", "")

        # extract month, day, year from the string
        us_date = us_date.split(" ")

        # check if month & day are in range
        if us_date[0].capitalize() not in months or int(us_date[1]) not in range(1,31):
            raise ValueError

    else:
        raise ValueError

    return True


def convert_date(us_date):
    # check if date was provided as numbers only, if yes extract month, day, year as digits separated with "/"
    if len(us_date) >= 8 and len(us_date) <= 10:
        us_date = us_date.split("/")
        for i in range(len(us_date)):
            us_date[i] = int(us_date[i])

    # if not, extract data differently
    else:
        # extract month, day, year from the string
        us_date = us_date.split(" ")

        # remove , char from the day
        us_date[1] = int(us_date[1].replace(",", ""))

        # convert month to Captalized & int
        us_date[0] = us_date[0].capitalize()

        # convert month name to month digit (1-12)
        us_date[0] = months.index(us_date[0]) + 1

    return f"{us_date[2]}" + "-" + f"{us_date[0]:02}" + "-" + f"{us_date[1]:02}"


main()
