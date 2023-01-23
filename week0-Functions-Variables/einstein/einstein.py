# CS50p Problem Set 0: Einstein
# https://cs50.harvard.edu/python/2022/psets/0/einstein/
#
# Goal: prompt the user for mass as an integer (in kilograms) and then output the equivalent number of Joules as an integer. Assume that the user will input an integer.
# Author: Adam Labedzki 2023-01-04

c = 300000000
m = int(input("Please enter mass in kg: "))
e = m*c*c
print(e)
#print(f"{e:,}") # nicer large numbers formatting with 000 separator