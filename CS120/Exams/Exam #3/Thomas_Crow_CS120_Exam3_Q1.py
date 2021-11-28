#  CS 120 Exam 3 Question #1
#  Thomas Crow

# Write a program that uses a while loop to determine how long it takes for an investment 
# to double at a given interest rate. The input will be an annualized interest rate, and the 
# output is the number of years it takes an investment to double.  

def getInput():
    userInput = float(input("Please enter the percentage of the annualized interest rate: "))/100
    return userInput

def calculateDoubleInvestment(air):
    dummyInvestment = 1000
    numYears = 0

    while(dummyInvestment < 2000):
        dummyInvestment = dummyInvestment + (dummyInvestment * air)
        numYears = numYears + 1
    
    print(f"The investment will double the investment in {numYears} years.")

    


def main():
    air = getInput()
    calculateDoubleInvestment(air)



main()