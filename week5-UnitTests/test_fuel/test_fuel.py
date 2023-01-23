# CS50p Problem Set 5: Refueling
# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/
#
# Goal: implement min. 2 test_ functions for unit testing of convert() & gauge() functions
# # Author: Adam Labedzki 2023-01-14


import pytest
from fuel import convert, gauge


def test_convert_x_larger_than_y():
    with pytest.raises(ValueError):
        convert("3/2")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_ok_values():
    assert convert("1/100") == 1
    assert convert("2/4") == 50
    assert convert("4/4") == 100


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"