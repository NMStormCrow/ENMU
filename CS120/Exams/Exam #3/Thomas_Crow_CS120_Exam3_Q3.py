#  CS 120 Exam 3 Question #2
#  Thomas Crow

# Design and implement a simulation of the game of volleyball. Normal volleyball is played 
# like racquetball in that a team can only score points when it is serving. Games are played 
# to 15, but must be won by at least two points. 
# Note: the probability of the team A wins a serve is 45% and the probability of the team 
# B wins a serve is 55%. You need to print out the detailed results of each five consecutive 
# games of team A and B, like: 13:15, 7:15, 17:19,15:10,15:13. 

from random import random

def simNGames(n, probA, probB):    
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        print(f"The score for game {(i+1)} was: {scoreA}:{scoreB}")
    
def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
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

def gameOver(a, b):
    return (a>=15 and (a-b >= 2)) or (b>=15 and (b-a >=2))

def main():
    simNGames(5,.45,.55)

main()