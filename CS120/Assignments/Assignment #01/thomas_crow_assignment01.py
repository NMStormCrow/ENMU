#  File: chaos.py
#  Thomas Crow
#  CS 120
#  Assignment #1
#  8-21-2021

# Inputs
# x is the first input from the user to be applied by the chaotic function
# y is the second input from the user to be applied by the chaotic function
# user_range is the third input from the user which specifies the number of times to run the chaotic function

# Student note: I'm unsure of the exact program requirements.  I have made this program run the chaotic function twice.
# The first time I am having the function print out a static value of 20 times.  I am using the the value 2.0 in the function in place of 3.  This is to meet the requirements
# of part one of the assignment
# The second time I have the user specify the number of times the function prints out. I am also using the original value of 3 to illustrate the difference in output.
# This is to meet the the second part of the assignment.


def main():

# Print to user the purpose of this program
    print("This program illustrates a chaotic function, first using two and second three")

# Define the value for the variable x
    x = eval(input("Please enter the first number between 0 and 1: "))

# Define the value for the variable y
    y = eval(input("Please enter the second number between 0 and 1: "))

# Print to user the number of times the first function will run
    print("The first function will run a predefined twenty times ")

# For loop runs 20 times, first updating then printing the value of x
    for i in range(20):
        x = 2.0 * x * (1 - x)
        print(x)

# Define the value of user_range, which determines the number of times the for loop runs
    user_range = eval(input("Please enter the number of times for the second function to run the function: "))

# For loop runs the value of user_range times, first updating then printing the value of y
    for j in range(user_range):
        y = 3 * y * (1 - y)
        print(y)

main()
