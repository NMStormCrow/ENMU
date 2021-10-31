# Assignment #8 Question #2
#
# Thomas Crow
# Date 10/10/2021
#
#   Requirements:
#
#   Write definitions for the following two functions:
#
#   sumN (n) returns the sum of the first n natural numbers.
#
#   sumNCubes (n) returns the sum of the cubes of the first n natural numbers.
#
#   Then use these functions in a program that prompts a user for an n and prints out the sum of the first n natural numbers
#   and the sum of the cubes of the first n natural numbers.
#
#   This assumes that 0 is the first natural number.


##################################################################################################################
#  Prompts user for the value n and returns this value
#  Input: None
#  Output: The value of n

def get_nth_number():

    whitespace=" "

    print("*" * 93)
    print("***", whitespace*85, "***")
    print("***", whitespace * 25, "This program returns the sum of:", whitespace * 26, "***")
    print("***", whitespace * 25, "The first n natural numbers.", whitespace * 30, "***")
    print("***", whitespace * 25, "The sum of the cubes of the first n natural numbers.", whitespace * 6, "***")
    print("***", whitespace*85,"***")
    print("*" * 93)
    print()

    nth_number=eval(input("Please enter the value n you wish to calculate: "))

    return (nth_number)
##################################################################################################################

##################################################################################################################
#  Prints the sum of the first n natural numbers
#  Input: The value of n
#  Output: None

def print_sum_of_natural_numbers(nth_number):

    sum = 0
    for i in range(nth_number):
        sum = sum + i

    print(f"The sum of the first natural numbers to the value of n {nth_number} is {sum}.")

##################################################################################################################

##################################################################################################################
#  Prints the sum of the cubes of the first n natural numbers
#  Input: The value of n
#  Output: None

def print_sum_of_cubes_of_natural_numbers(nth_number):

    sum = 0
    for i in range(nth_number):
        sum = sum + i**3

    print(f"The sum of the cubed values of first natural numbers to the value of n {nth_number} is {sum}.")

##################################################################################################################

##################################################################################################################
def main():

    n = get_nth_number()
    print()
    print_sum_of_natural_numbers(n)
    print_sum_of_cubes_of_natural_numbers(n)
    print()

##################################################################################################################

main()
