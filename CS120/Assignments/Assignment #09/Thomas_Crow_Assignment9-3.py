#   Assignment #9 Question #3
#
#   Thomas Crow
#   Date 10/17/2021
#
#   Requirements:
#
#   Suppose the cost of airmail letters is 30 cents for the first ounce and 25 cents for each additional ounce
#   (less than 1 once will be counted as 1). Write a complete Python program to compute the cost of a letter
#   for a given weight of the letter in ounce. The output sample like the following:
#
#   input  output
#   0.5     30 cents
#   1       30 cents
#   1.1     55 cents
#   2       55 cents
#   2.5     80 cents

import math

##################################################################################################################
#  Description: Determines the shipping cost of air. Prompts user for weight of letter and prints out
#               the cost of shipping.
#  Input: None
#  Output: None

def determineShippingCost():

    whitespace = " "
    print("*" * 100)
    print("*" * 3, whitespace * 92, "*" * 3)
    print("*" * 3, whitespace * 25, "Shipping rates are as follows:", whitespace * 35, "*" * 3)
    print("*" * 3, whitespace * 25, "Airmail: First ounce is 30 cents", whitespace * 33, "*" * 3)
    print("*" * 3, whitespace * 25, "Airmail: Additional ounces are 25 cents per ounce", whitespace * 16, "*" * 3)
    print("*" * 3, whitespace * 92, "*" * 3)
    print("*" * 100)
    print()
    print()
    letterWeight = eval(input("How many ounces is your letter? "))
    roundedLetterWeight = math.ceil(letterWeight)
    print(f"The letter weighs {letterWeight} ounces")
    shippingCost = 0.3 + (0.25 * (roundedLetterWeight - 1))
    print(f"The shipping cost is ${format(shippingCost,'.2f')}")

##################################################################################################################

def main():
    determineShippingCost()

main()
