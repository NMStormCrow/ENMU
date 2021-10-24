#   Assignment #10 Question #1
#
#   Thomas Crow
#   Date 10/23/2021
#
#   Requirements: The body mass index (BMI) is calculated as a person's weight (in pounds) times 720, divided by the square of the person's 
#                 height (in inches). A BMI in the range 19-25, inclusive, is considered healthy. Write a program that calculates a person's BMI
#                 and prints a message telling whether they are above, within, or below the healthy range.
#
#   


##################################################################################################################
#  Description: Calculates the BMI by requesting the user's weight and height, and prints to user the
#               calulated BMI and if it is within the established healthy range.
#
#  Input: None
#  Output: None

##################################################################################################################

def calculateBMI():
    
    print("This program calculates body mass index (BMI)") 
    userWeight = eval(input("Please enter your weight in pounds: "))
    userHeight = eval(input("Please enter your height in inches: "))
    userBMI = (userWeight  * 720) / (userHeight ** 2)
    print(f"The calculated BMI is: {round(userBMI,2)}")

    if (userBMI < 19):
        print("This BMI is considered below the healthy range.")
    elif (userBMI > 25):
        print("This BMI is considered above the healthy range.")
    else:
        print("This BMI is considered to be within the healthy range.")


def main():
    calculateBMI()

main()
