# CS50p Problem Set 5: Re-requesting a Vanity Plate
# https://cs50.harvard.edu/python/2022/psets/5/test_plates/
#
# Goal: implement min. 4 test_ functions for unit testing of is_valid() function
# # Author: Adam Labedzki 2023-01-14

from plates import is_valid

def test_ok_length():
    assert is_valid("a") == False
    assert is_valid("abc123") == True

def test_ok_start():
    assert is_valid("ab123") == True
    assert is_valid("a123") == False
    assert is_valid ("AB123") == True

def test_only_alphanumeric():
    assert is_valid("abc123") == True
    assert is_valid("awsm!") == False
    assert is_valid("Me too") == False

def test_number_at_end():
    assert is_valid("abc123") == True
    assert is_valid("abc1z3") == False
    assert is_valid("abc012") == False