#  CS 120 Final Question #2
#  Thomas Crow

# 

def determineTwoPowers(num1, num2):
    
    isPowerTwo = False
    powersOfTwo = []
    power = 0
    secondpowernumber = 1

    if (num1 < num2):
        smallerNumber = num1
        largerNumber = num2
    else:
        smallerNumber = num2
        largerNumber = num1
    
    while (secondpowernumber < largerNumber):
        secondpowernumber = 2 ** power
        for i in range (smallerNumber, largerNumber):
            if (i == secondpowernumber):
                isPowerTwo = True
                powersOfTwo.append(secondpowernumber) 
        power = power + 1
    
    return isPowerTwo, powersOfTwo







def main():
    print(f"This program determines if a power of two is between to inputted numbers.")
    number1 = eval(input("Please enter the first number: "))
    number2 = eval(input("Please enter the second number: "))
    is2ndpower, powersoftwo = determineTwoPowers(number1,number2)

    if (is2ndpower == True):
        print(f"The powers of two between {number1} and {number2} is:")
        print(powersoftwo)
    else:
        print(f"There were no powers of two between {number1} and {number2}.")



main()