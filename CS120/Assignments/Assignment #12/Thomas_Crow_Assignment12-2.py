#   Assignment #12 Question #2
#
#   Thomas Crow
#   Date 11/14/2021
#
#   Requirements: Suppose you are standing on a very long sidewalk that extends both in front
#                 of and behind you. You flip a coin. If it comes up heads, you take a step
#                 forward; tails means to take a step backward.
#
#                 Suppose you take a walk of n steps. On average, how many steps away from the 
#                 starting point will you end up.
#
#                 Write a program to help you investigate this question. The value of n is 
#                 entered by the user, and you need to print the "result" for each step and
#                 final steps away from the starting point. 

import random

##################################################################################################################
#  Description: Gets value n from user
#  Input: None
#  Output: The value for n

def getN():

    print("Suppose you are standing on a very long sidewalk that extends both in front")
    print("of and behind you. You flip a coin. If it comes up heads, you take a step")
    print("forward; tails means to take a step backward.")
    print("Suppose you take a walk of n steps. On average, how many steps away from the ")
    print("starting point will you end up.")
    print()
    n = eval(input("Please enter the value n: "))

    return n


##################################################################################################################


##################################################################################################################
#  Description: Simulates n coin fips
#               Heads means one step forward
#               Tails means one step back
#               
#  Input:  Number of coin flips
#  Output: None

def simNflips(n):

    stepsFromPoint = 0

    for i in range(n):
        coinflip = random.choice(['Heads','Tails'])
        if (coinflip == "Heads"):
            stepsFromPoint = stepsFromPoint + 1
            print(f"{coinflip}: One step forward.")
        else:
            stepsFromPoint = stepsFromPoint - 1
            print(f"{coinflip}: One step backwards.")
    
    if (stepsFromPoint > 0):
        print(f"After {n} steps, you were {stepsFromPoint} steps forward of the starting point.")
    elif (stepsFromPoint <0):
        print(f"After {n} steps, you were {abs(stepsFromPoint)} steps behind of the starting point.")
    else:        
        print(f"After {n} steps, you were on the starting point.")


##################################################################################################################

def main():
       
       nsteps = getN()
       simNflips(nsteps)

main()
