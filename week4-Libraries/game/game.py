# CS50p Problem Set 4: Guessing Game
# https://cs50.harvard.edu/python/2022/psets/4/game/
#
# Goal: user inputs some positive intiger n, program draws a random number between 1 and n, user tries to guess it
# Author: Adam Labedzki 2023-01-11

import sys
from random import randint


def main():
    # ask user for n level input (positive intiger) loop until correct value
    while True:
        try:
            n = input("Level: ").strip()
            if int(n) > 0:
                n = int(n)
                break
        except EOFError:
            break
        except:
            pass

    # draw target intiger from 1-n range
    target = randint(1, n)

    # ask user for a guess for target value, loop until he nails it
    while True:
        try:
            guess = input("Guess: ").strip()
            if int(guess) > 0:
                # when positive int is entered, check the results
                result = check(guess, target)
                # if it is a miss, print guiding msg
                if result[0] == 0:
                    print(result[1])
                # if it is a hit, print message and break the loop
                elif result[0] == 1:
                    print(result[1])
                    break
        except EOFError:
            break
        except:
            pass

    sys.exit()


# check if guess is a miss or hit, return result value and message to the user
def check(guess, target):
    if int(guess) > target:
        result = 0
        msg = "Too large!"
    elif int(guess) < target:
        result = 0
        msg = "Too small!"
    else:
        result = 1
        msg = "Just right!"
    return [result, msg]


if __name__ == "__main__":
    main()