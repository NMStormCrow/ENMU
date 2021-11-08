#   Assignment #11 Question #3
#
#   Thomas Crow
#   Date 10/30/2021
#
#   Requirements: The greatest common divisor (GCD) of two values can be computed using Euclid's algorithm.
#   Starting with the values m and n, we repeatedly apply the formula: n, m = m, n % m until m is 0.   
#   At that point, n is the GCD of the original m and n.
#   Write a program that finds the GCD of two numbers using this algorithm.
#

##################################################################################################################
#  Description: Obtains two numbers from user, determines if that are valid
#  Input: None
#  Output: Boolean value if numbers are valid
#          Integer values of the two user numbers

def obtainValidNumbers():
    userNumM = eval(input("Please enter the first non-negative integer: "))
#   Check to see if number is positive
    if (userNumM < 0):
        print(f"{userNumM} is negative number.")
        return False, userNumM, 0
#   If a float is entered:
#   If the float a whole number, convert to int 
#   Otherwise print that the number is not a whole number
    if isinstance(userNumM, float):
        if (userNumM.is_integer()):
            userNumM = int(userNumM)
        else:
            print(f"{userNumM} is not a whole number.")
            return False, userNumM, 0
    userNumN = eval(input("Please enter the second non-negative integer: "))
#   Check to see if number is positive
    if (userNumN < 0):
        print(f"{userNumN} is negative number.")
        return False, userNumM, userNumN
#   If a float is entered:
#   If the float a whole number, convert to int 
#   Otherwise print that the number is not a whole number
    if isinstance(userNumN, float):
        if (userNumN.is_integer()):
            userNumN = int(userNumN)
        else:
            print(f"{userNumN} is not a whole number.")
            return False, userNumM, userNumN
#   If both numbers are valid integers return True
    return True, userNumM, userNumN 
##################################################################################################################

##################################################################################################################
#  Description: Applies the Euclidian Algorithm to find the greatest common divisor of two passed values  
#  Input: Two integer valiues
#  Output: The GCD integer value

def gcdByEuclidian(m,n):

    gcdValue = n
    if m == 0:
        return gcdValue
    while (n != 0):
        gcdValue = n
        n = m % n
        m = gcdValue
    return gcdValue

##################################################################################################################

def main():

    numbersAreValid = False
    while (numbersAreValid == False):
        numbersAreValid, numberM, numberN = obtainValidNumbers()
    userGCD = gcdByEuclidian(numberM, numberN)
    print(f"The GCD of {numberM} and {numberN} is {userGCD}.")

main()
