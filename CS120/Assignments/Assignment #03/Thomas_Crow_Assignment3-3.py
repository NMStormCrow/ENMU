# Assignment #3 Question #2
#
# Thomas Crow
# Date 9/05/2021
#
# Requirements:
# Write a program that finds the average of a series of numbers entered by the user.
#
#
#
# Inputs:
# user_num = Number entered from user
#
#
# Outputs:
# user_average = The average of all the numbers given by user
#
#  Note for instructor:
#  To add a challenge to this assignment and help me learn more about Python, I decided to write the program that
#  calcuates the average number without prompting needing the user for the number of entries that will be entered.
#
#  I used Python's while loop, the try/except, and join commands and a list to accomplish this.
#
#  I have used input validation to prevent invalid user inputs to cause error to the program or the calculations
#
#

import math

def main():

#   Statement of program's purpose
    print("#################################################################################")
    print("## This program determines the average of a series of numbers entered entered. ##")
    print("## It will accept valid numbers, and discard invalid entries.                  ##")
    print("## The sum of the valid numbers will be divided by the number of valid entries ##")
    print("#################################################################################")
    print()

#   Initialize variables
    user_sum = 0
    valid_numbers = 0
    user_num = 0
    user_num_stack = []
    invalid_entry_stack = []

#   Input loop to obtain numbers from user_num
#   user_num is obtained from user as a string
#   It first is attempted to be converted to an integer.
#   If that fails, it is attempted to be converted to a floating point numbers
#   If that also fails, it is attepted to be converted to a string.
#   If tht works, it is checked it it equals the exit value.  If it is, the loop is broken using the break command.
#   If none of this applies, the user is given a invalid input error and the loop reloads.
#   Exit condition: the character q, regardless of case

    while True:
        user_num = input("Please enter a number.  Enter q to quit: ") #This stores the user input initally as a string
        try:
            val = int(user_num) # This tries to convert the string value to an int.  If it fails, the error will be caught by the except command
            user_sum += val
            valid_numbers += 1
            user_num_stack.append(user_num)
        except ValueError:
            try:
                val = float(user_num) # This tries to convert the string value to a float.  If it fails, the error will be caught by the except command
                user_sum += val
                valid_numbers += 1
                user_num_stack.append(user_num)
            except ValueError:
                try:
                    val = str(user_num) # This tries to convert the string value to a string.  If it fails, the error will be caught by the except command
                    if val.lower() == 'q': # This will allow the program to accept q regardless of case to exit the program
                        break
                    else:
                        invalid_entry_stack.append(user_num)
                        print("Invalid Entry:  Please enter a valid number or q to exit.")  # Gives user error message
                except ValueError:
                    invalid_entry_stack.append(user_num)
                    print("Please enter a valid number or q to exit.") #Gives user error message

#   The part where we make the computer do all the work
    if valid_numbers > 0: #This applies if there are any items in the list user_num_stack
        average_value = (user_sum / valid_numbers)
        all_numbers_entered = ", ".join(user_num_stack) #Prints the contents of the list user_num_stack
        all_invalid_entries_entered = ", ".join(invalid_entry_stack) #Prints the contents of the list invalid_entry_stack
#   Print values to user
        print()
        print("#################################################################################")

        if len(invalid_entry_stack) > 0:  #This applies if there are any items in the list invalid_entry_stack
            print(f"The invalid entries were: {all_invalid_entries_entered}")
        print(f"The numbers entered were: {all_numbers_entered}")
        print(f"The number of valid numbers entered was: {valid_numbers}")
        print(f"The average value of the numbers entered, rounded to two decimal places, is: {format(average_value, '0.2f')}")
        print("#################################################################################")
        print()

    else:
        all_invalid_entries_entered = ", ".join(invalid_entry_stack)
        print()
        print("#################################################################################")
        if len(invalid_entry_stack) > 0: #This applies if there are any items in the list invalid_entry_stack
            print(f"The invalid entries were: {all_invalid_entries_entered}") #Prints the contents of the list invalid_entry_stack
        print(f"No valid numbers were entered. Please rerun program and enter valid numbers.")
        print("#################################################################################")

        
main()
