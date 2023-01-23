# CS50p Problem Set 5: Back to the Bank
# https://cs50.harvard.edu/python/2022/psets/5/test_bank/
#
# Goal: implement min. 3 test_ functions for unit testing of value() function
# # Author: Adam Labedzki 2023-01-14

from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello!") == 0


def test_h():
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("hi!") == 20


def test_other():
    assert value("Yo") == 100
    assert value("Good day") == 100
    assert value("good morning") == 100
    assert value ("123") == 100