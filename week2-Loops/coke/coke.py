# CS50p Problem Set 2: Coke Machine
# https://cs50.harvard.edu/python/2022/psets/2/coke/
#
# Goal: prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Author: Adam Labedzki 2023-01-08

def main():
    # configuration (amount due, accepted coins)
    to_pay = 50
    denominations = [25, 10, 5]

    # inform user how much is there to pay and ask him for a coin
    print(f"Amount due: {to_pay}")
    coin = int(input("Insert Coin: "))
    change(to_pay, coin, denominations)
    return

def change(due, paid, denominations):
    # check if inserted coin is among accepted denominations
    if paid in denominations:
        # if yes substract inserted coin from due amount
        due -= paid
        # if there is nothing to pay, inform user is there anything owed
    if due <= 0:
        print(f"Change Owed: {abs(due)}")
        return
    # ask for another coin and do recurrention
    print(f"Amount Due: {due}")
    paid = int(input("Insert Coin: "))
    change(due, paid, denominations)


main()