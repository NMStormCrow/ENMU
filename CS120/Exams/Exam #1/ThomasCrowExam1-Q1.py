#  CS 120 Exam 1 Question #1
#  Thomas Crow

import math

def main():
    print("This program will calculate the sum of n/1 - n/3 + n/5 ... n/x")
    usern = eval(input("Please enter the value for n: "))
    userx = eval(input("Please enter the value for x: "))
    totalsum = 0
    sgn = 1
    for i in range(1, 2 *  userx, 2):
        if (sgn==1):
            totalsum = (totalsum + (usern / userx))
        if (sgn==-1):
            totalsum = (totalsum - (usern / userx))
        sgn = -(sgn)
    print("The sum is equal to: ", totalsum)

main()
