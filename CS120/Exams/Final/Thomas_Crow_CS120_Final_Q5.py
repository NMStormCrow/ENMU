#  CS 120 Final Question #5
#  Thomas Crow

#  Write a Python function “myRandom” that randomly generates an integer. The function must accept ONE small integer inputs and return ONE integer. 
#  The input defines the number of digits of the random number. For example, if the input is integer “3”, the output should #  be a 3 digits integer like “321”.
#  Write another Python function “myLeap” to determine if a given year is leap or not. Assume the year is 1900 or later. The input should be a 4 digit integer and the output should be a Boolean value.
#  Write a main function to generate a year between 1900 to 2021, and determine this year is leap or not. The main function should call the previous two functions, “myRondom” and “myLeap”.

import random

    
def myRandom(digits):

    randNum = 0

    for i in range (digits):
        number = (random.randint(0,9) * (10 ** i))
        randNum = randNum + number

    return randNum

def determineIfLeapYear(randomyear):

    if ((randomyear % 4) == 0):
        if ((randomyear % 100) == 0):
            if ((randomyear% 400) == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    

    yearGood = False

    numDigits = eval(input("Please enter the number of digits for a random number:"))
    while (yearGood == False):
        randomNumber = myRandom(numDigits)
        if (randomNumber > 1900) and (randomNumber < 2021):
            yearGood = True

    
    isLeapYear = determineIfLeapYear(randomNumber)

    if (isLeapYear == True):
        print(f"The year {randomNumber} is a leap year.")
    else:
        print(f"The year {randomNumber} is not a leap year.")



main()