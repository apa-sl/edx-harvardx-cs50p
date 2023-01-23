# CS50p Problem Set 2: Nutrition Facts
# https://cs50.harvard.edu/python/2022/psets/2/nutrition/
#
# Goal: prompts the user to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits
# Author: Adam Labedzki 2023-01-09

def main():
    fruit = input("Item: ").title()
    calories(fruit)


def calories(item):
    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
    }
    if item in fruits:
        return print(f"Calories: {(fruits[item])}")


main()