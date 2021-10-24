#   Assignment #10 Question #2
#
#   Thomas Crow
#   Date 10/23/2021
#
#   Requirements: A person is eligible to be a US senator if they are at least 30 years old and have been a US citizen for at least 9 years. To be a 
#                 US representative these numbers are 25 and 7, respectively. Write a program that accepts a person's age and years of 
#                 citizenship as input and outputs their eligibility for the Senate and House.
#
#   

##################################################################################################################
#  Description: Determined by user inputed age and length of US citizenship whether the user could serve
#               in the US House of Representatives or the US Senate.
#
#  Input: None
#  Output: None

def determineElgibility():

    print("This program determines whether one can serve in the US House of Representatives and the US Senate.")
    userAge = eval(input("Please enter your age: "))
    userTimeOfCitizenship = eval(input("Please enter how many years you have been a US Citizen: "))

    if (userAge < 25):
        print("You cannot serve in either the US House of Representatives or the US Senate.")
    elif (userAge < 30):
        if (userTimeOfCitizenship < 7):
            print("You cannot serve in either the US House of Representatives or the US Senate.")
        else:
            print("You can serve in the US House of Representatives but not the US Senate.")
    else:
        if (userTimeOfCitizenship < 7):
            print("You cannot serve in either the US House of Representatives or the US Senate.")
        elif (userTimeOfCitizenship < 9):
            print("You can serve in the US House of Representatives but not the US Senate.")
        else:
            print("You can serve in either the US House of Representatives or the US Senate.")

##################################################################################################################


def main():
    determineElgibility()


main()
