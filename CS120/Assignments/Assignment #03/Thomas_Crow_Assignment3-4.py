# Assignment #3 Question #2
#
# Thomas Crow
# Date 9/05/2021
#
# Requirements:
# Write a program that finds the sum of cubes of the first n natural numbers where the value of n
# is provided by the user
#
# Inputs:
# user_n -- Value of provided by the user
#
#
# Outputs:
# sum_of_cubes -- The sum of the cubes
#
#  Note for instructor:
#  I implemented input validation for the value n.  To run the loop, the value of n must be an integer with a value
#  greater than or equal to 0
#

import math

def main():

#   Statement of program's purpose
    print("#################################################################################################################################################")
    str_user_n = input("Please enter the value n, a postive integer value, for the number of natural numbers from zero that will have their cubes summed: ")
    print("#################################################################################################################################################")
    print()

#   Initial variables
    sum_of_cubes = 0


#   Make the computer do all the work
    try:
        int_user_n = int(str_user_n)
        if (int_user_n) >= 0:
            for i in range(1,int_user_n + 1):
                sum_of_cubes += (i ** 3)
#   Print output to user
            print(f"The value of these natural numbers cubed from 0 to {int_user_n} is: {sum_of_cubes}")
        else:
#   Print that numbers must be positive to user
            print(f"The value {int_user_n} is not valid. The value cannot be negative. Please run the program again and enter a valid positive integer.")
    except ValueError:
        try:
            float_user_n = float(str_user_n)
#   Print that numbers cannot be floating point to user
            print(f"The value {float_user_n} cannot be a floating point number. Please run the program again and enter a valid integer.")
        except ValueError:
#   Print catch-all error message to user
            print(f"The value \"{str_user_n}\" is not valid.  Please run the program again and enter a valid integer.")


main()
