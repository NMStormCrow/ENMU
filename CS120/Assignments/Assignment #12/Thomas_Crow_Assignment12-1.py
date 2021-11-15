#   Assignment #12 Question #1
#
#   Thomas Crow
#   Date 11/14/2021
#
#   Requirements: Revise the racquetball simulation to take shutouts into account. Your updated version should
#                 report for both players the number of wins, percentage of wins, number of shutouts,
#                 and percentage of wins that are shutouts

from random import random

##################################################################################################################
#  Description: Prints description of program
#  Input: None
#  Output:  None

def printlntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

##################################################################################################################

##################################################################################################################
#  Description: Obtains program values from user
#  Input: None
#  Output: Returns the three simulation parameters

def getlnputs():
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

##################################################################################################################

##################################################################################################################
#  Description: Simulates n games of racquetball between players whose
#               abilities are represented by the probability of winning a serve.
#               
#  Input: Number of games, probability of serve wins by A and B
#  Output: Returns number of wins for A and B

def simNGames(n, probA, probB):

    winsA = winsB = shutA = shutB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
        if shutA == 0:
            shutA = shutA + 1
        elif shutB == 0:
            shutB = shutB + 1 
    return winsA, winsB, shutA, shutB

##################################################################################################################

##################################################################################################################
#  Description: Simulates a single game or racquetball between players whose
#               abilities are represented by the probability of winning a serve.
#               
#  Input: Probability of winning a serve for each player
#  Output: Returns final scores for A and B

def simOneGame(probA, probB):

    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A" :
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

##################################################################################################################

##################################################################################################################
#  Description: Returns boolean value true if either score equals 15
#               
#               
#  Input: a and b represent scores for a racquetball game
#  Output: Returns True if the game is over, False otherwise.
#          
def gameOver(a, b):
    return a==15 or b==15

##################################################################################################################

##################################################################################################################
#  Description: Prints a summary of wins for each player.
#               
#               
#  Input: Number of wins for each player
#  Output: None

def printSummary(winsA, winsB, soutsA, soutsB):
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winsA, winsA/n))
    print("The number of shutouts for A: {0} ({1: 0.1%})".format(soutsA, soutsA/winsA))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB, winsB/n))
    print("The number of shutouts for B: {0} ({1: 0.1%})".format(soutsB, soutsB/winsB))
##################################################################################################################


def main():
    printlntro()
    probA, probB, n = getlnputs()
    winsA, winsB, shutoutsA, shutoutsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, shutoutsA, shutoutsB)
    


main()
