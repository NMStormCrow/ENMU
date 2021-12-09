#  CS 120 Final Question #1
#  Thomas Crow

# 


def determineWinner(n):
    
    playerLost = []
    playersLeft = n
    w = 1
    playerLostBool = False

    for i in range(n):
        playerLost.append(False)
    
    while (playersLeft > 1):
        for j in range(n):
            if playerLost[j] == False:
                for k in range((j+1), n):
                    if (playerLost[k] == False):
                        print(f"Player {k+1} lost!")
                        playerLost[k] = True
                        playersLeft = playersLeft - 1
                        w = (j+1)
                        playerLostBool = True
                if playerLostBool == True:
                    for l in range(j-1):
                        print(f"Player {l+1} lost!")
                        playerLost[l] = True
                        playersLeft = playersLeft - 1
                        w = (j+1)
                playerLostBool = False

    return w

def main():
    print(f"This game is called the Halloween Elimination Game")
    numPlayers = eval(input("How many players are there? "))
    winner = determineWinner(numPlayers)
    print(f"This winner is player {winner}.")
    



main()