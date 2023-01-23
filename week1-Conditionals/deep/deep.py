# CS50p Problem Set 1: Deep Thought
# https://cs50.harvard.edu/python/2022/psets/1/deep/
#
# Goal: Prompt the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
# Author: Adam Labedzki 2023-01-06

answer = input("What is the Great Question of Life? ").lower().strip()

match answer:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")