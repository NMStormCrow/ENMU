#   Assignment #11 Question #1
#
#   Thomas Crow
#   Date 10/30/2021
#
#   Requirements:
#   The Goldbach conjecture asserts that every even number is the sum of two prime numbers.
#   Write a program that gets a number from the user, checks to make sure that it is even,
#   and then finds two prime numbers that add up to the number
#
#   Note to instructor: Though not explicitly stated in the assignment, the above math statement applies to even
#   numbers greater than two. This code assumes that the number entered by the user must be a even whole number greater 
#   than two.
   

##################################################################################################################
#  Description: Determines if passed value is a prime number 
#  Input: Integer Value
#  Output: Boolean value of whether number is prime

def isNumPrime(value):
#   Assuming standard definition that 1 is not a prime number
    if (value < 2):
        return False
    for i in range(2, value):
        if ((value % i) == 0):
            return False
    return True
##################################################################################################################


##################################################################################################################
#  Description: Obtains number from user, determines if a valid number to test Goldbach conjecture
#  Input: None
#  Output: Boolean value if number is valid
#          User entered number
def obtainValidNumber():
    userNum = eval(input("Please enter a even whole number greater than two: "))
#   If a float is entered:
#   If the float a whole number, convert to int 
#   Otherwise print that the number is not a whole number
    if isinstance(userNum, float):
        if (userNum.is_integer()):
            userNum = int(userNum)
        else:
            print(f"{userNum} is not a whole number.")
            return False, userNum
#   Checks for the number being greater than 2
    if (userNum <= 2):
        print("The number needs to be greater than 2.")
        return False, userNum
#   Checks for number being even.
    if (userNum % 2 != 0) :
        print("The number must be even.")
        return False, userNum
    
#   If number is a valid even whole number greater than 2, return True
    return True, userNum 
##################################################################################################################

##################################################################################################################
#  Description: Finds two prime numbers of whose sum equal the user inputted value
#  Input: Integer Value of user inputted number
#  Output: Integer values of the two numbers

def findPrimeAddends(value):
    for i in range(2, value):
        if (isNumPrime(i)):
            for j in range(2, value):
                if (isNumPrime(j)):
                    if ((i + j) == value):
                        return i, j

##################################################################################################################


def main():

    numberValid = False
    print("Given an even number greater than two inputted by the user, this program finds two prime numbers which have a sum equal to the number.")
    while (numberValid == False):
        numberValid, userNumber = obtainValidNumber()
    firstPrimeAddend, secondPrimeAddend = findPrimeAddends(userNumber)
    print(f"Prime addends for the entered number {userNumber} is {firstPrimeAddend} and {secondPrimeAddend}.")

main()
