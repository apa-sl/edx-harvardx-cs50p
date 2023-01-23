# CS50p Problem Set 2: Felipe’s Taqueria
# https://cs50.harvard.edu/python/2022/psets/3/taqueria/
#
# Goal: Enables user to place an order from Felipe's Taqueria menu
# Author: Adam Labedzki 2022-01-09

"""
pseudocode:
0. initialize the menu
1. get item name from the user (case insensitive)
    if ctrl+d: stop asking for more items and display total bill
2. check if item menu is on the menu
    if yes: add to the bill and display current amount f($0.00)
            ask user for another item
    if no:  do nothing
"""

# initialize the menu dict
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# initizialize bill
bill = 0

# run everything in a loop so user can enter multiple items
while True:
    try:
        # get item to buy from the user
        item = input("What to order? ").title()

    # handle ctrl+d to finish items entering and break loop
    except EOFError:
        print(f"\nTotal bill: ${bill:.2f}")
        break

    else:
        # if item on the menu add it to the bill and display current amount
        if item in menu:
            bill += menu[item]
            print(f"Current bill: ${bill:.2f}")