# CS50p Problem Set 2: Grocery List
# https://cs50.harvard.edu/python/2022/psets/3/grocery/
#
# Goal: user can add items to grocery list (one per line). ctrl+d closes the list, display summary (names, quantities, sorted AZ)
# Author: Adam Labedzki 2023-01-10

# initialize grocery list
shopping_list = {}

while True:
    try:
        # ask user for item to add to the list
        item = input().upper()

    except EOFError:
        # on ctrl+d stop asking for items and display whole list sorted AZ with quantities
        for k, v in sorted(shopping_list.items()):
            print(v, k)
        break

    else:
        # check if item is already on the list and increase quantity or add it
        if item in shopping_list:
            shopping_list[item] += 1
        else:
            shopping_list[item] = 1