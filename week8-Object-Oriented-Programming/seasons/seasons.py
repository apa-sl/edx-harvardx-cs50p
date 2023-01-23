# CS50p Problem Set 8: Seasons of Love
# https://cs50.harvard.edu/python/2022/psets/8/seasons/
#
# User provides birth date and program signs how many minutes he lives, has to use classes
# Author: Adam Labedzki 2023-01-20

from datetime import date, datetime
from validator_collection import checkers
import inflect
import sys


class Person:
    """ person with a birthday, method to count minutes since birthday """
    def __init__(self, birth_date):
        self.birthday = birth_date

    # birthday getter
    @property
    def birthday(self):
        return self._birthday

    # birthday setter
    @birthday.setter
    def birthday(self, birth_date):
        if not checkers.is_date(birth_date):
            sys.exit("Invalid date")
        year, month, day = birth_date.split("-")
        # construct date time (date with 00:00 time)
        self._birthday = datetime.combine(date(int(year), int(month), int(day)), datetime.min.time())


    def __str__(self):
        return f"birthday: {self._birthday}"

    @classmethod
    def get(cls):
        birthday = input("Date of birth: ")
        return cls(birthday)


    def count_minutes(self):
        """ returns how many minutes have passed between birthday & today """
        minutes = datetime.combine(date.today(), datetime.min.time()) - self.birthday
        minutes = minutes.days * 24 * 60
        return minutes

# initialize inflect module engine
p = inflect.engine()


def main():
    # create person with birthday
    person = Person.get()
    # calcuate and print number of minutes since birthday
    print(f"{translate_digits_to_text(person.count_minutes()).capitalize()} minutes")


def translate_digits_to_text(n):
    """ translate number n to text description """
    return p.number_to_words(n, andword="")


if __name__ == "__main__":
    main()