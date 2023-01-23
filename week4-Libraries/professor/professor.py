# CS50p Problem Set 4: Little Professor
# https://cs50.harvard.edu/python/2022/psets/4/professor/
#
# Goal: user enters No of digits 1-3, program is throwing math problem X+Y at user with random X, Y with the digits count = n. User has 3 tries to answer
# Author: Adam Labedzki 2023-01-13

import random
import sys


def main():
    # configuration and user decision about number of digits in the values
    # how many tasks?
    quantity = 10
    # how many attempts to answer?
    attempts = 3


    tasks = []
    score = 0
    level = get_level()

    # create list of tasks (each task with X, Y and expected result)
    for i in range(quantity):
        tasks.append(generate_integer(level))
        tasks[i].append(tasks[i][0] + tasks[i][1])

    # shot all tasks at user 1 by 1
    for i in range(len(tasks)):
        # give x attempts to answer each task
        j = 0
        while j < attempts:
            try:
                answer = int(input(f"{tasks[i][0]} + {tasks[i][1]} = ").strip())
            except ValueError:
                pass
            else:
                # if answer is correct break the loop & save info that we need to add score
                if answer == (tasks[i][0] + tasks[i][1]):
                    add_score = True
                    break
                # print EEE message if answer is wrong
                elif answer != (tasks[i][0] + tasks[i][1]):
                    print("EEE")
                j += 1
            # if user provided correct answer, add 1 score, if not print correct answer
        if "add_score" in locals():
            score += 1
        else:
            print(f"{tasks[i][0]} + {tasks[i][1]} = {tasks[i][2]}")

    # after all tasks print the total score
    print(f"Score: {score}")


def get_level():
    # prompt user for level input (1-3)
    while True:
        try:
            n = int(input("Level: ").strip())
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass
        except EOFError:
            sys.exit()


def generate_integer(level):
    # generate non-negative intiger with level digits or throw ValueError
    if level not in [1, 2, 3]:
        raise ValueError
    if level == 1:
        range = [0, 9]
    if level == 2:
        range = [10, 99]
    if level == 3:
        range = [100, 999]
    x = random.randint(range[0], range[1])
    y = random.randint(range[0], range[1])
    return [x, y]


if __name__ == "__main__":
    main()