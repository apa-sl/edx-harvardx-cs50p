# CS50p Problem Set 1: Home Federal Savings Bank
# https://cs50.harvard.edu/python/2022/psets/1/bank/
#
# Goal: Prompt the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
# Author: Adam Labedzki 2023-01-06

greeting = input("How you want to greet? ").lower().lstrip()

if greeting.startswith("hello") == True:
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")