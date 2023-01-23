# CS50p Problem Set 5: Testing my twttr
# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/
#
# Goal: implement min. 1 test_ function for unit testing of twttr program
# Author: Adam Labedzki 2023-01-13

from twttr import shorten


def test_novowels():
        assert shorten("twttr") == "twttr"


def test_with_vowels():
        assert shorten("twittEr") == "twttr"
        assert shorten("you") == "y"


def test_only_vowels():
        assert shorten("iou") == ""


def test_multiword():
        assert shorten("g3t 0v3r h3h3") == "g3t 0v3r h3h3"
        assert shorten("How are you?") == "Hw r y?"